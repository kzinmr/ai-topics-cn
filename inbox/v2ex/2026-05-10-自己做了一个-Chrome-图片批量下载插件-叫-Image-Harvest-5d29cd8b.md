---
title: "自己做了一个 Chrome 图片批量下载插件，叫 Image Harvest 🌾"
source: v2ex
url: "https://www.v2ex.com/t/1211632"
author: "coderkyriewen"
date: 2026-05-10
score: 0
tags: ["ai"]
---

# 自己做了一个 Chrome 图片批量下载插件，叫 Image Harvest 🌾

独立开发的 Chrome 插件
做这个的起因是：市面上的图片下载器要么漏图（ CSS 背景图、iframe 里的图直接无视），要么往你电脑上塞广告追踪，要么界面像上个世纪的。我想做一个「真正能扒干净所有图片」的工具，同时隐私零负担。
🔍  [深度提取，一张不漏]
不只是扒  标签，CSS background-image 、<picture>/<source>、懒加载图、Shadow DOM 、同源 iframe 里的图片——全部提取出来。单次最多 1000 张。
📦  [筛选 + 批量 ZIP 下载]
按尺寸（自定义范围）、格式（ JPG/PNG/WebP/SVG 等 9 种）、布局（横/竖/方/全景）筛选。选中之后一键打包成 ZIP 下载，不用一张张右键保存了。
🎨  [还有这些好玩的] 

每张图自动提取 Top 5 主色调色板
反向搜图：右键 Google + TinEye 直达（免费）
侧边栏 / 弹窗双模式，深色 / 浅色 / 跟随系统主题
点击图片直接在网页上高亮定位

🛡️  [隐私优先]
零追踪、零远程代码、零数据上传。所有处理 100% 在你本地完成。源码 GitHub 开源，MIT 协议，欢迎审计。
💎  [ Pro 高级功能]
免费版已经覆盖了日常 80% 的场景。如果你是重度用户，Pro 解锁：

多标签页同时批量提取
pHash 相似图检测去重
格式转换（ PNG ↔ JPG ↔ WebP ）
图片收藏夹（本地存储）
自定义文件命名模板（ 12 种占位符）
Baidu + Yandex 反向搜图

🛒 Chrome 商店安装： https://chromewebstore.google.com/detail/iecgnjidmogebokcfnejncgnelcepffo

…(内容已截断)

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1211632)
