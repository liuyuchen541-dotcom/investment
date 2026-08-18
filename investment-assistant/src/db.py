import csv
from datetime import datetime
from pathlib import Path

from . import config


WATCHLIST_FIELDS = ["symbol", "name", "asset_type", "data_source", "enabled", "note"]
HOLDING_FIELDS = [
    "asset_code",
    "asset_name",
    "asset_type",
    "holding_amount",
    "cost_amount",
    "profit_rate",
    "updated_at",
    "note",
]
TRADE_FIELDS = ["asset_code", "asset_name", "action", "amount", "trade_date", "reason", "created_at"]
FUND_NAV_FIELDS = ["fund_code", "nav_date", "unit_nav", "accumulated_nav", "daily_return", "created_at"]
STOCK_DAILY_FIELDS = [
    "symbol",
    "trade_date",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "amount",
    "adjust_type",
    "created_at",
]
UPDATE_LOG_FIELDS = ["task_name", "status", "message", "started_at", "finished_at"]

NUMERIC_FIELDS = {
    "holding_amount",
    "cost_amount",
    "profit_rate",
    "amount",
    "unit_nav",
    "accumulated_nav",
    "daily_return",
    "open",
    "high",
    "low",
    "close",
    "volume",
}


def initialize_database(db_path=None):
    root = _root(db_path)
    _ensure_dirs(root)
    _ensure_csv(_watchlist_path(root), WATCHLIST_FIELDS, config.DEFAULT_WATCHLIST)
    _ensure_csv(_holdings_path(root), HOLDING_FIELDS, [])
    _ensure_csv(_trades_path(root), TRADE_FIELDS, [])
    _ensure_csv(_update_log_path(root), UPDATE_LOG_FIELDS, [])


def get_enabled_watchlist(db_path=None, limit=None):
    rows = [row for row in fetch_watchlist(db_path) if int(row.get("enabled") or 0) == 1]
    rows.sort(key=lambda item: (0 if item["symbol"] == "014777" else 1 if item["symbol"] == "002714" else 2))
    if limit is not None:
        return rows[: int(limit)]
    return rows


def fetch_watchlist(db_path=None):
    root = _root(db_path)
    initialize_database(root)
    rows = _read_rows(_watchlist_path(root))
    for row in rows:
        row["enabled"] = int(float(row.get("enabled") or 0))
    return rows


def fetch_watchlist_by_symbols(db_path=None, symbols=None):
    wanted = [symbol.strip() for symbol in (symbols or []) if symbol.strip()]
    if not wanted:
        return []
    by_symbol = {row["symbol"]: row for row in fetch_watchlist(db_path)}
    return [by_symbol[symbol] for symbol in wanted if symbol in by_symbol]


def get_latest_stock_date(db_path, symbol, adjust_type="qfq"):
    rows = [
        row
        for row in _read_stock_rows(_root(db_path), symbol)
        if row.get("adjust_type", "qfq") == adjust_type
    ]
    dates = [row["trade_date"] for row in rows if row.get("trade_date")]
    return max(dates) if dates else None


def get_latest_fund_nav_date(db_path, fund_code):
    rows = _read_fund_rows(_root(db_path), fund_code)
    dates = [row["nav_date"] for row in rows if row.get("nav_date")]
    return max(dates) if dates else None


def insert_stock_daily(db_path, rows):
    if not rows:
        return 0
    root = _root(db_path)
    _ensure_dirs(root)
    by_symbol = {}
    for row in rows:
        by_symbol.setdefault(row["symbol"], []).append(row)
    inserted = 0
    for symbol, symbol_rows in by_symbol.items():
        path = _stock_path(root, symbol)
        existing = _read_rows(path)
        seen = {
            (row.get("symbol"), row.get("trade_date"), row.get("adjust_type") or "qfq")
            for row in existing
        }
        new_rows = []
        for row in symbol_rows:
            normalized = _normalize_row(row, STOCK_DAILY_FIELDS)
            normalized["adjust_type"] = normalized.get("adjust_type") or "qfq"
            normalized["created_at"] = normalized.get("created_at") or _now()
            key = (normalized["symbol"], normalized["trade_date"], normalized["adjust_type"])
            if key not in seen:
                seen.add(key)
                new_rows.append(normalized)
        if new_rows:
            combined = existing + new_rows
            combined.sort(key=lambda item: (item.get("symbol", ""), item.get("trade_date", ""), item.get("adjust_type", "")))
            _write_rows(path, STOCK_DAILY_FIELDS, combined)
            inserted += len(new_rows)
        elif not path.exists():
            _write_rows(path, STOCK_DAILY_FIELDS, [])
    return inserted


