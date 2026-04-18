---
title: "cc-monitor — Claude Code リアルタイムToken消費モニター"
created: 2026-04-18
updated: 2026-04-18
tags: [claude-code, token-monitoring, cost-estimation, developer-tools, tui]
aliases: ["cc-monitor", "Claude-Code-Token-Monitor", "Claude-Code-コスト監視"]
source_lang: zh
---

# cc-monitor — Claude Code リアルタイムToken消費モニター

> **トレンド**: V2EXで話題化（2026-04-18）
> **ソース**: V2EXユーザー SIFT2009
> **GitHub**: https://github.com/SagesAi/claude-cost-monitor
> **重要性**: Claude Codeユーザーのコスト管理を改善する実用的な開発者ツール

## 概要

cc-monitorは、Claude Codeの開発中に複数のセッションをまたいだToken消費と費用をリアルタイムで監視・集計するPythonツールです。2026年4月18日にV2EXでユーザーSIFT2009によって紹介されました。

> "Claude Codeでプロジェクト開発をしていると、複数のセッションを同時に開いて作業することが多く、月末の請求を見て初めて某个プロジェクトが数十ドルも消費していたことに気づくことがある。Claude標準の`/cost`コマンドでは現在のセッションしか見えず、プロジェクト次元の集計もリアルタイム監視もできない。"
> （V2EX記事より引用）

## 主な機能

1. **プロジェクト別集計**: 複数のプロジェクトのtoken消費と費用を同時に監視
2. **リアルタイムTUI**: 2秒ごとに更新されるターミナルUI、最近の操作記録が自動スクロール
3. **二重データソース**: JSONLログ（正確）+ PostToolUse Hook（リアルタイム時系列）
4. **費用推定**: Sonnet/Opus/Haikuなどモデル別の価格で自動計算
5. **Compact検出**: コンテキスト圧縮を自動識別し、どのくらいのtokenを節約したかを表示

## インストール方法

```bash
git clone https://github.com/SagesAi/claude-cost-monitor.git
cd claude-cost-monitor
python -m pip install -e .
cc-monitor-install    # hookを一クリックでインストール
cc-monitor &          # モニターをバックグラウンドで起動
cc-monitor-tui        # ターミナルUIを起動
```

## TUI表示例

```
┌─────────────────────────────────────────────────────────────────┐
│ cc-monitor  ● hook  ● jsonl  refreshed 14:38:42  total: $7.72   │
│ ...（以降、各プロジェクト別の消費状況がリアルタイム表示）        │
└─────────────────────────────────────────────────────────────────┘
```

## Claude Codeエコシステムにおける位置づけ

cc-monitorはClaude Codeの公式ツールではなく、コミュニティが開発したサードパーティ製の監視ツールです。しかし、Claude Codeの大規模利用において、コスト管理は重要な課題となっており、このツールはそのギャップを埋める役割を果たしています。

### 関連ツールとの比較

| ツール | 提供元 | 機能 | 統合方法 |
|--------|--------|------|----------|
| **cc-monitor** | コミュニティ (SagesAi) | プロジェクト別費用集計、リアルタイムTUI | JSONL + Hook |
| **Claude Code `/cost`** | Anthropic | 現在のセッションのみ | 組み込み |
| **[claude-code-router](ccr)** | コミュニティ | モデル切り替え | 環境変数 |
| **OpenClaw** | コミュニティ | 電子商取引エージェント | API |

## 技術的詳細

- **言語**: Python
- **ライセンス**: オープンソース（詳細はGitHub参照）
- **依存関係**: Claude CodeのJSONLログファイルとPostToolUse Hook
- **対応モデル**: Claude Sonnet、Opus、Haiku

## 中国開発者コミュニティへの影響

Claude Codeの中国での採用が拡大する中、コスト管理の透明性は重要な関心事となっています。特に：

1. **複数プロジェクトの並行開発**: 中国の開発チームは複数のAIプロジェクトを同時に進めることが多く、プロジェクト別の費用追従が実用的な価値を持つ
2. **OpenClawとの関係**: 同じV2EXスレッドでOpenClaw電子商取引ツールも議論されており、Claude Codeエコシステムの拡大が示されている
3. **コスト最適化意識**: Compact検出機能により、token効率化への意識が高まっている

## 関連リンク

### 内部リンク

- [[claude-code]] — Claude Code本体
- [[ccr-claude-code-router]] — Claude Codeのモデル切り替えツール
- [[openclaw-ecommerce]] — Claude Codeを活用した電子商取引エージェント

### 外部ソース

| ソース | URL | ティア | 概要 |
|--------|-----|--------|------|
| V2EX | [v2ex.com/t/1206874](https://www.v2ex.com/t/1206874) | T1 | cc-monitor紹介 |
| GitHub | [github.com/SagesAi/claude-cost-monitor](https://github.com/SagesAi/claude-cost-monitor) | T2 | ソースコード |
