---
title: "手搓了个让 Claude Code、Codex、Cursor 共享记忆的小工具"
source: v2ex
url: "https://www.v2ex.com/t/1214263"
author: "pp3x325"
date: 2026-05-20
score: 0
tags: ["Cursor", "Claude", "MCP", "AI"]
---

# 手搓了个让 Claude Code、Codex、Cursor 共享记忆的小工具

在用 Claude Code 、Codex 、Cursor 这些 AI 工具写东西，感觉有个问题
每换一个工具、一个项目、一个新会话，都要重新解释一遍自己是谁
比如：我习惯用中文沟通、我希望它先读代码再下判断，每次都要给他教育一遍，定规则。。
所以我做了一个小工具，叫 Engram 。
简单说，它就是把这些记忆存在本地 JSON 里，然后通过 MCP 暴露给支持 MCP 的 AI 工具读取。
它主要做几件事：

记住我的身份、偏好、沟通习惯
记住项目里的经验教训和关键决策
多个 AI 工具共享同一份本地记忆
数据都在本地，JSON 可以直接编辑
通过 MCP 接入，不绑定某一个 AI 产品
比如我跟一个 AI 说过“这个项目不要自动改范围，先确认边界。”下次换到另一个 AI 工具时，
新 AI 也能知道这个要求。

老法师们有时间也帮忙看一下给点意见，第一次 VIBE CODING 。。。
https://github.com/Patdolitse/engram

## 涉及话题
- Cursor
- Claude
- MCP
- AI

[原文链接](https://www.v2ex.com/t/1214263)
