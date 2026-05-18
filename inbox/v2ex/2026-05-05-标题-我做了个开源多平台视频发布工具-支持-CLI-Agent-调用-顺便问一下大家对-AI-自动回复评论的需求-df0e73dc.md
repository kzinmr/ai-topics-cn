---
title: "标题：我做了个开源多平台视频发布工具，支持 CLI / Agent 调用，顺便问一下大家对 AI 自动回复评论的需求"
source: v2ex
url: "https://www.v2ex.com/t/1210373"
author: "hanliang"
date: 2026-05-05
score: 1
tags: ["AI Agent", "AI", "LangChain"]
---

# 标题：我做了个开源多平台视频发布工具，支持 CLI / Agent 调用，顺便问一下大家对 AI 自动回复评论的需求

最近把自己用的工具整理了一下开源出来：MatrixMedia

一个基于 Electron + Puppeteer 的多平台视频发布工具，支持：
抖音 / 快手 / B 站 / 视频号 / 头条 / 百家号

核心不同点：它有 CLI 接口，可以直接被脚本或 AI Agent 调用，不用打开 GUI 点来点去。

用法大概是：

  matrixmedia upload --platform douyin --title "xxx" --file ./video.mp4

或者在你的 n8n / LangChain / 自定义 Agent 流程里直接调这个接口，实现"视频生成完自动发布"的全链路。

现在在想做一个 Pro 版本的方向：本地 AI 知识库 + 自动回复评论/私信。也就是你上传一批 FAQ 或产品文档，工具自动监控各平台评论，用 AI 生成个性化回复，不是那种模板机器人的感觉。

想了解一下有没有人有这个场景，填一下这个表格会很有帮助： https://wj.qq.com/s2/26553035/aefd/

GitHub 地址在 https://github.com/hanliang97/MatrixMedia ，欢迎 star 或提 issue 。

## 涉及话题
- AI Agent
- AI
- LangChain

[原文链接](https://www.v2ex.com/t/1210373)
