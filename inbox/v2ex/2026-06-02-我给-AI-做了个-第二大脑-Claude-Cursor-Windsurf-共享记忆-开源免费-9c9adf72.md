---
title: "我给 AI 做了个「第二大脑」—— Claude、Cursor、Windsurf 共享记忆，开源免费"
source: v2ex
url: "https://www.v2ex.com/t/1217451"
author: "a1194597483"
date: 2026-06-02
score: 0
tags: ["Cursor", "AI", "GPT", "mcp", "Claude", "MCP"]
---

# 我给 AI 做了个「第二大脑」—— Claude、Cursor、Windsurf 共享记忆，开源免费

年初开始，我的工作流变成了 Claude + Cursor + Windsurf 三件套。效率起飞，但痛点也来了——
每个 AI 工具互不相识。
你在 Claude 里分析了半小时架构方案，切到 Cursor 写代码，它完全不知道你刚才聊过什么。你只能在窗口间复制粘贴上下文，像个人肉胶水。
更烦的是，同一个项目的技术决策、踩过的坑、约定好的规范，每次开新会话都得重新交代。时间全花在"教育 AI"上了。
市面上的方案我全试过了：
Mem0 / MemGPT：云端存储，公司代码谁敢往上传？
Cursor Rules：只管一个工具，跨不了
Continue.dev：IDE 内还行，出不了圈
最后决定自己造。三个月业余时间，边学 ONNX 边撸代码，搞出了 KeepThinking 。
它是什么
一个跑在本地的 AI 记忆引擎。你的所有 AI 工具共享同一份记忆。
🔍 本地语义搜索：ONNX 跑 paraphrase-multilingual-MiniLM-L12-v2 ，384 维向量，支持 50+ 语言。搜"部署上线"能匹配到"Nginx 配置""CI/CD 流程"——不用关键词，用语义。
🔗 认知图谱：自动把每次关键决策关联成知识网络，按关联度 × 时效性排序。
🐛 Bug 诊断：内置 6 种 Bug 模式（空指针、状态未更新、API 错误、依赖冲突、异步竞态、配置缺失），喂错误日志自动分析。
🌐 MCP 协议：7 个标准化工具，一行配置接入 Claude Desktop 、Cursor 、VS Code 。
🔒 100% 本地：数据存在 ~/.keepthinking/memory/，不采集不上传不联网。PBKDF2 加密保护。
技术栈：Node.js + Express + SQLite + ONNX Runtime 。MIT 协议开源。
安装

…(内容已截断)

## 涉及话题
- Cursor
- AI
- GPT
- mcp
- Claude
- MCP

[原文链接](https://www.v2ex.com/t/1217451)
