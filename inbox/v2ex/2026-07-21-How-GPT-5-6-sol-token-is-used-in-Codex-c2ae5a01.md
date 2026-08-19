---
title: "How GPT-5.6 sol token is used in Codex"
source: v2ex
url: "https://www.v2ex.com/t/1228941"
author: "yohjisakamoto"
date: 2026-07-21
score: 0
tags: ["ai", "LLM", "openai", "gpt", "GPT"]
---

# How GPT-5.6 sol token is used in Codex

我在 Codex CLI 上做了 280+ 次 GPT-5.6 Sol 测试。当前版本似乎仍有会增加 token 消耗的问题。
在多数基准中，GPT-5.6 Sol 的成本效益优于 GPT-5.5 。以 DeepSWE 为例：5.5 High 平均每任务 5.1 美元，5.6 Sol High 为 3.5 美元；但在 Codex CLI 0.144.1 ，我测到 5.6 Sol High 反而比 5.5 High 高约 21%。
https://preview.redd.it/how-gpt-5-6-sol-token-is-used-in-codex-v0-pghf32p14meh1.png?width=1080&crop=smart&auto=webp&s=1b501ae165714278d0e824a224f72fcb4dc730be
https://preview.redd.it/how-gpt-5-6-sol-token-is-used-in-codex-v0-esic3oac7meh1.png?width=1080&crop=smart&auto=webp&s=ffc29d6fdd8f3123f5eaec520889b470f1a9c406
可能原因是：5.5 明确使用 multi_tool_use.parallel，一轮可发出多个顶层工具调用； 5.6 多以单一顶层 exec 编排，因此每次 LLM 调用运行的命令更少（ 0.97 vs 2.5 ），同一任务的轮次却约为 1.84 倍。5.6 Sol High 的花费中约 66.5% 是缓存输入 token 。
代码位置：

…(内容已截断)

## 涉及话题
- ai
- LLM
- openai
- gpt
- GPT

[原文链接](https://www.v2ex.com/t/1228941)
