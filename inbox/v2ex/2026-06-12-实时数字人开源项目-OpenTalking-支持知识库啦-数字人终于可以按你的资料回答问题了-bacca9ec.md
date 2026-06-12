---
title: "[实时数字人开源项目] OpenTalking 支持知识库啦！数字人终于可以按你的资料回答问题了"
source: v2ex
url: "https://www.v2ex.com/t/1219981"
author: "xuxin123122"
date: 2026-06-12
score: 0
tags: ["AI", "RAG", "LLM", "ai"]
---

# [实时数字人开源项目] OpenTalking 支持知识库啦！数字人终于可以按你的资料回答问题了

V 站大佬们！ OpenTalking 最近把知识库能力接进来了！
之前 OpenTalking 主要是实时数字人对话链路：LLM 回复、TTS 、STT 、WebRTC 、字幕、数字人驱动模型这些。现在我们又补了一层 Agent Context ，可以给数字人挂知识库，让它不只是“会聊天”，也能基于你上传的资料回答业务问题、产品问题、文档问题。
现在大概能做这些：
上传文档，创建自己的知识库
一个数字人可以绑定一个或多个知识库
对话时自动检索相关片段，再注入给 LLM
知识库和长期记忆冲突时，事实类问题优先听知识库
没有检索到相关内容时，会尽量避免瞎编
Persona Package 里也可以带知识库，方便把一个完整数字人交付出去
比如你可以做：
带公司产品手册的数字人客服
带课程讲义的 AI 老师
带直播话术和商品资料的数字人导购
带项目文档的内部知识助手
带 FAQ / SOP 的培训数字人
我们想做的不是单纯的 RAG demo ，而是把知识库能力放进实时数字人的完整链路里：用户开口问，数字人检索资料、组织回答、合成语音、同步字幕和画面，最后像一个真正“懂业务”的虚拟角色一样回复。
目前项目还是开源免费的 side project ，欢迎大家体验、拍砖、提 issue ，也欢迎来贡献代码。
Github 传送：
https://github.com/datascale-ai/opentalking
B 站演示：
https://www.bilibili.com/video/BV18fEr6UEQW/
麻烦感兴趣的大佬顺手点个 Star ！你们的支持是我们继续保持免费和开源的动力！！！
欢迎大家体验，多多提意见！

## 涉及话题
- AI
- RAG
- LLM
- ai

[原文链接](https://www.v2ex.com/t/1219981)
