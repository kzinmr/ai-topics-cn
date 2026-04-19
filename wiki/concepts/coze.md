---
title: "扣子 (Coze) — ByteDanceのノーコードAI Agentプラットフォーム"
created: 2026-04-19
updated: 2026-04-19
tags: [agent-platform, low-code, bytedance, china, workflow, plugin]
aliases: ["Coze", "扣子", "字节跳动Coze", "Coze平台"]
source_lang: zh-CN
---

# 扣子 (Coze) — ByteDanceのノーコードAI Agentプラットフォーム

> **重要度**: 🔥🔥 MEDIUM — 中国Agentエコシステムの重要プレイヤー
> **関連概念**: [[china-ai-agent-ecosystem]], [[agent-skills]], [[dify]], [[mcp]]
> **関連エンティティ**: [[doubao-bytedance]], [[tencent-ai]], [[qwen]]

## 概要

**扣子（Coze）**はByteDance（字节跳动）が開発した**ノーコード/ローコードAI Agent構築プラットフォーム**。2024年に中国国内版がリリースされ、2026年4月現在、DAU 500万以上、登録Agent数100万超に成長。

「**搭积木一样做AI应用**」（ブロックを組み立てるようにAIアプリを作る）をスローガンに、技術者以外のマーケター・デザイナー・ビジネスパーソンが独自のAI Agentを作成できる。

## 核心機能

### 1. ビジュアルワークフローエディタ
ドラッグ&ドロップで**条件分岐・API呼び出し・データベース連携・LLM推論**を組み合わせ。ノードベースのUIにより、複雑なビジネスロジックをコードなしで構築可能。

- **トリガー**: スケジュール/イベント/手動実行
- **アクション**: HTTPリクエスト、DBクエリ、ファイル操作、LLM呼び出し
- **分岐**: 条件判定、ループ、エラーハンドリング

### 2. Pluginマーケットプレイス
1,000+の公式・コミュニティPluginが利用可能：
- **検索**: 百度搜索、Sogou、Bing
- **SNS**: WeChat公式アカウント、微博、小紅書
- **業務**: Feishu（飛書）、DingTalk（釘釘）、企業微信
- **データ**: 天気、株価、翻訳、OCR

### 3. 知識庫（ナレッジベース）
PDF・Word・Excel・Webページをアップロードし、**RAG（検索拡張生成）**でAgentの知識を拡張。中国語特化のエンベディングモデルにより、日本語・英語混在ドキュメントにも対応。

### 4. マルチモデル対応
扣子自体はモデルを提供せず、**バックエンドモデルを選択可能**：
- Doubao（ByteDance自社モデル）
- Qwen（Alibaba）
- GLM（Zhipu AI）
- GPT（OpenAI、接続制限あり）
- Claude（Anthropic、KYC制限あり）

## 中国国内版と国際版の違い

| 項目 | 国内版 (扣子) | 国際版 (Coze) |
|------|---------------|---------------|
| 提供元 | 字节跳动 | ByteDance Pte. Ltd. |
| 主要モデル | Doubao/Qwen/GLM | GPT/Claude/Gemini |
| Plugin | 中国SaaS特化 | グローバルSaaS |
| 決済 | 微信/支付宝 | クレジットカード |
| 規制 | 算法备案済み | GDPR対応 |

## 業界適用事例

| 業界 | 使用例 | Agent構成 |
|------|--------|-----------|
| **EC** | カスタマーサービスAgent | 知識庫(RAG) + 注文API + Doubao |
| **教育** | AIチューター | ワークフロー(診断→解説→演習) + Qwen |
| **メディア** | コンテンツ自動生成 | Plugin(検索→要約→投稿) + GLM |
| **金融** | リスク評価レポート | データ分析 + 条件分岐 + Doubao-Pro |

## 課題

1. **複雑ロジックの限界**: 大規模ワークフローは可読性が低下。「コードを書く方が早い」ケースが存在
2. **モデル依存**: バックエンドモデルの性能上限に制約される。Doubao単体ではGPT-4/Claude Opusに追いつかない
3. **コスト**: 無料枠は月100リクエストまで。Enterpriseプランは月額数万元

## 関連リンク

### 内部リンク
- [[china-ai-agent-ecosystem]] — 中国Agentプラットフォーム全景
- [[dify]] — オープンソース対抗馬
- [[doubao-bytedance]] — ByteDanceのAIチャットアプリ
- [[agent-skills]] — Agent能力定義

### 外部ソース
| ソース | URL | ティア | 概要 |
|--------|-----|--------|------|
| 扣子公式サイト | [coze.cn](https://www.coze.cn) | T1 | プラットフォーム本体 |
| 掘金 — 扣子ワークフロー | [juejin.cn](https://juejin.cn) | T2 | ハンズオンチュートリアル |
| 知乎 — 扣子vsDify比較 | [zhihu.com](https://www.zhihu.com) | T2 | プラットフォーム比較 |
