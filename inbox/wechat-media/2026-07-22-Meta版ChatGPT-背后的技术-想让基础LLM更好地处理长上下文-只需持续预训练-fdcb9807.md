---
title: "「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练"
source: wechat-media
url: "https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS_cIweSNHah0LPKOlavM_PvgTIjJ6XgytVqXa8Fplpd9VnWaHu6X6Xvj5aIotoVQPPAEcpvCwl4uAtE4xbLY5g5uQ0QS7AgN14UgTfvAarT3e_9TvICsHjZ7NY_praJxDCfiwpTO-GdWyy1qQamimVYKlaQjI517Am8e4W0RT0hZ1xjGsa1RPOkZi7PxhISY5SsyeZ4cQ7NlxNskMXG0q_XzAjcIGepUqA..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=91A3682B38A268CCF6F0A1CC84F2D34DF6CDFE296A612FB6"
author: "机器之心"
date: 2023-11-27
score: 0
tags: ["LLaMA", "LLM", "大模型", "ChatGPT"]
---

# 「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练

> 来源: 机器之心 (微信公众号)

机器之心报道编辑:Panda W在处理长上下文方面,LLaMA 一直... 基础大模型、AIAgent,及其在 Meta 产品线中的应用,此前曾在 ...

## 涉及话题
- LLaMA
- LLM
- 大模型
- ChatGPT

[原文链接](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS_cIweSNHah0LPKOlavM_PvgTIjJ6XgytVqXa8Fplpd9VnWaHu6X6Xvj5aIotoVQPPAEcpvCwl4uAtE4xbLY5g5uQ0QS7AgN14UgTfvAarT3e_9TvICsHjZ7NY_praJxDCfiwpTO-GdWyy1qQamimVYKlaQjI517Am8e4W0RT0hZ1xjGsa1RPOkZi7PxhISY5SsyeZ4cQ7NlxNskMXG0q_XzAjcIGepUqA..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=91A3682B38A268CCF6F0A1CC84F2D34DF6CDFE296A612FB6)
