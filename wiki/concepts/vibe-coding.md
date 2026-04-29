---
title: "Vibe Coding（氛围编程）— AIネイティブなソフトウェア開発手法"
created: 2026-04-17
updated: 2026-04-17
tags: [coding-agents, concept, technique, ai-agents]
aliases: ["Vibe Coding", "氛围编程", "バイブコーディング"]
source_lang: zh-CN
---

# Vibe Coding（氛围编程）— AIネイティブなソフトウェア開発手法

> **トレンド順位**: #15（2026-04-17集計、7言及）
> **ソース**: Juejin, V2EX

## 概要

**Vibe Coding（氛围编程）**は、AIモデルと自然言語で対話しながら、直感的・反復的にソフトウェアを開発する手法である。厳密なエンジニアリングプロセスを経由せず、「雰囲気（vibe）」に従ってコードを生成・組み立てる点に特徴がある。

Andrej Karpathyが命名したこの概念は、中国語圏の開発者コミュニティにおいても「氛围编程」として浸透し、[[claude-code]]や[[cursor]]等のAIコーディングツールの利用文化と密接に結びついている。

## [[harness-engineering]]との関係

Vibe Codingと[[harness-engineering]]は、AIコーディングのスペクトラム上の両端に位置する：

```
Vibe Coding ◄━━━━━━━━━━━━━━━━━━━━► Harness Engineering
（非形式的・直感的）                    （形式的・工学的）
```

両者は対立するものではなく、開発のフェーズや目的に応じて使い分けるものである。プロトタイピングにVibe Coding、本番用パイプラインにHarnessという使い分けが現実的である。

## 中国語圏での拡がり

### 包括的ガイド

掘金（Juejin）では「Vibe Coding 概念大全」（Vibe Codingコンセプト完全ガイド）と題した包括的な解説記事が公開されている。LLM、ファインチューニング、推論の文脈でVibe Codingの位置づけを整理している。

> **出典**: Juejin — [https://juejin.cn/post/7602191709389176874](https://juejin.cn/post/7602191709389176874) [Tier-2]

### 開発者アイデンティティへの影響

Vibe Codingが開発者の自己認識にも影響を与え始めていることを示す現象として、SBTI（性格診断型コンテンツ）のバイラル化がある。ある開発者がプログラマー版CBTIを作成し、これがオープンソースで公開された。ClaudeとCursorを使って「Vibe Coding」的に構築されている点も特徴的。

> **出典**: Juejin — [https://juejin.cn/post/7627948981355888676](https://juejin.cn/post/7627948981355888676) [Tier-2]

### AI依存のリスク

36krでは「不用则废」（使わなければ廃れる）という観点から、Vibe Codingを含むAIコーディングツールへの依存がもたらす隠れたコストについて警鐘が鳴らされている：

- **スキル劣化**: AIに依存しすぎると、基本的なコーディング能力が衰える
- **ベンダーロックイン**: 特定のAIツールへの依存
- **ブラックボックス化**: AIが生成したコードの理解不足

> **出典**: 36kr — [https://36kr.com/p/3767823043494658](https://36kr.com/p/3767823043494658) [Tier-1]

## 関連リンク

### 内部リンク

- [[harness-engineering]] — Vibe Codingの対極に位置する形式的アプローチ
- [[claude-code]] — Vibe Codingの主要ツール
- [[ai-agent]] — Vibe CodingからAgent活用への進化
- [[coding-plan]] — Vibe Coding実践者が利用するサブスクリプション

### 外部ソース



## Vibe Coding 概念大全（2026-04-24更新）

Juejinで**Vibe Codingの包括的概念リファレンス**が公開された。LLM/ファインチューニング/推論文脈でのVibe Codingの位置づけを体系的に整理。

### 概念整理の主要ポイント
- **Vibe Codingの定義**: 雰囲気で書くコーディング。厳密な設計よりも感覚的・直感的な開発スタイル
- **LLMとの関係**: プロンプトだけでコードが生成される現代の開発パラダイム
- **ファインチューニング文脈**: ドメイン特化モデルによる「Vibeに合う」コード生成
- **推論最適化**: 軽量モデルでも「Vibe」を保つ量子化・蒸留技術

### 中国開発者コミュニティでの受容
- 「Vibe Coding」という用語が中国技術コミュニティで定着
- 従来の厳格なエンジニアリング実践との対比で議論
- 若手開発者を中心に支持が拡大

> **出典**: Juejin — [Vibe Coding 概念大全](https://juejin.cn/post/7602191709389176874) [T2]
> **出典**: Juejin — [Vibe Coding 概念大全](juejin/2026-04-24-Vibe-Coding-概念大全-a8e1d486.md) (2026-04-24) [T2] — 包括的概念リファレンス記事

| ソース | URL | ティア |
|---|---|---|
| Juejin — Vibe Coding概念大全 | [juejin.cn/post/7602191709389176874](https://juejin.cn/post/7602191709389176874) | Tier-2 | Vibe Coding用語包括リファレンス |
| Juejin — CBTIプログラマー版 | [juejin.cn/post/7627948981355888676](https://juejin.cn/post/7627948981355888676) | Tier-2 |
| 36kr — AI依存のコスト | [36kr.com/p/3767823043494658](https://36kr.com/p/3767823043494658) | Tier-1 |
