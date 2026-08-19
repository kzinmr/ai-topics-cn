---
title: "ZKE：把 Kubernetes 多集群控制台做成 macOS 风格的 Web Desktop"
source: v2ex
url: "https://www.v2ex.com/t/1233876"
author: "joudev"
date: 2026-08-12
score: 2
tags: ["Copilot", "AI", "llm"]
---

# ZKE：把 Kubernetes 多集群控制台做成 macOS 风格的 Web Desktop

ZKE （ Z Kubernetes Engine ）是一款面向私有网络与混合云环境的开源 Kubernetes 多集群管理平台。每个集群中的 Agent 通过 QUIC/mTLS 主动连接 Server ；浏览器端 Console 采用 macOS 风格的桌面式交互，将资源管理、终端、权限与审计组织在同一个工作空间中。
项目地址：github.com/togettoyou/zke
在线体验：https://fbcupchhlacp.sealosbja.site/
体验账号：view

体验密码：LECQkqcp2tQ5Yh8

多集群管理
在多集群场景中，仅把资源展示出来还不够，还要处理网络与作用域两层问题。
第一层是网络。位于中心侧的管理平台未必能够主动访问私有网络、边缘机房或独立安全域中的 Kubernetes API Server 。根据网络边界和安全策略，团队可能需要维护专线、VPN 、反向代理或额外的跳板入口。
第二层是作用域。运维人员从一个集群切换到另一个集群时，界面看起来可能没有明显变化，但操作目标已经变了。查询可以汇总，写操作却必须精确落到某个 Cluster 、Namespace 和资源对象。权限、确认和审计如果没有携带相同的作用域，多集群入口反而会放大误操作风险。
ZKE 给出的原则很直接：

全局观察，按集群执行。

用户可以从全局入口查看有权访问的资源，但集群资源查询和操作都会定域到明确的目标集群。全局视图不等于全局操作权限。
第一眼亮点：把控制台做成桌面
ZKE 最直观的区别不是表格多了几列，而是 Console 采用了一套运行在浏览器中的桌面式交互界面。
集群接入管理、组织与资源、访问与审计、容器服务和终端都以独立应用存在。用户可以从桌面或 Dock 打开应用，在窗口之间切换、最小化、最大化，并保存自己的桌面布局和工作作用域。

…(内容已截断)

## 涉及话题
- Copilot
- AI
- llm

[原文链接](https://www.v2ex.com/t/1233876)