def insert_fund_nav(db_path, rows):
    if not rows:
        return 0
    root = _root(db_path)
    _ensure_dirs(root)
    by_fund = {}
    for row in rows:
        by_fund.setdefault(row["fund_code"], []).append(row)
    inserted = 0
    for fund_code, fund_rows in by_fund.items():
        path = _fund_path(root, fund_code)
        existing = _read_rows(path)
        seen = {(row.get("fund_code"), row.get("nav_date")) for row in existing}
        new_rows = []
        for row in fund_rows:
            normalized = _normalize_row(row, FUND_NAV_FIELDS)
            normalized["created_at"] = normalized.get("created_at") or _now()
            key = (normalized["fund_code"], normalized["nav_date"])
            if key not in seen:
                seen.add(key)
                new_rows.append(normalized)
        if new_rows:
            combined = existing + new_rows
            combined.sort(key=lambda item: (item.get("fund_code", ""), item.get("nav_date", "")))
            _write_rows(path, FUND_NAV_FIELDS, combined)
            inserted += len(new_rows)
        elif not path.exists():
            _write_rows(path, FUND_NAV_FIELDS, [])
    return inserted


def log_update(db_path, task_name, status, message, started_at):
    root = _root(db_path)
    initialize_database(root)
    rows = _read_rows(_update_log_path(root))
    rows.append(
        {
            "task_name": task_name,
            "status": status,
            "message": message,
            "started_at": started_at,
            "finished_at": _now(),
        }
    )
    _write_rows(_update_log_path(root), UPDATE_LOG_FIELDS, rows)


def fetch_recent_logs(db_path=None, limit=20):
    rows = _read_rows(_update_log_path(_root(db_path)))
    rows.reverse()
    return rows[: int(limit)]


def fetch_stock_prices(db_path, symbol, limit=25):
    rows = _read_stock_rows(_root(db_path), symbol)
    rows.sort(key=lambda item: item.get("trade_date", ""))
    points = [
        {"date": row.get("trade_date"), "value": _to_float(row.get("close"))}
        for row in rows
        if row.get("trade_date")
    ]
    return points[-int(limit) :]


def fetch_fund_navs(db_path, fund_code, limit=25):
    rows = _read_fund_rows(_root(db_path), fund_code)
    rows.sort(key=lambda item: item.get("nav_date", ""))
    points = [
        {"date": row.get("nav_date"), "value": _to_float(row.get("unit_nav"))}
        for row in rows
        if row.get("nav_date")
    ]
    return points[-int(limit) :]


def fetch_holdings(db_path=None):
    rows = _read_rows(_holdings_path(_root(db_path)))
    rows = [_coerce_row(row) for row in rows]
    rows.sort(key=lambda item: (item.get("asset_type", ""), item.get("asset_code", "")))
    return rows


def upsert_holding(db_path=None, holding=None):
    if holding is None:
        holding = {}
    missing = [key for key in ["asset_code", "asset_name", "asset_type"] if not holding.get(key)]
    if missing:
        raise ValueError(f"持仓记录缺少必要字段：{missing}")
    root = _root(db_path)
    initialize_database(root)
    rows = _read_rows(_holdings_path(root))
    normalized = _normalize_row(holding, HOLDING_FIELDS)
    normalized["updated_at"] = normalized.get("updated_at") or _now()
    replaced = False
    for index, row in enumerate(rows):
        if row.get("asset_code") == normalized["asset_code"]:
            rows[index] = normalized
            replaced = True
            break
    if not replaced:
        rows.append(normalized)
    rows.sort(key=lambda item: (item.get("asset_type", ""), item.get("asset_code", "")))
    _write_rows(_holdings_path(root), HOLDING_FIELDS, rows)


