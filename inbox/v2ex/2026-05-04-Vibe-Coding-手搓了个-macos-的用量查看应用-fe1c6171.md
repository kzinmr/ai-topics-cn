---
title: "Vibe Coding 手搓了个 macos 的用量查看应用"
source: v2ex
url: "https://www.v2ex.com/t/1210246"
author: "zivn"
date: 2026-05-04
score: 1
tags: ["AI", "DeepSeek"]
---

# Vibe Coding 手搓了个 macos 的用量查看应用

平时用 codex 和 cc + glm ，订阅了一堆服务，每天都要到各个网站查看很多次用量。

于是干脆手搓了一个 UsageBoard App ，用来查看所有订阅的用量。
目前支持 Codex 、智谱（ ZAI ）、DeepSeek 、MiniMax 、Tavily ，全部基于官方 API 。

其中 Codex 和智谱支持查看 token 用量统计图表，智谱用的官方 API ，Codex 基于本地会话分析。
功能特性

菜单栏常驻，点击图标打开快速预览。
支持分组展示和标签页展示。
支持手动刷新、定时刷新、单卡片刷新、退出按钮。
插件化用量查询，插件可独立配置刷新间隔和参数。
插件图标支持，从元数据配置加载远程图片并缓存。
订阅级别徽章显示（黑底白字圆角标签）。
插件设置界面从脚本元数据自动生成参数表单。
新增插件默认不启用，启用前会检查必填参数。
插件数据按 stateID 缓存到磁盘，启动后可展示上次成功数据。
首次启动会把内置插件安装到用户插件目录。
设置页支持开机启动、插件拖拽排序、插件帮助文档、检查更新和在线更新。
用量展示支持百分比或数字占比，支持重置时间、进度条颜色和可选 token 统计图。

插件
App 是个显示器和调度器，所有的用量信息通过插件来定时获取。

插件可以自由扩展，让 cc 读一下插件开发文档然后开始自己搓就行。  






github 地址： https://github.com/marsmay/UsageBoard

MIT 协议，随便 fork 随便 DIY 。

Token 和时间都花了不少，开发不易，求大佬们给加小星星。

## 涉及话题
- AI
- DeepSeek

[原文链接](https://www.v2ex.com/t/1210246)
