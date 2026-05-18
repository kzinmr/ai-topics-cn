---
title: "「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练"
source: wechat-media
url: "https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS_Pr8-16uGuLC3RfUW7LbtyWTCcmOExoa1qXa8Fplpd9Gt9ktZMLIBKymzxQi5ucqZBRg1o8qnvz6ft6nqZJNV_2MmUNhu2S7YKbJO4Pu8jyxmxWu7rsqJw8Yz4fTCGew6usIr0ZOjnLtVpulB2_K3u0YrYi16jbrCBmgRSuWpgBKAPrgIaPUzWgSXPCfQwTMRNfOPgI5yXsj7zOAwZr5kfvzHZXxeLdyg..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=46E3B166108940E7DEDB8D2EC3624146DE1EA9CF69F7B7B5"
author: "机器之心"
date: 2023-11-27
score: 0
tags: ["LLaMA", "LLM", "ChatGPT", "大模型"]
---

# 「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练

> 来源: 机器之心 (微信公众号)

机器之心报道编辑:Panda W在处理长上下文方面,LLaMA 一直... 基础大模型、AIAgent,及其在 Meta 产品线中的应用,此前曾在 ...

## 涉及话题
- LLaMA
- LLM
- ChatGPT
- 大模型

[原文链接](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS_Pr8-16uGuLC3RfUW7LbtyWTCcmOExoa1qXa8Fplpd9Gt9ktZMLIBKymzxQi5ucqZBRg1o8qnvz6ft6nqZJNV_2MmUNhu2S7YKbJO4Pu8jyxmxWu7rsqJw8Yz4fTCGew6usIr0ZOjnLtVpulB2_K3u0YrYi16jbrCBmgRSuWpgBKAPrgIaPUzWgSXPCfQwTMRNfOPgI5yXsj7zOAwZr5kfvzHZXxeLdyg..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=46E3B166108940E7DEDB8D2EC3624146DE1EA9CF69F7B7B5)
