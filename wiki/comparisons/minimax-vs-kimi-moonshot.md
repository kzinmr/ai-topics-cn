---
title: "MiniMax vs Moonshot/Kimi — 中国生成AIスタートアップ比較"
created: 2026-04-18
updated: 2026-04-18
tags: [comparison, china, llm, company, startup, multimodal, ai-agents]
aliases: ["MiniMax vs Kimi", "稀宇科技 vs 月之暗面", "MiniMax Moonshot comparison"]
source_lang: ja
---

# MiniMax vs Moonshot/Kimi — 中国生成AIスタートアップ比較

> **比較対象**: [[minimax]]（稀宇科技） vs [[kimi-moonshot]]（月之暗面）
> **出典**: 胡润AI50強、ChinAI #336、Juejin、V2EX
> **重要度**: 高 — 中国生成AIスタートアップの二大勢力

## 企業比較

| 項目 | **MiniMax（稀宇科技）** | **Moonshot AI（月之暗面）** |
|------|------------------------|---------------------------|
| **CEO** | 闫俊杰（Yan Junjie） | 楊植麟（Yang Zhilin） |
| **設立** | 2021年 | 2023年 |
| **拠点** | 上海 | 北京 |
| **胡润ランク** | トップ10（2025年） | トップ50入り |
| **主力製品** | MiniMax-M1/M2（マルチモーダル） | Kimi K2.5/K2.6（長文脈LLM） |
| **2025年ARR** | ~$100M | 未公表 |
| **累計資金** | $1.3B以上 | 未公表 |
| **主要投資家** | Alibaba, General Catalyst | 阿里、騰騰等 |
| **推論コスト** | $3.6M/月（H20 2,000基相当） | 未公表 |
| **月間アクティブユーザー** | 未公表 | MiniMaxの5分の1 |

## モデル比較

| 項目 | **MiniMax-M1/M2** | **Kimi K2.5/K2.6** |
|------|-------------------|-------------------|
| **アーキテクチャ** | MoE（456Bパラメータ、アクティブ4.6B） | 長文脈LLM |
| **OpenCompass順位** | 1位（2025年1月） | 未公表 |
| **推論性能** | マルチモーダル（テキスト・音声・画像） | コーディング能力に強み |
| **Claude Code代替** | 非対応 | ◎ K2.5/K2.6がClaude Code代替として人気 |
| **アクセス容易性** | 中国国内から容易 | 中国国内から容易 |
| **コスト** | 未公表 | Claude Proより低コスト |

## 市場ポジショニング

### MiniMaxの強み
- **マルチモーダル生成**: テキスト・音声・画像の統合生成に優れる
- **資本効率**: OpenAIの1/20〜1/50のリソースで同等の製品体験
- ** ARR**: 中国生成AI企業で最高水準の$100M
- **OpenAI的ビジネスモデル**: 中国で最も「OpenAIに近い」と評価

### Moonshot/Kimiの強み
- **長文脈処理**: Kimi Chatで高い知名度
- **コーディングエージェント**: K2.5/K2.6がClaude Code代替として急成長
- **開発者支持**: 掘金で224いいね・372スターの記事が象徴する高い評価
- **プラットフォーム統合**: 阿里云CodingPlanにバンドル提供

## 2025-2026年の動向

### MiniMax
- 2025年1月: M1モデルリリース、OpenCompassで1位
- 2025年8月: M2モデルリリース、マルチモーダル強化
- 2025年2月: $700M以上の資金調達（General Catalyst, Alibabaリード）

### Moonshot/Kimi
- 2026年4月: K2.6-code-previewを全サブスクリプションユーザー向けにリリース
- 開発者「孟健」がHermesフレームワーク内の23個のエージェント全てをK2.6に切り替えた実測レポート公開
- 阿里云CodingPlanにK2.5がバンドル提供

## 競合環境

中国生成AIスタートアップ市場は以下の構造になっている：

```
第一梯队（胡润トップ10）
├── MiniMax（マルチモーダル）
├── 月之暗面/Moonshot（長文脈LLM）
├── 阶跃星辰（AIGC大模型）
└── その他

第二梯队（トップ50）
├── DeepSeek（オープンソース）
├── Baidu（文心一言）
└── その他
```

## 関連リンク

### 内部リンク
- [[minimax]] — MiniMax詳細ページ
- [[kimi-moonshot]] — Kimi/Moonshot詳細ページ
- [[deepseek]] — オープンソース競合
- [[baidu-ernie]] — Baiduの文心一言
- [[coding-plan]] — Kimiがバンドル提供されるサブスクリプション

### 外部ソース
| ソース | URL | ティア | 概要 |
|---|---|---|---|
| ChinAI #336 | [substack.com](https://chinai.substack.com/) | T2 | MiniMaxのOpenAI的ビジネスモデル分析 |
| Juejin K2.5記事 | [juejin.cn/post/7611432757572141096](https://juejin.cn/post/7611432757572141096) | T2 | Claude→Kimi移行体験（224いいね） |
| Juejin K2.6記事 | [juejin.cn/post/7628520551066058803](https://juejin.cn/post/7628520551066058803) | T2 | 23エージェント移行実測 |
| 胡润AI50強 | — | T1 | 2025年中国AI企業ランキング |
