---
title: "豆包/ByteDance（Doubao）— 字節跳動のAIモデル・コーディングプラットフォーム"
created: 2026-04-18
updated: 2026-04-18
tags: [llm, model, china, coding-agents, company, bytedance]
aliases: ["豆包", "Doubao", "Trae", "MarsCode", "豆包MarsCode", "doubao-bytedance"]
source_lang: zh-CN
---

# 豆包/ByteDance（Doubao）— 字節跳動のAIモデル・コーディングプラットフォーム

> **トレンド順位**: NEW（2026-04-18集計、4言及）
> **ソース**: Juejin, V2EX
> **注目度**: 🔥🔥 — Doubao-Seed-2.0リリースとTrae無料提供で注目急上昇

## 概要

**豆包（Doubao）**は、**字節跳動（ByteDance）** — TikTokの親会社 — が開発・展開するAIアシスタント・大規模言語モデルブランドである。ByteDanceのAI戦略は、自社モデル（Doubao-Seedシリーズ）を基盤に、コーディングIDE（Trae）、AI開発プラットフォーム（豆包MarsCode）、クラウドインフラ（火山云/Volcengine）を統合的に提供する垂直統合型エコシステムの構築にある。

2026年4月現在、ByteDanceは**Doubao-Seed-2.0**モデルのリリースと**「中国版Trae」の無料提供**を軸に、中国AIコーディング市場で攻勢を強めている。掘金（Juejin）では「豆包2.0来了！中国版Trae免费用～」（豆包2.0が来た！中国版Traeが無料で使える～）と題した記事が57いいねを獲得し、開発者コミュニティでの関心の高さを示している。

> **出典**: 掘金 — 「豆包2.0来了！中国版Trae免费用～」（57いいね）[T2]

## Doubao-Seed-2.0モデル

### モデル概要

ByteDanceが2026年4月にリリースした**Doubao-Seed-2.0**は、プログラミング能力に特化した次世代モデルファミリーである。前世代からAgent能力、視覚理解（visual understanding）、フロントエンド開発の各領域で大幅な改良が施されている。

### バリエーション

| モデル | 位置づけ | 特徴 |
|---|---|---|
| **Doubao-Seed-2.0-Pro** | フラグシップ | 最高性能、複雑なAgent制御・マルチモーダル入力対応 |
| **Doubao-Seed-2.0-Lite** | バランス型 | 性能とコストの均衡、一般的な開発タスクに最適 |
| **Doubao-Seed-2.0-Mini** | 軽量型 | 低レイテンシ・低コスト、コード補完やリアルタイム応答向け |

### 主要能力

- **Agent能力の強化**: 自律的なタスク分解・実行、Skills（スキル）の呼び出しによるツール連携
- **マルチモーダル入力**: テキストに加え、画像・スクリーンショットからのコード生成が可能
- **視覚理解の向上**: UIデザインからのフロントエンドコード生成精度が大幅に改善
- **フロントエンド開発**: React、Vue等のモダンフレームワーク向けコード生成に特化した最適化

### 火山云 Coding Planでの提供

火山云（Volcengine）のCoding Planにおいて、Doubao-Seed-2.0-Codeは[[glm-zhipu|GLM-4.7]]とバンドルで提供されている。V2EXでは火山云Coding Planの議論が活発に行われており、Doubaoが主力モデル、GLM-4.7が補助的位置づけとの評価がなされている（[[coding-plan]]参照）。

