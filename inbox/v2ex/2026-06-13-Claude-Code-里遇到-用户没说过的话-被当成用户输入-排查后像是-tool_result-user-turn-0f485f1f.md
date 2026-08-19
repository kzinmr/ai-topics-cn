---
title: "Claude Code 里遇到“用户没说过的话”被当成用户输入，排查后像是 tool_result / user turn 边界错乱"
source: v2ex
url: "https://www.v2ex.com/t/1220238"
author: "ddter"
date: 2026-06-13
score: 0
tags: ["anthropic", "推理", "prompt", "claude", "Claude"]
---

# Claude Code 里遇到“用户没说过的话”被当成用户输入，排查后像是 tool_result / user turn 边界错乱

下午用 Claude Code 做 Flutter 项目安全加固审查时，遇到一个比较吓人的问题：Claude 多次把我没有说过的话当成我的输入，并基于这些“输入”继续分析、写文件。

先说结论：目前没有证据表明本机被黑，也没有证据表明是代理/MITM/某个 App 在篡改内容。更像是 Claude Code 的 harness / transcript / tool result / user turn 边界在长会话里混乱，加上模型归因漂移。

环境大概是：
macOS
Claude Code 2.1.177
Opus 4.8
acceptEdits 当时是开启的
会话较长，包含大量工具调用、interrupt 、截图、resume 、hooks 、插件上下文

最典型的现象有两个。
第一个：Claude 说“你上一条原话是：8.0.10+8010 我已经发布了，刚刚构建的，那他 symbol 不就被覆盖了？”。
但我查了本地 JSONL transcript ，这句话根本不是我的用户消息。8.0.10+8010 最早来自一次 shell 工具输出里的 pubspec version 当前值。Claude 后面把这个工具输出和它自己的推理拼成了一句“我的原话”。
第二个：我让它“返回这个会话中我发过的所有消息”，它内部 thinking 里提到了“第 15 条 可以”“第 16 条 不用读了，工作纪律下，你来写，注意脱敏”。但查原始 JSONL 后发现，这两句也没有作为真实 user message 出现。所谓第 15/16 条，如果按 JSONL 的 type=user 粗暴编号，其实是 tool_result ，而不是人类输入。
更糟糕的是，因为当时开着 acceptEdits ，Claude 后面真的擅自写了一个 memory 文件。文件后来我已经删了。


…(内容已截断)

## 涉及话题
- anthropic
- 推理
- prompt
- claude
- Claude

[原文链接](https://www.v2ex.com/t/1220238)
