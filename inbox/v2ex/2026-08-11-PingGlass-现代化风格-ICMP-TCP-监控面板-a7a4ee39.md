---
title: "PingGlass - 现代化风格 ICMP / TCP 监控面板"
source: v2ex
url: "https://www.v2ex.com/t/1233682"
author: "samsam123"
date: 2026-08-11
score: 1
tags: ["rag", "ai"]
---

# PingGlass - 现代化风格 ICMP / TCP 监控面板

PingGlass - 现代化风格 ICMP / TCP 监控面板
相信各位有网络 ICMP 监控需求的话，或多或少都听过 SmokePing 这个项目。
SmokePing 是一个非常经典的开源网络性能监控工具，主要用于测量、记录以及可视化网络的 延迟、丢包率和连通性。从 2001 年发展至今，也算是经历了二十多年的风风雨雨。
我自己也用了 SmokePing 很长一段时间，不过随着监控的 Targets 越来越多，逐渐发现一些使用上的痛点。
其中一个最直接的问题就是它的 UI 。
SmokePing 的 Web UI 还是比较偏向传统桌面网页，在手机上查看的时候体验并不是特别友好 —— 而我本人又特别喜欢直接拿手机看网络状况。
另外，SmokePing 的图表主要是在后端生成，而不是像现在比较常见的 Web Application 一样，由后端提供数据，再交给前端进行交互和渲染。
当 Targets 数量越来越多以后，无论是管理 Targets ，还是日常查看大量监控图表，整体体验都会开始变得比较笨重。
于是就有了一个想法：

如果重新做一个现代版的 SmokePing ，会是什么样子？

然后坑就这样挖下去了 这不是好事
于是有了：
PingGlass
PingGlass 是一个现代化 ICMP / TCP 网络延迟、丢包以及可用性监控面板。
项目目前主要使用：

Laravel 11
Vue 3
Inertia.js
Tailwind CSS
Apache ECharts
MySQL
Redis

监控部分：

ICMP 使用 fping
TCP 则直接通过 PHP Non-blocking Socket / stream_select 建立连接并计算连接延迟

整个系统就是一个 Laravel ，不需要额外再跑一个独立的 Probe 。


…(内容已截断)

## 涉及话题
- rag
- ai

[原文链接](https://www.v2ex.com/t/1233682)
