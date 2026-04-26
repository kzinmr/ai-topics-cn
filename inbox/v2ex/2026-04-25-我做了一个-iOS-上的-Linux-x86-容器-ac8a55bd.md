---
title: "我做了一个 iOS 上的 Linux x86 容器"
source: v2ex
url: "https://www.v2ex.com/t/1208561"
author: "unnyxi"
date: 2026-04-25
score: 0
tags: ["Gemini"]
---

# 我做了一个 iOS 上的 Linux x86 容器

技术详情
在线体验
GitHub Repo
AltStore
Podish 是一个面向 iOS / Apple Silicon 专门优化的高性能 Linux x86 用户态容器。它用 C++ 写了一个 i686 解释器核心，用 C# 写了 Linux 兼容层，在 iPhone 17 (A19) 上跑出 CoreMark ~3400 ，比 iSH 快一倍。
我最近几个月的周末一直在做一个项目：跨平台的 Linux x86 用户态容器，并面向 iOS/Apple Silicon 专门优化。
这个项目现在叫 Podish 。我的目标不是复刻一个 UTM ，而是尽可能高效地在 JIT 受限的平台（就是你，iOS ）上运行 x86 用户态程序。
它现在能跑 Busybox ，Bash ，Python, LuaJIT, GCC ，OpenSSH 甚至 Node.js 。我成功在上面跑起了 Gemini CLI 。

## 涉及话题
- Gemini

[原文链接](https://www.v2ex.com/t/1208561)
