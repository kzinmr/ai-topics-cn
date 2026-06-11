---
title: "Langgraph踩坑记录"
source: juejin
url: "https://juejin.cn/post/7646002025647718415"
author: "_Programmer"
date: 2026-06-01
score: 0
tags: ["Prompt", "LangChain"]
---

# Langgraph踩坑记录

1. 当你用到返回格式需要是json_object时 你现在的 System Prompt 是： 里面完全没有 json → 所以报错！ 怎么修？ 只需要在你的 SystemMessage 里加一个

> 👍 0   👁️ 0   ⭐ 0

## 涉及话题
- Prompt
- LangChain

[原文链接](https://juejin.cn/post/7646002025647718415)
