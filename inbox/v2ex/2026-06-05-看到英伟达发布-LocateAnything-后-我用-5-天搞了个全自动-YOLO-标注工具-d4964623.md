---
title: "看到英伟达发布 LocateAnything 后，我用 5 天搞了个全自动 YOLO 标注工具"
source: v2ex
url: "https://www.v2ex.com/t/1218331"
author: "Somnusochi"
date: 2026-06-05
score: 1
tags: ["大模型", "AI"]
---

# 看到英伟达发布 LocateAnything 后，我用 5 天搞了个全自动 YOLO 标注工具

分享个自己最近开源的项目：VLM-AutoYOLO。
项目地址： https://github.com/Somnusochi/VLM-AutoYOLO
前几天看到英伟达（ NVIDIA ）正式公布了 LocateAnything 视觉大模型，它那种用一段文本就能直接定位物体的能力让我觉得很有意思。结合 Facebook 最近开源的 SAM2 抠图模型，我就想：完全可以用一句话代替手工画框，实现自动化的 YOLO 数据集标注。
有了想法后，我在 AI 的辅助下大概花了 5 天时间，把这套全自动标注的流水线跑通了。
它是怎么工作的？
逻辑很简单，主要分三步：

一句话找目标：输入你想找的东西（比如“有划痕的零件”），后端的 LocateAnything 模型会先找出它的大致位置。
像素级抠图：把大概坐标扔给 SAM2 模型，由它负责精准吸附边缘，生成 Bounding Box 和 Mask 。
一键导出：流水线跑完后，自动打包成标准的 YOLO 数据集格式，可以直接丢给 YOLOv8/v11 去训轻量级模型。

技术实现细节
为了保证业务数据不上云，这个项目设计成了 100% 纯本地运行。这就需要处理显存压力的问题。

**后端 (FastAPI / PyTorch)**：
为了能在普通开发机上跑这套 30 亿参数的大模型，我在后端写了严格的显存清理机制。在我的 MacBook Pro (M4 Pro, 24GB) 上，开启 Apple MPS 加速后，处理一张高清图大概 4 秒。连续跑几百张图，系统内存占用稳在 12GB 左右，没有内存泄露，挂后台跑很稳。
**前端 (React / Vite / UnoCSS)**：
我个人不喜欢传统标注软件那种密密麻麻的控制台界面，所以用 UnoCSS 写了个极简风格的操作界面，用起来稍微顺眼点。

目前的坑

…(内容已截断)

## 涉及话题
- 大模型
- AI

[原文链接](https://www.v2ex.com/t/1218331)
