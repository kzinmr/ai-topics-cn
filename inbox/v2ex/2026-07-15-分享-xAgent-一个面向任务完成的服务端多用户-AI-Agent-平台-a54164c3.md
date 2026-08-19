---
title: "分享： xAgent，一个面向任务完成的服务端多用户 AI Agent 平台"
source: v2ex
url: "https://www.v2ex.com/t/1227596"
author: "coffeehc"
date: 2026-07-15
score: 0
tags: ["MCP", "AI Agent"]
---

# 分享： xAgent，一个面向任务完成的服务端多用户 AI Agent 平台

最近把 xAgent 的公开测试版完善到了 v0.0.4.beta ，想在这里分享一下这个项目的定位。
xAgent 不是聊天或陪伴产品，重点是让 AI Agent 在服务器上持续完成工作：用户给出目标和材料，Agent 可以使用 Skill 、Tool 、MCP 或连接器，产出文件、结果或需要确认的审批。
目前几个我认为比较有价值的设计：

服务端部署：一个二进制文件运行，用户通过 Web 或 IM Connector 使用；任务不依赖用户电脑保持在线。
多用户工作区隔离：不是简单按目录区分。xAgent 在底层文件系统之上维护虚拟文件系统，用户与其 Agent 会话只能发现、读取、写入被允许的文件；部分系统文件不会对用户暴露。
动态能力加载：会话默认只保留少量核心能力。任务缺少 Tool 或 Skill 时，Agent 可以自行发现并加载，减少无关上下文；高级配置中显示的是常驻能力，不会把动态加载结果混在里面。
运行中热切换：任务执行过程中可以调整提示词、Skill 或模型，不必放弃会话重新开始。
安全治理：管理员可以配置公共审批底线，高级用户也可以细调个人审批策略，用于控制外部发送、敏感数据或高风险动作。
连接器：当前已发布微信、Telegram 、飞书 Connector ，可以把 IM 消息作为任务入口； Connector 管理外部登录态和凭证，避免把真实密钥放入会话。

目前是二进制发布的测试版，免费版 5 用户内可用，推荐部署在自己的服务器与数据环境中。没有官方 SaaS 计划。
中文文档：
https://xagent.xiagaogao.com/
GitHub Release：
https://github.com/coffeehc/xagent-releases/releases

…(内容已截断)

## 涉及话题
- MCP
- AI Agent

[原文链接](https://www.v2ex.com/t/1227596)
