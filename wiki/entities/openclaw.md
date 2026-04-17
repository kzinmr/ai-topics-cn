---
title: OpenClaw — AI Agentエンドポイントツール
created: 2026-04-17
updated: 2026-04-17
tags: [ai-agents, open-source-ai, tooling, china]
aliases: [\"openclaw\", \"OpenClaw\"]
source_lang: zh-CN
---

# OpenClaw — AI Agentエンドポイントツール

> **トレンド順位**: #9（2026-04-17集計、17言及）  
> **ソース**: 36kr, Juejin, V2EX（全3ソースタイプ）  
> **出典**: 中国語圏のAgentフレームワーク戦争における新興プレイヤー

## 概要

OpenClawは、AI Agentが外部ツール・API・システムと自律的にやり取りするための**エンドポイント型ツールチェーン**フレームワークである。2025年半ばから中国語圏の開発者コミュニティで急速に注目を集め、Claude Code ([[claude-code]]) やHermes Agentとの比較対象として議論されている。

「[[openclaw]]」という名前通り、複数の「爪」（ツール.endpoint）を并发的に伸ばしてタスクを処理する並列実行モデルが最大の特徴。

## 機能と設計思想

### 並列ツール実行アーキテクチャ

OpenClawは単一のツール呼び出しに留まらず、複数のエンドポイントを同時に伸張（伸出）して実行できる：

```
OpenClaw Agent
  ├── Endpoint: FileSystem (読み書き)
  ├── Endpoint: Git (commit/push)
  ├── Endpoint: Browser (スクレイピング)
  ├── Endpoint: Database (クエリ)
  └── Endpoint: API (外部サービス呼び出し)
```

この設計により、Claude Codeの単一セッション内でも複数のツール操作を同时進行できる。36krは「OpenClawの多爪構造がAI Agentの作业方式を根本的に変えた」と評している。

### MCPプロトコルとの統合

OpenClawは[[mcp]]（Model Context Protocol）ベースのセキュリティ問題を提起したフレームワークでもある。36krが「OpenClaw爆火，暴露12类致命隐患」と報じた通り、MCPプロトコル利用時の致命的脆弱性が問題化。

### 12類的安全隐患

36kr（新智元）が報じたOpenClawの安全隐患（_security vulnerabilities_）：

1. ツール権限の過大な払い出し
2. MCPエンドポイント間のデータ漏洩
3. 第三者ツールチェーンへの汚染
4. 認証情報の横方向的移動（lateral movement）
5. ファイルシステム抽象化の不備
6. ネットワークプロキシ悪用
7. セッション固定攻撃
8. ツール呼び出しの再帰的暴走
9. タイムアウト後の不整合状態
10. ログ露出によるcredential流出
11. エンドポイントフェイク（なりすまし）
12. プロトコルバージョン不和

> **出典**: 36kr — [https://36kr.com/p/3768662327935747](https://36kr.com/p/3768662327935747) [T1]

## Hermes Agentとの対比

2026年4月、掘金で「GitHub 85K Star 新王挑战 357K Star 霸主：Hermes 还是 OpenClaw？最强Agent框架怎么选」と題した比較記事が大いに議論された。

| 指標 | Hermes Agent | OpenClaw |
|------|-------------|----------|
| GitHub Stars | 357K | 85K |
| 設計思想 | 長期記憶・自己進化 | 並列ツールチェーン |
| アーキテクチャ | Stateful session | Stateless endpoint |
| 中国コミュニティ人気 | 高（exe.dev統合） | 急上昇中 |
| MCP安全性 | 調査中 | 12類問題曝光 |

著者の「大模型真好玩」は以下のように総括している：

> 「Hermes并非简单取代OpenClaw，而是开辟新路径：赋予Agent长期记忆与自我进化能力」  
> （Hermesは単にOpenClawを置換するものではなく、新しい道を切り開いている：Agentに長期記憶と自己進化能力を付与する）

> **出典**: 掘金 — [https://juejin.cn/post/7628854568781545506](https://juejin.cn/post/7628854568781545506) [T2]

## 阿里云との統合（算力自由）

2026年4月16日、阿里云（Alibaba Cloud）がOpenClawユーザーが阿里云の算力（GPUインスタンス）に直接アクセスできる統合を発表した。「终于不怕OpenClaw烧token啦，直接算力自由」（もうOpenClawのトークン消費を心配しなくていい、算力が自由になった）と評されている。

これはOpenClaw利用のコスト障壁を下げる Alibaba Cloudの戦略的動きと解读できる。

> **出典**: 掘金 — [https://juejin.cn/post/7629308995309322290](https://juejin.cn/post/7629308995309322290) [T2]

## 中国語圏での立ち位置

OpenClawは中国語圏AI Agent市場で以下の位置づけ：

- **「第二勢力」**: Claude Code ([[claude-code]])に次ぐ注目度
- **トレンド成長**: 17言及（前回集計から増加傾向）
- **問題提起者**: MCPプロトコルの安全問題を世界で初めて体系的に列出
- **阿里云との関係**: 中国市場攻略における有力パートナー

## 関連リンク

### 内部リンク

- [[claude-code]] — 主要競合・比較対象
- [[mcp]] — 安全問題の中心にあるプロトコル
- [[harness-engineering]] — 类似的Agent Harness概念
- [[ai-agent]] — 上位カテゴリ

### 外部ソース

| ソース | URL | ティア | 概要 |
|---|---|---|---|
| 36kr — 12類安全隐患 | [36kr.com/p/3768662327935747](https://36kr.com/p/3768662327935747) | T1 | 安全問題の体系的分析 |
| 掘金 — Hermes vs OpenClaw | [juejin.cn/post/7628854568781545506](https://juejin.cn/post/7628854568781545506) | T2 | フレームワーク比較 |
| 掘金 — 阿里云統合 | [juejin.cn/post/7629308995309322290](https://juejin.cn/post/7629308995309322290) | T2 | 阿里云との統合 |