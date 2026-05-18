---
title: "做了一个把电商/门店需求转成 Image2 广告图 Prompt 的小工具，求各位大佬指点"
source: v2ex
url: "https://www.v2ex.com/t/1210320"
author: "kwistzzqq"
date: 2026-05-05
score: 0
tags: ["AI", "Prompt", "OpenAI"]
---

# 做了一个把电商/门店需求转成 Image2 广告图 Prompt 的小工具，求各位大佬指点

最近又把之前的小项目更新了一版，叫 Image2 Ads Studio 。
GitHub：
https://github.com/kwistzzqq-byte/image2-ads-studio
它不是一个 Prompt 合集，也不是一个完整的 AI 画图网站。
更准确地说，它是一个面向广告作图的 Prompt Agent：用 OpenAI 把用户很口语化的商业需求，整理成更适合 Image2 / 生图工具使用的广告图 Prompt 。
我最近在试 AI 广告图、电商主图、门店宣传图的时候，发现一个现实问题：很多人其实会把需求描述成生图模型能稳定理解的 Prompt 。
比如客户通常会说：
“帮我做一张奶茶店海报。”
“门店活动要发朋友圈。”
“上传这张门店图，把招牌改一下。”
这些话人能懂，但直接丢给生图模型，经常会缺很多关键条件：行业、尺寸、构图、产品位置、材质、光线、背景、文字层级、参考图到底是保留结构还是只参考风格等等。
所以我做了这个工具。
现在的流程大概是：
输入一句商业需求
→ 解析用途、行业、输入方式
→ 匹配广告业务模板
→ 匹配视觉配方
→ 用 OpenAI 重新组织 Prompt
→ 输出给 Image2 或其他生图工具测试
这次主要更新了双语版本：
GitHub README 有英文和中文入口
Web UI 支持中文 / English 切换
输出 Prompt 也可以按中文或英文生成
每个案例都是“一张图 + 一份中文 Prompt + 一份英文 Prompt”
目前开源版主要覆盖这些方向：
电商主图、产品广告图、品牌海报、门店宣传图、门头店招、易拉宝、活动背景板、标识导视、形象墙、本地商家促销图、商业摄影风格图。

…(内容已截断)

## 涉及话题
- AI
- Prompt
- OpenAI

[原文链接](https://www.v2ex.com/t/1210320)
