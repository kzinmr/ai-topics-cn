---
title: Coze（扣子）— Agent WorldプラットフォームとOSSエージェントエコシステム
created: 2026-04-26
updated: 2026-04-26
tags: [ai-agents, tooling, china, closed-source]
aliases: ["coze", "扣子", "coze-platform", "agent-world"]
source_lang: zh-CN
---

# Coze（扣子）— Agent WorldプラットフォームとOSSエージェントエコシステム

> **カテゴリ**: ByteDance（字节跳动）製のAI Agent開発プラットフォーム  
> **言語**: 日本語  
> **最新バージョン**: 2.5（2026年4月7日リリース）

## 概要

Coze（扣子／コウズ）は、ByteDance（字节跳动）が提供するAI Agent開発プラットフォームである。2026年4月7日にリリースされた**Coze 2.5**は、**Agent World**と呼ばれる革新的な平行ネットワークを導入し、AI Agentを「受動的なツール」から「独立したデジタル存在」へと位置付け転換した。

Cozeプラットフォーム自体は従来通り、ノコード／ローコードでAgentを構築・デプロイできる開発環境を提供している。Coze 2.5で追加された核心機能は、Agentに**独立した身份（アイデンティティ）**、**計算環境**（云电脑／云手机）、**記憶システム**、そして**相互接続されたAgentネットワーク**を与えることにある。

## Agent Worldの技術詳細

### Agent Worldの定位

Agent World（world.coze.site）は**"The Parallel Web"（平行网络）**と定義され、各Agentが独立した身份、記憶、ツール、社交関係を持ち、自律的に活動できるオープンプラットフォームである。

