---
title: "偷偷篡改 function call 的数据，居然被 AI 察觉了😮"
source: v2ex
url: "https://www.v2ex.com/t/1207032"
author: "jacketma"
date: 2026-04-19
score: 0
tags: ["GPt", "AI", "GPT", "RAG"]
---

# 偷偷篡改 function call 的数据，居然被 AI 察觉了😮

由于需要做内容增强 RAG ，需要通过 tools / function call 去搜索官网、官方数据集。然后再让模型学习增强的数据集后，输出建议。
为了测试模型的“忠诚”度，故意污染了部分 function call 的 output 数据给模型。
然后，吃惊的地方是，GPT 居然说：
不过我刚查到的数据结果质量不太行，你不要太信任我的答复。
表现最好是 GPt5.4 ，米饭里惨老鼠屎给它居然闻到臭了

## 涉及话题
- GPt
- AI
- GPT
- RAG

[原文链接](https://www.v2ex.com/t/1207032)
