---
title: "写了个小工具 TokenLens，专门用来追踪本地 AI 编程工具的 token 消耗和成本"
source: v2ex
url: "https://www.v2ex.com/t/1211931"
author: "zwhui111"
date: 2026-05-11
score: 2
tags: ["Gemini", "Cursor", "AI", "OpenAI", "Qwen", "Copilot", "Claude"]
---

# 写了个小工具 TokenLens，专门用来追踪本地 AI 编程工具的 token 消耗和成本

希望大佬看看有没有哪里可以改进的，或者哪里有问题的 
 
核心功能

支持 18 种编程工具（ Claude Code 、Cursor 、Copilot 、Gemini CLI 等）
可视化 Token 消耗、缓存命中率，成本趋势
支持按项目，时间范围（ 7D/30D/60D/ALL ）筛选
Code Change Trends / Tool Call Analytics / 24 小时活跃热力图
本地运行，不上传数据，不依赖云服务

支持的编程工具
Claude Code 、OpenAI Codex 、GitHub Copilot 、Cursor 、Gemini CLI 、OpenClaw 、OpenCode 、Kiro 、Pi / OMP 、Droid 、Roo Code 、Kilo Code 、Qwen 、Goose 、Antigravity

项目筛选

安装方式
需要 Node.js >= 22
# npx 免安装
npx @mikeyxyz/tokenlens

# 全局安装（长期使用推荐）
npm install -g @mikeyxyz/tokenlens
tokenlens

GitHub： https://github.com/mikeymiaoxyz/tokenlens

## 涉及话题
- Gemini
- Cursor
- AI
- OpenAI
- Qwen
- Copilot
- Claude

[原文链接](https://www.v2ex.com/t/1211931)
