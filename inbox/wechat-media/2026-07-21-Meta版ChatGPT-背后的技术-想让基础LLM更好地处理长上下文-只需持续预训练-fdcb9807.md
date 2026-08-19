---
title: "「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练"
source: wechat-media
url: "https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS8FBffzh1LaSaepEjtDRf2PMtH_JI9iIGFqXa8Fplpd90OK9Fcpx-EVMyOcRGz8VymdVPj7daO0hdx1pHZ99ztXSKhkdU8E9Fw65jEjclHhyV33FK2Px7Lh1sib9CGV8DqU3CCJAoa_LsVQD0GXe4WTNdOhyuZH-RJ4FmK4Ygvnbuwy7WGtSdHnDCS_2drtugYSgFYDd8hXFCgxYQEHJacpOJBjQH7pCxQ..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=89F832B4C65C9633090F5E2D5BFCCBB1099F1E6D6A5FDE21"
author: "机器之心"
date: 2023-11-27
score: 0
tags: ["LLaMA", "大模型", "ChatGPT", "LLM"]
---

# 「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练

> 来源: 机器之心 (微信公众号)

机器之心报道编辑:Panda W在处理长上下文方面,LLaMA 一直... 基础大模型、AIAgent,及其在 Meta 产品线中的应用,此前曾在 ...

## 涉及话题
- LLaMA
- 大模型
- ChatGPT
- LLM

[原文链接](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS8FBffzh1LaSaepEjtDRf2PMtH_JI9iIGFqXa8Fplpd90OK9Fcpx-EVMyOcRGz8VymdVPj7daO0hdx1pHZ99ztXSKhkdU8E9Fw65jEjclHhyV33FK2Px7Lh1sib9CGV8DqU3CCJAoa_LsVQD0GXe4WTNdOhyuZH-RJ4FmK4Ygvnbuwy7WGtSdHnDCS_2drtugYSgFYDd8hXFCgxYQEHJacpOJBjQH7pCxQ..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=89F832B4C65C9633090F5E2D5BFCCBB1099F1E6D6A5FDE21)
