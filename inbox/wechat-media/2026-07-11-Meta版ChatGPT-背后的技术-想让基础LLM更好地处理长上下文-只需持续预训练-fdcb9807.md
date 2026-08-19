---
title: "「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练"
source: wechat-media
url: "https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS-uWX6u8fIhvz5AaaBz-ByZADKFVDNcUelqXa8Fplpd9N5PL3XkTletmjtOPR0W_f2uvBfwHRW76N6GdxtBcK_aZWmXEmeSLMlWDV_tNVzfS60cNuhfcN2QC8macL3LhcZ2mV3G1zIcEZyLwRXLUABnr_dxnYHLSiq87QYMtYA8bA68Hmcrj0Gz8rnr3WdBMY2jOatiu4RGtZk3X-QyeFJ_vzHZXxeLdyg..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=3FD50FB264FF3591ABACFDF781423BBAABC37B1C6A52AF49"
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

[原文链接](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS-uWX6u8fIhvz5AaaBz-ByZADKFVDNcUelqXa8Fplpd9N5PL3XkTletmjtOPR0W_f2uvBfwHRW76N6GdxtBcK_aZWmXEmeSLMlWDV_tNVzfS60cNuhfcN2QC8macL3LhcZ2mV3G1zIcEZyLwRXLUABnr_dxnYHLSiq87QYMtYA8bA68Hmcrj0Gz8rnr3WdBMY2jOatiu4RGtZk3X-QyeFJ_vzHZXxeLdyg..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=3FD50FB264FF3591ABACFDF781423BBAABC37B1C6A52AF49)
