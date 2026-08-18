# Findings & Decisions

## Requirements
- User wants a deep multi-agent analysis to find quality assets matching their investment philosophy.
- Universe can include stocks and funds; A-share exposure is preferred.
- Output should be practical but should not become an unconditional trade order.

## Local Philosophy Extract
- Long-term investing over speculation.
- Value and fundamentals before short-term price movement.
- User is a long-term net buyer and prefers small-batch execution.
- If an individual company is not clearly understood, prefer ETF/fund exposure.
- Broad low-cost index funds should become a core long-term base.
- Good company still needs a good or at least reasonable price.
- High dividend assets require sustainable cash flow; high yield alone can be a trap.
- User's current fund workflow should account for Alipay Fund conventions and the 15:00 cutoff.

## Research Findings
- 中证A500 official factsheet shows a broad 500-stock index covering representative companies across A-share industries; 2026-05-29 factsheet PE was 16.79 and 2025 return was 22.43%.
- 沪深300 remains the large-cap core broad index; public valuation pages around 2026-07-02 show PE roughly in the mid-teens and dividend yield around 2%-3%, so it is not a panic-price asset.
- 红利低波/红利低波100 fits the user's cash-flow and low-volatility preference better than chasing single high-dividend stocks, but it still contains cyclical and financial exposure and cannot be treated as risk-free.
- 中证芯片产业 and 中证人工智能 theme factsheets show very strong recent returns and high PE levels; this supports "hold existing low-cost positions, do not chase new highs."
- 机器人 and 电网 equipment valuation evidence also points to high volatility or high valuation percentiles; they should remain satellite/watchlist directions rather than core new money.
- Stable quality examples such as 伊利股份、双汇发展、美的集团、贵州茅台 now look more reasonable than in prior consumer-stock bubbles, but each has industry-specific risks and still requires business-level understanding.
- Parallel fund/ETF research favored 中证A500/沪深300 plus 红利低波 as the main fund-side structure; consumer and healthcare ETFs are optional small satellites.
- Parallel dividend/value research found no current "8% yield + sustainable dividend + crisis mispricing" signal. 中国移动 is the cleanest high-dividend individual-stock research candidate; 宝钢 and coal names need value-trap/cycle checks.
- Parallel stable-quality research favored 伊利、双汇、美的、茅台 as understandable businesses, but emphasized growth slowdown and valuation discipline.
- Parallel tech-growth research confirmed chips/AI/grid/robotics are long-term themes, but high valuation and recent heat mean "hold existing low-cost exposure and wait for pullbacks" rather than chase.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Use multi-agent research by asset sleeve | The fund, dividend, stable-quality, and technology-growth questions are independent enough to investigate in parallel. |

## Multi-Agent Outcome (2026-07-13)
- Four parallel agents were launched for index funds, dividend stocks, durable compounders, and portfolio red-team review.
- All four reached the account usage limit before returning a usable report. No incomplete agent output is used as evidence.
- The main analysis completed the same four tracks and verified the final shortlist against dated index factsheets, fund disclosures, exchange filings, and issuer reports.

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| Agent Reach health check did not return within 30 seconds | Continue with browser/public-data workflow and record the limitation. |

## Resources
- Local context: C:\Users\Lenovo\Desktop\投资\投资理念.md
- Local context: C:\Users\Lenovo\Desktop\投资\投资总框架.md
- Local context: C:\Users\Lenovo\Desktop\投资\基金\基金投资上下文.md
- Local context: C:\Users\Lenovo\Desktop\投资\基金\宽基指数投资理念.md
- Local context: C:\Users\Lenovo\Desktop\投资\股票\股票通用方法论.md
- Local context: C:\Users\Lenovo\Desktop\投资\股票\高股息资产投资理念.md
- CSI A500 factsheet: https://oss-ch.csindex.com.cn/static/html/csindex/public/uploads/indices/detail/files/zh_CN/000510factsheet.pdf
- CSI 红利低波100 factsheet: https://oss-ch.csindex.com.cn/static/html/csindex/public/uploads/indices/detail/files/zh_CN/930955factsheet.pdf
- 易方达中证A500ETF联接A/C product pages: https://www.efunds.com.cn/Mobile/fund/022459.shtml and https://www.efunds.com.cn/Mobile/fund/022460.shtml
- 易方达沪深300ETF联接C product page: https://www.efunds.com.cn/Mobile/fund/007339.shtml
- 中证芯片产业 factsheet: https://oss-ch.csindex.com.cn/static/html/csindex/public/uploads/indices/detail/files/zh_CN/H30007factsheet.pdf
- 中证人工智能主题 factsheet: https://oss-ch.csindex.com.cn/static/html/csindex/public/uploads/indices/detail/files/zh_CN/930713factsheet.pdf
- 牧原股份 2026 Q1 report: https://static.cninfo.com.cn/finalpage/2026-04-22/1225136604.PDF
- 中国移动 2025 annual report/HKEX source: https://www.hkexnews.hk/listedco/listconews/sehk/2026/0326/2026032602020_c.pdf
- 中国移动 valuation/data source: https://data.eastmoney.com/gzfx/detail/600941.html

## Visual/Browser Findings
- Pending external market research.

## 2026-07-13 Refresh Notes
- The prior 2026-07-02 screen is useful as a hypothesis set, but all market-sensitive claims must be refreshed before reuse.
- Canonical local inputs currently include general philosophy, total framework, fund context, broad-index philosophy, stock methodology, high-dividend methodology, gold philosophy, and a separate Muyuan position context.
- The Alipay Fund workflow remains a material execution constraint: small mutual-fund buys, the 15:00 trading-day cutoff, and final platform confirmation of NAV, fees, and settled amounts.
- The final screen must evaluate portfolio fit and overlap, not only standalone asset quality; the user's existing technology exposure makes another high-beta technology candidate a higher hurdle.
- Agent Reach's local health check timed out and the documented Exa MCP server is not installed in the current environment. Live verification therefore uses public web retrieval with primary-source preference; this is a retrieval limitation, not evidence for or against any asset.
- Current local records show meaningful existing exposure to chips, AI, robotics, Hang Seng technology, and power-grid equipment, plus a separate 200-share Muyuan position. New "quality asset" candidates should therefore improve diversification rather than add another technology story.
- The current recurring-plan record is 70 yuan/week in 022459 (A500 linked A), 30 yuan/week in 021550 (dividend low-volatility 100 linked A), plus small recurring S&P 500 and Nasdaq-100 contributions. These planned deductions are not treated as completed holdings until Alipay confirms them.

## Screening Scorecard
- Business or index durability: 25 points.
- Financial quality and cash conversion: 20 points.
- Valuation and margin of safety: 20 points.
- Portfolio diversification and overlap: 15 points.
- Shareholder return and dividend sustainability: 10 points.
- Product cost, tracking, liquidity, and execution fit: 10 points.

## Live Fund Evidence (2026-07-13 Review)
- The CSI A500 official factsheet dated 2026-05-29 showed 500 constituents, PE 16.79, dividend yield 1.94%, one-year return 35.45%, and broad industry representation. More recent public valuation snapshots put market-cap-weighted PE around 17-18x, so it is not a distress valuation.
- A500 still contains meaningful technology/communications exposure: the May factsheet showed about 22.3% information technology and 11.8% communications, with names such as Cambricon, Luxshare, Eoptolink, CATL, and InnoLight among major constituents. It diversifies single-theme risk but does not eliminate technology exposure.
- The CSI Dividend Low Volatility 100 official factsheet dated 2026-05-29 showed PE 8.68 and dividend yield 5.18%. A 2026-07-09 public snapshot showed PE about 8.23 and indicated a recent drawdown, supporting a cheaper defensive role rather than a momentum thesis.
- Dividend Low Volatility 100 is not bond-like: its official factsheet showed substantial energy, industrial, consumer, financial, and communications exposure, including cyclical names. Low volatility and high historical dividend do not guarantee stable future payouts.
- 022459 had about 4.582 billion total fund shares at 2026-Q1 end; the A class held about 2.421 billion shares. Its product summary states at least 90% target-ETF exposure, 0.15% management fee, 0.05% custody fee, and no redemption fee after seven days under the disclosed schedule.
- 021550 is a 1-yuan-minimum open-ended linked fund. Bosera's current product page shows 0.15% management fee, 0.05% custody fee, 0% sales-service fee for A shares, and at least 90% target-ETF exposure. The page also labels it medium-high risk and shows repeated cash distributions, which should not be mistaken for guaranteed yield.
- 021550's 2026-Q1 report listed about 1.546 billion total fund shares; a regulator-sourced public fund record showed total assets around RMB 1.529bn at 2026-03-31. The product is not too small for the user's purpose, while still materially smaller than 022459.
- The latest official CSI 300 factsheet reviewed (2026-05-29) showed PE 14.62, dividend yield 2.32%, and a one-year return of 27.39%. It has a longer live history and a somewhat cheaper valuation than A500, but its top names and major sector exposures overlap heavily with A500.
- Holding both A500 and CSI 300 as co-equal domestic cores would add complexity without much diversification. Because the user already has an A500 recurring plan, CSI 300 is a substitute or future style switch, not an additional required fund.

## Live Stock Triage (2026-07-13 Market Snapshot)
- A live Eastmoney quote snapshot was used only for approximate price and valuation triage; dividend fields from that endpoint were internally inconsistent and are excluded from the evidence set.
- Approximate TTM PE at the snapshot: Midea 13.6x, China Mobile 14.4x, Yili 13.0x, Gree 7.3x, Yangtze Power 19.0x, Kweichow Moutai 18.2x, Fuyao 14.7x, Mindray 21.9x, Haier Smart Home 10.2x, and Wanhua 16.3x. These are screening values, not final normalized valuations.
- Trading-lot affordability is a decisive user-fit constraint. At the same snapshot, one A-share lot cost roughly RMB 7,900 for Midea, RMB 9,000 for China Mobile, RMB 2,500 for Yili, RMB 2,000 for Haier, and over RMB 120,000 for Kweichow Moutai. Direct ownership can conflict with the user's small-batch and cash-reserve discipline even when the business is attractive.
- Midea's 2025 annual report states revenue of RMB 458.5 billion and attributable net profit of RMB 43.95 billion, both growing at double-digit rates, with overseas revenue of RMB 195.9 billion and ToB revenue of RMB 122.8 billion. This supports a diversified durable-compounder thesis, but the global acquisition footprint adds integration and currency risk.
- Haier's 2026-Q1 official report showed revenue down 6.86%, attributable profit down 15.22%, and operating cash flow down 29.46% year over year. Its low headline valuation therefore requires a business-slowdown check rather than automatic bargain classification.

## Primary-Report Stock Evidence
- Midea 2025: attributable profit RMB 43.95bn, operating cash flow RMB 53.35bn, weighted ROE 19.70%, and total announced 2025 cash dividend RMB 4.30/share. Cash generation covered both profit and the proposed payout. However, 2026-Q1 revenue grew 2.55% and headline profit 2.03% while ex-special-item profit fell 14.02%; the quality case remains intact but near-term earnings quality is not uniformly improving.
- China Mobile 2025: revenue RMB 1,050.2bn, net profit RMB 137.1bn, total dividend HKD 5.27/share, and payout ratio 75%. At an A-share price near RMB 90, the gross indicated yield is roughly 5% after currency conversion, not an 8% crisis yield. 2026-Q1 attributable profit fell 4.2%, while the official quarterly filing showed operating cash flow materially above capital expenditure. It is a stable cash-flow research candidate, but tax/regulatory pressure and capital intensity remain material.
- Yili 2025: revenue RMB 115.64bn (+0.21%), attributable profit RMB 11.57bn (+36.82%), ex-special-item profit RMB 11.07bn, operating cash flow RMB 14.34bn (-34.02%), ROE 20.87%, and total 2025 cash distributions RMB 8.73bn (75.48% of profit, about RMB 1.38/share). The payout was covered by annual operating cash flow, but the flat revenue and weaker annual cash flow prevent treating the low valuation as a free bargain.
- Yili 2026-Q1: revenue +5.47%, attributable profit +10.68%, ex-special-item profit +15.11%, and operating cash flow RMB 3.73bn versus RMB 0.95bn a year earlier. This is an encouraging rebound, not yet proof of a new long-term growth regime.
- Midea, China Mobile, and Yili pass the first quality screen, but all are already represented in broad or dividend indices. Direct purchase would create single-name concentration and should require a clear reason to prefer that company over the fund basket.
- Gree, CNOOC, Shenhua, and Wanhua remain value/cycle-sensitive candidates rather than stable-compounder defaults. Yangtze Power remains high quality but its current valuation does not provide the same income margin. Haier is on hold pending evidence that the 2026-Q1 decline is temporary.

## Veto Criteria
- The investment case depends mainly on a popular narrative the user cannot independently explain.
- Reported profit is persistently unsupported by operating/free cash flow, or leverage threatens the thesis.
- A high dividend is funded by debt, peak-cycle earnings, or an unsustainable payout.
- A low PE is mainly the result of cyclical peak earnings rather than durable earning power.
- Valuation requires an optimistic growth path with little room for disappointment.
- A fund adds substantial exposure already present in chips, AI, robotics, or Hang Seng technology without a clear portfolio role.
- Product fees, tracking quality, scale, or purchase constraints are poor relative to a close substitute.
- The 15x PE, 5% yield, and crisis-only 8% yield levels are research references, not automatic buy triggers.

## Final Narrowed Pool
- Executable domestic core: 022459 易方达中证A500ETF联接A. It fits the low-cost broad-index role, but the current valuation and technology weight support regular small contributions rather than a large one-time purchase.
- Executable defensive complement: 021550 博时中证红利低波动100ETF联接A. Its valuation and historical dividend yield are more defensive, while its cyclical/energy exposure prevents treating it as a cash substitute.
- The existing 70/30 A500/dividend-low-volatility recurring split is reasonable. If the user wants a materially more defensive domestic sleeve, 60/40 is the nearest simple alternative; adding CSI 300 is unnecessary.
- Individual-stock research list only: Midea first for overall business quality, China Mobile first for cash-flow/dividend character, and Yili first for understandability and trading-lot affordability. None is a necessary immediate purchase while the user is still using small recurring amounts.
- Hold/watch rather than add: Haier, Gree, Yangtze Power, CNOOC, Shenhua, Wanhua, Moutai, China Merchants Bank, and InnoLight. Reasons include current earnings pressure, cycle/value-trap risk, valuation, trading-lot size, business-understanding burden, or overlap with existing technology exposure.
- Muyuan remains in its separate dedicated position pool and is not counted as a new generic quality-asset allocation.

