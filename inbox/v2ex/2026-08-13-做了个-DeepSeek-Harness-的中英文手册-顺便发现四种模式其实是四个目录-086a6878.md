---
title: "做了个 DeepSeek Harness 的中英文手册，顺便发现四种模式其实是四个目录"
source: v2ex
url: "https://www.v2ex.com/t/1234238"
author: "zanearrives"
date: 2026-08-13
score: 2
tags: ["DeepSeek"]
---

# 做了个 DeepSeek Harness 的中英文手册，顺便发现四种模式其实是四个目录

DeepSeek Harness 发布后翻了几天源码，发现中文圈转述的一些说法和实际对不上，索性整理成了站： https://dshkit.dev （中英双语，48 篇）
几个和外面传的不一样的地方：
四种模式不是代码分支，是 apps/cli/config/agent-presets/ 下的四个目录——standard / code / minimal / cordis ，各自一个 agent.cordis.yml + 一个 preset.yml 。切模式 = 会话指定跑哪个 preset 。
PTC 不是社区外号，是官方中文名。 code/preset.yml 里写着 name: PTC 模式。四个的官方中文名是标准模式 / PTC 模式 / 极简模式 / 创造模式，英文文档那边叫 Code mode 。
minimal 的 persona 带 complete: true——人设即完整系统提示词，后面所有装配监听器都插不进文本了。「极简」是靠少组装几行做出来的，不是靠关一堆开关。
站里每条技术论断都标了源码路径，文档没写的地方我直接写「文档未覆盖」，没有猜的成分。
有人自己写过 preset 吗？ isolate: 那块我只读了 README 没跑通——按说明，引用了发布进程全局服务的行会在挂载时被拒，得用 entry-local 领域包一层。

## 涉及话题
- DeepSeek

[原文链接](https://www.v2ex.com/t/1234238)
