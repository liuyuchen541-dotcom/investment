from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src import config, db  # noqa: E402


def main():
    db.initialize_database(config.DATA_DIR)
    watchlist = db.fetch_watchlist(config.DATA_DIR)
    print(f"文件账本已初始化：{config.DATA_DIR / 'ledger'}")
    print(f"默认关注标的数量：{len(watchlist)}")
    print("可重复运行，本脚本不会删除已有持仓、交易或行情数据。")


if __name__ == "__main__":
    main()
