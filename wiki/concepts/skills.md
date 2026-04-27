---
title: Skills — AI Agentの能力モジュール
description: AI Agentにおけるスキルの概念、実装方法、中国エコシステムでの標準化動向。
status: active
category: concept
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

### Zero Guideの発表

Juejinで**「Skills Guide Zero」**という記事が公開され、AI Agentのスキル設計に関する基本的な考え方が整理された。

## 関連リソース

- [[agent]] — AI Agent全体像
- [[claude]] — Skillsを積極活用しているLLM
- [[mcp]] — Model Context Protocol
