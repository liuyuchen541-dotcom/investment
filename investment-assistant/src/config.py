from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
DB_PATH = DATA_DIR / "investment_data.db"  # Legacy SQLite source/backup path only.
LEDGER_DIR = DATA_DIR / "ledger"
MARKET_DIR = DATA_DIR / "market"
FUND_NAV_DIR = MARKET_DIR / "fund_nav"
STOCK_DAILY_DIR = MARKET_DIR / "stock_daily"
LOG_DIR = DATA_DIR / "logs"
ARCHIVE_DIR = DATA_DIR / "archive"
CONTEXT_DIR = PROJECT_ROOT / "docs" / "context"

DEFAULT_START_DATE = "20240101"
REQUEST_SLEEP_SECONDS = 1.0


DEFAULT_WATCHLIST = [
    {
        "symbol": "014777",
        "name": "富国中证芯片产业 ETF 联接 C",
        "asset_type": "fund",
        "data_source": "akshare",
        "enabled": 1,
        "note": "支付宝基金；开放式基金净值",
    },
    {
        "symbol": "014881",
        "name": "天弘中证机器人 ETF 联接 C",
        "asset_type": "fund",
        "data_source": "akshare",
        "enabled": 1,
        "note": "支付宝基金；开放式基金净值",
    },
    {
        "symbol": "011840",
        "name": "天弘中证人工智能主题指数 C",
        "asset_type": "fund",
        "data_source": "akshare",
        "enabled": 1,
        "note": "支付宝基金；开放式基金净值",
    },
    {
        "symbol": "013309",
        "name": "易方达恒生科技 ETF 联接(QDII) C",
        "asset_type": "fund",
        "data_source": "akshare",
        "enabled": 1,
        "note": "支付宝基金；开放式基金净值",
    },
    {
        "symbol": "025857",
        "name": "华夏中证电网设备主题 ETF 联接 C",
        "asset_type": "fund",
        "data_source": "akshare",
        "enabled": 1,
        "note": "支付宝基金；开放式基金净值",
    },
    {
        "symbol": "023037",
        "name": "中欧资源精选混合 C",
        "asset_type": "fund",
        "data_source": "akshare",
        "enabled": 1,
        "note": "支付宝基金；开放式基金净值",
    },
    {
        "symbol": "022460",
        "name": "易方达中证 A500 ETF 联接 C",
        "asset_type": "fund",
        "data_source": "akshare",
        "enabled": 1,
        "note": "支付宝基金；开放式基金净值",
    },
    {
        "symbol": "002714",
        "name": "牧原股份",
        "asset_type": "stock",
        "data_source": "akshare",
        "enabled": 1,
        "note": "A 股股票；默认前复权 qfq",
    },
    {
        "symbol": "sh000300",
        "name": "沪深300",
        "asset_type": "index",
        "data_source": "akshare",
        "enabled": 1,
        "note": "已确认：AKShare index_zh_a_hist 查询代码 000300",
    },
    {
        "symbol": "000510",
        "name": "中证A500",
        "asset_type": "index",
        "data_source": "akshare",
        "enabled": 1,
        "note": "已确认：AKShare index_zh_a_hist 查询代码 000510",
    },
    {
        "symbol": "HSTECH",
        "name": "恒生科技",
        "asset_type": "index",
        "data_source": "akshare",
        "enabled": 1,
        "note": "已确认：AKShare stock_hk_index_daily_sina 查询代码 HSTECH",
    },
    {
        "symbol": "H30007",
        "name": "中证芯片产业指数",
        "asset_type": "index",
        "data_source": "akshare",
        "enabled": 1,
        "note": "已确认：AKShare index_zh_a_hist 查询代码 H30007",
    },
    {
        "symbol": "H30590",
        "name": "中证机器人指数",
        "asset_type": "index",
        "data_source": "akshare",
        "enabled": 1,
        "note": "已确认：AKShare index_zh_a_hist 查询代码 H30590",
    },
]
