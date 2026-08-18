import pandas as pd
import streamlit as st

from . import dashboard_charts, dashboard_data


DISCIPLINE_RULES = [
    "不追涨。",
    "不因为一天涨跌频繁交易。",
    "基金补仓结合回撤幅度、持仓收益率和资金安排。",
    "单笔补仓以 20-50 元的小额分批为主，常见 30 元。",
    "股票只做观察提醒，不输出确定性买卖结论。",
    "本项目仅用于个人学习、数据记录和纪律提醒，不构成投资建议。",
]


def set_page(title):
    st.set_page_config(page_title=title, layout="wide")


def render_sidebar():
    st.sidebar.header("投资纪律")
    for rule in DISCIPLINE_RULES:
        st.sidebar.write(f"- {rule}")
    st.sidebar.divider()
    st.sidebar.info("如需更新数据，请手动运行：python scripts/update_daily.py")


def show_result_message(result):
    if not result.ok and result.message:
        st.warning(result.message)
        return True
    return False


def render_overview():
    set_page("投资看板 - 总览")
    render_sidebar()
    st.title("投资数据看板")
    st.caption("本页面只读取本地 CSV 文件账本，不会自动联网更新，也不会写入交易。")

    counts = dashboard_data.get_table_counts()
    if show_result_message(counts):
        return

    logs = dashboard_data.load_update_logs(limit=200)
    asset_statuses = dashboard_data.load_asset_statuses()
    holdings = dashboard_data.load_holdings()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("关注标的数量", counts.data.get("watchlist", 0))
    col2.metric("基金净值行数", counts.data.get("fund_nav", 0))
    col3.metric("股票/指数日线行数", counts.data.get("stock_daily", 0))
    col4.metric("持仓记录数", counts.data.get("portfolio_holding", 0))

    col5, col6, col7 = st.columns(3)
    col5.metric("更新日志行数", counts.data.get("update_log", 0))
    success_count = 0
    failed_count = 0
    if logs.ok and not logs.data.empty:
        success_count = int((logs.data["status"] == "success").sum())
        failed_count = int((logs.data["status"] == "failed").sum())
    col6.metric("成功更新次数", success_count)
    col7.metric("失败更新次数", failed_count)

    st.subheader("最近更新")
    if logs.ok and not logs.data.empty:
        success = logs.data[logs.data["status"] == "success"].head(1)
        failed = logs.data[logs.data["status"] == "failed"].head(1)
        c1, c2 = st.columns(2)
        c1.write("最近一次成功更新")
        c1.dataframe(success, width="stretch", hide_index=True)
        c2.write("最近一次失败更新")
        c2.dataframe(failed, width="stretch", hide_index=True)
        fig = dashboard_charts.status_bar(logs.data)
        if fig:
            st.plotly_chart(fig, width="stretch")
    else:
        st.info("暂无更新日志。需要数据时，请手动运行：python scripts/update_daily.py")

    st.subheader("标的状态分类")
    if asset_statuses.ok:
        status_frame = _status_frame(asset_statuses.data)
        if not status_frame.empty:
            status_counts = status_frame["状态"].value_counts().reset_index()
            status_counts.columns = ["状态", "数量"]
            st.dataframe(status_counts, width="stretch", hide_index=True)
            st.dataframe(status_frame, width="stretch", hide_index=True)
        else:
            st.info("暂无关注标的。")
    elif asset_statuses.message:
        st.warning(asset_statuses.message)

    if holdings.ok and holdings.data.empty:
        st.info("目前还没有录入真实持仓，所以只能看行情，不能判断个人补仓条件。")


def render_fund_page():
    set_page("基金观察")
    render_sidebar()
    st.title("基金观察")

    funds = dashboard_data.load_watchlist(asset_types=["fund"])
    if show_result_message(funds):
        return
    if not funds.data:
        st.info("暂无基金关注标的。")
        return

    selected = st.selectbox("选择基金", funds.data, format_func=_asset_label)
    navs = dashboard_data.load_fund_nav(fund_code=selected["symbol"])
    holdings = dashboard_data.load_holdings()
    if show_result_message(navs):
        return
    if navs.data.empty:
        st.warning("这只基金暂无净值数据。请先运行：python scripts/update_daily.py")
        return

    change_5 = dashboard_data.period_change(navs.data, "unit_nav", 5)
    change_20 = dashboard_data.period_change(navs.data, "unit_nav", 20)
    holding = _matching_holding(holdings.data, selected["symbol"]) if holdings.ok else None
    profit_rate = None if holding is None else holding.get("profit_rate")
    observation = dashboard_data.fund_observation_text(change_20, profit_rate)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("近 5 日涨跌幅", dashboard_data.format_pct(change_5))
    c2.metric("近 20 日涨跌幅", dashboard_data.format_pct(change_20))
    c3.metric("持仓收益率", dashboard_data.format_pct(profit_rate))
    c4.metric("观察提示", observation)

    fig = dashboard_charts.fund_nav_line(navs.data, selected["name"])
    if fig:
        st.plotly_chart(fig, width="stretch")

    with st.expander("最近净值数据"):
        st.dataframe(navs.data.tail(20), width="stretch", hide_index=True)


