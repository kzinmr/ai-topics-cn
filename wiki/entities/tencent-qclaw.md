---
title: "Tencent QClaw Agent — 騰訊の極簡AIエージェントプラットフォーム"
created: 2026-04-28
updated: 2026-04-28
tags: [company, ai-agents, china, tencent, open-source, agent-platform]
aliases: ["QClaw", "QClaw Agent", "腾讯QClaw", "OpenClaw China"]
source_lang: zh-CN
---

# Tencent QClaw Agent — 騰訊の極簡AIエージェントプラットフォーム

> **開発元**: Tencent（騰訊）
> **ベースフレームワーク**: OpenClaw（Peter Steinberger）
> **最新バージョン**: V2（V0.2.5、2026年4月13日）
> **海外版ベータ**: 2026年4月22日開始
> **重要度**: 高 — 中国10日で100万ユーザー、Agent実用化の最前線

## 概要

**QClaw**はTencentがOpenClawオープンソースフレームワークをベースに開発した「極簡（ミニマル）」AIエージェントプラットフォーム。開発者向けOpenClawを一般消費者向けにラップしたもので、「ダウンロード→インストール→扫码（QRコードスキャン）」の3ステップ約3分で利用開始できる。国内版は微信小程序（WeChat Mini Program）を入口とし、海外版はWhatsApp/Telegramに対応。2026年4月時点で国内10日で100万ユーザーを達成。

## 製品哲学

- **"Do less, Live more"**: 複雑な設定不要、即時利用
- **零コードAI Agent**: 技術知識不要でAgentを活用
- **ローカル実行**: データはユーザーデバイス上で処理、クラウド非依存
- **自己進化**: 海外版は99%のコードをQClaw自身が書いて開発（5日間）

## バージョン履歴

### V2（V0.2.5、2026年4月13日）— 国内版メジャーアップデート

**3大核心機能**:

#### 1. マルチAgent協働
- 最大**3つのAgentを並列実行**可能
- 各Agentの性格・口調・経験をカスタマイズ
- 3つのプリセットAgent:
  - **「无不言」**: 毒舌コメンテーター
  - **「林且慢」**: 父親系カウンセラー
  - **「代可行」**: 実務派プログラマー

#### 2. 跨アプリ直連（コネクター）
- **一度の扫码で永続接続**（再ログイン不要）
- 対応アプリ: 腾讯文档、腾讯会議、ima、金山文档、腾讯问卷、Notion、メール
- AIがコンテンツ生成後、**直接ドキュメント作成やメール送信**を実行
- シーン別テンプレートで2ステップで接続完了

#### 3. 龙虾管家（セキュリティモジュール）
- 業界初の組み込みAI安全ガード
- プロンプト・スキル・実行スクリプトを**リアルタイム監視**
- 高リスク操作を自動ブロック
- 詳細なセキュリティログ記録

### 海外版ベータ（2026年4月22日）

**リリース状況**:
- 対象国: アメリカ、カナダ、シンガポール、韓国など
- ログイン: Googleアカウント（今後追加予定）
- 対応IM: **WhatsApp**、**Telegram**
- 言語: 中国語、英語、フランス語、スペイン語、韓国語

**3つのコア使用モード**:
1. **QClaw it**: 高頻度・複雑な日常業務の自動化
   - 例: IRS（米国国税庁）サイトからの税務フォームDL→入力→申告→最適化案作成
2. **QClaw Daily**: 日常的な自己管理
   - 例: パーソナルフィットネスコーチ、トレーニング計画→進捗追跡→可視化
3. **QClaw Up**: 専門分野サポート
   - 例: SNS運営方法论の学習→コンテンツ企画→運営代行（3日で200+フォロワー増の事例）

**QClaw Playground（专家広場）**:
- フィットネスコーチ、金融アドバイザー、言語教師などのプリセット专家角色
- 「我想要（欲しい）」をクリックするだけで数秒でAgentが準備完了

**ベータ特典**:
- 1日**4,000万token無料**（最大$700/日の価値）
- 先着20,000名の「Founding Claw（創始龙虾）」枠

