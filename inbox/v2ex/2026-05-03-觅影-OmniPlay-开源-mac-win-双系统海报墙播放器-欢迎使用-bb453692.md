---
title: "觅影 OmniPlay-开源 mac、win 双系统海报墙播放器，欢迎使用"
source: v2ex
url: "https://www.v2ex.com/t/1210090"
author: "nandie"
date: 2026-05-03
score: 0
tags: ["ai", "AI"]
---

# 觅影 OmniPlay-开源 mac、win 双系统海报墙播放器，欢迎使用

觅影 OmniPlay
觅影 OmniPlay 是一款原生开发的海报墙播放器，支持 mac 、win 双系统。mac 采用 swift 开发，win 采用 C# + .net + Avalonia UI 。底层播放器核心为 MPVKit-GPL / libmpv / FFmpeg 相关组件。ios 版正在开发中。
软件截图


功能特色
UI

UI 简洁且美观，海报墙没有做过多的分类功能，只有搜索、排序功能。

海报墙媒体库

支持海报墙和分集剧照
采用 TMDB 刮削，增加了更宽松的刮削规则和自定义编辑功能。避免重命名和硬链接。

媒体源管理

支持添加本地文件夹、WebDAV 、SMB 。mac 版因为开发一直有 bug ，不支持 SMB 直连，请在访达中挂载 SMB ，再在软件中添加本地文件夹，间接连接 SMB 。可以将访达挂载的 SMB 添加到开机自启
不需要将电影、剧集分不同文件夹进行挂载，软件自动识别。

自动扫描与刮削

支持公共 TMDB 源，也支持自定义 TMDB API Key / v4 Token 。公共源 API 做了限制，建议注册 TMDB 后获取 API 。如果 TMDB api 连通测试失败，请挂代理或改 host 。

github 仓库地址

见我的博客： https://blog.nandielinghai.de ，还有 AI 中转站地址也在博客，有需要也可以支持下。

## 涉及话题
- ai
- AI

[原文链接](https://www.v2ex.com/t/1210090)
