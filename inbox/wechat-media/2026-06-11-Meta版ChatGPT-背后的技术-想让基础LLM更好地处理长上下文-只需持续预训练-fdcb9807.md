---
title: "「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练"
source: wechat-media
url: "https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS-Ca30eJ9oKojPdsBpmyo-LQm8hx1iYIrFqXa8Fplpd96W-voCf0SI2BU-KvIRjeqmkvAqmdrQQL3W-CuiGHX9XTkF0R7PM1hJZr9Qh9ERiFgxZMHTYLdjK3bP5X1uWkaF9vTMtriEoZA2zsv8X9opG0JDuCtr3HNrN2lDTCQmaDzArFnATRQxpO1Ji90-5xQbysGgOsQDViET15vYaZ3E4YJSSFPgfogQ..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=6F7367B83BA268CCF6F3A60068E4BACDF64E79456A2A798F"
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

[原文链接](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS-Ca30eJ9oKojPdsBpmyo-LQm8hx1iYIrFqXa8Fplpd96W-voCf0SI2BU-KvIRjeqmkvAqmdrQQL3W-CuiGHX9XTkF0R7PM1hJZr9Qh9ERiFgxZMHTYLdjK3bP5X1uWkaF9vTMtriEoZA2zsv8X9opG0JDuCtr3HNrN2lDTCQmaDzArFnATRQxpO1Ji90-5xQbysGgOsQDViET15vYaZ3E4YJSSFPgfogQ..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=6F7367B83BA268CCF6F3A60068E4BACDF64E79456A2A798F)
