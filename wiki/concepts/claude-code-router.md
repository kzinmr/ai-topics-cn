---
title: "claude-code-router — モデル切り替えルーター"
created: 2026-04-18
updated: 2026-04-18
tags: [claude-code, tooling, open-source, china]
aliases: ["ccr", "claude-code-router"]
source_lang: zh-CN
---

# claude-code-router (ccr) — Claude Code用モデル切り替えルーター

## 概要

**claude-code-router**（通称 `ccr`）は、[[claude-code]] のバックエンドモデルをコマンド1つで切り替えるためのオープンソースツール。AnthropicのAPI互換インターフェースを利用し、Claude Codeの設定ファイル（`~/.claude/settings.json`等）を変更せずに実行時モデルを差し替えることができる。

中国の開発者コミュニティにおいて、Anthropicの強制身分認証（KYC）問題やコスト最適化の文脈で注目されている。

## 主要機能

### モデル切り替え

```bash
# Kimi K2.5に切り替え
ccr switch kimi-k2.5

# GLM-5に切り替え
ccr switch glm-5

# Claude Opus 4.5に戻す
ccr switch claude-opus-4.5
```

### 環境変数による制御

以下の環境変数を設定することで、Claude Codeのモデル呼び出しをインターセプトする：

| 変数 | 説明 |
|------|------|
| `ANTHROPIC_BASE_URL` | APIエンドポイント（ccrがローカルプロキシを立てる） |
| `ANTHROPIC_AUTH_TOKEN` | 認証トークン |
| `ANTHROPIC_MODEL` | 使用するモデル名 |

### Kimi K2.5統合

[[kimi-moonshot]] のK2.5モデルは、Anthropic API互換インターフェースを提供しており、claude-code-router経由でClaude Codeから直接呼び出せる。これにより：

- Anthropicの身分認証問題を回避
- 中国国内からの安定したアクセス
- コスト最適化（K2.5はOpus 4.5比で大幅に低コスト）

が可能になる。

## 使用場面

1. **Anthropic KYC回避**: 中国大陸ユーザーが身分認証なしでClaude Codeエコシステムを利用
2. **コスト最適化**: タスクに応じて安価なモデルに切り替え
3. **モデル比較**: 同じプロンプトで複数モデルの出力を比較
4. **フェイルオーバー**: 某モデルがダウン時に別モデルに自動切り替え

## 関連ツール

### cc-monitor

[[cc-monitor]]はClaude CodeのJSONLログとPostToolUse Hookを活用したリアルタイムToken消費モニター。複数プロジェクトのコストを同時に監視できる。

### Skillエコシステム

掘金で「别再裸用 Claude Code 了！32 个亲测Skills + 8 个 MCP」という記事が434いいね・1,087スターを獲得。Claude Codeのカスタマイズが中国開発者コミュニティで定着しつつある。

## 関連リンク

### 内部リンク
- [[claude-code]] — ルーターの対象ツール
- [[kimi-moonshot]] — 主要な代替モデル
- [[glm-zhipu]] — GLM-5もAPI互換で利用可能
- [[cc-monitor]] — Claude Code用リアルタイムToken消費モニター
- [[ollama-criticism]] — Ollama批判論争（ローカルLLM倫理）

### 外部ソース
| ソース | URL | ティア |
|--------|-----|--------|
| 掘金 — Kimi K2.5 × Claude Code | [juejin.cn/post/7611432757572141096](https://juejin.cn/post/7611432757572141096) | T2 |
