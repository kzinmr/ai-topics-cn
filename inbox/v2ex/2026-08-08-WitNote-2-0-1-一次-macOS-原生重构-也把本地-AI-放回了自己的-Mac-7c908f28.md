---
title: "WitNote 2.0.1：一次 macOS 原生重构，也把本地 AI 放回了自己的 Mac"
source: v2ex
url: "https://www.v2ex.com/t/1232801"
author: "hashtome"
date: 2026-08-07
score: 26
tags: ["AI", "推理", "大模型", "Qwen"]
---

# WitNote 2.0.1：一次 macOS 原生重构，也把本地 AI 放回了自己的 Mac

大家好，我是 WitNote 的独立开发者。
这是 WitNote 2.0.1 。对我来说，它不是一次普通更新，而是一次把自己第一个 Vibe Coding 项目推翻重做的记录。
去年开始做 WitNote 时，我会写 Markdown ，也会大量使用 AI ，于是想做一个真正围绕写作的工具：不把文章复制进网页，而是在自己的文件夹里写作，让 Markdown 、本地文件和 AI 放在同一个工作流里。为了快速验证想法，第一版用了 Electron 。
Electron 让我很快做出了能运行的产品，也让我第一次经历了开源、上架、审核、推广和有人付费。但真实用户出现以后，启动速度、内存、界面响应和 macOS 融合感的问题也一起出现了。“能用”和“真正好用”之间，还有很长一段距离。
当 WitNote 越来越强调本地 AI ，我开始重新想：既然它主要给 Mac 用户使用，为什么不真正用 Swift 和 Apple Silicon 的 MLX 路线重做？于是大约两个月前，我决定从 Electron 转向 Swift 原生 macOS 。文件系统、Markdown 编辑器、窗口状态、模型运行、权限、沙盒、StoreKit ，几乎都要重新处理。
这次重构里 Codex 也成了重要的开发搭档。我会先让它理解旧版功能，再一起讨论原生 macOS 应该怎么设计；它帮我写代码、查 Bug 、做重构，我负责判断哪些功能该留下，哪些应该删掉。Vibe Coding 并没有让产品自动变简单，却让我能一边做，一边更快理解架构、性能、权限和用户体验。
2.0.1 留下了什么

Swift 原生 macOS 写作工作区：本地 Markdown 文件夹、编辑/预览分栏、Focus Mode 、Finder 打开文稿。

…(内容已截断)

## 涉及话题
- AI
- 推理
- 大模型
- Qwen

[原文链接](https://www.v2ex.com/t/1232801)
