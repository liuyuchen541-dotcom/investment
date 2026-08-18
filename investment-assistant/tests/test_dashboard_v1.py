import csv
import tempfile
import unittest
from pathlib import Path

import pandas as pd


class DashboardV1Test(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.root = Path(self.tmp.name)
        self._create_sample_ledger()

    def tearDown(self):
        self.tmp.cleanup()

    def _create_sample_ledger(self):
        from src import db

        db.initialize_database(self.root)
        _write_csv(
            self.root / "ledger" / "watchlist.csv",
            ["symbol", "name", "asset_type", "data_source", "enabled", "note"],
            [
                ("014777", "富国中证芯片产业 ETF 联接 C", "fund", "akshare", 1, "基金"),
                ("025857", "华夏中证电网设备主题 ETF 联接 C", "fund", "akshare", 1, "基金"),
                ("002714", "牧原股份", "stock", "akshare", 1, "股票"),
                ("sh000300", "沪深300", "index", "akshare", 0, "指数"),
                ("CSI_A500_PENDING", "中证A500", "index", "akshare_pending", 0, "AKShare 指数代码待确认"),
            ],
        )
        db.insert_fund_nav(
            self.root,
            [
                {"fund_code": "014777", "nav_date": "2026-06-09", "unit_nav": 1.0, "accumulated_nav": None, "daily_return": None},
                {"fund_code": "014777", "nav_date": "2026-06-10", "unit_nav": 0.98, "accumulated_nav": None, "daily_return": -2.0},
                {"fund_code": "014777", "nav_date": "2026-06-11", "unit_nav": 0.95, "accumulated_nav": None, "daily_return": -3.06},
            ],
        )
        db.insert_stock_daily(
            self.root,
            [
                {"symbol": "002714", "trade_date": "2026-06-09", "open": 33.0, "high": 34.0, "low": 32.5, "close": 33.8, "volume": 1000, "amount": 33800, "adjust_type": "qfq"},
                {"symbol": "002714", "trade_date": "2026-06-10", "open": 33.8, "high": 34.2, "low": 33.2, "close": 33.4, "volume": 1200, "amount": 40080, "adjust_type": "qfq"},
                {"symbol": "002714", "trade_date": "2026-06-11", "open": 33.4, "high": 33.9, "low": 33.0, "close": 33.1, "volume": 900, "amount": 29790, "adjust_type": "qfq"},
                {"symbol": "sh000300", "trade_date": "2026-06-09", "open": 4700.0, "high": 4720.0, "low": 4680.0, "close": 4710.0, "volume": None, "amount": 100000, "adjust_type": "none"},
                {"symbol": "sh000300", "trade_date": "2026-06-10", "open": 4710.0, "high": 4730.0, "low": 4690.0, "close": 4705.0, "volume": None, "amount": 100000, "adjust_type": "none"},
            ],
        )
        db.upsert_holding(
            self.root,
            {
                "asset_code": "014777",
                "asset_name": "富国中证芯片产业 ETF 联接 C",
                "asset_type": "fund",
                "holding_amount": 890.8,
                "cost_amount": 679.0,
                "profit_rate": 31.19,
                "updated_at": "2026-06-12",
                "note": "测试",
            },
        )
        db.log_update(self.root, "update fund 014777 富国中证芯片产业 ETF 联接 C", "success", "新增 3 行", "2026-06-12T10:00:00")
        db.log_update(self.root, "update fund 025857 华夏中证电网设备主题 ETF 联接 C", "failed", "接口暂无数据/待确认", "2026-06-12T10:01:00")
        db.log_update(self.root, "update stock 002714 牧原股份", "failed", "网络失败", "2026-06-12T10:02:00")

    def test_missing_ledger_returns_user_friendly_error(self):
        from src import dashboard_data

        missing = Path(self.tmp.name) / "missing"

        result = dashboard_data.get_table_counts(missing)

        self.assertEqual(result.data, {})
        self.assertIn("python scripts/init_db.py", result.message)

    def test_table_counts_and_watchlist_filters_are_read_only(self):
        from src import dashboard_data

        counts = dashboard_data.get_table_counts(self.root)
        funds = dashboard_data.load_watchlist(self.root, asset_types=["fund"])

        self.assertEqual(counts.data["watchlist"], 5)
        self.assertEqual(counts.data["fund_nav"], 3)
        self.assertEqual(counts.data["stock_daily"], 5)
        self.assertEqual(len(funds.data), 2)
        self.assertEqual(funds.data[0]["symbol"], "014777")

    def test_load_price_holdings_and_filtered_logs(self):
        from src import dashboard_data

        fund_nav = dashboard_data.load_fund_nav(self.root, "014777")
        stock_daily = dashboard_data.load_stock_daily(self.root, "002714")
        holdings = dashboard_data.load_holdings(self.root)
        failed_logs = dashboard_data.load_update_logs(self.root, limit=20, status="failed")

        self.assertEqual(list(fund_nav.data["unit_nav"]), [1.0, 0.98, 0.95])
        self.assertEqual(list(stock_daily.data["close"]), [33.8, 33.4, 33.1])
        self.assertEqual(holdings.data.iloc[0]["profit_rate"], 31.19)
        self.assertEqual(len(failed_logs.data), 2)
        self.assertEqual(failed_logs.data.iloc[0]["status"], "failed")

    def test_asset_statuses_distinguish_usable_empty_failed_pending_and_incomplete(self):
        from src import dashboard_data

        statuses = dashboard_data.load_asset_statuses(self.root).data
        by_symbol = {row["symbol"]: row for row in statuses}

        self.assertEqual(by_symbol["014777"]["status"], "已有可用数据")
        self.assertEqual(by_symbol["025857"]["status"], "接口失败")
        self.assertIn("接口暂无数据", by_symbol["025857"]["reason"])
        self.assertEqual(by_symbol["sh000300"]["status"], "数据字段不完整")
        self.assertTrue(by_symbol["sh000300"]["can_show_price"])
        self.assertIn("成交量", by_symbol["sh000300"]["reason"])
        self.assertEqual(by_symbol["CSI_A500_PENDING"]["status"], "代码待确认")

    def test_observation_text_never_uses_absolute_buy_sell_language(self):
        from src import dashboard_data

        text = dashboard_data.fund_observation_text(change_20=-6.0, profit_rate=-8.0)

        self.assertIn("可考虑小额补仓", text)
        self.assertNotIn("必须买", text)
        self.assertNotIn("立即卖", text)

    def test_chart_builders_handle_empty_and_non_empty_data(self):
        from src import dashboard_charts

        empty = pd.DataFrame()
        fund = pd.DataFrame(
            {
                "date": ["2026-06-09", "2026-06-10"],
                "unit_nav": [1.0, 0.98],
            }
        )
        stock = pd.DataFrame(
            {
                "date": ["2026-06-09", "2026-06-10"],
                "open": [33.0, 33.8],
                "high": [34.0, 34.2],
                "low": [32.5, 33.2],
                "close": [33.8, 33.4],
                "volume": [1000, 1200],
            }
        )
        holdings = pd.DataFrame(
            {
                "asset_name": ["基金A", "股票B"],
                "holding_amount": [100.0, 200.0],
                "profit_rate": [3.0, -2.0],
            }
        )

        self.assertIsNone(dashboard_charts.fund_nav_line(empty, "空基金"))
        self.assertEqual(len(dashboard_charts.fund_nav_line(fund, "基金A").data), 1)
        self.assertEqual(len(dashboard_charts.stock_candlestick(stock, "牧原股份").data), 1)
        self.assertEqual(len(dashboard_charts.stock_volume_bar(stock, "牧原股份").data), 1)
        self.assertEqual(len(dashboard_charts.holding_profit_bar(holdings).data), 1)
        self.assertEqual(len(dashboard_charts.holding_amount_pie(holdings).data), 1)


def _write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(fields)
        writer.writerows(rows)


if __name__ == "__main__":
    unittest.main()
