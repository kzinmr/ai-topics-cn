---
title: "五一放假后 Vibe Coding 了一款 K8s 算力调度管理产品"
source: v2ex
url: "https://www.v2ex.com/t/1213370"
author: "joudev"
date: 2026-05-17
score: 0
tags: ["Claude"]
---

# 五一放假后 Vibe Coding 了一款 K8s 算力调度管理产品

一直想做一款自己的 K8s 运维平台方面的产品，五一放假那天开了 Claude Max 5x 订阅，一有时间就吭哧吭哧干，现在基本集群管理 + GPU 算力调度（基于 Volcano + HAMi-core ）都完工了，下一步计划是模型服务。

开源地址： https://github.com/togettoyou/kpilot

架构上采用 Server + Worker 模式，Worker 主动发起双向 gRPC 连接，所有 K8s 操作由 Worker 代理执行。Server 端不持有任何集群的 kubeconfig ，运行时数据 100% 来自 Worker push 。

整个项目都是和 Claude 结对写的。两周多的 commit 数密到都让我怀疑这种迭代速度是不是真的 😂

## 涉及话题
- Claude

[原文链接](https://www.v2ex.com/t/1213370)
