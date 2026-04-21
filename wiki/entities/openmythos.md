---
title: "OpenMythos — Claude Mythosアーキテクチャ逆推开源"
created: 2026-04-21
updated: 2026-04-21
tags: [mythos, claude, architecture, open-source, moe, deepseek]
aliases: ["OpenMythos", "Mythos架构逆推", "22歳天才"]
source_lang: zh-CN
source: juejin
url: "https://juejin.cn/post/7630668808157954048"
---

# OpenMythos — Claude Mythosアーキテクチャ逆推开源

> **トレンド順位**: NEW（2026-04-20 Juejin、量子位报道）
> **ソース**: Juejin（量子位）
> **作者**: 量子位
> **関連**: [[claude-opus-4-7]], [[deepseek]]

## 概要

**OpenMythos**は、22歳の開発者によりClaude Mythosアーキテクチャを逆推して实现された开源プロジェクトである。Mythosの「危险性强すぎて封印された」という評判を覆し、公開研究と主流推測を統合して再建した。

## 背景：Mythosとは

Claude Mythosは、Anthropicの未发布（or一部限定提供）の先进アーキテクチャ。以下の特征があると言われる：

- 非常に强大的な推論能力
- 危険な研究任务への対応
- セキュリティ上の理由から封印状態

## OpenMythosの技術的選択

| 技術要素 | Mythosでの推测 | OpenMythosでの実装 |
|---------|---------------|-------------------|
| MoEアーキテクチャ | 专家混合路由 | DeepSeek風のMoE実装 |
| 注意機構 | 改良Attention | Long Context Attention |
| 訓練データ | 合成データ主体 | 公开データ+合成 |

## DeepSeekの影響

OpenMythosはDeepSeekの技術を積極的に取り込んでいる：

- **MoE實現** — DeepSeek-MoEアーキテクチャ参考
- **動的路由** — DeepSeekの専門家選択メカニズム
- **細粒度計算** — DeepSeekの/$D_{split}$アプローチ

## 主要信息来源

- [Mythos架构被22岁小伙“逆推”开源了！MoE和注意力借鉴DeepSeek](https://juejin.cn/post/7630668808157954048)（量子位）
- [OpenMythos GitHub](https://github.com/openmythos)