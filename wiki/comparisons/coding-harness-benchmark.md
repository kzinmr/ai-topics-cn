---
title: "AI Coding Harness & Model Compatibility Benchmark"
created: 2026-05-01
updated: 2026-05-01
tags: [comparison, coding-agents, harness, benchmark, llm, model-compatibility]
aliases: ["ハーネス比較", "AIコーディングツール比較", "coding-harness-benchmark", "agent-harness-comparison"]
source_lang: en
---

# AI Coding Harness & Model Compatibility Benchmark

> **比較対象**: [[claude-code]], Cursor, OpenCode, Codex CLI, [[openclaw]], [[harness-engineering]], Kilo Code, Aider, Gemini CLI
> **出典**: Sigmabench, OpenAIToolsHub, ZBuild, ComputingForGeeks, Sanj.dev, LearnAIForge, NivaaLabs, 36kr, Juejin
> **重要度**: 高 — 2026年5月時点のAIコーディングハーネス総決算

## 概要

2026年5月現在、AIコーディングハーネス（エージェント型開発ツール）は**ターミナル型**、**IDE統合型**、**ハイブリッド型**の3つのカテゴリに分化している。本ページは主要ハーネスの性能、モデル互換性、コスト効率、実務適用性を比較し、「結局どのモデルをどのハーネスで使えばいいのか」に答える。

---

## ハーネス分類と特徴

| タイプ | ツール | 設計思想 | 特徴 |
|--------|--------|---------|------|
| **ターミナル型** | Claude Code | エージェント自律実行 | ターミナルで完結、高い自律性 |
| **ターミナル型** | OpenCode | プロバイダー中立 | OSS、75+モデル対応、TUI |
| **ターミナル型** | Codex CLI | OpenAIネイティブ | ChatGPTサブスクで利用可能 |
| **ターミナル型** | Aider | Gitネイティブ | 変更ごとにコミット、安全性重視 |
| **ターミナル型** | Gemini CLI | Google無料枠 | 無料、1Mコンテキスト |
| **ターミナル型** | Goose | プランニングファースト | レシピ機能、アーキテクチャ重視 |
| **IDE統合型** | Cursor | IDEファースト | VS Codeフォーク、視覚的編集 |
| **IDE統合型** | Kilo Code | オープンソースIDE | Cline/Roo Code系、500+モデル |
| **ハイブリッド型** | OpenClaw | 並列エンドポイント | MCPベース、マルチツール同時実行 |
| **ハイブリッド型** | Hermes Agent | 長期記憶・自己進化 | スキル管理、cron統合、メモリ |

---

## ベンチマーク性能比較

### SWE-bench Verified（実世界バグ修正）

| ハーネス + モデル | スコア | 出典 |
|---|---|---|
| **Claude Code + Claude Opus 4.6** | **80.8%** | Sigmabench / LearnAIForge |
| **Cursor + Gemini 3.1 Pro** | 80.6% | LearnAIForge |
| Codex CLI + GPT-5.2 Codex | 80.0% | Sigmabench |
| Cursor (Composer 2 multilingual) | 73.7% | LearnAIForge |
| MiniMax M2.5 | 80.2% | Sigmabench |
| GLM-5 | 77.8% | AwesomeAgents |
| DeepSeek V3.2-Speciale | 77.8% | AwesomeAgents |
| Claude Sonnet 4.5 | 72.1% | solvedbycode.ai |
| Grok Code Fast 1 | 70.8% | solvedbycode.ai |

### Terminal-Bench（自律ターミナル操作）

| ハーネス + モデル | スコア | 出典 |
|---|---|---|
| **Cursor Composer 2** | **61.7%** | 36kr |
| Codex CLI + GPT-5.3-Codex | 61.5% | AwesomeAgents |
| Claude Code + Claude Opus 4.6 | 58.3% | AwesomeAgents |
| Claude Opus 4.5 | 55.2% | AwesomeAgents |
| GPT-5.2 Pro | 54.1% | AwesomeAgents |
| Gemini 3 Pro | 50.3% | AwesomeAgents |

