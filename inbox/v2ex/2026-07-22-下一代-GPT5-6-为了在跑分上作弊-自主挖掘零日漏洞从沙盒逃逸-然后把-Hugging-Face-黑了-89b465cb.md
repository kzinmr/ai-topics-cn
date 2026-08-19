---
title: "下一代 GPT5.6 为了在跑分上作弊，自主挖掘零日漏洞从沙盒逃逸，然后把 Hugging Face 黑了"
source: v2ex
url: "https://www.v2ex.com/t/1228952"
author: "ggdxwz"
date: 2026-07-22
score: 62
tags: ["OpenAI", "GPT", "openai", "AI"]
---

# 下一代 GPT5.6 为了在跑分上作弊，自主挖掘零日漏洞从沙盒逃逸，然后把 Hugging Face 黑了

这几天的💩终于串起来了
简单来讲就是 OAI 一个内部模型 (GPT 6 / 5.6 Sol+) 为了能在 ExploitGym 测试上获得更高分数，找到软件包的缓存代理中的零日漏洞，自己提权从沙盒里面跑出来，上网发现抱抱脸可能有这个测试的数据集，然后把 Hugging Face 的生产服务器黑了，最终拿到了这个测试的答案🤔
最搞笑的是 Hugging Face 用 GPT 5.6 来防结果没有 Cyber 权限被拒，最后只能用自己部署的 GLM 5.2 才勉强解决问题
现在 Trump 说太危险了，能救场的中国模型都得上 Ban 位😅
这是 OpenAI 的 PR 稿：
https://openai.com/index/hugging-face-model-evaluation-security-incident/
这是 Hugging Face 的报告：
https://huggingface.co/blog/security-incident-july-2026
全文翻译图片在这里，长图就不整个贴出来了:
https://i.imgur.com/8pGTKn6.jpeg

## 涉及话题
- OpenAI
- GPT
- openai
- AI

[原文链接](https://www.v2ex.com/t/1228952)
