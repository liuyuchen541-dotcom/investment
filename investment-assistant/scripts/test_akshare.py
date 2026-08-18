from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src import akshare_client  # noqa: E402


def main():
    print("AKShare 接口体检")
    print("=" * 20)
    ak = _check_install()
    if ak is None:
        return
    _check_fund("014777")
    _check_stock("002714")
    _check_index("sh000300", "沪深300")
    _check_index("hkHSTECH", "恒生科技")


def _check_install():
    try:
        import akshare as ak

        version = getattr(ak, "__version__", "未知版本")
        print(f"[成功] AKShare 已安装，版本：{version}")
        return ak
    except Exception as exc:
        print(f"[失败] {akshare_client.describe_error(exc)}")
        return None


def _check_fund(fund_code):
    try:
        rows = akshare_client.fetch_fund_nav(fund_code)
        latest = rows[-1] if rows else {}
        print(
            f"[成功] 基金 {fund_code} 净值接口可用，返回 {len(rows)} 行，最新日期：{latest.get('nav_date')}"
        )
    except Exception as exc:
        print(f"[失败] 基金 {fund_code} 净值接口不可用：{akshare_client.describe_error(exc)}")


def _check_stock(symbol):
    try:
        rows = akshare_client.fetch_stock_daily(symbol, "20240101")
        latest = rows[-1] if rows else {}
        print(
            f"[成功] 股票 {symbol} 日线接口可用，返回 {len(rows)} 行，最新日期：{latest.get('trade_date')}"
        )
    except Exception as exc:
        print(f"[失败] 股票 {symbol} 日线接口不可用：{akshare_client.describe_error(exc)}")


def _check_index(symbol, name):
    try:
        rows = akshare_client.fetch_index_daily(symbol, "20240101")
        latest = rows[-1] if rows else {}
        print(
            f"[成功] 指数 {name}（{symbol}）接口可用，返回 {len(rows)} 行，最新日期：{latest.get('trade_date')}"
        )
    except Exception as exc:
        print(
            f"[失败] 指数 {name}（{symbol}）接口不可用：{akshare_client.describe_error(exc)}"
        )


if __name__ == "__main__":
    main()
