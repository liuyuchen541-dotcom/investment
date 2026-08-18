from pathlib import Path
import argparse
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src import config, db  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description="手动新增或更新一条持仓记录")
    parser.add_argument("--asset-code", required=True, help="标的代码，例如 014777")
    parser.add_argument("--asset-name", required=True, help="标的名称")
    parser.add_argument(
        "--asset-type",
        required=True,
        choices=["fund", "stock", "index"],
        help="标的类型",
    )
    parser.add_argument("--holding-amount", type=float, required=True, help="当前持仓金额")
    parser.add_argument("--cost-amount", type=float, required=True, help="累计投入本金")
    parser.add_argument("--profit-rate", type=float, required=True, help="当前收益率，例如 -1.5")
    parser.add_argument("--note", default="", help="备注")
    args = parser.parse_args()

    db.initialize_database(config.DATA_DIR)
    db.upsert_holding(
        config.DATA_DIR,
        {
            "asset_code": args.asset_code,
            "asset_name": args.asset_name,
            "asset_type": args.asset_type,
            "holding_amount": args.holding_amount,
            "cost_amount": args.cost_amount,
            "profit_rate": args.profit_rate,
            "note": args.note,
        },
    )
    print(f"持仓已保存：{args.asset_name}（{args.asset_code}）")


if __name__ == "__main__":
    main()
