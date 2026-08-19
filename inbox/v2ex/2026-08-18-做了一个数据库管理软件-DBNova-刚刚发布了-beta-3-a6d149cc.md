---
title: "做了一个数据库管理软件 DBNova，刚刚发布了 beta.3"
source: v2ex
url: "https://www.v2ex.com/t/1235432"
author: "suruiran"
date: 2026-08-18
score: 0
tags: ["ai"]
---

# 做了一个数据库管理软件 DBNova，刚刚发布了 beta.3

支持多种 SQL 数据库，以及 MongoDB 和 Redis 。


目前支持 Windows.x64 、Linux.x64 和 Macos.Arm64 。


对 SQL 语法和注释做了一点点扩展，可以实现 SQL 的参数化复用。文档


如果你可以使用 Typescript 的话，就更好了。DBNova 不仅可以通过 ts 和数据库交互，还可以将数据库的
结构生成 d.ts，然后注入到 Monaco Editor 中。SQL Builder 也是自己实现的，github
aghsorm。


基于 Wails 构建，尽管安装包不大，执行的时候还是需要依赖系统的 webkit 。但是基于
我在虚拟机中的测试，够用。设置中也可以禁用全部的 CSS 特效……


目前没有什么需要付费解锁的功能，设想中的需要付费解锁的功能只有一个，就是单个数据库
可以打开单独的窗口。但是这个功能我想要等 Wails3 正式发布在开始做。所以也没什么激活码好
送的。（感谢 Cloudflare 和 Oracle ，我几乎没有什么成本。）


下载地址
文档地址
欢迎体验和反馈……😉

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1235432)
