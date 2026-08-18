from . import config, db


def run_quality_checks(db_path=None):
    path = db_path or config.DATA_DIR
    messages = []

    stock_rows = db.read_stock_daily_frame(path)
    fund_rows = db.read_fund_nav_frame(path)

    _check_duplicates(
        stock_rows,
        messages,
        "stock_daily",
        ["symbol", "trade_date", "adjust_type"],
    )
    _check_duplicates(fund_rows, messages, "fund_nav", ["fund_code", "nav_date"])
    _check_missing_values(stock_rows, fund_rows, messages)
    _check_stock_price_ranges(stock_rows, messages)

    if not messages:
        messages.append("未发现明显数据质量问题。")
    return messages


def _check_duplicates(frame, messages, table, columns):
    if frame.empty:
        messages.append(f"{table} 暂无数据，跳过重复检查。")
        return
    duplicate_count = int(frame.duplicated(subset=columns, keep=False).sum())
    if duplicate_count:
        messages.append(f"{table} 存在重复数据：{duplicate_count} 行。")
    else:
        messages.append(f"{table} 未发现重复数据。")


def _check_missing_values(stock_rows, fund_rows, messages):
    stock_required = ["trade_date", "open", "high", "low", "close"]
    fund_required = ["nav_date", "unit_nav"]

    stock_missing = _missing_count(stock_rows, stock_required)
    fund_missing = _missing_count(fund_rows, fund_required)
    if stock_missing or fund_missing:
        messages.append(
            f"缺失值检查：stock_daily {stock_missing} 行，fund_nav {fund_missing} 行。"
        )
    else:
        messages.append("缺失值检查：未发现关键字段缺失。")


def _check_stock_price_ranges(stock_rows, messages):
    if stock_rows.empty:
        messages.append("价格异常检查：stock_daily 暂无数据。")
        return
    required = ["open", "high", "low", "close"]
    if any(column not in stock_rows.columns for column in required):
        messages.append("价格异常检查：缺少 open/high/low/close 字段。")
        return

    bad = stock_rows[
        (stock_rows["close"] > stock_rows["high"])
        | (stock_rows["close"] < stock_rows["low"])
        | (stock_rows["open"] > stock_rows["high"])
        | (stock_rows["open"] < stock_rows["low"])
    ]
    if bad.empty:
        messages.append("价格异常检查：未发现 close/open 超出 high/low。")
    else:
        messages.append(f"价格异常检查：发现 {len(bad)} 行 close/open 超出 high/low。")


def _missing_count(frame, columns):
    if frame.empty:
        return 0
    existing = [column for column in columns if column in frame.columns]
    if not existing:
        return 0
    return int(frame[existing].isna().any(axis=1).sum())
