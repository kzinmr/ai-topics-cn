---
title: "「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练"
source: wechat-media
url: "https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS4HbLx4e5rvLNHucq2EfHJe7mfos5_VfbVqXa8Fplpd9-LtlRkYUFNSMueATGOaj4zN8lDlnyP-hDjiQU8Nx0MLlR-wYSBRAJZPLkO0jLxXx1AhpCWUA2bRnOZUziSn48Nlxilo1TacgPAAGdxiZkwaeFR94hRWIv8X8J8QRulHWcOpDu-pwCM4pBNULbCK7b9jedWf1Huh6lydmqFy0yT86Ebq8fk9diw..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=D0CA3CA322B973D7ECEBBB378CA5B695ED1B75D46A6BBBAE"
author: "机器之心"
date: 2023-11-27
score: 0
tags: ["大模型", "LLaMA", "LLM", "ChatGPT"]
---

# 「Meta版ChatGPT」背后的技术:想让基础LLM更好地处理长上下文,只需持续预训练

> 来源: 机器之心 (微信公众号)

机器之心报道编辑:Panda W在处理长上下文方面,LLaMA 一直... 基础大模型、AIAgent,及其在 Meta 产品线中的应用,此前曾在 ...

## 涉及话题
- 大模型
- LLaMA
- LLM
- ChatGPT

[原文链接](https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS4HbLx4e5rvLNHucq2EfHJe7mfos5_VfbVqXa8Fplpd9-LtlRkYUFNSMueATGOaj4zN8lDlnyP-hDjiQU8Nx0MLlR-wYSBRAJZPLkO0jLxXx1AhpCWUA2bRnOZUziSn48Nlxilo1TacgPAAGdxiZkwaeFR94hRWIv8X8J8QRulHWcOpDu-pwCM4pBNULbCK7b9jedWf1Huh6lydmqFy0yT86Ebq8fk9diw..&type=2&query=%E6%9C%BA%E5%99%A8%E4%B9%8B%E5%BF%83 LLM AI Agent %E5%A4%A7%E6%A8%A1%E5%9E%8B&token=D0CA3CA322B973D7ECEBBB378CA5B695ED1B75D46A6BBBAE)
