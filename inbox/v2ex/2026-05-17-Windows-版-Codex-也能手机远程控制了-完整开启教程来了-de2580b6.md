---
title: "Windows 版 Codex 也能手机远程控制了，完整开启教程来了"
source: v2ex
url: "https://www.v2ex.com/t/1213297"
author: "scf2024"
date: 2026-05-17
score: 1
tags: ["ChatGPT", "AI", "ai"]
---

# Windows 版 Codex 也能手机远程控制了，完整开启教程来了

这两天，我把 Windows 版 Codex 的手机远程控制功能折腾通了。
先说结论：
Windows 版 Codex 其实已经带了远程控制能力，只是默认没有完全放出来。
如果你的界面里只有 SSH connections from this PC，看不到 Control this PC 或 Control other devices，不一定是你版本太旧，也不一定是你找错了地方。更可能的情况是：功能代码已经在客户端里，但开关还没有真正生效。
我一开始也被这个问题绕了一圈。
官方页面还在说 Windows 支持即将到来，客户端安装包里却已经有了 Connect a device to this PC、Control this PC 这些界面文案。真正把问题拆开后才发现，“功能已经写进客户端” 和 “功能已经对你的账号开放” 之间，中间还隔着一层配置和授权。
这篇文章不只讲原理，也把完整脚本、完整操作步骤，以及一段可以直接复制给 Codex 的提示词都放出来。
你甚至可以把这篇文章直接发给 Codex ，让它照着检查你的电脑并自动完成配置。
一、先确认你遇到的是不是同一个问题
如果你打开 Codex：

进入 Settings
打开 Connections
页面里只看到 SSH connections from this PC

那你遇到的，大概率就是我碰到的这个问题。
也就是说：

客户端里已经有远程控制相关功能
但当前界面只展示了 SSH
远程控制的入口还没有真正出现

二、真正关键的配置，不在界面里
Codex 的本地配置文件在这里：
C:\Users\<你的用户名>\.codex\config.toml

打开后，找到 [features] 这一段。
很多人的配置里，原本只有这些：
[features]
goals = true

…(内容已截断)

## 涉及话题
- ChatGPT
- AI
- ai

[原文链接](https://www.v2ex.com/t/1213297)
