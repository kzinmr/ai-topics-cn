---
title: "分享下自己 vibecoding 的 android ssh 软件，基于 connectbot + frp 来实现"
source: v2ex
url: "https://www.v2ex.com/t/1207272"
author: "awenforlinux"
date: 2026-04-20
score: 0
tags: ["ai"]
---

# 分享下自己 vibecoding 的 android ssh 软件，基于 connectbot + frp 来实现

我在 mini 主机上安装了 OpenClaw 对接了飞书和微信，有时候他自动升级后就挂了，比如变更了权限导致飞书问问题卡且不回复，但是如果是在外面没法远程家里的机器，无法 SSH 连接，虽然有 Cloudflare Tunnel Tailscale 但是我试了比较卡，所以我自己基于 connectbot  把 frp 整合下，实现 android 客户端 ssh 主要是服务端你如果有带公网的主机完全可以自己部署，自建服务端、完全可控、不依赖网关转发，我使用 Go 交叉编译了 Android 版的 frpc ，以 libfrpc.so 的形式打包进 APK 。这样 Android 安装时会自动按 ABI 解压到 nativeLibraryDir ，避免了 Android 10+ 对动态提取二进制文件的执行限制。

具体见我的博客 https://www.awen.me/post/27e55299.html
项目地址 https://github.com/monkey-wenjun/connectbot

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1207272)