## New Research: RMB 30,000 For A Student In Melbourne (2026-07-13)

### Assumptions To Surface
- The user is newly arrived in Melbourne and has AUD-denominated future expenses, but explicitly confirmed that this RMB 30,000 is fully discretionary and does not affect living costs.
- The funds can therefore be treated as long-term marginal capital rather than emergency liquidity; the AUD allocation is for currency diversification and attractive cash yield, not necessity.
- The user's observed AUD 5 charge is confirmed by the current BOC Australia schedule as the receiving fee for an AUD Overseas Student Account; it still does not represent the complete cost because FX spread, outbound, or intermediary charges can be larger.

### Required Evidence
- Current CBA introductory and conditional savings rates and their exact duration/conditions.
- Current Bank of China Australia savings and term-deposit rates, liquidity, and receiving fees.
- Australian deposit-protection and interest-tax rules relevant to an international student.
- China individual FX quota and outward-remittance documentation rules.
- A dated AUD/CNY reference plus an executable staged-transfer calculation.

### Verified Australian Cash Evidence
- CommBank NetBank Saver currently advertises 5.20% p.a. variable for the first five months of a customer's first NetBank Saver, not six months. It comprises a 2.10% standard variable rate plus a fixed 3.10% bonus margin. There are no monthly deposit conditions and the savings account has no monthly fee, but an eligible linked transaction account is required and may have fees.
- After the introductory period, the current NetBank Saver standard variable rate is 2.10% p.a.; the rate itself remains variable.
- CommBank GoalSaver currently advertises 5.00% p.a., comprising 0.25% standard plus 4.75% bonus. To qualify in a calendar month, the customer must make at least one deposit and finish the month with a higher balance than at the start; otherwise only 0.25% applies.
- APRA's Financial Claims Scheme protects eligible Australian-dollar deposits up to AUD 250,000 per account holder per locally incorporated ADI. APRA's list dated 1 July 2026 includes both Commonwealth Bank of Australia and Bank of China (Australia) Limited. Citizenship or residency does not remove coverage, but foreign-currency deposits are not covered.
- Bank of China Australia's latest deposit-rate page found is effective 7 May 2026. Its 5.35% p.a. new-customer Online Saver offer required account opening/debit-card activation by 30 June 2026 and a daily AUD 3,000-499,999.99 balance for three months; it cannot be assumed available to a new applicant on 13 July 2026.
- Outside that expired promotion, BOC Australia's Online Saver rate shown for AUD 3,000+ is 2.10% p.a. The same rate page lists term-deposit rates for AUD 5,000-29,999.99 of 4.30% for three months, 4.50% for six or nine months, 5.25% for 11 months, and 5.00% for 12 months. These rates must still be confirmed at placement because the page is dated 7 May and deposit rates can change.
- BOC Australia's personal Online Saver has no account-keeping fee according to its current target-market document.
- BOC Australia's current fee schedule effective 31 March 2026 confirms an AUD 5 inward telegraphic-transfer fee for an AUD-denominated Overseas Student Account. Other customer accounts are generally charged AUD 10. Overseas/intermediary-bank fees may still be additional, so the user's pre-submit and final receipt remain the controlling all-in evidence.
- The same current schedule lists personal internet/mobile-banking domestic funds transfers as free. The practical route is therefore BOC China to the user's BOC Australia AUD Overseas Student Account, then a free domestic transfer to CBA.
- CommBank Smart Access normally charges AUD 4 per month, but the fee is waived for customers under 30 or when at least AUD 2,000 is deposited in the calendar month, among other criteria. A newly arrived migrant application may also receive a first-year waiver. Because the linked transaction-account fee can materially reduce interest on a roughly AUD 3,000 balance, the user must confirm the app shows a zero monthly fee.
- The user confirmed that the RMB 30,000 is genuinely free capital and does not affect living costs. The final recommendation can therefore use the fully funded reserve scenario, while retaining an AUD cash allocation for currency diversification and future AUD liabilities.

### Verified China FX And Remittance Evidence
- SAFE's 2026 guidance confirms an annual personal convenient FX-purchase quota of USD 50,000 equivalent. This is a purchase quota, not a simple statement that every transfer is unrestricted.
- For a domestic individual's foreign-currency savings account, current-account remittances abroad up to USD 50,000 equivalent in a day generally require identity documents; above that amount, banks require identity plus transaction-amount evidence. Banks must verify that the stated FX-purchase purpose and payment purpose are consistent.
- Genuine overseas-study tuition and living costs can be handled within the annual quota with identity documents; amounts above the convenient quota may be handled against genuine supporting documents. The user must not make a false purpose declaration.
- Official BOC material warns that convenient-quota FX purchases must not be used for unapproved overseas securities investment. The final plan must therefore keep remitted money in AUD deposit/living-liquidity use and keep stock/fund investing in the user's existing lawful domestic channels.
- RMB 30,000 is far below the regulatory USD 50,000-equivalent thresholds. A separate BOC mobile-banking transaction/security limit may still apply; no current authoritative public personal-channel limit was found, so the exact app limit must be confirmed in the user's own transfer screen or with 95566.
- BOC's published general tariff historically lists ordinary telegraphic-transfer charges as 0.1% with a RMB 50 minimum plus a separate cable fee, while group-transfer promotions and customer-specific fee waivers can differ. The user's own pre-submit quote is the controlling evidence; AUD 5 alone is not enough to estimate total cost.

### Exchange-Rate And Tax Evidence
- The RBA's latest available reference on 10 July 2026 was 1 AUD = CNY 4.7111. At that non-commercial midpoint, RMB 30,000 equals about AUD 6,367.93 before bank spread and fees.
- A 1% exchange-rate move on RMB 30,000 is RMB 300, comparable with several months of deposit interest. Currency exposure therefore dominates the advertised rate difference over short periods.
- ATO guidance says an overseas student enrolled in a course lasting six months or more may be an Australian resident for tax purposes. Tax residency is separate from visa status.
- Australian tax residents generally declare Australian bank interest. A resident can benefit from the AUD 18,200 tax-free threshold, subject to part-year and other-income effects. A temporary resident who is also an Australian tax resident still declares Australian interest, while special rules can exclude much foreign income.
- The user should determine tax residency and provide/update TFN or foreign-resident details correctly with the bank. The plan must quote gross interest and avoid assuming a zero tax rate.
- BOC China's published AUD spot selling rate on 10 July 2026 was CNY 473.47 per AUD 100, or CNY 4.7347 per AUD. Against the RBA reference of 4.7111, the retail purchase rate embedded a spread of about 0.50% before transfer charges.
- At the BOC selling rate, RMB 30,000 buys approximately AUD 6,336.20 before charges. If the user's only additional deduction really is AUD 5, net receipt would be about AUD 6,331.20, roughly 0.58% below the RBA midpoint amount.
- For a RMB 15,000 transfer at the same rate, gross AUD would be about 3,168.10 and about 3,163.10 after a single AUD 5 deduction. The fixed fee is small enough for one transfer, but repeated small transfers would unnecessarily raise the percentage cost.
- A current BOC China retail-deposit benchmark could not be reliably isolated from overseas BOC branch pages. Recent mainland BOC structured-deposit maturities found ranged roughly 1.45%-2.02%, but those are product-specific and not a valid universal domestic comparison; no broad domestic return assumption will be used in the final calculation.

### Recommended Marginal Allocation For The RMB 30,000
- Default allocation: RMB 15,000 equivalent (50%) to AUD high-interest cash, RMB 12,000 (40%) to diversified domestic index-fund contributions, and RMB 3,000 (10%) as an individual-stock opportunity reserve rather than an immediate order.
- The AUD half creates currency diversification and matches future AUD liabilities without converting the entire portfolio at one exchange rate. One transfer is preferred because a second small transfer duplicates fixed charges.
- For the AUD cash, use an active BOC Australia 5.35% promotion only if the user's own account was opened/activated by the expired 30 June deadline and the app confirms the promo. Otherwise, use an eligible first CBA NetBank Saver at 5.20% for the remaining five-month introductory period, then reassess or move to GoalSaver if its bonus rate and conditions remain competitive.
- On approximately AUD 3,163.10 net after the example BOC retail rate and AUD 5 deduction, simple gross interest is about AUD 68.53 for five months at 5.20%. If rates stayed at 5.20% for five months and 5.00% for seven months, illustrative 12-month gross interest would be about AUD 160.79, around RMB 757.50 at the RBA reference rate. This is illustrative, variable, and before tax.
- The extra 0.25 percentage point between a hypothetical 5.25% locked term deposit and a 5.00% flexible account is only about AUD 8 per year on AUD 3,163; it is not enough compensation for an 11-month lock for this user.
- Deploy the RMB 12,000 fund sleeve over 48 weeks at RMB 250 per week: RMB 175 to 022459 A500 linked A and RMB 75 to 021550 dividend-low-volatility 100 linked A. This preserves the existing 70/30 structure and avoids a lump sum after a strong A500 period.
- Hold the RMB 3,000 stock reserve in a liquid RMB cash product. Do not buy merely to fill the allocation; the maximum single-stock allocation is 10% of this new-money sleeve. Yili is the only prior research candidate near the intended lot size, but earlier fundamental review still called for more evidence of durable recovery.

### Final Execution Checklist
- Confirm in the CBA app that the NetBank Saver rate is 5.20%, determine how much of the five-month window remains from the original opening date, and verify the linked Smart Access monthly fee is AUD 0.
- In BOC China, enter a single RMB 15,000 AUD purchase/remittance preview. Record the live selling rate, outbound fee, cable/intermediary fee, and estimated AUD sent before confirming. Do not rely on the AUD 5 receiving fee alone.
- Use the truthful study/living-expense current-account purpose where applicable; do not state a false purpose and do not use convenient-quota funds for unapproved overseas securities investment.
- Receive into the BOC Australia AUD Overseas Student Account, verify the actual AUD receipt and AUD 5 charge, then transfer domestically to CBA at the published zero personal online/mobile transfer fee.
- At the end of the NetBank Saver introductory period, compare the then-current standard rate, GoalSaver bonus rate/conditions, and BOC term-deposit rates. If GoalSaver remains near 5%, use a small monthly deposit and finish each month above the starting balance to keep the bonus.
- Determine Australian tax residency and update TFN or foreign-resident details correctly. Treat every interest estimate as gross before tax.
## 伊利股份（600887）专项研究｜2026-07-15

### 用户适配约束
- 用户以长期、低频、基本面和合理估值为主，不追求短期题材交易。
- 现有持仓偏科技成长，稳定消费龙头在风格上有分散价值。
- 新增3万元方案中，个股机会资金约3000元；一手伊利接近该额度上限，因此最多适合作为一手观察仓，不能因“高股息”连续加仓。
- 中证A500、红利低波等基金本身可能已经持有伊利，直接买入会形成主动超配，需要更严格的买入理由。

### 待回答问题
- 2025年利润大增而收入近乎不增，增长质量和可持续性如何？
- 经营现金流下降是否由营运资本、税费、采购周期或一次性因素造成？
- 液态奶、奶粉及奶制品、冷饮等业务的真实竞争力和增长结构如何？
- 当前价格对应的正常化市盈率、股息率和自由现金流回报是否留有安全边际？
- 伊利更适合三至五年持有，还是存在可信的短线交易逻辑？
- 哪些数据变化会证伪买入逻辑？

### 财务质量原始资料定位（独立分析轨道）
- 公司投资者关系页已取得2025年年度报告、2026年第一季度报告、2024年年度报告和2023年年度报告全文；后续年度将同时用原年报与下一年报的可比数核验。
- 2025年报披露日为2026-04-30，审计意见为标准无保留意见；2025年营业收入1156.36亿元、归母净利润115.65亿元、扣非归母110.68亿元、经营现金流143.44亿元。
- 2024年归母84.53亿元、扣非60.11亿元；2025年利润高增必须先拆分2024年非流动资产处置收益和经营性减值等低基数，不能把同比增速直接外推。
- 2025年非经常性损益净额4.97亿元，其中政府补助10.48亿元、其他营业外收支净额-5.02亿元；2024年非经常性损益净额24.42亿元，主要含非流动资产处置损益25.64亿元。
- 原始PDF：https://www.yili.com/uploads/2026-04-30/85ed8e5f-8d6f-49b4-9f10-c5d217f83ff31777526591734.pdf
- 2026Q1 PDF：https://www.yili.com/uploads/2026-04-30/f55be7d8-cac0-4540-9bb8-0dce0e7f8fe51777526693097.pdf
- 2024年报 PDF：https://www.yili.com/uploads/2025-04-29/478095e5-22ea-40f7-87eb-7d55651a0ad51745927217322.pdf
- 2023年报 PDF：https://www.yili.com/uploads/2024-06-20/5f497176-2366-48bf-b45b-3d6da58553ef1718860520349.pdf

### 2025利润与现金流初步还原
- 2025年营业收入仅增2.43亿元，但营业成本下降6.45亿元，合计使毛利增加8.88亿元；销售费用下降4.38亿元，其中广告营销费下降7.92亿元，职工薪酬增加2.97亿元。
- 2024年信用减值+资产减值合计52.31亿元，2025年降至9.99亿元，减值少计42.32亿元，是2025扣非利润高增的最大来源；2024年还确认处置长期股权投资收益25.80亿元，属于非经常性低基数/高基数交错，必须用利润桥而非单看同比。
- 2025年经营现金流143.44亿元，同比少73.96亿元。间接法显示：2024年存货、经营性应收、经营性应付合计贡献现金约+50.21亿元；2025年合计占用约-26.99亿元，营运资本同比摆动-77.20亿元，已足以解释现金流下降。
- 2025年经营现金流/归母净利润约1.24倍，自由现金流（经营现金流减购建长期资产现金）约113.07亿元；仍有现金含金量，但2024年的177.61亿元自由现金流明显受营运资本顺风和较低资本开支共同抬高。
- 2022年收购澳优59.17%股权，合并成本87.35亿元、初始商誉43.51亿元；2024年影响合并报表的澳优商誉减值30.37亿元。2025年澳优相关资产组账面价值98.40亿元、可收回金额104.63亿元，约6.23亿元缓冲，对增长率7.00%-8.25%、毛利率39.33%-45.70%、税前折现率10.82%的假设较敏感。

