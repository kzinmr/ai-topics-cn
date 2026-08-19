---
title: "手搓 LangChain 工具调用：原来 Agent 的核心逻辑，就是个 while 循环"
source: juejin
url: "https://juejin.cn/post/7660857644618399780"
author: "To_OC"
date: 2026-07-11
score: 3
tags: ["LangChain", "人工智能", "LLM"]
---

# 手搓 LangChain 工具调用：原来 Agent 的核心逻辑，就是个 while 循环

直到我把完整的 response 打印出来，才发现返回的 AIMessage 里藏了个tool_calls数组，里面清清楚楚写着要调用read_file，参数就是我传的文件路径。合着模型根本没执行工具

> 👍 3   👁️ 0   ⭐ 3

## 涉及话题
- LangChain
- 人工智能
- LLM

[原文链接](https://juejin.cn/post/7660857644618399780)
