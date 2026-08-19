---
title: "给 sing-box 提交 XHTTP 实现后 PR 被关闭且账号被 Block，想请教是哪里做错了"
source: v2ex
url: "https://www.v2ex.com/t/1229097"
author: "universitypking"
date: 2026-07-22
score: 0
tags: ["AI"]
---

# 给 sing-box 提交 XHTTP 实现后 PR 被关闭且账号被 Block，想请教是哪里做错了

先说明一下，发这个帖子不是想挂人，也不是要求项目必须合并我的代码。
我只是第一次遇到这种情况：花时间实现了一个功能、补测试和文档、修完 CI ，随后 PR 在没有任何评论的情况下被关闭，之后发现
自己的 GitHub ID 似乎也被该项目 Block 了。
因为没有收到原因，所以想把时间线和技术背景完整写出来，请有开源项目维护经验的 V 友帮我看看，问题可能出在哪里。
项目：SagerNet/sing-box
PR： https://github.com/SagerNet/sing-box/pull/4326
PR 标题：feat(xhttp): add XHTTP transport
时间线：


7 月 17 日开始实现 sing-box 的 XHTTP transport 。


7 月 22 日 14:34 左右整理并提交主要实现，包括：

XHTTP 客户端和服务端
stream-one 、stream-up 、packet-up 等模式
HTTP/1.1 、HTTP/2 、h2c
Xray 兼容配置字段
xmux 、padding 、download settings 等功能



14:35 左右补充生命周期测试、协议测试以及与外部 Xray-core 可执行文件的互操作测试。


14:37 创建 PR #4326 。


PR 创建后发现 CI/Lint 有格式问题，于是根据 CI 输出修正并重新推送。


14:58 推送 lint 修复。之后 GitHub Actions 中 Linux 、Windows 、macOS 、Android 各平台的 Lint 和 Test 都通过了。


15:23 ，PR 被项目维护者直接关闭。



…(内容已截断)

## 涉及话题
- AI

[原文链接](https://www.v2ex.com/t/1229097)
