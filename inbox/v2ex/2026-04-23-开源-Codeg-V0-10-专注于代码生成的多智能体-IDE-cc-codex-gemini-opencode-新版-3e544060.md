---
title: "[开源] Codeg V0.10：专注于代码生成的多智能体 IDE（cc、codex、gemini、opencode……），新版本重构了工作区，飞一般的体验，支持桌面端、服务器部署"
source: v2ex
url: "https://www.v2ex.com/t/1208060"
author: "molicloud"
date: 2026-04-23
score: 0
tags: ["Claude", "gemini", "MCP", "Gemini", "智能体", "AI", "代码生成"]
---

# [开源] Codeg V0.10：专注于代码生成的多智能体 IDE（cc、codex、gemini、opencode……），新版本重构了工作区，飞一般的体验，支持桌面端、服务器部署

前言
新版本重构了工作区，大大提升工作体验，当前项目纯开源为爱发电，欢迎各种反馈和批判，或者路线建议。
Codeg （ Code Generation ）是一个企业级多 Agent 编码工作台。 它将本地 AI 编码代理（ Claude Code 、Codex CLI 、OpenCode 、Gemini CLI 、OpenClaw 、Cline 等）统一到桌面应用、独立服务器或 Docker 容器中——通过浏览器即可远程开发——支持对话聚合、 并行 git worktree 开发、MCP/Skills 管理、消息渠道交互（ Telegram 、飞书、iLink 等），以及集成的 Git/文件/终端工作流。
开源地址
https://github.com/xintaofei/codeg
通信流程

核心亮点

同一项目中的多 Agent 统一工作台
本地对话解析与结构化渲染
内置 git worktree 并行开发流程
项目启动器 — 可视化创建新项目，实时预览效果
消息渠道 — 连接 Telegram 、飞书、iLink （微信）等即时通讯应用到编码代理，实时接收通知、完整会话交互、远程任务控制
MCP 管理（本地扫描 + 市场搜索/安装）
Skills 管理（全局与项目级）
Git 远程账号管理（支持 GitHub 及其它 Git 服务器）
Web 服务模式 — 开启后可在浏览器中访问 Codeg ，支持远程工作
独立服务器部署 — 在任意 Linux/macOS 服务器上运行 codeg-server ，通过浏览器访问
Docker 支持 — docker compose up 或 docker run ，可自定义令牌、端口，支持数据持久化及项目目录挂载
集成工程闭环（文件树、Diff 、Git 变更、提交、终端）

主界面

## 涉及话题
- Claude
- gemini
- MCP
- Gemini
- 智能体
- AI
- 代码生成

[原文链接](https://www.v2ex.com/t/1208060)
