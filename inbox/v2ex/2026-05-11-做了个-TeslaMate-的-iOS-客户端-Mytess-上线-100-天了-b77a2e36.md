---
title: "做了个 TeslaMate 的 iOS 客户端 Mytess，上线 100 天了"
source: v2ex
url: "https://www.v2ex.com/t/1211921"
author: "yekk"
date: 2026-05-11
score: 5
tags: ["Claude", "AI"]
---

# 做了个 TeslaMate 的 iOS 客户端 Mytess，上线 100 天了

利益相关：我是 mytess 作者。
2 月初上架了一个 TeslaMate 的 iOS 客户端，叫 mytess 。到现在差不多 100 天，从 1.0 更到了 1.5 ，想简单记录一下。
App Store： https://apps.apple.com/app/id6757828502

官网： https://www.mytess.net/zh
先说定位：

它不是 Tesla 官方 App 的替代品，也不做车辆控制。它只是连接你自己部署的 TeslaMate ，把里面的用车数据用原生 iOS App 的方式展示出来。
如果你没跑 TeslaMate ，那这个 App 基本没用；如果你已经在 NAS / 小主机 / VPS 上跑了 TeslaMate ，可能会比较对口。
为什么做
我自己用 TeslaMate 时最大的感受是：数据都有，但手机上看不舒服。
Grafana 很强，但它更像后台面板。

我想要的是一个平时会打开的 App：

看这趟开得怎么样
看最近充电花了多少钱
看电池容量有没有明显变化
看一年里都去了哪些地方
偶尔能生成一张还算好看的分享图

所以 mytess 基本就是围绕这些点做的。

这 100 天主要做了什么
1.1：成就、更新记录、小组件
1.1 做了一些“让数据有记忆点”的东西。
比如成就系统，会根据 TeslaMate 里的历史数据解锁一些徽章。

还有车辆软件版本记录，可以从首页点车机版本进去，看每个版本用了多久、期间跑了多少。
另外也重做了一些小组件和路线分享。

1.2：Trips
TeslaMate 的原始数据是一段一段 drive 。

但真实用车里，一次出行经常是多段驾驶、几次充电、一些停留点。
所以 1.2 做了 Trips：

可以把多段驾驶整理成一次旅途，支持途径点、照片、天气和路线分享。

…(内容已截断)

## 涉及话题
- Claude
- AI

[原文链接](https://www.v2ex.com/t/1211921)
