import csv
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

import pandas as pd


class FakeAkshareClient:
    def __init__(self):
        self.calls = []

    def fetch_stock_daily(self, symbol, start_date, end_date):
        self.calls.append(("stock", symbol, start_date, end_date))
        return [
            {
                "symbol": symbol,
                "trade_date": "2026-06-10",
                "open": 41.0,
                "high": 42.0,
                "low": 40.5,
                "close": 41.5,
                "volume": 1000,
                "amount": 41500,
                "adjust_type": "qfq",
            }
        ]

    def fetch_fund_nav(self, fund_code, start_date, end_date):
        self.calls.append(("fund", fund_code, start_date, end_date))
        if fund_code == "014777":
            raise RuntimeError("simulated fund source failure")
        return []

    def fetch_index_daily(self, symbol, start_date, end_date):
        self.calls.append(("index", symbol, start_date, end_date))
        return [
            {
                "symbol": symbol,
                "trade_date": "2026-06-10",
                "open": 4000.0,
                "high": 4010.0,
                "low": 3990.0,
                "close": 4005.0,
                "volume": 1000,
                "amount": 4005000,
                "adjust_type": "none",
            }
        ]


class InvestmentAssistantV1Test(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_init_database_creates_csv_ledger_once(self):
        from src import db

        db.initialize_database(self.root)
        db.initialize_database(self.root)

        self.assertTrue((self.root / "ledger" / "watchlist.csv").exists())
        self.assertTrue((self.root / "ledger" / "holdings.csv").exists())
        self.assertTrue((self.root / "ledger" / "trades.csv").exists())
        self.assertFalse((self.root / "investment_data.db").exists())
        watchlist = db.fetch_watchlist(self.root)
        self.assertEqual(len(watchlist), 13)
        self.assertEqual(len([row for row in watchlist if row["asset_type"] == "fund"]), 7)
        self.assertEqual({row["symbol"]: row for row in watchlist}["002714"]["enabled"], 1)

    def test_update_daily_logs_failures_and_continues_next_asset(self):
        from src import db, update_data

        db.initialize_database(self.root)
        fake_client = FakeAkshareClient()

        results = update_data.update_daily(
            db_path=self.root,
            client=fake_client,
            limit=2,
            sleep_seconds=0,
        )

        stock_rows = db.read_stock_daily_frame(self.root, "002714")
        logs = db.fetch_recent_logs(self.root, limit=10)
        logs.reverse()

        self.assertEqual(len(stock_rows), 1)
        self.assertEqual(len(results), 2)
        self.assertIn(("fund", "014777", "20240101", results[0]["end_date"]), fake_client.calls)
        self.assertEqual(logs[0]["status"], "failed")
        self.assertIn("014777", logs[0]["task_name"])
        self.assertEqual(logs[1]["status"], "success")
        self.assertIn("002714", logs[1]["task_name"])

    def test_update_daily_can_update_specific_disabled_index_by_symbol(self):
        from src import db, update_data

        db.initialize_database(self.root)
        fake_client = FakeAkshareClient()

        results = update_data.update_daily(
            db_path=self.root,
            client=fake_client,
            symbols=["sh000300"],
            sleep_seconds=0,
        )

        index_rows = db.read_stock_daily_frame(self.root, "sh000300")

        self.assertEqual(results[0]["symbol"], "sh000300")
        self.assertEqual(len(index_rows), 1)

    def test_update_daily_skips_pending_index_without_calling_interface(self):
        from src import db, update_data

        class ClientThatMustNotBeCalled:
            def fetch_index_daily(self, symbol, start_date, end_date):
                raise AssertionError("pending index should not call AKShare")

        db.initialize_database(self.root)
        _append_watchlist_row(
            self.root,
            {
                "symbol": "CSI_A500_PENDING",
                "name": "中证A500",
                "asset_type": "index",
                "data_source": "akshare_pending",
                "enabled": 0,
                "note": "AKShare 指数代码待确认",
            },
        )

        results = update_data.update_daily(
            db_path=self.root,
            client=ClientThatMustNotBeCalled(),
            symbols=["CSI_A500_PENDING"],
            sleep_seconds=0,
        )

        logs = db.fetch_recent_logs(self.root, limit=1)

        self.assertEqual(results[0]["status"], "failed")
        self.assertIn("代码待确认", logs[0]["message"])

    def test_index_daily_uses_confirmed_mainland_index_mapping_with_volume(self):
        from src import akshare_client

        class FakeAk:
            @staticmethod
            def index_zh_a_hist(symbol, period, start_date, end_date):
                assert symbol == "000300"
                return pd.DataFrame(
                    [
                        {
                            "日期": "2026-06-12",
                            "开盘": 4784.64,
                            "最高": 4809.86,
                            "最低": 4757.56,
                            "收盘": 4785.68,
                            "成交量": 279740191,
                            "成交额": 735952267217.2,
                        }
                    ]
                )

        original_loader = akshare_client._load_akshare
        akshare_client._load_akshare = lambda: FakeAk
        try:
            rows = akshare_client.fetch_index_daily("sh000300", "20260601", "20260612")
        finally:
            akshare_client._load_akshare = original_loader

        self.assertEqual(rows[0]["symbol"], "sh000300")
        self.assertEqual(rows[0]["close"], 4785.68)
        self.assertEqual(rows[0]["volume"], 279740191)

    def test_index_daily_uses_hong_kong_index_mapping(self):
        from src import akshare_client

        class FakeAk:
            @staticmethod
            def stock_hk_index_daily_sina(symbol):
                assert symbol == "HSTECH"
                return pd.DataFrame(
                    [
                        {
                            "date": "2026-06-12",
                            "open": 4713.29,
                            "high": 4750.6,
                            "low": 4702.74,
                            "close": 4655.74,
                            "volume": 1919568648,
                            "amount": 69447302309,
                        }
                    ]
                )

        original_loader = akshare_client._load_akshare
        akshare_client._load_akshare = lambda: FakeAk
        try:
            rows = akshare_client.fetch_index_daily("HSTECH", "20260601", "20260612")
        finally:
            akshare_client._load_akshare = original_loader

        self.assertEqual(rows[0]["symbol"], "HSTECH")
        self.assertEqual(rows[0]["close"], 4655.74)
        self.assertEqual(rows[0]["volume"], 1919568648)

    def test_empty_update_after_existing_data_is_success_with_no_new_rows(self):
        from src import akshare_client, db, update_data

        class EmptyAfterLatestClient:
            def fetch_fund_nav(self, fund_code, start_date, end_date):
                raise akshare_client.EmptyDataError("no rows for requested date range")

        db.initialize_database(self.root)
        db.insert_fund_nav(
            self.root,
            [
                {
                    "fund_code": "014777",
                    "nav_date": "2026-06-11",
                    "unit_nav": 1.0,
                    "accumulated_nav": None,
                    "daily_return": None,
                }
            ],
        )

        results = update_data.update_daily(
            db_path=self.root,
            client=EmptyAfterLatestClient(),
            symbols=["014777"],
            sleep_seconds=0,
        )

        self.assertEqual(results[0]["status"], "success")
        self.assertIn("暂无新数据", results[0]["message"])

    def test_quality_check_finds_duplicate_missing_and_price_errors(self):
        from src import db, quality_check

        db.initialize_database(self.root)
        _write_csv(
            self.root / "market" / "stock_daily" / "TEST.csv",
            db.STOCK_DAILY_FIELDS,
            [
                {
                    "symbol": "TEST",
                    "trade_date": "2026-06-10",
                    "open": "",
                    "high": 10,
                    "low": 8,
                    "close": 11,
                    "volume": 1,
                    "amount": 1,
                    "adjust_type": "qfq",
                    "created_at": "",
                },
                {
                    "symbol": "TEST",
                    "trade_date": "2026-06-10",
                    "open": "",
                    "high": 10,
                    "low": 8,
                    "close": 11,
                    "volume": 1,
                    "amount": 1,
                    "adjust_type": "qfq",
                    "created_at": "",
                },
            ],
        )

        messages = quality_check.run_quality_checks(self.root)
        joined = "\n".join(messages)

        self.assertIn("缺失值", joined)
        self.assertIn("价格异常", joined)
        self.assertIn("重复", joined)

    def test_report_uses_observation_language_not_absolute_advice(self):
        from src import analysis, db

        db.initialize_database(self.root)
        db.insert_stock_daily(
            self.root,
            [
                {
                    "symbol": "002714",
                    "trade_date": f"2026-06-{idx:02d}",
                    "open": close,
                    "high": close,
                    "low": close,
                    "close": close,
                    "volume": 1,
                    "amount": 1,
                    "adjust_type": "qfq",
                }
                for idx, close in enumerate([10, 9.5, 9.0, 8.8, 8.7], start=1)
            ],
        )

        report = analysis.generate_report(self.root)

        self.assertIn("不构成投资建议", report)
        self.assertIn("可考虑小额补仓", report)
        self.assertNotIn("必须买入", report)
        self.assertNotIn("立即卖出", report)

    def test_fund_nav_accepts_missing_accumulated_nav_when_unit_nav_exists(self):
        from src import akshare_client

        class FakeAk:
            @staticmethod
            def fund_open_fund_info_em(symbol, indicator):
                return pd.DataFrame(
                    [
                        {
                            "净值日期": "2026-06-10",
                            "单位净值": "1.2345",
                            "日增长率": "-0.12",
                        }
                    ]
                )

        original_loader = akshare_client._load_akshare
        akshare_client._load_akshare = lambda: FakeAk
        try:
            rows = akshare_client.fetch_fund_nav("014777", "20260601", "20260612")
        finally:
            akshare_client._load_akshare = original_loader

        self.assertEqual(rows[0]["fund_code"], "014777")
        self.assertEqual(rows[0]["accumulated_nav"], None)
        self.assertEqual(rows[0]["unit_nav"], 1.2345)

    def test_fund_nav_calculates_daily_return_when_return_column_missing(self):
        from src import akshare_client

        class FakeAk:
            @staticmethod
            def fund_open_fund_info_em(symbol, indicator):
                return pd.DataFrame(
                    [
                        {"净值日期": "2026-06-09", "单位净值": "1.0000"},
                        {"净值日期": "2026-06-10", "单位净值": "1.0200"},
                    ]
                )

        original_loader = akshare_client._load_akshare
        akshare_client._load_akshare = lambda: FakeAk
        try:
            rows = akshare_client.fetch_fund_nav("014777", "20260601", "20260612")
        finally:
            akshare_client._load_akshare = original_loader

        self.assertEqual(rows[1]["daily_return"], 2.0)

    def test_error_messages_are_classified_by_real_cause(self):
        from src import akshare_client

        self.assertIn(
            "未安装 AKShare",
            akshare_client.describe_error(ModuleNotFoundError("No module named akshare")),
        )
        self.assertIn(
            "网络或接口连接失败",
            akshare_client.describe_error(RuntimeError("SSL: UNEXPECTED_EOF_WHILE_READING")),
        )
        self.assertIn(
            "接口字段变化",
            akshare_client.describe_error(ValueError("stock_zh_a_hist 返回字段缺失：['日期']")),
        )
        self.assertIn(
            "暂无数据",
            akshare_client.describe_error(akshare_client.EmptyDataError("empty")),
        )

    def test_report_lists_success_failures_and_data_gaps(self):
        from src import analysis, db

        db.initialize_database(self.root)
        db.log_update(
            self.root,
            "update fund 014777 富国中证芯片产业 ETF 联接 C",
            "success",
            "获取 2 行，新增 2 行",
            datetime.now().isoformat(timespec="seconds"),
        )
        db.log_update(
            self.root,
            "update stock 002714 牧原股份",
            "failed",
            "网络或接口连接失败：SSL: UNEXPECTED_EOF_WHILE_READING",
            datetime.now().isoformat(timespec="seconds"),
        )

        report = analysis.generate_report(self.root)

        self.assertIn("成功更新的标的", report)
        self.assertIn("014777", report)
        self.assertIn("更新失败的标的", report)
        self.assertIn("002714", report)
        self.assertIn("数据不足的标的", report)
        self.assertIn("暂无手动持仓记录", report)

    def test_can_upsert_manual_holding(self):
        from src import db

        db.initialize_database(self.root)
        db.upsert_holding(
            self.root,
            {
                "asset_code": "014777",
                "asset_name": "富国中证芯片产业 ETF 联接 C",
                "asset_type": "fund",
                "holding_amount": 100.0,
                "cost_amount": 120.0,
                "profit_rate": -1.5,
                "note": "测试持仓",
            },
        )

        holdings = db.fetch_holdings(self.root)

        self.assertEqual(len(holdings), 1)
        self.assertEqual(holdings[0]["asset_code"], "014777")
        self.assertEqual(holdings[0]["profit_rate"], -1.5)


def _append_watchlist_row(root, row):
    path = root / "ledger" / "watchlist.csv"
    with path.open("a", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["symbol", "name", "asset_type", "data_source", "enabled", "note"],
        )
        writer.writerow(row)


def _write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    unittest.main()
