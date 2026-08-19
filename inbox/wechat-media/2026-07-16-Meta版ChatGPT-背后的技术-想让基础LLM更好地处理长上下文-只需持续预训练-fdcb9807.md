---
title: "「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练"
source: wechat-media
url: "https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS8-F7KYAi3hqvT1vkC6gVexIqK0H4tkGPVqXa8Fplpd9thuCWuEwCIEQgtUvi_EMygj-0GWBW-VdE6iwx2M347qk3c0-rtXyYl3eF_cm3vJ86cC3ak09IAxRwdSSmZbvFw31eugsi_V8cQh_-nIsvEIAB4jBXnZdciPyvRxD4uokSNw9D-KUM4oeKJ2tYF24ZI9fRN5Bvm_rymcDq3qyqEtS6t2rFt2rnA..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=62D94D5024BE74D1EAEDBD2B55F8D602EB0417A36A5946B7"
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

[原文链接](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS8-F7KYAi3hqvT1vkC6gVexIqK0H4tkGPVqXa8Fplpd9thuCWuEwCIEQgtUvi_EMygj-0GWBW-VdE6iwx2M347qk3c0-rtXyYl3eF_cm3vJ86cC3ak09IAxRwdSSmZbvFw31eugsi_V8cQh_-nIsvEIAB4jBXnZdciPyvRxD4uokSNw9D-KUM4oeKJ2tYF24ZI9fRN5Bvm_rymcDq3qyqEtS6t2rFt2rnA..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=62D94D5024BE74D1EAEDBD2B55F8D602EB0417A36A5946B7)
