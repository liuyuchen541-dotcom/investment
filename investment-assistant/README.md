# 个人轻量级投资数据助手

这是一个本地个人投资数据账本和纪律提醒工具。v1 只用于个人学习、数据记录、质量检查和观察报告，不构成投资建议，不自动交易，不连接券商，不下单。

## 当前数据源

项目已经取消运行期 SQLite 依赖。现在的权威数据源是 `CSV + Markdown`：

- `data/ledger/holdings.csv`：个人持仓
- `data/ledger/trades.csv`：手动交易记录
- `data/ledger/watchlist.csv`：关注标的
- `data/market/fund_nav/*.csv`：基金净值缓存
- `data/market/stock_daily/*.csv`：股票和指数日线缓存
- `data/logs/update_log.csv`：更新日志
- `docs/holdings/`：人工可读持仓快照说明

旧 SQLite 文件不会删除。迁移后会归档到：

```text
data/archive/investment_data_*.db
```

如 CSV 迁移异常，可以用归档库重新导出核对。

## 项目边界

- 不修改上一级 `C:\Users\Lenovo\Desktop\投资` 内的原始投资资料。
- 不保存任何账号密码。
- 不接入券商，不自动下单。
- 报告只输出“观察 / 可考虑小额补仓 / 暂不操作”等辅助判断。
- AKShare 接口字段不明确时，停止写入该标的，并把失败原因写入日志。

## 安装

```powershell
cd C:\Users\Lenovo\Desktop\投资\investment-assistant
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 常用命令

初始化文件账本：

```powershell
python scripts\init_db.py
```

更新少量标的：

```powershell
python scripts\update_daily.py --limit 2 --no-sleep
```

更新指定标的：

```powershell
python scripts\update_daily.py --symbols "014777,002714,sh000300" --no-sleep
```

检查数据质量：

```powershell
python scripts\check_quality.py
```

生成观察报告：

```powershell
python scripts\generate_report.py
```

手动新增或更新一条持仓：

```powershell
python scripts\add_holding.py --asset-code 014777 --asset-name "富国中证芯片产业 ETF 联接 C" --asset-type fund --holding-amount 100 --cost-amount 120 --profit-rate -1.5 --note "手动测试"
```

运行测试：

```powershell
python -m unittest discover -s tests -v
```

## 文件字段

`holdings.csv`

- `asset_code`
- `asset_name`
- `asset_type`
- `holding_amount`
- `cost_amount`
- `profit_rate`
- `updated_at`
- `note`

`trades.csv`

- `asset_code`
- `asset_name`
- `action`
- `amount`
- `trade_date`
- `reason`
- `created_at`

`watchlist.csv`

- `symbol`
- `name`
- `asset_type`
- `data_source`
- `enabled`
- `note`

## Windows 任务计划程序示例

v1 不自动替你创建系统任务。可以手动创建一个每天收盘后运行的任务：

1. 打开“任务计划程序”。
2. 选择“创建基本任务”。
3. 触发器选择“每天”，时间可设为 16:30 或 17:00。
4. 操作选择“启动程序”。
5. 程序填写 Python 路径，例如：

```text
C:\Users\Lenovo\Desktop\投资\investment-assistant\.venv\Scripts\python.exe
```

6. 参数填写：

```text
scripts\update_daily.py --limit 2
```

7. 起始于填写：

```text
C:\Users\Lenovo\Desktop\投资\investment-assistant
```

第一次建议保留 `--limit 2`，确认稳定后再扩大更新范围。

## AKShare 说明

项目主要使用 AKShare 获取公开行情和基金净值。AKShare 接口可能变化；如果返回字段缺失、接口空表或网络失败，脚本会记录失败原因并继续处理下一个标的，不会强行写入含义不明的数据。

## 后续扩展方向

- 把观察报告另存为 Markdown 文件。
- 增加更清晰的图表或本地看板。
- 为指数接口逐个确认代码口径。
- 细化补仓观察区规则，但继续保持“不自动交易、不输出绝对买卖建议”的边界。
