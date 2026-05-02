---
title: "开源了一个面向 Image2 广告作图的 Prompt Agent： Image2 Ads Studio"
source: v2ex
url: "https://www.v2ex.com/t/1210038"
author: "kwistzzqq"
date: 2026-05-02
score: 0
tags: ["Prompt", "LLM", "ai", "prompt"]
---

# 开源了一个面向 Image2 广告作图的 Prompt Agent： Image2 Ads Studio

它的定位不是“提示词合集”，而是一个面向广告作图场景的 Prompt Agent：把业务 brief 、行业、文案、画幅、参考图用途这些信息，整理成更稳定、更可执行的 Image2 测试提示词。

我做这个的背景是：广告作图里直接对白话需求生图，结果经常会比较飘；而网上很多 prompt 案例又是一次性的，难以迁移到真实客户需求里。所以我把流程拆成了几层：

Brief -> 意图解析 -> 广告业务模板 -> 视觉配方 -> LLM Prompt Brain -> 确定性检查 -> optimized prompt

当前社区版包含：

- 本地 Web 工作台
- 120 条广告业务模板
- 75 条视觉配方
- 50 个一图一 prompt 的 gallery case
- 参考图策略
- 确定性 prompt 校验
- 手动 Image2 测试流程

现在它还不直接调用生图 API ，只做 prompt planning layer 。也就是说，工具输出 optimized prompt ，用户再手动复制到 Image2 测试。后续真实生图 adapter 、批量案例、ERP/生产系统集成会单独往后放。

和普通 prompt 仓库的区别，我自己理解主要有三点：

1. 输入不是“复制一条酷 prompt”，而是业务需求、行业、文案和参考图。
2. 模板不是只记录画面描述，而是带 task type 、use case 、材质/构图/文字层级/负面约束。
3. 最终 prompt 会做确定性检查，尽量把“高级感、网红风、类似某某”这类词改成可执行的构图、色彩、灯光、材质和排版规则。

GitHub：
https://github.com/kwistzzqq-byte/image2-ads-studio

Gallery：

…(内容已截断)

## 涉及话题
- Prompt
- LLM
- ai
- prompt

[原文链接](https://www.v2ex.com/t/1210038)
