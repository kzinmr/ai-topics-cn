---
title: "Codex agentic loop 会导致代码严重膨胀，有人遇到吗？有没有系统性的解法？"
source: v2ex
url: "https://www.v2ex.com/t/1208629"
author: "longxinglink"
date: 2026-04-26
score: 2
tags: ["rag"]
---

# Codex agentic loop 会导致代码严重膨胀，有人遇到吗？有没有系统性的解法？

具体案例：V2EX Safe Reading Helper 5.3.0，一个油猴脚本，核心逻辑不复杂，但 530 行里能清楚看到几层叠加痕迹：

topic 来源从 API 一路加到 /recent、节点页、ID 逐个扫描——每次拿不到帖子就加一个 fallback ，互相没有合并
两套 refill 防重入并存（isRefilling flag + refillPromise 互斥）
legacy key 迁移代码永远留在运行时，跑一次之后就是死代码
hasGMStorage() 每次读写都检测，而不是初始化时确定一次
对一个翻页脚本加了完整的白屏 watchdog + 自动刷新恢复机制

模型每次报错就往上堆，不回头清理，不合并逻辑。
有没有系统性的解法？还是说这就是现阶段 agentic coding 的固有缺陷？

## 涉及话题
- rag

[原文链接](https://www.v2ex.com/t/1208629)