## 伊利股份专项研究结论（2026-07-15）

### 综合判断
- 公司质量中上，护城河主要来自品牌、全国渠道、奶源协同和多品类规模；增长属性已转为成熟消费龙头。
- 25.93元对应报告TTM市盈率约13.6倍、扣非TTM约13.9倍；按更保守的正常化EPS 1.58-1.75元，对应约14.8-16.4倍。
- 2025年每股分红1.38元，对应历史税前股息率约5.32%；该分红已除息，不能视为未来保证。
- 基准合理价值约25-28元。当前价格合理略偏便宜，但安全边际不宽，不属于需要立即追买的深度价值区。

### 关键事实
- 2025年收入1156.36亿元，仅增长0.21%；归母净利115.65亿元、增长36.82%，主要受2024年大额减值低基数影响，不能外推。
- 2025年液态奶收入704.22亿元、下降6.11%；奶粉及奶制品增长10.42%，冷饮增长12.63%，结构转型在推进，但尚未完全补回液奶压力。
- 2025年经营现金流143.44亿元、同比下降34.02%，仍为净利润1.24倍；简化自由现金流约113.07亿元。
- 2026Q1收入增长5.47%、扣非利润增长15.11%、经营现金流恢复，但一个季度不足以证明液奶和终端价格已形成持续拐点。
- 澳优历史减值、短期融资滚续、产业链担保、部分股东及管理层持股质押，是需要持续跟踪的治理和资本配置风险。

### 执行结论
- 属性：只适合3-5年以上的防御型长期持有，不适合作为短线题材交易。
- 价格：23元以下吸引力较高；23-25元可考虑一手；25-27元为观察区；28元以上除非盈利预期上调，否则不追。
- 用户当前约3000元个股机会资金只能覆盖一手。25.93元买100股约2593元并几乎占满预算，因此默认等待回踩或2026半年报验证，不在单日上涨后追买。
- 若坚持当前建仓，最多100股，视为完整目标仓；半年报前不加第二手。
- 退出/证伪：液奶量价连续恶化、毛利率与费用率同时恶化、自由现金流不能覆盖分红、再次大额并购减值、重大食品安全或治理事件。

## A股低估优质个股筛选结论｜2026-07-15

### 筛选边界
- 以长期持有、可理解业务、盈利和现金流质量、资产负债表、治理、正常化估值为主，不按最低PE机械排序。
- 对银行、保险、地产链、资源、航运和化工先还原信用或周期风险；低PE若来自盈利高点、坏账不透明或现金回收弱，不视为安全边际。
- 用户个股预算1万至2万元，A股按100股一手计算；现有A500和红利低波基金可能已经持有候选公司，直接买入属于主动超配。

### 2026-07-15收盘快照
- 招商银行37.76元，一手3776元；按2025年EPS 5.70元和每股净资产43.43元计算，约6.62倍PE、0.87倍PB；2025年度拟合计分红2.016元，对应静态税前股息率约5.34%。
- 格力电器39.83元，一手3983元；按2025年EPS 5.20元计算约7.66倍PE；2025年度中期1元加年度2元合计3元，对应历史税前股息率约7.53%，未来能否重复不保证。
- 海尔智家21.02元，一手2102元；行情口径滚动PE约10.5倍，但2026Q1收入、净利和经营现金流分别下降6.86%、15.22%和29.46%。
- 万华化学70.09元，一手7009元；按2025年EPS 3.99元约17.6倍PE、约2.0倍PB，2025年股息率约1.8%，不属于当前深度低估。

### 优先级与安全边际
- 第一名招商银行：零售和财富管理护城河、0.94%不良率和接近388%的拨备覆盖率，使其在低估银行中质量更可靠。2026Q1收入增长3.81%、净利增长1.52%，但净息差仍下降。悲观约30元，基准约39-43元，乐观约48元；38元以内可建立一手，35元以内更有吸引力，43元以上不追。
- 第二名格力电器：现金流和分红强，估值补偿充分，但本质是低增长收益型资产。2025年收入和净利均下降约9.9%；2026Q1收入和净利恢复约3%增长，但扣非净利微降、经营现金流下降29.1%。悲观约29元，基准约40-53元；40元以内可买一手，36元以内更有吸引力，45元以上不追。
- 条件候选海尔智家：全球化和多品牌经营质量优于单一空调逻辑，2025年仍增长，但2026Q1北美天气、关税和需求造成明显回落。20元以下或半年报确认修复后再考虑；当前不与格力同时重仓。
- 观察候选万华化学：公司质量高，2026年上半年盈利预告增长60%-70%，但高资本开支、62.8%资产负债率和石化业务低毛利意味着周期风险仍高。65元以下或半年报后再评估，不在70元附近追。

### 排除的“低PE”
- 中国建筑、部分低估银行和中国平安：低倍数背后分别有地产链回款、信用成本或保险投资收益的分析难度，现阶段不如招商银行清晰。
- 中远海控、中国海油和煤炭股：利润与运价、油价或煤价高度相关，当前PE不能代表中周期估值。
- 伊利当前25.93元约13.6倍PE，属于合理略便宜而非捡漏；贵州茅台一手资金远超预算；美的、中国移动、长江电力当前估值也不够便宜。

### 可执行方案
- 1万元：招商银行100股加格力电器100股，按收盘价约7759元，保留约2241元；两笔最低佣金合计约10元。
- 2万元：仍先执行同一首仓，保留约12241元。招商银行到35元附近再加100股，格力到36元附近再加100股；若未触发，不为满仓而买。
- 若更重视成长质量而非当期股息，用海尔替代格力，但只在20元以下或半年报确认北美修复后买；格力和海尔不同时作为重仓。
- 计划持有3-5年，每个半年报复核净息差和资产质量、家电收入和扣非利润、经营现金流、分红覆盖及治理变化；基本面破坏时退出，不以短期涨跌机械止损。

## 招商银行与格力电器专项复核｜招商银行证据（2026-07-15）

### 为什么它不只是普通低PE银行
- 2025年末管理零售客户总资产17.08万亿元，同比增长14.44%；零售客户2.24亿户，金葵花及以上客户593.15万户，同比增长13.29%。零售业务对公司营收和利润贡献均超过50%。
- 零售财富管理手续费及佣金收入237.94亿元，同比增长17.85%；2026Q1进一步增长25.42%。这部分轻资本收入能部分缓冲净息差下行，但会随资本市场景气波动。
- 2025年客户存款增长8.13%，核心存款日均余额增长9.69%、占客户存款日均余额87.41%；2026Q1存款平均成本率从1.29%降至0.99%，低成本负债是核心护城河。
- 2025年ROAE为13.44%，2026Q1年化ROAE为13.48%；2025年不良率0.94%、拨备覆盖率391.79%，2026Q1分别为0.94%和387.76%。在盈利仍高于多数银行资本成本的同时，股价低于账面价值，形成质量调整后的低估。

### 低估值背后的真实代价
- 2025年净息差1.87%，同比下降11个基点；2026Q1继续降至1.83%，同比下降8个基点。净利息收入增长主要依靠规模和存款成本下降，资产端收益率压力尚未结束。
- 2026Q1信用减值损失148.46亿元，同比增长15.65%。零售贷款余额在一季度下降1%，说明居民信贷需求和风险偏好仍弱。
- 2025年零售贷款不良率由0.98%升至1.08%；小微贷款不良率由0.79%升至1.22%；住房贷款不良率由0.48%升至0.51%。信用卡不良率由1.75%微降至1.74%，但关注率从4.17%升至4.81%，风险尚未完全释放。
- 2025年信用卡交易额、利息收入和非息收入分别下降7.62%、7.30%和15.73%，传统信用卡高收益模式正在承压。
- 2025年拨备覆盖率同比下降20.19个百分点，2026Q1再下降4.03个百分点；当前缓冲仍厚，但不能只看不良率静态数值。

### 初步定性
- 招商银行的优势不是高速增长，而是客户资产、低成本存款、财富管理和风险定价共同构成的复合护城河。
- 37.76元对应2025年约6.62倍PE、0.87倍PB和5.34%历史分红收益率；这是“优质银行被按低增长银行定价”，而不是无风险便宜。
- 最需要跟踪的四项：净息差、零售关注类贷款、信用减值增速、ROAE能否维持在11%-12%以上。

### 2026Q1风险与资本补充
- 一季度信用卡贷款不良率由2025年末1.74%升至1.90%，关注率由4.81%升至5.20%；信用卡新生成不良120.42亿元，同比增加20.35亿元。短期最明确的资产质量压力来自信用卡，而不是公司贷款。
- 一季度整体新生成不良189.27亿元，同比增加22.75亿元，年化不良生成率1.08%，同比升0.08个百分点；信用成本年化0.82%，同比升0.04个百分点。
- 集团高级法核心一级资本充足率14.13%、资本充足率17.76%，仍明显高于8.25%和11.25%的监管底线；但一级资本和总资本充足率较年末分别下降0.46和0.48个百分点，扩表与分红仍受资本约束。
- 一季度零售AUM继续增长4.52%至17.86万亿元，金葵花及以上客户增长4.80%；财富端护城河延续，信贷端风险则在分化。

## 招商银行与格力电器专项复核｜格力电器证据（2026-07-15）

### 正面逻辑
- 2025年消费电器收入1330.55亿元，占营业收入78.06%，毛利率35.28%、同比提升0.37个百分点；核心产品仍具品牌、渠道、规模采购和自研压缩机等制造优势。
- 2025年归母净利润290.03亿元、ROE20.30%，即使收入和利润下降约9.9%，资本回报率仍高；基本每股收益5.20元对应当前约7.66倍PE。
- 2025年经营现金流463.83亿元，购建长期资产现金17.17亿元，表面现金创造能力强；2025年度中期每股1元加年度每股2元，合计每股3元，约占归母净利润57.8%。
- 2025年末货币资金1105.53亿元，其中受限货币资金105.78亿元；账面流动性足以覆盖分红和正常经营。
- 研发投入64.44亿元，占收入3.78%，资本化率仅0.63%；研发费用化比例高，利润没有依靠大规模资本化粉饰。

### 必须修正的“现金牛”表象
- 经营现金流同比增长57.93%，公司明确解释主要受经营活动相关受限资金到期收回影响；现金流补充表中的“其他”包含票据保证金等净减少156.67亿元。该增量不能机械外推。
- 2025年末现金及现金等价物仅275.66亿元，远低于1105.53亿元货币资金；大量资金为定期存款、准备金或保证金，不能把全部货币资金视作随时可分配现金。
- 投资活动净流出485.99亿元，主要来自金融投资和其他投资现金流，而非制造业资本开支；格力同时具有制造企业和财务资金管理特征，分析净现金不能只看一个科目。

### 增长与集中度风险
- 2025年消费电器收入下降10.44%，内销主营下降10.67%，外销主营下降2.93%；工业制品及绿色能源仅增长0.78%，智能装备虽增长60.51%但收入占比只有0.40%，还无法成为第二增长曲线。
- 研发投入下降9.75%，与收入降幅接近，研发强度稳定但绝对投入收缩；这不支持给高成长股估值。
- 董明珠于2025年4月不再兼任总裁但继续任董事长，张伟接任总裁。治理从强人主导向分工过渡，可能改善，也带来接班和决策机制的不确定性。

### 初步定性
- 格力的护城河是真实的，但投资逻辑主要是“成熟龙头+高资本回报+高股东回报+低估值”，不是“第二增长曲线即将爆发”。
- 39.83元的安全边际来自低倍数和分红，而非收入增长确定性；最重要的证伪项是核心消费电器继续双位数下降且扣非利润同步恶化。
## 本轮补充：格力电器 2026Q1、治理与激励

- 2026Q1 营收 429.66 亿元，同比增长 3.52%；归母净利润 60.82 亿元，同比增长 3.01%，但扣非净利润 57.02 亿元，同比下降 0.27%。利润表的恢复力度弱于表面归母净利润增速。
- 一季度经营现金流净额 77.99 亿元，同比下降 29.11%；非经常性损益约 3.80 亿元，其中金融资产公允价值变动及处置收益约 3.53 亿元。因此，不能把一季度净利润增长完全理解为主营经营改善。
- 珠海明骏持股约 9.02 亿股，其中约 7.91 亿股处于质押状态，约占其持股 87.6%。珠海明骏与董明珠构成一致行动关系，这会放大控股层面的融资与治理风险。
- 2026 年回购计划金额 50 亿至 100 亿元，至少 70% 用于注销，最多 30% 用于员工持股计划。若按计划完成，注销部分对每股价值有利，但在实际完成前不能将上限金额视作确定回报。
- 第四期员工持股计划受让价 38.61 元，接近当前股价，并非明显低价输送；2026/2027 年归属考核要求 ROE 至少 16%（18% 对应 100% 归属）且现金分红率至少 50%，利益约束方向较好。资金来自公司计提的激励基金，仍属于薪酬成本，不能等同于员工用全部自有资金承担风险。

## 本轮补充：招商银行房地产与资产质量

- 2026Q1 公司房地产贷款约 2,837.08 亿元，占贷款总额约 4.00%；不良率 4.44%，较 2025 年末下降 0.20 个百分点。超过 85% 的开发贷投向一、二线城市。
- 承担信用风险的房地产业务余额约 3,479.35 亿元，较年初下降 1.70%。风险在收缩且结构较好，但 4.44% 的房地产贷款不良率仍显著高于全行 0.94%，不能说风险已经消失。

## 两家公司估值情景（以 2026-07-15 收盘价估算）

### 招商银行：37.76 元

- 2025 年 EPS 5.70 元、每股净资产 43.43 元，对应约 6.6 倍 PE、0.87 倍 PB；2025 年拟派息 2.016 元，对应静态股息率约 5.34%。
- 悲观情景：可持续 ROE 降至约 10%，市场仅给 0.7 倍 PB，参考价值约 30.4 元，价格下行约 19.5%。
- 基准情景：可持续 ROE 约 11.5%-13%，估值回到 0.9-1.0 倍 PB，参考价值约 39.1-43.4 元；加上股息后，未来 3-5 年年化总回报中枢粗估约 7%-11%。
- 乐观情景：ROE 稳在 13% 以上、估值回到 1.1 倍 PB，参考价值约 47.8 元。以上均为假设推演，不是目标价承诺。
- 操作区间：38 元以内可建观察仓；35 元以内更有安全边际；43 元以上不追。

