---
title: "Soul Killer — Claude Code用Galgame Agent & Skill作成器"
created: 2026-04-18
updated: 2026-04-18
tags: [ai-agents, coding-agents, tooling, open-source-ai, media]
aliases: ["灵魂杀手", "Galgame Agent", "Claude Code Skill"]
source_lang: zh-CN
---

# Soul Killer — Claude Code用Galgame Agent & Skill作成器

Claude Codeのスキルシステムを活用し、Galgame（美少女ゲーム）の自動生成・実行を可能にするオープンソースAgent。REPLバイナリを提供し、インターネット資料からキャラクター・世界観・シナリオを生成する。

## 概要

開発者: DouglasDong（Xeonice）  
GitHub: [Xeonice/soul-killer](https://github.com/Xeonice/soul-killer)

14日間の開発期間。《同事 Skill》（同僚スキル）とPPTX生成Agentの経験に触発され、Claude CodeのSkillフォーマットでGalgameを自動生成するプロジェクト。

## 機能

### 1. REPL バイナリ

ユーザーがインストール後、以下のスタックで動作：
- **モデル**: OpenRouter経由のLLM
- **検索エンジン**: Exa.ai / Tavily
- **役割**: インターネット資料からSoul（人物）、World（世界書）を自動作成

### 2. Soul（人物） + World（世界書）

- インターネット検索でキャラクターの性格・背景・関係を構築
- 世界観設定（時代背景・舞台・ルール）を自動生成
- 両者を組み合わせてシナリオ生成の基盤とする

### 3. Galgame Skill 生成

- Soul + World から対応するプロットのGalgame Skillを生成
- Skill実行でゲーム起動
- 初回起動時はシナリオをリアルタイム生成

### 4. ゲーム機能

- セーブ・ロード対応
- 分岐ルート表示
- シナリオキャッシュ
- ユーザーの選択肢でゲーム進行
- マルチエンディング・マルチブランチ対応

## インスピレーション源

- [同事 Skill（colleague-skill）](https://github.com/titanwings/colleague-skill) — Claude Code Skillの実例
- [pptx-openxml-renderer](https://pptx-openxml-renderer.vercel.app/) — PPTX生成Agent
- 開発者のGalgame制作経験

## Claude Code Skillsエコシステムとの関係

このプロジェクトは、Claude Codeの**Skillシステム**が単なる開発支援ツールを超えて、エンターテインメントコンテンツ生成にも応用可能であることを示す好例。

- [[agent-skills]] — Agentのモジュール化スキル
- [[claude-code]] — Claude Codeプラットフォーム

## 出典

- [V2EX: Claude Code 也能玩 Galgame —— 灵魂杀手 Agent 及 skill 创建器](https://www.v2ex.com/t/1206215) — DouglasDong (2026-04-15)
- [GitHub: Xeonice/soul-killer](https://github.com/Xeonice/soul-killer)