### LiveCodeBench V6（競技プログラミング）

| モデル | スコア | 出典 |
|---|---|---|
| **GLM-4.7** | **84.9** | solvedbycode.ai |
| Claude Sonnet 4.5 | 83.2 | solvedbycode.ai |
| Big Pickle | 82.8 | solvedbycode.ai |
| Grok Code Fast 1 | 81.4 | solvedbycode.ai |

### τ²-Bench（多ターンエージェント性能）

| モデル | 標準 | 思考保持あり | 出典 |
|---|---|---|---|
| GLM-4.7 | 74.5% | **87.4%** | solvedbycode.ai |
| Claude Sonnet 4.5 | **76.2%** | — | solvedbycode.ai |
| Grok Code Fast 1 | 71.3% | — | solvedbycode.ai |

---

## 実世界タスク性能（Code With Seb 独自ベンチマーク）

同じ5つのタスクを3ツールで実行。トークン数・壁時計時間・再作業率を計測。

### リネームリファクタ

| ツール | トークン | 時間 | 再作業率 |
|---|---|---|---|
| **Claude Code** | **33K** | 47秒 | **0%** |
| Cursor | 180K | 52秒 | 0% |
| Codex | 95K | 4分12秒 | 0% |

### デバッグ

| ツール | トークン | 時間 | 再作業率 |
|---|---|---|---|
| **Claude Code** | **78K** | 6分31秒 | **0%** |
| Cursor | 420K | 8分02秒 | 20% |
| Codex | 112K | 9分44秒 | 50% |

### 新機能実装

| ツール | トークン | 時間 | 再作業率 |
|---|---|---|---|
| Cursor | 310K | **6分47秒** | 30% |
| Claude Code | 94K | 8分15秒 | 10% |
| Codex | 180K | 14分20秒 | 10% |

### テスト生成

| ツール | トークン | 時間 | 品質 |
|---|---|---|---|
| Claude Code | 145K | 11分40秒 | **高** |
| Cursor | 580K | 9分12秒 | 中 |
| Codex | 220K | 16分55秒 | 高 |

### アーキテクチャレビュー

| ツール | トークン | 時間 | 品質 |
|---|---|---|---|
| **Claude Code** | **58K** | 4分10秒 | **高** |
| Cursor | 88K | 3分45秒 | 中 |
| Codex | 104K | 7分20秒 | 高 |

> **結論**: Claude Codeは**トークン効率が5.5倍**高く、再作業率が最も低い。Cursorは**速度**に優れるがトークン消費が多い。Codexは非同期実行に向くが遅い。

---

## モデル互換性比較

| ハーネス | 対応モデル | プロバイダー数 | ローカルモデル | BYOK |
|---|---|---|---|---|
| **OpenCode** | Claude, GPT, Gemini, Grok, Qwen, MiniMax, GLM等 | **75+** | ✅ Ollama | ✅ |
| **Kilo Code** | 500+モデル | 60+ | ✅ | ✅ |
| **Cursor** | Claude, GPT, Gemini, 自社モデル | 制限あり | ❌ | ⚠️ 制限付き |
| **Aider** | OpenAI互換API全般 | 75+ | ✅ Ollama | ✅ |
| **Claude Code** | **Claudeのみ** | 1 | ❌ | ✅ APIキー |
| **Codex CLI** | **OpenAI GPT-5系のみ** | 1 | ❌ | ❌ サブスク |
| **Gemini CLI** | **Geminiのみ** | 1 | ❌ | ❌ |
| **Goose** | 複数 | 制限あり | ✅ | ✅ |
| **OpenClaw** | 複数（MCP経由） | MCP次第 | ❌ | ✅ |
| **Hermes Agent** | 複数（スキル経由） | 設定次第 | ❌ | ✅ |

---

## Sigmabench エージェント比較（OpenCode vs 各CLI）

### OpenCode + Kimi K2.5 vs Claude Code + Opus 4.5

