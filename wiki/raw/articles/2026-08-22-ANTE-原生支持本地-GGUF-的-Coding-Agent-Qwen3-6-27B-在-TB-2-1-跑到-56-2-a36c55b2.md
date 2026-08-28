---
title: "ANTE：原生支持本地 GGUF 的 Coding Agent， Qwen3.6 27B 在 TB 2.1 跑到 56.2%"
source: v2ex
url: "https://www.v2ex.com/t/1236484"
author: "Koimiao"
date: 2026-08-22
score: 0
tags: ["OpenAI", "Anthropic", "Coding Agent", "llama", "Gemini", "Claude", "LLM", "Qwen", "ai", "推理", "DeepSeek"]
---

# ANTE：原生支持本地 GGUF 的 Coding Agent， Qwen3.6 27B 在 TB 2.1 跑到 56.2%

ANTE 一个运行在终端里的 Coding Agent 。使用方式类似 Claude Code / Codex ，但它从头用 Rust 编写，下载包约 15 MB ，解压后是一个没有 Node.js 、Python 等运行时依赖的单文件程序。

ANTE 可以管理 llama.cpp 的安装、GGUF 模型发现、内存预估、加载进度和服务生命周期。模型下载完成后，不需要账号、API Key 或网络，模型请求和输出都留在本机。已经在使用 Ollama 、LM Studio 、vLLM 或其他 OpenAI-compatible 服务的话，也可以直接接入。

当然，它也支持 OpenAI 、Anthropic 、Gemini 、DeepSeek 、OpenRouter 等在线模型，可以在同一个客户端里切换本地和云端模型。

一些跑
使用 Terminal-Bench 2.1 评测 ANTE 的 agent harness 。测试采用 89 个任务、每个任务 5 次，共 445 次 trial ；每次评测固定公开发布的 ANTE 版本，并提供原始 Harbor run 。
目前公开结果包括：
- ANTE + DeepSeek V4 Flash 0731 max：82.7% ± 1.79 SE ，通过 368/445 次 trial ，完整评测推理成本约 68.41 美元。
- ANTE + 本地 Qwen3.6 27B Q4_K_M：56.2% ± 2.36 SE 。模型下载约 17 GB ，完全在本地运行。
- ANTE + GLM 5.2：74.6% ± 2.06 SE 。
- ANTE + MiniMax M3：62.1% ± 2.33 SE 。
完整结果、具体版本和原始运行记录都在这里： https://antigma.ai/eval


…(内容已截断)

## 涉及话题
- OpenAI
- Anthropic
- Coding Agent
- llama
- Gemini
- Claude
- LLM
- Qwen
- ai
- 推理
- DeepSeek

[原文链接](https://www.v2ex.com/t/1236484)
