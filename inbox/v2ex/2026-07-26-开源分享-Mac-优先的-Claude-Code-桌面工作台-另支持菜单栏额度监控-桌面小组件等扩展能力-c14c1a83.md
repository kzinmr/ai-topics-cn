---
title: "[开源分享] Mac 优先的 Claude Code 桌面工作台。另支持菜单栏额度监控,桌面小组件等扩展能力"
source: v2ex
url: "https://www.v2ex.com/t/1229978"
author: "xxmym"
date: 2026-07-26
score: 0
tags: ["MCP", "AI", "Claude", "ai", "llm"]
---

# [开源分享] Mac 优先的 Claude Code 桌面工作台。另支持菜单栏额度监控,桌面小组件等扩展能力

最初只是想做一个方便分屏的 GUI ，结果功能越塞越多。我目前已经完全脱离 VS Code 来开发。
纯本地，而且对 Claude Code 会话文件完全只读。可以集中管理和搜索会话，管理 MCP 、Skill 、记忆等内容。
基于 Tauri 跨平台，但只针对 Mac 进行了优化，Windows 凑合能用。 不过菜单栏、桌面组件，以及涉及强制唤醒电脑的定时任务，只支持 Mac 。

也可以只当成一个 Claude Code 额度监控的小工具。或者统计小组件。跟主应用的进程是分开的，不会有额外资源消耗。

相比 CLI ，在会话上又做了很多便捷功能：


支持并行会话每个会话可以非常简单地热切换渠道和模型。


支持赛马模式，直观对比不同渠道、不同模型的回答质量和 Token 消耗。


会话嵌了一个简单的命令台，可以直接启动项目。并且日志可以通过 MCP 暴露给会话。


异步面板可以实时查看子 Agent 详情。


文件管理可以汇总查看改过哪些文件.


并且对会话提供了一些增强能力，比如说 AI 总结、打标，HTML 的增强渲染。


锚点导航 + 提问吸顶 + 回底浮标


详细功能见github，也可以直接把下面链接发给你的 Agent 来了解。
https://raw.githubusercontent.com/zenolab124/monet/main/llms.txt

## 涉及话题
- MCP
- AI
- Claude
- ai
- llm

[原文链接](https://www.v2ex.com/t/1229978)
