---
title: "Hermes Agent 多用户 / Multi-tenant 应该怎么设计？一个实例服务多个用户可行吗？"
source: v2ex
url: "https://www.v2ex.com/t/1235423"
author: "anamulhaque1268"
date: 2026-08-18
score: 0
tags: ["MCP", "AI", "prompt"]
---

# Hermes Agent 多用户 / Multi-tenant 应该怎么设计？一个实例服务多个用户可行吗？

最近在研究 Hermes Agent ，准备把它作为一个多用户应用的 Agent runtime ，想请教一下熟悉 Hermes / MCP / Agent 架构的朋友。

我的需求比较简单：

多个用户使用同一套 AI 能力，例如：

相同的 system prompt
相同的模型
公共 Skills
公共 MCP
Web Search
公共知识库

但是每个用户必须拥有独立的：

conversation/session
long-term memory
user profile/preferences
reminders / cron jobs
private data
MCP credentials / permissions

例如：

             Hermes
                │
        ┌───────┼───────┐
        ▼       ▼       ▼
      User A  User B  User C

我目前主要纠结两个方案。

方案一：多个用户共享一个 Hermes instance

通过：

user_id
session_key

来区分用户。

例如：

user:10001
user:10002
user:10003

Hermes 本身负责：

reasoning
skills
MCP
tool calling

用户相关的数据则由应用层隔离。

这种方式看起来最合理，也方便以后横向扩展。

但我比较担心 Hermes 内部的一些状态，例如：

USER.md
memory
session
cron
MCP context

是否完全适合 multi-tenant 环境。

例如 User A 告诉 Agent：

我叫张三，我住上海。


…(内容已截断)

## 涉及话题
- MCP
- AI
- prompt

[原文链接](https://www.v2ex.com/t/1235423)
