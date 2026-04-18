---
title: "CreatorWeave — ローカル優先のブラウザ創作ワークスペース"
created: 2026-04-18
updated: 2026-04-18
tags: [ai-agents, tooling, open-source-ai, framework]
aliases: ["クリエイターウィーブ", "ワークスペース並行", "ブラウザIDE"]
source_lang: zh-CN
---

# CreatorWeave — ローカル優先のブラウザ創作ワークスペース

ブラウザ上で動作する**ローカル優先（Local-First）**の創作ワークスペース。IDEや複雑な環境構築なしに、ブラウザを開くだけでテキストコンテンツ創作・開発作業を始められる。

## 概要

開発者: camolNjujlc  
GitHub: [nutstore/creatorweave](https://github.com/nutstore/creatorweave)  
オンライン体験: [creatorweave.eo2suite.cn](https://creatorweave.eo2suite.cn/)

純テキストコンテンツ創作に特化。エディタ・ブラウザ・端末間の行き来によるコンテキスト断裂を解決する。

## 核心機能

### ワークスペース並行（Workspace Parallelism）

- 複数のワークスペースを並行して実行可能
- git worktree に似た概念だが、gitの知識は不要
- 創作の分岐・並行開発を視覚的に管理

### ローカルファイルマッピング

- ユーザーが明示的に認可したローカルフォルダに直接アクセス
- ブラウザ権限モデルに準拠 — 未認可ファイルへのアクセスは不可
- IDEインストール不要でローカルファイルを操作

### 多智能体（Multi-Agent）协作

- デフォルトエージェントの役割・作業モードを調整可能
- エージェントが他のエージェントを生成できる
- 現在「作者＋編集者」ロールで网文（ウェブ小説）の章単位の共同執筆をテスト中

## Roadmap

1. Web端の基礎体験と安定性の継続的改善
2. リモート制御機能の回補・完善（初期バージョンは存在したが一時停止）
3. LLM Wiki の推進 — 蓄積可能・検索可能・追跡可能な知識フロー
4. AgentへのSubAgent機能強化 — 複雑タスク実行品質の向上

## 関連プロジェクト

- [[openclaw]] — 多智能体思路の参考元の一つ
- [[ai-agent]] — エージェントパターン全般
- [[vibe-coding]] — AIネイティブな開発スタイル

## 出典

- [V2EX: CreatorWeave — 本地優先的瀏覽器創作工作空間](https://www.v2ex.com/t/1206316) — camolNjujlc (2026-04-16)
- [GitHub: nutstore/creatorweave](https://github.com/nutstore/creatorweave)
