---
title: "[开源自荐] 下蛋 XiaDown：用 Wails 3 做的一款视频/音频下载 + 在线音乐桌面工具"
source: v2ex
url: "https://www.v2ex.com/t/1209506"
author: "dreamusername"
date: 2026-04-29
score: 2
tags: ["ai"]
---

# [开源自荐] 下蛋 XiaDown：用 Wails 3 做的一款视频/音频下载 + 在线音乐桌面工具

大家好，我是 XiaDown （下蛋）的作者。
之前在 V2EX 看到过 tiny-rdm ，印象挺深。自己平时也写 Go ，一直想找个机会做一款基于 Wails 的桌面工具。后来 Wails 3 慢慢可用了，就用它做了这个项目：下蛋 / XiaDown。
它的定位比较简单：把视频/音频下载、在线音乐播放和本地资源整理放在一个桌面应用里。
项目地址：

GitHub：https://github.com/arnoldhao/xiadown
官网：https://xiadown.dreamapp.cc/

做这个的原因
一开始主要是自己的需求。
找素材、做内容、写代码的时候，经常会遇到两个比较碎的场景：

看到一个视频或音频素材，想先下载下来，最好字幕、封面、元信息也能一起保留。
工作时会放 Lo-Fi 或在线音乐，但不太想在下载工具、浏览器、播放器之间来回切。

所以就做了 XiaDown 。它不是想替代专业剪辑软件，也不是想做成复杂的媒体中心，更像是一个每天可以开在后台的桌面媒体工具。
现在能做什么
主要功能：

基于 yt-dlp 下载视频和音频，支持保存字幕、封面等素材。
下载完成后可以继续转码，并在本地资源库里管理。
可以播放 YouTube Lo-Fi 电台和 YouTube Music 。
支持搜索歌曲、艺人、歌单，播放队列、歌词、封面等基础能力。
喜欢的在线曲目可以继续保存到本地。
支持主题、强调色、侧边栏样式、精灵等个性化外观。
依赖和更新会在应用内维护，尽量减少首次配置成本。

支持平台：

macOS Apple Silicon / Intel
Windows x64 安装版 / 便携版

技术栈
主要是：

Go
Wails 3
React
SQLite
yt-dlp
FFmpeg


…(内容已截断)

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1209506)
