---
title: "「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练"
source: wechat-media
url: "https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7tmHmw5-4kOE_yG7kOgN4AU_8IeoWibuVqXa8Fplpd9dj6xH0LMyIZrqd9o9T7wKs0r2tyDEJPWSmv1uZy4TUD8prqwRdKt1ScN2e0q8JlCf0A4KywQTIj5nOZoC5POGSXM4tFiMnkWaZOhs24N8CY0Vb_NOwGU7N1lnQB-N3V4Uk5LdMra2TUlpdBgl1Wz7iquFRMXGo-k-16G_3abp8Be0WC6Sbi7DA..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=F6502E36EC75BC1B2124723DC4C5FCC92289A62D69E9E00F"
author: "机器之心"
date: 2023-11-27
score: 0
tags: ["LLM", "LLaMA", "ChatGPT", "大模型"]
---

# 「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练

> 来源: 机器之心 (微信公众号)

机器之心报道编辑:Panda W在处理长上下文方面,LLaMA 一直... 基础大模型、AIAgent,及其在 Meta 产品线中的应用,此前曾在 ...

## 涉及话题
- LLM
- LLaMA
- ChatGPT
- 大模型

[原文链接](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS7tmHmw5-4kOE_yG7kOgN4AU_8IeoWibuVqXa8Fplpd9dj6xH0LMyIZrqd9o9T7wKs0r2tyDEJPWSmv1uZy4TUD8prqwRdKt1ScN2e0q8JlCf0A4KywQTIj5nOZoC5POGSXM4tFiMnkWaZOhs24N8CY0Vb_NOwGU7N1lnQB-N3V4Uk5LdMra2TUlpdBgl1Wz7iquFRMXGo-k-16G_3abp8Be0WC6Sbi7DA..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=F6502E36EC75BC1B2124723DC4C5FCC92289A62D69E9E00F)
