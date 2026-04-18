---
title: "Claude Design — Anthropicのデザインツール（Figma/Canva競合）"
created: 2026-04-18
updated: 2026-04-18
tags: [claude, product, tooling, anthropic]
aliases: ["Claude Design", "claude-design"]
source_lang: zh-CN
---

# Claude Design — Anthropicのデザインツール

> **トレンド順位**: 04-18急上昇（36kr, V2EX, The New Stackで言及）
> **ステータス**: Research Preview
> **リリース日**: 2026-04-17
> **URL**: [claude.ai/design](https://claude.ai/design)

## 概要

Claude Designは、[[anthropic]]傘下のAnthropic Labsが2026年4月17日にリリースしたAIネイティブデザインツール。[[claude]]をベースに、デザインの生成・編集・エクスポートをテキスト指示で実行できる。[[cursor]]や[[claude-code]]と同じく、「人間が指示してAIが作る」パターンをデザイン領域に適用した製品である。

The New Stackは「Figma and Canva rival built on Claude」と報じ、36krは「Figma杀手」（フィグマキラー）という見出しで伝えた。

## 主要機能

### デザインシステム自動生成
既存のコードベース、デザインファイル、ビジュアルアセットを読み込み、基礎的なデザインシステムを自動構築する。配色、タイポグラフィ、レイアウト要素の一貫したルールセットを生成。

### インタラクティブ編集
- 特定のプレビュー要素に直接コメント
- デザイン上への直接描画（ドローイング）
- プロパティ（背景、フォント等）のインプレース編集
- AIがリアルタイムでスライダー/オプションを生成し、追加プロンプトなしで微調整可能

### 出力フォーマット
- デザインシステム → ウェブサイトプロトタイプ
- プレゼンテーション資料（スライドデッキ）
- ワンペーパー、マーケティング資料
- インタラクティブなウェブサイト

### [[claude-code]]との統合
Claude Designで作成したデザインは、[[claude-code]]に直接ハンドオフして機能する製品に変換できる。デザイン→開発の翻訳オーバーヘッドを削減する。

## トークンエコノミクス

Claude Designは独自の週次トークン制限を持つ（Claude有料プラン: Pro, Max, Team, Enterpriseに含まれる）。

The New Stackのテストによると：
- デザインシステム1つ + ニュースウェブサイトプロトタイプ + 微調整 + 説明動画1本 = **週次割り当ての50%以上を消費**
- 週次制限超過後は従量課金（pay-as-you-go）
- ワイヤーフレームや基本スライドデッキはフルモックアップより大幅にトークン消費が少ない

> **出典**: The New Stack — [Anthropic launches Claude Design](https://thenewstack.io/anthropic-claude-design-launch/) [T1]

## 市場インパクト

### Figma株価への影響
AnthropicのCPOマイク・クリーガーがFigma取締役会を辞任した直後にClaude Designが発表された。

| 指標 | 数値 |
|------|------|
| Figma株価（12ヶ月） | 約50%下落 |
| Claude Design発表直後 | 追加5%下落 |
| 36kr見出し | 「设计软件股暴跌」（デザインソフト株暴落） |

### Canvaとの競合
The New StackはCanvaも競合として位置づけている。Claude DesignはCanvaへの直接エクスポートに対応（Figmaへのネイティブエクスポートは未実装）。

> **出典**: 36kr — [设计行业的"棺材板"，要被Claude Design盖上了](https://36kr.com/p/3771690585223689) [T1]
> **出典**: 36kr — [刚刚，Claude推出"Figma杀手"，设计软件股暴跌](https://36kr.com/p/3771756155077127) [T1]

## 制限事項（Research Preview段階）

- **チーム共有非対応**: 作成したプロトタイプをチームとリアルタイム共有する機能はまだない
- **トークン消費の速さ**: 反復的な使用で週次制限をすぐに超過
- **エクスポート先**: Canvaは対応、Figmaは非対応（今後の統合予定）
- **プレビュー状態**: 機能セット、エクスポートオプション、インテグレーションは進化中

## Anthropicの戦略的文脈

Claude Designの発表は、Anthropicが単なるLLMプロバイダーから**垂直統合型プラットフォーム企業**への転換を図っていることを示唆する。

1. [[claude-code]] → 開発領域
2. Claude Design → デザイン領域
3. [[claude-opus-4-7]] → モデル基盤

この3製品を組み合わせることで、デザイン→開発→デプロイの全工程をClaudeエコシステム内で完結させるビジョンが読み取れる。

36krの分析では「从设计到Coding的活它都要干」（デザインからコーディングまで全部やる）と評されている。

## 中国コミュニティの反応

V2EXでは「Claude Design」というスレッドが立ち、「看上去挺牛逼的」（かなり凄そうだ）と簡潔に評価された。詳細な機能分析よりも、Figmaへの影響や株価下落の方が注目されている。

> **出典**: V2EX — [Claude Design](https://www.v2ex.com/t/1206766) [T1]

## 関連リンク

### 内部リンク
- [[anthropic]] — 開発元
- [[claude-code]] — 開発ハンドオフ先
- [[claude-opus-4-7]] — バックエンドモデル
- [[cursor]] — デザイン・開発統合の文脈での競合

### 外部ソース
| ソース | URL | ティア | 概要 |
|---|---|---|---|
| The New Stack | [thenewstack.io/...](https://thenewstack.io/anthropic-claude-design-launch/) | T1 | 機能詳細、トークンエコノミクス |
| 36kr/智东西 | [36kr.com/p/3771756155077127](https://36kr.com/p/3771756155077127) | T1 | 「Figma杀手」報道、株価影響 |
| 36kr/字母AI | [36kr.com/p/3771690585223689](https://36kr.com/p/3771690585223689) | T1 | デザイン→コーディング統合分析 |
| V2EX | [v2ex.com/t/1206766](https://www.v2ex.com/t/1206766) | T1 | コミュニティ初反応 |

## Mike KriegerとFigmaとの関係

### 経歴
- **Instagram共同創設者**: 2010年にInstagramを共同創業、2012年のFacebookによる10億ドル買収に貢献
- **2024年5月**: AnthropicのCPO（Chief Product Officer）に就任
- **2026年4月14日**: Figma取締役会を辞任

### Claude Design発表のタイミング
Mike KriegerがFigma取締役会を辞任した直後にClaude Designが発表された。V2EXでは「これは偶然ではない」という見方が支配的で、Anthropicがデザインツール市場に本格的に参入する意図の表れと分析されている。

Figmaの株価は、過去12ヶ月で約50%下落していたが、Claude Design発表後にさらに6.84%下落した。

> **出典**: 36kr — [刚刚，Anthropic的CPO从Figma董事会辞职](https://36kr.com/p/3771736819647233) [T1]
