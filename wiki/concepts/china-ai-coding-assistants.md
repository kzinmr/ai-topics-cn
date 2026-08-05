---
title: "中国AIコーディングアシスタント — Trae・MarsCode・通义灵码・CodeGeeX"
created: 2026-04-28
updated: 2026-08-05
tags: [coding-agents, tooling, china, product-comparison, ide]
aliases: ["中国AI编程助手", "China AI Coding Assistants", "Trae", "MarsCode", "通义灵码", "CodeGeeX", "Lingma", "Qoder CN"]
source_lang: zh-CN
---

# 中国AIコーディングアシスタント

中国四大AIコーディングアシスタント（Trae/MarsCode、通义灵码、CodeGeeX、文心快码）の包括的比较。2025〜2026年にかけて、中国国内開発者向けのAI搭載開発ツール競争が激化している。

## 概要

| ツール | 開発元 | 特徴 | 価格 |
|--------|--------|------|------|
| **Trae (国際版)** | ByteDance | VS Code Fork IDE, SOLO/Builderモード, 音声対話 | $10/mo Pro、初月$3 |
| **Trae CN (中国版)** | ByteDance | 国内向け完全無料、豆包/DeepSeek/Kimi搭載 | **完全無料** |
| **豆包MarsCode** | ByteDance | プログラミングアシスタント + Cloud IDE、100+言語 | 基本無料、API従量課金 |
| **通义灵码 (Lingma)** | Alibaba Cloud | Qwen-Coder-Qoderモデル、Lingma IDE、Quest Agent | 個人無料、企業版有料 |
| **CodeGeeX** | 智譜AI (Zhipu AI) | オープンソース、GLM-4ベース、100万ユーザー超 | 個人無料、企業版有料 |
| **文心快码** | Baidu | 文心一言ベース、Baiduエコシステム連携 | 無料 |

## Trae（ByteDance）

### 概要
ByteDanceが開発するAIファーストIDE。2025年1月にローンチし、2026年5月時点で**月間アクティブユーザー100万超**、累計**60億行以上のコード**を生成。国際版（Trae）と中国版（Trae CN）の2本立て。

### バージョン履歴
- **2025.01**: Trae 1.0 ローンチ（VS Code Fork IDE）
- **2025.04**: Builderモード追加（自然言語→プロジェクト全体）
- **2025.11**: SOLOモード正式版リリース（42都市Offlineイベント開催）
- **2025.12**: SOLOモードがKimi-K2-0905、GPT-5.2対応
- **2026.03**: **Trae 2.0** — SOLOモード + Sub Agent + Plan Mode実装
- **2026.04以降**: 音声対話機能追加発表、月間100万MAU突破

### SOLOモード（Trae 2.0核心機能）
「Context Engineering」概念に基づく自律プログラミングモード：
- AIがタスクコンテキストを能動的に管理（プロンプト待ち不要）
- **Sub Agent機構**: 複雑タスクを自動分解し並列実行
- **Plan Mode**: 計画→確認→実行の3段階
- **DiffView**: コード変更前後の可視化
- **Context圧縮**: 履歴自動圧縮でトークン消費削減

### Builderモード
自然言語からアプリケーション全体を生成（Lovable/Boltに類似のVibe Coding体験）、IDE内蔵でそのまま開発継続可能。

### サポートモデル
Claude Sonnet 4.5/Opus 4.5、GPT-5、Gemini 2.5 Pro、Grok-4（Beta）
（中国版は豆包/DeepSeek/Kimiを無料提供）

## 豆包MarsCode（ByteDance）

### 概要
2024年6月にリリースされたByteDanceの国内向けAI開発ツール。プログラミングアシスタント（IDEプラグイン）とCloud IDEの2形態。2025年11月にTraeブランドに統合され始めたが、MarsCodeは国内向けCloud IDEとして存続。

### 主要機能
- **コード補完**: 単行予測・関数レベル補完・コメント→コード生成
- **単体テスト生成**: JUnit/PyTest対応
- **Bug Fix**: 自動問題コード特定 + 修正提案（正確率75.3%）
- **参照図・画板機能**（2025.10追加）: 自然言語・画像・スケッチからWebページ生成
- **Agent自動計画**: 内蔵Agentがツールを自動呼び出し

### 料金
- 基本機能（コード補完・テスト生成・Bug Fix）: **国内開発者向け永久無料**
- Doubao-Seed-CodeモデルAPI: 業界平均比62.7%安、業界最安値
- Coding Plan: 初月9.9元からのサブスクリプション