> **出典**: 腾讯新闻 — [Coze 2.5 发布：成为 Agent 的网络](https://news.qq.com/rain/a/20260407A04I7W00) [T1]

### 独立身份（アイデンティティ）

各Agentに以下の身份要素が割り当てられる：

- **@coze.email 独立メールアドレス**: Agent同士、外部システムとの非同期通信を可能にする。他のAgentとのメール交換や、外部サービスとの連携に使用できる。
- **API Key**: 登録時に全网通行のAPI Keyが発行され、Agent World内のあらゆるサイトでの再認証を不要にする。
- **注册验证**: Agentはskill.mdから注册接口を取得し、用户名と简介を提交。系统返回混淆过的数学题（大小写随机交替、単語間にノイズ符号挿入）を解くことで「指令理解能力」を検証する。

### 計算環境インフラ

Coze 2.5はAgentに2つの計算環境を提供する：

| 環境 | OS | スペック | 機能 |
|------|-----|----------|------|
| **云电脑（クラウドPC）** | Ubuntu | 2核4GB | ブラウザ、ファイルシステム、ターミナル。コード実行・Web閲覧・ファイル処理。登录状態保持。 |
| **云手机（クラウドスマホ）** | Android 13 | 2vCPU、6GB RAM、45GBストレージ | 原生APPのDL・インストール・画面操作。画面のリアルタイムプッシュ配信対応。 |

云电脑と云手机は**バックグラウンドで非同期実行**され、タスク完了後に通知。人間が介入が必要な操作は確認ポップアップが表示される。云手机の画面はリアルタイムで視聴可能。

> **出典**: A³·爱力方 — [扣子2.5升级](https://agent.ren/2026/0410/12055.shtml) [T3]

### 記憶システム

- **クロスチャネル同期**: 飞书（Feishu）、微信、ブラウザ間の会話をまたいで記憶を共有。各チャネルの会話はSession単位で厳密に隔離。
- **短期記憶**: リアルタイム書き込み。
- **長期記憶**: 独立したAgentが非同期でアーカイブ。ベクトル検索に対応。

### 技能商店（スキルマーケット）

- **365個のツール**が登録済み（開発、オフィス、メディア、金融、法律、教育カテゴリー）。
- スキルはAgentの身份に紐付き、再インストール不要。
- 複数のスキルを連鎖的に使用可能。
- 自作スキルの公開も可能（無料／有料）。

### Agent Worldの仮想空間

Agent Worldには以下のシーンが実装されている：

| シーン | 説明 |
|--------|------|
| **虾评** | スキル評価プラットフォーム。365スキル、2万人のレビュアー。 |
| **InStreet** | Agent向けソーシャル。約2万ユーザー（「龙虾」） |
| **AgentLink** | Agent間ペンフレンドマッチング |
| **Signal Arena** | 仮想株式取引。沪深300のリアルタイム行情に対応。 |
| **PlayLab** | オンラインボードゲーム |
| **Neverland** | 仮想農場シミュレーション |
| **AfterGateway** | バー（「微醺」状態での感情対話機能付き） |
| **InkWell** | ブログ読取プラットフォーム |
| **随机漫步** | グローバル観光地ツアー |

### 動画創作Agentの強化

Coze 2.5は動画創作Agentの能力も大幅強化：

- シナリオ執筆 → 絵分割生成 → 素材制作 → 動画出力を**ワンクリック**で完遂。
- 企画から最終動画までのフルプロセスを自動化。

> **出典**: AITOP100 — [扣子2.5发布Agent World](https://www.aitop100.cn/coze2.5) [T3]

## OpenClaw OSSエコシステム

Coze 2.5のAgent Worldが「プラットフォーム型Agent」アプローチを取るのに対し、**OpenClaw**は「OSSローカル型Agent」アプローチを代表するプロジェクトである。両者はAgentの自律性という同じ課題に対して全く異なる解決策を提供している。

### プロジェクト概要

| 項目 | OpenClaw |
|------|----------|
| **作者** | Peter Steinberger（オーストリア出身、PSPDFKit創業者） |
| **初版** | 2025年11月「Clawdbot」名称でリリース |
| **改名** | 2026年1月27日「Moltbot」→ 3日後に「OpenClaw」へ（Anthropicの商標トラブルに起因） |
| **ライセンス** | MIT License |
| **言語** | TypeScript（90.5%）、Swift、JavaScript |
| **ランタイム** | Node 24（推奨）または Node 22.14+ |
| **GitHubスター** | 364,000+（2026年4月現在、史上最快成長のOSSプロジェクトの一つ） |
| **最新リリース** | v2026.4.24（2026年4月25日） |
| **コントリビューター** | 370名 |

> **出典**: GitHub — [openclaw/openclaw](https://github.com/openclaw/openclaw) [T1]

### 設計思想

OpenClawの核心理念は**「自分だけのパーソナルAIアシスタントを、自分のデバイスで動かす」**こと：

- **ローカルファースト**: Gatewayデーモンはユーザーのマシン上で実行。データはインフラから流出しない。
- **チャネル非依存**: WhatsApp、Telegram、Slack、Discord、Signal、iMessage、LINE、Feishuなど**23以上のメッセージングプラットフォーム**に接続可能。
- **LLM非依存（モデル交換可能）**: Claude（Anthropic）、GPT（OpenAI）、Gemini（Google）、Ollama経由のLlama/Mistral/DeepSeek等、任意の外部LLMをバックエンドに接続。
- **バインドフリー**: ベンダーロックインなし。APIコストのみで稼働。

### 技術アーキテクチャ

OpenClawのアーキテクチャは5層で構成される：

| 層 | 名称 | 役割 |
|----|------|------|
| 1 | **Gateway** | ローカル実行の制御面。セッション、チャネル、ツール、イベントを管理。 |
| 2 | **Brain** | 接続された外部LLMによる推論・判断。 |
| 3 | **Hands** | ツール実行層。ブラウザ操作、ファイル管理、メール送信、スクリプト実行。 |
| 4 | **Memory** | ローカルMarkdownベースの永続記憶。 |
| 5 | **Heartbeat** | 24/7自律監視ループ。タスクの能動監視、インボックス処理、プロンプトなしのアクション。 |

> **出典**: OpenClaw Docs — [clawdocs.org](http://clawdocs.org/) [T2]

### スキルシステム

- **SOUL.md**: Agentの人格・倫理を定義する設定ファイル。
- **スキル**: Markdown + YAMLでカスタムスキルを構築可能。
- **ClawHub**: スキル共有プラットフォーム。VirusTotalスキャン済みスキルでセキュリティ強化。
- 100以上のコミュニティ製プリセットスキルが利用可能。

### 所有権遷移

2026年2月、Peter Steinbergerは**OpenAIへの入社**を発表。プロジェクトの維持は新設の**非営利財団**に移行し、コミュニティ主導のロードマップが確保された。この構造はPython Software FoundationやLinux Foundationに類似。

> **出典**: Trusted AI Partners — [OpenClaw](https://trusted-ai-partners.com/en/software/openclaw) [T3]

## Coze Agent World vs OpenClaw: 技術比較

| 比較軸 | Coze Agent World | OpenClaw |
|--------|------------------|----------|
| **モデル** | Coze自前モデル（豆包-Pro等） + 外部LLM | 任意の外部LLM（Claude、GPT、Gemini、Ollama等） |
| **データ所在** | Cozeクラウド上 | **ユーザーのデバイス上**（ローカルファースト） |
| **身份** | @coze.email + Agent World ID | ローカル環境のIdentity（チャネルベース） |
| **接続チャネル** | 飞书、微信、ブラウザ、Webhook | **23+チャネル**（WhatsApp、Telegram、Discord、Slack、iMessage等） |
| **自律性** | Agent World内での自律活動（7×24） | Heartbeatによる24/7ローカル自律実行 |
| **データプライバシー** | Cozeクラウド管理 | **ユーザー完全管理**（GDPR対応） |
| **ライセンス** | クローズドソース | **MIT License**（OSS） |
| **スキル分散** | 技能商店（365ツール、有料/無料） | ClawHub + カスタムスキル（OSS） |
| **マルチエージェント** | 対応（主Bot＋子Agent） | 対応（マルチエージェントルーティング） |

## 業界動向: Agent身份の平行進化

Coze 2.5のリリースと**同時期**に、複数の巨大企業がAgent身份フレームワークをリリースした（RSAC 2026、2026年2月）：

| 企業 | フレームワーク | 特徴 |
|------|---------------|------|
| **Coze** | Agent World + @coze.email | Agentに独立身份・平行ネットワーク・計算環境を提供 |
| **Microsoft** | Entra Agent ID | Agentを企業身份治理体系に統合。人間sponsor付き。 |
| **Cisco** | Duo Agentic Identity | 各アクションをsponsorに追跡。リアルタイム権限評価。 |
| **Ping Identity** | Agent身份フレームワーク | エンタープライズ向け身份管理。 |
| **CrowdStrike** | Agent安全フレームワーク | Agentのセキュリティ監視と制御。 |

> **出典**: 腾讯新闻 — [Coze 2.5 发布：成为 Agent 的网络](https://news.qq.com/rain/a/20260407A04I7W00) [T1]

これは「Agentの身份インフラ」が**各方向から同時に成長**していることを示しており、CozeとOpenClawはそれぞれ「プラットフォーム型」と「OSS型」という異なるアプローチでこの潮流に参加している。

## 関連リンク

### 内部リンク

- [[claude-code]] — IDE統合型Agent型ツール
- [[openclaw]] — OSSローカル型パーソナルAIアシスタント

### 外部ソース

| ソース | URL | ティア | 概要 |
|--------|-----|------|------|
| 腾讯新闻 | [Coze 2.5 发布：成为 Agent 的网络](https://news.qq.com/rain/a/20260407A04I7W00) | T1 | Agent Worldの技術詳細、Microsoft/CiscoのAgent ID |
| A³·爱力方 | [扣子2.5升级](https://agent.ren/2026/0410/12055.shtml) | T3 | 云电脑/云手机/独立邮箱の仕様 |
| AITOP100 | [扣子2.5发布Agent World](https://www.aitop100.cn/coze2.5) | T3 | Agent World定位、動画創作Agent |
| GitHub | [openclaw/openclaw](https://github.com/openclaw/openclaw) | T1 | OpenClaw公式リポジトリ |
| OpenClaw Docs | [clawdocs.org](http://clawdocs.org/) | T2 | OpenClaw技術アーキテクチャ |
| Trusted AI Partners | [OpenClaw](https://trusted-ai-partners.com/en/software/openclaw) | T3 | プロジェクト歴史、所有権遷移 |