> **出典**: V2EX — [https://www.v2ex.com/t/1206049](https://www.v2ex.com/t/1206049) [T2]

## Trae — AI IDE

### 概要

**Trae**は、ByteDanceが開発するAIコーディングIDE（統合開発環境）である。[[cursor|Cursor]]と同様のAIネイティブIDE路線を取り、VS Codeベースのエディタ上でAI機能を深く統合している。

国際版Traeが先行してリリースされていたが、2026年4月に**「中国版Trae」**（中国国内向けバージョン）が**無料で**一般提供されたことが大きな話題を呼んでいる。

### 「中国版Trae」の特徴

- **無料提供**: Cursorが有料サブスクリプションモデルであるのに対し、Traeは基本機能を無料で提供
- **Doubao-Seed-2.0統合**: 自社モデルをバックエンドに使用し、低レイテンシ・高精度なコード生成を実現
- **中国国内アクセス**: VPN不要、身分認証の障壁なし — [[claude-code]]のKYC問題（[[claude-opus-4-7]]参照）に直面する中国開発者にとって大きな優位性
- **Skills呼び出し**: Doubao-Seed-2.0のAgent機能と連携し、外部ツール・APIの自動呼び出しが可能

### Cursor / Claude Codeとの比較

| 項目 | Trae（中国版） | [[cursor|Cursor]] | [[claude-code|Claude Code]] |
|---|---|---|---|
| 価格 | 無料 | $20/月〜 | Claude Pro ($20/月〜) |
| バックエンドモデル | Doubao-Seed-2.0 | 複数モデル選択可 | Claude Opus 4.7 |
| 中国アクセス | ✅ 障壁なし | ⚠️ アクセス可能だが制約あり | ❌ KYC問題で制限 |
| IDE統合 | VS Codeベース | VS Codeベース | ターミナルベース |
| Agent能力 | Skills連携 | Composer Agent | Routines / Hooks |

掘金コミュニティでは「中国版Trae」の無料提供が、Cursor有料化に不満を持つ中国開発者の受け皿として注目されている。

## 豆包MarsCode（AI coding platform）

### 概要

**豆包MarsCode**は、ByteDanceが提供するクラウドベースのAIコーディングプラットフォームである。ブラウザ上で動作するAIペアプログラミング環境として、以下の機能を提供する：

- **AIコード補完**: Doubaoモデルによるリアルタイムコード補完
- **AIコードレビュー**: プルリクエスト時の自動レビュー・改善提案
- **AIチャット**: コードベースに関する質問応答、リファクタリング提案
- **クラウドIDE**: 環境構築不要のブラウザ開発環境

### Traeとの棲み分け

| 製品 | 形態 | 対象ユーザー |
|---|---|---|
| **Trae** | ローカルIDE（VS Codeベース） | 本格的な開発者、大規模プロジェクト |
| **豆包MarsCode** | クラウドIDE + AI拡張 | 軽量な開発、学習、プロトタイピング |

ByteLineのAI製品戦略として、Traeがデスクトップ開発、MarsCodeがクラウド開発をそれぞれカバーし、Doubao-Seedモデルが両製品のバックエンドを共通基盤として支える構造となっている。

## 中国AIコーディング市場における位置づけ

### 競合比較

2026年4月現在の中国AIコーディングエコシステムにおいて、ByteDance/Doubaoは以下のプレイヤーと競合している：

| プレイヤー | モデル | IDE/ツール | 強み |
|---|---|---|---|
| **ByteDance（豆包）** | Doubao-Seed-2.0 | Trae, MarsCode | 無料IDE、垂直統合、マルチモーダル |
| **月之暗面（Moonshot）** | [[kimi-moonshot\|Kimi K2.5/K2.6]] | Kimi Chat | コード品質がClaudeに匹敵、コスト優位 |
| **智谱AI（Zhipu）** | [[glm-zhipu\|GLM-5/5.1]] | — | オープンソース744B、Agent制御 |
| **阿里巴巴（Alibaba）** | [[qwen\|Qwen-3.5]] | [[coding-plan\|CodingPlan]] | クラウド統合、マルチモデルバンドル |
| **Anthropic** | [[claude-code\|Claude Code]] | — | 最高性能（SWE-bench 87.6%）、KYC問題 |

### ByteDanceの差別化戦略

1. **無料戦略**: Trae中国版の無料提供により、Cursor・Claude Codeからの移行を促進
2. **垂直統合**: モデル（Doubao-Seed）→ IDE（Trae）→ クラウド（火山云）の一気通貫
3. **マルチモーダル優位**: 画像→コード変換能力は、テキストベースの競合に対する差別化要因
4. **Agent能力の深化**: Skills呼び出しによるエコシステム拡張は、[[ai-agent]]パラダイムの実装として注目

### 課題

- **モデル性能**: SWE-benchなどの標準ベンチマークでの公開スコアが限定的であり、Claude Opus 4.7（87.6%）やGLM-5（77.8%）との直接比較が困難
- **エコシステム成熟度**: Claude CodeのSkills + MCPエコシステムや、阿里云CodingPlanのマルチモデルバンドルに比べ、Doubaoのエコシステムはまだ発展途上
- **国際競争力**: Traeの国際版は存在するが、海外市場でのCursor・Claude Codeとのシェア争いは未知数

## 関連リンク

### 内部リンク

- [[claude-code]] — 最大の国際競合、ターミナルベースAIコーディングエージェント
- [[kimi-moonshot]] — 中国国産LLM競合、Claude代替として急成長
- [[coding-plan]] — 中国発AIコーディングサブスクリプションモデル（火山云Coding Plan含む）
- [[ai-agent]] — AIエージェントパラダイム（Doubao-Seed-2.0のAgent能力が関連）
- [[glm-zhipu]] — 火山云Coding PlanでDoubaoとバンドル提供される中国国産LLM
- [[cursor]] — Traeの直接的競合となるAIネイティブIDE
- [[qwen]] — 阿里巴巴の大規模言語モデル、CodingPlanエコシステムの競合

### 外部ソース

| ソース | URL | ティア | 概要 |
|---|---|---|---|
| 掘金 — 豆包2.0リリース | — | T2 | 「豆包2.0来了！中国版Trae免费用～」（57いいね） |
| V2EX — 火山云 Coding Plan | [v2ex.com/t/1206049](https://www.v2ex.com/t/1206049) | T2 | Doubao-Seed-2.0-Code + GLM-4.7バンドル議論 |

### 公式リンク

- 豆包公式: [https://www.doubao.com/](https://www.doubao.com/)
- Trae公式: [https://www.trae.ai/](https://www.trae.ai/)
- 豆包MarsCode: [https://www.marscode.cn/](https://www.marscode.cn/)
- 火山云（Volcengine）: [https://www.volcengine.com/](https://www.volcengine.com/)
