---
title: "Codex 手机号验证教程:怎么获取号码 + 收不到、whatsapp 二次验证怎么办"
source: v2ex
url: "https://www.v2ex.com/t/1213653"
author: "softsoil"
date: 2026-05-18
score: 1
tags: ["OpenAI", "ai", "openai"]
---

# Codex 手机号验证教程:怎么获取号码 + 收不到、whatsapp 二次验证怎么办

Codex 手机号验证教程:怎么获取号码 + 收不到怎么办

> 整理一下最近被问得最多的 Codex 踩坑问题,顺便分享出来。


四个坑,按踩到的频率从高到低排:


1. WhatsApp 推送陷阱
这是最容易翻车的一个。
有些国家的号码,OpenAI 默认通过 WhatsApp 推送验证码,而不是 SMS 。你从号码服务这边拿到的是个纯 SMS 通道的号,那这个号永远收不到 OpenAI 的验证码——因为信根本没发到 SMS 这条路上来。
这跟号码本身好不好用没关系。你换号、换平台、点重发,都是同一个结果——只要你选的国家被 OpenAI 划到 WhatsApp 推送区域,SMS 信道这边就是死路。


判断方法很简单:看 OpenAI 验证页面那行提示——如果写的是 `a code has been sent to ... via WhatsApp`,基本就废了。美国 / 英国 / 俄罗斯一般走 SMS,相对稳定。


2. 重复点 resend 会被静默限流
这是另一个普遍误判。
OpenAI 后端对「重发验证码」有 silent rate limit——你点一次,它发一次;你连续点 5 次,后面那几次不是「让队列里多塞几条」,而是被静默扔掉,你在前端完全看不到错误,只看到一直没收到。
这套机制本来是反脚本的,但顺带把着急的真实用户一并误伤了。
如果你前 1 分钟点了三次 resend 都没收到,别再点了。等 15-20 分钟,让节流窗口过去,再点一次,通常就到了。这事 GitHub 上 openai/codex 仓库的讨论区已经有维护者确认过,不是猜的。


3. 号码格式 bug
几个具体国家踩过:

…(内容已截断)

## 涉及话题
- OpenAI
- ai
- openai

[原文链接](https://www.v2ex.com/t/1213653)
