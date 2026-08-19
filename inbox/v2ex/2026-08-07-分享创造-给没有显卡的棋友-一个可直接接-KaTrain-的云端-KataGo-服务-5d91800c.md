---
title: "[分享创造] 给没有显卡的棋友：一个可直接接 KaTrain 的云端 KataGo 服务"
source: v2ex
url: "https://www.v2ex.com/t/1232840"
author: "malusama"
date: 2026-08-07
score: 0
tags: ["ai"]
---

# [分享创造] 给没有显卡的棋友：一个可直接接 KaTrain 的云端 KataGo 服务

电脑没显卡，或者笔记本跑不动全盘复盘，但想用 KaTrain 分析棋谱？我做了一个云端 KataGo 服务，KaTrain 里只需要填一个 WSS 地址。
怎么接入

注册后拿到 Token： https://go.malu.moe
KaTrain v1.18+ 的设置里，Remote Engine 填：wss://go.malu.moe/v1/katago/<你的 Token>
走的是标准 KataGo Analysis Engine JSON over WebSocket ，复盘、深度分析、Sweep 这些功能都兼容
不想用 GUI 的话也有 REST 接口：POST /v1/analyze

免费额度（注册即用，不用绑卡）

单次分析最多 1,000 visits
每月 1,000,000 visits ，按 KaTrain 默认 500 visits/手算，大约够 10 局全盘复盘
并发 1 ，最多 5 个 Token

实测数据
我用 2016 年 AlphaGo vs 李世石第 2 局（ 211 手，就是神之一手那盘）做了全盘逐手 800 visits 的串行复盘：

稳态下每手约 2.4 秒
整盘热状态约 8 分钟
但因为服务闲置会缩容到零，冷启动尖峰 17 秒到 2 分半不等，实际整盘约 20 分钟
这也是目前最需要大家帮忙压测的点。

另外

iOS/macOS 原生客户端 KataGo Review 也在做，棋谱走私人 iCloud 同步，Plus 订阅单次 5,000 visits 、每月 2,000,000 ，已提交 App Store 审核
macOS 上我封装了一个命令行：katagoreview game.sgf --visits 800 --review，一条命令导入棋谱并自动整局复盘


…(内容已截断)

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1232840)
