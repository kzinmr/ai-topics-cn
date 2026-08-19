---
title: "「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练"
source: wechat-media
url: "https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgSyv24OX1TBrNbITR6ya2O2xuuYoz1Y3NOlqXa8Fplpd9KXYZB_wyKuhCZvv_askHPCbTI6cz6ezLJ8g846aW3RvWB6iZYjmL_xLSDPt9iqqgX1KJbzJF7dfwW7j_QpJkSc9Q40_2spnqMv_50rlWG1Zwe6VFi69fJt1HR3oeznZeuhjF3p9ITwKdQJhWUkE8pRMJz8GN3OPFp3jw_fzHrTBj3x9Nw6p-Fg..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=68738233A538F2566B6D3207D90688646CD170506A8619B3"
author: "机器之心"
date: 2023-11-27
score: 0
tags: ["大模型", "LLM", "LLaMA", "ChatGPT"]
---

# 「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练

> 来源: 机器之心 (微信公众号)

机器之心报道编辑:Panda W在处理长上下文方面,LLaMA 一直... 基础大模型、AIAgent,及其在 Meta 产品线中的应用,此前曾在 ...

## 涉及话题
- 大模型
- LLM
- LLaMA
- ChatGPT

[原文链接](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgSyv24OX1TBrNbITR6ya2O2xuuYoz1Y3NOlqXa8Fplpd9KXYZB_wyKuhCZvv_askHPCbTI6cz6ezLJ8g846aW3RvWB6iZYjmL_xLSDPt9iqqgX1KJbzJF7dfwW7j_QpJkSc9Q40_2spnqMv_50rlWG1Zwe6VFi69fJt1HR3oeznZeuhjF3p9ITwKdQJhWUkE8pRMJz8GN3OPFp3jw_fzHrTBj3x9Nw6p-Fg..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=68738233A538F2566B6D3207D90688646CD170506A8619B3)
