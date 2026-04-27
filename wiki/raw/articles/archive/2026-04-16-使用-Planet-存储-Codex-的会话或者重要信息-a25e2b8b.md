---
title: "使用 Planet 存储 Codex 的会话或者重要信息"
source: v2ex
url: "https://www.v2ex.com/t/1206386"
author: "Livid"
date: 2026-04-16
score: 0
tags: ["Claude", "ai", "prompt"]
---

# 使用 Planet 存储 Codex 的会话或者重要信息

把下面这段 prompt 发给 Codex 创建 skill：
Create a skill called /save-session that saves the current session summary as a Planet article. One planet per project, one article per session. If the article already exists, update it.

Planet API docs: https://raw.githubusercontent.com/Planetable/Planet/refs/heads/main/Technotes/API.md

Planet API server is already running on http://127.0.0.1:8086

让 Planet 运行并打开 API 支持，这样 Codex 会先跑一些测试，然后就会自己写代码来操纵 Planet 。

然后就可以根据需要把会话或者是其他有用信息放进 Planet 里了。
如果你同时还在用其他支持创建 skill 的 agent ，比如 Claude Code 或者 OpenClaw ，那么可以用类似的 prompt 让它们也来读写同一个 Planet 站点。这样就可以用 Planet 作为本地 agent 的信息交换中心了。
如果你想让内容进入指定的 Planet 站点，那么可以明确提供站点的 UUID 给 agent：

## 涉及话题
- Claude
- ai
- prompt

[原文链接](https://www.v2ex.com/t/1206386)
