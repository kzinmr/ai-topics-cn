---
title: "NiceEval: 为你的 Agent 构建评估"
source: v2ex
url: "https://www.v2ex.com/t/1225343"
author: "HXHL"
date: 2026-07-06
score: 0
tags: ["Prompt", "agi", "ai", "gpt", "prompt"]
---

# NiceEval: 为你的 Agent 构建评估

评估的意义
在过去程序的开发中，大家用测试来保障程序质量与程序员今晚不会被 oncall 可以安全下班的自信。而现在评估对于 Agent 也是一样意义。
除了保障功能本质，迭代功能本身也需要评估。换模型、调提示词，同一套用例跑一遍看分数在哪些用例是差一点，在哪些指标上更好了。
Langfuse 与 BrainTrust 有什么问题
尽管现在市面上已经有了 DeepEval 、LangFuse 、BrainTrust 。但是它们是 Prompt Enginering 时代的产物，现在 Agent 评估套进 Dataset 还有 Golden 的模型会非常别扭。
随着开发范式收敛，Agent 胜出，所以我做了 NiceEval ，是一个开源、专为 Agent 设计的估计工具。 在 Agent 需要评估多轮对话、工具调用还有 Skill 加载的场景，都能被很好的解决了。
import { defineEval } from "niceeval";

export default defineEval({
  description: "实时天气必须走 get_weather 工具，不许编造",

  async test(t) {
    const turn = await t.send("北京今天天气怎么样？");
    t.succeeded();

    t.calledTool("get_weather", { input: { city: "北京" } });
    t.notCalledTool("web_search");
    t.eventOrder(["action.called", "action.result", "message"]);
    t.messageIncludes(/°C|晴|多云|雨/);


…(内容已截断)

## 涉及话题
- Prompt
- agi
- ai
- gpt
- prompt

[原文链接](https://www.v2ex.com/t/1225343)
