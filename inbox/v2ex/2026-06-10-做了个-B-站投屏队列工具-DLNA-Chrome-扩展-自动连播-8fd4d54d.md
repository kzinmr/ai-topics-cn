---
title: "做了个 B 站投屏队列工具(DLNA + Chrome 扩展),自动连播"
source: v2ex
url: "https://www.v2ex.com/t/1219407"
author: "jimsshom2"
date: 2026-06-10
score: 0
tags: ["ai", "AI"]
---

# 做了个 B 站投屏队列工具(DLNA + Chrome 扩展),自动连播

起因
刷 B 站的时候一直有个痛点:投屏只能一个一个投。躺着刷,经常一口气看到好几个想丢电视上看的(纪录片、长视频、合集),但手机一次只能推一个,剩下的只能干等;等当前这个播完,往往就忘了刚才要看哪几个,再翻回去又找不到了。
找了一圈没有顺手的,就自己写了一个,叫 QCast。核心就一件事:给投屏加一个队列,一次把想看的都排进去,一个播完自动播下一个,中途不用碰手机。
是什么

手机 App(Android)维护队列,从 B 站 App 分享视频即可入队

两种投屏端,同一时刻二选一:
电视:走标准 DLNA/UPnP,自动发现局域网渲染器
浏览器:配套的 Chrome 扩展,视频在电脑浏览器里全屏播放


完全免费,纯本地局域网通信,不注册、不上传任何数据

这个项目基本是 vibe coding 做出来的(全程 AI 结对),算是一次完整的"从想法到上架"的实践,体验还挺顺的。
已知限制(先说清楚)

只支持 Bilibili,YouTube 等暂不支持
仅 Android(Flutter 写的,iOS 没精力签名分发)
电视端需要支持标准 DLNA;有些投屏 App(如乐播)默认不开 DLNA,得手动打开,或换当贝/快投屏
DLNA 投屏时,视频流经手机中转给电视,所以投屏期间手机别断网/别杀进程
建议把 QCast 加入电池优化白名单(允许后台运行),否则手机后台一刷新进程,投屏就断了

链接

Chrome 扩展(已上架):https://chromewebstore.google.com/detail/qcast/llggfegahlihjijpcbhegehafpnnacdd
Android APK(GitHub Release):https://github.com/jimsshom/QCast-release/releases/latest

最后

…(内容已截断)

## 涉及话题
- ai
- AI

[原文链接](https://www.v2ex.com/t/1219407)
