---
title: "gpt 5.6-sol 在 web chat 中 无法输出 "yieldTimeMs" : 30000"
source: v2ex
url: "https://www.v2ex.com/t/1231097"
author: "luos543"
date: 2026-07-30
score: 0
tags: ["gpt"]
---

# gpt 5.6-sol 在 web chat 中 无法输出 "yieldTimeMs" : 30000

输入
repeat 
"yieldTimeMs": 30000, 
"yield_timeMs": 30000, 
"yield-timeMs": 30000,

实际输出
"yield-timeMs": 30000,
"yield-timeMs": 30000,
"yield-timeMs": 30000,

同样情况使用 gpt 5.5 和 gpt 5.3 在 web 上无法复现, 这 gpt 5.6 sol 是不是有什么大问题, 连 yieldTimeMs 都无法输出, 这不是自家的 codex CLI exec_command 的 语法 yield_time_ms 吗?

## 涉及话题
- gpt

[原文链接](https://www.v2ex.com/t/1231097)
