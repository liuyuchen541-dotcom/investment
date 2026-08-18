from contextlib import redirect_stderr, redirect_stdout
from datetime import date
import io

from . import index_symbols


class EmptyDataError(RuntimeError):
    """AKShare 接口没有返回可写入数据。"""


class PendingSymbolError(RuntimeError):
    """关注标的代码口径还没确认，不能写入行情。"""


def _load_akshare():
    try:
        import akshare as ak
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "未安装 AKShare。请先运行：pip install -r requirements.txt"
        ) from exc
    return ak


def describe_error(exc):
    text = str(exc)
    cause = getattr(exc, "__cause__", None)
    cause_text = str(cause) if cause else ""
    joined = f"{text} {cause_text}"
    if isinstance(exc, PendingSymbolError) or "代码待确认" in joined:
        return f"代码待确认：{text}"
    if isinstance(exc, ModuleNotFoundError) or "No module named 'akshare'" in joined:
        return "未安装 AKShare。请先运行：pip install -r requirements.txt"
    if "未安装 AKShare" in joined:
        return "未安装 AKShare。请先运行：pip install -r requirements.txt"
    if isinstance(exc, EmptyDataError) or "暂无数据" in joined or "empty" in joined.lower():
        return f"接口暂无数据/待确认：{text}"
    field_markers = ["字段缺失", "返回字段", "KeyError"]
    if any(marker in joined for marker in field_markers):
        return f"AKShare 接口字段变化：{text}"
    network_markers = [
        "SSL",
        "HTTPSConnectionPool",
        "Connection",
        "Timeout",
        "timed out",
        "RemoteDisconnected",
        "ProxyError",
        "Max retries exceeded",
        "UNEXPECTED_EOF",
    ]
    if any(marker in joined for marker in network_markers):
        return f"网络或接口连接失败：{text}"
    return f"更新失败：{text}"


def fetch_stock_daily(symbol, start_date, end_date=None):
    ak = _load_akshare()
    end = end_date or date.today().strftime("%Y%m%d")
    df = _quiet_call(
        ak.stock_zh_a_hist,
        symbol=symbol,
        period="daily",
        start_date=start_date,
        end_date=end,
        adjust="qfq",
    )
    if df is None or df.empty:
        raise EmptyDataError(f"stock_zh_a_hist 未返回 {symbol} 的数据")
    required = ["日期", "开盘", "最高", "最低", "收盘", "成交量", "成交额"]
    _ensure_columns(df, required, "stock_zh_a_hist")
    rows = []
    for _, row in df.iterrows():
        rows.append(
            {
                "symbol": symbol,
                "trade_date": _date_text(row["日期"]),
                "open": _to_float(row["开盘"]),
                "high": _to_float(row["最高"]),
                "low": _to_float(row["最低"]),
                "close": _to_float(row["收盘"]),
                "volume": _to_float(row["成交量"]),
                "amount": _to_float(row["成交额"]),
                "adjust_type": "qfq",
            }
        )
    return [row for row in rows if row["trade_date"]]


def fetch_index_daily(symbol, start_date, end_date=None):
    ak = _load_akshare()
    end = end_date or date.today().strftime("%Y%m%d")
    resolved = index_symbols.resolve_index_symbol(symbol)
    if index_symbols.is_pending_symbol(symbol):
        raise PendingSymbolError(f"{symbol} 代码待确认，{resolved.note}")

    if resolved.interface == "index_zh_a_hist":
        df = _quiet_call(
            ak.index_zh_a_hist,
            symbol=resolved.query_symbol,
            period="daily",
            start_date=start_date,
            end_date=end,
        )
        return _rows_from_cn_index(df, symbol, resolved.interface)

    if resolved.interface == "stock_hk_index_daily_sina":
        df = _quiet_call(ak.stock_hk_index_daily_sina, symbol=resolved.query_symbol)
        return _rows_from_hk_index(df, symbol, start_date, end)

    try:
        df = _quiet_call(
            ak.stock_zh_index_daily_tx,
            symbol=resolved.query_symbol,
            start_date=start_date,
            end_date=end,
        )
    except TypeError:
        df = _quiet_call(ak.stock_zh_index_daily_tx, symbol=resolved.query_symbol)
    if df is None or df.empty:
        raise EmptyDataError(f"stock_zh_index_daily_tx 未返回 {symbol} 的数据")
    required = ["date", "open", "close", "high", "low"]
    _ensure_columns(df, required, "stock_zh_index_daily_tx")
    rows = []
    for _, row in df.iterrows():
        rows.append(
            {
                "symbol": symbol,
                "trade_date": _date_text(row["date"]),
                "open": _to_float(row["open"]),
                "high": _to_float(row["high"]),
                "low": _to_float(row["low"]),
                "close": _to_float(row["close"]),
                "volume": _to_float(row.get("volume")),
                "amount": _to_float(row.get("amount")),
                "adjust_type": "none",
            }
        )
    return [row for row in rows if row["trade_date"]]