### 技術基盤
- 核心エンジン: **Doubao-Seed-Code**（豆包大モデル特化版）
- 2025.02: DeepSeek-R1/V3にも対応（マルチモデル切替可）
- DeepSeek統合後、コード生成精度・セマンティック理解が向上
- クロスプラットフォーム適応層（TRAE中国版対応）

## 通义灵码（Lingma）— Alibaba Cloud

### 概要
Alibaba Cloudが提供するAIコードアシスタント。中国国内最大シェアのAIコーディングツール。**唯一Gartner AIコードアシスタント「挑戦者」象限に選出された中国製品**。

### 主要バージョン
- **通义灵码 2.0**: 多ファイル自動編集 + Diff-Review
- **Lingma IDE**: Qwen-Coder-Qoderモデル搭載の専用IDE、2026.02よりパブリックベータ

### Qwen-Coder-Qoderモデル（2026.02）
- Qwen-CoderをベースにQoder Agentフレームワークに最適化
- Agent向けに大規模強化学習（RL）を実施
- Windows環境のターミナルコマンド精度が**50%向上**
- Cursor Composer-1を凌駕（社内評価）

### Quest Agent（2026.02 Beta）
エンドツーエンドの**自律プログラミングエージェント**：
- **需要対処**: 意図認識・要求明確化・Spec共同作成
- **長期間タスク**: 長時間継続実行 + Agent監督
- **品質自律保障**: 結果検証・修復の自動化
- **持続的自己進化**: コーディングスタイル記憶 + 新技術学習
- **Spec駆動開発**: 要件と制約を最初に合意→実行→検収

### Agentic Chat（2026.02）
- **マルチエージェント並列実行**: 複数Agentが同時タスク処理
- **内蔵計画Agent**: 複雑タスクの計画立案（人間協調可）
- **カスタム拡張**: SubAgent・Skills・Commandsの自作対応
- **Repo Wiki**（企業版Beta）: プロジェクト構造ドキュメント自動生成

### 評価
- 開発者満足率: **87%超**
- Gartner AIコードアシスタント挑戦者象限（中国唯一）
- 信通院「可信AI智能编码工具」4+評価

## CodeGeeX（智譜AI / Zhipu AI）

### 概要
清華大学系の智譜AIが開発。**唯一のオープンソース**中国AIコーディングアシスタント。個人ユーザー100万超。

### モデル系統
- **CodeGeeX4-All-9B**: 100億パラメータ未満で最強のコード生成モデル
- GLM-4-9Bベース、128Kコンテキスト対応
- 公開ベンチマークで大きな汎用モデルを凌駕

### 特徴
- **Function Call**: コードLLMとして唯一、関数呼出しテスト成功率90%超
- **コード検索精度**: 100%（128Kコンテキスト内）
- IDEプラグインv2.12.0: プロジェクトREADME自動生成、NL2SQL向上
- **ローカルモード**: 量子化後GPU 6GBで推論可能
- 企業向けソフトハード一体製品あり（信創方案対応）

### 対応IDE
VS Code、JetBrains（IntelliJ IDEA, PyCharm, GoLand, WebStorm, Android Studio）

## 文心快码（Baidu）

### 概要
Baiduの文心一言（ERNIE）をベースとするコーディングアシスタント。百度のクラウド・検索エコシステムに統合。
- Baidu AI Cloudとの連携が強み
- 中国国内のBaiduエコシステム開発者向け
- 詳細な技術情報は少なく、他の3ツールと比較してシェアは小さい

## ツール間比較（2026.04時点）

| 比較軸 | Trae (国際) | Trae CN | 通义灵码 | CodeGeeX |
|--------|-----------|---------|---------|----------|
| 価格 | $10/mo Pro | **無料** | 個人無料 | 個人無料 |
| 独自モデル | なし | 豆包/DeepSeek | Qwen-Coder-Qoder | CodeGeeX4-9B |
| エージェントモード | SOLO + Builder | SOLO | Quest + Agentic Chat | 基本Agent |
| IDE種類 | VS Code Fork IDE | VS Code Fork | Lingma IDE + Plugin | Pluginのみ |
| オープンソース | ❌ | ❌ | ❌ | ✅ |
| JetBrains対応 | ❌ | ❌ | ✅ | ✅ |
| Cloud IDE | ✅ | ✅ | ❌ | ❌ |
| Gartner認知 | ❌ | ❌ | ✅ (挑戦者) | ❌ |
| MAU/規模 | 100万+ | — | 国内最大級 | 100万+ |
| 海外対応 | ✅ (多言語) | ❌ | 限定的 | ❌ |

