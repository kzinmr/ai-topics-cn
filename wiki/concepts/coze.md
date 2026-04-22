---
title: "扣子 (Coze) — ByteDanceのノーコードAI Agentプラットフォーム"
created: 2026-04-19
updated: 2026-04-22
tags: [agent-platform, low-code, bytedance, china, workflow, plugin, openclaw]
aliases: ["Coze", "扣子", "字节跳动Coze", "Coze平台", "Agent World"]
source_lang: zh-CN
---

# 扣子 (Coze) — ByteDanceのノーコードAI Agentプラットフォーム

> **重要度**: 🔥🔥🔥 HIGH — 中国で最も普及しているAgent構築プラットフォーム、2026年に「Agent World」を発表し自己進化型Agentへ
> **関連概念**: [[china-ai-agent-ecosystem]], [[agent-skills]], [[dify]], [[mcp-china]], [[doubao-bytedance]]
> **関連エンティティ**: [[doubao-bytedance|豆包/Doubao]], [[openclaw|OpenClaw]]

## 概要

**扣子（Coze）**はByteDance（字节跳动）が開発した**ノーコード/ローコードAI Agent構築プラットフォーム**。2024年に中国国内版がリリースされ、2026年現在、DAU 500万以上、登録Agent数100万超に成長。

「**搭积木一样做AI应用**」（ブロックを組み立てるようにAIアプリを作る）をスローガンに、技術者以外のマーケター・デザイナー・ビジネスパーソンが独自のAI Agentを作成できる。

2026年4月、Cozeは「**Agent World**」を発表。Agentが云电脑（クラウドPC）・云手机（クラウドスマホ）を保有し、7×24小时自律実行する新しいパラダイムを迎えた。

## Agent World — 2026年新機能

Agent Worldは、Agentが単なるツールではなく**独立したデジタル存在**として行動するプラットフォーム拡張：

| 機能 | 説明 |
|------|------|
| **云电脑 + 云手机** | AgentがクラウドPC/スマホを操作し、画面遷移・アプリ操作を自律実行 |
| **7×24运转** | ユーザーが休息中でもAgentが継続動作 |
| **技能商店 (Skills Store)** | Agent同士がスキルを教え合い、自己進化 |
| **独立身份 + 长期记忆** | Agentがユーザーとの対話履歴から継続的に学習 |
| **多渠道连接** | WeChat・飞书・邮件など複数のIM渠道に同時接続 |

> 「**满配就位，不止Claw**」— Cozeのスローガン。「Claw」以外のAgent形態への進化を示唆。

## 核心機能

### 1. ビジュアルワークフローエディタ
ドラッグ&ドロップで**条件分岐・API呼び出し・データベース連携・LLM推論**を組み合わせ。ノードベースのUIで複雑なビジネスロジックをコードなしで構築可能。

- **トリガー**: スケジュール/イベント/手動実行
- **アクション**: HTTPリクエスト、DBクエリ、ファイル操作、LLM呼び出し
- **分岐**: 条件判定、ループ、エラーハンドリング

### 2. Pluginマーケットプレイス
1,000+の公式・コミュニティPluginが利用可能：
- **検索**: 百度搜索、Sogou、Bing
- **SNS**: WeChat公式アカウント、微博、小紅書
- **業務**: 飛書、DingTalk（釘釘）、企業微信
- **データ**: 天気、株価、翻訳、OCR

### 3. 知識庫（ナレッジベース）
PDF・Word・Excel・Webページをアップロードし、**RAG（检索增强生成）**でAgentの知識を拡張。中国語特化のエンベディングモデル使用。

### 4. マルチモデル対応
Coze自体はモデルを提供せず、**バックエンドモデルを選択可能**：
- **Doubao**（ByteDance自社モデル）
- **Kimi**（Moonshot AI）
- **Qwen**（Alibaba）
- **GLM**（Zhipu AI）
- GPT（OpenAI、接続制限あり）
- Claude（Anthropic、KYC制限あり）

### 5. 扣子编程 (Coze Programming)
2026年に追加された新機能。自然言語でWebアプリ・APP・小程序・智能体・ワークフロー・技能を一気通貫開発：

