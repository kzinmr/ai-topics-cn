---
title: "🔥 Cursor 最 🐂 中转｜ 把 Cursor 的 token 账单拆开看，九成的钱花在 cache read 上"
source: v2ex
url: "https://www.v2ex.com/t/1232502"
author: "patamon0321"
date: 2026-08-06
score: 0
tags: ["Cursor"]
---

# 🔥 Cursor 最 🐂 中转｜ 把 Cursor 的 token 账单拆开看，九成的钱花在 cache read 上

把 Cursor 的 token 账单拆开看，九成的钱花在 cache read 上翻自己的用量记录时发现一件事。
一次 Opus 请求，总共 905 万 token ，四段拆开是：input 120 、cache write 40,319 、cache read 8,630,088、output 388 。
也就是说 99.6% 的 token 是缓存读取。按单价折算，这一段吃掉的钱也在九成以上。
这就有意思了 —— cache read 的单价只有 input 的十分之一。按实价算这次扣 $7.75 ；要是哪家中转把 cache read 混进 input 收，同一个请求能收你十倍不止，而你完全看不出来，因为它只会告诉你「本次消耗 1 次」。
所以判断一家中转有没有拿到上游真实用量，就看它给不给你这四个独立数字。

这是我做的 CodePass ，四段分开记。顺带 Composer / Grok / Tab 都在。$13/月，官方 Pro 要 $20 。
注册体验 👉： https://code-pass.dev?invite=VS9GZDEMW4VK
体验额度不够后台留言就行
💬 QQ 群：1018074251

## 涉及话题
- Cursor

[原文链接](https://www.v2ex.com/t/1232502)
