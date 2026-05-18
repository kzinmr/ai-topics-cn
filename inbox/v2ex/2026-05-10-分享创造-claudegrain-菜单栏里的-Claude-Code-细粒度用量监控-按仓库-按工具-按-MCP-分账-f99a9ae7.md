---
title: "[分享创造] claudegrain — 菜单栏里的 Claude Code 细粒度用量监控（按仓库/按工具/按 MCP 分账）"
source: v2ex
url: "https://www.v2ex.com/t/1211709"
author: "zhoubohanpro"
date: 2026-05-10
score: 0
tags: ["Claude", "MCP", "claude", "ai"]
---

# [分享创造] claudegrain — 菜单栏里的 Claude Code 细粒度用量监控（按仓库/按工具/按 MCP 分账）

做了一个开源 macOS 菜单栏小工具，解决一个我自己天天遇到的痛点：
Claude Code 自带的 /usage 只告诉你"会话用了 30%"，但不告诉你这 30%
是哪个仓库花掉的、哪个工具（ Bash/Edit/MCP ）最烧 token 。我开了 7-8 个
重度项目，月底 quota 透支也搞不清楚谁占大头。
claudegrain 三层数据源做这件事：

从 macOS Keychain 读 OAuth token ，调用未公开的 oauth/usage 接口拿
真实会话/周配额。
直接解析 ~/.claude/projects/**/*.jsonl ，按 cwd / 工具 / MCP /
缓存命中率细分。OAuth 接口不暴露这些维度。
兜底跑 claude /usage 抓 stdout 。

技术栈：原生 Swift/SwiftUI ，仅依赖 GRDB ，~10MB binary 。LSUIElement 无
Dock 图标。深色 phosphor + 浅色 thermal paper 两套主题。
GitHub: https://github.com/FlyTOmeLight/claudegrain
安装方式：
Homebrew: brew tap FlyTOmeLight/claudegrain && brew install --cask claudegrain
DMG 下载: 仓库 Releases 页

MIT 协议，欢迎试用 / 拍砖。

## 涉及话题
- Claude
- MCP
- claude
- ai

[原文链接](https://www.v2ex.com/t/1211709)
