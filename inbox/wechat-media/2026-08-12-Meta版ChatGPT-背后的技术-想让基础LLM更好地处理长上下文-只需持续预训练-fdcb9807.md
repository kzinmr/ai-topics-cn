---
title: "「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练"
source: wechat-media
url: "https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgSyYIgirMiNdo2cTTEWi0E9eh4f4IT82V8FqXa8Fplpd9IhvtQWoiLd4Oo95QYTj5tFsBQkUDVSLLgH8WZRQh-mPxtiB6_4neXEWzA73Tl54Ie9em8zmQ_IX_J178lJ3Lqh2q-k_YDJ_Q7HzV4i6VK92wpBz3OHkG95hpXY71as_lN56fhRml2Hzzz51ePP_Z2YuCeRDDMB5aX__JIbFPifY6Ebq8fk9diw..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=34A961E8841ED7734A4C1196AD8C0C414A2CCC256A7CDF38"
author: "机器之心"
date: 2023-11-27
score: 0
tags: ["LLM", "ChatGPT", "大模型", "LLaMA"]
---

# 「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练

> 来源: 机器之心 (微信公众号)

机器之心报道编辑:Panda W在处理长上下文方面,LLaMA 一直... 基础大模型、AIAgent,及其在 Meta 产品线中的应用,此前曾在 ...

## 涉及话题
- LLM
- ChatGPT
- 大模型
- LLaMA

[原文链接](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgSyYIgirMiNdo2cTTEWi0E9eh4f4IT82V8FqXa8Fplpd9IhvtQWoiLd4Oo95QYTj5tFsBQkUDVSLLgH8WZRQh-mPxtiB6_4neXEWzA73Tl54Ie9em8zmQ_IX_J178lJ3Lqh2q-k_YDJ_Q7HzV4i6VK92wpBz3OHkG95hpXY71as_lN56fhRml2Hzzz51ePP_Z2YuCeRDDMB5aX__JIbFPifY6Ebq8fk9diw..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=34A961E8841ED7734A4C1196AD8C0C414A2CCC256A7CDF38)
