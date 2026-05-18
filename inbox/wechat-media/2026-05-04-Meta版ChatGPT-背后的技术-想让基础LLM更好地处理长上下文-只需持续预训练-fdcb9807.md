---
title: "「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练"
source: wechat-media
url: "https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS9vHZgyQ411ahwZFmUat5AKehmI7On2D51qXa8Fplpd9v-8Y608LP6oAnVCsv50RSHik08yzv2jr4NQ56gZ97LMwttHRXd-19KEqDox_3npCZKutnlBQnnRsz0UY3PjKr4X1BZ3GAHnzmdlE0Eqy2ax9_C8bSiBBuRVVL9bnOojN5PbhbTMr-6is1mSSkIzH3xzNLcBkxgRrIPJaHyw3HNbFcvUoAZZH7Q..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=4EBCC4C9B42EE4437A7F2B7E41F8E0CA7AF7EBFA69F90924"
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

[原文链接](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS9vHZgyQ411ahwZFmUat5AKehmI7On2D51qXa8Fplpd9v-8Y608LP6oAnVCsv50RSHik08yzv2jr4NQ56gZ97LMwttHRXd-19KEqDox_3npCZKutnlBQnnRsz0UY3PjKr4X1BZ3GAHnzmdlE0Eqy2ax9_C8bSiBBuRVVL9bnOojN5PbhbTMr-6is1mSSkIzH3xzNLcBkxgRrIPJaHyw3HNbFcvUoAZZH7Q..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=4EBCC4C9B42EE4437A7F2B7E41F8E0CA7AF7EBFA69F90924)
