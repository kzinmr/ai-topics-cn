---
title: "记录一次 Android 14 + coturn 下 WebRTC 通话 30 秒后断开的排查"
source: v2ex
url: "https://www.v2ex.com/t/1214939"
author: "snowlyg"
date: 2026-05-23
score: 0
tags: ["ai", "AI"]
---

# 记录一次 Android 14 + coturn 下 WebRTC 通话 30 秒后断开的排查

最近整理了一次 WebRTC 问题排查，脱敏后记录一下。

背景是一个 Android WebRTC 音视频通话场景。原来主要在内部网络使用，后续为了支持更复杂的网络边界，引入了 `coturn` 做 TURN 中继。

问题现象：

- Android 14 设备和旧版 Android 设备通话时，Android 14 端经常在 30-60 秒内自动退出。
- 旧版 Android 设备基本正常。
- 少数情况下双方也能持续正常通话。
- 强制走 TURN relay 后更容易稳定复现。

一开始日志里有一条本地地址相关的中继协商 timeout ，而且经常出现在断开前后，所以很容易误判为根因。

后面看 WebRTC 状态变化，真正关键的是：

```text
IceConnectionChange -> DISCONNECTED / FAILED
StandardizedIceConnectionChange -> DISCONNECTED / FAILED
```

排查过程大概是：

1. 先统一链路，强制走 `coturn`，避免内部网络直连把问题掩盖掉。
2. 替换过 WebRTC 依赖版本，排除单纯的 SDK 版本问题。
3. 扩大设备矩阵，问题逐渐收敛到 Android 14 设备。
4. 回到 TURN 服务侧检查证书、安全参数和端口开放。
5. 调整 `coturn` 相关配置后，同样测试矩阵下不再出现 30-60 秒自动断开。

这次最大的教训是：WebRTC 问题不要只盯某一条高频日志。更可靠的路径是先看 ICE 状态机、candidate pair 、当前到底走的是直连还是 relay 。

另外，直连和中继混在一起测，很容易让问题看起来像“网络随机抖动”。强制走 relay 后，问题才变成可复现、可分析。


…(内容已截断)

## 涉及话题
- ai
- AI

[原文链接](https://www.v2ex.com/t/1214939)
