import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def _has_columns(frame, columns):
    return frame is not None and not frame.empty and all(column in frame for column in columns)


def fund_nav_line(frame, title):
    if not _has_columns(frame, ["date", "unit_nav"]):
        return None
    fig = px.line(frame, x="date", y="unit_nav", title=f"{title} 单位净值走势")
    fig.update_layout(xaxis_title="日期", yaxis_title="单位净值", hovermode="x unified")
    return fig


def stock_close_line(frame, title):
    if not _has_columns(frame, ["date", "close"]):
        return None
    fig = px.line(frame, x="date", y="close", title=f"{title} 收盘价走势")
    fig.update_layout(xaxis_title="日期", yaxis_title="收盘价", hovermode="x unified")
    return fig


def stock_candlestick(frame, title):
    required = ["date", "open", "high", "low", "close"]
    if not _has_columns(frame, required):
        return None
    clean = frame.dropna(subset=required)
    if clean.empty:
        return None
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=clean["date"],
                open=clean["open"],
                high=clean["high"],
                low=clean["low"],
                close=clean["close"],
                name=title,
            )
        ]
    )
    fig.update_layout(title=f"{title} K线图", xaxis_title="日期", yaxis_title="价格", xaxis_rangeslider_visible=False)
    return fig


def stock_volume_bar(frame, title):
    if not _has_columns(frame, ["date", "volume"]):
        return None
    clean = frame.dropna(subset=["volume"])
    if clean.empty:
        return None
    fig = px.bar(clean, x="date", y="volume", title=f"{title} 成交量")
    fig.update_layout(xaxis_title="日期", yaxis_title="成交量")
    return fig


def holding_profit_bar(frame):
    if not _has_columns(frame, ["asset_name", "profit_rate"]):
        return None
    clean = frame.dropna(subset=["profit_rate"]).sort_values("profit_rate")
    if clean.empty:
        return None
    fig = px.bar(clean, x="asset_name", y="profit_rate", title="持仓收益率排序")
    fig.update_layout(xaxis_title="标的", yaxis_title="收益率(%)")
    return fig


def holding_amount_pie(frame):
    if not _has_columns(frame, ["asset_name", "holding_amount"]):
        return None
    clean = frame.dropna(subset=["holding_amount"])
    clean = clean[clean["holding_amount"] > 0]
    if clean.empty:
        return None
    return px.pie(clean, names="asset_name", values="holding_amount", title="持仓金额占比")


def status_bar(frame):
    if frame is None or frame.empty or "status" not in frame:
        return None
    counts = frame["status"].value_counts().reset_index()
    counts.columns = ["status", "count"]
    fig = px.bar(counts, x="status", y="count", title="更新状态统计")
    fig.update_layout(xaxis_title="状态", yaxis_title="次数")
    return fig
