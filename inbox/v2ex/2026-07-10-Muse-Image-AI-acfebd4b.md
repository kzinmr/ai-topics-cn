---
title: "Muse Image AI"
source: v2ex
url: "https://www.v2ex.com/t/1226514"
author: "zxhywork"
date: 2026-07-10
score: 0
tags: ["ai", "prompt", "AI"]
---

# Muse Image AI

Meta Superintelligence Labs 7 月 7 号发布了他们第一个图像模型 Muse Image ，内部代号 Mango 。玩了两天，这个模型有几个点确实有意思：

Agentic 生成：出图前先规划布局，需要事实的场景会联网搜，画完自查一轮再交稿，长 prompt 一次过的概率明显高
图内文字能看了：海报标题、图表、甚至可扫的二维码都能直接画进图里，这是大部分生图模型至今糊掉的地方
多参考图合成：从几张照片里分别取人脸、服装、产品、背景，融成一张不违和的图

官方入口在 Meta AI App / meta.ai / Instagram Stories ，国内用着别扭，还得装 App 。我就照着上一个站的路子做了个纯网页版：museimages.io。
产品上砍得很狠，只做图像，三个入口：

Meta Muse Image 在线生成器 —— 主生成入口
AI 文生图 —— 直出 4K
AI 图生图 —— draw-to-edit + 多参考图改图

技术栈还是那套：Next.js 15 + Cloudflare Workers （ OpenNext ）+ Supabase + Stripe 。这次从克隆仓库到绑域名上线只花了 3 天，模板化上站的流程算是被我彻底摸顺了。
顺带一提，Muse Image 发布后争议也不小 —— 公开的 Instagram 账号可以被别人 @ 进 prompt 里拿照片生成新图，隐私这块 Meta 又被喷了一轮，感兴趣的可以搜下 TechCrunch 的报道。
新注册有免费额度，欢迎体验。有 bug 或文案问题直接拍脸上，感谢。

## 涉及话题
- ai
- prompt
- AI

[原文链接](https://www.v2ex.com/t/1226514)
