from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src import analysis, config  # noqa: E402


def main():
    print(analysis.generate_report(config.DATA_DIR))


if __name__ == "__main__":
    main()