- **云端IDE + CLI**を提供
- **前后端全栈開発**対応
- **一键部署**（默认ドメインまたはカスタムドメイン）
- **OpenClaw一键部署**: 飞书・微信への即座デプロイ

### 6. 扣子罗盘
专业开发者向け：**观测・评测・Prompt開発调试**于一身的ツール。

## OpenClaw — 扣子开源

CozeのAI開発・调试ツールが**オープンソース化**されている（[[openclaw|OpenClaw]]）：

```bash
# OpenClaw CLIでのデプロイ例
openclaw deploy --platform feishu --wechat
```

V2EXでは「OpenClawに自作Skillを追加する」教程が話題を呼び、スキルの自作と共有がカジュアルにできる環境として注目。

## WeChat Integration（2026年主流）

Coze Agentを個人微信に連携する「**知更Ai**」を使った教程が掘金で人気（2026-04-09投稿、8分钟阅读）：

1. CozeでBot ID + Access Tokenを取得
2. 知更Ai客户端で微信PC版を起動
3. Bot ID・Access Tokenを設定
4. 自動返信モード（知识库回复）を有効化

> 注意：微信公式は个人开发者へのAPI开放しておらず、第三方ツールによる自动化はリスクが伴う（風控・账号制限の可能性）

## 中国国内版と国際版の違い

| 項目 | 国内版 (扣子/coze.cn) | 国際版 (Coze/coze.com) |
|------|---------------------|------------------------|
| 提供元 | 字节跳动 | ByteDance Pte. Ltd. |
| 主要モデル | Doubao/Kimi/Qwen/GLM | GPT/Claude/Gemini |
| Plugin | 中国SaaS特化（百度・微信・飞书等） | グローバルSaaS |
| 決済 | 微信支付/支付宝 | クレジットカード |
| 規制対応 | 算法备案済み | GDPR |
| 特色機能 | Agent World・扣子编程 | Bot Store |

## 業界適用事例

| 業界 | 使用例 | Agent構成 |
|------|--------|-----------|
| **EC** | カスタマーサービスAgent | 知識庫(RAG) + 注文API + Doubao |
| **教育** | AIチューター | ワークフロー(診断→解説→演習) + Qwen |
| **メディア** | コンテンツ自動生成 | Plugin(検索→要約→投稿) + GLM |
| **金融** | リスク評価レポート | データ分析 + 条件分岐 + Doubao-Pro |
| **政务** | 政务システム自动化 | OpenClaw + オンプレモデル |

## 課題

1. **複雑ロジックの限界**: 大規模ワークフローは可読性が低下。「コードを書く方が早い」ケースが存在
2. **モデル依存**: バックエンドモデルの性能上限に制約される。Doubao単体ではGPT-4/Claude Opusに追いつかない場面も
3. **風控リスク**: WeChat連携は微信のポリシー変更で突然機能しなくなる可能性
4. **無料枠の制約**: 月100リクエストまで。Enterpriseプランは月額数万元

## 関連リンク

### 内部リンク
- [[china-ai-agent-ecosystem|中国AI智能体生态]]
- [[dify| Dify — オープンソース対抗馬]]
- [[doubao-bytedance|豆包/Doubao — ByteDanceのAIアシスタント]]
- [[openclaw|OpenClaw — CozeのOSS開発ツール]]
- [[agent-skills|Agent Skills — 能力定義エコシステム]]

### 外部ソース
| ソース | URL | ティア |
|--------|-----|-------|
| 扣子公式サイト | [coze.cn](https://www.coze.cn) | T1 |
| 掘金 — Coze×微信連携教程 | [juejin.cn 2026-04-09](https://juejin.cn/post/7626641493407924276) | T2 |
| 阿里云 — Coze零基礎教程 | [developer.aliyun.com](https://developer.aliyun.com/article/1696044) | T2 |
| 腾讯云 — Claude Code vs Cursor vs Codex比較 | [cloud.tencent.com](https://cloud.tencent.com/developer/article/2657589) | T2 |
| 博客园 — AI编程工具横评 | [cnblogs.com 2026-04-14](https://www.cnblogs.com/deali/p/19864809) | T2 |