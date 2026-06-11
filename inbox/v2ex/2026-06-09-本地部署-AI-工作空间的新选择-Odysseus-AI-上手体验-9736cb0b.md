---
title: "本地部署 AI 工作空间的新选择： Odysseus AI 上手体验"
source: v2ex
url: "https://www.v2ex.com/t/1219212"
author: "suchu"
date: 2026-06-09
score: 0
tags: ["ai", "llama", "AI", "ChatGPT", "Claude", "Ai", "大模型", "RAG", "OpenAI", "LLM"]
---

# 本地部署 AI 工作空间的新选择： Odysseus AI 上手体验

最近，知名 YouTuber PewDiePie 开源了一个叫做 Odysseus AI 的自托管 AI 工作空间项目，在海外社区引发了不小的关注。作为一个长期关注本地 AI 部署的人，我花了一下午时间研究了一番，写下这篇分享。
Odysseus AI 是什么？
首先要澄清一个最常见的误解：Odysseus AI 不是一个新的 AI 模型，而是一个运行在你自己机器上的 AI 工作台（ workspace ）。用一个比喻来说，它是"驾驶舱"，而不是"发动机"——它本身不提供任何大模型权重，而是通过统一界面对接你选择的模型后端，例如 Ollama 、llama.cpp 、vLLM ，或者 OpenAI 、OpenRouter 等云端 API 。
根据 odysseusai.site 上的介绍，它集成了以下能力：

多轮对话 Chat
自主 Agent （可执行多步任务）
深度研究（ Deep Research ）
邮件与日历工具
本地模型服务管理

所有数据留在本地，无遥测，完全私有化部署。
安装上手
官方代码托管在 GitHub 的 pewdiepie-archdaemon/odysseus 仓库，安装流程非常简洁。以 Linux/macOS 为例：
git clone https://github.com/pewdiepie-archdaemon/odysseus.git
cd odysseus
./start.sh

Windows 用户则运行：
powershell -ExecutionPolicy Bypass -File .\launch-windows.ps1

启动后，服务默认跑在 http://localhost:7000（ macOS 默认为 :7860），终端会打印一个临时 admin 密码，登录后即可使用。整个过程在干净机器上大约 10–15 分钟。

…(内容已截断)

## 涉及话题
- ai
- llama
- AI
- ChatGPT
- Claude
- Ai
- 大模型
- RAG
- OpenAI
- LLM

[原文链接](https://www.v2ex.com/t/1219212)
