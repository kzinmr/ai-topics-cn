---
title: "我的第一个 iOS App ， OAuth 登录的 Cloudflare 管理客户端"
source: v2ex
url: "https://www.v2ex.com/t/1220405"
author: "chenzhe"
date: 2026-06-14
score: 0
tags: ["ai"]
---

# 我的第一个 iOS App ， OAuth 登录的 Cloudflare 管理客户端

App 叫 Orange Cloud ，是 iPhone / iPad 上的一个 Cloudflare 第三方管理客户端。我自己有几个域名、一堆 Workers 和 R2 挂在 Cloudflare 上，平时想在手机上看一眼流量、改条 DNS 、翻翻 Workers 日志，要么得开电脑，要么去开官方的移动网页，都不太顺手。第三方 App 也试过几个，最劝退我的是登录方式：先去 Dashboard 手动建一个 API Token ，一项项勾权限，再把一长串粘进 App 。权限给多了不放心，给少了又不够用，想换还得从头来。

所以这个 App 我最先动手重做的，就是登录。

Cloudflare 官方其实是支持 OAuth 2.0 + PKCE 的，只是很少有第三方用。我把整个登录都搭在它上面：点一下登录，弹出官方授权页，想授哪些权限自己一项项勾，DNS 读写、Workers 、分析都能单独选；授权完 Token 只写进设备本地的钥匙串，不上传，也不过我的服务器。我这边的 Web 端只是个 OAuth 回调中转，连授权码都不留。不想用了，去 Cloudflare Dashboard 一键撤销。对我来说这是装上之后最安心的一点。

剩下的就是尽量把常用功能塞进去：域名和 DNS 的增删改查、代理开关；流量分析，请求、带宽、缓存命中、拦了多少威胁都在里面，用 Swift Charts 画；存储这块 R2 对象浏览、D1 的 SQL 控制台、KV 键值都能管；再加上 WAF 规则的查看启停和 Tunnel 状态。

我自己最常开的是 Workers 实时日志，基本就是把 wrangler tail 搬到了手机上。WebSocket 直连，日志一行行往下滚，还接进了灵动岛和锁屏实时活动。


…(内容已截断)

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1220405)