### 格力电器：39.83 元

- 2025 年 EPS 5.20 元，对应约 7.7 倍 PE；全年合计分红 3.00 元，对应静态股息率约 7.53%，但下一年度分红并不保证相同。
- 悲观情景：常态 EPS 降至 4.5 元、估值 6.5 倍，参考价值约 29.3 元，下行约 26%。
- 基准情景：常态 EPS 5.0-5.3 元、估值 8-9 倍，参考价值约 40-47.7 元；未来 3-5 年年化总回报中枢粗估约 6%-10%，主要依靠分红。
- 乐观情景：EPS 约 5.3 元、估值 10 倍，参考价值约 53 元。若主营收入继续收缩，分红再高也可能被估值和利润下降抵消。
- 操作区间：40 元以内可买一手观察仓；36 元以内更适合加仓；45 元以上不追。

## 最终比较与组合含义

- 招商银行属于“优质经营能力被低估”：零售客户资产、低成本存款、财富管理收费和风险定价共同构成护城河，主要风险是净息差、信用卡及小微资产质量和房地产尾部风险。
- 格力电器属于“成熟现金牛被低估”：品牌、渠道、制造效率、高毛利和高分红仍强，但主业集中、第二增长曲线很小、治理对核心人物依赖较高，估值便宜有其原因。
- 质量排序：招商银行 A-，格力电器 B+。若只能选一只，优先招商银行；若两只都买，个股资金目标权重建议招商银行 60%、格力电器 40%。
- 两只股票都受中国内需、地产链和红利价值风格影响，不能视作充分分散；用户已有 A500/红利低波基金时，直接买入意味着主动超配，应作为卫星仓而不是替代基金底仓。
- 1 万元个股预算：招商银行 100 股 + 格力电器 100 股，约用 7,759 元，保留约 2,241 元。
- 2 万元个股预算：先执行上述一手各一只；招商银行到 35 元附近优先再加 100 股，格力到 36 元附近再考虑加 100 股。价格不到则保留现金，不为凑满仓位而追价。
## 牧原股份专项复核：本地文档初步结论

- 本地权威上下文并未把牧原判定为“不值得推荐”。相反，牧原被单独划为5万元专项资金池，明确定位为生猪养殖龙头、具备成本优势，并配置了左侧金字塔和右侧确认两套加仓纪律。
- 当前记录持有200股：2026-06-11以33.90元买入100股，2026-06-24以32.40元买入100股，累计投入6630元，平均成本33.15元，专项资金剩余约43370元。
- 文档给牧原的核心定性是“猪周期底部偏弱阶段的小仓试探”，而不是稳定复利型高股息资产。短期利润主要由猪价与养殖成本差决定，AI养猪等长期效率因素不能替代周期确认。
- 现有计划的优点是没有一次性用满5万元，并要求价格触发之外再检查猪价、完全成本、现金流、负债和产能去化；这说明策略本身已经承认牧原存在较大的周期与资产负债表波动。
- 上一轮低估值筛选使用的是盈利稳定性、现金流可预测性和分红回报等框架，天然有利于银行、家电等成熟资产。牧原的周期底部利润或周期顶部利润都不适合直接使用静态PE排序，因此“未列入榜首”不等于基本面否定，而是候选池口径不一致。

## 文档整体投资理念与上一轮筛选偏差

- 最高层投资理念并不只偏好高股息，还明确认可产业趋势、科技成长、低位逻辑变化和长期净买入；看不懂单一公司时用宽基或行业ETF，看得懂公司后才用个股获取alpha。
- 高股息策略在文档中被定位为未来资金规模更大或流动性危机中的防守预案，不是当前所有选股的唯一主策略；当前主线仍包括宽基底仓和科技成长仓纪律。
- 上一轮问题是寻找“估值较低、像捡便宜、适合投入1万至2万元”的个股，因此筛选框架强调正常化盈利、现金流、分红和回撤控制，最终偏向招商银行、格力电器。这回答了稳健价值部分，却没有单列成长资产部分，属于报告覆盖不完整，而不是用户理念只接受高股息。
- 后续应至少区分三类资产：稳定复利型质量价值、周期成长型、结构成长型；不同类别分别使用PB/ROE、周期中枢利润、PEG/自由现金流等估值方法，不能混在一个静态PE榜单里。

## 牧原实时复核：第一批官方证据

- 牧原2025年度业绩预告显示归母净利润约147亿至157亿元，同比下降12.20%至17.79%；全年商品猪销售均价约13.5元/公斤，同比下降17.3%，但公司继续降低养殖成本。该结果证明成本领先仍能在猪价下跌时创造可观利润，但也显示利润对猪价极为敏感。
- 2026Q1公司净利润同比下降126.46%，主要因为猪价下降；官方行业材料披露牧原一季度亏损约12.15亿元。存货跌价损失和应收款信用损失也明显增加，周期下行已经进入财务报表，而不是只存在于市场预期。
- 农业农村部7月第1周监测显示全国生猪均价10.48元/公斤，环比上涨4.2%，但同比下降29.9%；仔猪价格同比下降40.1%。单周反弹不能视作猪周期反转确认。
- 商务部商品价格信息显示，2026年一季度末全国能繁母猪约3904万头，仍高于3750万头左右的正常保有目标；行业正在政策和亏损推动下去产能，但生产效率提升会部分抵消母猪数量下降，供需拐点仍有不确定性。
- 当前投资逻辑应表述为“行业亏损推动去产能，牧原凭成本、规模和融资能力扩大相对优势，等待未来猪价回归成本线上方”，而不是“当前利润高增长”。这属于周期份额成长，确定性低于稳定复利公司，但潜在弹性高于招商银行和格力。

## 牧原2026Q1财务压力测试

- 一季度营收298.94亿元，同比下降17.10%；归母净亏损12.15亿元，扣非净亏损11.41亿元；经营现金流净流出9.20亿元，而上年同期净流入75.06亿元。亏损基本来自主营周期，而不是一次性会计项目。
- 期末总资产1771.97亿元、总负债898.94亿元，资产负债率约50.73%，较2025年末约54.15%下降。改善主要伴随H股发行取得约106亿元筹资现金和资本公积增加，既增强抗周期能力，也带来约5.7%的股本扩张。
- 货币资金约142.70亿元，短期借款约401.72亿元，一年内到期非流动负债约65.29亿元；流动资产601.37亿元、流动负债658.50亿元，流动比率约0.91。公司融资渠道强且负债下降，但短债规模仍要求经营和再融资持续顺畅。
- 固定资产约991.80亿元，占总资产约56%；一季度购建长期资产支出44.91亿元，同时经营现金流为负。这是重资产、高折旧、高生物安全投入的商业模式，不能按轻资产成长股给予高估值。
- 一季度存货增至396.98亿元，资产减值损失约3.22亿元；猪价低于成本时，存货和生物资产的减值波动会放大利润风险。

## 牧原2026年6月经营快照

- 2026年6月销售商品猪622.7万头，同比下降11.28%；商品猪销售均价9.69元/公斤，同比下降31.18%；销售收入75.00亿元，同比下降41.40%。量、价、收入同时下降，当前不是收入成长阶段。
- 2026年1至6月累计销售商品猪3861.5万头、销售收入501.45亿元；公司月度商品猪均价从1月12.57元/公斤降至4月9.45元，5至6月仍在9.7元左右，持续处于严重盈利压力区。
- 6月屠宰生猪295.6万头，能繁母猪存栏311.3万头。屠宰一体化和规模效率提供一定缓冲，但还不能消除上游猪价与养殖成本差对利润的决定性影响。
- 33.15元的现有平均成本属于前期文档定义的小仓试探区；在当前经营数据下，合理动作是保留200股核心观察仓，新增资金必须等待成本、猪价或行业产能去化出现可验证改善，不能仅凭股价达到旧补仓档位执行。

## 牧原2025年报：竞争力与第二曲线

- 2025年营业收入1441.45亿元，同比增长4.49%；归母净利润154.87亿元，同比下降13.39%；扣非净利润159.88亿元；经营现金流300.56亿元，覆盖利润约1.94倍；ROE为20.57%。利润含金量在盈利年度较好。
- 2025年销售商品猪7798.1万头，屠宰生猪2866.3万头；全年生猪养殖完全成本约12元/公斤，同比降低约2元/公斤。成本下降来自生产成绩、疫病防控、营养配方、育种和智能化的综合改善，是公司最核心的可持续竞争优势。
- 屠宰肉食收入452.28亿元，同比增长86.32%，2025年首次实现全年盈利，全年产能利用率98.8%。这条业务能提高全产业链效率并形成产品化能力，但目前仍不能完全平滑养殖周期。
- 2025年末资产负债率54.15%，同比下降4.53个百分点，负债总额减少171亿元；经营现金流较强且利息保障倍数7.18。公司在上一个盈利窗口主动去杠杆，增强了2026年低猪价环境下的生存能力。
- 2025年实施的两次现金分红合计80.85亿元，并完成约20亿元回购；针对2025年度另提出约24.35亿元现金分红预案。公司具备股东回报意识，但牧原的分红金额随周期利润变化，不应当作固定高股息资产。
- 牧原的真正成长属性来自三部分：单位成本持续下降、行业集中度提高带来的份额成长、屠宰肉食业务从亏损走向盈利。猪价反弹只是利润放大器，不是唯一长期价值来源。

## 牧原2026年半年度业绩预告

- 公司预计2026年上半年归母净亏损57亿至67亿元，扣非净亏损55亿至65亿元，而上年同期归母净利润105.30亿元；基本每股亏损约1.03至1.21元。
- 上半年商品猪销售均价约10.4元/公斤，同比下降约28%。由于一季度归母亏损12.15亿元，预告意味着二季度可能单季亏损约44.9亿至54.9亿元，盈利压力较一季度显著扩大。
- 公司同时表示养殖成本仍同比下降，但成本改善尚不足以抵消猪价下跌。投资判断必须等待猪价与完全成本价差收窄，而不能只看成本下降方向。
- 2026年7月10日前后的公开行情快照约38.14元，对应总市值约2202亿元。市场已经部分计入未来去产能和周期修复预期，不能用2025年154.87亿元周期盈利简单计算约14倍PE后认定明显低估，更不能用2026年亏损期PE估值。
- 更合理的估值方法是以正常化周期利润、每公斤正常利润和可持续出栏量进行情景分析，并对高负债、重资产、动物疫病与周期预测错误留出折价。

## 牧原当前价格与正常化估值（2026-07-15）

- 腾讯行情快照显示A股收盘约39.65元。现有200股按平均成本33.15元计算，市值约7930元，未计交易成本的浮盈约1300元，收益率约19.61%。
- 按一季度末总股本57.73亿股计算，总市值约2289亿元；按归母净资产872.80亿元计算，每股净资产约15.12元、PB约2.62倍。该估值不是深度破净型价值股定价。
- 如果把100亿、150亿、200亿元分别视作可持续正常化利润，当前对应约22.9倍、15.3倍、11.4倍正常化PE。只有在正常化利润能够稳定接近150亿以上时，当前价格才算合理或偏便宜。
- 情景参考：悲观情况下正常化利润100亿元、13倍PE，对应约22.5元；基准情况下150亿元、14至16倍PE，对应约36.4至41.6元；乐观情况下200亿元、15至17倍PE，对应约52.0至58.9元。估值跨度大本身就是周期股风险的体现。
- 当前39.65元接近基准价值区，现有低成本仓可继续持有，但不适合追涨加仓；新增仓应等待价格重新回到34至36元且基本面未恶化，或者猪价和成本差明确改善后再右侧确认。

## A股成长候选：筛选框架与第一批

- 成长候选必须同时满足：收入或正常化利润有清晰增长来源、经营现金流和资产负债表能够支持增长、估值没有要求完美兑现、与用户现有科技基金重叠可控。
- 美的集团是第一批“质量成长”候选。2025年收入4585亿元、归母净利润439.5亿元，均实现双位数增长；海外收入1959亿元、同比增长16%，ToB收入1228亿元、同比增长17.5%。增长来自全球本地化、自有品牌和工业技术第二曲线，不是单纯高股息。
- 中际旭创属于高景气高成长候选，核心受益于AI算力和高速光模块升级；但用户已有芯片、AI、机器人和恒生科技敞口，直接再买单一光模块龙头会增加行业和估值集中，需要比一般成长股更高的安全边际。
- 福耀玻璃属于中速质量成长候选，逻辑是全球汽车玻璃份额、单车玻璃价值量和海外产能；需要继续核对2025年及2026Q1增长、美国扩产收益、关税与汇率风险后再排序。
- 立讯精密可作为备选观察，但客户集中、消费电子周期、资本开支和供应链地缘风险较高；除非估值明显优于美的或福耀，否则不作为用户的第一只新增成长个股。

## 美的与福耀实时复核

- 美的2026Q1营收1310.99亿元，同比增长2.55%；归母净利润126.75亿元，同比增长2.03%，但扣非净利润109.62亿元，同比下降14.02%；经营现金流145.29亿元，同比增长1.45%。2025年的成长逻辑仍在，但2026年初主营利润质量暂时减速。
- 福耀2025年营收457.87亿元，同比增长16.65%；归母净利润93.12亿元，同比增长24.20%；经营现金流120.55亿元，同比增长40.79%；高附加值产品占比提高5.44个百分点，汽车玻璃收入增长17.30%，是非常扎实的质量成长年度。
- 福耀2026Q1营收104.13亿元，同比增长5.08%；归母净利润17.12亿元，同比下降15.68%；扣非净利润下降17.32%。利润下降部分与汇兑损益基数变化有关，收入仍增长，但速度显著放缓。
- 福耀一季度经营现金流下降82.22%，公司解释主要为客户使用票据结算增加、到期应付票据付款增加，具有一定时点性；仍需用二季度现金回款验证，不能仅凭解释直接忽略。
- 当前排序：美的仍是最均衡的质量成长研究对象，福耀的2025质量更强但2026Q1需要确认；两者都不是“现在闭眼追”的高增长股，更适合等估值或下一份财报提供安全边际。

