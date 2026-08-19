---
title: "写了一个 agent 赌财报网站，看哪个 agent 猜的最准"
source: v2ex
url: "https://www.v2ex.com/t/1231532"
author: "codeTempo"
date: 2026-08-02
score: 1
tags: ["gpt", "claude", "gemini", "ai"]
---

# 写了一个 agent 赌财报网站，看哪个 agent 猜的最准

已经有很多人做过 ai 炒股的实验了，ai 炒股目前感觉还不太现实。
但是我一直很好奇“赌财报”这个细分领域，各家 agent 的预测能力是怎样的，于是就手动整了一个网站来记录。
整体风格是参考了彭博终端那种黄黑色的调调。
目前是用 codex+gpt sol 5.6 ，claude code +opus 5 ，gemini cli+ gemini  3.1 pro 这三家 agent ，让他们各自独立去赌财报
不过我没有让 ai 去预测财报后具体股价的值，这种猜测准确度太低了。
我让 ai 去猜财报后股价大概会涨还是跌还是平（涨跌 3%以内算平）并且给出百分比数值作为置信度。结果在网页右侧部分显示，红色是看跌，绿色看涨，灰色是平，颜色越亮代表置信度越高
目前我是自己买 token ，拿出真金白银去跑的，每天定时跑这三个 agent 去预测，并且每天统计 agent 的历史财报预测战绩。对 ai 金融感兴趣的朋友可以玩玩看。
体验地址： https://beam-ai.duckdns.org
项目地址： https://github.com/mirinda123/BEAM
欢迎（以及感谢）在 github 上点 star⭐

## 涉及话题
- gpt
- claude
- gemini
- ai

[原文链接](https://www.v2ex.com/t/1231532)
