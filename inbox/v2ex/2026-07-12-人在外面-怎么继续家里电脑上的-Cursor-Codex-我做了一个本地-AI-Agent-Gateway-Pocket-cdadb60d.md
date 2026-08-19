---
title: "人在外面，怎么继续家里电脑上的 Cursor / Codex？我做了一个本地 AI Agent Gateway-PocketPilot"
source: v2ex
url: "https://www.v2ex.com/t/1226717"
author: "stoneTojing"
date: 2026-07-12
score: 0
tags: ["AI", "AI Agent", "Gemini", "Claude", "Coding Agent", "Cursor"]
---

# 人在外面，怎么继续家里电脑上的 Cursor / Codex？我做了一个本地 AI Agent Gateway-PocketPilot

人在外面，怎么继续家里电脑上的 Cursor / Codex ？我做了一个本地 AI Agent Gateway
最近做了一个开源项目，叫 PocketPilot。

GitHub：https://github.com/gong0019/pocket-pilot
在线体验：https://pp.95ym.cn/

它的定位是一个 本地 AI Agent Gateway：让运行在自己电脑上的 Cursor Agent CLI 、Codex CLI 、Claude CLI 等工具，可以通过手机或浏览器访问。
先说明一下：它不是远程桌面，也不是把开发环境搬到云端。
PocketPilot 主要做的是，在本地 AI Agent 和 Web 之间增加一层连接、会话恢复与多 Agent 管理能力。

为什么会做这个项目
最近使用 AI Coding Agent 的频率越来越高。
Cursor 、Codex 、Claude Code 这类工具已经不只是补全几行代码了。很多时候，我会让 Agent 在本地项目里持续执行任务，例如：

阅读项目代码；
修改多个文件；
运行测试；
排查报错；
继续之前没有完成的任务。

但这些 Agent 通常依赖本地电脑上的代码、终端、依赖环境和登录状态。
于是就有了一个很具体的问题：
Agent 在家里或办公室的电脑上运行，但人一离开电脑，就很难查看进度、回复问题，或者继续之前的 Session 。
我遇到过几种情况：

出门之后，想看 Agent 是否已经执行完成；
Agent 中途提出问题，但没法及时回复；
想在手机上恢复之前的 Session ；
想让 Agent 接着处理一个任务；
只想操作 Agent ，并不想远程控制整台电脑。

远程桌面当然可以解决一部分问题，但对这个场景来说有些重。

…(内容已截断)

## 涉及话题
- AI
- AI Agent
- Gemini
- Claude
- Coding Agent
- Cursor

[原文链接](https://www.v2ex.com/t/1226717)
