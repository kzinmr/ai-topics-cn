---
title: "用 Socket 保护 DeekSeep Harness 的安装和执行过程"
source: v2ex
url: "https://www.v2ex.com/t/1235436"
author: "Livid"
date: 2026-08-18
score: 2
tags: ["ai", "deepseek", "DeepSeek"]
---

# 用 Socket 保护 DeekSeep Harness 的安装和执行过程

socket.dev 是一个 NPM 生态的安全扫描服务。
安装和打开 socket 提供的防御：
npm install -g socket
socket wrapper on

然后在通过 npx 执行 DeepSeek Harness 就可以看到 socket 的保护生效了：
npx @deepseek-ai/dsh web

## 涉及话题
- ai
- deepseek
- DeepSeek

[原文链接](https://www.v2ex.com/t/1235436)
