from . import config, db


def generate_report(db_path=None):
    path = db_path or config.DATA_DIR
    db.initialize_database(path)
    watchlist = db.fetch_watchlist(path)
    logs = db.fetch_recent_logs(path, limit=30)
    latest_logs = _latest_log_by_symbol(logs)
    lines = [
        "个人投资数据助手观察报告",
        "=" * 24,
        "说明：本报告仅用于个人学习、数据记录和纪律提醒，不构成投资建议。",
        "",
        "一、最近更新日志",
    ]

    if logs:
        for log in logs[:5]:
            lines.append(
                f"- {log.get('finished_at')} {log.get('task_name')}：{log.get('status')}：{log.get('message')}"
            )
    else:
        lines.append("- 暂无更新日志。")

    success_logs = [log for log in latest_logs.values() if log.get("status") == "success"]
    failed_logs = [log for log in latest_logs.values() if log.get("status") == "failed"]
    lines.extend(["", "二、更新完整性"])
    if failed_logs:
        lines.append("提示：当前只有部分数据更新成功，下面不是完整市场报告。")

    lines.append("成功更新的标的：")
    if success_logs:
        for log in success_logs:
            lines.append(f"- {_log_label(log)}：{log.get('message')}")
    else:
        lines.append("- 暂无成功更新记录。")

    lines.append("更新失败的标的：")
    if failed_logs:
        for log in failed_logs:
            lines.append(f"- {_log_label(log)}：{_short_reason(log.get('message', ''))}")
    else:
        lines.append("- 暂无失败更新记录。")

    lines.extend(["", "三、标的观察"])
    visible_count = 0
    insufficient = []
    for item in watchlist:
        points = _load_price_points(path, item)
        if len(points) < 2:
            insufficient.append(item)
            continue
        visible_count += 1
        change_5 = _period_change(points, 5)
        change_20 = _period_change(points, 20)
        advice = _observation_text(change_20 if change_20 is not None else change_5)
        lines.append(
            "- {name}（{symbol}）：近5日 {c5}，近20日 {c20}，提示：{advice}".format(
                name=item["name"],
                symbol=item["symbol"],
                c5=_format_pct(change_5),
                c20=_format_pct(change_20),
                advice=advice,
            )
        )
    if visible_count == 0:
        lines.append("- 暂无可分析行情数据。请先运行更新脚本。")

    lines.append("")
    lines.append("数据不足的标的：")
    if insufficient:
        for item in insufficient:
            status_note = "未启用自动更新" if not item["enabled"] else "暂无足够行情/净值数据"
            lines.append(f"- {item['name']}（{item['symbol']}）：{status_note}")
    else:
        lines.append("- 暂无。")

    lines.extend(["", "四、持仓观察"])
    holdings = db.fetch_holdings(path)
    if holdings:
        for holding in holdings:
            rate = holding.get("profit_rate")
            if rate is None:
                note = "缺少收益率，先补充持仓数据。"
            elif rate <= -5:
                note = "进入亏损观察区，可结合规则考虑小额补仓。"
            else:
                note = "继续观察，避免因为单日波动频繁操作。"
            lines.append(f"- {holding['asset_name']}：{note}")
    else:
        lines.append("- 暂无手动持仓记录。")

    lines.extend(
        [
            "",
            "五、纪律提醒",
            "- 不追涨，不因为一天涨跌就频繁交易。",
            "- 基金资金池和牧原股份股票资金池分开看。",
            "- 单笔补仓以 20-50 元的小额分批为主，常见 30 元。",
        ]
    )
    return "\n".join(lines)


def _load_price_points(db_path, item):
    if item["asset_type"] == "fund":
        return db.fetch_fund_navs(db_path, item["symbol"], limit=25)
    if item["asset_type"] in {"stock", "index"}:
        return db.fetch_stock_prices(db_path, item["symbol"], limit=25)
    return []


def _period_change(points, days):
    if len(points) < 2:
        return None
    start_index = max(0, len(points) - days)
    start = points[start_index]["value"]
    end = points[-1]["value"]
    if start in (None, 0) or end is None:
        return None
    return (end - start) / start * 100


def _format_pct(value):
    if value is None:
        return "数据不足"
    return f"{value:.2f}%"


def _observation_text(change):
    if change is None:
        return "观察，数据还不够。"
    if change <= -5:
        return "可考虑小额补仓，但需要结合估值、持仓和当天市场。"
    if change >= 8:
        return "暂不操作，避免追涨。"
    return "观察，暂不操作。"


def _latest_log_by_symbol(logs):
    latest = {}
    for log in logs:
        symbol = _symbol_from_task(log.get("task_name", ""))
        if symbol and symbol not in latest:
            latest[symbol] = log
    return latest


def _symbol_from_task(task_name):
    parts = task_name.split(" ", 3)
    if len(parts) >= 3 and parts[0] == "update":
        return parts[2]
    return None


def _log_label(log):
    parts = log.get("task_name", "").split(" ", 3)
    if len(parts) >= 4:
        return f"{parts[3]}（{parts[2]}）"
    return log.get("task_name", "")


def _short_reason(message):
    if len(message) <= 120:
        return message
    return message[:117] + "..."
