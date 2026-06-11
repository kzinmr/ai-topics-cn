---
title: "大家用 WSL2 跑 CodeAgent / Harnss 的话， Windows 桌面这边一般怎么配合？"
source: v2ex
url: "https://www.v2ex.com/t/1217140"
author: "DiKaErJi"
date: 2026-06-01
score: 2
tags: ["AI", "Cursor", "MCP", "Gemini", "coding agent", "Claude"]
---

# 大家用 WSL2 跑 CodeAgent / Harnss 的话， Windows 桌面这边一般怎么配合？

最近想认真把 WSL2 配起来，当成主力开发环境用。
主要原因是现在很多 CodeAgent ，比如 Claude Code 、Codex 、Gemini CLI 、Harnss 这类东西，感觉放在 Linux 环境里会更自然一点。跑命令、装依赖、跑测试、读写项目文件，应该都比在 Windows 原生环境下少一点奇怪问题。
但我平时又不是纯 CLI 开发，有时候会用 Windows 上的 desktop 软件，比如 VS Code 、Cursor 、浏览器、文件管理器，还有一些其他 GUI 工具。
所以现在有点纠结，想问问大家实际怎么搭工作流。
我目前想到的方案是：
项目放 WSL2：
/home/me/projects/xxx
Agent 也在 WSL2 里跑：
Claude Code / Codex / Harnss / 其他 CLI agent
Windows 这边负责图形界面：
VS Code / Cursor 用 Remote WSL
文件管理器通过 \wsl.localhost 访问
需要的时候在 WSL 里 explorer.exe .
这样看起来比较合理，但是还有几个点不太确定：
1.如果 Windows desktop 软件不支持 Remote WSL ，直接打开 \wsl.localhost\Ubuntu\home\me\projects\xxx 会不会很难用？
2.agent 跑在 WSL2 里，想打开 Windows 浏览器或者控制 Chrome ，一般是怎么做？ Playwright MCP ？ Chrome DevTools MCP ？
3.有没有人试过 Harnss 跑在 WSL2 里，然后 GUI 通过 WSLg 显示到 Windows ？

…(内容已截断)

## 涉及话题
- AI
- Cursor
- MCP
- Gemini
- coding agent
- Claude

[原文链接](https://www.v2ex.com/t/1217140)
