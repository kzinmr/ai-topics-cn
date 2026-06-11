---
title: "easy-tdx：接手停更的 pytdx，加了 CLI 和 30 个技术指标"
source: v2ex
url: "https://www.v2ex.com/t/1216216"
author: "handsomejustin80"
date: 2026-05-28
score: 0
tags: ["AI Agent", "Claude"]
---

# easy-tdx：接手停更的 pytdx，加了 CLI 和 30 个技术指标

做量化或 A 股相关开发的人大概都知道 pytdx ，通达信 TCP 行情协议的 Python 客户端，用了好多年了。问题是这个项目已经很久没人维护了，issue 堆着没人回，最后几次提交还是几年前的事。

  我自己平时要用，就 fork 过来接着改。改着改着加了不少东西，干脆换了名字叫 easy-tdx ，重新发到 PyPI 上。目前版本 1.4.0 。

  加了个 CLI 工具，装好就有 easy-tdx 命令，默认输出 JSON 。这个设计是给 AI Agent 用的，Claude Code 、OpenClaw 、Hermes 这类工具可以直接调 CLI 拿行情数据，不用写 Python：

  easy-tdx kline SZ 000001 --count 30 --table
  easy-tdx quote "SZ 000001,SH 600519"
  easy-tdx indicator MACD,KDJ,RSI -m SH -c 600519 --table

  内置了 30 个技术指标，MACD 、KDJ 、RSI 、BOLL 、DMI 、ATR 这些常用的都有。直接拿 K 线数据算好返回 DataFrame ，不用自己再写一遍指标计算。底层用的是 MyTT （麦语言指标库），可以一次算多个：

  from easy_tdx import MacClient, Market

  with MacClient.from_best_host() as c:
      df = c.get_stock_kline_with_indicators(
          Market.SH, "600519",
          indicators=["MACD", "KDJ", "RSI", "BOLL"],

…(内容已截断)

## 涉及话题
- AI Agent
- Claude

[原文链接](https://www.v2ex.com/t/1216216)