## 中际旭创：高成长不等于当前可买

- 中际旭创2025年营收382.40亿元，同比增长60.25%；归母净利润107.97亿元，同比增长108.78%；经营现金流108.96亿元，同比增长244.31%；ROE达到43.84%。盈利和现金流增长质量都很强。
- 2026Q1营收194.96亿元，同比增长192.12%；归母净利润57.35亿元，同比增长262.28%；扣非净利润增长264.56%；经营现金流33.68亿元，同比增长55.58%。这是候选中最强的当期成长。
- 2026年7月15日收盘约1169.31元，行情快照动态PE约87倍，一手约11.69万元，远超用户1万至2万元个股预算。即使未来利润继续高增，当前估值对订单、价格、技术路线和云厂商资本开支都要求非常高。
- 用户已有芯片、AI、机器人和恒生科技仓位。中际旭创同时存在AI资本开支周期、海外大客户集中、光模块降价、技术迭代和出口限制风险，直接加仓会放大已有风险，而不是补足组合短板。
- 结论：中际旭创是“公司高质量、成长极强、当前不适合买”的典型；优先通过已有AI/科技基金持有行业敞口，不建议当前直接买A股一手。

## 成长候选当前行情可执行性（2026-07-15）

- 美的集团约82.67元，一手约8267元，行情快照PE约14.24倍。估值合理、业务最均衡，但2026Q1扣非利润下降使其更适合观察或小仓，不宜一次用满个股预算。
- 福耀玻璃约52.90元，一手约5290元，行情快照PE约15.35倍。估值不贵、2025成长扎实，但2026Q1利润和现金流转弱，需要等待二季度确认。
- 中际旭创约1169.31元，一手约11.69万元、动态PE约87倍，既不满足预算，也不满足安全边际。

## 牧原历史下跌报告复核与最新成本

- 2026-06-11历史报告记录当时股价34.16元、猪价9.80元/公斤、完全成本约11.6元/公斤，并主观划分29至31元中等下行情景、25至28元极端情景。报告本身已明确这些概率没有可验证模型，不能作为估值铁底。
- 最新公开公司信息显示2026年6月养殖完全成本约11.7元/公斤，对比当月商品猪均价9.69元/公斤，每公斤经营价差约为负2.01元。成本较5月11.6元略有反复，说明降本不会线性进行。
- 旧文档38.5元右侧突破加仓线形成时，尚未计入上半年亏损57亿至67亿元和二季度亏损扩大的新证据。按照文档自己的“新基本面优先”原则，这条价格触发应暂时冻结，不能机械执行。
- 当前建议是保留200股核心仓；39.65元不新增。只有回调至34至36元且成本优势、负债和去产能逻辑未恶化，或猪价持续回到公司完全成本上方并由经营现金流确认，才重新评估100股加仓。

## 立讯精密备选复核

- 立讯精密2026Q1营收838.88亿元，同比增长35.77%；归母净利润36.60亿元，同比增长20.24%；扣非净利润27.76亿元，同比增长15.22%。消费电子、数据中心高速互连和汽车业务提供多条增长线。
- 一季度经营现金流净流出70.68亿元，较上年同期净流出66.92亿元进一步扩大；虽存在季节性和营运资金因素，但增长对供应链资金和资本投入的要求较高。
- 2026年7月15日约60.47元，一手约6047元，行情快照PE约27.13倍。估值明显高于美的、福耀，且与用户现有科技仓位重叠。
- 结论：立讯是有真实成长的公司，但并非当前组合第一优先；除非估值回到约22倍以下或数据中心/汽车业务显著提高利润和现金流质量，否则先观察。

## 牧原与成长股最终决策（2026-07-15）

- 对上一轮结论的修正：没有重点推荐牧原，主要因为上一轮是在寻找“低估、稳健、1万至2万元可执行”的新增个股，并且牧原已经有独立5万元专项资金池。筛选口径偏向招商银行、格力这类盈利与现金流较稳定的资产，遗漏了单列成长股清单；这不等于牧原不值得投资。
- 牧原的正确归类是“周期成长型龙头”，不是高股息防御股，也不是线性复利成长股。其成长来源是完全成本下降、行业集中度提升和屠宰肉食盈利改善，猪价决定利润弹性。
- 当前动作：继续持有200股，不在39.65元附近追涨，也不执行旧文档38.5元突破加仓。旧触发线在上半年预亏57亿至67亿元之前制定，应暂时冻结。
- 重新评估加仓100股的两类条件：一是股价回到34至36元，同时成本优势、负债和行业去产能逻辑未恶化；二是猪价持续4至8周高于公司完全成本，并由经营现金流或季度利润改善确认。剩余43370元不是必须投入额度。
- 牧原持有周期应按3至5年穿越猪周期理解，但每月检查销售均价与完全成本，每季检查经营现金流、短债、母猪存栏和屠宰业务。成本优势显著收窄、负债率重新升向60%、上行周期仍持续负经营现金流、逆势扩产或重大疫病与治理问题，均应停止加仓并重估逻辑。
- 新增成长候选排序：美的集团第一，福耀玻璃第二，立讯精密观察，中际旭创当前不直接买。美的更适合等待78元以下或二季度扣非利润恢复；福耀更适合等待50元以下且二季度现金流确认；立讯需更低估值或现金流改善；中际旭创虽成长最强，但一手资金和估值均不符合用户预算与安全边际。
- 组合角色：招商银行是质量价值与防守，格力是低增长收益资产，牧原是高波动周期成长，美的和福耀是中速质量成长，中际旭创是高预期科技成长。此前推荐高股息股的合理性在于补足用户已有科技基金和牧原专项仓的波动，而不是认为高股息优于所有成长资产。
- 对用户最匹配的执行顺序：现有牧原200股继续作为成长观察仓；新增个股资金若重视组合平衡，优先招商银行；若明确想增加成长属性，优先观察美的或福耀，而不是在牧原已上涨且半年报预亏扩大的阶段继续集中加仓。

## 美的集团专项：第一轮官方证据（2026-07-15）

- 2025年营业总收入4585亿元、归母净利润439.5亿元，收入和利润均实现双位数增长；海外收入1959亿元、同比增长16%，ToB收入1228亿元、同比增长17.5%。增长来源已不只是国内白电，而是海外本地化和ToB第二曲线共同驱动。
- 海外本地化自营业务覆盖全球主要50个国家，拥有29个海外研发中心和43个主要制造基地；这有助于从出口转向本地制造和自主品牌，但也增加固定成本、合规、汇率和跨国管理风险。
- 2025年完成Arbonia、东芝电梯中国业务和锐珂医疗国际业务等收购。ToB框架扩张很快，但未来必须区分有机增长与并表增长，并持续检查商誉、整合和资本回报。
- 2025年全年每10股现金分红43元，其中中期每10股5元已实施、年末拟每10股38元；按每股4.30元和2026-07-15收盘价82.67元计算，历史税前股息率约5.20%，但未来分红不保证维持。
- 2026-07-15腾讯行情快照为82.67元，动态PE字段约14.24倍，一手约8267元；当前股价接近52周区间上部，不能仅凭绝对PE不高就认定存在明显安全边际。
- 第一项待查问题是2026Q1归母利润小幅增长而扣非利润下降14.02%的分化，必须还原非经常性收益、汇率、毛利率、费用和并购影响后再判断正常化盈利。

## 美的集团2026Q1利润分化还原

- 官方一季报确认营业收入1310.99亿元、同比增长2.55%；归母净利润126.75亿元、增长2.03%；扣非净利润109.62亿元、下降14.02%；经营现金流145.29亿元、增长1.45%。
- 毛利额由325.31亿元增至335.23亿元，按营业收入计算毛利率约由25.45%升至25.57%；销售费用由118.75亿元降至113.56亿元，研发费用由43.48亿元降至41.66亿元。主营经营并没有呈现与扣非利润相同幅度的衰退。
- 最大负面来自财务损益：2025Q1为财务收入28.40亿元，2026Q1转为财务费用13.50亿元，形成约41.90亿元同比拖累，公司解释为汇兑损益变动。
- 同期投资收益增加约5.08亿元、公允价值变动收益改善约17.35亿元，其他收益增加约3.27亿元；2026Q1共确认17.13亿元非经常性净收益，其中非流动资产处置约7.37亿元、金融与衍生工具相关约8.27亿元。
- 这造成分析上的分类错位：部分汇率损失进入经常性财务费用，而部分套保或金融工具收益被扣除为非经常性，因而扣非下降14.02%会夸大实际主营恶化；但汇率、套保有效性与海外利润折算仍是实质风险，不能完全忽略。
- 一季度楼宇科技收入108亿元、增长10.1%，机器人与自动化82亿元、增长11.8%，工业技术68亿元、下降11.7%。ToB并非所有板块同步增长，工业技术是当期短板。
- 期末归母权益2323.08亿元，货币资金940.92亿元；短期借款374.19亿元、长期借款135.77亿元，账面流动性较强。商誉332.15亿元，占归母权益约14.3%，并购整合和减值仍需持续检查。

## 美的集团2025财务质量与业务结构

- 2025年营业收入4564.52亿元、同比增长12.11%；归母净利润439.45亿元、增长14.03%；扣非归母净利润412.67亿元、增长15.46%；ROE为19.70%，仍属高资本回报企业。
- 经营现金流533.46亿元、同比下降11.84%，仍为归母净利润的1.21倍；购建长期资产现金支出111.42亿元，简化自由现金流约422.04亿元，对应当前约6294亿元总市值的收益率约6.7%。该算法未扣除企业收购支出，不能直接当作可全额分配现金。
- 智能家居收入2999.27亿元、增长11.28%、毛利率29.90%，仍是利润基石；楼宇科技357.91亿元、增长25.72%；机器人与自动化310.11亿元、增长8.05%；工业技术272.32亿元、增长10.24%；其他创新业务287.19亿元、增长26.94%。
- 分部利润显示智能家居约371.30亿元、楼宇科技约45.04亿元、工业技术约50.88亿元，主业仍高度依赖智能家居；ToB第二曲线已具规模，但尚未取代白电利润核心。
- 海外营业收入1959.48亿元、占营业收入42.93%、增长15.92%；海外本地化使关税风险相对纯出口模式更可控，但汇率、地缘、当地合规和固定成本风险同步上升。
- 年末应收账款账面原值421.70亿元、同比增长13.36%，与收入增速大致匹配；坏账准备17.20亿元。2026Q1应收账款进一步升至525.37亿元，存在季节性，也需要半年报验证回款。
- 年末商誉342.57亿元，2026Q1为332.15亿元；其中KUKA商誉约234.35亿元。商誉约占归母权益14%至15%，暂非资产负债表致命问题，但机器人、医疗和楼宇并购整合失败可能导致减值。
- 2025年研发费用177.88亿元、增长9.58%，研发人员2.39万人；研发增速略低于收入增速，需继续观察第二曲线扩张是否以足够研发产出支撑。
- 2025年经营现金流下降而资本开支从78.40亿元升至111.42亿元，表明全球化与新业务仍处投入期；高自由现金流是真的，但不能把2025年高额回购机械外推为每年固定回报。

## 美的集团政策周期与资本配置

- 2025年国内家电增长明显受以旧换新支持。2026年国家统一补贴收窄为6类一级能效家电、补贴15%、单件最高1500元；2025年为12类、一级能效最高20%、单件最高2000元。2026年政策仍托底，但力度和覆盖面下降，存在2025年需求提前释放后的高基数风险。
- 国家统计局披露2026年1至2月限额以上家电和音像器材零售额仅增长3.3%，明显低于2025年一季度19.3%的增速；与美的2026Q1收入增长2.55%相互印证，短期国内需求已从高增长回归低个位数。
- 2025年度每股现金分红4.30元，按当前82.67元计算静态税前股息率约5.20%；2025年公司A股和H股回购超过116亿元，但部分A股回购用于激励，并非全部注销，不能等同于现金分红。
- 2026年公司另提出65亿至130亿元A股回购并注销方案，回购价格上限100元；按上限和下限估算可减少约0.9%至1.7%总股本，对每股价值有利。
- 该回购资金可由自有资金及股票回购专项贷款构成，银行承诺贷款可达实际回购金额的90%、期限不超过3年。低成本融资回购在估值合理时有利，但会提高杠杆，且执行进度、实际价格和最终金额尚需跟踪。
- 2025年完成的30亿元A股回购平均成交区间约69.50至80.44元，当前82.67元已高于该批回购成交上沿；公司认可价值不能替代投资者自己的安全边际。

## 美的集团护城河与第二曲线独立复核

- 核心护城河是多品类共享采购、研发、物流、渠道和售后，叠加压缩机、电机等核心部件纵向一体化；这比单一爆款或单纯品牌溢价更难复制。
- 2025年美的系在国内主流线上和主要线下渠道家电销售额均居行业前列，下沉市场零售规模超过300亿元；智能家居内销中电商收入占比超过55%，客户库存周转效率改善10%以上。
- 海外收入占42.93%，海外毛利率约26.60%，与国内约26.24%接近；海外OBM自有品牌收入已占智能家居海外收入45%以上。海外业务已是经营支柱，不再只是出口代工，但年报没有完整拆分剔除并购和汇率后的有机增速。
- ToB占收入已接近27%，但内部质量分化：楼宇科技2025年增长25.72%、毛利率约30.58%，最接近成熟第二引擎；机器人增长8.05%、工业技术毛利率约17.5%，其他创新业务毛利率较低，不能把全部ToB统一给予高成长估值。
- KUKA中国2025年出货超过3.2万台、增长30%以上，国内份额约9.6%；但集团机器人与自动化收入只增长8.05%，说明单一区域出货高增尚未完全转化为集团利润高增。
- 管理层执行和长期激励较强，但2026年员工持股计划主要考核ROE。注销回购也能机械抬升ROE，未来仍需同时检查收入、有机利润和自由现金流，不能只看ROE达标。
- 公司2026年发行净募资约171.74亿港元的零息可转债，约60%拟用于国际扩张和境外流动性；若全部转换存在约2.11%潜在摊薄。低息融资降低当期利息成本，但海外投资回报需覆盖整合成本和股本摊薄。
- 经营逻辑的主要证伪信号：智能家居连续四季跑输行业且毛利率下降超过2个百分点、海外有机增长跌至低个位数、ToB增速长期不高于集团、工业技术持续负增长、重大商誉减值，以及股东回报连续超过自由现金流同时债务上升。

