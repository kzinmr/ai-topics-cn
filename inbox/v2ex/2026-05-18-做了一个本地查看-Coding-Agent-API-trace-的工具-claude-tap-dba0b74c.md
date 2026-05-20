---
title: "做了一个本地查看 Coding Agent API trace 的工具： claude-tap"
source: v2ex
url: "https://www.v2ex.com/t/1213562"
author: "liaohch3"
date: 2026-05-18
score: 0
tags: ["claude", "Gemini", "Cursor", "prompt", "Claude", "Kimi", "Coding Agent"]
---

# 做了一个本地查看 Coding Agent API trace 的工具： claude-tap

最近把一个自己用来研究 Coding Agent 的小工具整理了一下，开源叫 claude-tap 。
它主要解决一个问题：当 Claude Code 、Codex CLI 这类 Coding Agent 在工作时，我们很难看清它们实际发给模型 API 的完整请求。
项目地址：
https://github.com/liaohch3/claude-tap
一开始是因为我想看清楚 Claude Code 实际发给模型 API 的内容：system prompt 、messages 、tool 定义、tool calls 、response stream 、token/cache usage 等等。
后来发现这个视角对调试 Coding Agent 很有用，就做成了本地 JSONL trace + 自包含 HTML viewer 。每次运行会把请求记录下来，然后可以在浏览器里查看、搜索、diff ，也可以直接分享 HTML 作为复现证据。
现在支持的客户端包括：Claude Code 、Codex 、Gemini CLI 、Cursor CLI 、Kimi CLI 、Pi 、Qoder 、OpenCode ，也支持 OpenClaw 和 Hermes
claude-tap  不联网，不上报任何数据，trace 都在本机，常见认证 header 会脱敏。
如果你也在研究 Coding Agent 的上下文、工具调用、token/cache usage ，或者遇到“模型到底看到了什么”的调试问题，欢迎试试。也欢迎 issue / PR 。

## 涉及话题
- claude
- Gemini
- Cursor
- prompt
- Claude
- Kimi
- Coding Agent

[原文链接](https://www.v2ex.com/t/1213562)
