from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from . import config, db, index_symbols


INIT_HINT = "文件账本不存在。请先运行：python scripts/init_db.py"
UPDATE_HINT = "暂无可展示数据。请先运行：python scripts/update_daily.py"


@dataclass
class DashboardResult:
    data: object
    ok: bool = True
    message: str = ""


def _root(db_path=None):
    path = Path(db_path or config.DATA_DIR)
    if path.suffix.lower() == ".db":
        path = path.parent
    return path


def _ensure_ledger_exists(db_path=None):
    root = _root(db_path)
    if not (root / "ledger" / "watchlist.csv").exists():
        raise FileNotFoundError(INIT_HINT)
    return root


def _safe_read(default, reader):
    try:
        return DashboardResult(reader())
    except FileNotFoundError as exc:
        return DashboardResult(default, ok=False, message=str(exc))
    except Exception as exc:
        return DashboardResult(default, ok=False, message=f"读取文件账本失败：{exc}")


def get_table_counts(db_path=None):
    def reader():
        root = _ensure_ledger_exists(db_path)
        return {
            "watchlist": len(db.fetch_watchlist(root)),
            "fund_nav": len(db.read_fund_nav_frame(root)),
            "stock_daily": len(db.read_stock_daily_frame(root)),
            "portfolio_holding": len(db.fetch_holdings(root)),
            "trade_record": len(db.fetch_trades(root)),
            "update_log": len(db.fetch_recent_logs(root, limit=1000000)),
        }

    return _safe_read({}, reader)


def load_watchlist(db_path=None, asset_types=None):
    wanted = set(asset_types or [])

    def reader():
        root = _ensure_ledger_exists(db_path)
        rows = db.fetch_watchlist(root)
        if wanted:
            rows = [row for row in rows if row.get("asset_type") in wanted]
        rows.sort(key=lambda row: (row.get("asset_type", ""), -int(row.get("enabled") or 0), row.get("symbol", "")))
        return rows

    return _safe_read([], reader)


def load_fund_nav(db_path=None, fund_code=None):
    def reader():
        root = _ensure_ledger_exists(db_path)
        frame = db.read_fund_nav_frame(root, fund_code)
        if frame.empty:
            return pd.DataFrame(columns=["date", "unit_nav", "accumulated_nav", "daily_return"])
        frame = frame.rename(columns={"nav_date": "date"})
        return frame[["date", "unit_nav", "accumulated_nav", "daily_return"]].sort_values("date")

    return _safe_read(pd.DataFrame(), reader)


def load_stock_daily(db_path=None, symbol=None):
    def reader():
        root = _ensure_ledger_exists(db_path)
        frame = db.read_stock_daily_frame(root, symbol)
        if frame.empty:
            return pd.DataFrame(columns=["date", "open", "high", "low", "close", "volume", "amount", "adjust_type"])
        frame = frame.rename(columns={"trade_date": "date"})
        return frame[["date", "open", "high", "low", "close", "volume", "amount", "adjust_type"]].sort_values("date")

    return _safe_read(pd.DataFrame(), reader)


def load_holdings(db_path=None):
    def reader():
        root = _ensure_ledger_exists(db_path)
        return pd.DataFrame(db.fetch_holdings(root))

    return _safe_read(pd.DataFrame(), reader)


def load_update_logs(db_path=None, limit=20, status=None):
    def reader():
        root = _ensure_ledger_exists(db_path)
        logs = db.fetch_recent_logs(root, limit=1000000)
        if status in {"success", "failed"}:
            logs = [row for row in logs if row.get("status") == status]
        return pd.DataFrame(logs[: int(limit)])

    return _safe_read(pd.DataFrame(), reader)


def load_asset_statuses(db_path=None):
    def reader():
        root = _ensure_ledger_exists(db_path)
        watchlist = db.fetch_watchlist(root)
        return [_asset_status(root, item) for item in watchlist]

    return _safe_read([], reader)


def _asset_status(root, item):
    symbol = item["symbol"]
    asset_type = item["asset_type"]
    if item.get("data_source") == "akshare_pending" or index_symbols.is_pending_symbol(symbol):
        mapping = index_symbols.resolve_index_symbol(symbol)
        return _status_row(item, "代码待确认", mapping.note, can_show_price=False)

    if asset_type == "fund":
        row_count = len(db.read_fund_nav_frame(root, symbol))
        if row_count >= 2:
            return _status_row(item, "已有可用数据", f"已有 {row_count} 条净值数据")
        failed = _latest_failed_message(root, symbol)
        if failed:
            return _status_row(item, "接口失败", failed, can_show_price=False)
        return _status_row(item, "暂无数据", "本地暂无净值数据；接口暂无数据/待确认", can_show_price=False)

    if asset_type in {"stock", "index"}:
        frame = db.read_stock_daily_frame(root, symbol)
        rows = len(frame)
        close_rows = int(frame["close"].notna().sum()) if "close" in frame else 0
        volume_rows = int(frame["volume"].notna().sum()) if "volume" in frame else 0
        if rows >= 2 and close_rows >= 2:
            if volume_rows == 0:
                return _status_row(
                    item,
                    "数据字段不完整",
                    "当前指数数据源未提供成交量，已仅展示价格走势",
                    can_show_price=True,
                )
            return _status_row(item, "已有可用数据", f"已有 {rows} 条日线数据")
        failed = _latest_failed_message(root, symbol)
        if failed:
            return _status_row(item, "接口失败", failed, can_show_price=False)
        return _status_row(item, "暂无数据", "本地暂无日线数据", can_show_price=False)

    return _status_row(item, "暂无数据", "暂不支持的标的类型", can_show_price=False)


def _latest_failed_message(root, symbol):
    logs = db.fetch_recent_logs(root, limit=1000000)
    for row in logs:
        if row.get("status") == "failed" and symbol in row.get("task_name", ""):
            return row.get("message")
    return None


def _status_row(item, status, reason, can_show_price=True):
    return {
        "symbol": item["symbol"],
        "name": item["name"],
        "asset_type": item["asset_type"],
        "enabled": item["enabled"],
        "status": status,
        "reason": reason,
        "can_show_price": can_show_price,
    }


def period_change(frame, value_column, days):
    if frame is None or frame.empty or value_column not in frame:
        return None
    values = frame[value_column].dropna()
    if len(values) < 2:
        return None
    start_index = max(0, len(values) - int(days))
    start = values.iloc[start_index]
    end = values.iloc[-1]
    if start == 0:
        return None
    return (end - start) / start * 100


def fund_observation_text(change_20=None, profit_rate=None):
    if change_20 is None:
        return "数据不足，暂不判断。"
    if profit_rate is not None and profit_rate <= -5 and change_20 <= -5:
        return "进入补仓观察区，可考虑小额补仓，但仍需结合资金安排。"
    if change_20 <= -5:
        return "回撤较明显，进入观察区；没有持仓数据时先不判断补仓。"
    if change_20 >= 8:
        return "涨幅较大，暂不操作，避免追涨。"
    return "继续观察，不因一天涨跌频繁交易。"


def stock_observation_text(change_20=None):
    if change_20 is None:
        return "数据不足，暂不判断。"
    if change_20 <= -5:
        return "走势回落，先做观察提醒，不输出确定性买入建议。"
    if change_20 >= 8:
        return "涨幅较大，注意不追涨。"
    return "继续观察，保持纪律。"


def format_pct(value):
    if value is None:
        return "数据不足"
    return f"{value:.2f}%"
