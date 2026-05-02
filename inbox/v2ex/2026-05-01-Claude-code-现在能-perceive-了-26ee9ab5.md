---
title: "Claude code 现在能 /perceive 了"
source: v2ex
url: "https://www.v2ex.com/t/1209922"
author: "Daniel6606"
date: 2026-05-01
score: 1
tags: ["claude", "Claude", "MCP", "ai"]
---

# Claude code 现在能 /perceive 了

目前的 MCP （模型上下文协议）和各种 Skills 确实让 Claude Code 变得很强，你可以让它运行构建、查询数据库、发起 PR 或关闭 Ticket 。但这些本质上仍然是被动的——只有在你敲下键盘后，Claude Code 才会行动。它对终端之外发生的事情完全没有感知。

然而，90% 的实际工程工作——比如“PR 审核了吗”、“部署完成了吗”、“竞品发新版了吗”或是“生产环境报警了吗”——仍然需要你先注意到，然后再去问 Claude 。

W2A 改变了这一切：

它给 Claude Code 装上了“传感器”。这些小程序会盯着某个特定的信息源（比如 GitHub 、Steam 、X 、Slack 、日历等），并以统一的架构发出事件信号。每个信号都带有一个 Claude 可以直接处理的“自然语言摘要”字段，以及一个供模型深入分析时使用的“结构化原始数据”字段。

一旦传感器触发，Claude Code 就会根据安装时通过自然语言需求生成的 Skill 自动决策，完全不需要你手写脚本或设置 Cron 定时任务。你甚至可以随时使用 build-w2a-sensor 这个 Skill 来按需构建你想要的传感器。

上手体验：

想最快感受 W2A 的威力，直接在 Claude Code 的活动会话中安装这个插件：

Bash
/plugin marketplace add machinepulse-ai/world2agent-plugins
/plugin install world2agent@world2agent-plugins
/reload-plugins
添加一个传感器（以 Hacker News 为例）：

Bash
/world2agent:sensor-add @world2agent/sensor-hackernews

…(内容已截断)

## 涉及话题
- claude
- Claude
- MCP
- ai

[原文链接](https://www.v2ex.com/t/1209922)
