---
title: "周末项目： 303 期 Lenny's Podcast → 中文翻译 + AI 摘要 + 思维导图"
source: v2ex
url: "https://www.v2ex.com/t/1209663"
author: "xiajingsi00"
date: 2026-04-30
score: 1
tags: ["Ai", "AI", "DeepSeek", "OpenAI"]
---

# 周末项目： 303 期 Lenny's Podcast → 中文翻译 + AI 摘要 + 思维导图

Lenny's Podcast 是产品经理/产品领域较有影响力的播客之一，主持人 Lenny Rachitsky 邀请过 Brian Chesky （ Airbnb CEO ）、Marty Cagan 、Kevin Weil （ OpenAI CPO ）、Shreyas Doshi 等一线产品人进行深度访谈。
但存在几个痛点：

全英文内容，无字幕版本的 YouTube / Apple Podcasts 理解成本较高
单期时长 60-90 分钟，定位特定观点需要手动快进
中文圈现有几个 GitHub 仓库属于档案型（双语稿堆叠），检索不便

因此我搭建了 https://t.gotofuse.com/
主要功能：

抓取全部 303 期文字稿（ fork 自 Lenny 官方仓库）
调用 DeepSeek API 进行逐句中文翻译，附带说话人标识和时间戳的对照译文
每期自动生成 AI 摘要、思维导图、金句卡片
跨期聚合了「话题级方法论文档」（如「产品管理」聚合了 15 期相关访谈的核心观点）
支持全文搜索（基于 fuse.js ），可按嘉宾、公司、话题筛选
自动同步最新播客

完全免费，无付费墙、无广告、无需注册，欢迎反馈。

## 涉及话题
- Ai
- AI
- DeepSeek
- OpenAI

[原文链接](https://www.v2ex.com/t/1209663)
