---
title: "尝试只用 clash 核心筛选解锁 ChatGPT 的节点"
source: v2ex
url: "https://www.v2ex.com/t/1227321"
author: "340746"
date: 2026-07-14
score: 0
tags: ["AI", "openai", "chatgpt", "ChatGPT"]
---

# 尝试只用 clash 核心筛选解锁 ChatGPT 的节点

clash 的自动选择代理组有两个参数

url 是测速链接,expected-status 是测速的返回值,支持范围和准确数值,只有返回这些数值时才判定为 alive

询问 AI 得到

url: https://api.openai.com/v1/models
expected-status: 401
我只用网页版的 ChatGPT,这个组合用了一段时间发现效果不是很好

尝试设置 chatgpt.com,预期状态 200,发现所有节点均为 false

问题来了,用 api 使用相同的配置测速,一半以上节点都是 alive,把配置文件里面的预期状态改为 200-500,测速后得到正常的结果

经过多次测试,得到预期状态为 403 时,一半以上的节点能通过测试且可正常使用

## 涉及话题
- AI
- openai
- chatgpt
- ChatGPT

[原文链接](https://www.v2ex.com/t/1227321)