| 指標 | OpenCode (K2.5) | Claude Code (Opus 4.5) | 差 |
|---|---|---|---|
| Sigmascore | 32.7% | 32.0% | ± |
| Accuracy | Tier 4 | **Tier 2** | Opusが上 |
| Consistency | Tier 4 | **Tier 2** | Opusが上 |
| Speed | **Tier 3** | Tier 5 | K2.5が22%速い |
| 推論コスト | **88%安い** | 高 | K2.5が圧倒的 |

### OpenCode + GPT-5.2 Codex vs Codex CLI

| 指標 | OpenCode | Codex CLI | 差 |
|---|---|---|---|
| Accuracy | 統計的同等 | 統計的同等 | — |
| Consistency | Tier 7 | **Tier 6** | Codexがやや上 |
| Speed | 474秒 | **420秒** | Codexが13%速い |
| Sigmascore | Tier 7 | **Tier 6** | Codexが上 |

### OpenCode + Gemini 3 Flash vs Gemini CLI

| 指標 | OpenCode | Gemini CLI | 差 |
|---|---|---|---|
| Sigmascore | **Tier 2** | Tier 3 | OpenCodeが上 |
| Accuracy | **上** | 下 | OpenCodeが上 |
| Speed | **31%速い** | 遅い | OpenCodeが上 |

---

## トークン効率とコスト比較

### ベンチマークタスク1回あたりのトークン消費

| ツール | トークン数 | 効率比 |
|---|---|---|
| **Claude Code** | **~33,000** | **1x（基準）** |
| Codex | ~95,000 | 2.9x |
| Cursor | ~181,000 | 5.5x |

### APIコスト見積もり（OpenCode経由、1セッションあたり）

| セッション種別 | Claude Sonnet 4.5 | GPT-5.4 | DeepSeek-V3 |
|---|---|---|---|
| 30分探索的 | $0.40 | $0.35 | $0.03 |
| 1時間機能実装 | $1.80 | $1.60 | $0.14 |
| 大規模リファクタ | $4.20 | $3.80 | $0.35 |
| 月間（日4h使用） | $180–250 | $160–220 | **$12–20** |

### サブスクリプション比較

| ツール | 無料枠 | 最安プラン | 最高プラン |
|---|---|---|---|
| OpenCode | **✅ フル機能+無料モデル** | $0（APIのみ） | — |
| Claude Code | ❌ 制限付き | $20/月（Pro） | $200/月（Enterprise） |
| Cursor | 2,000補完 | $20/月（Pro） | $200/月（Ultra） |
| Kilo Code | **✅ OSS（MIT）** | $0（APIのみ） | KiloClawホスティング |
| Aider | **✅ フル機能** | $0（APIのみ） | — |
| Gemini CLI | **✅ 無料** | $0 | — |

---

## OpenCode vs Claude Code 実タスク比較（OpenAIToolsHub 2026年2-3月）

| タスクカテゴリ | Claude Code（ネイティブ） | OpenCode + Sonnet 4.6 | OpenCode + Gemini 3.1 Pro |
|---|---|---|---|
| マルチファイルリファクタ（10件） | **8/10 (80%)** | 7/10 (70%) | 7/10 (70%) |
| バグ修正（15件） | **12/15 (80%)** | 11/15 (73%) | 11/15 (73%) |
| 機能実装（8件） | **7/8 (88%)** | 6/8 (75%) | 6/8 (75%) |
| テスト生成（5件） | 4/5 (80%) | 4/5 (80%) | **5/5 (100%)** |
| **合計（38件）** | **31/38 (82%)** | 28/38 (74%) | 29/38 (76%) |

> **示唆**: Claude Codeは同じモデル（Sonnet 4.6）でもOpenCodeより**8ポイント高い**。これはAnthropicがClaude Code専用にシステムプロンプトとエージェントループを最適化しているため。

---

## OpenCode vs Aider（sanj.dev 2026年3月）

