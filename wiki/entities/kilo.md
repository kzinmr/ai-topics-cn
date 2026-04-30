---
title: "Kilo（キロコード）— オープンソースAIコーディングプラットフォーム"
created: 2026-04-30
updated: 2026-04-30
tags: [coding-agents, open-source-ai, product, company, tooling]
aliases: ["Kilo Code", "kilocode", "KiloClaw", "Kilo Gateway"]
source_lang: en
---

# Kilo（Kilo Code Inc.）

| Field | Value |
|-------|-------|
| 社名 | Kilo Code Inc. |
| 設立 | 2025年3月 |
| CEO | Scott Breitenother（元Brooklyn Data創設者） |
| 共同創設者 | Sid Sijbrandij（GitLab共同創設者・元CEO） |
| 従業員 | 約34名 |
| 資金調達 | $8M シード（2025年12月、Cota Capitalリード / General Catalyst, Breakers, Quiet Capital, Tokyo Black参加） |
| 本社 | リモートファースト（サンフランシスコ・アムステルダム） |
| 開発者数 | 2.3M+ |
| トークン処理量 | 月間6兆トークン |
| ライセンス | MIT / Apache-2.0 |
| GitHub | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) |
| Webサイト | https://kilo.ai/ |

## 概要

Kiloは、2025年3月に設立された**オープンソースAIコーディングプラットフォーム**企業。Cline（VS Code用オープンソースAIコーディング拡張、500万+インストール）とRoo Codeをフォーク・統合し、**最も人気のあるオープンソースAIコーディングエージェント**として急成長。VS Code、JetBrains IDE、CLIに対応し、500+のAIモデルをゼロマークアップで利用可能。

「Kilo Speed」と呼ばれる哲学 — 高速に動いて毎日デプロイし、ユーザーの声に耳を傾ける — を掲げ、エンジニアが機能のエンドツーエンド所有（設計→実装→デバッグ→デプロイ→改善）をAIエージェントと共に行うワークフローを推進している。

## 主要プロダクト

### Kilo Code（コーディングエージェント）
VS Code / JetBrains / CLI向けAIコーディングエージェント。6つのエージェントモードを提供：
- **Code Mode** — 本番レディなコードの生成・リファクタリング
- **Architect Mode** — 複雑な機能の設計と構造化されたガイダンス
- **Debug Mode** — エラー読み取り、トレース、修正提案
- **Ask Mode** — 質問・探索モード
- **Custom Mode** — ユーザー定義モード
- **Orchestrator Mode** — タスクの並列実行・調整

**Kilo CLI**はOpenCodeのフォークで、CI/CDパイプラインでの自律実行に対応（`--auto`フラグでプロンプト確認なし実行可能）。

### KiloClaw（ホスト型OpenClawサービス）
2026年2月ローンチ。[[openclaw]]の完全マネージドホスティングサービス：
- 60秒でデプロイ完了（SSH不要、Docker不要、YAML不要）
- Fly.io製マルチテナントVMアーキテクチャによるエンタープライズグレードのセキュリティ
- 「3時クラッシュ問題」（ローカルNode.jsプロセスのサイレント停止）を自動監視・再起動で解決
- Kilo Gateway経由で500+モデル切り替え可能
- 新規ユーザーに7日間無料コンピュート提供
- ローンチ後2週間で3,500+開発者がウェイトリストに登録

### Kilo Gateway（モデルルーティング基盤）
60+プロバイダー、500+モデルへの統一アクセスポイント：
- Anthropic、OpenAI、Googleなどのリスト価格そのまま（ゼロマークアップ）
- BYOK（Bring Your Own Key）対応
- OpenRouter、Vercel、AWS Bedrock、Azure OpenAI等との統合
- 月間6兆トークン処理

### PinchBench
OpenClawワークフロー向けオープンソースベンチマーク：
- 23の実世界タスク（カレンダー管理、マルチソース調査、メール作成、ファイル整理等）でモデル評価
- [github.com/pinchbench/skill](https://github.com/pinchbench/skill)で公開

## 資金調達・成長

| 時期 | 出来事 |
|------|--------|
| 2025年3月 | 会社設立、Kilo Code開発開始 |
| 2025年12月 | $8Mシードラウンド完了（Cota Capitalリード） |
| 2026年2月 | KiloClaw GAローンチ |
| 2026年4月 | 開発者数2.3M+、GitHub Stars 18,600+、月間6兆トークン処理 |

## 経営哲学「Kilo Speed」

CEO Scott Breitenotherが提唱する開発哲学：
- エンジニアは機能のエンドツーエンド所有（設計→実装→デバッグ→デプロイ→改善）
- 拡張PRDレビューフェーズや承認待ちなしで即座に作業開始
- AIエージェント（Architect→Orchestrator→Code→Debug→Code Reviewer）を活用した高速開発サイクル
- 数週間で複数の大機能（Kilo Sessions、Code Reviewer、Cloud Agents、Kilo Man）を連続リリース

## Kilo vs 競合

| 比較軸 | Kilo Code | [[cursor]] | [[claude-code]] |
|--------|-----------|------------|-----------------|
| ライセンス | MIT/Apache-2.0（OSS） | 独自（クローズド） | Anthropic製 |
| モデル選択 | 500+（ゼロマークアップ） | 制限あり | Claudeのみ |
| IDE対応 | VS Code/JetBrains/CLI | VS Code系 | CLI/ターミナル |
| エージェントモード | 6種類 | 複数 | 単一 |
| ホスティング | KiloClaw（Fly.io） | Cursor Cloud | 自前 |
| 月間トークン | 6兆 | 非公開 | 非公開 |

## 関連

- [[openclaw]] — KiloClawのベースとなったOSSパーソナルAIエージェント
- [[cursor]] — 競合AIコードエディタ
- [[claude-code]] — 競合AIコーディングエージェント
- [[coding-agents]] — コーディングエージェントエコシステム全体

## ソース

- https://kilo.ai/ — 公式サイト
- https://kilo.ai/about — 会社情報・Kilo Speed哲学
- https://github.com/Kilo-Org/kilocode — GitHubリポジトリ（18,600+ Stars、430貢献者）
- https://www.venturebeat.com/orchestration/kilo-launches-kiloclaw-allowing-anyone-to-deploy-hosted-openclaw-agents-into — KiloClawローンチ記事
- https://blog.kilo.ai/p/kiloclaw-hosted-openclaw — KiloClaw GAアナウンス
- https://www.openaitoolshub.org/en/blog/kilo-code-review — Kilo Codeレビュー記事
- https://kilocode.ai/pricing — 価格情報
