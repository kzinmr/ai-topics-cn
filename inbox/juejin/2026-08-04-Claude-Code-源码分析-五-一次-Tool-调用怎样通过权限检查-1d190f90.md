---
title: "Claude Code 源码分析（五）：一次 Tool 调用怎样通过权限检查"
source: juejin
url: "https://juejin.cn/post/7669977060371185670"
author: "windliang"
date: 2026-08-04
score: 0
tags: ["Claude", "前端", "面试", "人工智能"]
---

# Claude Code 源码分析（五）：一次 Tool 调用怎样通过权限检查

上一篇走到 checkPermissionsAndCallTool() 时，权限部分只保留了一个结论：只有 behavior === 'allow'，才会执行 tool.call()。 继续往下读，先

> 👍 0   👁️ 0   ⭐ 0

## 涉及话题
- Claude
- 前端
- 面试
- 人工智能

[原文链接](https://juejin.cn/post/7669977060371185670)