## 美的集团估值Agent结论

- 2026-07-15收盘82.67元，最新总股本约76.134亿股；以A股价格等值计算股权价值约6294亿元。2026Q1归母权益2323.08亿元，对应每股净资产约30.51元、PB约2.71倍。
- 2025年报EPS为5.80元，当前静态PE约14.25倍；考虑2026Q1扣非利润波动，采用400亿至440亿元正常化利润、中心值420亿元，对应正常化EPS约5.25至5.78元，当前正常化PE约15倍。
- 2025年简化自由现金流约422亿元，对应当前自由现金流收益率约6.7%；2025年度每股分红4.30元，对应历史税前股息率约5.2%、派息率约73.6%。年末3.80元分红已经除息，新买入者不能重复获得。
- 三情景五年回报测算：悲观情景盈利低增、退出12倍PE，年化约0%至1%；基准情景盈利增长约7%、退出15倍PE，年化约10%至11%；乐观情景增长10%、退出17倍PE，年化约17%左右。结果对盈利增速和终值PE均高度敏感，不是收益承诺。
- 价格纪律：82至85元属于合理价但安全边际弱；78元以下开始出现小幅安全边际；72至75元是较理想的主要建仓区；70元以下在基本面未恶化时才属于明显安全边际。
- 最新库存股和可转债、期权存在潜在摊薄，极端完全摊薄估算约2.7%；注销式回购可部分抵消，但不能在实际执行前全部计入价值。
- 估值结论：82.67元可以建立观察仓，但不是捡便宜；当前最多占计划仓位约三分之一，半年报或价格回落后再决定第二笔。

## 美的集团财务取证与反方结论

- 财务取证没有发现官方披露层面的偿债危机或财务造假信号；2025年审计意见为标准无保留，经营现金流仍覆盖净利润。当前核心风险是增长质量和资本配置，而非生存风险。
- 2025年简化自由现金流约422亿元、同比下降约20%，与利润增长形成背离；原因包括经营现金流下降及资本开支增加。若未来分红、回购和并购持续同时高投入，自由现金流可能承受压力。
- 2026Q1非经常性净收益由上年同期约负3.28亿元变为正17.13亿元，改善约20.4亿元，对归母净利润形成明显支撑；扣非下降同时又被汇率和套保分类错位放大，下一份半年报比单看归母净利润更关键。
- 应收账款、合同资产和商誉需要持续检查；KUKA与TLSC商誉减值测试已被审计机构列为关键审计事项，2025年未计提减值，但可收回金额安全垫没有以简单金额完整披露。
- 2026年上半年全国限额以上家电零售额同比下降约7.4%，房地产开发投资下降约18%；内需与地产后周期仍是短期逆风，不能按2025年补贴期增速外推。
- 美国自2026年2月24日起对部分进口商品实施临时10%附加关税，当前公告期限至7月24日，后续存在延长或调整不确定性。美的海外本地化制造比纯中国出口更有缓冲，但供应链、原产地和合规成本仍可能上升。
- 组合层面，美的与牧原及科技基金行业相关性较低，可以降低单一猪周期和科技景气风险；但美的已存在于中证A500和红利低波100，直接买入是主动超配公司，不是新增资产类别。
- 最重要的否决条件：半年报扣非利润继续明显下降且智能家居收入转负；应收与库存持续快于收入；楼宇科技收入增长但利润继续下降；重大商誉减值；自由现金流走弱时仍以借款高额回购；海外关税和汇率导致毛利率持续下降。

## 美的集团最终执行判断

- 公司质量：A-，属于A股少数兼具现金流、全球化和中速成长的制造龙头；不是高爆发科技股，也不只是高股息家电股。
- 当前价格：82.67元为合理价偏上沿，预期回报主要来自约5%股息、5%至7%每股盈利增长和小幅回购增厚；安全边际不足以支持一次性重仓。
- 若个股目标预算只有1万元，一手约8267元会占用83%，当前不建议立即买，优先等待78元以下或半年报确认。
- 若个股目标预算约2万元且持有5年以上，可在当前最多买100股作为观察仓，保留至少一半资金；第二笔优先等待75至78元且基本面未恶化，72至75元才是主要加仓区。
- 用户已有A500，因此不买美的也不等于错过公司；直接买的前提应是愿意主动超配并每季跟踪扣非利润、自由现金流、海外有机增长和商誉，而不是仅因PE看起来不高。

## 牧原股份策略重构：官方证据与判断（2026-07-20）

### 行业周期

- 农业农村部2026年修订方案将全国能繁母猪正常保有量由3900万头下调至3750万头，说明生产效率提升后，旧的母猪数量基准已经偏高；判断产能不能继续沿用3900万头旧锚。
- 国家统计局披露，2026年二季度末能繁母猪存栏3780万头，同比下降6.5%，为3750万头新目标的100.8%；基础产能已明显调减，但上半年生猪出栏仍同比增长1.7%，供给传导尚未完全结束。
- 农业农村部与国家发改委6月座谈会要求大型企业压减产能和产量、严控二次育肥、淘汰弱仔猪并降低出栏体重。监管要求本身证明短期肥猪节奏与隐性产能仍是周期判断的核心变量。
- 农业农村部口径显示，7月第1周全国生猪均价10.48元/公斤、环比上涨4.2%；湖南农业农村厅转引农业农村部监测称7月第2周升至11.35元/公斤、环比上涨8.3%。两周快速上涨是修复信号，但持续时间太短，不能单独确认周期反转。
- 当前行业状态应从“红灯深度承压”上调为“黄灯初修复”：产能已接近政策目标、价格快速反弹，但上涨来源、出栏体重、二次育肥和盈利持续性仍需验证。

### 牧原经营与财务

- 牧原2026年6月销售622.7万头，销售均价9.69元/公斤，销售收入75.00亿元；截至6月末能繁母猪311.3万头。6月销售均价仍显著低于公司约11.7元/公斤的公开交流成本口径。
- 公司2026年半年度业绩预告预计归母净利润亏损57亿至67亿元，上半年商品猪销售均价约10.4元/公斤、同比下降约28%。这意味着7月现货反弹尚未进入已披露财务报表，不能用股价上涨替代利润和现金流确认。
- 2026Q1归母净利润亏损12.15亿元，经营现金流净流出9.20亿元；期末货币资金142.70亿元，短期借款401.72亿元，一年内到期非流动负债65.29亿元。H股融资后资产负债率下降，但短债和现金流仍要求新增仓位保留安全边际。
- 7月17日行情快照显示牧原收于约39.83元；现有300股趋势仓40.92元买入后并未形成大幅安全垫。价格处于基准估值附近时，不应仅凭再次突破增加集中度。

### 策略结论

- 基本面状态拥有最高权限，技术突破和回踩只能在基本面允许后决定执行时点。
- 当前500股继续分为200股核心仓和300股趋势仓；截至本轮策略重构，不因41.50元或43.50元突破自动增加仓位。
- 黄灯升级为绿灯至少需要：全国猪价或牧原月度均价连续4周覆盖公司最新完全成本；标肥价差、二次育肥和出栏体重没有显示供应只是后移；月度销售与下一份季度现金流/利润至少有一项形成确认。
- 黄灯降为红灯的信号包括：猪价重新持续低于成本且快速回落、二育/压栏推动出栏体重上升、完全成本反弹、经营现金流和短债恶化、公司逆势扩产或重大疫病/治理事件。
- 左侧低价也不是自动买入许可。仓位速度按证据强度分级：黄灯最多100股，绿灯最多200股，强绿灯一轮最多300股但拆成200股加100股；每次买后至少观察3个交易日，不再允许单一技术判断直接决定300股仓位。

### 本轮主要来源

- 国家统计局2026年上半年畜牧数据：https://www.stats.gov.cn/sj/zxfbhjd/202607/t20260716_1964140.html
- 农业农村部2026年产能调控方案转发：https://www.hunan.gov.cn/zqt/zcsd/202605/t20260518_33979020.html
- 农业农村部、国家发改委产能调控座谈会：https://xmsyj.moa.gov.cn/gzdt/202606/t20260622_6485180.htm
- 农业农村部7月第1周价格：https://xmsyj.moa.gov.cn/jcyj/202607/t20260707_6485602.htm
- 湖南农业农村厅转引7月第2周价格：https://agri.hunan.gov.cn/agri/tslm/njnqx/202607/t20260713_34025587.html
- 牧原2026年6月销售简报：https://static.cninfo.com.cn/finalpage/2026-07-07/1225411958.PDF
- 牧原2026Q1报告：https://static.cninfo.com.cn/finalpage/2026-04-22/1225136604.PDF
- 香港联交所牧原2026年半年度业绩预告：https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0710/2026071001011.pdf

## 2026-07-24 白银投资研究（阶段性发现）

- 截至 2026-07-23，国际银价约 58 美元/盎司、金价约 4059 美元/盎司，金银比约 70。
- 白银在 2025 年初约 29 美元，2026 年 1 月一度突破 100 美元；当前位置较泡沫高点回撤很深，但仍明显高于 2025 年均价，不能简单称为绝对低估。
- 白银协会预计 2026 年仍为连续第六年供需缺口；但工业需求受光伏减银和替代影响下降，回收供应上升。缺口提供中期支撑，却不会自动造成短期暴涨。
- 约 70 倍金银比高于 1970-2026 年略低于 60 倍的长期均衡，显示白银相对黄金略便宜；央行结构性买金可能令均衡比率上移，不能机械套用历史均值。
- 美国 10 年期实际利率约 2.37%，对无息资产仍是逆风；地缘冲突既有避险利好，也可能通过能源通胀、利率和经济放缓压制白银的工业属性。
- 白银更适合作为高波动卫星仓，而不是现金、黄金或股票底仓的替代品。
- 最新《World Silver Survey 2026》预计全年需求下降 2% 至 11.1 亿盎司、工业需求下降 3%，矿产供应基本持平，供需缺口约 4630 万盎司；此前 2 月的 6700 万盎司为初步预测。
- 12-24 个月情景框架（不是点位预测）：悲观 42-50 美元，基准 55-72 美元，乐观 80-95 美元；主要变量为实际利率、美元、金银比、ETF 资金流及工业需求。
- 当前判断：绝对估值不便宜，相对黄金略便宜，处于大牛市后的深度回撤与高波动消化期；综合吸引力约 6.5/10。
- 执行原则：白银占可投资金融资产 1%-3% 较合适，激进上限 5%；贵金属内部优先黄金，黄金与白银可约 70:30 或 80:20。
- 分批而非重仓：首笔只建目标仓位约 25%，其余结合更低价格、金银比升至 75 以上或实际利率回落等信号投入；不使用杠杆和期货。
- 再平衡信号：金银比低于 50、白银仓位因上涨显著超标、短期上涨 50%-70%，或连续两年供需缺口明显收窄时分批止盈；长期高实际利率、ETF 持续流出及工业替代加速是逻辑恶化信号。

## 2026-07-24 厄尔尼诺与有色金属

- NOAA 2026年7月确认厄尔尼诺正在增强，预计持续至2027年初；2026年10-12月成为极强事件的概率约81%。
- 厄尔尼诺主要通过秘鲁、智利洪水和运输中断、印尼偏旱、能源及水电成本影响供给；同时也可能推高通胀、利率并压制全球需求，方向并非单向利多。
- 学术研究显示，ENSO对部分金属存在样本内相关性，但对金属价格缺乏稳定的样本外预测能力，不能把厄尔尼诺单独作为买入信号。
- 世界银行金属与矿产价格指数2026年以来已上涨约20%，5月创名义月度新高；预计铜、铝、锡2026年全年价格达到纪录水平，当前商品整体不属于低估区。
- 分品种：铜、铝、锡基本面最强但价格偏贵；锌处于偏高而供给改善；镍和铅价格相对不高但供给或需求较弱；锂和稀土更多由产能、政策和出口管制驱动，不是厄尔尼诺交易。
- 中证有色金属指数截至2026-06-30滚动PE约18.8倍、PB约2.97倍，但2025年上涨91.67%、过去一年上涨60.64%；低PE与高PB并存，说明利润处于周期高位，并非深度低估。
- 当前判断：商品端整体偏贵；A股有色板块处于合理至略有吸引力区间，估值低于历史PE中枢但并非低价格或高安全边际。
- 执行原则：行业卫星仓不超过总可投资资产3%-5%，首笔只投入目标仓位20%-25%，其余等待板块10%-20%回撤、商品价格回落或盈利继续兑现。

## 2026-07-24 电网基金025857复核

- 权威持仓快照仍为2026-07-20：华夏中证电网设备主题ETF联接C（025857）投入285元、市值243.48元、收益率-15.10%；未收到更新后的支付宝截图，不直接改写持仓账本。
- 基金净值从2026-06-22约1.5395降至7月20日1.0846，阶段最大回撤约29.6%；7月23日净值反弹至1.1474，按旧份额粗略估算持有亏损已收窄至约-9.6%，以支付宝最终显示为准。
- 中证电网设备主题指数截至2026-06-30年初以来上涨40.57%、过去一年上涨92.23%，滚动PE约35.82倍、PB约3.63倍；前期高涨幅和高估值是本轮下跌的主要根源。
- 指数不是低波动公用事业指数：工业权重约68.2%、通信服务约27.3%，并集中持有国电南瑞、思源电气、东材科技、宏发股份、远东股份等高弹性设备、材料和通信公司，受AI电力、出海和动量交易影响明显。
- 国家电网十五五计划投资4万亿元，跨区跨省输电能力目标提升超过30%；2026年特高压招标继续提速，长期产业逻辑没有被证伪。

## 2026-08-05 其余中国/港股基金组合研究

- 研究范围：022459、021550、013309、019934、025857、010770、015210、023037、005224。
- 组合基线暂沿用2026-07-20支付宝持仓截图；未收到更新截图，因此金额、收益率和份额不视为2026-08-05已确认数据。
- 资料优先级：基金公司与法定披露、指数公司、国务院及部委、港交所和上市公司财报；第三方资料仅用于线索或交叉检查。
- 检索状态：Agent Reach于2026-08-05检查可用的网页后端为Jina Reader；Exa未配置、雪球未登录，不使用雪球社区数据支撑结论。

