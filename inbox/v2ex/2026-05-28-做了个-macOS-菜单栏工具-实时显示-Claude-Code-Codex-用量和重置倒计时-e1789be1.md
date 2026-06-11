---
title: "做了个 macOS 菜单栏工具，实时显示 Claude Code + Codex 用量和重置倒计时"
source: v2ex
url: "https://www.v2ex.com/t/1216310"
author: "ShuovO"
date: 2026-05-28
score: 0
tags: ["ai", "claude", "ChatGPT", "Claude"]
---

# 做了个 macOS 菜单栏工具，实时显示 Claude Code + Codex 用量和重置倒计时

两种显示模式：
文字模式 / 图标环模式，菜单里随时切换。


点开菜单可以看到精确百分比和重置倒计时：


数据来源：

Claude：直接调 claude.ai/api/oauth/usage，复用 Claude Code 本地的 OAuth token ，和 /usage 命令数据一致，无需额外配置
Codex：读取 ~/.codex/sessions/ 下最新 session JSONL 里的 rate_limits 字段（来自 ChatGPT 后端响应）

## 涉及话题
- ai
- claude
- ChatGPT
- Claude

[原文链接](https://www.v2ex.com/t/1216310)
