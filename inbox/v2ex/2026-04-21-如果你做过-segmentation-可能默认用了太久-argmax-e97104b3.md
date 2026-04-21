---
title: "如果你做过 segmentation，可能默认用了太久 argmax"
source: v2ex
url: "https://www.v2ex.com/t/1207289"
author: "lev1s"
date: 2026-04-20
score: 1
tags: ["transformer", "AI", "推理", "Transformer", "MCP"]
---

# 如果你做过 segmentation，可能默认用了太久 argmax

最近 AI 圈聊 agent 、workflow 、MCP 聊得很热，我最近反而回头看了一个很土的地方：image segmentation 最后那一步，到底是不是应该那么理所当然地 argmax。
如果你做过这类任务，流程基本都差不多：模型吐出 per-pixel logits 或 probability map ，插值回原图尺寸，然后 argmax 或 threshold 出 mask 。SegFormer 、DeepLab 、UPerNet 这类语义分割模型是这样，很多把 SAM 或别的视觉 backbone 接到语义分割结果上的链路，最后也还是这一步。写久了之后，很容易把它当成一个收尾动作，而不是一个值得单独优化的决策规则。
但 image segmentation 偏偏不是一个只看局部对错的任务。线上或者论文里真正看的，通常是 mIoU / mDice 这类整体 overlap 指标，而 argmax / threshold 更像是逐像素做贪心决策。每个 pixel 单独看都没问题，不代表整张 mask 的全局指标最优，尤其是小物体、边界、遮挡和一些碎区域，常常就是在最后这一步开始丢。
我最近在参与 RankSEG 这条线，做的事情其实很朴素：不改训练，不碰模型权重，只重写“怎么把概率图变成最终 mask”这一步。换句话说，就是把 pipeline 里默认的 probs.argmax(dim=1) 换成一个更贴 segmentation 指标的后处理。对已经有现成推理链路的人来说，改动点非常明确，不是另起一套系统。

…(内容已截断)

## 涉及话题
- transformer
- AI
- 推理
- Transformer
- MCP

[原文链接](https://www.v2ex.com/t/1207289)
