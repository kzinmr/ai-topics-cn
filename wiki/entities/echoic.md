---
title: "Echoic — オープンソースAI口语練習ツール"
created: 2026-04-18
updated: 2026-04-18
tags: [ai-agents, tooling, open-source-ai, media]
aliases: ["エコーイック", "AI口语", "発音評価"]
source_lang: zh-CN
---

# Echoic — オープンソースAI口语練習ツール

ローカルモデルを使用したAI発音評価ツール。プライバシー保護・完全無料・自デプロイ可能。音素レベルでの発音スコアリングを提供する。

## 概要

開発者: xialeistudio  
GitHub: [xialeistudio/echoic](https://github.com/xialeistudio/echoic)

市場の口语練習ツールは有料・会員登録・データ外部送信が必要なものが多い。これを解決するため、**データがローカルから出ない**オープンソースツールを開発。

## 核心機能

### 発音評価（音素レベル）

- **准确度** — 発音の正確さ
- **流利度** — フルーエンシー
- **完整度** — 文章の完結度
- 単語・音素ごとにスコアを色分け表示

### 技術スタック

| 層 | 技術 |
|---|---|
| フロントエンド | React 18 + Tailwind v4 |
| バックエンド | FastAPI |
| 音声認識 | WhisperX |
| 発音評価 | wav2vec2 + phonemizer（**ローカル実行、クラウドAPI不使用**） |
| データベース | PostgreSQL |
| デプロイ | Docker（単一コマンド） |

### 学習機能

- **内容広場**: VOA / BBC Learning English番組内置
- **逐句跟読**: 0.5×〜2×速度調整、原声/録音A/B比較
- **単語復盤**: 全練習単語の准确度汇总、弱点特定
- **練習歴史**: 録音アーカイブ・再生
- **AI文章分析**: 翻訳・構文解析（OpenAI/Ollama接続オプション）
- **熱力図・コレクション・習得マーク・文章検索**

## プライバシー設計

**最大の特徴**: 発音評価にwav2vec2モデルを**ローカル**で実行。データは一切外部に送信されない。

```bash
git clone https://github.com/xialeistudio/echoic.git
cd echoic
docker compose up
# http://localhost:8000 でアクセス
# 初回のみ約1GBのモデルダウンロード
```

## 関連プロジェクト

- [[ollama-criticism]] — ローカル推論のエコシステム
- [[vibe-coding]] — AI支援開発

## 出典

- [V2EX: 开源了一个 AI 口语练习工具，音素级发音评分，完全免费可自部署](https://www.v2ex.com/t/1206381) — xialeistudio (2026-04-16)
- [GitHub: xialeistudio/echoic](https://github.com/xialeistudio/echoic)
