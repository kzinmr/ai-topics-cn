---
title: "做了一个 Typeless 平替，便宜 10 倍，用 Claude Code / Agent 时再也不用憋着慢慢打字了"
source: v2ex
url: "https://www.v2ex.com/t/1207595"
author: "teaguexiao"
date: 2026-04-21
score: 1
tags: ["LLM", "Cursor", "AI", "Claude"]
---

# 做了一个 Typeless 平替，便宜 10 倍，用 Claude Code / Agent 时再也不用憋着慢慢打字了

自从开始用 Claude Code 和各种 Agent 产品，发现一个新的痛点：你需要输入的东西越来越长、越来越完整。
给 Agent 下指令，你想把需求说清楚，但打字又慢又累，最后要么描述不够准确，要么懒得写细节，然后 AI 给你的结果也差强人意。
我的解法是做了一个 AI 语音输入工具：Sayd Desktop 。
核心使用场景：

用 Claude Code / Cursor / Codex / 任何 Agent 产品时：直接说需求，想说多详细说多详细，不用憋着打字，AI 帮你润色成干净的文本再输入
跟任何 Agent 交互时：口述完整的任务描述、背景、约束条件，比手打快 5 倍
写代码注释、提交信息、PR 描述：说出来，自动格式化

技术实现：

基于 amical 开源项目二次开发
云端实时转录 + 内置 LLM 文本润色，输出直接是干净可用的文本
浮动悬浮窗 + 自定义快捷键，不打断工作流

支持平台：

macOS （ M 系列 / Intel ）
Windows x64

费用：

注册即送 $5 免费额度，无需绑卡，永不过期
实时转录单价约 $0.126/小时，$5 大约能用 40 小时（保守估计）
每天使用 15 分钟的话，$5 大约能用 20 个月

开源 MIT ，代码和下载都在这里： https://github.com/teaguexiao/sayd-desktop
注册免费 API （含 $5 Credit ）： https://sayd.dev/zh/signup
现在写提示词、给 Agent 下指令基本靠嘴，效率差不多是纯打字的 3-5 倍。感兴趣可以试试，有问题欢迎 issue 或直接这里聊。

## 涉及话题
- LLM
- Cursor
- AI
- Claude

[原文链接](https://www.v2ex.com/t/1207595)
