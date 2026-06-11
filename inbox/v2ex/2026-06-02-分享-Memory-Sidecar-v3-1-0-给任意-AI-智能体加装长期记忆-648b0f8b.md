---
title: "[分享] Memory Sidecar v3.1.0 — 给任意 AI 智能体加装长期记忆"
source: v2ex
url: "https://www.v2ex.com/t/1217342"
author: "cycloner"
date: 2026-06-02
score: 0
tags: ["embedding", "智能体", "AI", "Claude", "Cursor"]
---

# [分享] Memory Sidecar v3.1.0 — 给任意 AI 智能体加装长期记忆

AI 智能体有个硬伤：记不住你。每次新对话都是白纸一张。你上周讨论过的项目背景、写过的代码逻辑、提过的个人偏好，它全忘了。这不是你的问题，是所有对话式 AI 的天生缺陷。
Memory Sidecar v3.1.0 就是为了解决这个。它是一个外挂记忆系统，跑在你的智能体（ Hermes 、Claude Code 、Cursor 、Codex ，什么都行）旁边，不碰核心代码，独立进程、共享目录。装完你的智能体就有了三层记忆：热层（当前会话 context ）→ 温层（ PostgreSQL 事实图谱，50ms 级召回）→ 冷层（知识图谱 + 十万条消息的全文搜索）。
说人话就是：它帮你智能体记住了所有聊过的东西，并且知道在什么时候把什么拿出来。
架构很薄。去掉了之前那个笨重的 Docker 中间层，现在三层的故障点更少，部署一条命令搞定。支持重点档案（ Focused Dossier ）——比如某个重要的人、长期项目、反复出现的故障，可以单独追踪、优先召回。
生产数据来自一台连续跑了 2 个月的 Hermes 服务器：10,885 个知识图谱页面、42,481 个提取的事实节点、105,601 条可搜索的会话消息。不是原型，是每天在用的东西。
安装很简单：设一下 AGENT_HOME ，跑 install.sh ，选个 embedding 模型（ 6 种可选，默认推荐中英混合的 multilingual-e5-small ），其他自动完成。开源 MIT 协议。
https://github.com/mage0535/hermes-memory-installer

## 涉及话题
- embedding
- 智能体
- AI
- Claude
- Cursor

[原文链接](https://www.v2ex.com/t/1217342)