### v0.1.9（2026年3月18日）— 初期版

- 微信小程序入口
- 靈感広場（プリセットSkills）
- タスク検索・管理
- 定時タスク区分

## 技術アーキテクチャ

```
ユーザー層: 微信小程序 / WhatsApp / Telegram
     ↕
サーバー層: 腾讯云ホスティング
     ↕
実行層: ローカルQClawクライアント
     ↕
コア層: OpenClaw Core（MCPプロトコル + Skills編成）
     ↕
モデル層: 混元Hy3 / 他社LLM（APIキーでカスタム可能）
```

### 要件
| プラットフォーム | 要件 |
|----------------|------|
| **Windows** | Win 10 1903+ / Win 11、64bit、4GB+ RAM |
| **macOS** | 10.15+、Intel / Apple Silicon両対応 |
| **ネットワーク** | 腾讯云APIエンドポイントへのアクセス（企業内网はホワイトリスト設定必要） |

## OpenClawとの関係

QClawはOpenClawの**極簡パッケージ版**。OpenClaw創設者のPeter SteinbergerはソーシャルメディアでTencentチームに謝意を表明。両者は協力してOpenClawテストフレームワークの性能向上を図り、修正をオープンソースリポジトリに還元した。

**住み分け**:
- **QClaw**: 入門・検証・日常利用向け
- **OpenClaw**: 深度カスタマイズ・開発者向け

**移行パス**: QClawでニーズを明確化 → OpenClawで深度カスタマイズ

## 混元との統合

QClawのデフォルトLLMプロバイダーは**腾讯混元（Hunyuan）**。Hy3 Previewのリリースにより、QClawはより高度なAgentタスク（コード生成、複雑なコンテキスト理解、マルチステップ推論）を実行可能になった。

Tencentの2025年度業績公告では、混元3.0、元宝、WorkBuddyと並びQClawが「AI投資が実際の効果を上げたプロジェクト」として列挙されている。

## 市場インパクト

- **10日で100万ユーザー**: 国内リリース後の爆発的成長
- **Agent実用化の象徴**: ChatbotからAgentへの移行を一般消費者レベルで体現
- **微信エコシステムとの統合可能性**: WeChat（13億ユーザー）との連動が噂される
- **海外展開**: 中国AI製品のグローバル展開の最前線ケース

## 競合

| 製品 | 開発元 | 特徴 | ターゲット |
|------|--------|------|-----------|
| **QClaw** | Tencent | 極簡、微信/WhatsApp統合、ローカル実行 | 一般消費者 |
| **OpenClaw** | Peter Steinberger | オープンソース、深度カスタマイズ | 開発者 |
| **Claude Code** | Anthropic | コーディング特化、Skills/MCP統合 | 開発者 |
| **Kimi** | Moonshot AI | 長文コンテキスト、コーディング | 開発者/学生 |
| **豆包** | ByteDance | 推薦アルゴリズム、システムレベル統合 | 一般消費者 |

## 関連

- [[tencent-ai]] — 親組織
- [[tencent-hunyuan]] — QClawのベースLLM
- [[openclaw]] — オープンソースベースフレームワーク
- [[mcp-china]] — 中国MCPエコシステム
- [[china-ai-superapp-race]] — 中国AIスーパーアプリ競争
- [[agent-skills]] — AIエージェントのモジュール型能力システム

## ソース

- [QClaw V2リリース — 腾讯云開発者コミュニティ](https://cloud.tencent.com/developer/article/2653629)
- [QClaw海外版ベータ発表 — 腾讯云](https://cloud.tencent.com/developer/article/2658243)
- [QClaw v0.1.9技術解説 — 腾讯云開発者コミュニティ](https://developer.cloud.tencent.com/article/2640971)
- [Tencent QClaw Global Launch — Tencent公式](https://www.tencent.com/en-us/articles/2202318.html)
- [TechWeez — QClaw Overseas Analysis](https://techweez.com/2026/04/21/tencent-qclaw-ai-agent-overseas-launch/)