def render_stock_page():
    set_page("股票指数观察")
    render_sidebar()
    st.title("股票 / 指数观察")

    assets = dashboard_data.load_watchlist(asset_types=["stock", "index"])
    if show_result_message(assets):
        return
    if not assets.data:
        st.info("暂无股票或指数关注标的。")
        return

    selected = st.selectbox("选择股票或指数", assets.data, format_func=_asset_label)
    prices = dashboard_data.load_stock_daily(symbol=selected["symbol"])
    if show_result_message(prices):
        return
    if prices.data.empty:
        st.warning("这个标的暂无日线数据。请先运行：python scripts/update_daily.py")
        return

    change_5 = dashboard_data.period_change(prices.data, "close", 5)
    change_20 = dashboard_data.period_change(prices.data, "close", 20)
    st.metric("观察提醒", dashboard_data.stock_observation_text(change_20))
    c1, c2 = st.columns(2)
    c1.metric("近 5 日涨跌幅", dashboard_data.format_pct(change_5))
    c2.metric("近 20 日涨跌幅", dashboard_data.format_pct(change_20))

    candle = dashboard_charts.stock_candlestick(prices.data, selected["name"])
    if candle:
        st.plotly_chart(candle, width="stretch")
    else:
        close_line = dashboard_charts.stock_close_line(prices.data, selected["name"])
        if close_line:
            st.plotly_chart(close_line, width="stretch")

    volume = dashboard_charts.stock_volume_bar(prices.data, selected["name"])
    if volume:
        st.plotly_chart(volume, width="stretch")
    elif selected.get("asset_type") == "index":
        st.info("当前指数数据源未提供成交量，已仅展示价格走势。")
    else:
        st.info("当前成交量数据不足，暂不展示成交量柱状图。")

    with st.expander("最近日线数据"):
        st.dataframe(prices.data.tail(20), width="stretch", hide_index=True)


def render_holdings_page():
    set_page("持仓页")
    render_sidebar()
    st.title("持仓页")

    holdings = dashboard_data.load_holdings()
    if show_result_message(holdings):
        return
    if holdings.data.empty:
        st.warning("目前还没有录入真实持仓，所以只能看行情，不能判断个人补仓条件。")
        st.info("请先录入持仓数据。")
        return

    total_holding = holdings.data["holding_amount"].fillna(0).sum()
    total_cost = holdings.data["cost_amount"].fillna(0).sum()
    current_return = None if total_cost == 0 else (total_holding - total_cost) / total_cost * 100

    c1, c2, c3 = st.columns(3)
    c1.metric("持仓金额", f"{total_holding:.2f}")
    c2.metric("成本金额", f"{total_cost:.2f}")
    c3.metric("当前收益率", dashboard_data.format_pct(current_return))

    st.dataframe(holdings.data, width="stretch", hide_index=True)
    bar = dashboard_charts.holding_profit_bar(holdings.data)
    pie = dashboard_charts.holding_amount_pie(holdings.data)
    c4, c5 = st.columns(2)
    if bar:
        c4.plotly_chart(bar, width="stretch")
    if pie:
        c5.plotly_chart(pie, width="stretch")


def render_update_log_page():
    set_page("更新日志")
    render_sidebar()
    st.title("更新日志")

    status_label = st.radio("筛选状态", ["全部", "success", "failed"], horizontal=True)
    status = None if status_label == "全部" else status_label
    logs = dashboard_data.load_update_logs(limit=20, status=status)
    if show_result_message(logs):
        return
    if logs.data.empty:
        st.info("暂无匹配的更新日志。需要更新数据时，请手动运行：python scripts/update_daily.py")
        return
    st.dataframe(logs.data, width="stretch", hide_index=True)


def _asset_label(item):
    enabled = "启用" if item.get("enabled") else "未启用"
    return f"{item['name']}（{item['symbol']}，{enabled}）"


def _matching_holding(frame, asset_code):
    if frame is None or frame.empty:
        return None
    matched = frame[frame["asset_code"] == asset_code]
    if matched.empty:
        return None
    return matched.iloc[0].to_dict()


def _status_frame(rows):
    return pd.DataFrame(
        [
            {
                "代码": row["symbol"],
                "名称": row["name"],
                "类型": row["asset_type"],
                "状态": row["status"],
                "原因": row["reason"],
                "价格主图": "可展示" if row["can_show_price"] else "不可展示",
            }
            for row in rows
        ]
    )
