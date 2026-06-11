---
title: "给 AI Agent 造了个免费股票数据弹药库 — pip install 装了就能跑"
source: v2ex
url: "https://www.v2ex.com/t/1218903"
author: "handsomejustin80"
date: 2026-06-08
score: 0
tags: ["AI", "LLM", "AI Agent", "Claude"]
---

# 给 AI Agent 造了个免费股票数据弹药库 — pip install 装了就能跑

量化机构花百万买的毫秒级行情通道，散户连一根日线都得手动截图。

我不想抱怨这事，我直接造了个开源工具把墙拆了。

easy-tdx：免费、无注册、无 API Key 的行情数据源

GitHub: https://github.com/handsomejustin/easy-tdx

一行命令装上，30 秒后你屏幕上的数据和机构看到的是同一份。

pip install easy-tdx

它能干嘛？

拉数据：A 股、港股、美股、期货 —— K 线、实时报价、分时明细、逐笔成交、资金流向、板块轮动，毫秒级返回。

# 茅台日 K 线
easy-tdx kline SH 600519 --count 30 --table

# 港股腾讯
easy-tdx ex kline HK_MAIN_BOARD 00700 --count 30 --table

# 美股苹果
easy-tdx ex kline US_STOCK AAPL --table

# 全 A 股按涨幅排序
easy-tdx quote-list A --count 20 --table

算指标：32 个技术指标开箱即用 —— MACD 、KDJ 、RSI 、BOLL 、DMI 、ATR 、WR 、CCI 、BIAS……连"捉妖大师"和"30 日乖离率信号"都给你算好了。

easy-tdx indicator MACD,KDJ,RSI,BOLL -m SH -c 600519 --count 20 --table

缠论分析：K 线合并→分型→笔→中枢→线段→买卖点→背驰，一键出结果。

easy-tdx chanlun SZ 000001 --table

为什么说它是 AI Agent 的天然弹药？


…(内容已截断)

## 涉及话题
- AI
- LLM
- AI Agent
- Claude

[原文链接](https://www.v2ex.com/t/1218903)
