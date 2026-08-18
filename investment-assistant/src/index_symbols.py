from dataclasses import dataclass


@dataclass(frozen=True)
class IndexSymbol:
    display_name: str
    query_symbol: str | None
    interface: str | None
    note: str


INDEX_SYMBOLS = {
    "sh000300": IndexSymbol("沪深300", "000300", "index_zh_a_hist", "已确认：沪深300"),
    "000510": IndexSymbol("中证A500", "000510", "index_zh_a_hist", "已确认：中证A500"),
    "H30007": IndexSymbol("中证芯片", "H30007", "index_zh_a_hist", "已确认：中证芯片产业指数"),
    "H30590": IndexSymbol("机器人指数", "H30590", "index_zh_a_hist", "已确认：中证机器人指数"),
    "HSTECH": IndexSymbol("恒生科技", "HSTECH", "stock_hk_index_daily_sina", "已确认：恒生科技指数"),
    "CSI_A500_PENDING": IndexSymbol("中证A500", "000510", "index_zh_a_hist", "旧 pending 标的；建议迁移为 000510"),
    "HSTECH_PENDING": IndexSymbol("恒生科技", "HSTECH", "stock_hk_index_daily_sina", "旧 pending 标的；建议迁移为 HSTECH"),
    "CSI_CHIP_PENDING": IndexSymbol("中证芯片", "H30007", "index_zh_a_hist", "旧 pending 标的；建议迁移为 H30007"),
    "ROBOT_INDEX_PENDING": IndexSymbol("机器人指数", "H30590", "index_zh_a_hist", "旧 pending 标的；建议迁移为 H30590"),
}


def is_pending_symbol(symbol):
    return str(symbol or "").endswith("_PENDING")


def resolve_index_symbol(symbol):
    return INDEX_SYMBOLS.get(
        symbol,
        IndexSymbol(str(symbol), symbol, "stock_zh_index_daily_tx", "未配置映射，使用旧接口"),
    )
