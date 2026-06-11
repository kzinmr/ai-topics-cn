---
title: "[产品自荐] 业余两周做了个 AI Visual Agent，自动选模型、写 prompt、调参数，想请 V 友帮忙看看"
source: v2ex
url: "https://www.v2ex.com/t/1216031"
author: "yestwind"
date: 2026-05-27
score: 0
tags: ["AI", "DeepSeek", "prompt", "ai", "GPT"]
---

# [产品自荐] 业余两周做了个 AI Visual Agent，自动选模型、写 prompt、调参数，想请 V 友帮忙看看

大家好，我是 Orylia 的作者，业余花了大概两周做了一个多模型 AI 图片/视频生成工作台：
https://orylia.ai 
为什么做这个
我自己每天都在用 AI 生图，但每次都要纠结：

用哪个模型？ GPT Image 2 写实强、Seedream 风格化好、Nano Banana 速度快……20 多个模型各有所长
比例、分辨率、quality 怎么选？
prompt 怎么写才能出好图？构图、光影、镜头语言全要自己编
试错一圈积分就烧完了

我想把这个给不懂 AI 的朋友用，但学习成本太高。所以做了一个 Agent 来解决这个问题。
Orylia Agent 做了什么
你用自然语言描述想要的画面（比如"帮我拍一张运动鞋的产品图，大理石桌面，杂志风"），Agent 会：

问 1-2 个澄清问题（风格偏好、用途等）
从 20+ 模型里选最合适的（ GPT Image 2 / Nano Banana Pro / Seedream 4.5 / Midjourney V7 / Seedance 2.0 等）
自动生成专业级 prompt （构图、光影、色温、镜头）
选择最优参数组合（比例、分辨率、quality ），在省积分的前提下保证质量
对结果进行自我评估，给出优化建议

相当于一个懂所有 AI 模型定价和能力的创意总监。
技术栈

Next.js 15 App Router + Vercel
通过 Evolink API 统一调度 20+ 图片/视频模型
6 个 Mentor 人格（不同创意方向的导师）
三阶段积分账本（预扣 → 结算 → 退款），用户永远不会多付
DeepSeek 做 prompt 增强
40+ 一键 AI 工具（去背景、证件照、换脸等）

目前状态
非常早期，自己用 + 朋友在测。免费注册每天有 50 积分，够试大部分功能。

…(内容已截断)

## 涉及话题
- AI
- DeepSeek
- prompt
- ai
- GPT

[原文链接](https://www.v2ex.com/t/1216031)
