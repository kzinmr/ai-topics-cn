---
title: "使用 Hermes Agent 结合 MiniMax Token Plan 使用体验"
source: v2ex
url: "https://www.v2ex.com/t/1206404"
author: "hubianluanma"
date: 2026-04-16
score: 1
tags: ["AI"]
---

# 使用 Hermes Agent 结合 MiniMax Token Plan 使用体验

最新的 MiniMax Token Plan 中悄悄的多了很多其他能力，除了之前的文本生成能力，现在具备：

Text to Speech HD
music-2.6
music-cover
lyrics_generation
image-01
coding-plan-vlm
coding-plan-search

这周我在深度使用 Hermes Agent ，目前感觉下来要比 OpenClaw 强，因为我用不到很多花里胡哨的功能，只希望能跑通以下几点：

可以帮我收集最新动态然后生成博客，自动部署博客
为博客配图，图片为 AI 生成
可以做音乐（纯玩，已经开通了网易云音乐人），可以写歌词+做音乐自动化
其他一些简单的自动化任务

目前来说我都跑通了，只用了 MiniMax 这一个模型，具体的过程我也让 Hermes 自动写了一篇博文部署到了我的站点: https://blog.hubianluanma.com/posts/minimax-media-pipeline/
做的音乐可以在网易云搜索：胡编乱码，我比较满意的是《晓春》这首，是写给我老婆的。
如果有 MiniMax Plus 订阅的小伙伴可以试一下，不过要说明的是，其实我 Macmini 本地已经在之前搭建好了基础环境，例如：

结合 Cloudflare 的内网穿透
MinIO 对象存储，以便生成的图片和其他文件能够被域名访问到（以通过 Hermes 总结为 skills 固化）
Hugo + GitHub Actions 的博客自动化部署

所以，如果真的想很方便的干一些有价值的事情，基础环境很重要。

## 涉及话题
- AI

[原文链接](https://www.v2ex.com/t/1206404)
