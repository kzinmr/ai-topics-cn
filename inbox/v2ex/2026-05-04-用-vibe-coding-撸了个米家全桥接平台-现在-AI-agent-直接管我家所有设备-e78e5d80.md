---
title: "用 vibe coding 撸了个米家全桥接平台，现在 AI agent 直接管我家所有设备"
source: v2ex
url: "https://www.v2ex.com/t/1210247"
author: "handsomejustin80"
date: 2026-05-04
score: 0
tags: ["MCP", "AI agent", "Claude", "AI"]
---

# 用 vibe coding 撸了个米家全桥接平台，现在 AI agent 直接管我家所有设备

折腾智能家居有段时间了，米家生态的东西越买越多，但说实话小米官方那套自动化能做的事太有限。尤其是最近上手了 Claude Code 之后，就一直在想——能不能让 AI 直接操作我家的设备？
于是就搞了个玩意出来。
核心思路很简单：给米家设备套一层 REST API + MCP 协议，这样不管是 CLI 还是各种 AI agent 都能直接调。
现在我家的情况大概是这样：
命令行控设备
mijia-control device list
mijia-control device set <did> power on
mijia-control scene execute "回家模式"
躺床上不想拿手机的时候 SSH 进去敲两行命令，比打开米家 app 翻半天快多了。
AI agent 直接接管
这是我觉得最有意思的部分。项目内置了 MCP Server ，配好之后 Claude Code 、Hermes Agent 、OpenClaw 这类 agent 可以直接作为智能家居的控制层。比如我跟 Claude 说"把书房灯调到 40% 暖光"，它就直接调 API 去执行了，不用我写任何中间层。
前两天试了下用 Hermes Agent 做了个自动化：温湿度传感器超过阈值 → 自动开空调 → 等温度降下来再关。整个过程用自然语言描述规则就行，agent 自己去查设备、调接口。
HomeKit 桥接
这个是顺手做的，但用下来体验很好。通过 HAP-Python 把米家设备桥接到 Apple 家庭里，Siri 就能直接控制了。"嘿 Siri ，关灯"终于不用再买 HomeBridge 插件折腾了。灯光、插座、温控器、传感器都支持。
其他零碎的

SocketIO 实时推送设备状态变更
能耗统计仪表板，看哪个设备费电
BLE 直连温湿度计，不走云端，延迟低很多

…(内容已截断)

## 涉及话题
- MCP
- AI agent
- Claude
- AI

[原文链接](https://www.v2ex.com/t/1210247)
