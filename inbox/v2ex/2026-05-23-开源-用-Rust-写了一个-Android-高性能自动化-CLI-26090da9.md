---
title: "[开源] 用 Rust 写了一个 Android 高性能自动化 CLI"
source: v2ex
url: "https://www.v2ex.com/t/1214989"
author: "prasanta"
date: 2026-05-23
score: 0
tags: ["LLM", "ai"]
---

# [开源] 用 Rust 写了一个 Android 高性能自动化 CLI

handsets —— 用 Rust 写的 Android 高性能自动化 CLI 。
设计

客户端 Rust 单二进制
daemon 是一个 ~几百 KB 的 jar ，通过 adb forward 跑在设备 shell UID 下，无需 root 也无需装 APK
通信走长度前缀的二进制帧

性能




handsets
adb shell
uiautomator2
Appium




单次调用延迟
2-7ms
40-700ms
30-100ms
100-500ms

adb shell input tap 之所以慢且不稳定，是因为它走 injectInputEvent(ev, sync=true)，sync 模式会阻塞到 InputDispatcher 处理完事件 —— 当 UI 线程在做动画或 layout
的时候，sync 排在队尾等。实测最长 tap 尖峰 2.3 秒。
handsets 默认走 AccessibilityNodeInfo.ACTION_CLICK，绕开 InputDispatcher ，直接触发 widget 的 OnClickListener ，p99 ~50ms 。OnTouchListener-only 的自定义 View 会
fallback 到 gesture path 。
hs ui 的输出格式
不是 XML accessibility dump ，而是 verb-led 表格：
  tap   ImageButton  "返回"   #back_btn   98,243
  fill  EditText     "邮箱"   #email_et   540,540
  fill  EditText     "密码"   #pwd_et     540,640  [password]

…(内容已截断)

## 涉及话题
- LLM
- ai

[原文链接](https://www.v2ex.com/t/1214989)
