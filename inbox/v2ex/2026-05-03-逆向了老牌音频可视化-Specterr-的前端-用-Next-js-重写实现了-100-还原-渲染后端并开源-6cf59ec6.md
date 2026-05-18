---
title: "逆向了老牌音频可视化 Specterr 的前端，用 Next.js 重写实现了 100%还原+渲染后端并开源"
source: v2ex
url: "https://www.v2ex.com/t/1210139"
author: "linncharm9"
date: 2026-05-03
score: 0
tags: ["llM"]
---

# 逆向了老牌音频可视化 Specterr 的前端，用 Next.js 重写实现了 100%还原+渲染后端并开源

最近一直在用 Specterr 给音乐做可视化视频，但它要订阅收费，而且功能其实挺简单的——无非就是 waveform / spectrum 跑在一段背景视频上，加个 logo 导出。
后面发现他的代码没有关闭 source map
于是干脆逆向了它的前端源码，摸清楚数据结构和渲染逻辑之后，用 Next.js 从头重写了前端，然后自己实现了渲染后端。
项目叫 Spectral ，现在开源了：
https://github.com/charmlinn/spectral
技术栈：
前端：Next.js 16 + React 19 + PixiJS （实时预览）
渲染后端：Node.js + Headless Chromium + ffmpeg （帧渲染 + 编码）
队列：Redis + BullMQ
存储：Cloudflare R2 / MinIO
数据库：PostgreSQL + Prisma
核心设计思路： 前端预览和后端导出共用同一套 PixiJS runtime 和同一份项目 schema ，保证预览和导出结果一致。
目前支持：waveform / spectrum 可视化、背景图片/视频、logo 、文字图层、浏览器实时预览、后端异步渲染队列。
本地用 Docker Compose 起全套环境，README 里有详细文档。
如果有人用 Specterr 或者类似工具的，欢迎试试，也欢迎提 issue 或者聊聊渲染这块的实现细节。

## 涉及话题
- llM

[原文链接](https://www.v2ex.com/t/1210139)
