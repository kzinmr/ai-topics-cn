---
title: "vibe 了一个基于 cdp,聚合自己知乎/B 站/推特账号的推荐和关注流的 web 应用,开源."
source: v2ex
url: "https://www.v2ex.com/t/1219487"
author: "oaa"
date: 2026-06-10
score: 0
tags: ["ai"]
---

# vibe 了一个基于 cdp,聚合自己知乎/B 站/推特账号的推荐和关注流的 web 应用,开源.

https://github.com/woodgear/refresh
Refresh
Refresh 是一个自托管的个人账号 feed API：用你自己的浏览器登录态，把 X/Twitter 、知乎、B 站推给你的内容采集成结构化资源，再通过网页、RSS 和 JSON API 消费。
它不是多用户托管服务，也不内置第三方账号凭据。登录态、抓取到的内容、媒体缓存和日志都属于本机运行态数据，不提交到仓库。
它做什么

通过 Chrome DevTools Protocol 操控一个独立的 Chrome profile 。

使用你自己的登录态抓取平台推荐流：
X/Twitter home timeline GraphQL 响应
知乎 topstory / moments API
B 站动态流 / 热门 API


每次抓取保存为不可变的 RefreshWindow 档案。
将内容归一化为 Message / Author / Account 等 k8s 风格资源。
提供 React 阅读界面：按源过滤、未读追踪、登录恢复、手动刷新。
提供 RSS：/rss/<source>.xml 和 /rss/all.xml。
图片会本地化到 data/media，方便 RSS 阅读器稳定回源。

隐私边界
仓库只放应用代码。以下运行态路径已被 git 忽略：

profiles/：Chrome profile 、cookies 、登录态
data/：抓取内容、媒体、overlay 、调度器状态、日志
.env / .env.*：本地部署配置

公开仓库前不要把运行态目录、截图、导出的 cookie 、本地环境变量文件或真实数据样例提交进来。
本地运行
依赖：

Bun
pnpm
Chrome / Chromium
jq、xmllint（用于 verify.sh）

启动：

…(内容已截断)

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1219487)
