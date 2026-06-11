---
title: "LinkPeek AI 总结 接入 iMessage Bot"
source: v2ex
url: "https://www.v2ex.com/t/1219200"
author: "shigella"
date: 2026-06-09
score: 0
tags: ["AI"]
---

# LinkPeek AI 总结 接入 iMessage Bot

https://github.com/shigella520/LinkPeek/releases/tag/v1.3.0
最近 LinkPeek 从 1.1.0 之后更新了不少东西，这次最想分享的是：它已经不只是一个「链接预览工具」了。
现在它更像一个可以配合 iMessage 使用的链接分享 Bot 。
以前 LinkPeek 主要解决的是：

在 iMessage 里分享 V2EX 、NGA 、LINUX DO 、Bilibili 等链接时，自动生成更稳定、更好看的链接预览。
这次更新后，重点能力变成了三件事：
1. AI 分享总结

LinkPeek 现在可以按天、按周期整理分享过的链接，让 AI 自动总结这段时间大家都看了什么、聊了什么。
比如一天里丢了很多帖子、视频、社区链接，最后可以自动生成一份「今日链接总结」。

不用再手动翻聊天记录，也不用一个个点开回忆内容。
2. AI 生图对接

总结不只是一段文字，还可以进一步生成分享图。
也就是说，LinkPeek 可以把一段时间内的链接内容，整理成一张适合继续转发的图片卡片。

这对群聊复盘、内容推荐、每日摘要都很实用。
3. Webhook 自动通知

新增 Webhook 后，LinkPeek 可以把总结结果、分享图生成结果等事件自动推送出去。
这也是最关键的一步：

配合 BlueBubbles ，就可以把 LinkPeek 接进 iMessage ，做成一个真正能自动回复、自动推送的 LinkPeek Bot 。
大概效果是：
群里分享链接

LinkPeek 负责生成预览、记录链接

AI 定时总结内容

AI 生成分享图

Webhook 通知 BlueBubbles

最后由 iMessage Bot 发回群里

…(内容已截断)

## 涉及话题
- AI

[原文链接](https://www.v2ex.com/t/1219200)
