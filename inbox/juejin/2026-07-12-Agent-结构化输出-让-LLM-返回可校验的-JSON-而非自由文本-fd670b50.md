---
title: "Agent 结构化输出 —— 让 LLM 返回可校验的 JSON，而非自由文本"
source: juejin
url: "https://juejin.cn/post/7661251852345769993"
author: "RebornL"
date: 2026-07-12
score: 1
tags: ["LLM"]
---

# Agent 结构化输出 —— 让 LLM 返回可校验的 JSON，而非自由文本

前几篇文章的 Agent 输出是自由文本，下游系统只能用正则解析，脆弱且不可靠。本文拆解 Structure.py 的 ~140 行实现：把输出也变成一个 Tool，LLM 调用 final_outp

> 👍 1   👁️ 0   ⭐ 0

## 涉及话题
- LLM

[原文链接](https://juejin.cn/post/7661251852345769993)
