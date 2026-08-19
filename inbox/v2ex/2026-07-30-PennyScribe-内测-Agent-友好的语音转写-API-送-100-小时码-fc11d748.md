---
title: "PennyScribe 内测： Agent 友好的语音转写 API [送 100 小时码]"
source: v2ex
url: "https://www.v2ex.com/t/1231005"
author: "yedaxia"
date: 2026-07-30
score: 1
tags: ["Claude", "ai", "MCP", "Qwen", "AI Agent", "ChatGPT", "AI"]
---

# PennyScribe 内测： Agent 友好的语音转写 API [送 100 小时码]

大家好，我是叶大侠。
这是我第一次尝试完全依靠 AI 编程工具（ Codex ），从零到一开发一款产品。整个过程中，我自己一行代码都没有写。
转写模型使用的是 Qwen ASR ，GPU 算力来自 Vast.ai 。Vast.ai 的消费级 GPU 虽然价格便宜，但想把它做成稳定、可靠的在线服务，并不是一件容易的事。
为了兼顾成本与服务稳定性，我借助 Codex 放弃了官方的 Serverless 方案，从零构建了一套 GPU 实例调度系统。
这个过程中踩了很多坑，但非常值得。如果没有 Codex 的帮助，我估计至少需要 3 个月才能把这件事做好，而现在只用了不到两周——当然，对很多大佬来说，这个速度可能依然不算快。
接下来，郑重向大家介绍一下我的新产品：PennyScribe。
PennyScribe 是一款面向 AI Agent 和开发者的音频转写服务，可以将音频、视频中的语音快速转换为结构化文本，再交给 Agent 完成内容总结、知识提取、信息检索和自动化处理。
如果你曾经让 ChatGPT 或 Claude Code 处理音频转写任务，可能会发现它们经常需要先下载并运行 Whisper 。这不仅会让处理时间变得漫长，还可能因为设备性能不足或网络问题而中断。
这时，一个对 Agent 友好的云端语音转写服务就能派上用场。尤其是在需要批量处理大量音频时，云端多台 GPU 并行处理的优势会更加明显。
在测试过程中，我发现 Qwen ASR 的文本转写效果非常出色，但 Qwen ForcedAligner 生成时间戳的效果并不理想。去除背景音乐和环境噪声后会有所改善，但这也会增加处理流程的复杂度和计算成本。
因此，PennyScribe 现阶段决定先专注于一件事：把语音转写成高质量的纯文本。

…(内容已截断)

## 涉及话题
- Claude
- ai
- MCP
- Qwen
- AI Agent
- ChatGPT
- AI

[原文链接](https://www.v2ex.com/t/1231005)
