from datetime import date, datetime, timedelta
import time

from . import akshare_client, config, db


def update_daily(db_path=None, client=None, limit=None, sleep_seconds=None, symbols=None):
    path = db_path or config.DATA_DIR
    source = client or akshare_client
    delay = config.REQUEST_SLEEP_SECONDS if sleep_seconds is None else sleep_seconds
    db.initialize_database(path)

    if symbols:
        watchlist = db.fetch_watchlist_by_symbols(path, symbols)
        if limit is not None:
            watchlist = watchlist[: int(limit)]
    else:
        watchlist = db.get_enabled_watchlist(path, limit=limit)

    results = []
    for item in watchlist:
        results.append(_update_one(path, source, item))
        if delay:
            time.sleep(delay)
    return results


def _update_one(db_path, client, item):
    started_at = datetime.now().isoformat(timespec="seconds")
    task_name = f"update {item['asset_type']} {item['symbol']} {item['name']}"
    end_date = date.today().strftime("%Y%m%d")
    try:
        if item.get("data_source") == "akshare_pending" or str(item["symbol"]).endswith("_PENDING"):
            raise akshare_client.PendingSymbolError(
                f"{item['symbol']} 代码待确认，未调用接口，避免写入错误数据"
            )

        start_date = _next_start_date(db_path, item)
        if start_date > end_date:
            message = "本地数据已是最新，无需更新"
            db.log_update(db_path, task_name, "success", message, started_at)
            return _result(item["symbol"], "success", 0, message, end_date)

        if item["asset_type"] == "stock":
            rows = client.fetch_stock_daily(item["symbol"], start_date, end_date)
            inserted = db.insert_stock_daily(db_path, rows)
        elif item["asset_type"] == "index":
            rows = client.fetch_index_daily(item["symbol"], start_date, end_date)
            inserted = db.insert_stock_daily(db_path, rows)
        elif item["asset_type"] == "fund":
            rows = client.fetch_fund_nav(item["symbol"], start_date, end_date)
            inserted = db.insert_fund_nav(db_path, rows)
        else:
            raise ValueError(f"暂不支持的 asset_type：{item['asset_type']}")

        message = f"获取 {len(rows)} 行，新增 {inserted} 行"
        db.log_update(db_path, task_name, "success", message, started_at)
        return _result(item["symbol"], "success", inserted, message, end_date)
    except akshare_client.EmptyDataError as exc:
        if _has_existing_data(db_path, item):
            message = f"暂无新数据：{exc}"
            db.log_update(db_path, task_name, "success", message, started_at)
            return _result(item["symbol"], "success", 0, message, end_date)
        message = akshare_client.describe_error(exc)
        db.log_update(db_path, task_name, "failed", message, started_at)
        return _result(item["symbol"], "failed", 0, message, end_date)
    except Exception as exc:
        message = akshare_client.describe_error(exc)
        db.log_update(db_path, task_name, "failed", message, started_at)
        return _result(item["symbol"], "failed", 0, message, end_date)


def _result(symbol, status, inserted, message, end_date):
    return {
        "symbol": symbol,
        "status": status,
        "inserted": inserted,
        "message": message,
        "end_date": end_date,
    }


def _next_start_date(db_path, item):
    if item["asset_type"] == "fund":
        latest = db.get_latest_fund_nav_date(db_path, item["symbol"])
    else:
        adjust_type = "none" if item["asset_type"] == "index" else "qfq"
        latest = db.get_latest_stock_date(db_path, item["symbol"], adjust_type)
    if not latest:
        return config.DEFAULT_START_DATE
    next_day = datetime.strptime(latest, "%Y-%m-%d").date() + timedelta(days=1)
    return next_day.strftime("%Y%m%d")


def _has_existing_data(db_path, item):
    if item["asset_type"] == "fund":
        return db.get_latest_fund_nav_date(db_path, item["symbol"]) is not None
    adjust_type = "none" if item["asset_type"] == "index" else "qfq"
    return db.get_latest_stock_date(db_path, item["symbol"], adjust_type) is not None
