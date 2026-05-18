---
title: "Hermes TTS（语音回复， Discord 语音频道交互）本地搭建分享（4GB 显存要求）"
source: v2ex
url: "https://www.v2ex.com/t/1212277"
author: "sentinelK"
date: 2026-05-12
score: 0
tags: ["推理", "LLM", "chatGPT", "ChatGPT"]
---

# Hermes TTS（语音回复， Discord 语音频道交互）本地搭建分享（4GB 显存要求）

简而言之：Fish Speech 1.5 + 真实参考音色（可以直接让 hermes 去 youtube 和 bilibili 去扒，选自己喜欢的，没有 bgm 的，最好是那种纯聊天的视频）

关键配置：
"chunk_length": 400,
"temperature": 0.7,
"top_p": 0.8,
"repetition_penalty": 1.1,

参考音色控制在 15 秒以内（超过 20 秒会过拟合，起反效果）

推理精度：FP32 （~3.5GB VRAM ；也可以 --half FP16 ~1.74GB ）

最终性能：RTX 3070 ，0.32 倍时间消耗（生成 1 分钟的音频，大概需要 18~20 秒）

推荐 hermes PUA 话术：
1 、hermes ，帮我安装 fish speech1.5 当作你的 TTS 工具
2 、把(一个 bilibili 网址)这个视频的人的音色当作参考音色，截取最清晰的 12 秒
3 、设置参数：如上
4 、生成 X 个种子样例，我听听看选择哪个种子效果。
5 、ok ，就选 x 种子吧，以后回复语音的时候你要进行口语化润色。
6 、把整个目前敲定的 TTS 流程记下来。以后我发语音给你，你就要语音回复我。

以上这套配置，只要 hermes 的基座 LLM 够快，完全可以支撑 discord 语音频道对话聊天，且没有机器人感，体验不亚于 ChatGPT 的 Talk 模式。

当然，chatGPT 的语音是类似 chatTTS 的模拟聊天类，会有更多口语的润色效果，且支持打断。目前 Fish Speech 的方案还不能支持。

## 涉及话题
- 推理
- LLM
- chatGPT
- ChatGPT

[原文链接](https://www.v2ex.com/t/1212277)
