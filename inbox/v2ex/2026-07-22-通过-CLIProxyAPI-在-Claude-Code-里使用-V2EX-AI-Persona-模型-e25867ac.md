---
title: "通过 CLIProxyAPI 在 Claude Code 里使用 V2EX AI Persona 模型"
source: v2ex
url: "https://www.v2ex.com/t/1229174"
author: "Livid"
date: 2026-07-22
score: 0
tags: ["CLAUDE", "ANTHROPIC", "Claude", "OpenAI", "AI", "claude", "ai"]
---

# 通过 CLIProxyAPI 在 Claude Code 里使用 V2EX AI Persona 模型

先看跑起来的效果：

模型那里显示的是 coder



问它能做什么



写个程序然后跑一下试试



/usage 显示是未知模型



如果你已经有一个能顺利使用 Claude Code 及原版模型的环境，那么这个折腾方式不一定适合你。为了不破坏你本来已经能用的环境，你最好是在一个全新环境里试。
如果你从来没有用过 Claude Code，那么这个方式可以让你免费体验上。

Step 1 - 安装 CLIProxyAPI
如果你本地已经有装好的 CLIProxyAPI，那么可以直接跳到 Step 2。
可以通过 brew 直接安装：
brew install cliproxyapi

然后通过 brew 启动服务：
brew services start cliproxyapi

然后打开 http://localhost:8317/management.html 进 CLIProxyAPI 配置界面。
Step 2 - 在 CLIProxyAPI 里添加 V2EX AI Persona
把 V2EX 作为 OpenAI 兼容 提供商添加：


服务地址 https://edge.v2ex.com/chat/v1
模型名填 coder 或者是你自己定制的 V2EX AI 角色的 name
API Key 就是你的 V2EX Persona Access Token https://edge.v2ex.com/settings/tokens

Step 3 - 安装 Claude Code 并用定制方式启动
安装 Claude Code，装好之后不需要登陆任何 Claude 账号：
curl -fsSL https://claude.ai/install.sh | bash

用下面的参数启动 claude 命令行工具：

…(内容已截断)

## 涉及话题
- CLAUDE
- ANTHROPIC
- Claude
- OpenAI
- AI
- claude
- ai

[原文链接](https://www.v2ex.com/t/1229174)
