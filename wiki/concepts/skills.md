---
title: Skills — AI Agentの能力モジュール
description: AI Agentにおけるスキルの概念、実装方法、中国エコシステムでの標準化動向。
status: active
category: concept
source_lang: zh-CN
---

# Skills（AIスキル）

**Skills**はAI Agentが特定のタスクを実行するための**能力モジュール**。LLM単体では実現できない専門的な機能を補完する。

## 基本概念

### Claude Code 32 Skills

2026年4月、Anthropicが**Claude Code**に32のSkillsとMCP（Model Context Protocol）統合を追加。開発者向けワークフローの大幅な強化を図った。

### Skillの標準化

中国AIコミュニティでは、**AI Agentスキルガイド**が複数発表されており、Skillsの定義・実装・評価方法の標準化が進んでいる。

## 技術スタック

Skillsは以下の要素で構成される：

1. **トリガー条件** — どの状況でSkillを発動するか
2. **入力パラメータ** — Skillが受け取るデータ
3. **処理ロジック** — 実行されるアルゴリズムまたはAPIコール
4. **出力形式** — Skillの実行結果

## 最新動向（2026年4月）

### 「PromptよりSkill」のパラダイムシフト

2026年1-4月にかけて、中国AIコミュニティ（特にClaude Code/Juejin）で**「Skill」**が大きなトレンドとなっている。

> 「继续堆 Prompt，真的不如早点学 Skill」
> （Promptを積み続けるより、とっととSkillを学んだほうがいい）

この議論の核心は以下の通り：

1. **Promptエンジニアリングの限界**: プロンプトの量と複雑さが増すにつれて、メンテナンスコストが跳ね上がる
2. **Skillの再利用性**: 一度定義したSkillは複数のプロジェクト・タスクで使い回せる
3. **ワークフローの標準化**: SkillはSOP（標準作業手順）として機能し、チーム開発にも適している

Juejinの記事は62いいね・97スターを獲得し、開発者コミュニティでSkillへの関心が高いことを示している。

📎 出典: [Juejin — Prompt vs Skill](https://juejin.cn/post/7598433254128205864)（62いいね・97スター）`[Tier-1: 掘金/技術コミュニティ]`

### Cursor AI Skillsの実践例

Flutter開発において、CursorのSkills機能を使用してページ生成・コード作成・ドキュメント生成を自動化した事例が報告されている。これはSkillsが単なる概念ではなく、実際の開発ワークフローに組み込まれている証拠。

📎 出典: [Juejin — Cursor AI Skills実践](https://juejin.cn/post/7629863917262471203)（Cursor Skills Flutter自動化）`[Tier-2: 掘金/技術コミュニティ]`

### Zero Guideの発表

Juejinで**「Skills Guide Zero」**という記事が公開され、AI Agentのスキル設計に関する基本的な考え方が整理された。

## 関連リソース

- [[agent]] — AI Agent全体像
- [[claude]] — Skillsを積極活用しているLLM
- [[mcp]] — Model Context Protocol
