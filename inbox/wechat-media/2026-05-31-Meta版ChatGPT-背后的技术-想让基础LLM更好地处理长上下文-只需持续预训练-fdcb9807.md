---
title: "「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练"
source: wechat-media
url: "https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgSwBMLTvT9kOKdPOr9ky0SUO-vw0n61ofdVqXa8Fplpd9tyINFv9F9NXu5Ml8dVQ6L80C1TUdDQfwTEE-ZosEUJbM2jdE4QvXK3B6I0RbKH5CE5FHZB1EHRNH2b5mjhLtg-VB9EX4HtH8IPvfy1TPWZJl9EqxGTaS6pdpP49mhudX9nU7hwY_rIUP4opUCGqbB6p-7Fb532BWtEPciPeES1HS-e4Yz84xMA..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=1E76B4E722BF72D1EBEDBFCF8B1982BCEC71A36B6A1CA1A0"
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

[原文链接](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgSwBMLTvT9kOKdPOr9ky0SUO-vw0n61ofdVqXa8Fplpd9tyINFv9F9NXu5Ml8dVQ6L80C1TUdDQfwTEE-ZosEUJbM2jdE4QvXK3B6I0RbKH5CE5FHZB1EHRNH2b5mjhLtg-VB9EX4HtH8IPvfy1TPWZJl9EqxGTaS6pdpP49mhudX9nU7hwY_rIUP4opUCGqbB6p-7Fb532BWtEPciPeES1HS-e4Yz84xMA..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=1E76B4E722BF72D1EBEDBFCF8B1982BCEC71A36B6A1CA1A0)