### 已核验的基金披露

- 中欧资源精选混合发起C（023037）2026年二季报于2026-07-15披露，报告期末股票仓位89.24%，其中A股采矿业36.04%、制造业46.64%，港股通能源和基础材料合计4.42%。官方报告：https://www.zofund.com/tempdir/minisite/20260714/b5ca6ec7-4c89-4d4e-aea3-69804bbd8324_1784033310416.pdf
- 023037前十大重仓合计约57.83%，前三大紫金矿业9.90%、西部矿业8.95%、洛阳钼业8.53%，另有厦门钨业、盐湖股份、金钼股份、藏格矿业、中钨高新、东方钽业等；这不是宽泛资源分散仓，而是高集中度工业金属和战略小金属主动仓。
- 023037二季度C份额净值下跌7.70%，过去一年上涨65.41%，净值标准差高于业绩基准；报告期末C份额从期初14.55亿份降至11.02亿份，申赎均大，说明高收益后波动和资金行为风险均明显。
- 基金经理在二季报中的当前排序为铜、战略小金属、碳酸锂、黄金、铝、油煤；这是管理人观点，不等同于已兑现的盈利，也不能用来替代商品价格和公司盈利验证。
- 广发基金官方定期公告页确认广发中证基建工程ETF联接基金2026年二季报于2026-07-20披露，原始PDF为：https://www.gffunds.com.cn/jjgg/dqgg/202607/P020260720325300006698.pdf

### 农业基金真实暴露

- 天弘中证农业主题ETF联接C（010770）已在2025年11月完成ETF联接化，目标ETF为天弘中证农业主题ETF（512620）；联接基金的真实暴露仍是中证农业主题指数（000949），不是基金经理主动选股。2026年一季报原始页：https://www.sse.com.cn/disclosure/fund/announcement/c/new/2026-04-22/512620_20260422_L7W6.pdf
- 中证农业主题指数选50只农业相关股票，但2026-06-30前十大占61.97%，依次含牧原、温氏、海大、盐湖、藏格、亚钾、正邦、梅花生物、新希望、生物股份。其真实暴露是养殖/饲料/动保与钾肥、锂资源的混合，既受猪周期影响，也受资源价格影响，不是粮价或种业纯主题。指数官方事实表稳定URL：https://oss-ch.csindex.com.cn/static/html/csindex/public/uploads/indices/detail/files/zh_CN/000949factsheet.pdf
- 前海开源农业015210对应的基金主代码为164403，是主动管理的沪港深农业LOF。2026-06-30前十大为天马科技7.92%、巨星农牧7.19%、牧原7.14%、中牧6.56%、海大5.99%、立华5.86%、现代牧业5.55%、优然牧业5.50%、华统5.18%、温氏4.80%，合计约62.69%。二季报提示性公告确认原文在基金公司和证监会披露，发布日期2026-07-21：https://paper.cnstock.com/html/2026-07/21/content_2246859.htm
- 015210比010770更集中于畜禽养殖、饲料和奶牛产业，且主动管理费率更高；两只基金与用户现有500股牧原直接持仓同时重叠。010770通过指数还持有盐湖、藏格等，亦与023037资源仓交叉。

### A500、港股科技与基建

- 022459的2026年二季报于2026-07-21披露；2026-06-30持有目标ETF 159361占基金净值91.95%，另有约1.97%直接股票，因此应按中证A500而非联接基金披露的零散新股理解风险。A类期末份额30.36亿份，二季度净值增长14.49%，过去一年37.05%，说明基本面和科技行情已带来明显估值/价格修复，不处于明显恐慌区。官方报告：https://cdn.efunds.com.cn/owch/data/bulletin/20260721/%E6%98%93%E6%96%B9%E8%BE%BE%E4%B8%AD%E8%AF%81A500%E4%BA%A4%E6%98%93%E5%9E%8B%E5%BC%80%E6%94%BE%E5%BC%8F%E6%8C%87%E6%95%B0%E8%AF%81%E5%88%B8%E6%8A%95%E8%B5%84%E5%9F%BA%E9%87%91%E8%81%94%E6%8E%A5%E5%9F%BA%E9%87%912026%E5%B9%B4%E7%AC%AC2%E5%AD%A3%E5%BA%A6%E6%8A%A5%E5%91%8A.pdf
- 013309的2026年二季报于2026-07-21披露；2026-06-30持有目标ETF 513010占净值94.53%，C类期末份额92.31亿份，二季度净值-4.85%、上半年-20.69%、过去一年-19.21%。官方报告：https://cdn.efunds.com.cn/owch/data/bulletin/20260721/%E6%98%93%E6%96%B9%E8%BE%BE%E6%81%92%E7%94%9F%E7%A7%91%E6%8A%80%E4%BA%A4%E6%98%93%E5%9E%8B%E5%BC%80%E6%94%BE%E5%BC%8F%E6%8C%87%E6%95%B0%E8%AF%81%E5%88%B8%E6%8A%95%E8%B5%84%E5%9F%BA%E9%87%91%E8%81%94%E6%8E%A5%E5%9F%BA%E9%87%91%EF%BC%88QDII%EF%BC%892026%E5%B9%B4%E7%AC%AC2%E5%AD%A3%E5%BA%A6%E6%8A%A5%E5%91%8A.pdf
- 恒生指数公司2026年6月事实表显示HSTECH为30只、自由流通市值加权、单股8%上限；2026-06-30 PE 27.56倍、股息率1.08%，近一年波动率27.12%。权重集中在中芯、网易、腾讯、美团、比亚迪、小米、阿里、华虹、百度、京东等，仍是高波动成长指数而非“低估值港股”整体。官方事实表：https://www.hsi.com.hk/static/uploads/contents/en/dl_centre/factsheets/hsteche.pdf
- 019934跟踪国证港股通科技指数987008，目标ETF为159636；2026年7月官方事实表显示可选消费41.70%、信息技术28.92%、医药卫生15.72%、电信11.58%，单股权重上限15%，前十大约80%。腾讯、阿里、小米、美团、比亚迪、中芯与HSTECH高度重叠，同时额外集中百济神州、药明生物、信达生物。官方事实表：https://www.cnindex.com.cn/html2pdf/preview/jj_987008.pdf
- 因此019934不是013309的有效分散：共同核心持仓仍由腾讯、阿里、小米、美团、比亚迪、中芯和快手驱动；差异主要是019934更集中并叠加创新药，单一指数规则和政策风险更高。
- 005224二季报显示2026-06-30持有目标ETF 516970占净值95.16%，C份额净资产约4.65亿元，二季度净值-6.27%、成立以来-18.72%；C份额期内赎回3.17亿份、高于申购1.78亿份。官方报告：https://www.gffunds.com.cn/jjgg/dqgg/202607/P020260720325300006698.pdf
- 中证基建工程指数2026-06-30事实表显示50只、100%工业，PE 10.06倍、PB约0.6倍、股息率2.78%，近三个月-6.98%、五年年化0.96%。前十大以中国建筑、中国中铁、中国电建、中国能建、中国铁建、中国化学等建筑央企为主，并纳入金诚信、亚翔集成、汇绿生态、太极实业等；低估值同时反映低ROE、回款和地方财政约束，不是无条件安全边际。官方事实表：https://oss-ch.csindex.com.cn/static/html/csindex/public/uploads/indices/detail/files/zh_CN/399995factsheet.pdf

### 检索与工具记录

- 广发PDF经Jina Reader只返回隐藏iframe提示，改为下载原始PDF并用uv临时加载pypdf解析；系统未安装pdftotext，Windows应用别名python也不可用。原始PDF与基金公司公告页交叉确认一致。
- 下跌性质定性为估值和拥挤交易消化为主、基本面破坏为辅；高铜铝价格、出口和关税不确定性、订单兑现节奏及应收账款仍需跟踪。
- 当前动作：持有，不在7月23日约5%的反弹后补仓。若净值回到1.06-1.09且无基本面恶化，可补30元；回到0.98-1.03可再补30-50元；跌破0.95先重估，不机械补。
- 主题仓按基金总资产5%-6%设上限；当前仓位已接近该范围，后续总新增暂不超过100元，优先级低于A500、标普500和红利低波等核心底仓。

## 牧原股份摩根士丹利转录稿核验｜2026-08-04

### 可靠部分
- 公司2026年半年度业绩预告确认归母净亏损57亿至67亿元，商品猪销售均价约10.4元/公斤，同比下降约28%。
- 2026年6月公司商品猪销售均价9.69元/公斤；公开交流显示6月完全养殖成本约11.7元/公斤，短期养殖业务仍处亏损。
- 2025年平均完全成本约12元/公斤，公司2026年全年目标为11.5元/公斤以下。成本领先、规模、疫病防控和一体化模式构成相对竞争优势。
- 行业生产效率提高会削弱单纯母猪去化对未来出栏量的影响，这是转录稿最有价值的行业判断。

### 需要打折或无法核验的部分
- 未检索到可公开访问的摩根士丹利报告原文，无法独立确认48元/49港元目标价、2026年EPS -0.72元、2027年EPS 3.68元和2027年三季度反弹等具体口径。公开可见的较早摩根士丹利摘要仍是57元目标价和2026年下半年拐点，可能是报告后来下调，也可能是视频混合了不同版本。
- 转录稿采用8840万头出栏量，但公司2026年正式指引为7500万至8100万头，二者明显不一致。
- 按猪价11元/公斤、成本11.5元/公斤、126公斤/头计算，7500万至8100万头对应约47亿至51亿元负养殖价差；即使采用8840万头也约为负56亿元，无法同时得到养殖板块正毛利润14亿元。该处大概率存在转述、单位或口径错误。
- MSY口径不统一。公开行业资料给出2025年全国平均MSY约21.52头，另有专家口径为22至24头；牧原公开评级材料披露的是PSY 28+，不能直接把视频的牧原MSY 25与行业20视作同口径精确比较。
- 2026年二季度末全国能繁母猪已降至3780万头，环比下降3.2%，距3750万头新目标仅0.8%；这削弱了“去产能仍极慢”的绝对表述。但同期生猪存栏仍约4.25亿头、生产效率提高且传导有时滞，短期供给宽松判断仍成立。

### 投资解释
- “下行周期中受益”只能解释为牧原相对同业更能生存、可能提升份额，不能解释为公司绝对利润或股价立即受益。长期低价仍会造成亏损、现金消耗和估值下修。
- 牧原是周期股，低谷期用下一年预测PE判断“历史底部”具有循环论证风险。更应跟踪猪价减完全成本的持续价差、母猪与仔猪、出栏体重、现金流、债务和屠宰利润。
- 2026-08-04 13:40行情约37.95元，用户500股平均成本37.812元，基本接近盈亏平衡。该转录稿不足以触发加仓或减仓，维持黄灯观察和基本面优先纪律。
- 下一验证点为7月销售简报、半年报现金流和负债、连续至少4周公司销售均价覆盖完全成本，以及母猪去化是否被补栏和效率提升抵消。

## 2026-08-05 中国科技三类基金底层基本面与风险

### 研究边界
- 基金：富国014777、天弘011840、天弘014881。
- 只研究标的指数结构、产业兑现、估值或拥挤度、政策与外部风险、近期行情触发因素。
- 2026数据仅在官方披露或可交叉核验时采用；无法确认项明确标注。

### 已确认：基金与指数身份
- 014777为富国中证芯片产业ETF发起式联接C，目标ETF跟踪中证芯片产业指数H30007。
- 011840为天弘中证人工智能主题指数C，跟踪中证人工智能主题指数930713。
- 014881为天弘中证机器人ETF发起联接C，目标ETF跟踪中证机器人指数H30590。

### 已确认：指数编制与首轮快照
- H30007：过去一年日均成交额剔除后20%，主题待选中按过去一年日均总市值取前50；芯片业务占比较低的样本单股权重不超过5%，其他样本不超过10%；每年6月、12月调整。
- 930713：中证官方指数单张日期为2026-06-30，样本50只；当日滚动PE 61.94倍、PB 9.84倍、股息率0.44%，近1月13.32%、近3月55.09%、年初至今45.19%、近1年128.72%，1年年化波动率36.71%。
- H30590：选取系统方案商、系统集成商、自动化设备、底层零部件及其他机器人公司，按过去一年日均总市值取前100（不足则全纳入），单股权重不超过10%，每年6月、12月调整。
- 待补：H30007和H30590的2026-06-30最新单张、三条指数前十大权重精确加总与行业集中度。

### 已确认：2026-06-30官方指数单张
- H30007：50只，滚动PE 125.45倍、PB 13.59倍、股息率0.10%，近1月36.26%、近3月108.62%、年初至今98.34%、近1年176.67%，1年年化波动率40.42%；行业权重100%为信息技术。
- 930713：50只，滚动PE 61.94倍、PB 9.84倍、股息率0.44%，近1月13.32%、近3月55.09%、年初至今45.19%、近1年128.72%，1年年化波动率36.71%；信息技术68.4%、通信服务28.6%、可选消费2.0%、工业1.0%。
- H30590：64只，滚动PE与PB均显示“--”、股息率0.41%，近1月2.65%、近3月25.08%、年初至今12.85%、近1年35.07%，1年年化波动率27.38%；工业64.8%、可选消费18.6%、信息技术14.9%、公用事业1.2%、医药卫生0.5%。PE缺失不能解释为低估，应视为指数整体盈利口径不具可比性或含亏损样本。
- 三份单张由Agent Reach的Jina Reader读取，PDF发布时间为2026-07-30，数据日期统一为2026-06-30。

### 已确认：2026-06-30前十大与集中度
- H30007前十大合计56.14%：兆易创新9.17%、寒武纪8.44%、北方华创6.45%、澜起科技5.99%、中微公司5.92%、海光信息5.80%、中芯国际5.45%、佰维存储3.14%、江波龙3.01%、拓荆科技2.77%。
- 930713前十大合计65.15%：寒武纪10.66%、新易盛9.81%、中际旭创9.19%、澜起科技9.14%、海光信息8.86%、中科曙光4.04%、芯原股份4.02%、海康威视3.23%、光迅科技3.20%、协创数据3.00%。
- H30590前十大合计60.00%：大族激光10.58%、汇川技术9.01%、三花智控8.40%、科大讯飞6.72%、中控技术6.37%、恒立液压4.94%、绿的谐波4.59%、拓普集团4.20%、大华股份2.77%、双环传动2.42%。
- 重叠风险：寒武纪、海光信息、澜起科技同时进入芯片与AI前十大；科大讯飞和大华股份同时进入AI或机器人主题的核心样本。三只产品不能视为彼此独立的风险桶。

