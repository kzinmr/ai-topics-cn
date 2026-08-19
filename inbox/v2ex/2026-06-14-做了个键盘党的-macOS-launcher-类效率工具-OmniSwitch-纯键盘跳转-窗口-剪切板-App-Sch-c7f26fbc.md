---
title: "做了个键盘党的 macOS launcher 类效率工具 OmniSwitch: 纯键盘跳转, 窗口/剪切板/App Schema Link/脚本执行"
source: v2ex
url: "https://www.v2ex.com/t/1220310"
author: "OrbitTerminus"
date: 2026-06-14
score: 0
tags: ["ai"]
---

# 做了个键盘党的 macOS launcher 类效率工具 OmniSwitch: 纯键盘跳转, 窗口/剪切板/App Schema Link/脚本执行

各位 V2er, 最近自己 vibe coding 做的,macOS 上的一个键盘效率工具 OmniSwitch。一句话:AltTab + Paste + Alfred,装进一个快捷键。

▶︎ 11s 演示,无声循环(点图看视频):https://orbit-terminus.pages.dev/assets/video/hero-loop.mp4
起因很简单:我每天在 ⌘Tab、剪贴板工具、文本片段三个东西之间来回横跳,想把它们收进一个快捷键,而且全程不按回车。
怎么用:
典型场景:

呼出界面-> 按 S -> 直接跳转到 VSCode
呼出界面-> 连续按键 G,1 -> 直接跳转到 Google Chrome 的第一个窗口
呼出界面-> 连续按键 V,1 -> 直接 在当前 Input 区域内 粘贴 剪切板的第一个内容 
呼出界面-> 连续按键 B,1 -> 直接 在当前 Input 区域内 粘贴 某个 ssh root 的密码 
呼出界面-> 连续按键 F,1 -> 直接  跳转到 Slack 的 #某个频道
呼出界面-> 连续按键 A,1 -> 直接  执行 某个 Apple script(比如触发 xcode build) 脚本

机制:

按下全局热键(默认 ⌃⌥W,避开被 Spotlight 占的 ⌘Space;可改成任意组合键,或「双击修饰键」比如双击 ⌘);
第一屏是你所有 App 的网格,每个 App 一个字母键帽;多窗口的 App 用层叠卡片提示;
按 App 字母:单窗口直达;多窗口的话其余 App 退场、动画展开成该 App 的窗口网格,按数字直达。两下键、不用回车、不用在列表里翻。
「 App 字母 + 数字」永远命中同一个窗口,真能形成肌肉记忆,不会因为你激活过谁就漂移。



同一个面板下半部分还有(同屏,不用切工具):


…(内容已截断)

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1220310)
