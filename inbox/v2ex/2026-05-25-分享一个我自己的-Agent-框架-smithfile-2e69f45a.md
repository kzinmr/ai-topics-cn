---
title: "分享一个我自己的 Agent 框架： smithfile"
source: v2ex
url: "https://www.v2ex.com/t/1215326"
author: "flankerfc"
date: 2026-05-25
score: 0
tags: ["Cursor", "AI agent", "LLM", "Claude", "AI"]
---

# 分享一个我自己的 Agent 框架： smithfile

每次和 Claude Code 聊天，都需要重复介绍自己和项目
我是谁、在做什么、项目是什么、团队成员有哪些、上次那篇文章记得吗、上次你做的方法记得吗？
当然 OpenClaw 、Hermers 也解决了这个问题。
但我的 smithfile （实际是因为我的 Agent 叫 Agent Smith ），是一个更轻量、更本地、更容易上手的 个人助力：
设计目标

作为你个人长期的 AI 助手
拥有身份、知道你，有记忆、有项目、有联系人，跨会话不忘
所有内容都是显式的，纯 markdown 可以版本控制
不绑定厂商，Claude Code/Codex/Cursor 任意 CLI Agent 都可以用
借鉴了 Karpathy 的 LLM Wiki（用 LLM 帮自己建知识库的思路）和 Hermes Agent 的 Skill 自我进化机制

那为什么不直接用 Hermes Agent :)

一个很大的原因是可以充分利用 Claude Code 的订阅（其他厂商未来对 Hermes 这种第三方的限制越来越明显了）

安装
仓库里有 BOOTSTRAP.md ，粘贴给你的 AI agent ，问几个问题就初始化好了。
仓库地址： https://github.com/flanker/smithfile
欢迎试试和拍砖。

## 涉及话题
- Cursor
- AI agent
- LLM
- Claude
- AI

[原文链接](https://www.v2ex.com/t/1215326)