| 特徴 | Aider | OpenCode |
|---|---|---|
| 価格 | APIキーのみ | APIキー + サブスク連携可 |
| Git統合 | **最上位（自動コミット）** | 上位（手動コミット） |
| プロバイダー | 75+（OpenAI互換） | **75+（Models.dev）** |
| 自律性 | ペアプログラマー（段階的編集） | **ビルドエージェント（フル自動化）** |
| MCP | ❌ | ✅ |
| GitHub Stars | 42K | **131K** |
| 最適用途 | Git安全・レビュー可能な変更 | マルチファイル足場・高速反復 |

---

## ハーネス × モデル 最適組み合わせ

### 用途別おすすめ

| 用途 | おすすめハーネス | おすすめモデル | 理由 |
|------|----------------|---------------|------|
| **最高品質・複雑なデバッグ** | Claude Code | Claude Opus 4.6 | SWE-bench 80.8%、再作業率0% |
| **IDE統合・視覚的編集** | Cursor | Claude Opus 4.6 / Gemini 3.1 Pro | 低学習コスト、Composer機能 |
| **コスト最適・日常タスク** | OpenCode | DeepSeek-V3 / Kimi K2.5 | 月額$12-20、十分な性能 |
| **モデル中立・柔軟性** | OpenCode / Aider | GLM-4.7 / Gemini 3.1 Pro | 75+プロバイダー、ロックインなし |
| **Git安全性重視** | Aider | Claude Sonnet 4.5 | 自動コミット、取り消し可能 |
| **無料・入門** | Gemini CLI | Gemini 3 Flash | 1Mコンテキスト、無料 |
| **非同期・バッチ処理** | Codex CLI | GPT-5.3-Codex | バックグラウンド実行 |
| **アーキテクチャ設計** | Goose / Claude Code | Claude Opus 4.6 | プランニング重視 |
| **並列ツールチェーン** | OpenClaw | Kimi K2.5 / GLM-4.7 | マルチエンドポイント同時実行 |
| **長期記憶・cron自動化** | Hermes Agent | 設定次第 | スキル統合、定期実行 |

### 中国モデル特化（OpenCode経由）

| モデル | プロバイダー | LiveCodeBench | SWE-bench | 1セッションコスト | 最適ハーネス |
|---|---|---|---|---|---|
| **GLM-4.7** | Zhipu AI | **84.9** | 73.8% | 無料（期間限定） | OpenCode |
| **Kimi K2.5** | Moonshot AI | — | — | 低 | OpenCode / Claude Code |
| **MiniMax M2.5** | MiniMax | — | 80.2% | 低 | OpenCode |
| **Qwen 3.5** | Alibaba | 54.8 | 62.5% | 低 | OpenCode |
| **DeepSeek V3.2** | DeepSeek | 62.3 | 77.8% | **$0.03/セッション** | OpenCode |

---

## 中国コミュニティでの実評価

### ハーネス採用パターン（2026年4月調査）

| パターン | 説明 | 割合 |
|---|---|---|
| **Claude Code + Cursor併用** | IDE日常 + ターミナル複雑タスク | 多数派 |
| **OpenCode + 国産モデル** | コスト最適・検閲回避 | 急増中 |
| **Aider単体** | Git安全性重視・個人開発者 | 安定 |
| **OpenClaw + 阿里云** | 並列実行・GPUリソース活用 | 新興 |

### 課題と注意点

- **Claude Code**: 2026年1月以降、OAuth認証がブロックされAPIキー必須に。ProサブスクからClaude Codeへのアクセス制限も発生
- **Cursor**: 1Mコンテキスト非対応、トークン消費がClaude Codeの5.5倍
- **OpenCode**: Anthropic OAuthブロック（2026年1月）、RCE脆弱性の歴史、長期セッションでのメモリ肥大（TypeScript LSP使用時1.2GB）
- **Codex CLI**: UXの問題、エラーハンドリングの未成熟
- **OpenClaw**: 12カテゴリのセキュリティ脆弱性報告、MCPプロトコルの権限管理問題

