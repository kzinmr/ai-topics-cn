---
title: "Google I/O 快开了，分享一个 Veo Omni AI 视频生成站"
source: v2ex
url: "https://www.v2ex.com/t/1213840"
author: "bibohaha"
date: 2026-05-19
score: 0
tags: ["prompt", "AI", "Gemini"]
---

# Google I/O 快开了，分享一个 Veo Omni AI 视频生成站

北京时间 5 月 20 日凌晨 1 点是 Google I/O ，估计今年还是 Gemini / Veo 相关更新比较多。
我最近做了一个 AI 视频生成网站：Veo Omni。
现在支持：

Text to video
Image to video
Video edit
文件上传
异步任务轮询
生成结果链接查看

做这个项目主要是想把视频生成的几个常见流程封装一下。底层模型一般都是异步任务，输入里又经常混着 prompt 、图片、视频、音频，直接接 API 的话前后处理比较烦。
目前 Veo Omni 做的事情比较简单：

用户上传文件
文件先传到对象存储
后端把公网 URL 和 prompt 组装成模型参数
提交视频生成任务
轮询任务状态
返回生成结果

这次 Google I/O 我比较好奇 Veo 会不会继续往可编辑方向走。单纯 text to video 其实不太够用，开发者更需要的是稳定的工作流：参考图、源视频、局部修改、镜头续写、失败重试、任务队列、结果管理。
我自己做下来感觉，AI video generator 这类产品难点不只是在模型调用，更多是在这些工程细节：

文件上传和公网访问
异步任务状态同步
失败状态处理
参数兼容
成本和额度控制
用户历史记录

## 涉及话题
- prompt
- AI
- Gemini

[原文链接](https://www.v2ex.com/t/1213840)
