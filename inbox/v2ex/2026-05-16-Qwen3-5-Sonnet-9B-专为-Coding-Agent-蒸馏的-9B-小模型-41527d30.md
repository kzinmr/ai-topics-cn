---
title: "Qwen3.5-Sonnet-9B: 专为 Coding Agent 蒸馏的 9B 小模型"
source: v2ex
url: "https://www.v2ex.com/t/1213159"
author: "ytgui"
date: 2026-05-16
score: 4
tags: ["claude", "LLM", "Qwen", "Coding Agent", "Claude"]
---

# Qwen3.5-Sonnet-9B: 专为 Coding Agent 蒸馏的 9B 小模型

最近炼了一个小模型放出来给大家玩，专门针对 OpenCode （还有 Claude Code ）做了蒸馏。
FP8 量化后权重大概 13GB ，单张 24GB 显卡用 vLLM 就能跑 200K 上下文。
核心目标：claude 的风格，降低 tool call 的失败率，让 agent 能跑更长的连续任务。
蹲一下：Bug 反馈、奇怪的 trace 、改进建议都欢迎 🙏
🤗 HF: Qwen3.5-Sonnet-9B

## 涉及话题
- claude
- LLM
- Qwen
- Coding Agent
- Claude

[原文链接](https://www.v2ex.com/t/1213159)
