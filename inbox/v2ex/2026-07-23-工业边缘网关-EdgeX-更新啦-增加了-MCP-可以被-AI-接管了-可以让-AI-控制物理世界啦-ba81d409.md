---
title: "[工业边缘网关] EdgeX 更新啦，增加了 MCP，可以被 AI 接管了，可以让 AI 控制物理世界啦"
source: v2ex
url: "https://www.v2ex.com/t/1229421"
author: "anviod"
date: 2026-07-23
score: 0
tags: ["AI", "Cursor", "Claude", "mcp", "MCP"]
---

# [工业边缘网关] EdgeX 更新啦，增加了 MCP，可以被 AI 接管了，可以让 AI 控制物理世界啦

原本只是想体验一下 MCP ，结果越折腾越觉得，这东西和工业现场还挺搭
做工业项目这么多年，感觉最耗时间的从来不是写代码。
而是翻协议文档、整理寄存器、配点位、抓报文、调设备。
很多事情每个项目都要重新来一遍，而且不少都是重复劳动。
所以最近一直在想，如果 AI 真有价值，那它是不是应该直接接触现场设备，而不是只负责聊天。于是就把 MCP 接到了 EdgeX 。
现在支持 MCP 的客户端（ Claude 、Cursor; 各种 AI Studio 等），已经可以直接连接 EdgeX ，调用网关能力。
目前已经实现 MCP 的能力：

自动创建采集全流程
边缘计算规则策略部署和调试
AI 诊断和巡检
AI 辅助设备接入测试

另外，之前做的一些 AI 协同能力也逐步整合进来了：

协议文档解析
Excel 点表识别
寄存器整理
采集配置生成
通信报文分析
设备接入辅助

我现在越来越觉得，AI 在工业现场最有价值的地方，不是聊天，而是帮现场实施的人少做重复工作。
比如上传一份厂家协议文档，或者抓一段通信报文，AI 就能帮助整理点表、生成配置，再通过 MCP 直接读取设备验证结果。
这样接一个新设备，可能就不用再从零开始折腾了。
MCP 接入文档：
https://anviod.github.io/edgex/guide/mcp-access-guide
AI 协同组件说明：
https://github.com/anviod/edgex/blob/dev/docs/TODO/AI%E5%8D%8F%E5%90%8C%E7%BB%84%E4%BB%B6%E8%A7%84%E5%88%92.md
官网：
https://anviod.github.io/edgex/

…(内容已截断)

## 涉及话题
- AI
- Cursor
- Claude
- mcp
- MCP

[原文链接](https://www.v2ex.com/t/1229421)
