---
title: "agentserver: 把多台设备组成“个人算力网”，欢迎试用"
source: v2ex
url: "https://www.v2ex.com/t/1215157"
author: "v2mryao"
date: 2026-05-24
score: 0
tags: ["llm", "LLM", "OpenAI", "ai", "openai"]
---

# agentserver: 把多台设备组成“个人算力网”，欢迎试用

写了一个开源项目 agentserver ，主要解决一个问题：当你有多台机器（笔记本、台式机、云主机、HPC ）都想用 codex 跑任务时，缺一个统一的注册、调度、凭证管理机制。

GitHub：github.com/agentserver/agentserver
托管实例： https://agent.cs.ac.cn （中国内地），https://agentserver.dev （海外）
License：Apache-2.0

核心模型

Connector：被接入的设备，在上面跑 codex exec-server --remote 即可注册进工作区。
Browser：实际敲命令的客户端或者 IM 渠道。codex --remote 把请求路由到指定 Connector ，也可以直接在微信 / Telegram 上直接指挥。
Server：注册表、凭证托管、LLM 代理、配额、审计、Web UI 。

围绕 OpenAI codex CLI 原生构建，设备端不需要额外装客户端，一行 npm i -g @openai/codex 就能接入。
主要特性：

会话跑在服务端，跨终端续接：同一段 codex 会话可以在 CLI 之间无缝切换，换设备不丢上下文。
IM 通道：支持微信 / Telegram / Matrix 作为指挥入口，离开桌面也能下发任务。
凭证不下发到端：Connector 永远不接触真实 LLM key ，所有出口流量过 llmproxy ，按工作区限速 / 统计 / 审计。
多人协作：邀请其他用户加入工作区，按 owner / maintainer / developer / guest 控制 RBAC 权限。
SSO：GitHub OAuth + 通用 OIDC （ Keycloak / Authentik 等）。

欢迎大家试用和拍砖🧱

…(内容已截断)

## 涉及话题
- llm
- LLM
- OpenAI
- ai
- openai

[原文链接](https://www.v2ex.com/t/1215157)
