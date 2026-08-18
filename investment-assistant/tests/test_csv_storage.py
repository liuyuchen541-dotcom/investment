import tempfile
import unittest
from pathlib import Path


class CsvStorageTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_initialize_creates_csv_ledger_without_sqlite_file(self):
        from src import db

        db.initialize_database(self.root)
        holdings = self.root / "ledger" / "holdings.csv"
        trades = self.root / "ledger" / "trades.csv"
        watchlist = self.root / "ledger" / "watchlist.csv"

        self.assertTrue(holdings.exists())
        self.assertTrue(trades.exists())
        self.assertTrue(watchlist.exists())
        self.assertFalse((self.root / "investment_data.db").exists())
        self.assertEqual(len(db.fetch_watchlist(self.root)), 13)

    def test_csv_storage_preserves_holding_and_trade_records(self):
        from src import db

        db.initialize_database(self.root)
        db.upsert_holding(
            self.root,
            {
                "asset_code": "002714",
                "asset_name": "牧原股份",
                "asset_type": "stock",
                "holding_amount": 3501.0,
                "cost_amount": 3390.0,
                "profit_rate": 3.2743,
                "note": "100 股",
            },
        )
        db.insert_trade_record(
            self.root,
            {
                "asset_code": "002714",
                "asset_name": "牧原股份",
                "action": "buy",
                "amount": 3390.0,
                "trade_date": "2026-06-11",
                "reason": "33.90 元买入 1 手",
            },
        )

        holdings = db.fetch_holdings(self.root)
        trades = db.fetch_trades(self.root)

        self.assertEqual(len(holdings), 1)
        self.assertEqual(holdings[0]["asset_name"], "牧原股份")
        self.assertEqual(holdings[0]["cost_amount"], 3390.0)
        self.assertEqual(len(trades), 1)
        self.assertEqual(trades[0]["action"], "buy")

    def test_market_rows_are_deduplicated_in_csv_files(self):
        from src import db

        db.initialize_database(self.root)
        rows = [
            {
                "symbol": "002714",
                "trade_date": "2026-06-12",
                "open": 34.0,
                "high": 35.5,
                "low": 33.9,
                "close": 35.01,
                "volume": 1,
                "amount": 3501,
                "adjust_type": "qfq",
            },
            {
                "symbol": "002714",
                "trade_date": "2026-06-12",
                "open": 34.0,
                "high": 35.5,
                "low": 33.9,
                "close": 35.01,
                "volume": 1,
                "amount": 3501,
                "adjust_type": "qfq",
            },
        ]

        inserted_first = db.insert_stock_daily(self.root, rows)
        inserted_second = db.insert_stock_daily(self.root, rows)

        self.assertEqual(inserted_first, 1)
        self.assertEqual(inserted_second, 0)
        self.assertEqual(db.get_latest_stock_date(self.root, "002714", "qfq"), "2026-06-12")


if __name__ == "__main__":
    unittest.main()
