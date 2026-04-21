---
title: "开源了一个 AI Agent 认证工具 sig —— 让 AI Agent 安全访问外部系统"
source: v2ex
url: "https://www.v2ex.com/t/1207593"
author: "YuanJiwei"
date: 2026-04-21
score: 5
tags: ["AI Agent", "claude", "AI", "ai"]
---

# 开源了一个 AI Agent 认证工具 sig —— 让 AI Agent 安全访问外部系统

做 AI Agent 的都知道一个痛点—— Agent 需要访问 Jira 、Slack 、Confluence 、内部 API ，但凭证怎么传？粘贴到 shell 历史里？写在 .env 里？直接丢给 Agent 的上下文窗口？每一种都是安全隐患。
所以做了 sig ，核心思路：在网络层解决认证问题，让凭证永远不暴露给 AI Agent 。
MITM 代理——最安全的方式
这是 sig 最核心的能力。一条命令启动本地 HTTPS 代理：
sig proxy start
# Proxy: running  pid=26676  port=60702
#   http_proxy=http://127.0.0.1:60702
#   https_proxy=http://127.0.0.1:60702

原理很直接：

sig 在 127.0.0.1 启动一个 MITM 代理（ ECDSA P-256 CA + 按域名动态签发叶证书）
AI Agent 的 Agent Skill 只需设置 HTTP_PROXY / HTTPS_PROXY，正常发 HTTPS 请求(curl, wget, python scripts)
MITM 代理拦截请求，根据目标域名匹配 provider ，自动注入 Cookie / Authorization / 自定义 Header
AI Agent 从头到尾不知道凭证的存在——它发的是代理请求，凭证注入在网络层透明完成

  AI Agent                    sig proxy (127.0.0.1)              Target API
     │                              │                               │

…(内容已截断)

## 涉及话题
- AI Agent
- claude
- AI
- ai

[原文链接](https://www.v2ex.com/t/1207593)