## 市場動向（2025-2026）

### 価格競争の激化
- ByteDanceはTrae CNを**完全無料**で提供し、国内シェア拡大を図る
- 通义灵码（Alibaba）も個人向け無料を継続、CodeGeeXも無料
- 国際市場ではTrae $10/mo vs Cursor $20/moの価格差が差別化要因

### 機能面の収束
- 全ツールがAgentモード（自律コード生成・実行）を標準搭載
- マルチモデルサポートが標準（豆包/DeepSeek/Claude/GPT等）
- MCP対応が進む（特にByteDance系はCoze/Trae連携）

### 中国市場の独自性
- VPN不要で使える国内版が優位（Trae CNはCursorが使えない中国開発者に人気）
- ByteDanceエコシステム（Douyin/今日頭条）とのコンテンツ連携が強み
- 企業向けはカスタマイズ・プライベートデプロイが重視される
- 2026年4月のVS Code 1.115リリースでは標準Agent機能が追加され、サードパーティツールとの競合が激化

## 2026年5月最新動向

### 1. Trae SOLO獨立Desktop/Webアプリ化とMTCモード

2026年3月31日、ByteDanceはTrae SOLOを**独立したDesktopアプリ・Web版**としてローンチ。従来はTrae IDE内蔵機能だったSOLOモードが、**任意の開発環境で使用可能**な独立製品に進化：

- **Desktopアプリ**: macOS/Windows対応、既存の任意IDEと併用可能
- **Web版**: ブラウザから直接SOLOモードを使用可能（登録不要のFree Tierあり）
- **Trae IDE版**: 従来通りIDE内蔵

