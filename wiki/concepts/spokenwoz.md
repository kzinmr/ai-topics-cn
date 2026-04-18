---
title: "SpokenWOZ — 达摩院Dialogue Agents基盤"
created: 2026-04-18
updated: 2026-04-18
tags: [ai-agents, dialogue, damo, alibaba, spoken-language]
aliases: ["SpokenWOZ", "spokenwoz", "Dialogue Agents"]
source_lang: zh-CN
---

# SpokenWOZ — 达摩院Dialogue Agents基盤

> **トレンド順位**: 04-18初登場（WeChat PaperWeeklyで言及）
> **ステータス**: Research/Dataset
> **開発元**: 阿里巴巴达摩院（Alibaba DAMO Academy）

## 概要

SpokenWOZは、阿里巴巴达摩院（DAMO Academy）が推進する**Dialogue Agents**の新基盤プロジェクト。大規模言語モデル（LLM）を対話エージェントに応用する際のコア課題——**短期記憶（会話状態追跡）**のボトルネック——に焦点を当てた研究・データセット基盤である。

OpenAIのLilian Wengが提唱した「Agent = LLM + Memory + Planning + Tools」フレームワークを、**音声対話（Spoken Dialogue）**の文脈で具体化する試みとして位置づけられる。

## 技術的背景

大規模モデルの対話エージェントにおける主要課題：

- **短期記憶の限界**: LLMsは会話状態追跡（Dialogue State Tracking, DST）において短期記憶のボトルネックに直面
- **マルチモーダル統合**: 音声入力 → 意味理解 → 状態追跡 → 応答生成のパイプライン
- **実世界対話の複雑性**: ノイズ、割り込み、文脈依存の発話への対応

## 関連プロジェクト

SpokenWOZは以下の文脈で位置づけられる：
- [[ai-agent]] — 大規模Agentエコシステムの一部
- 复旦NLPチームの80頁Agent総説 — 学術的裏付け
- DAMO Academyの対話AI研究シリーズ

## 出典

| ソース | 言及 | ティア |
|---|---|---|
| PaperWeekly (WeChat) | [大模型剑指AIAgents,达摩院推出Dialogue Agents新基SpokenWOZ](https://weixin.sogou.com/link?url=...) | T4: WeChatメディア（タイトルのみ） |

> **注意**: 2026-04-18時点でフルコンテンツの記事は確認できていない。タイトル情報のみの言及。

## 関連リンク

### 内部リンク
- [[ai-agent]] — AI Agent全般
- [[damo-alibaba]] — 达摩院（DAMO Academy）
