---
title: "[自用开源] QuotaBarWin，在 Windows 系统下也能通过托盘菜单查看 Agent 剩余额度了"
source: v2ex
url: "https://www.v2ex.com/t/1227060"
author: "Shawlaw"
date: 2026-07-13
score: 1
tags: ["DeepSeek", "Kimi"]
---

# [自用开源] QuotaBarWin，在 Windows 系统下也能通过托盘菜单查看 Agent 剩余额度了

项目地址
https://github.com/Shawlaw/QuotaBarWin

Why
1 、手动开着 Agent 提供商的网页或者在各 TUI/客户端分开查询好繁琐
2 、CodexBar 挺好看的，可惜只支持 MacOS ，但我的常驻平台是 Windows
3 、没试过 Tauri 这种原生 WebView 容器的桌面客户端开发，看样子比裸 Rust+EGUI 的方案好看很多，想试试，所以就没有再去 Github 上搜成品项目

What
一个仅 Windows 平台的 Agent 剩余额度查询展示软件，QuotaBarWin 。
特性：
1 、基本开箱即用，目前支持 Codex 、智谱 CodingPlan 、Kimi Plan 还有 DeepSeek 余额的查询显示；支持自定义来源查询——理论上能做任何业务额度的查询展示工具
2 、支持右下角图标点击后出托盘小窗显示剩余额度
3 、支持 cli 调用，方便给本地 Agent 调用使用感知自身可用额度从而规划推进长序任务——例如，“每完成一步任务都通过 cli 查询验证自己的额度是否低于 3%，如果低于 3%，那么睡眠直到重置时间之后再推进下一步任务”
4 、支持同一 Agent 多账号的剩余额度查询展示
5 、程序本体大小大概 5MB 左右
6 、只支持额度查询显示，没有更详尽的用量统计

感想
一个能跑的程序和一个觉得足够通用到能够让我觉得可以发文自荐的程序之间确实隔着不少迭代，这甚至还只是“方便查看剩余额度”的这个小需求而已

## 涉及话题
- DeepSeek
- Kimi

[原文链接](https://www.v2ex.com/t/1227060)