#### MTC (More Than Coding) モード
SOLOモードが**コード生成の枠を超え**、以下の業務にも対応：
- UIデザイン・カンプからの実装
- API設計書からのコード自動生成
- プロジェクト管理タスクの自動化
- 技術文書生成・レビュー
- 出典: Juejin — [Trae SOLO独立Desktopアプリ発表](https://juejin.cn/post/7508138384481755172) [T2]

### 2. 通义灵码（Lingma）5月アップデート

Alibabaの通义灵码が2026年5月に主要アップデートを実施：

- **Agentic Ask mode**: 従来のチャット対話から、**Agentが能動的に質問・確認**するモードに進化。不完全な要件でもAgentが不足情報を自律的に収集
- **NES (Natural-language Enabled Search)**: 自然言語でコードベース全体を検索・理解
- **Inline Chat**: IDE内でインラインコード編集（選択範囲に直接修正提案）
- **Lingma IDE 正式版**: パブリックベータから正式版へ移行
- **通义灵码 VS Codeプラグイン非推奨化**: 新機能はLingma IDEにのみ追加。既存ユーザーはIDEへの移行を推奨
- 出典: 通义灵码公式 — [2026年5月更新ノート](https://lingma.aliyun.com/changelog/2026-05) [T1]

### 3. TRAE SOLO Mobile 三端同期リリース（2026年5月5日）

2026年5月5日、ByteDanceはTRAE SOLO Mobile（モバイル版）を正式リリース。Desktop・Web・Mobileの三端が完全同期：

- **App版**: iOS対応、Phone Pairing機能搭載（同アカウントのDesktopと自動ペアリング）
- **三端ワークフロー同期**: 手機で発行したタスクがDesktopに即座に表示、Desktopの進捗も手機で確認可能
- **Code / MTC デュアルモード**: Code（開発者向けコード・Diff・Git操作）とMTC（文書整理・データ分析・コンテンツ作成）をモバイルでも利用可能
- **飞书連携**: 飞书ドキュメントリンクをSOLOに貼り付け→自動解析。処理結果を飛書文書に直接書き戻し可能
- **Windows版同時リリース**: Desktop版がMacのみだった制約を解消
- **プロモーション**: 星巴克（Starbucks）とのコラボキャンペーン（5月5日-8日）、SOLO COFFEE TALKイベント（5月6日-6月15日）

> **出典**: 腾讯新闻 — [TRAE SOLO移动端全量上线](https://news.qq.com/rain/a/20260508A04MHS00) [T1]; 火山引擎开发者社区 — [TRAE SOLO移动端上线](https://developer.volcengine.com/articles/7636955544025464841) [T2]; 36kr — [TRAE SOLO龙虾化](https://www.36kr.com/p/3747994426897156) [T1]

### 4. 腾讯CodeBuddy計費改定とWorkBuddy統合（2026年5月15日）

- **計費方案改定**: CodeBuddy企業旗艦版が78元/人/月→198元/人/月へ値上げ。WorkBuddyとの統合サブスクリプションに移行
- **WorkBuddy統合**: 1アカウントでCodeBuddy（プログラミング支援）とWorkBuddy（AI Workplaceデスクトップエージェント）を同時利用可能に
- **CloudAgent新機能**: 企業がカスタムAgentをクラウド上で定義・共有可能。各メンバーに獨立サンドボックスインスタンス
- **CodeBuddy NES（Next Edit Suggestions）**: コード補完の次世代機能。現在行だけでなく後続のコードブロック全体を予測して提案する「写一补十」方式
- **Plan/Craft/Ask 3モード**: 複雑度に応じてPlan（自治型）、Craft（局所編集）、Ask（対話型）を切替可能
- **CodeBuddy Skills・MCP**: ユーザー/プロジェクト設定でSkills定義、MCP経由のサードパーティツール統合に対応

> **出典**: 腾讯云 — [CodeBuddy計費改定公告](https://cloud.tencent.com/announce/detail/2270) [T1]; 腾讯云 — [CodeBuddy製品概要](https://cloud.tencent.com/developer/article/2653581) [T1]; 36kr — [TRAE SOLO龙虾化](https://www.36kr.com/p/3747994426897156) [T1]

### 5. 競争環境変化

- **Trae $10/mo vs Cursor $20/mo**: Trae Proの価格差が国際市場で顕著な差別化要因に。中国版Trae CNは完全無料を継続
- **VS Code 1.115 Agent機能**: 2026年4月、VS Code標準機能としてAgentモードが追加。サードパーティツール（Trae・Cursor等）との競合が新段階に
- **国内ネットワーク問題の解決策**: ofox.ai等のAPI仲介プラットフォームがClaude Code・Cursor API・Gemini CLIの中国国内利用を可能に
- 出典: 各種開発者フォーラム・V2EX議論 [T3]

### 6. 通义灵码 → Qoder CN リブランド（2026.05.20）

**5月20日**、Alibaba（阿里巴巴）が通义灵码（Lingma）の**国際ブランド「Qoder CN」へのリブランド**を発表：

- **名称変更**：通义灵码（Tongyi Lingma） → **Qoder CN**（英文ブランド名「Qoder」の中国版として位置づけ）
- **背景**：
  - AlibabaのQwenモデルファミリーと統合ブランド戦略
  - 「Lingma」から「Qoder」への統一により、グローバル市場でのブランド認知向上
  - Qoderは国際版、Qoder CNは中国国内版としての整理
- **既存機能は継続**：Agentic Ask、NES、Inline Chat、Lingma IDE等の機能はQoder CNに引き継がれ、機能削減なし
- **製品体系**：
  - **Qoder CN**: 中国国内向け（旧通义灵码）。百炼プラットフォーム経由
  - **Qoder**: 国際向け。Qwen3.7-Max搭載、グローバル展開
  - **Lingma IDE**: ブランド名は当面維持。バックエンドはQoderに統合
- **今後の展開**：Qoder CNはQwen3.7-Max（Agent-firstモデル）との連携を強化。自律エージェント機能が中核に

> **出典**: Alibaba Cloud Summit 2026（5月20日）、36kr、量子位 [T1]

## 2026年6月上旬更新 — AIプログラミングパラダイムの大転換期

### 1. AIプログラミングパラダイムの転換 — 「Vibe Coding」から「Agentic Engineering」へ（6月上旬）

36kr記事（6月8日）「大人，AI编程又变天了，Claude Code之父、龙虾创始人同时力捧新范式，杀死提示词工程？」で、Claude Codeの父（所属組織）とOpenClaw（龙虾）の創設者が同時に「新パラダイム」を宣言：

- **プロンプトエンジニアリングの終焉**：従来のプロンプト設計・調整の時代は終わり、**Agent Orchestration時代**に移行
- **Claude Code 100万行リライト事件**（6月初旬）：BunのコードベースをClaude Codeで9日間・6,755コミット・99.8%テスト通過率で全書き換え
- **Anthropic内製80%コードAI生成**：トレーニングコード52倍高速化。Mythos 5トレーニングで実証
- **意義**：中国国内のコーディングアシスタントも、このパラダイム転換の影響を受ける。コード生成の「量」から「エージェント・ワークフロー品質」への競争軸シフト

> **出典**: 36kr — [AI编程又变天了](https://36kr.com/p/3844224911346184) [T1]

### 2. Kimi Work — 中国版Codexではなく「Vibe Working」ツール（6月8日）

36krの詳細分析記事（6月8日）「Kimi Work不是中国版Codex」が大きな話題に：

- **Kimi Work**（6月3日Beta開始）は**「中国版Codex」としての位置づけを明確に否定**
- プログラマー向けコードエージェントではなく、**知識ワーカー向けVibe Workingツール**として差別化
- WebBridge（ブラウザ操作）＋Agent Cluster（K2.5由来）＋専門データベース（同花順・天眼查等）を統合
- **コアユーザー**: プログラマーではない一般知識ワーカー（マーケター、アナリスト、研究者）
- これにより中国AIコーディングアシスタント市場は「Codex型（コード特化）」と「Kimi Work型（知識ワーク）」に二極化する可能性

> **出典**: 36kr — [Kimi Work不是中国版Codex](https://36kr.com/p/3844257852885256) [T1]

### 3. 豆包MarsCode — Codex統合戦略（6月8日）

36kr（6月8日）「拿'Codex'当馅儿，豆包才值钱」：

- ByteDanceが豆包（Doubao）の価値を高める手段としてCodex互換機能を戦略的に位置づけ
- 豆包の商業化（有料課金）とEC/団購への拡大と並行して、AIプログラミング機能を差別化要素に
- 豆包MarsCodeはDeepSeek V4統合による低価格路線を継続

> **出典**: 36kr — [拿'Codex'当馅儿，豆包才值钱](https://36kr.com/p/3844260642634375) [T1]

### 4. 開発者コミュニティの動き — Claude Code→Kimi K2.5への移行（6月上旬）

- **掘金記事（6月7日）**「Claude Code换成了Kimi K2.5后，我再也回不去了」：Kimi K2.5への移行体験がホットトピックに
- **掘金（6月7日）**「智谱GLM-5这次开源，让高级程序员也危险了」：GLM-5のオープンソース化がコード生成の民主化を加速
- **掘金（6月9日）**「Codex大更新！不只写代码，6套职业技能，开始接手知识工作流」：Codexが知識ワーカー向けにも進化
- **Codex第三社API対応**: CodexからDeepSeek/GLM/Kimiを直接利用可能に（6月3日確認）

> **出典**: 掘金 — 各記事 [T1/T2]

### 5. Trae/Qoder/CodeGeeXの6月状況

6月1日〜9日期間に、**Trae SOLO、Qoder CN、CodeGeeXの目立ったメジャーアップデートはなし**：

| ツール | 6月上旬の状況 |
|--------|-------------|
| **Trae SOLO** | 前回5月5日Mobile版リリース以降、メジャーアップデートなし。独立Desktop版・MTCモードは安定期 |
| **Qoder CN** | 5月20日リブランド以降、新機能発表なし。Qwen3.7-Max連携強化が継続中と推定 |
| **CodeGeeX** | GLM-5.1ベースのコード生成が掘金で話題に。新バージョンリリース情報なし |

- **Qoder市場シェア47.6%（IDC公式）**: 2026年7月、IDC「2025中国AI编程市場份额」レポートでQoderが47.6%を獲得し国内1位を確認。智谱・商汤・腾讯・百度の合計を上回る
- **Claude Codeバックドア問題（7月）**: 中国ユーザー識別コード発覚 → Alibaba社内全Claudeソフト禁止 → 国家脆弱性DB（CNNVD）警告。国産ツールへの移行が不可逆的に加速
- **7/24〜8/5にTrae・CodeGeeX・MarsCodeの目立ったメジャーアップデートなし**: 各ツールは既存機能の安定運用フェーズ
- 代わりに**Agent Orchestrationパラダイム**や**Kimi Work型知識ワーカーツール**など、競争軸の多様化が顕著

> **出典**: IDC "2025中国AI编程市場份额" (2026-07), CNNVD警告 (2026-07-08), 各種開発者フォーラム

中国発コーディングアシスタント市場は**機能の安定化・コミュニティ浸透フェーズ**に移行
- 代わりに**Agent Orchestrationパラダイム**や**知識ワーカー向けツール**（Kimi Work）など、競争軸の多様化が顕著

## 出典
- ByteDance Trae公式: [trae.ai](https://www.trae.ai) [T1]
- 通义灵码公式: [lingma.aliyun.com](https://lingma.aliyun.com) [T1]
- CodeGeeX: 智譜AI公式発表・GitHub [T1]
- 百度百科「豆包MarsCode」 [T2]
- Gartner AI Code Assistantレポート [T2]
- trae-vs-cursor比較 (codepick.dev) [T2]
- 36氪報道: 字节跳动发布豆包MarsCode [T1]
