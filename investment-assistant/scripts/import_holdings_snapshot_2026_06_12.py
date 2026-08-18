from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src import config, db  # noqa: E402


SNAPSHOT_DATE = "2026-06-12"

FUND_HOLDINGS = [
    ("014777", "富国中证芯片产业 ETF 联接 C", 890.80, 679.00, 31.19, 5.43, 211.80, "微信图片_20260612131726_672_7.jpg"),
    ("014881", "天弘中证机器人 ETF 联接 C", 1052.87, 944.00, 11.53, -34.48, 108.87, "微信图片_20260612131725_671_7.jpg"),
    ("011840", "天弘中证人工智能主题指数 C", 411.81, 344.50, 19.54, -9.86, 67.31, "微信图片_20260612131724_670_7.jpg"),
    ("013309", "易方达恒生科技 ETF 联接(QDII) C", 484.61, 515.00, -5.90, -6.05, -30.39, "微信图片_20260612131715_664_7.jpg"),
    ("025857", "华夏中证电网设备主题 ETF 联接 C", 259.17, 245.00, 5.78, -3.64, 14.17, "微信图片_20260612131723_669_7.jpg"),
    ("023037", "中欧资源精选混合 C", 197.12, 215.00, -8.32, 2.38, -17.88, "微信图片_20260612131717_666_7.jpg"),
    ("022460", "易方达中证 A500 ETF 联接 C", 20.00, 20.00, 0.02, 0.00, 0.00, "微信图片_20260612131719_668_7.jpg"),
    ("010770", "天弘中证农业主题 ETF 联接 C", 29.42, 30.00, -1.92, 0.04, -0.58, "微信图片_20260612131718_667_7.jpg"),
    ("005224", "广发中证基建工程 ETF 联接 C", 282.80, 309.74, -8.70, -0.45, -26.94, "微信图片_20260612131716_665_7.jpg"),
    ("019934", "工银瑞信国证港股通科技 ETF 联接 C", 435.75, 501.00, -13.02, -8.21, -65.25, "微信图片_20260612131713_662_7.jpg"),
    ("015210", "前海开源沪港深农业主题精选灵活配置混合(LOF) C", 217.58, 259.99, -16.31, 2.03, -42.41, "微信图片_20260612131715_663_7.jpg"),
]


def main():
    db.initialize_database(config.DATA_DIR)
    for code, name, amount, cost, rate, yesterday, profit, source in FUND_HOLDINGS:
        db.upsert_holding(
            config.DATA_DIR,
            {
                "asset_code": code,
                "asset_name": name,
                "asset_type": "fund",
                "holding_amount": amount,
                "cost_amount": cost,
                "profit_rate": rate,
                "note": (
                    f"截图提取快照 {SNAPSHOT_DATE}；昨日收益 {yesterday:+.2f} 元；"
                    f"持有收益 {profit:+.2f} 元；来源 {source}"
                ),
            },
        )

    latest_prices = db.fetch_stock_prices(config.DATA_DIR, "002714", limit=1)
    latest_close = latest_prices[-1]["value"] if latest_prices else 33.90
    holding_amount = round(latest_close * 100, 2)
    cost_amount = 3390.00
    profit_rate = round((holding_amount - cost_amount) / cost_amount * 100, 4)

    db.upsert_holding(
        config.DATA_DIR,
        {
            "asset_code": "002714",
            "asset_name": "牧原股份",
            "asset_type": "stock",
            "holding_amount": holding_amount,
            "cost_amount": cost_amount,
            "profit_rate": profit_rate,
            "note": (
                "用户确认：2026-06-11 以 33.90 元买入 1 手（100 股）；"
                f"当前金额按本地最新收盘价 {latest_close:.2f} 元估算。"
            ),
        },
    )
    db.insert_trade_record(
        config.DATA_DIR,
        {
            "asset_code": "002714",
            "asset_name": "牧原股份",
            "action": "buy",
            "amount": 3390.0,
            "trade_date": "2026-06-11",
            "reason": "用户确认：33.90 元买入 1 手（100 股）",
        },
    )
    print("已导入 2026-06-12 持仓截图快照。")


if __name__ == "__main__":
    main()
