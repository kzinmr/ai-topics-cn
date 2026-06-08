---
title: "Agentic Engineering（エージェントエンジニアリング）— 第2世代AI開発パラダイム"
type: concept
tags: [ai-agent, software-engineering, agentic-engineering, paradigm-shift, vibe-coding, harness]
created: 2026-05-26
updated: 2026-06-08
source_lang: zh-CN
---

# Agentic Engineering（エージェントエンジニアリング）

> **概念定義**: AIエージェントによる自律的ソフトウェア開発・運用の体系的アプローチ
> **重要度**: 高 — Vibe Codingの次の進化段階、2026年業界主要トレンド

| 区分 | Vibe Coding（第1世代） | Agentic Engineering（第2世代） |
|------|----------------------|-------------------------------|
| 開発者役割 | プロンプト記入者 | エージェント監督者 |
| 自律性 | 低（都度対話） | 高（長時間自律実行） |
| 品質管理 | 事後確認 | プロセス内蔵（Harness/検証） |
| 対象タスク | 単純コード生成 | 複合ワークフロー・デプロイ |
| 代表製品 | Cursor/ChatGPT | Claude Code/Codex/DeepSeek Harness |

## 概要

Agentic Engineeringは、2026年半ばに台頭した第2世代AI開発パラダイム。**Vibe Coding**（氛围编程）が「AIに話しかけてコードを生成する」という受動的モデルだったのに対し、Agentic Engineeringは「AIエージェントが自律的にタスクを分解・実行・検証し、人間は監督と方向づけに集中する」という能動的モデルへの転換を意味する。

この概念は複数の情報源から同時に現れている：
- **36kr**: Vibe CodingからAgentic Engineeringへの移行を「必然的進化」と位置づけ
- **Simon Willison**: Agentic EngineeringをVibe Codingの次の段階として提唱
- **Ahmed E. Hassan（SE 3.0）**: Software Agent Software Engineeringの体系化
- **DeepSeek Harnessチーム**: `Model + Harness = Agent` として実装層で具体化

## SE 3.0 — Software Agent Software Engineering

カーネギーメロン大学Ahmed E. Hassan教授が提唱する**SE 3.0（第3世代ソフトウェアエンジニアリング）**は、Agentic Engineeringの学術的基礎となるフレームワーク。

### 3層構造
1. **ACE（Agent Coordination Engine）**: 複数エージェントのタスク配分・協調
2. **AEE（Agent Execution Environment）**: 個々のエージェントが動作するサンドボックス環境
3. **BriefingScripts/MentorScripts/MRP/CRP**: 人間→エージェントへの指示体系

### SEの世代区分
| 世代 | 時期 | 特徴 |
|------|------|------|
| SE 1.0 | 2000s-2010s | 人間中心の設計・実装・テスト |
| SE 2.0 | 2020-2025 | AI支援（Copilot/補完） |
| SE 3.0 | 2026〜 | AI自律実行、人間は監督・検証 |

## Tony Bai「From Vibe-Coding to Agentic Engineering」

中国の著名テックブロガーTony Baiは2026年5月2日、Vibe CodingからAgentic Engineeringへの移行を論じ、**7つの生存ルール**を提唱：

1. **理解なきコードは技術負債**: AIが生成したコードを理解せずにマージするな
2. **境界線を持つ**: AIに任せられるタスクと人間が手がけるタスクを明確にせよ
3. **検証は人間の仕事**: AIの出力は常にレビュー・テストせよ
4. **プロンプトより仕様**: 明確な仕様書がAIへの最良の指示である
5. **Harnessで制御**: 自由生成を制約・検証・収束するエンジニアリング層が必要
6. **継続的学習**: AI技術の進化に追いつき、判断基準を更新し続けよ
7. **責任は人間**: AIの出力に対する最終責任は開発者にある

## DeepSeek Harness — Model + Harness = Agent

2026年5月20日、**DeepSeek**がAgent Harnessチームの採用を開始。これは単なるClaude Code競合ではなく、より深い意味を持つ：

- **Harness（制御枠組み）**: モデルの自由生成を制約・検証・修正・収束させるエンジニアリング層
- **Model + Harness = Agent**: 基礎モデルだけではAgentにならない。コンテキスト管理、ツール呼び出し、ファイル読み書き、端末実行、テストフィードバック、エラー訂正・収束の全サイクルを統合して初めてAgentとなる
- **サードパーティラッパーの限界**: モデルとエンジニアリング環境が分断されているため、コンパイルエラー発生時にモデルはランタイムコンテキストを持たず推測するしかない
- **DeepSeekのアプローチ**: コンパイラログ、lintフィードバック、テスト結果、ランタイムシグナルをすべてモデル最適化に直接フィードバックする閉ループを自社で構築

製品完成まで**6〜12ヶ月**と予測され、500億人民元調達と連動した**商業化加速の第一弾**と位置付けられている。

## 業界構造の変化

### エージェント三巨頭サミット（2026年5月18日）
智譜AutoGLM 3.0 + Qwen Agent v2 + DeepSeek R2が同時に発表され、中国AI業界が「モデル競争」から「エージェント競争」へ移行したことを象徴。

### 価格階層とエージェントアーキテクチャ
- **DeepSeek V4-Flash**: ¥0.28/百万tokens出力 — 単純Agentタスクに最適
- **DeepSeek V4-Pro**: ¥3.48/百万tokens出力 — 複雑推論・高度Agent
- **GPT-5.5**: $30/百万tokens出力 — 最先端Agentic Coding
- **階層型Agent**: 高価格モデルで計画→低価格モデルで実行という2層アーキテクチャが一般化

## Vibe Codingからの移行

中国コミュニティでは2026年5月時点で、Vibe CodingからAgentic Engineeringへの移行が「不可避」とのコンセンサスが形成されつつある：

- **通義灵码**: SE 3.0対応を予告（2026年5月）
- **36kr分析**: 「氛围编程の時代は終わった。これからはエージェントが主役」
- **コミュニティ反響**: 開発者間でHarness Engineeringの重要性が急速に認知

## 課題と限界

1. **認知債務（Cognitive Debt）**: AI生成コードの理解不足が長期的な保守コストに
2. **品質保証**: 自律実行の結果をどう検証するか — 形式的検証（Lean等）との連携が課題
3. **セキュリティ**: Agentにファイルシステム・ネットワーク・APIへのアクセスを許容するリスク
4. **経済性**: 推論コストが高騰（Deloitte: AI総需要の2/3が推論）し、GPU逼迫

## 関連

- [[vibe-coding]] — 第1世代AI開発（前段階）
- [[vibe-coding-china]] — 中国でのVibe Coding受容とAgentic Engineeringへの進化
- [[harness-engineering]] — Harnessパターン詳細
- [[concepts/deepseek]] — DeepSeek Harnessチーム採用情報
- [[claude-code]] — Agentic Engineeringの代表製品
- [[coding-plan]] — AIコーディングサブスクリプション

## 出典

- [36kr — 氛围编程到Agentic Engineering](https://36kr.com/p/3770223251866372) [T1]
- [Tony Bai — From Vibe-Coding to Agentic Engineering](https://tonybai.com) [T2]
- [Zhihu Frontier Weekly — AI Reasoning, Agents, and Infrastructure Race](https://substack.com/@zhihufrontier) [T2]
- [知乎 — DeepSeek Harnessチーム分析](https://www.zhihu.com/question/2040450519303288568) [T2]
- [知乎 — SE 3.0議論](https://www.zhihu.com/question/2038213982293579409) [T2]
