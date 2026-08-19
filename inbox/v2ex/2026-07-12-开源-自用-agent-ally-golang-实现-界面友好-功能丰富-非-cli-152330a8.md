---
title: "『开源』自用 agent ally， golang 实现，界面友好，功能丰富（非 cli）"
source: v2ex
url: "https://www.v2ex.com/t/1226780"
author: "bronyakaka"
date: 2026-07-12
score: 0
tags: ["AI", "MCP", "OpenAI", "Anthropic"]
---

# 『开源』自用 agent ally， golang 实现，界面友好，功能丰富（非 cli）

平常工作基本使用自己写的 agent ，特点：
0. 类 codex app ，非 cli
cli 做 UI 渲染不怎么方便，个人更喜欢直接的 GUI APP ，基于 webview 实现，安装包~30mb 。

1. 不绑定单一模型厂商
支持多种 API 格式，包括：

OpenAI Chat Completions
OpenAI Responses
Anthropic Messages

2. 功能完整
除了聊天，Ally 还可以：

批量读取、搜索和修改项目文件
执行本地命令
展示代码差异
管理待办事项和长期目标
调用 MCP 工具
委派子任务给子 Agent
创建定时执行的 Agent 任务
保存跨项目使用的长期记忆
通过 Skill 扩展特定工作流
完整的 git 变更视图，不用特地打开 vscode 去瞅一眼了

上面功能都是从零开始手撸，1w 多行 ReAct 。
Ally 适合谁？
比较适合：

希望自由切换不同模型或 API 服务的开发者
在意代码修改过程和 Diff 可见性的人
想尝试 MCP 、Skill 、子 Agent 或目标模式的人
偏好本地桌面应用，不想完全依赖在线 IDE 的用户
愿意自己配置并逐步打磨 AI 编程工作流的人

项目地址： https://github.com/Bronya0/ally-agent

## 涉及话题
- AI
- MCP
- OpenAI
- Anthropic

[原文链接](https://www.v2ex.com/t/1226780)
