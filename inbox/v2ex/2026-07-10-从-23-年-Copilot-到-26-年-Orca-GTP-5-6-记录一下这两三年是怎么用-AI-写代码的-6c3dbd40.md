---
title: "从 23 年 Copilot 到 26 年 Orca（GTP 5.6），记录一下这两三年是怎么用 AI 写代码的"
source: v2ex
url: "https://www.v2ex.com/t/1226428"
author: "yekk"
date: 2026-07-10
score: 0
tags: ["Gemini", "GPT", "MCP", "Cursor", "CLAUDE", "Claude", "AI", "Copilot", "大模型", "Prompt"]
---

# 从 23 年 Copilot 到 26 年 Orca（GTP 5.6），记录一下这两三年是怎么用 AI 写代码的

最近回头想了一下，做独立开发差不多一年半了，开发方式已经和以前完全不一样。现在我基本不会手敲代码了。
以前写代码，会先在脑子里过一遍实现，再坐在编辑器前一个字符一个字符敲出来。现在更多是在聊需求、看方案、拆任务、验收结果，不对的地方再继续调整。
这篇不算教程，也不是工具横评，主要记录一下这一年半用过的工具，以及自己的开发方式是怎么变化的。
最早用的是 GitHub Copilot
大概是 2023 到 2024 年，当时 GitHub Copilot 好像是每个月 10 美元。主要就是 Tab 补全，帮忙写一些简单方法和重复代码。整体还是自己在编程，Copilot 只是猜接下来要写什么。
中间大概 Gap 了半年。到 2025 年三四月份开始用 Cursor ，才算真的进入现在大家说的 Vibe Coding 。
用 Cursor 做了「字节篝火」
我用 Cursor 做的第一个完整项目，是一个叫「字节篝火」的自动化科技播客。
大概流程是：

n8n 获取 GitHub Trending 、Hacker News 等内容
Gemini 2.5 负责翻译、筛选和整理
海螺，也就是现在的 MiniMax ，负责生成音频
Python 小服务处理爬虫、TTS 分段、音频合成和时间戳
Supabase 和 Vercel 展示原文、译文和摘要
最后通过影刀 RPA 自动上传到小宇宙，填写时间轴和关键点

n8n 是我自己研究的，里面涉及的 Python 小项目基本都是 Cursor 写的。这个项目实际跑了三四个月，一共做了六十多期，不是只跑通了一次的 Demo 。

字节篝火｜小宇宙

从那时开始，我基本就不怎么手动敲代码了。以前碰到不熟悉的技术，第一反应是要不要先学一下、需要学多久。后来逐渐变成先确定自己想做什么，再把爬虫、TTS 、网站和 RPA 拼起来。

…(内容已截断)

## 涉及话题
- Gemini
- GPT
- MCP
- Cursor
- CLAUDE
- Claude
- AI
- Copilot
- 大模型
- Prompt

[原文链接](https://www.v2ex.com/t/1226428)
