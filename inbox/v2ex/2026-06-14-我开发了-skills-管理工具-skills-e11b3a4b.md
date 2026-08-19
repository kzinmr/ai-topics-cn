---
title: "我开发了 skills 管理工具， skills++"
source: v2ex
url: "https://www.v2ex.com/t/1220401"
author: "VforVendetta"
date: 2026-06-14
score: 0
tags: ["Cursor", "Gemini", "Claude", "Copilot", "AI", "ai"]
---

# 我开发了 skills 管理工具， skills++

Claude Code 、Codex 、OpenClaw 各有一套 skill 目录，同一个 skill 得分别安装、复制或软链。手搓了几次实在烦了，决定写个有界面的工具。
它从 skills sh 、LobeHub 等地方聚合 skills ，自动识别你本机装了哪些 AI 工具，然后就能一键安装/卸载/重装 skills 。四种安装策略:
git 克隆、文件拷贝、压缩包解压、软链接——默认自动选最合适的，你也可以手动指定。



发现页
已安装管理
skills 目录管理











安装 Skill
Skill 详情
搜索








功能：

skills 多来源聚合，统一的发现页，支持搜索和筛选
安装前预览 SKILL md 内容
自动扫描本机 AI Skills 目录，目前支持 Codex 、Claude 、Cursor 、Gemini CLI 、OpenCode 、GitHub Copilot 等 10+ 工具
检测已安装 skill 是否有新版本
浅色/深色/跟随系统三种主题，Tauri 原生窗口主题同步

技术栈：Tauri 2.x + React 19 + TypeScript + Tailwind CSS v4 + SQLite ，Rust 做后端。
详细功能和使用说明见 GitHub：
skills++
目前还比较早期，有想法直接提 issue ，想动手的欢迎 PR

## 涉及话题
- Cursor
- Gemini
- Claude
- Copilot
- AI
- ai

[原文链接](https://www.v2ex.com/t/1220401)
