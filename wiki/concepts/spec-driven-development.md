---
title: Spec-Driven Development — 実践における課題
created: 2026-05-02
updated: 2026-05-02
tags: [sdd, harness, openspec, developer-experience]
aliases: ["SDD", "仕様駆動開発", "Spec-Driven", "Harness Engineering"]
source_lang: zh-CN
---

# Spec-Driven Development — 実践における課題

## 概要

Spec-Driven Development（SDD）は、AIコーディングエージェントが仕様書（Spec）に基づいて開発を進めるパラダイム。OpenAIが提唱する[[claude-code|Harness Engineering]]や、オープンソースのOpenSpecなどが代表的な実装である。しかし2026年4月〜5月のV2EXコミュニティでは、実践における複数の課題が報告されている。

## 主要課題

### 1. 「正しい废话」問題

OpenSpecが生成するdesign/proposalの多くが「正しい废话」（当たり前のことを述べているだけで実質的価値がない）であり、レビューが困難。重点を見極めるのが難しいという声が上がっている。

> 「openspec 会自己生成一堆 design & proposal，很多都是正确的废话，给人 Review 就很困难，找不到重点」
> — V2EXユーザー、大プロジェクトでのSDD実践経験者

### 2. Specとコードの乖離

生成されたSpecにバグ修正の内容を書き戻す運用が「tricky」（巧妙すぎる）との指摘。AI固有の問題を人間用のドキュメントに書くことへの違和感が報告されている。

### 3. プロセス遵守のコスト

Specの流程に厳密に従う（Task実行など）必要があり、バグ修正を含めた総時間が「Planning機能 + 少量のヒント修正」よりも長くなるケースがある。

### 4. Spec合併のdelta不一致

Specのdelta（差分）が合併時に不一致になる問題が報告されている。

### 5. Codexリポジトリとの矛盾

OpenAIのHarness Engineeringドキュメントでは「Spec & Planning & Tasksの進捗をgitリポジトリに入れる」とされているが、実際のCodexリポジトリには这些东西がなく、多くのSpecはIssueで議論されている。

## 実践パターンの比較

| パターン | 特徴 | 課題 |
|----------|------|------|
| OpenSpec | Spec自動生成、Proposalベース | 正しい废话、delta不一致 |
| Harness | OpenAI公式、git連動 | リポジトリとドキュメントの乖離 |
| Planning+ヒント | 軽量、柔軟 | ドキュメント管理が手動 |

## 開発者の声

- 「実行後も还是有些 Bug、这种再写回到 Spec 让他修复感觉很 tricky」
- 「明明是 AI 特定问题，结果却要写到给人看的文档中」
- 「加上 Bug 修复。总时间感觉不如用 Planning 功能，再加少量提示词修正顺手」

## 出典

| ソース | URL | スコア | ティア |
|--------|-----|--------|--------|
| V2EX — SDD実践議論 | https://www.v2ex.com/t/1208418 | 39 | T1 |
| OpenAI Harness | https://openai.com/zh-Hans-CN/index/harness-engineering/ | - | T1 |

## 関連ページ

- [[claude-code]] — AIコーディングエージェント
- [[ai-coding-reality]] — AIコーディングの実際
