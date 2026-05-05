---
title: "中国AIコーディングアシスタント — Trae・MarsCode・通义灵码・CodeGeeX"
created: 2026-04-28
updated: 2026-05-05
tags: [coding-agents, tooling, china, product-comparison, ide]
aliases: ["中国AI编程助手", "China AI Coding Assistants", "Trae", "MarsCode", "通义灵码", "CodeGeeX", "Lingma"]
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

### 3. 競争環境変化

- **Trae $10/mo vs Cursor $20/mo**: Trae Proの価格差が国際市場で顕著な差別化要因に。中国版Trae CNは完全無料を継続
- **VS Code 1.115 Agent機能**: 2026年4月、VS Code標準機能としてAgentモードが追加。サードパーティツール（Trae・Cursor等）との競合が新段階に
- **国内ネットワーク問題の解決策**: ofox.ai等のAPI仲介プラットフォームがClaude Code・Cursor API・Gemini CLIの中国国内利用を可能に
- 出典: 各種開発者フォーラム・V2EX議論 [T3]

## 出典
- ByteDance Trae公式: [trae.ai](https://www.trae.ai) [T1]
- 通义灵码公式: [lingma.aliyun.com](https://lingma.aliyun.com) [T1]
- CodeGeeX: 智譜AI公式発表・GitHub [T1]
- 百度百科「豆包MarsCode」 [T2]
- Gartner AI Code Assistantレポート [T2]
- trae-vs-cursor比較 (codepick.dev) [T2]
- 36氪報道: 字节跳动发布豆包MarsCode [T1]
