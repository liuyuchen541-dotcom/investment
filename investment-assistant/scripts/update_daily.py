from pathlib import Path
import argparse
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src import config, update_data  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description="更新关注标的的本地行情 CSV 缓存")
    parser.add_argument("--limit", type=int, default=None, help="只更新前 N 个启用标的")
    parser.add_argument(
        "--symbols",
        default="",
        help="只更新指定代码，多个代码用逗号分隔，例如 014777,002714,sh000300",
    )
    parser.add_argument("--no-sleep", action="store_true", help="测试时跳过 1 秒等待")
    args = parser.parse_args()

    sleep_seconds = 0 if args.no_sleep else config.REQUEST_SLEEP_SECONDS
    symbols = [item.strip() for item in args.symbols.split(",") if item.strip()]
    results = update_data.update_daily(
        config.DATA_DIR,
        limit=args.limit,
        sleep_seconds=sleep_seconds,
        symbols=symbols,
    )
    print("数据更新完成：")
    for item in results:
        print(
            f"- {item['symbol']}：{item['status']}，新增 {item['inserted']} 行，{item['message']}"
        )


if __name__ == "__main__":
    main()