### 来源补充
- 中证H30007指数单张：https://oss-ch.csindex.com.cn/static/html/csindex/public/uploads/indices/detail/files/zh_CN/H30007factsheet.pdf
- 中证H30590指数单张：https://oss-ch.csindex.com.cn/static/html/csindex/public/uploads/indices/detail/files/zh_CN/H30590factsheet.pdf

### 2026盈利与订单：首轮已确认
- 海光信息2026-07-17自愿披露上半年业绩预告：营收85亿至93亿元，同比+55.56%至+70.20%；归母净利17亿至18.3亿元，同比+41.50%至+52.32%；扣非净利15.1亿至17亿元，同比+38.53%至+55.96%。公司归因于AI大模型、AI Agent和国产化商业应用，但数据未经审计，正式半年报尚待披露。
- 光迅科技2026-07-15业绩预告：上半年归母净利5.5855亿至6.1497亿元，同比+50.00%至+65.15%；扣非净利同比+51.31%至+66.59%。公司称全球AI算力投资和国内云服务商数据中心投入推动数通光模块需求。
- 新易盛2026-07-19业绩预告：上半年归母净利70亿至80亿元，同比+77.56%至+102.93%；扣非净利69.81亿至79.81亿元，同比+77.46%至+102.88%。2026-07-20投资者交流中公司称三、四季度及明年订单能见度较高，800G已为主力、1.6T二季度环比明显增长并预计下半年进一步放量；该订单口径来自公司交流但仍未经过正式半年报确认。
- 中芯国际2026Q1：收入176.17亿元，同比+8.1%；归母净利13.61亿元，同比+0.4%；产能利用率93.1%，期末折合8英寸月产能107.825万片，资本支出108.71亿元。公司给出2026Q2收入环比+14%至+16%、毛利率20%至22%的指引，并称基于客户需求和在手订单对全年更乐观。全年资本开支指引与2025年81亿美元大致持平。制造端高利用率和扩产兑现，但Q1利润弹性明显弱于收入/订单景气。
- 兆易创新2026-07-10业绩预告：上半年营收约115亿元，同比+177%；归母净利约69亿元，同比+1099%；扣非净利约48.5亿元，同比+791%。公司称存储芯片供给紧张、产品量价齐升，同时明确提示存储周期波动和证券投资公允价值变动风险；归母与扣非相差约20.5亿元，利润质量需以半年报拆分复核。
- 澜起科技2026-07-17业绩预告：上半年营收约33.35亿元，同比+26.6%；归母净利19亿至21亿元，同比+63.9%至+81.2%；扣非净利12.5亿至14.5亿元，同比+14.5%至+32.9%。互连芯片收入约31.11亿元，同比+26.4%，Q2互连收入环比+19.5%；DDR5 RCD和MRCD/MDB、PCIe Retimer等新品兑现，但归母增速明显高于扣非，投资收益及公允价值变动也有贡献。

### 来源
- 海光信息2026H1业绩预告转录页（原公告日期2026-07-17）：https://money.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12450844&stockid=688041
- 光迅科技2026H1业绩预告转录页（原公告日期2026-07-15）：https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12444965&stockid=002281
- 新易盛2026H1业绩预告和投资者交流补充：https://www.thepaper.cn/newsDetail_forward_33623893
- 中芯国际2026Q1报告：https://www.hkexnews.hk/listedco/listconews/sehk/2026/0514/2026051400914_c.pdf
- 中芯国际2025业绩及2026全年资本开支指引：https://www.hkexnews.hk/listedco/listconews/sehk/2026/0210/2026021000526_c.pdf
- 兆易创新2026H1业绩预告转录页（原公告日期2026-07-10）：https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12438158
- 澜起科技2026H1业绩预告转录页（原公告日期2026-07-17）：https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?CompanyCode=81585146&gather=1&id=12451057

### 基金规模与拥挤度补充
- 天弘中证人工智能2026Q2报告：截至2026-06-30总份额23.557亿份，A/C合计净资产约52.26亿元；C类单季净值增长52.37%，同期业绩基准+51.90%。前十大指数投资占基金净值约62.02%，与官方指数前十大65.15%的差异主要来自基金约95%股票仓位。季度高涨幅、61.94倍指数PE和65.15%指数前十大集中度共同构成拥挤证据。
- 富国014777为目标ETF联接，合同要求投资目标ETF比例原则上不低于基金资产净值90%；2026-03-24起管理费0.15%/年、托管费0.05%/年，C类销售服务费0.20%/年。其风险几乎来自目标ETF和H30007，而不是基金经理主动选股。
- 富国014777与天弘014881的2026Q2报告均已确认于2026-07-21披露，但当前官网/代销抓取页混有Q1缓存；在取得原报告前，不以Q1规模替代2026-06-30规模。

### 来源
- 天弘中证人工智能2026Q2报告PDF：https://static.howbuy.com/gkxx/ggfile//2026/2026-7/2026-07-21/5391737.pdf
- 富国014777官方产品页：https://wap.fullgoal.com.cn/fundDetail/014777/index.html

### 机器人产业兑现与政策
- 国家统计局2026-07-15数据：2026年上半年工业机器人产量537,689套，同比+28.0%；服务机器人10,319,211套，同比+11.9%。国家统计局进一步披露，上半年机器人减速器产量同比+57.3%。量产景气已兑现，但统计口径是行业产量，不能直接等同于H30590成分股收入或利润。
- 工信部、国务院国资委2026年度实景实训专项行动要求：到2026年底，人形机器人等重点产品在代表性场景完成应用验证和常态部署，形成百个以上高价值场景并带动万台级规模落地能力。政策强调作业成功率、效率、安全可靠性、经济可行性和验证报告，说明产业仍处应用验证向规模部署过渡期，并非所有部件企业已经获得可确认利润。
- 科大讯飞2026-07-15业绩预告：上半年归母净亏损1.80亿至2.28亿元，较上年亏损收窄5%至25%；扣非净亏损6.0亿至6.75亿元，同比扩大65%至85%。合同额同比+27%、回款约118亿元并增加约15亿元，但研发投入超过28亿元、同比增加约5亿元，投入仍压制利润。科大讯飞占H30590权重6.72%，也是机器人指数盈利口径失真的重要样本之一。
- 大族激光2026-07-21业绩快报：上半年营收134.13亿元，同比+76.19%；归母净利12.86亿元，同比+163.47%；扣非净利13.94亿元，同比+434.13%；新签订单约160亿元，同比增100%以上。增长主要来自AI PCB、消费电子、锂电及半导体设备、通用工业激光设备，不是人形机器人收入。其作为H30590第一大权重10.58%，说明“机器人指数”实际混合了AI资本开支、消费电子和通用设备周期。
- 汇川技术2026Q1营收101.43亿元，同比+12.98%，归母净利10.13亿元，同比-23.39%；三花智控2026Q1营收77.74亿元，同比+1.36%，归母净利9.28亿元，同比+2.68%。两者合计占H30590约17.41%，利润增长明显弱于指数主题热度。汇川数据目前仅找到公司公告的新闻转述；三花来自公司一季报转录页。

### 来源
- 国家统计局2026年6月工业生产数据：https://www.stats.gov.cn/sj/zxfb/202607/t20260715_1964123.html
- 国家统计局2026上半年工业结构解读：https://www.stats.gov.cn/xxgk/jd/sjjd2020/202607/t20260716_1964141.html
- 工信部/国资委2026人形机器人与具身智能实景实训专项行动：https://www.miit.gov.cn/jgsj/kjs/wjfb/art/2026/art_cd666691abf8471fb8553d463aa416e3.html
- 科大讯飞2026H1业绩预告转录页（原公告日期2026-07-15）：https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12446483&stockid=002230
- 大族激光2026H1业绩快报（巨潮原始PDF）：https://static.cninfo.com.cn/finalpage/2026-07-21/1225433787.PDF
- 三花智控2026Q1报告转录页：https://money.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12285147&stockid=002050
- 汇川技术2026Q1公告新闻转述：https://finance.sina.com.cn/jjxw/2026-04-27/doc-inhvxxww9017155.shtml

### 来源
- 中证H30007编制方案：https://oss-ch.csindex.com.cn/static/html/csindex/public/uploads/indices/detail/files/zh_CN/20231208180055-H30007_Index_Methodology_cn.pdf
- 中证930713指数单张：https://oss-ch.csindex.com.cn/static/html/csindex/public/uploads/indices/detail/files/zh_CN/930713factsheet.pdf
- 中证H30590编制方案：https://oss-ch.csindex.com.cn/static/html/csindex/public/uploads/indices/detail/files/zh_CN/20231208180051-H30590_Index_Methodology_cn.pdf
## 2026-08-15 腾讯六份抖音稿核验（进行中）

### 官方二季度数据
- 腾讯 2026Q2 收入 2047.85 亿元，同比 +11%；IFRS 归母净利润 560.22 亿元，同比 +0.7%；Non-IFRS 归母净利润 684.15 亿元，同比 +9%。
- “不计新AI产品”的 Non-IFRS 经营利润为 861 亿元，同比 +19%。该口径不是净利润，也不能直接称为“腾讯真实利润”；它排除了元宝、WorkBuddy、CodeBuddy、小微等新AI产品的贡献与成本。
- 增值服务收入 +8%，其中本土游戏 +17%、国际游戏按报表口径 -0.8%（固定汇率 +4%）；营销服务 +22%；金融科技及企业服务 +9%。转录稿把增值服务整体说成“接近20%”不准确。
- 微信及 WeChat 合并月活 14.39 亿，同比 +2%；QQ 移动月活 5.20 亿，同比 -2%；收费增值服务账户 2.59 亿，同比 -2%、环比 -3%。视频号使用时长同比 +20%。
- Q2 总资本开支 527.84 亿元，同比 +176%；其中经营性资本开支 518 亿元，同比 +190%。转录稿中的“+109%”错误。
- Q2 自由现金流为 -138 亿元，净现金从 Q1 的 1468.6 亿元降至 581.9 亿元；同期派息 416 亿元、回购 147 亿元。AI算力预付款调整口径仍待电话会核验。
- 联营/合营公司份额由盈利转为亏损约 100 亿元，主要源于一家未上市被投公司的可转换可赎回优先股公允价值变动；这解释了 IFRS 与 Non-IFRS 利润增速的差异。博主的方向基本正确，但把 0.7%、9%、19%统称为“真假利润”会误导。

### 六份稿件的初步可信度
- AI产品稿：WorkBuddy 在易观 2026年6月“中国PC端AI原生办公智能体月交互量”中排名第一，2750万次，确实高于第二、第三名之和；但这不是月活或全平台流量，不能外推为全面领先。
- “算力可外租”有官方背书：腾讯称若内部需求不足，可经腾讯云对外出租并获得有吸引力的价格；“几个月前买入的算力可贵30%卖出”尚未在官方材料中核实。
- “腾讯用户时长份额29.7%、字节40.1%”来自外部机构口径，尚待找到原始报告；即使属实，也不能直接等同于利润份额或微信生态衰退。
- “腾讯业务利润53%来自增值服务、约30%金融科技、约20%广告”与官方分部毛利润占比大致相符，但腾讯不披露分部经营利润，称作“利润结构”不够严谨。
- 用季度EPS乘4得到年化盈利，再把盈利收益率与回购/分红率直接相加，会受季节性影响并存在重复计算风险，不能作为腾讯预期收益率的可靠公式。
- “AI流量五年达到人类流量1000倍”“WorkBuddy是腾讯第三个战略级产品”等更接近观点或内部消息，不能当作已证实的投资前提。

### 工具与证据说明
- 本机无 `pdftotext`，直接抽取官方PDF失败；改用 Agent Reach 的 Jina Reader读取腾讯官方业绩公告和演示材料成功。

### 公司、组织与长期路径
- 腾讯官方仍为六大事业群：CDG、CSIG、IEG、PCG、TEG、WXG。投资分析更适合按“身份与关系—内容与娱乐—服务与交易—商业化—云和AI基础设施”的经济闭环理解。
- 微信、支付、小程序、商户、广告和内容形成从发现到付款的闭环；游戏则提供高毛利现金引擎和全球化。真正的护城河是多网络协同，不只是用户时长。
- 腾讯2025年底以来强化AI Infra、AI Data和基础模型组织，由姚顺雨统筹底层模型与基础设施；WorkBuddy采用3至5人小队快速试验。方向是“昂贵底座集中化、前线产品小队化”，但付费、留存和单位经济性仍待验证。
- AI回报应分三层：广告/游戏/云效率已经开始兑现；WorkBuddy和企业Agent处于商业化验证期；微信智能体交易闭环是高赔率期权，不能计入基础估值。
- Prosus截至2026-03-31持股22.66%并继续减持以支持自身回购；腾讯回购可部分吸收供给，但2026年回购将低于2025年，减持仍可能压制估值。

### 估值与执行结论
- 2026-08-14腾讯收盘440港元；按HKD/CNY约0.865和滚动四季Non-IFRS摊薄EPS 29.338元，调整后滚动PE约12.97倍。
- 2026年5月公开研报引用的Bloomberg一致预期EPS约30.4元，对应前瞻PE约12.52倍；财报后的最新预期可能变化。
- 当前人民币市值约3.46万亿元；上市投资公允价值4870亿元、未上市投资账面值3880亿元、净现金582亿元，合计约9332亿元。保守处理折价和重复计算后，核心业务隐含约10至11倍调整后盈利。
- 12至18个月情景区间：悲观330至380港元，基准480至550港元，乐观620至700港元。440港元属于可分批建仓但非重仓抄底区。
- 建议3至5年以上持有；430至450港元只建目标仓位1/5，395至415港元且逻辑未坏再加，350至380港元重新核验后才加大；500港元以上若盈利未上调则不追。
- 腾讯每手100股，440港元约需4.4万港元、约3.8万元人民币。若一手超过用户单股目标仓位，应通过现有港股科技/恒生科技基金参与，不为最小交易单位破坏分批纪律。