def fetch_fund_nav(fund_code, start_date=None, end_date=None):
    ak = _load_akshare()
    df = _quiet_call(
        ak.fund_open_fund_info_em,
        symbol=fund_code,
        indicator="单位净值走势",
    )
    if df is None or df.empty:
        raise EmptyDataError(f"fund_open_fund_info_em 未返回 {fund_code} 的数据")
    date_col = _first_existing_column(df, ["净值日期", "日期", "FSRQ"])
    unit_col = _first_existing_column(df, ["单位净值", "DWJZ", "净值"])
    acc_col = _first_existing_column(df, ["累计净值", "LJJZ", "LJZ"], required=False)
    return_col = _first_existing_column(
        df, ["日增长率", "涨跌幅", "增长率", "JZZZL"], required=False
    )
    rows = []
    for _, row in df.iterrows():
        nav_date = _date_text(row[date_col])
        if start_date and nav_date and nav_date.replace("-", "") < start_date:
            continue
        if end_date and nav_date and nav_date.replace("-", "") > end_date:
            continue
        rows.append(
            {
                "fund_code": fund_code,
                "nav_date": nav_date,
                "unit_nav": _to_float(row[unit_col]),
                "accumulated_nav": _to_float(row[acc_col]) if acc_col else None,
                "daily_return": _to_float(row[return_col]) if return_col else None,
            }
        )
    rows = [row for row in rows if row["nav_date"] and row["unit_nav"] is not None]
    rows.sort(key=lambda item: item["nav_date"])
    _fill_missing_daily_return(rows)
    if not rows:
        raise EmptyDataError(f"fund_open_fund_info_em 没有可写入的 {fund_code} 净值数据")
    return rows


def _rows_from_cn_index(df, symbol, interface_name):
    if df is None or df.empty:
        raise EmptyDataError(f"{interface_name} 未返回 {symbol} 的数据")
    required = ["日期", "开盘", "收盘", "最高", "最低", "成交量", "成交额"]
    _ensure_columns(df, required, interface_name)
    rows = []
    for _, row in df.iterrows():
        rows.append(
            {
                "symbol": symbol,
                "trade_date": _date_text(row["日期"]),
                "open": _to_float(row["开盘"]),
                "high": _to_float(row["最高"]),
                "low": _to_float(row["最低"]),
                "close": _to_float(row["收盘"]),
                "volume": _to_float(row["成交量"]),
                "amount": _to_float(row["成交额"]),
                "adjust_type": "none",
            }
        )
    return [row for row in rows if row["trade_date"]]


def _rows_from_hk_index(df, symbol, start_date, end_date):
    interface_name = "stock_hk_index_daily_sina"
    if df is None or df.empty:
        raise EmptyDataError(f"{interface_name} 未返回 {symbol} 的数据")
    required = ["date", "open", "high", "low", "close"]
    _ensure_columns(df, required, interface_name)
    rows = []
    for _, row in df.iterrows():
        trade_date = _date_text(row["date"])
        compact_date = trade_date.replace("-", "") if trade_date else ""
        if start_date and compact_date < start_date:
            continue
        if end_date and compact_date > end_date:
            continue
        rows.append(
            {
                "symbol": symbol,
                "trade_date": trade_date,
                "open": _to_float(row["open"]),
                "high": _to_float(row["high"]),
                "low": _to_float(row["low"]),
                "close": _to_float(row["close"]),
                "volume": _to_float(row.get("volume")),
                "amount": _to_float(row.get("amount")),
                "adjust_type": "none",
            }
        )
    rows = [row for row in rows if row["trade_date"]]
    if not rows:
        raise EmptyDataError(f"{interface_name} 没有可写入的 {symbol} 数据")
    return rows


def _fill_missing_daily_return(rows):
    previous_nav = None
    for row in rows:
        if row["daily_return"] is None and previous_nav not in (None, 0):
            row["daily_return"] = round(
                (row["unit_nav"] - previous_nav) / previous_nav * 100, 4
            )
        previous_nav = row["unit_nav"]


def _quiet_call(func, *args, **kwargs):
    buffer = io.StringIO()
    with redirect_stdout(buffer), redirect_stderr(buffer):
        return func(*args, **kwargs)


def _ensure_columns(df, columns, interface_name):
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise ValueError(
            f"{interface_name} 返回字段缺失：{missing}；当前字段：{list(df.columns)}；为避免写入错误含义，已停止该标的更新"
        )


def _first_existing_column(df, candidates, required=True):
    for col in candidates:
        if col in df.columns:
            return col
    if required:
        raise ValueError(
            f"基金接口返回字段缺失：{candidates}；当前字段：{list(df.columns)}；为避免写入错误含义，已停止该基金更新"
        )
    return None


def _to_float(value):
    if value in (None, "", "-"):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _date_text(value):
    if value is None:
        return None
    if isinstance(value, (int, float)) and value > 100000000000:
        return date.fromtimestamp(value / 1000).strftime("%Y-%m-%d")
    if hasattr(value, "strftime"):
        return value.strftime("%Y-%m-%d")
    return str(value)[:10]
