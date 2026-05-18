---
title: "做了一个 Chrome 扩展 Grok Automation，让 Grok Imagine 可以批量跑图跑视频"
source: v2ex
url: "https://www.v2ex.com/t/1212539"
author: "funet"
date: 2026-05-13
score: 0
tags: ["AI", "agi", "prompt", "ai"]
---

# 做了一个 Chrome 扩展 Grok Automation，让 Grok Imagine 可以批量跑图跑视频

起因
我自己日常在 grok 上用 Grok Imagine 出图、出短视频，主要是给 YouTube Shorts 做素材和给电商的 SKU 出测试图。
用着用着发现一个很尴尬的事：grok 的网页只能一条 prompt 一条 prompt 地提交，出图要等,出视频更要等，
而且每生成完一个还得手动右键「另存为」,文件名还都是 (1).mp4、(2).mp4 这种鬼东西。
我一晚上能写 80 条 prompt ，但真要把它们全跑完、再整理好，得我守着电脑两三个钟头。
这种活，机器干显然比人干合适。
思路
xAI 那个官方的 Grok Tasks 只能做「定时让 Grok 帮你跑一次问答然后邮件给你」，
完全不解决我这种「批量生成媒体文件」的场景。
所以路线只有一个：写个 Chrome 扩展，注入 content script ，接管 grok 的 UI ，自己点自己等自己存。
后来这个扩展我起名叫 Grok Automation，下面把几个有点意思的实现细节说一下。
实现里几个有点意思的点


DOM 变化用 MutationObserver 兜底
grok 的前端是 SPA ，按钮、loading 状态、生成完成的标记都是异步出现的。
一开始用 setTimeout 轮询，跑 50 条以上就开始飘。后来全部改成 MutationObserver
监听特定容器，配合一个状态机，稳定性才上来。


智能延迟，不是固定 sleep
一开始我设的是「每条 prompt 之间 sleep 10 秒」，结果有些 prompt 5 秒就出完了在干等，
有些跑 30 秒还没好就被下一条挤掉。后来改成「等当前生成结束 + 一个小抖动」，
既不被限流也不浪费时间。


自动下载和命名

…(内容已截断)

## 涉及话题
- AI
- agi
- prompt
- ai

[原文链接](https://www.v2ex.com/t/1212539)
