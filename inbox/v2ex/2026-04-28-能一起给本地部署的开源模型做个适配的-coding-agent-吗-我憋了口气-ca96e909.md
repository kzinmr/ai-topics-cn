---
title: "能一起给本地部署的开源模型做个适配的 coding agent 吗？我憋了口气"
source: v2ex
url: "https://www.v2ex.com/t/1209195"
author: "KaiWuBOSS"
date: 2026-04-28
score: 59
tags: ["Prompt", "微调", "LLM", "coding agent", "Claude", "qwen", "MCP", "ai", "llama", "prompt", "Qwen", "Cursor", "DeepSeek", "开源模型", "embedding", "GPT", "OpenAI", "Coding Agent", "推理", "Anthropic"]
---

# 能一起给本地部署的开源模型做个适配的 coding agent 吗？我憋了口气

我做了一个专门为本地开源模型优化的 Coding Agent ，希望更多华人开发者一起来搞

本贴发布的目的不是推产品，不是炫技，而是想扬眉吐气——和华人开发者一起，和开源模型本地部署开发者一起，做一件我们自己的事。


一、我遇到了什么问题
去年开始用本地模型做编程辅助。原因很简单：公司代码不能传到海外服务器，Claude Code 和 Cursor 走不通。
但更大的问题是：中国开发者根本没有一个好用的本地 coding agent 平台。
CC 需要翻墙，还要订阅。Cursor 同样。Codex 刚出来也是海外服务。Hermes 这类开源工具不支持 Windows 原生运行，要装 WSL2 ，劝退了大多数国内开发者。最后大家的选择是：要么翻墙凑合用，要么忍着不用。
这是一个真实存在的空缺，没有人填。
本地跑 qwen3:8b ，然后发现问题一个接一个：
🔴 无限循环，像卡带一样
这是本地小模型最让人抓狂的问题。遇到它不会处理的场景，它不会说"我不知道"，而是开始重复——同一句话说三遍，同一个错误的修改建议循环出现，同一段代码反复生成。整个任务卡死，只能手动强制退出。这不是偶发现象，是小模型在推理能力不足时的典型崩溃模式。
🔴 修 bug 反复踩同一个坑
让它修一个函数，第一次失败，第二次用完全一样的方式再试，第三次依然。三次机会全浪费在同一个错误上，什么都没推进。
🔴 模型能力本身就弱于 API 模型
这是无法回避的现实。8B 、14B 的参数量，推理能力和 Claude Opus 、GPT-4 差距明显。让一个 8B 模型扛下一个复杂任务的全部推理，成功率很低，这不是哪个工具的问题，是模型本身的边界。
🔴 找不到要改的文件

…(内容已截断)

## 涉及话题
- Prompt
- 微调
- LLM
- coding agent
- Claude
- qwen
- MCP
- ai
- llama
- prompt
- Qwen
- Cursor
- DeepSeek
- 开源模型
- embedding
- GPT
- OpenAI
- Coding Agent
- 推理
- Anthropic

[原文链接](https://www.v2ex.com/t/1209195)
