---
title: "VibeTime - 给 AI 编程时代做的本地时间追踪器，支持 Claude Code / Cursor / Codex / Gemini CLI"
source: v2ex
url: "https://www.v2ex.com/t/1212208"
author: "BarryYangi"
date: 2026-05-12
score: 0
tags: ["coding agent", "AI agent", "Cursor", "Claude", "AI", "Gemini", "OpenAI"]
---

# VibeTime - 给 AI 编程时代做的本地时间追踪器，支持 Claude Code / Cursor / Codex / Gemini CLI

大家好，分享一个我最近做的小工具。
背景
我每天都在用 AI agent 写代码（ Claude Code 、Cursor ），但一直有一个困扰：我完全不知道每天在 AI 辅助编程上花了多少时间，时间分布在哪些项目上。
WakaTime 追踪的是键盘输入，RescueTime 追踪的是应用使用时长，但没有任何工具在追踪 AI agent 的工作会话。
所以我做了 VibeTime 。
它是什么
VibeTime 是一个菜单栏应用，通过 hooks 机制自动记录 AI coding agent 的工作时长。
支持：Claude Code / Cursor / OpenAI Codex / Gemini CLI
设计原则

纯本地：数据存在 ~/.vibetime/ 目录下的 SQLite ，没有云端，没有账号
自动追踪：通过 hooks 记录 session 的开始和结束，计算时间差
隐私优先：无遥测，无数据上传，你的数据只属于你

功能

实时 Dashboard ，今天的工作一目了然
GitHub 风格的贡献热力图
按项目维度的时间统计
CLI 工具，支持导出和诊断
一键安装/卸载 agent hooks

下载

macOS (Apple Silicon): .dmg
Windows (x64): .exe

GitHub: https://github.com/BarryYangi/vibetime
MIT 开源，欢迎 Star ⭐ 和 PR 。
技术栈：Electron + React + TypeScript + SQLite + Bun ，pnpm monorepo 。
欢迎反馈，尤其想听听同样在用 AI agent 写代码的朋友们的想法。

## 涉及话题
- coding agent
- AI agent
- Cursor
- Claude
- AI
- Gemini
- OpenAI

[原文链接](https://www.v2ex.com/t/1212208)
