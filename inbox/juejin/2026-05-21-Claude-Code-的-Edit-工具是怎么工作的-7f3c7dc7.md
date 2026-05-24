---
title: "Claude Code 的 Edit 工具是怎么工作的"
source: juejin
url: "https://juejin.cn/post/7642229486806450227"
author: "candyTong"
date: 2026-05-21
score: 1
tags: ["Claude", "架构", "后端", "JavaScript"]
---

# Claude Code 的 Edit 工具是怎么工作的

Claude Code 修改文件的方式不是传行号，也不是打 AST patch。它让模型输出一段要替换的原文 old_string 和替换后的文本 new_string，由 Edit 工具完成实际写入

> 👍 1   👁️ 0   ⭐ 0

## 涉及话题
- Claude
- 架构
- 后端
- JavaScript

[原文链接](https://juejin.cn/post/7642229486806450227)
