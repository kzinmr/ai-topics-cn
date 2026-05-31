---
title: OpenClaw — オープンソースAIエージェント
created: 2026-05-02
updated: 2026-05-31
tags: [concept, agent, open-source, openclaw, china]
aliases: ["OpenClaw", "open-claw", "オープンクロー"]
source_lang: zh-CN
---

# OpenClaw — オープンソースAIエージェント

## 概要

OpenClawは、2026年4〜5月に中国で急成長したオープンソースAIエージェントプロジェクト。Juejinで「阿里出手了！终于不怕OpenClaw烧token啦、直接算力自由〜」と報道され、個人開発者から注目されている。

## 特徴

### トークン効率最適化

- 阿里（Alibaba）がOpenClawのトークン消費問題に対処
- 「算力自由」（計算リソースの自由な利用）を実現するアプローチ
- 個人開発者にとって実用的なコストパフォーマンス

### 自動投稿機能

- Juejinでは「用OpenClaw实现小红书自动发帖」が報告
- 小红书（Xiaohongshu/RED）への自動コンテンツ投稿
- MCP（Model Context Protocol）との統合により、プラットフォーム横断的な自動化が可能

### コミュニティ評価

- V2EXで「OpenClaw, Hermes, Mercury或其他，哪个个人Agent能真正投入使用？」と議論
- 個人Agentの実用性比較で常に名前が挙がる
- 376k+ Starを獲得（GitHub v2026.5.28時点で376K）

## 競合エージェントとの比較

| エージェント | 特徴 | 開発元 |
|---|---|---|
| OpenClaw | オープンソース、トークン効率 | コミュニティ |
| Claude Code | 高品質、MCP統合 | Anthropic |
| Hermes | 多機能、スキルシステム | Nous Research |
| Mercury | 軽量、高速 | 不明 |
| Codex | OpenAI純正、電話認証必須 | OpenAI |

## 業界への影響

- 個人Agentの実用化が加速
- オープンソースAgentと商用Agentの競争が激化
- 「Agentは最終的にデータベース問題」という批判に対し、OpenClawは実務重視のアプローチで応える

> **出典**: Juejin — [阿里出手了！终于不怕OpenClaw烧token啦](https://juejin.cn/post/7610637031321698330) [T1]
> **出典**: Juejin — [用OpenClaw实现小红书自动发帖](https://juejin.cn/post/7615379311402467354) [T1]
> **出典**: V2EX — [OpenClaw, Hermes, Mercury或其他](https://www.v2ex.com/t/1209907) [T2]

## 関連リンク

### 内部リンク

- [[agent-skills]] — Agentのスキル機能
- [[mcp]] — Model Context Protocol
- [[china-coding-agents]] — 中国のコーディングエージェント
- [[claude]] — Claudeモデル
- [[hermes-agent]] — Hermes Agent

### 外部ソース

| ソース | URL | ティア | 概要 |
|---|---|---|---|
| Juejin — OpenClaw烧token | [juejin.cn/post/7610637031321698330](https://juejin.cn/post/7610637031321698330) | T1 | 阿里の最適化 |
| Juejin — OpenClaw小红书 | [juejin.cn/post/7615379311402467354](https://juejin.cn/post/7615379311402467354) | T1 | 自動投稿機能 |
| V2EX — Agent比較 | [v2ex.com/t/1209907](https://www.v2ex.com/t/1209907) | T2 | 実用性議論 |

## 2026年5月下旬最新動向

### ▼ v2026.5.28 リリース: 376K Stars、マルチプロバイダー対応とAgentランタイム改善（5月30日）

OpenClawはGitHubで376K Starを記録。v2026.5.28リリースで以下を対応:

- **マルチプロバイダー対応拡大**: Claude Opus 4.8、Fal Krea画像生成、NVIDIAモデルカタログ、MiniMaxストリーミング音楽、音声モデルカタログ
- **Codex/エージェント改善**: サブエージェントのcwd/workspace分離強化、セッションロックのタイムアウト解放、フックコンテキストのprompt-local化
- **GitHub Copilot agent runtime** と **Codex Supervisor** プラグインパッケージを追加
- **iOSアプリ**: Pro Command、Chat、Agents、Settings、hosted push relay、realtime Talkをgatewayセッションに接続
- **Workboard**: アクティブエージェントの作業追跡とハンドオフ用コーディネーションツール

### ▼ v2026.5.27: OpenAI埋め込みプロバイダーとセキュリティ境界強化（5月28日）

- **Memory**: OpenAI互換embeddingプロバイダー（ローカル/ホステッドエンドポイント対応）
- **Providers**: Pixverse動画生成プロバイダー追加
- **セキュリティ**: 信頼できないグループプロンプトメタデータをシステムプロンプト外にルーティング、QQBotフォールバック承認ボタンをゲート、admin権限によるノード/デバイスロール承認を必須化
- **Gateway/パフォーマンス**: 読み取り専用セッションキャッシュ、プラグインメタデータフィンガープリントキャッシュ、分離cronプロンプトキャッシュ最適化

### ▼ 主要開発者: @steipete、@yetval、@luoyanglangら

v2026.5.27/28リリースで最も貢献が多い開発者:
- @steipete: リリースマネージャー、コア改善
- @yetval: Codexランタイム、プロバイダーauth改善
- @luoyanglang: エージェントランタイム、compaction改善
- @vincentkoc: プロバイダー拡張、音声モデルカタログ

**出典**: GitHub OpenClaw Releases v2026.5.28, v2026.5.27
