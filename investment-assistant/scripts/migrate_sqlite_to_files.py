from datetime import datetime
from pathlib import Path
import shutil
import sqlite3
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src import config, db  # noqa: E402


TABLES = [
    "watchlist",
    "stock_daily",
    "fund_nav",
    "portfolio_holding",
    "trade_record",
    "update_log",
]


def main():
    db_path = config.DB_PATH
    if not db_path.exists():
        print("未找到旧 SQLite 数据库，跳过迁移。")
        return

    with sqlite3.connect(db_path) as conn:
        counts = _table_counts(conn)
        frames = {table: pd.read_sql_query(f"SELECT * FROM {table}", conn) for table in TABLES}

    _validate_personal_records(frames, counts)
    _write_csv_files(frames)
    _write_holdings_doc()
    _validate_csv_counts(counts)

    archive_path = _archive_path()
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(db_path), archive_path)

    print("SQLite 已迁移为 CSV + Markdown 文件账本。")
    print(f"旧数据库已归档：{archive_path}")
    print(f"迁移行数：{counts}")


def _archive_path():
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return config.ARCHIVE_DIR / f"investment_data_{stamp}.db"


def _table_counts(conn):
    return {
        table: conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        for table in TABLES
    }


def _write_csv_files(frames):
    config.LEDGER_DIR.mkdir(parents=True, exist_ok=True)
    config.FUND_NAV_DIR.mkdir(parents=True, exist_ok=True)
    config.STOCK_DAILY_DIR.mkdir(parents=True, exist_ok=True)
    config.LOG_DIR.mkdir(parents=True, exist_ok=True)

    _write_csv(frames["portfolio_holding"], config.LEDGER_DIR / "holdings.csv", db.HOLDING_FIELDS)
    _write_csv(frames["trade_record"], config.LEDGER_DIR / "trades.csv", db.TRADE_FIELDS)
    _write_csv(frames["watchlist"], config.LEDGER_DIR / "watchlist.csv", db.WATCHLIST_FIELDS)
    _write_csv(frames["update_log"], config.LOG_DIR / "update_log.csv", db.UPDATE_LOG_FIELDS)

    fund_nav = frames["fund_nav"]
    if not fund_nav.empty:
        for fund_code, group in fund_nav.groupby("fund_code", sort=True):
            _write_csv(group, config.FUND_NAV_DIR / f"{fund_code}.csv", db.FUND_NAV_FIELDS)

    stock_daily = frames["stock_daily"]
    if not stock_daily.empty:
        for symbol, group in stock_daily.groupby("symbol", sort=True):
            _write_csv(group, config.STOCK_DAILY_DIR / f"{symbol}.csv", db.STOCK_DAILY_FIELDS)


def _write_csv(frame, path, columns):
    path.parent.mkdir(parents=True, exist_ok=True)
    output = frame.drop(columns=["id"], errors="ignore").copy()
    for column in columns:
        if column not in output:
            output[column] = ""
    output = output[columns]
    output.to_csv(path, index=False, encoding="utf-8-sig")


def _write_holdings_doc():
    docs_dir = PROJECT_ROOT / "docs" / "holdings"
    docs_dir.mkdir(parents=True, exist_ok=True)
    readme = docs_dir / "README.md"
    readme.write_text(
        "\n".join(
            [
                "# 持仓文件账本说明",
                "",
                "本目录用于保存人工可读的持仓快照说明。",
                "",
                "- 权威持仓数据：`data/ledger/holdings.csv`",
                "- 权威交易数据：`data/ledger/trades.csv`",
                "- 权威关注清单：`data/ledger/watchlist.csv`",
                "- 来源：由旧 SQLite `data/investment_data.db` 迁移导出，并保留旧库归档备份。",
                "- 维护方式：后续通过脚本或手动编辑 CSV 维护；项目运行不再依赖 SQLite。",
                "",
                "注意：个人持仓和交易记录优先保护；行情缓存可重新拉取，但迁移时也会尽量保留。",
                "",
            ]
        ),
        encoding="utf-8",
    )


def _validate_personal_records(frames, counts):
    expected = {
        "portfolio_holding": 12,
        "trade_record": 1,
        "watchlist": 13,
    }
    for table, expected_count in expected.items():
        if counts[table] != expected_count:
            raise RuntimeError(f"{table} 行数不符合预期：SQLite={counts[table]}, 预期={expected_count}")

    holdings = frames["portfolio_holding"]
    trades = frames["trade_record"]
    muyuan_trade = trades[
        (trades["asset_code"].astype(str) == "002714")
        & (trades["action"].astype(str) == "buy")
        & (trades["amount"].astype(float).round(2) == 3390.00)
        & (trades["trade_date"].astype(str) == "2026-06-11")
    ]
    if muyuan_trade.empty:
        raise RuntimeError("未找到牧原股份 2026-06-11 / buy / 3390.00 交易记录，停止迁移。")

    muyuan_holding = holdings[
        (holdings["asset_code"].astype(str) == "002714")
        & (holdings["cost_amount"].astype(float).round(2) == 3390.00)
    ]
    if muyuan_holding.empty:
        raise RuntimeError("未找到牧原股份成本 3390.00 的持仓记录，停止迁移。")
    note_text = " ".join(muyuan_holding["note"].fillna("").astype(str).tolist())
    if "100" not in note_text:
        raise RuntimeError("牧原股份持仓备注中未找到 100 股说明，停止迁移。")

    required_funds = ["014777", "014881"]
    missing_funds = [
        code
        for code in required_funds
        if holdings[holdings["asset_code"].astype(str) == code].empty
    ]
    if missing_funds:
        raise RuntimeError(f"关键基金持仓缺失：{missing_funds}")


def _validate_csv_counts(expected_counts):
    checks = {
        "portfolio_holding": len(pd.read_csv(config.LEDGER_DIR / "holdings.csv")),
        "trade_record": len(pd.read_csv(config.LEDGER_DIR / "trades.csv")),
        "watchlist": len(pd.read_csv(config.LEDGER_DIR / "watchlist.csv")),
        "update_log": len(pd.read_csv(config.LOG_DIR / "update_log.csv")),
    }
    checks["fund_nav"] = sum(len(pd.read_csv(path)) for path in config.FUND_NAV_DIR.glob("*.csv"))
    checks["stock_daily"] = sum(len(pd.read_csv(path)) for path in config.STOCK_DAILY_DIR.glob("*.csv"))

    for table, actual in checks.items():
        expected = expected_counts[table]
        if actual != expected:
            raise RuntimeError(f"{table} 迁移行数不一致：SQLite={expected}, CSV={actual}")


if __name__ == "__main__":
    main()
