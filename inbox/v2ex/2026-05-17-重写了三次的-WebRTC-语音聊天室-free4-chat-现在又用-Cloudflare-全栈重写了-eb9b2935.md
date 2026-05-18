---
title: "重写了三次的 WebRTC 语音聊天室： free4.chat，现在又用 Cloudflare 全栈重写了"
source: v2ex
url: "https://www.v2ex.com/t/1213306"
author: "bmpidev2019"
date: 2026-05-17
score: 1
tags: ["AI", "ai"]
---

# 重写了三次的 WebRTC 语音聊天室： free4.chat，现在又用 Cloudflare 全栈重写了

四年前我发了第一个帖子介绍这个项目：搭了一个 WebRTC 语音聊天室，效果惊人
两年前用 Elixir 重写了一次：用 Elixir 重写 WebRTC 语音聊天室，自带集群扩容
现在又用 Cloudflare 全栈重写了一遍，顺便把一直想加的功能都加上了，水个帖子。

free4.chat 是什么？
一个无需注册、开箱即用的浏览器实时聊天室。你分享房间链接，对方打开就能聊，用完什么都不留。
核心理念就两个字：简单、隐私。
目前支持：

🎙️ 语音通话：多人房间，WebRTC SFU 架构，延迟低
💬 文字聊天：支持发文本、图片、文件
🖥️ 屏幕共享：一键分享，房间内所有人可见
🤖 Luna AI 助手：房间内 @luna 即可召唤 AI ，有上下文记忆，每个房间独立会话
🎮 互动小工具：白板、投票、小游戏（进行中）

开源地址： https://github.com/i365dev/free4chat
在线地址： https://free4.chat

这次重写做了什么？
之前是 Elixir 后端部署在 AWS EC2 + 前端部署在 Cloudflare Pages ，要维护两台服务器集群，运维成本不低。
这次用 Cloudflare 全栈重写：

前端：Next.js 15 ，通过 @opennextjs/cloudflare 编译成 Cloudflare Worker 运行
实时通信：换成 Dyte/RTK （ Realtime Kit ），托管 SFU ，不用自己维护媒体服务器了
AI 会话：Cloudflare Durable Objects ，每个房间一个独立的 AI 会话，用 @cf/zai-org/glm-4.7-flash 模型
安全：Cloudflare Turnstile 防机器人，KV 限流，Origin 白名单

…(内容已截断)

## 涉及话题
- AI
- ai

[原文链接](https://www.v2ex.com/t/1213306)
