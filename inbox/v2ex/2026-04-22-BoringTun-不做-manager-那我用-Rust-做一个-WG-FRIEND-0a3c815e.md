---
title: "BoringTun 不做 manager，那我用 Rust 做一个： WG-FRIEND"
source: v2ex
url: "https://www.v2ex.com/t/1207613"
author: "enrolls"
date: 2026-04-21
score: 1
tags: ["prompt"]
---

# BoringTun 不做 manager，那我用 Rust 做一个： WG-FRIEND

最近在折腾一个项目：WG-FRIEND
一句话介绍：
Semantic WireGuard/BoringTun lifecycle and client management helper
它的出发点其实很简单：
我这边最近比较常见的几个场景，是需要一台比较稳定的服务器做跨网络访问，需要远程回家，也需要把多台设备之间的 WireGuard 生命周期管理得更清楚一些。
但我一直觉得，现有这类方案里有个空档：

wg-quick 很好用，但更像“把接口拉起来”的工具
PiVPN 这类方案很适合快速起量，但整体还是偏 shell/script orchestration
BoringTun 很强，尤其是 Rust userspace WireGuard 这条路线很有价值，但它本身并不负责 manager / control plane

所以用 Rust 实现 的 wg-friend 就此开始：将“拉起接口 / 管理服务 / 管理客户端 / 导入历史资产 / 做诊断”这些事情，从零散脚本提升成一个语义更明确的 control plane 。
目前这个项目主要做了几件事：
1. 把 WireGuard/BoringTun 的操作语义化
命令面我切成了四组：

server
client
service
doctor

我不太想继续沿用“全靠 shell 拼起来”的方式，而是想把常用动作收敛成更稳定的 CLI 语义。
2. 不再把客户端状态散落在各处
wg-friend 会把可完整物化的客户端，纳入 /etc/wg-friend 下面的 canonical state 。
也就是说，进入管理域的前提不是“这个客户端貌似存在过”，而是它必须足够完整，能产出：

元数据
标准导出配置
QR-ready payload

3. 给历史部署一条 import 路径

…(内容已截断)

## 涉及话题
- prompt

[原文链接](https://www.v2ex.com/t/1207613)
