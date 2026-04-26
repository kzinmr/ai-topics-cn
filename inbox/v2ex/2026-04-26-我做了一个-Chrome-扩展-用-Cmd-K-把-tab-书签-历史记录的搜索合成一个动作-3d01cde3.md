---
title: "我做了一个 Chrome 扩展，用 Cmd+K 把 tab、书签、历史记录的搜索合成一个动作"
source: v2ex
url: "https://www.v2ex.com/t/1208687"
author: "Tuy"
date: 2026-04-26
score: 0
tags: ["ai"]
---

# 我做了一个 Chrome 扩展，用 Cmd+K 把 tab、书签、历史记录的搜索合成一个动作

起因是我用了飞书的 Cmd+K 之后发现我切任何一个 app 都想用这个快捷键，然后发现 chrome 这么大的一个浏览器竟然没有这个功能,遂起意做一个插件,目前更新到了 1.4.4,我自己用了几个月了,目前可以说非常顺手,主要涵盖了四个场景：

找已经打开的 tab ？翻窗口
找书签？打开书签菜单翻
找历史记录？打开历史记录页搜
搜新内容？先开一个新 tab

下面是比较官方的介绍
于是做了 Pounce：在任意页面按 Cmd+K （ Windows 是
Alt+K ），弹出一个搜索框，同时模糊匹配所有打开的
tab 、书签、历史记录和常用网站。方向键选，Enter 跳转，Esc 关闭。
技术栈：Fuse.js 客户端模糊搜索 + 自定义评分（权重：open tabs > history > bookmarks >
top sites ），Manifest V3 ，纯本地无网络请求。
GitHub （ MIT ）： https://github.com/TuYv/pounce
Chrome Web Store： https://chromewebstore.google.com/detail/pounce-%E2%80%93-cmd+k-search-tab/clgpmlhecjlekgipngaopglbfdkonjdf
用了几个月了，现在离不开了。欢迎试用，有想法直接说。

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1208687)
