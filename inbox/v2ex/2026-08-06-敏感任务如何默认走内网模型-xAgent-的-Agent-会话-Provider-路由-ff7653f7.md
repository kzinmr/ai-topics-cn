---
title: "敏感任务如何默认走内网模型： xAgent 的 Agent / 会话 Provider 路由"
source: v2ex
url: "https://www.v2ex.com/t/1232480"
author: "coffeehc"
date: 2026-08-06
score: 0
tags: ["LLM", "MCP"]
---

# 敏感任务如何默认走内网模型： xAgent 的 Agent / 会话 Provider 路由

很多团队同时有两类任务：日常工作可以调用第三方 LLM API ，合同、客户材料和内部经营数据则希望模型请求只到公司控制的服务.

我把这个边界落在了三个可复用的配置层：

管理员准备两条模型配置：例如 general-external 指向获准的外部 Provider ，confidential-internal 指向自建模型或内网模型网关。
为机密资料处理创建专用 Agent ，把默认模型选择为 confidential-internal ，并只附带该业务真正需要的 Skill 和 Tool 。
从这个 Agent 新建的 Session 会以内部模型配置作为默认路由；一次性的敏感任务也可以直接在 Session 层选择内部模型。

这里的关键不是把 Provider 地址或 API Key 写进提示词。Agent 和 Session 只引用模型配置名，服务端再解析为实际 Provider client ，凭据和 Base URL 仍保留在管理员配置中。
上线前不能只看设置页。我们用带唯一标识的测试材料验证：xAgent 运行记录里的实际模型配置、内部网关日志、外部 Provider 网关或出口代理日志必须形成一致证据。附件、Tool 、子会话和后续追问也要分别复测。
边界也要说清楚： Agent 或 Session 默认走内部模型，只说明模型请求默认进入内部 Provider ；它不自动证明所有数据都不会离开公司。MCP 、Tool 、Connector 、文件服务和网络出口仍需要独立做权限、审批、允许列表和审计控制。
完整配置与验证步骤：
https://xagent.xiagaogao.com/blog/agent-session-provider-routing/

## 涉及话题
- LLM
- MCP

[原文链接](https://www.v2ex.com/t/1232480)
