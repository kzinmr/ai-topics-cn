---
title: "「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练"
source: wechat-media
url: "https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS2IuWgVPPK44XEWqSGzj9K0I4LMh-hFMvVqXa8Fplpd9skLEq2WLM4K94lWCtwsgfjh6Js_FQOqGCdG9yV2Kz8W6iyeHjp15AP9RPh6uGpSqmTC0JV1Ju5OGtmYD4zvLp0zgfHi-AdiL6VMJ4WQQns4uwthvVNb1u1SWQxJQkG7dSrEd-BigKpeyyd98s5gm3mGm7ouYxEOcBWXQe3ww-X85eBgmN3LoYQ..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=7A6709A92EB441E5DFE6B622C97C8A67E022C6B86A5D3B16"
author: "机器之心"
date: 2023-11-27
score: 0
tags: ["ChatGPT", "大模型", "LLM", "LLaMA"]
---

# 「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练

> 来源: 机器之心 (微信公众号)

机器之心报道编辑:Panda W在处理长上下文方面,LLaMA 一直... 基础大模型、AIAgent,及其在 Meta 产品线中的应用,此前曾在 ...

## 涉及话题
- ChatGPT
- 大模型
- LLM
- LLaMA

[原文链接](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS2IuWgVPPK44XEWqSGzj9K0I4LMh-hFMvVqXa8Fplpd9skLEq2WLM4K94lWCtwsgfjh6Js_FQOqGCdG9yV2Kz8W6iyeHjp15AP9RPh6uGpSqmTC0JV1Ju5OGtmYD4zvLp0zgfHi-AdiL6VMJ4WQQns4uwthvVNb1u1SWQxJQkG7dSrEd-BigKpeyyd98s5gm3mGm7ouYxEOcBWXQe3ww-X85eBgmN3LoYQ..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=7A6709A92EB441E5DFE6B622C97C8A67E022C6B86A5D3B16)
