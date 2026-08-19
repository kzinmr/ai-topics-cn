---
title: "[开源]或许是 WindTerm 精神的续作： SSH 客户端 OxideTerm 焕新为原生软件， Windows 空载内存仅 25 MB"
source: v2ex
url: "https://www.v2ex.com/t/1229777"
author: "soleilune"
date: 2026-07-25
score: 25
tags: ["AI", "大模型"]
---

# [开源]或许是 WindTerm 精神的续作： SSH 客户端 OxideTerm 焕新为原生软件， Windows 空载内存仅 25 MB

大家好，我是 OxideTerm 的作者。
WindTerm 是很多人的心头好，极低的内存占用、原生级的流畅度，很少有替代品能完全复现。但它已经停更一年多了，积压的 Issue 长期也似乎无人修复，当然我也很希望作者能够再度更新。现在不少朋友一直在找下一个归宿，但市面上大多是 Electron/Tauri 的 WebView 应用，空载几百兆起步，很难找回那种轻快感。
我自己一直很尊重 WindTerm 坚持原生、不妥协的产品理念，也在做一款开源 SSH 工具 OxideTerm。我的 1.x 是用 Tauri 写的，很快就撞到了 WebView 的天花板：

空载吃内存：即使没打开任何会话，浏览器引擎、DOM 和 JS 运行时的固定开销就占着几百兆。
前后端跨语言通信效率受限：终端内容要跨越 Rust 和前端 JS 之间的数据链路，大日志刷屏时压力可能不小。

我发现局部优化解决不了架构问题。所以我做了一个决定：抛弃 WebView ，用纯 Rust 和 GPUI （ Zed 编辑器用的原生 GPU 渲染框架）完全重写了它。通过移除 WebView 、DOM 和 JavaScript 运行时，更换数据链路 ，我们省去了跨语言的序列化和 IPC 。macOS 空载从 320MB 降到了 80MB 出头，Windows 则从约 180MB 降到了 25MB 。 （自己的机器实测）

最近刚好过了 1000 Star 门槛，历经大量 issue 反馈，算是有了一定完成度，所以发出来再和大家分享。
OxideTerm 和 WindTerm 有什么共同点？


…(内容已截断)

## 涉及话题
- AI
- 大模型

[原文链接](https://www.v2ex.com/t/1229777)