def insert_trade_record(db_path=None, trade=None):
    if trade is None:
        trade = {}
    missing = [key for key in ["asset_code", "asset_name", "action", "amount", "trade_date"] if not trade.get(key)]
    if missing:
        raise ValueError(f"交易记录缺少必要字段：{missing}")
    root = _root(db_path)
    initialize_database(root)
    rows = _read_rows(_trades_path(root))
    normalized = _normalize_row(trade, TRADE_FIELDS)
    normalized["created_at"] = normalized.get("created_at") or _now()
    key = (
        normalized["asset_code"],
        normalized["action"],
        str(normalized["amount"]),
        normalized["trade_date"],
    )
    seen = {
        (row.get("asset_code"), row.get("action"), str(row.get("amount")), row.get("trade_date"))
        for row in rows
    }
    if key not in seen:
        rows.append(normalized)
        _write_rows(_trades_path(root), TRADE_FIELDS, rows)


def fetch_trades(db_path=None):
    rows = _read_rows(_trades_path(_root(db_path)))
    return [_coerce_row(row) for row in rows]


def read_fund_nav_frame(db_path=None, fund_code=None):
    import pandas as pd

    return pd.DataFrame(_read_fund_rows(_root(db_path), fund_code))


def read_stock_daily_frame(db_path=None, symbol=None):
    import pandas as pd

    return pd.DataFrame(_read_stock_rows(_root(db_path), symbol))


def _root(db_path=None):
    if db_path is None:
        return config.DATA_DIR
    path = Path(db_path)
    if path.suffix.lower() == ".db":
        return path.parent
    return path


def _ensure_dirs(root):
    _ledger_dir(root).mkdir(parents=True, exist_ok=True)
    _fund_dir(root).mkdir(parents=True, exist_ok=True)
    _stock_dir(root).mkdir(parents=True, exist_ok=True)
    _log_dir(root).mkdir(parents=True, exist_ok=True)


def _ledger_dir(root):
    return Path(root) / "ledger"


def _fund_dir(root):
    return Path(root) / "market" / "fund_nav"


def _stock_dir(root):
    return Path(root) / "market" / "stock_daily"


def _log_dir(root):
    return Path(root) / "logs"


def _watchlist_path(root):
    return _ledger_dir(root) / "watchlist.csv"


def _holdings_path(root):
    return _ledger_dir(root) / "holdings.csv"


def _trades_path(root):
    return _ledger_dir(root) / "trades.csv"


def _update_log_path(root):
    return _log_dir(root) / "update_log.csv"


def _fund_path(root, fund_code):
    return _fund_dir(root) / f"{fund_code}.csv"


def _stock_path(root, symbol):
    return _stock_dir(root) / f"{symbol}.csv"


def _ensure_csv(path, fields, default_rows):
    if not path.exists():
        _write_rows(path, fields, [_normalize_row(row, fields) for row in default_rows])


def _read_fund_rows(root, fund_code):
    if fund_code is None:
        rows = []
        for path in _fund_dir(root).glob("*.csv"):
            rows.extend(_read_rows(path))
        return [_coerce_row(row) for row in rows]
    return [_coerce_row(row) for row in _read_rows(_fund_path(root, fund_code))]


def _read_stock_rows(root, symbol):
    if symbol is None:
        rows = []
        for path in _stock_dir(root).glob("*.csv"):
            rows.extend(_read_rows(path))
        return [_coerce_row(row) for row in rows]
    return [_coerce_row(row) for row in _read_rows(_stock_path(root, symbol))]


def _read_rows(path):
    path = Path(path)
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def _write_rows(path, fields, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(_normalize_row(row, fields))


def _normalize_row(row, fields):
    normalized = {}
    for field in fields:
        value = row.get(field, "")
        if value is None:
            value = ""
        normalized[field] = value
    return normalized


def _coerce_row(row):
    coerced = dict(row)
    for field in NUMERIC_FIELDS:
        if field in coerced:
            coerced[field] = _to_float(coerced[field])
    if "enabled" in coerced:
        coerced["enabled"] = int(float(coerced["enabled"] or 0))
    return coerced


def _to_float(value):
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _now():
    return datetime.now().isoformat(timespec="seconds")
