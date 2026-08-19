---
title: "memU：给 Claude Code、OpenClaw、Hermes 装上共享 memory 层"
source: v2ex
url: "https://www.v2ex.com/t/1231096"
author: "Daniel6606"
date: 2026-07-30
score: 4
tags: ["OpenAI", "Prompt", "向量数据库", "AI Agent", "GPT", "推理", "Embedding", "Claude", "AI", "ai", "llama", "LLM", "Cursor", "prompt"]
---

# memU：给 Claude Code、OpenClaw、Hermes 装上共享 memory 层

hihi 朋友们，我是 memU 团队的工程师
今天想给大家分享一个我们一直在打磨的开源项目：memU ，一个面向个人开发者和极客的轻量级 Agent 记忆层。说人话就是：给你常用的几个 Agent 装上同一个大脑，让它们之间互相认识。
定位和 mem0 ，Zep ，Letta （原 MemGPT ）差不多，都是 AI 记忆层的赛道，但我们走了和他们完全不同的路：我们摒弃了传统的记忆框架的臃肿，把代码从 3 万行缩短到了 500 行，只要会用 Agent 的人都可一行 prompt 以轻松部署
GitHub：github.com/NevaMind-AI/memU （求个 Star ～⭐）
官网：memu.pro
一、为什么做这件事
现在用 AI Agent 干活的人越来越多：用 Claude Code 写代码、Cursor 改前端、Hermes 跑 cron job 自动化任务；但用过一段时间，绝大多数人都会撞上同一堵墙：记忆孤岛。
每个 Agent 都是独立的会话。早上用 Claude Code 配好的项目环境，下午切到 Cursor 又要重新讲一遍。台式机上调教好的偏好设置，换到 macbook 上一切归零
市面上不是没有记忆方案，但要么太重（ Docker + 向量数据库 + 多阶段 LLM Pipeline ），要么只绑死在一个工具上（比如只能给 Claude 用）。
我们想要的是一个能让所有 Agent 都接入、部署足够轻、数据自己能掌控的记忆层。
这就是今天的 memU 。
二、就三个功能，没有第四个
① 跨 Agent 、跨设备共享记忆
Claude Code 、Codex 、Cursor 、Hermes 、OpenClaw 全部共用同一层记忆库。上午在台式机用 Claude Code 学到的项目上下文，下午笔记本上的 Cursor 直接就能检索到。


…(内容已截断)

## 涉及话题
- OpenAI
- Prompt
- 向量数据库
- AI Agent
- GPT
- 推理
- Embedding
- Claude
- AI
- ai
- llama
- LLM
- Cursor
- prompt

[原文链接](https://www.v2ex.com/t/1231096)
