from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src import config, quality_check  # noqa: E402


def main():
    messages = quality_check.run_quality_checks(config.DATA_DIR)
    print("数据质量检查结果：")
    for message in messages:
        print(f"- {message}")


if __name__ == "__main__":
    main()