---

## 結論：結局どれを使えばいいのか？

### 3つの正解

1. **「最高性能」を求めるなら → Claude Code + Opus 4.6**
   - SWE-bench 80.8%、トークン効率5.5倍、再作業率最低
   - 月額$20-200だが、プロ開発者の時間コストを考慮すれば元は取れる

2. **「コスト×柔軟性」を求めるなら → OpenCode + DeepSeek-V3 / Kimi K2.5**
   - 月額$12-20、75+プロバイダー、OSS
   - Claude Codeより8ポイント低いが必要な場面では十分

3. **「IDE統合×日常作業」を求めるなら → Cursor**
   - 最も低い学習コスト、視覚的編集、チームコラボ
   - トークン消費は多いがUI/UXは最高

### ハイブリッド戦略（プロ開発者の最適解）

> **Cursorで日常コーディング + Claude Codeで複雑タスク + OpenCodeでバッチ処理**

この3層アプローチが2026年5月時点で最も生産性が高いと複数の独立レビューで報告されている。

---

## 関連リンク

### 内部リンク
- [[claude-code]] — Anthropicのターミナルエージェント
- [[cursor]] — IDE統合型AIコーディングツール
- [[openclaw]] — MCPベースの並列エージェント
- [[harness-engineering]] — ハーネスエンジニアリング概論
- [[kimi-moonshot]] — Kimi K2.5モデル
- [[glm-zhipu]] — GLM-4.7/5モデル
- [[minimax]] — MiniMax M2.5/M2.7モデル
- [[qwen]] — Qwen 3.5モデル

### 外部ソース
| ソース | URL | ティア |
|---|---|---|
| Sigmabench — OpenCode vs Kimi K2.5 | [sigmabench.com](https://sigmabench.com/blog/opencode-kimi-k-2-5-open-source-open-weight-agentic-coding-is-here/) | T1 |
| Sigmabench — OpenCode vs Codex CLI | [sigmabench.com](https://sigmabench.com/blog/opencode-vs-codex-cli-on-gpt-5-1-codex-mini-and-5-2-codex/) | T1 |
| OpenAIToolsHub — OpenCode Review | [openaitoolshub.org](https://www.openaitoolshub.org/en/blog/opencode-review-terminal-ai-coding) | T1 |
| OpenAIToolsHub — OpenCode vs Claude Code | [openaitoolshub.org](https://www.openaitoolshub.org/en/blog/opencode-vs-claude-code) | T1 |
| ZBuild — OpenCode vs Claude Code vs Cursor | [zbuild.io](https://www.zbuild.io/resources/news/opencode-vs-claude-code-vs-cursor-2026) | T1 |
| ComputingForGeeks — 3ツール比較 | [computingforgeeks.com](https://computingforgeeks.com/opencode-vs-claude-code-vs-cursor/) | T1 |
| Code With Seb — 実タスク比較 | [codewithseb.com](https://www.codewithseb.com/blog/claude-code-vs-cursor-vs-codex-honest-developer-comparison-2026) | T2 |
| Sanj.dev — CLIショーダウン | [sanj.dev](https://sanj.dev/post/comparing-ai-cli-coding-assistants/) | T2 |
| NivaaLabs — Claude Code vs OpenCode | [nivaalabs.com](https://nivaalabs.com/claude-code-vs-opencode-in-2026-is-the-free-open-source-alternative-worth-it-for-developers/) | T2 |
| solvedbycode.ai — OpenCode Benchmark | [solvedbycode.ai](https://solvedbycode.ai/blog/opencode-benchmark-review-january-2026) | T2 |
| AwesomeAgents — Coding Leaderboard | [awesomeagents.ai](https://awesomeagents.ai/leaderboards/coding-benchmarks-leaderboard) | T2 |
| LearnAIForge — Best Tools 2026 | [learnaiforge.com](https://www.learnaiforge.com/articles/best-ai-coding-tools-2026) | T1 |
