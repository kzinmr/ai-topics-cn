---
title: "原来 Anthropic 才是最正义的公司"
source: v2ex
url: "https://www.v2ex.com/t/1241357"
author: "Rorysky"
date: 2026-09-11
score: 19
tags: ["OpenAI", "DeepSeek", "Anthropic", "Kimi", "AI", "Qwen", "Claude"]
---

# 原来 Anthropic 才是最正义的公司

看这个报告，A 社太苦了！ 理解 Dario 的一天
这些人为什么这么坏呀！还有涉及组织化网络攻防的信息，太敏感不说了
https://x.com/AnthropicAI/status/2098097512544444447

- 阿里：体量最大。高峰一天抽近 300 万条，3500 多个假号，整段归因超 1.51 亿，专扒 Opus 4.6/4.7 的思考过程去喂 Qwen 3.5/3.6/3.7 。
- 月之暗面：用户请求悄悄转给 Claude ，再把回复当成 Kimi 吐回去。10 天转了近 30 万条，整段归因超 2300 万。还绕过 thinking signature ，把思考过程抠出来训自己的模型。
- DeepSeek：同一套。14 天超 1210 万条。专门把走 Claude Code / OpenCode 的用户请求转去 Opus 。
- 智谱：把偷来的 Claude 思考过程再喂回 Claude 洗干净，好拿去训自家 GLM 。10 天 273 个假号专抽 Opus 4.8 ，光清洗就 77 万条，17 天总共归因 340 万条，还拿 Claude 当裁判给训练数据打分。GLM 5.3 发布前，用公开漏洞集出 CTF 题，去套另一家美国顶模的黑客能力。Fable 防护太硬啃不动，转头打防护更弱的 Opus 4.6 ，主要拿它给那家模型的答案打分。
- 小米 MiMo：把自家用户跟 MiMo 的聊天、写代码记录回放给 Claude 做训练数据，并不拿去给用户看。20 天 40 多万条，走了 1500 多个代理号。时间点刚好卡在 MiMo-V2-Pro 免费试用结束时，疑似靠免费吸引全球开发者来刷量，好批量收割去蒸馏。

…(内容已截断)

## 涉及话题
- OpenAI
- DeepSeek
- Anthropic
- Kimi
- AI
- Qwen
- Claude

[原文链接](https://www.v2ex.com/t/1241357)
