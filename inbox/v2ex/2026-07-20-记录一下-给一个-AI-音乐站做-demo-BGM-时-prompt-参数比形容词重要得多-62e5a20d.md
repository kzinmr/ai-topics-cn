---
title: "记录一下：给一个 AI 音乐站做 demo BGM 时， prompt 参数比形容词重要得多"
source: v2ex
url: "https://www.v2ex.com/t/1228614"
author: "quanmengli"
date: 2026-07-20
score: 1
tags: ["AI", "prompt"]
---

# 记录一下：给一个 AI 音乐站做 demo BGM 时， prompt 参数比形容词重要得多

最近给自己一个小页面做 demo 视频，想快速弄一段不侵权、能放在背景里的音乐。之前总觉得 AI 音乐就是输入一句“cinematic / emotional / inspiring”然后碰运气，实际折腾下来发现，真正有用的不是这些形容词，而是更具体的音乐参数。
我测试的页面是这个： https://flowmusic.co/

不是来吹效果多神，主要是拿它当一个 text-to-song 的测试对象。
比较稳定的 prompt 写法大概是：
lo-fi hip hop, dusty piano, vinyl crackle, mellow, 70 bpm, no vocals

比下面这种靠谱很多：
emotional, cinematic, inspiring

原因挺直观的：后者只给了情绪，没有告诉模型到底是什么曲风、什么乐器、有没有人声、速度大概多少。结果通常就是一段很泛的广告/预告片味背景音乐。
目前感觉比较有用的顺序是：

先写 genre ，比如 lo-fi hip hop / ambient electronic / acoustic ballad
再写 instrumentation ，比如 dusty piano / soft synth pads / light percussion
明确 vocals / no vocals
写 bpm 或 slow / mid-tempo
最后再补 mood ，比如 calm / nostalgic / darker tone

如果只是产品 demo 、加载页、短视频背景这种用途，no vocals 很重要。带人声以后变量太多，歌词、发音、声线都会抢注意力，反而不好当背景。

…(内容已截断)

## 涉及话题
- AI
- prompt

[原文链接](https://www.v2ex.com/t/1228614)
