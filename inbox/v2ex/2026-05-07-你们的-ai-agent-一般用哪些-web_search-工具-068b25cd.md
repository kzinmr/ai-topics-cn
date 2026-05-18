---
title: "你们的 ai agent 一般用哪些 web_search 工具？"
source: v2ex
url: "https://www.v2ex.com/t/1211001"
author: "lynn1su"
date: 2026-05-07
score: 3
tags: ["openai", "gemini", "mcp", "ai agent", "ai"]
---

# 你们的 ai agent 一般用哪些 web_search 工具？

楼主用了 16 个工具
1.minimax （ cli+mcp ）
2.step
3.baidu
4.baidu ai search
5.tavily
6.doubao
7.bailian
8.exa
9.brave
10.linkup
11.serpapi
12.bocha
13.openai
14.grok
15.duckduckgo （ hermes agent 自带搜索工具）
16.gemini
目前这些都是免费的
之前楼主都是全部写入我的 agent ，然后让自己的 agent 装上，然后一股脑全部调用，然后发现太耗费 token 了，
然后就弄了个子 agent ，用 minimax-m2.7 ，专门用来提炼+总结，
如果主 agent 需要搜索就派发任务给子 agent ，然后子 agent 反馈给主 agent ，然后主 agent 屏蔽自身的所有搜索功能。
目前是这个玩法
大家是怎么玩的？
------------------------------------------------------------------------
然后所有搜索工具，如果是原始搜索的，返回条目拉到最大。
如果是 ai 总结的，有挡位的调到最大
mcp 用的是自己写的 mcp 工具，把所有搜索汇集在一起了

## 涉及话题
- openai
- gemini
- mcp
- ai agent
- ai

[原文链接](https://www.v2ex.com/t/1211001)
