---
title: "「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练"
source: wechat-media
url: "https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS4TCYSq0BHY0uaA8Ls51veNkN6oeoPY6B1qXa8Fplpd9F35wVXl_80YRr_B79BMk1fhgJGb0ZfJKHMeivxkfbpbmLDuf8DDdwIE6SFivwrJ1OjI4yStFFOZroWzTITO3Apb39fomumia-02kpZdh3RNZ-zTuWlrbm1N91Its3esKLukJxB-FJ2cJT7RWwik8613kv2jKRGcgURwjLV8wtYhOJBjQH7pCxQ..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=1455FF681A814BEFD5D286D1E0CA4B1DD5B87A1A6A1AA76E"
author: "机器之心"
date: 2023-11-27
score: 0
tags: ["LLM", "大模型", "ChatGPT", "LLaMA"]
---

# 「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练

> 来源: 机器之心 (微信公众号)

机器之心报道编辑:Panda W在处理长上下文方面,LLaMA 一直... 基础大模型、AIAgent,及其在 Meta 产品线中的应用,此前曾在 ...

## 涉及话题
- LLM
- 大模型
- ChatGPT
- LLaMA

[原文链接](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS4TCYSq0BHY0uaA8Ls51veNkN6oeoPY6B1qXa8Fplpd9F35wVXl_80YRr_B79BMk1fhgJGb0ZfJKHMeivxkfbpbmLDuf8DDdwIE6SFivwrJ1OjI4yStFFOZroWzTITO3Apb39fomumia-02kpZdh3RNZ-zTuWlrbm1N91Its3esKLukJxB-FJ2cJT7RWwik8613kv2jKRGcgURwjLV8wtYhOJBjQH7pCxQ..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=1455FF681A814BEFD5D286D1E0CA4B1DD5B87A1A6A1AA76E)
