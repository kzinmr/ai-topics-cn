---
title: "做了一个给开发者用的 Claude + GPT Image 2 API 入口，想找 V 友小范围试用"
source: v2ex
url: "https://www.v2ex.com/t/1217062"
author: "lei83314"
date: 2026-06-01
score: 0
tags: ["Cursor", "Prompt", "Claude", "GPT", "AI"]
---

# 做了一个给开发者用的 Claude + GPT Image 2 API 入口，想找 V 友小范围试用

大家好，我最近在折腾一个 AI API 入口，叫飞源 API 。
先说明一下，这是推广帖，所以我发在推广节点。

我不想写那种“全网最低”“永不封”“无限并发”的话，主要想找几个真实场景的用户帮忙跑一跑。
我自己平时会用 Cursor 、Claude Code 、Dify ，也会做一些 Telegram Bot 和内容自动化。用下来发现一个问题：不同任务其实不应该都走同一个池子。
比如：
写代码、跑项目、客户交付，最好走稳定一点的 Claude 官 key 。
批量改写、草稿、日常低敏任务，很多时候没必要上最贵的，可以走 Claude 经济池。
做封面、海报、Bot 出图、营销素材，就应该直接接出图 API 。
所以我现在把飞源拆成三块：


Claude 官 key

适合 Cursor 、Claude Code 、Dify 、客户项目、长上下文任务。主打稳定、usage 可查、支持 Prompt Cache ，不做网页订阅号反代。


Claude 经济池

适合草稿、批量改写、日常问答、低敏任务。它的定位就是省成本，我不会把它包装成官 key ，也不建议拿它跑核心交付。


GPT Image 2 出图

现在先做低清和标清两档。低清适合批量试图、封面草稿、广告测试；标清适合产品海报、朋友圈图、客户交付素材。


简单说就是：
重要任务走官 key ，

低成本跑量走经济池，

要做图就走出图 API 。
目前比较想找这几类人测试：

Cursor / Claude Code 用户
Dify / Coze / n8n 工作流用户
做 Bot 、工具站、出图站的人
做内容营销，需要批量生成封面、海报、配图的人
想用 Claude API ，但不想折腾海外卡和充值的人

不太适合：

只想找最低价
要无限并发
要把经济池当官 key 用
要保证每张图都是高清 4K


…(内容已截断)

## 涉及话题
- Cursor
- Prompt
- Claude
- GPT
- AI

[原文链接](https://www.v2ex.com/t/1217062)
