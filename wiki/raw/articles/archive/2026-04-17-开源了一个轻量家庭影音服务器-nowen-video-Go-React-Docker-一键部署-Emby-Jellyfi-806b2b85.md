---
title: "开源了一个轻量家庭影音服务器 nowen-video， Go + React， Docker 一键部署， Emby/Jellyfin 的轻量替代"
source: v2ex
url: "https://www.v2ex.com/t/1206709"
author: "cropflre"
date: 2026-04-17
score: 1
tags: ["通义千问", "llama", "DeepSeek", "ai", "OpenAI", "AI"]
---

# 开源了一个轻量家庭影音服务器 nowen-video， Go + React， Docker 一键部署， Emby/Jellyfin 的轻量替代

正文
各位 V 友好，分享一个自己在做的开源项目 nowen-video —— 一个轻量级家庭媒体服务器。
做这个的初衷是觉得 Emby/Jellyfin 对于小 NAS 来说太重了，想要一个单二进制 + SQLite 、Docker 一键跑起来的方案。
技术栈

后端：Go + Gin + GORM + SQLite(WAL)
前端：React 18 + TypeScript + Tailwind CSS
客户端：Android 原生（ Jetpack Compose ）
部署：Docker Alpine ，前端内嵌，单端口服务

主要功能
🎬 媒体管理 — 自动扫描 MKV/MP4 等 9 种格式，FFprobe 提取元数据，实时文件监控（ fsnotify ）
📺 智能播放 — 浏览器兼容格式直接播放，不兼容走 HLS 按需转码（ 360p~1080p ），支持 Intel QSV / VAAPI / NVENC 硬件加速
🎨 多源刮削 — Provider Chain 架构，TMDb → 豆瓣 → TheTVDB → Bangumi → Fanart.tv → AI 兜底，自动匹配海报/简介/评分
📂 剧集识别 — 自动识别 S01E01 / 第 01 集 / EP01 等命名格式，支持季目录结构
🧠 AI 功能 — 自然语言搜索、智能推荐、元数据增强、文件重命名、AI 对话式管理助手（支持 OpenAI/DeepSeek/通义千问/Ollama ）
👨‍👩‍👧‍👦 多用户 — 独立账号/历史/收藏/播放列表，细粒度权限控制，内容分级
📡 Emby 兼容 — 提供 Emby 兼容 API ，支持第三方客户端接入
📱 Android 客户端 — 原生 Jetpack Compose 开发，赛博朋克主题

…(内容已截断)

## 涉及话题
- 通义千问
- llama
- DeepSeek
- ai
- OpenAI
- AI

[原文链接](https://www.v2ex.com/t/1206709)
