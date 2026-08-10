---
title: "MCP中国生态（Model Context Protocol在中国的採用状況）"
type: concept
tags: [mcp, chinese-ai, agent-protocol, a2a, standardization, tool-integration, github, enterprise]
created: 2026-04-17
updated: 2026-08-10
source_lang: zh-CN
---

# MCP中国生态（Model Context Protocol 中国採用状況）

| | |
|---|---|
| **プロトコル** | MCP (Model Context Protocol) |
| **提唱** | Anthropic (2024年末) |
| **ガバナンス** | Linux Foundation → 智能体AI基金会 (AAIF, 2025年12月) |
| **中国での地位** | Agent時代の「USB接口」として認知 |
| **関連プロトコル** | A2A (Agent-to-Agent, Google提唱) |

## 概要

MCP（Model Context Protocol）は、AIシステムが外部ツールやデータに安全かつ統一された方法でアクセスするための標準プロトコル。2025年12月にAnthropicからLinux Foundation傘下の**智能体AI基金会（AAIF）**へ正式寄贈され、企業私有標準からグローバル中立ガバナンスへ移行。中国では2026年初頭から急速に採用が進み、Agent生態系の「標準接続インターフェース」として定着しつつある。

## MCPの核心价值: 中国メディアによる解釈

立委NLP频道（2026年3月）の記事「**2026年智能体范式大爆发：从認知幻象到工業化協同**」は、MCPを以下の観点で評価:

### 伝統API統合 vs MCPプロトコル

| 比較項目 | 伝統API統合 | MCPプロトコル |
|---------|------------|--------------|
| **接入コスト** | 各モデル向けカスタム「糊コード」必要 | 1回開発、複数モデル共通接入 |
| **コンテキスト占用** | 全ツール定義を事前読込、最大67k+ tokens | 遅延読込（Lazy Loading）、オンデマンド |
| **安全性** | API Keyが各アプリに散在、権限管理困難 | トークンベースの細粒度権限制御と監査 |
| **拡張性** | 線形成長、メンテナンス困難 | 動的登録、50+ツールの並行调用サポート |

## 中国MCP採用の主要プレイヤー

### プラットフォーム統合

| プラットフォーム | MCP対応状況 | 特徴 |
|-----------------|------------|------|
| **Dify** | 原生統合 | MCPサービス消費者・提供者の両対応。Volvo Carsが実装事例 |
| **BetterYeah AI** | 原生対応 | A2A+MCP統合、NeuroFlowエンジン |
| **阿里云百煉** | 統合済み | Agent 2.0でMCPをツールとして統一。釘釘（DingTalk）連携 |
| **扣子Coze** | 部分対応 | Einoフレームワーク(Go言語)、Coze StudioはApache 2.0でOSS |
| **百度文心** | 計画中 | 千帆大モデルプラットフォーム経由 |
| **腾讯云ADP** | 計画中 | 企業微信（WeCom）統合予定 |

### 業界別MCP適用事例

- **旅遊**: 途牛MCP開放プラットフォーム（2026年2月正式上线）、OpenClaw生態接入
- **電商跨境**: MCPをAIとデータ接続の重要インフラとして活用
- **金融**: MCPベースの細粒度権限管理によるコンプライアンス対応
- **製造**: MCP経由の産業IoTデータ収集・分析

## A2Aプロトコル: Agent間協同の標準化

MCPがAgentとツールの**垂直接続**を解決するなら、A2A（Agent-to-Agent）はAgent間の**水平協同**を解決する。

### A2Aの核心コンポーネント
1. **智能体卡片（Agent Card）**: LLMのモデルカードに類似。Agentの能力、認証要件、入出力モダリティ、サポートスキルを記述
2. **任務オブジェクト（Task Object）**: 跨Agentワークの全ライフサイクル管理
   - 状態遷移: 提交 → 執行中 → 需要輸入 → 已完成 → 已失敗
   - 数時間〜数日にわたる非同期協同をサポート

### MCP + A2Aの相乗効果
中国メディアは「**MCP+A2A构建了智能体互联网**」（MCP+A2AがAgentインターネットを構築）と表現。垂直接続（MCP）と水平協同（A2A）の組み合わせにより、Agentは相互に発見・評価・協働できるようになる。

## 中国特有のMCPトレンド

### 1. 微信・釘釘・飛書統合
中国企業エコシステムの三大プラットフォーム（WeChat、DingTalk、Feishu/Lark）へのMCP統合が進行中。これにより、中国独自のSaaS生態系とAI Agentの接続が標準化される。

### 2. 国産モデルMCP対応
Qwen、DeepSeek、ChatGLM等の中国製モデルがMCPサーバーとして動作するためのSDK・アダプター開発が活発。ModelScope（魔搭）プラットフォーム上でのMCPツール公開も増加。

### 3. MCP Tool Search（2026年初頭）
「MCPツール検索」機能の導入により、コンテキストウィンドウを冗長なツール定義で占有する問題が解決。遅延読込（Lazy Loading）により、必要なツール定義のみオンデマンドで取得。

## Agentアーキテクチャの4層モデル

2026年の中国Agent開発では、以下の4層モデルが標準になりつつある:

| 層 | 役割 | 中国語 |
|----|------|--------|
| **認知層** | LLMによる意図理解、任務分解、計画生成 | 認知层 |
| **技能層** | 原子化的実行単位。明確な境界・入出力・監査証跡 | 技能层 |
| **接続層** | 外部世界（DB、SaaS、社内ネット、CLI）との接続 | 连接层 |
| **持続層** | 状態・記憶の管理。任務ブレイクポイント、長期嗜好 | 持续层 |

## 技能密度（Skill Density）: 新競争指標

2026年のAgent競争は「モデルパラメータ規模」から「**技能密度**」へ移行:

| 段階 | 技能数 | 表現形式 | 核心价值 |
|------|--------|---------|---------|
| 初期 | < 20 | スクリプト化Agent | 単純反復作業の自動化 |
| 成長期 | 50-150 | 垂直業界Agent | 特定分野の複雑ワークフロー処理 |
| 成熟期 | > 200 | 通用任務エンジン | 跨システムの複雑任務オーケストレーション |

## 50%任務完成時間水平線

Agent能力の客観的指標として「**50%任務完成時間水平線**」が導入:
- Agentが50%の成功率で自律完了できる、元々人类専門家が必要とした作業の時間
- 2026年初頭、主要モデル（Claude 3.7、Gemini 3.0）の软件工程任務で約**50分**に到達
- 2019年以来、約**7ヶ月ごとに倍増**

## 中国AI規制とMCP

MCPの標準化は中国のAI規制環境においても有利に働く:
- **生成式AI管理弁法**: ツールアクセスの標準化により監査が容易
- **データセキュリティ法**: トークンベースの権限管理がコンプライアンス要件を満たす
- **算法推薦管理規定**: Agentの行動追跡・記録がMCP標準で実現可能

## 2026年4月最新動向

### MCP月間ダウンロード量が9,700万回を突破

Anthropicの発表によると、MCPの月間ダウンロード量は**2026年3月に9,700万回**を突破。16ヶ月間で200万→9,700万へ**47.5倍の成長**を記録。

### アクティブ公開MCPサーバーが10,000+に到達

2026年4月時点で、**10,000以上のアクティブ公開MCPサーバー**が存在。中国国内のMCPツール・サーバー公開も急増。

### MCP公式2026ロードマップ

AnthropicのMCP公式ロードマップは4つの柱:
1. **传输层可扩展性**: Streamable HTTPをステートレス化
2. **企业级功能**: 監査、SSO認証の標準化
3. **治理演进**: Contributor Ladder（貢献者制度）の導入
4. **任務生命週期**: リトライ、有効期限のサポート

### コンテキストウィンドウの冗長問題解消

中国でのMCPツール検索（MCP Tool Search）の導入により、コンテキストウィンドウを冗長なツール定義で占有する問題が解消された。遅延読込（Lazy Loading）により、必要なツール定義のみオンデマンドで取得可能。

## 2026年4月下旬アップデート — エコシステム成熟期へ

### 1. GitHub公式MCP Serverリリース（2026年4月）

GitHubがAnthropicと共同開発した**公式MCP Server（github-mcp-server）**をGo言語でフルスクラッチ再実装。v1.0.2（2026-04-22リリース）時点で**29K+ GitHub Stars**を獲得。以下の全機能をカバー：

- リポジトリ・コードファイルの読み取り
- Issues・PRの管理
- コード解析・ワークフロー自動化
- 自然言語インターフェースでのGitHub操作

GitHubの公式サポートによりMCPは「コミュニティのおもちゃ」から**「プラットフォーム級インフラ」**へ正式に昇格。GitLab・Bitbucketの追従が予測される。

### 2. MCP月間ダウンロード97M、公開サーバー10,000+へ

2026年3月、MCP SDK月間ダウンロードが**9,700万回**、アクティブ公開MCPサーバーが**10,000以上**に到達（Anthropic発表）。16ヶ月で200万→9,700万へ**47.5倍増**。全主要AIラボがMCPをネイティブサポート：

| プラットフォーム | MCP対応時期 |
|----------------|------------|
| ChatGPT (OpenAI) | 2025年4月 |
| Claude (Anthropic) | 2024年11月（初始） |
| Gemini (Google DeepMind) | 2026年3月 |
| Microsoft Copilot | 2025年7月 |
| Cursor | 2025年 |
| VS Code | 2025年7月 |
| Meta AI | 2026年4月（Connect発表） |

### 3. 「プロトコル戦争」終結宣言

MCPの97Mダウンロード達成により、各社が独自に推進していたツール呼び出し形式の**「プロトコル戦争」は実質終結**。OpenAI・Google・Microsoft・AWS・Cloudflareの全社がMCPを支持。開発者にとっては「Write Once, Run Everywhere」が現実のものに。

### 4. GLM-5.1がMCP Atlasベンチマーク首位

Z.AI（智譜AI）の**GLM-5.1**がMCP Atlasベンチマークで**71.8%**を記録し、GPT-5.4（67.2%）を上回る。MCPツール呼び出し精度で事実上のトップ。無料Flashティアが提供されており、中国国外での評価が急上昇中。

### 5. MCP Auth標準化 & Streamable HTTP

2026年3月26日、MCP仕様が重要なアップデート：
- **Auth認証メカニズム**: 草案から正式仕様へ。企業レベルの権限制御が標準化
- **Streamable HTTP**: SSE（Server-Sent Events）を置き換え、ブラウザ環境でのネイティブ動作を実現

### 6. Docker MCP Toolkit & Microsoft Azure MCP Server

- **Docker**: MCP Toolkitをリリース。コンテナ環境でのMCPサーバー運用を標準化
- **Microsoft**: Azure MCP Server 2.0.0（2026-04-10）— C#実装、Azure全サービスをカバー
- **Microsoft MCP Serverカタログ**: GitHub 2,954 Stars、84リリース

### 7. MCP Serverエコシステムの内訳

| カテゴリ | 割合 | 代表例 |
|---------|------|--------|
| 開発ツール | 35% | GitHub, GitLab, Linear, Notion, Sentry |
| データ基盤 | 22% | Postgres, Snowflake, Databricks, BigQuery |
| クラウドサービス | 18% | AWS, GCP, Azure, Cloudflare |
| SaaSアプリ | 15% | Slack, Stripe, Figma, Zapier |
| 内部/カスタム | 10% | エンタープライズ内製サーバー |

247+のオープンソースMCP Server実装が存在。

### 8. 中国QwenのMCPツール呼び出し性能

Qwen3.6-35B-A3B（2026-04-16リリース）が**MCPMark 37.0%**を記録 — Gemma 4-31B（18.1%）の**2倍以上**。Qwen3.6 Plus（2026-03-31リリース）は128Kコンテキスト、SWE-bench 78.8%のフラッグシップ。中国モデルがMCPツール呼び出し領域で急成長。

### 9. MCP成熟化：批判と現実

2026年4月の中国技術コミュニティでは「MCPは沈静化したが、それは死ではなく成熟」との評価が主流：

- **肯定的**: 大企業（Alibaba Cloud、Tencent Cloud、Meta、Docker）は黙々と実装を進めている
- **批判的**: Perplexity CTO Denis Yaratsが「MCPの複雑さが解決する問題を上回る」と発言、CLI回帰を主張
- **現実**: ScaleKitベンチマークでMCPの8%タスクが失敗（タイムアウト・接続不安定）
- **結論**: MCPは「USB-C」の道を歩む — 最も熱い時期ではなく、最も重要な時期にある

### 10. Anthropic MCP実践ガイド（2026年4月末〜5月初）

2026年4月末、Anthropicが「**Building Agents that reach production systems with MCP**」と題するブログを公開し、コミュニティからの批判に正面から回答した：

#### MCP SDK月間ダウンロードが3億回に急成長
- 年初（2026年1月）の1億回/月から**3億回/月**へ成長
- 中国コミュニティでは「爆発的採用が沈静化ではなく加速している証拠」と解釈

#### コミュニティの三大批判とAnthropicの回答

| 批判 | Anthropicの回答 | 技術的解決 |
|------|----------------|-----------|
| **トークン消費が膨大**（Context Window overflow） | Tool Search + プログラム化呼び出し | Tool Searchで**85%+削減**、プログラム化呼び出しで**37%追加削減** |
| **Schema爆発**（定義が肥大化） | Tool Search: 必要な定義のみ遅延取得 | 1K tokens以内に抑える（Cloudflare実証） |
| **CLIより非効率** | 三者使い分けが正解 | 直連API（簡単）/ CLI+Skills（ローカル開発）/ MCP+Skills（クラウド本番） |

#### 3つの接続パターン（Anthropic公式フレームワーク）

| パターン | 向け環境 | 特徴 |
|---------|---------|------|
| **直連API** | 単純な1-2ツール呼び出し | 軽量、認証最小、低レイテンシ |
| **CLI + Skills** | ローカル開発環境 | 軽量（データがコンテキストを通らない）、高速、CLAUDE.mdベース |
| **MCP + Skills** | クラウド本番環境 | 標準化、認証（OAuth+Vaults）、クロスプラットフォーム |

Anthropicの明確な立場：「MCPとCLIは対立しない。良いMCPサーバーはCLIのように設計されるべき」。

#### MCP + Skillsパッケージングの登場
- Canva、Notion、SentryがMCPサーバーと同時にSkillsを公開開始
- MCPコミュニティがSkillsのMCPサーバー直接配布を開発中（API更新時にSkillsも自動アップデート）
- 中国でも「MCP Server + Skillテンプレート」の組み合わせ配布が始まる可能性

#### Cloudflareの革新的MCP実装
- わずか**2つのMCPツール**で**2,500以上のエンドポイント**をカバー
- コードをサーバーサイドのサンドボックスで実行し、結果のみ返却
- Agentが `search` で必要なドキュメントを検索し、`execute` でコードを実行
- 実質的にCLIの哲学をMCPプロトコルに移した設計 — 「MCPの正しい使い方」の参照実装に

### 11. 中国コミュニティ「沈静化＝成熟」評価（2026年5月）

腾讯云开发者社区（2026年5月）の分析記事「MCP协议2025年大爆发，2026年反而相对平静」が示したMCPの現状評価：

#### 「2026年の静けさ」の本当の意味
- 2025年3月はMCPが中国技術コミュニティで「顶流（トップトレンド）」だった
- 2026年は発言が減ったが、**大企業が静かに実装を進めている証拠**
- OpenAI：継続対応、Google：継続、Microsoft：Win11システム層にMCP統合
- Alibaba Cloud百煉：MCP全ライフサイクルサービス稼働中
- **Meta**：Connect 2026でAIツールのMCP対応発表
- **Docker**：MCP Toolkitリリース
- **Linux Foundation AAIF**：正式にプロトコル管理開始

#### 技術的成熟（2026年3月26日）
- **Auth認証**：草案から正式仕様へ — 企業レベルの権限制御を標準化
- **Streamable HTTP**：SSEを置き換え、ブラウザ環境でのネイティブ動作を実現

#### 残存する批判
- Perplexity CTO Denis Yarats（内部メモ流出）：「MCPの複雑さは解決する問題を上回る」— 自社ではAPI+CLIに回帰
- ScaleKitベンチマーク（2026年2月）：CLIがMCPより2倍効率的、MCPで8%のタスクがタイムアウト
- 中国開発者コミュニティではCLI+Skills回帰が一部で進行中

#### 結論：最も重要な時期にある
| フェーズ | 時期 | 特徴 |
|---------|------|------|
| **誕生** | 2024年11月〜2025年2月 | Anthropic単独推進、コミュニティ小規模 |
| **爆発** | 2025年3月〜6月 | 全社対応表明、Server急増、中国頂流 |
| **批判** | 2025年後半〜2026年初 | トークン問題・非効率性が顕在化 |
| **成熟** | **2026年現在** | 批判に対応した改善実装、大企業の静かな本番投入 |

> 「MCP能不能走到那一步，不知道。但它现在正在经历一个协议最重要的阶段——不是最热的时候，而是最关键的时候。」（腾讯云开发者社区）

### 12. MCPエコシステム拡大：新プロトコルの出現（2026年5月）

MCP中文站（mcpcn.com）のエコシステム拡大が見られる：

| 新プロトコル | 役割 | 中国コミュニティ |
|------------|------|----------------|
| **A2A（Agent-to-Agent）** | Agent間の水平協同 | A2A中国コミュニティ設立 |
| **AP2（Agent Payments Protocol）** | Agent間決済 | AP2 Lab |
| **ACP Commerce** | Agentic Commerce | ACP Commerceコミュニティ |
| **ChatGPT中国語** | 翻訳・ローカライズ | ChatGPT中文コミュニティ |

MCPを中核として、Agent間通信（A2A）、Agent決済（AP2）、Agent商取引（ACP）と、Agent経済の標準化レイヤーが整備されつつある。

## 2026年5月上旬アップデート — 生態系の更なる成熟とセキュリティ事件

### 1. MCP生态平台盘点：中国8大MCP广场の定量的比較

2026年5月時点の中国MCP生態系は、雲ベンダー主導のプラットフォームと第三者集約プラットフォームに分化。以下8大プラットフォームが確認されている:

| プラットフォーム | 運営元 | サービス数 | タイプ | 特徴 |
|----------------|--------|-----------|--------|------|
| **魔搭社区 MCP 广场** | 阿里云 (ModelScope) | 9,227+ | 総合 | 最大の中国語MCPコミュニティ、支付宝MCP独占提供、MCP実験場・Bench評価ツール |
| **百度智能云 MCP World** | 百度 | 56,757+ | 企業級 | 国内最多収録、百度検索連動トラフィック、無料ホスティング、SLA保証 |
| **阿里云百煉 MCP 市场** | 阿里云 | 184+ | 精選 | 業界初の全ライフサイクルMCP、5分でスマート体構築、サンドボックス分離 |
| **腾讯云 MCP 广场** | 腾讯云 | 1,089+ | 業務型 | MCP+Agent+小程序一体化、微信生態統合、ビジュアルAgent構築 |
| **讯飞星辰 MCP 广场** | 科大讯飞 | 16,318+ | 音声AI | 音声認識/合成MCP、星火大モデル統合、教育・医療向け産業ソリューション |
| **MCP 星球** | 第三方 | 54,555+ | 集約 | 最多収録（集約型）、中立・ベンダー非依存、詳細チュートリアル |
| **AIbase MCP 资源站** | 第三方 | 13,784+ | 集約 | GitHubリポジトリミラー、中文ドキュメント翻訳、使用事例共有 |
| **心流开放平台 MCP 市场** | 第三方 | 3,852+ | 展示 | データ透明（閲覧数・保存数統計）、ワンクリックJSON構成複製 |

中国MCP生態の2019→2026の展開トレンド：
- 2025年初頭: 手動JSON構成
- 2025年中: 構成テンプレート提供
- 2025年末: ワンクリッククラウドデプロイ
- 2026年: 5分でスマート体構築（定常化）

**出典**: [啊靓啊笔记 — 2026年国内MCP广场大盘点](https://alianga.com/articles/mcp-servers) (2026年5月)

### 2. MCP开发者峰会（2026年4月2-3日、ニューヨーク）

約1,200人が参加した初のMCP開発者サミットで、以下の重要な発表・合意があった：

| 発表 | 内容 |
|------|------|
| **Uber GenAI Gateway** | 週数万回のAgent実行を処理する内部ゲートウェイアーキテクチャを公開 |
| **Amazon agent-sop** | 内部MCP発見インフラを公開、`agent-sop`プロジェクトをOSS化 |
| **Docker/Kong/Solo.io** | MCP Gatewayは本番環境に必須と総意。プロキシレイヤーでのセキュリティ・認証統一 |
| **x402 Foundation** | Linux Foundation傘下として正式始動。MCPのガバナンスと標準化を推進 |

**企業採用率**: 79%の企業がAI Agentを試用、43%が本番投入済み。

**出典**: [freebird2913 — MCP開発实战(二)](https://www.freebird2913.tech/posts/mcp_deep_dive_2/) (2026-05-02)

### 3. MCP Gateway：企業級アーキテクチャの共通認識

2026年4月のMCP開発者サミットで最も重要な合意事項の一つが「生産環境ではMCPにGatewayとRegistryが必須」という点。

**Uber GenAI Gateway**: 認証・認可・レート制限・監査を一元管理。週数万回のAgent実行を捌く。
**Gatewayパターンの利点**:
- セキュリティの統一（認証・認可・監査ログ）
- ツール発見の一元管理
- レート制限とコスト管理
- マルチプロトコル（MCP/A2A/ACP）のブリッジ

### 4. MCPセキュリティ事件：CVE-2026-30615（2026年4月15日）

イスラエルのセキュリティ企業OX SecurityがMCPに**アーキテクチャレベルの設計欠陥**を発見・報告。以下の衝撃的な内容：

**脆弱性の核心**: MCP Server（信頼できない側）がSamplingメカニズムを悪用し、ホストのMCP Clientに任意のツール呼び出し（RCE: Remote Code Execution）を実行させることが可能。プロセス分離境界を突破。

**影響範囲**:
| 影響コンポーネント | 範囲 | 深刻度 |
|-------------------|------|--------|
| @modelcontextprotocol/sdk (Node.js) | ≤ 0.9.x | Critical |
| @modelcontextprotocol/sdk (Python) | ≤ 0.5.x | Critical |
| Claude Desktop | 全バージョン | Critical |
| VS Code Cursor | 全バージョン | Critical |
| Cline / Continue / Windsurf | 全バージョン | High |

**規模**: 全世界で約20万台のMCPサーバーが影響を受け、その大部分は企業内のAI開発環境。

**Anthropicの対応**: 複数回の通報に対し「これは予期された設計上の動作（expected design）」として根本的修正を拒否。セキュリティはアプリケーションレイヤーとゲートウェイレイヤーで解決すべきという立場。

**コミュニティの反応**:
- 支持派: 「MCPはnpmのようなオープンエコシステム。ユーザーが信頼できるServerを選ぶべき」
- 批判派: 「MCPはWindows 11にシステムレベル統合されている。セキュリティ基準はOSレベルが必要。npmレベルの安全意識は不十分」
  → 「MCPはシステムレベルの能力として位置づけられているが、セキュリティ基準はnpmレベルに留まっている」が核心的批判。

**CVE一覧**: 10個のCVE番号が割り当てられ、すべて「Critical（深刻）」評価。

**緩和策**:
- 短期: MCP Gatewayプロキシを導入しサプライチェーン監査を実施
- 長期: ゼロトラストアーキテクチャへの移行、業界全体のAI Agentセキュリティ標準の確立

**出典**: [程序员茄子 — MCP协议致命漏洞CVE-2026-30615深度解析](https://www.chenxutan.com/d/1931.html) | [freebird2913](https://www.freebird2913.tech/posts/mcp_deep_dive_2/)

### 5. MCP 2026年路線図アップデート

AnthropicエンジニアDavid Soria Parraが2026年4月19日のAI Engineer Shareで発表：

| 機能 | 時期 | 内容 |
|------|------|------|
| **無状態転送プロトコル** | 2026年6月 | Googleチームと共同開発。Cloud Run/Kubernetes環境での水平スケーリングを実現 |
| **Server Discovery** | 2026年後半 | Agentがウェブサイト訪問時にMCP Serverを自動発見 |
| **MCP Apps** | 実験的 | 独自UIを持つAgent。Skills over MCPパッケージング |
| **Skills over MCP** | 研究中 | Canva/Notion/SentryがMCP Server+Skills同時公開。MCPコミュニティがSkillsのMCP経由直接配布を開発中 |

**SDK月間ダウンロード**: 2026年1月の1億回/月から**3億回/月**（Anthropic実践ガイド発表、4月末時点）。

**GitHubコミュニティMCP Server**: 1,000超。
**主流フレームワーク**: LangChain, AutoGen 3.0, CrewAI, LlamaIndexがすべてネイティブサポート。

**出典**: [freebird2913 — MCP開発实战(二)](https://www.freebird2913.tech/posts/mcp_deep_dive_2/) (2026-05-02) | Anthropic Blog

## 関連エンティティ

- [[concepts/mcp]] — MCPプロトコルの基本概念
- [[concepts/mcp-chinese-tools]] — 中国MCPツール・サーバー
- [[concepts/mcp-security]] — MCPのセキュリティ側面
- [[concepts/ai-agent]] — AIエージェント一般
- [[concepts/china-ai-agent-ecosystem]] — 中国AI Agent生態系
- [[concepts/dify]] — Difyプラットフォーム
- [[concepts/coze]] — 扣子Cozeプラットフォーム

## 2026年5月13日〜19日更新 — セキュリティ事件の連鎖と国家級MCP展開

### 1. MCPデータベースサーバー3大脆弱性（5月13日）
AkamaiのTomer Peledが3つのMCPデータベースサーバーの重大な脆弱性を発見（x33fconで発表予定）:

| サーバー | CVE | 脆弱性 | 状態 |
|---------|-----|--------|------|
| **Apache Doris MCP** | CVE-2025-66335 | SQLインジェクション（`db_name`パラメータ） | パッチ済み(v0.6.1) |
| **Apache Pinot MCP(StarTree)** | 未割当 | 認証バイパス＋SQLクエリ実行 | OAuth追加済み、SQLi残存 |
| **Alibaba Cloud RDS MCP** | 未割当 | RAGツール認証なしアクセス | **Alibabaがパッチ拒否** |

**Alibaba Cloudのパッチ拒否**は中国MCPセキュリティの分岐点。CERT/CCに報告済み。
- **出典**: [The Register](https://www.theregister.com/security/2026/05/13/bug-hunter-tracks-down-three-serious-mcp-database-flaws-one-left-unpatched/5238916) [T1]

### 2. MCP攻撃対象領域3倍拡大 — 銀行のSEC開示（2026年5月）
CVE-2026-5058（CVSS 9.8）: コミュニティ保守のMCPサーバーにおけるコマンドインジェクション。EC2インスタンス経由でS3/DynamoDB/Lambda/IAMに横断移動可能。ある銀行が**SECにForm 8-K**を提出 — AIエージェント脆弱性に関する初のSEC開示事例。
- **出典**: [dev.to](https://dev.to/mspro3210/may-2026-the-mcp-attack-surface-tripled-three-disclosures-and-a-banks-sec-filing-tell-you-what-23nd) [T2]

### 3. Trend Micro: 露出MCPサーバー1,467台に急増（4月28日発表、5月拡散）
前回調査(2025年7月: 492台)から**約3倍**に増加。1,227台が非推奨のSSEトランスポートを使用。70ホストで`execute_sql`ツールが露出。AWS/Azure用非公式MCPサーバーにCVSS 9.8脆弱性。19,000以上のMCPサーバーソースコードの48%が`.env`ファイルに秘密情報を平文保存。
- **出典**: [Trend Micro](https://www.trendmicro.com/vinfo/gb/security/news/vulnerabilities-and-exploits/update-on-exposed-mcp-servers-the-threat-widens-to-the-cloud) [T1]

### 4. CVEカスケードとClawHubサプライチェーン攻撃（5月）

| CVE | 対象 | CVSS | 状態 |
|-----|------|------|------|
| CVE-2026-30623 | liteLLM MCPサーバー コマンドインジェクション | 9.8 | パッチ済み(v1.83.7) |
| CVE-2026-23744 | MCPJam Inspector RCE | 9.8 | パッチ済み(v1.4.3) |
| CVE-2026-7593 | command-executor-mcp-server OSインジェクション | 8.5 | **パッチなし**（プロジェクトアーカイブ済み） |
| CVE-2025-53967 | Framelink Figma MCP | 9.1 | パッチ済み(v0.6.3) |
| CVE-2026-6599 | LangFlow MCP | 9.8 | **パッチなし**（ベンダー応答なし） |

**ClawHub（OpenClawスキルレジストリ）サプライチェーン攻撃**: 341個の悪意あるスキル（レジストリ全体の12%）がAPIキー・認証情報・機密データを窃取。
- **出典**: [ThreatAft](https://threataft.com/articles/mcp-servers-remote-code-execution-crisis) [T2]

### 5. 新华财经MCP服务矩阵 — 国家級金融MCP基盤（5月18日）⭐最重要
国家級金融データ基盤として初の本格的MCP展開。**6大MCPサービス体系**:
1. **リアルタイム行情**: 株式・債券・為替・商品のリアルタイムデータ
2. **金融市場**: 銘柄分析、セクター動向、資金フロー
3. **マクロ/業界**: GDP、CPI、PMI等マクロ指標＋業界別レポート
4. **企業データ**: 1.5億件企業情報、45省庁監督データ
5. **ニュース/公告**: 24時間365日ニュース速報、上場企業公告
6. **政策/研究**: 18万件超政策法規、6,000以上の发文機関カバー

**30以上のコアMCPサービス**を提供。国家金融情報プラットフォームとしての権威ある信頼性が競争優位。
- **出典**: [新华财经](https://m.cnfin.com/hg-lb//zixun/20260518/4413883_1.html) [T1]

### 6. MCP SDK月間ダウンロード1.1億回突破（5月）
前回更新（5月13日）からの数値更新:
- MCP SDK月間DL: **1.1億回**（xiezhixin/Anthropic発表）
- GitHub Stars (serversレポ): **84.1k**
- 公開MCPサーバー数: **9,400+**（前年比7.8倍）
- エンタープライズ採用率: **78%**が本番環境にMCP対応エージェント展開
- A2A採用組織: **150+**組織、Microsoft/AWS/Salesforce/SAP/ServiceNowが本番稼働
- **出典**: [SiliconReport](https://www.siliconreport.com/model-context-protocol-targets-production-scaling-issues-in-2026-roadmap-e941542f3b363948) [T2]

### 7. MCP 2026年ロードマップ進捗（5月14日）
本番スケーリング問題に焦点。4優先分野:
1. **トランスポート層進化**: 無状態トランスポート（2026年6月予定）— セッション状態と水平スケーリングの矛盾を解決
2. **エージェント通信**: Tasksプリミティブ（SEP-1686）の実験的機能
3. **ガバナンス成熟化**: コアメンテナーによるレビューボトルネック解消
4. **エンタープライズ対応**: 監査、SSO統合、ゲートウェイ標準化
- **出典**: [SiliconReport](https://www.siliconreport.com/model-context-protocol-targets-production-scaling-issues-in-2026-roadmap-e941542f3b363948) [T2]

## 2026年5月19日〜24日更新

### 1. Alibaba Cloud Summit 2026（5月20日）— 全クラウド製品のMCP化宣言
杭州で開催。アリババがAgent時代に向けた**全スタックのAgent化**戦略を発表:

- **全クラウド製品のMCP化**: ECS/OSS/VPC/RDS等をMCP Serverに改造。Alibaba Cloud Ops MCP Server（v0.9.27, GitHub Stars 115）公開
- **千問雲（Qianwen Cloud）新サイト**: Agent専用プロダクトサイト。トップページにAgent可読プロンプト1行。150+モデルAPIをSkills/CLIツールに標準化。OpenClaw/Hermes Agent/Claude Codeが1行指示で全機能を学習可能
- **Qwen3.7-Max発表**: Arenaグローバル盲検テストで中国モデル首位（Kimi-K2.6/DeepSeek-v4-pro凌駕）
- **ModelScope MCP広場**: 千種類以上のMCPサービス、支付宝/Alipay/MiniMax等独占提供
- **トークン収益5ヶ月で15倍増**: 年内にECSを超える最大収益源見通し
- **出典**: [澎湃新聞](https://www.thepaper.cn/newsDetail_forward_33204218) [T1]

### 2. ByteDance火山引擎MCP Server OSS公開（5月19日）
- **100+ MCP Server**: GitHub「volcengine/mcp-server」リポジトリ（Stars 271, 90 contributors, MITライセンス）
- **三位一体アーキテクチャ**: MCP Market＋火山方舟＋Trae—ツール→モデル→デプロイのフルサイクル
- **開発期間70%短縮、リソースコスト80%削減**
- **日次トークン呼び出し12.7兆**（火山エンジン全AIスタック）
- **出典**: [腾讯云开发者](https://developer.cloud.tencent.com/news/2576909) [T1]

### 3. Tencent Cloud MCP製品群集中リリース（5月18日〜22日）
- **MCP Gateway（5月21日）**: 既存RESTful APIをゼロコードでMCP Tool化。認証集中管理・監査ログ自動化
- **MCP-FLOW研究（5月18日）**: 小規模モデルのツール呼び出し精度99.2%（Qwen3-4Bベース、1,166 Server・11,536 Tools）
- **Tencent Docs MCP（5月22日）**: 9種ドキュメントタイプ対応MCP Server（smartcanvas含む）
- **TKE MCP**: Kubernetesクラスタ管理用MCP Server（PyPI公開）
- **出典**: [腾讯云开发者](https://developer.cloud.tencent.com/article/2671873) [T1]

### 4. AAIF（Agentic AI Foundation）43新メンバー追加（5月18日）
- **Gold会員**: F5, GoDaddy, Stripe, TRON（ブロックチェーン）
- **Silver会員**: Atlassian, Fastly, Teradata, VeriSign, Avaya等27社
- **Associate会員**: 米陸軍(U.S. Army)、Sandia国立研究所、Penn State等12団体
- **総会員数**: 190組織に拡大（華為Huaweiは2月Gold会員済み）
- **出典**: [AAIF](https://aaif.io/press/agentic-ai-foundation-adds-43-new-members/)

### 5. MCPアーキテクチャ設計脆弱性（OX Security, 4月-5月継続）
MCPのSTDIO転送機構に設計上のRCE脆弱性が内在。Anthropicは「期待された動作」として修正拒否。

**影響範囲**: **200,000+サーバインスタンス**、**150M+ SDKダウンロード**、9/11 MCPレジストリでテストペイロード受理可能。

### 6. Community Bank SEC 8-K開示（5月7日）
従業員が未許可サードパーティAIに顧客PIIをアップロード。**AI Agent脆弱性に関する初のSEC開示事例**。MCP STDIOの権限継承モデルが銀行業界のサードパーティリスクとして浮上。
- **出典**: [dev.to](https://dev.to/mspro3210/may-2026-the-mcp-attack-surface-tripled-three-disclosures-and-a-banks-sec-filing-tell-you-what-23nd) [T2]

### 7. MCPエコシステム統計（5月時点）
| 指標 | 数値 |
|------|------|
| 公開MCPサーバ全世界 | 9,400+（前年比7.8倍） |
| SDK月間DL | **3億回**（年初1億→3億） |
| エンタープライズ採用率 | 78%（Q1 2026） |
| 中国AI Agent市場規模 | ¥4,490億($62B)/年（前年比+107%） |
| npm SDKパッケージ | 53個 |
| npmサーバパッケージ | 751個 |

## 2026年5月24日〜6月1日更新 — 新プラットフォームと生態系の拡大

### 1. 阿里「悟空」(Wukong) Agent OS + MCP広場（5月26日〜29日）⭐最重要

阿里巴巴が新Agent OS「悟空」（Wukong）をリリース。OpenClaw（龙虾）に対抗するエコシステムとして位置づけられる。

- **「悟空」の核心**: 釘钉（DingTalk）生態系と深く統合されたAgent OS。MCPをネイティブサポート
- MCP広場を内包し、Agent発見・実行・管理を一元化
- 開発者は「悟空」上でMCP Serverを公開・収益化可能
- OpenClaw（龙虾）からの移行を促すプロモーション活動が活発化
- **出典**: [掘金 — 体验完阿里「悟空」，我想把电脑里的龙虾换掉了](https://juejin.cn/post/7618418125198196779) (2026-05-26) [T2]

### 2. Browser for AI Agent — MCPブラウザ操作ツール（5月26日）

V2EXユーザーが「Browser for AI Agent」を公開。AIエージェントがブラウザのログイン状態を読み取り、Webページ上のツールをMCP経由で呼び出すことを可能に。

- AIがユーザーの認証情報を共有せずにログイン済みページにアクセス
- REST APIをMCPツールにラップ
- **出典**: [V2EX](https://www.v2ex.com/t/1215754) (2026-05-26) [T1]

### 3. Alibaba Qwen3.7Max / QwenPaw Agent（5月29日〜30日）

Qwen3.7Maxが中国コミュニティでテストされ、「国产最佳、世界第二」と評価。同時にQwenPaw Agentの実装原理が掘削記事で詳細解説された。

- QwenPaw AgentはMCPベースのツール呼び出しをネイティブサポート
- **出典**: [掘金 — Qwen3.7Max測了一波](https://juejin.cn/post/7644794219849744394) [T1]
- **出典**: [掘金 — QwenPaw Agent 实现原理深度剖析](https://juejin.cn/post/7645147490087403530) [T2]

### 4. Anthropic Knowledge Work Plugins公開（5月26日）

Anthropicが公式「Knowledge Work Plugins」（职能专家插件库）をリリース。MCP/Skills over MCPパッケージングの実装例として位置づけられ、各職能（人事、財務、エンジニアリング等）向けのMCP Serverテンプレートを含む。

- **出典**: [掘金 — 一天一个开源项目（第112篇）](https://juejin.cn/post/7643831685151834118) (2026-05-26) [T2]

### 5. AI Agent記憶システム設計比較（5月28日）

「AI Agent记忆系统架构设计：OpenClaw、Claude Code、Hermes Agent深度对比」と題する詳細な比較記事が掘金で公開。3大AgentプラットフォームのMCP活用と記憶管理の差異を分析。

- **出典**: [掘金](https://juejin.cn/post/7644628777114042420) (2026-05-28) [T2]

### 6. LLM-as-Agent評価比較（5月30日、机器之心）

机器之心が「LLM-as-Agent技术哪家强?」と題する分析記事を公開。主要LLMのMCPツール呼び出し能力を比較評価。Qwen、DeepSeek、GLM等の中国モデルのエージェント性能を測定。

- **出典**: 机器之心 微信公众号 (2026-05-30) [T2]

### 7. FastAPI脆弱性とAI Agentセキュリティ（5月28日、36kr）

「3.25亿次周下载、FastAPI'地基'爆雷、这个Python框架曝出「致命漏洞」:一个字符，AI Agent集体"裸奔"?」— FastAPIの脆弱性がAI Agent/MCPエコシステム全体に影響を与える可能性を指摘。MCPインフラの依存関係リスクが浮き彫りに。

- **出典**: [36kr](https://36kr.com/p/3828901167911812) (2026-05-28) [T1]

### 8. MCP教育コンテンツの爆発的増加（5月24日〜31日）

期間中、以下のMCP教育記事が継続的に出現（各日で重複掲載）:
- 「AI Agent（写一个简易的MCP天气查询工具）」— MCP天気ツールのチュートリアル
- 「手把手写一个MCP Server：从零到能用，只要 30 分钟」— MCP Server作成チュートリアル
- 「一个程序员眼中的AI核心概念，讲透LLM、Agent、MCP、Skill、RAG」— 概念解説
- 「用OpenClaw实现小红书自动发帖」— MCP + OpenClaw実践事例

中国開発者コミュニティにおけるMCP学習リソースの成熟が顕著。

### 9. Claude Opus 4.8リリースとAgent生態系への影響（5月28日〜29日）

AnthropicがClaude Opus 4.8をリリース。Agent能力の向上（ツール呼び出し精度・長文脈処理）が中国コミュニティでも大きな話題に。MCPサーバーとの連携改善が期待される。

- **出典**: [V2EX](https://www.v2ex.com/t/1216300) | [36kr](https://36kr.com/p/3829914029762434) [T1]

### 10. 中国MCP生態系の総合動向（5月24日〜31日）

- **DingTalk + MCP**: 阿里「悟空」Agent OSが钉钉（DingTalk）生態系とMCPを統合。WeChat/Feishuに続く3大プラットフォームのMCP化が加速
- **QwenPaw Agent**: 阿里巴巴がQwenベースのAgent実装「QwenPaw」を公開。MCPネイティブ対応
- **Coze（扣子）**: ByteDanceのCozeプラットフォームがKimi Code経由でMCP機能を拡張中
- **OpenClaw発展**: 百度APPがOpenClawに正式対応（全ユーザー期間限定無料）、Rednote（小红书）との連携が注目
- **価格競争**: DeepSeek永久値下げ、MiMo（小米）トークン無料配布など、中国MCPエコシステムのトークン価格競争が激化
- **SEC開示余波**: Community BankのSEC 8-K開示（5月7日）に関する中国コミュニティでの議論が継続。MCP STDIO権限継承モデルのリスク認識が広まる

### 11. 中国MCP生態系の最新動向（6月1日〜3日）

- **MCP Skills実装**: V2EX開発者がMCP skillsツールを公開、短视频分析機能をMCP経由で実装。実用的なMCPサーバー実装の事例が増加中
- **MCP/A2A/AG-UIプロトコル比較**: 掘金で3大Agentプロトコルの全景解析記事が公開。MCPがツール連携、A2AがAgent間通信、AG-UIがUI統合をそれぞれ担当する住み分けが明確化
- **MCPプロトコル標準化**: 「Agentシリーズ」記事でMCPプロトコルをツール生態系の標準化アクセスとして解説。企業レベルでのMCP採用ガイドラインが整備されつつある
- **AI「第二脳」プロジェクト**: Claude/Cursor/Windsurfの共有記憶システムをMCP経由で実装するオープンソースプロジェクトがV2EXで話題に。複数AIツールの記憶統合という新しいユースケース
- **OpenClaw実用記事**: 小红书自動投稿の実装ガイドが引き続き注目され、MCPサーバーの実践的な適用事例として参照されている
- **MCP Serverチュートリアル**: 30分で使えるMCP Serverを構築するハンズオン記事が掘金で公開。開発者向けの参入障壁が低下

- **出典**: [V2EX - MCP skills](https://www.v2ex.com/t/1217743) | [Juejin - MCP/A2A/AG-UI](https://juejin.cn/post/7646938869472378915) | [Juejin - MCPプロトコル](https://juejin.cn/post/7646537363406323753) | [V2EX - 第二脳](https://www.v2ex.com/t/1217451) | [Juejin - MCP Server](https://juejin.cn/post/7604881286038028340) [T1]

## 2026年6月4日〜8日更新 — MCP教育コンテンツの爆発的増加と生態系の静かな成熟

### 1. MCP教育コンテンツの爆発的増加（6月4日〜7日）

期間中、MCP教育コンテンツは中国開発者コミュニティで連日出現：
- **6月4日**: 掘金で「AI Agent（写一个简易的MCP天气查询工具）」が公開。MCP天気ツールのハンズオンチュートリアルとして入門者向け
- **6月7日**: 掘金で「手把手写一个MCP Server：从零到能用，只要30分钟」が公開。30分で実用的MCP Serverを構築するチュートリアルが新たに登場
- **6月4日〜7日**: 「用OpenClaw实现小红书自动发帖」（MCP + OpenClaw実践）が連日掘金の主要記事としてランクイン
- **Agentシリーズ**: 「实现一个Coding Agent」シリーズ（全5回、6月6日〜7日）でMCPを含むAgentアーキテクチャを詳細解説

中国開発者コミュニティにおけるMCP学習リソースの成熟が顕著。参入障壁は低下し続けている。

### 2. MCP/A2A/AG-UI三大プロトコル比較（6月2日〜4日）

掘金で「MCP + A2A + AG-UI：三大Agent互联协议全景解析」が公開（6月2日〜4日頃）。住み分けが明確化：
- **MCP**: ツール連携（Agent↔Toolの垂直接続）
- **A2A**: Agent間通信（Agent↔Agentの水平協同）
- **AG-UI**: UI統合（Agent↔User Interfaceの接続）

この住み分けにより、中国開発者の間で「どのプロトコルをいつ使うか」の判断基準が整備されつつある。

### 3. 「AI第二脳」共有記憶プロジェクト（6月初旬）

V2EXで話題の「AI第二脳（Second Brain）」プロジェクト — Claude/Cursor/Windsurfの共有記憶システムをMCP経由で実装。複数AIツール間での記憶統合という新しいユースケース。MCP Skillsツールの短视频分析機能も同時期に公開。

### 4. MCPプロトコル無状態RC進捗（5月21日発表、6月継続監視）

mcp-chinese-toolsのノートによると、MCPプロトコルの**無状態RC（Stateless RC）**が**5月21日**にリリース済み：
- セッションIDを廃止し、Streamable HTTPをベースに水平スケーリングを実現
- **7月28日**に最終仕様リリース予定
- Googleチームとの共同開発。Cloud Run/Kubernetes環境でのネイティブ動作に対応

### 5. 生態系の静かな成熟：MCP「沈静化＝成熟」フェーズ継続

中国技術コミュニティでは2026年6月現在も「MCPの沈静化は死ではなく成熟」との評価が支配的：
- 大企業（Alibaba Cloud、Tencent Cloud、ByteDance）は前月の大規模発表後、静かに実装を進めている
- 教育コンテンツの爆発的増加は、参入障壁の低下と開発者基盤の拡大を示す
- 新たなセキュリティインシデントやCVEは6月4日〜8日期間に確認されず
- 阿里悟空（Wukong）Agent OSへの移行が加速中（掘金で115票の好評価）

### 6. 観測された制約：Web調査の限界

本期間の調査では、Exa SDKの権限障害および主要検索エンジン（Bing/DuckDuckGo）のbot対策により、外部Web検索が不能であった。以下の情報源のみから総合判断：
- **T1**: V2EX・掘筋のdaily digest（自動クロール）
- **T2**: hot-topics.yamlノート（自動更新）
- **内部**: 既存wikiページの内容

新しいMCPプラットフォーム発表、CVE開示、AAIF新メンバー追加などの「ブレイキングニュース」は本期間内に確認されなかった（5月下旬の発表が最新）。

### 7. 6月9日〜12日の動向 — パラダイム整理とFable 5週間

6月9日〜12日も基本的に「静かな成熟」フェーズ継続。大きな新発表（AAIF、クラウドベンダーMCP展開）はなかったが、教育コンテンツと概念整理に顕著な進展があった。ただし、6月10日〜12日はClaude Fable 5/Mythos 5のローンチにメディア関心が集中。

#### 7-1. パラダイム再整理 —「CLI + MCP + Skill」三范式（6月11日）⭐最重要

掘金（米小虾）「CLI + MCP + Skill：2026年AI Agent开发的三大范式」:
- 2026年のAI Agent開発における3パラダイム（CLI/MCP/Skill）を体系化
- Anthropicの「直連API / CLI+Skills / MCP+Skills」フレームワークを解説
- CLIとMCPは対立するものではなく適材適所で使い分けるべきと論じる
- 中国コミュニティでのパラダイム理解の成熟を示す画期的記事

**出典**: 掘金 2026-06-11

#### 7-2. AI Skills工程化（6月12日）

掘金（米小虾）「AI Skills 工程化：当每个开发者都有一支「AI 小队」」:
- MCP+Skillsパラダイムの発展形として、開発者が「AIチーム」をどう管理するかを論じる
- 「Skills over MCP」パッケージングの実践的考察
- 2日連続で米小虾氏が高品質MCP解説記事を公開したことが注目点

**出典**: 掘金 2026-06-12

#### 7-3. Hermes vs OpenClaw Agent Loop比較（6月10日）

掘金（吴佳浩Alben）「Hermes vs OpenClaw：基于源码的 Agent Loop 全面分析」:
- Hermes AgentとOpenClawのAgent Loopをソースコードレベルで比較分析
- 中国コミュニティでのエージェントフレームワーク競争の現状を示す

**出典**: 掘金 2026-06-10

#### 7-4. Anthropic中国制限議論（6月12日）

掘金（IT乐手）「Anthropic 为何限制中国大陆使用 Claude？」:
- MCP発祥企業Anthropicの中国戦略を分析
- Anthropicの中国本土でのClaude利用制限理由を考察
- MCP標準の中国採用に与える影響についてコミュニティで議論

**出典**: 掘金 2026-06-12

#### 7-5. 火山引擎Viking AI Search CLI（6月9日）

掘金「Viking AI 搜索 CLI 正式发布」:
- ByteDance火山引擎がViking AI Search CLIをリリース
- CLIツールとしてMCP Skillパラダイムに適合
- 火山引擎のMCPエコシステム（火山方舟・Trae）との連携が示唆される

**出典**: 掘金 2026-06-09

#### 7-6. 本期間に確認されなかったトピック

| トピック | 状況 |
|---------|------|
| AAIF新メンバー追加 | 確認されず |
| Alibaba Cloud百煉MCP | 新情報なし（5/20が最新） |
| ByteDance火山引擎MCP Server OSS | 新情報なし（5/19が最新） |
| 腾讯云MCP Gateway | 新情報なし（5/21が最新） |
| MCP脆弱性（CVE） | 新たな報告なし |
| A2A/AG-UIプロトコル | 言及なし |
| MCP標準化動向 | 新たな進展なし |

## 出典

- [多智能体协同从概念验证到规模生产 (知乎)](https://zhuanlan.zhihu.com/p/2020234672798442229)
- [2026年智能体范式大爆发 (立委NLP)](https://liweinlp.com/13484)
- [2026跨境电商MCP服务终极指南 (网易)](https://www.163.com/dy/article/KQ42Q9UG05564TOE.html)
- [途牛MCP开放平台上线 (新浪财经)](https://finance.sina.com.cn/roll/2026-03-10/doc-inhqnmhx6391543.shtml)
- [2026年企业级智能体平台选型指南 (BetterYeah)](https://www.betteryeah.com/blog/2026-enterprise-ai-agent-platform-selection-guide)
- [Top 50 Most Popular MCP Servers 2026 (Reddit/中文)](https://www.reddit.com/r/mcp/comments/1s3fu45/top_50_most_popular_mcp_servers_in_2026/?tl=zh-hans)
- [阿里悟空Agent OS (掘金)](https://juejin.cn/post/7618418125198196779)
- [QwenPaw Agent实现原理 (掘金)](https://juejin.cn/post/7645147490087403530)
- [AI Agent記憶システム設計比較 (掘金)](https://juejin.cn/post/7644628777114042420)
|- [FastAPI漏洞与AI Agent安全 (36kr)](https://36kr.com/p/3828901167911812)

## 2026年6月中旬〜7月の新展開

### MCP Stateless RC 最終仕様 — 2026年7月28日リリース予定

MCPプロトコルの重要なマイルストーン：**無状態（Stateless）RCの最終仕様**が2026年7月28日にリリース予定。Googleチーム（Cloud Run/Kubernetes）と共同開発：

- **セッションID廃止**: 既存のセッションベース通信を排除し、クラウドネイティブ環境での水平スケーリングを実現
- **SSE → Streamable HTTP**: Server-Sent Eventsを置き換え、ブラウザ環境でのネイティブ動作を実現
- **必須ルーティングヘッダー**: マルチテナント環境でのリクエストルーティングを標準化
- **OAuth 2.1 / OIDC**: 企業レベルの認証・認可を標準プロトコルで実現
- **12ヶ月の非推奨バッファー**: 既存のSSEベースサーバーへの影響緩和

**意義**: MCPの「最大の技術的課題」であったセッション状態と水平スケーリングの矛盾を解決。Kubernetes環境での本番デプロイが容易になり、企業採用が加速すると見られる。

> **出典**: Anthropic MCP公式ロードマップ、SiliconReport 2026-05-14 [Tier-2]

### 45日間のクロールギャップ（2026年6月13日〜7月28日）

2026年6月中旬から7月28日までの間、MCP中国生態系で目立った新規プラットフォーム発表は確認されなかった。ただし、以下の既知の進展が進行中：

| トピック | 状況 |
|---------|------|
| MCP Stateless最終仕様 | 7/28リリース予定 |
| AAIF新メンバー | 5/18以降の追加確認なし（現在190組織） |
| 新規CVE | 5月の波（CVE-2026-30615等）以降の新報告なし |
| Alibaba/Tencent/ByteDance MCP | 5月下旬の発表以降の新情報なし |
| DeepSeek V4.1 MCP対応 | 6月リリース予定のまま未確認 |
| MCP SDK月間DL | 3億回/月（4月末時点、更新なし） |
| 公開MCPサーバー数 | 9,400+（更新なし） |

## 2026年8月3日〜10日更新 — MCP理解の深化と教育コンテンツの成熟

### 1. MCP Serverの「三つの機能」理解が広まる（8月4日〜6日）⭐最重要
掘金で「**我写过 MCP Server，却一直以为 MCP 只有 Tool**」（8月4日）が公開。GitLab MCPサーバーを開発した経験者による反省記事：MCPをTool（ツール呼び出し）のみと誤解していた。実際にはMCPには3つのコア機能がある:
- **Tool**: ツール呼び出し（開発者が最も馴染み深い）
- **Resource**: データソースへのアクセス（コンテキスト提供）
- **Prompt**: プロンプトテンプレート（会話フロー定義）

同著者は翌日の「**Agent 已经能跑起来了，我却不知道怎样判断它好不好**」（8月6日）で、「MCP原理から実際のServerまで、Tool・Resource・Prompt・エラーバウンダリーを全て実践した」と報告。中国開発者コミュニティにおけるMCP理解の深化を示す。
- **出典**: [掘金 — MCP Server Tool](https://juejin.cn/post/7669999915607982134) (2026-08-04) | [掘金 — Agent評価](https://juejin.cn/post/7670798157669335086) (2026-08-06) [T1]

### 2. MCPツール・アプリケーションの新規公開（8月4日〜7日）

| ツール | 開発元 | 特徴 | 出典 |
|--------|--------|------|------|
| **iOS MCP调试工具** (SandboxServer) | xinghelee | iOS用APPレベルMCPデバッグツール。サンドボックスファイル操作、ネットワークキャプチャ、DB閲覧、スクリーンミラリング等をMCP経由で提供 | [V2EX](https://www.v2ex.com/t/1232119) (8/4) |
| **DataZen v0.0.8** | flyxl | Tauri v2 + Rust + React製DBクライアント（10MB未満）。PostgreSQL/MySQL/SQLite/Redis対応。MCPワークフロー機能搭載 | [V2EX](https://www.v2ex.com/t/1232833) (8/7) |
| **Linkly AI Note** | blueeon | MCP対応ローカルMarkdownノート。MCP隧道機能でChatGPT/Claude Web版から直接ノート読み書き可能 | [V2EX](https://www.v2ex.com/t/1232052) (8/4) |
| **codebase-memory-mcp** | 冬奇Lab | LightRAG（20,674ノード/94,517エッジ）上でベクトル/グラフ/記号の3路リコールを実装したコード知識庫MCP | [掘金](https://juejin.cn/post/7671153017660014655) (8/7) |

中国開発者コミュニティでは、MCPサーバー開発が「入門」フェーズから「多様なユースケース開発」フェーズへ移行中。

### 3. MCP JSON-RPC 2.0プロトコル学習記事（8月5日）
掘金で「**LLM Agent 底层揭秘：大模型如何通过 JSON-RPC 2.0 协议跨进程调工具？**」が公開。MCPの下位レイヤーであるJSON-RPC 2.0プロトコルを、工業級Agentフレームワークの観点から解説。MCP技術理解の深層化を示す。
- **出典**: [掘金](https://juejin.cn/post/7670174583553523712) (2026-08-05) [T1]

### 4. Agent Skills完全ガイド公開（8月8日〜9日）
掘金で「**Agent Skills 完全指南：从目录规范到渐进式加载的工程实践**」が公開（8月8日、👍6）。Agent Skillsの概念・構造・構築ガイドを体系的に解説。同時に「**滴滴面试官摇头：你 SKILL.md 全塞进 context 了，人家是按需加载的**」（8月7日〜9日、シリーズ3記事）で、SKILL.mdの最適なサイズと渐进式加载（プログレッシブローディング）の実践を考察。
- Anthropic文書に基づき、SKILL.mdは全量をコンテキストに読み込むのではなく、オンデマンドで取得すべきと主張
- 中国企業面接（字节跳動、滴滴）でSKILL.md設計が面接テーマとして登場
- **出典**: [掘金 — Skills完全ガイド](https://juejin.cn/post/7671467814255755315) (2026-08-08) | [掘金 — SKILL.md](https://juejin.cn/post/7670174583553523712) [T1]

### 5. Claude Code + MCP + Skillsチュートリアル継続（8月3日〜9日）
「**别再裸用 Claude Code 了！32 个亲测Skills + 8 个 MCP，开发效率直接拉满！**」が8月3日〜9日の間、掘金で6日連続でdigest上位にランクイン（最も長く持続したMCP関連記事）。32のSkills + 8つのMCPサーバーの実践的セットアップガイド。
- **出典**: [掘金](https://juejin.cn/post/7620060655607857178) (継続掲載) [T1]

### 6. 大模型工具調用とMCP安全境界（8月8日）
掘金で「**大模型工具调用与 MCP：格式、并行与安全边界**」が公開。OpenAI function callingからAnthropic MCPまで、構造化出力・並列呼び出し・プロトコル設計・エンジニアリングセキュリティ境界を網羅的に解説。
- **出典**: [掘金](https://juejin.cn/post/7671607298570108982) (2026-08-08) [T1]

### 7. LiteLLMセキュリティ警告（8月4日、MCPエコシステム影響）
36krが「**建议立即检查并移除LiteLLM**」を報道。LiteLLMはMCPエコシステムでも広く使用されるLLMプロキシで、セキュリティ脆弱性が報告された。MCP依存チェーンのリスク管理が浮き彫りに。
- **出典**: [36kr](https://36kr.com/p/3924989565302921) (2026-08-04) [T1]

### 8. 本期間に確認されなかったトピック

| トピック | 状況 |
|---------|------|
| AAIF新メンバー追加 | 確認されず（5/18以降、現在190組織） |
| 新規CVE（MCP固有） | 確認されず（5月の波以降、新報告なし） |
| Alibaba Cloud百煉MCP | 新情報なし（5/20が最新） |
| Tencent Cloud MCP Gateway | 新情報なし（5/21が最新） |
| ByteDance火山引擎MCP Server | 新情報なし（5/19が最新） |
| MCP Stateless最終仕様 | 7/28リリース予定→進捗不明 |
| MCP SDK月間DL | 3億回/月（4月末時点、更新なし） |
| 公開MCPサーバー数 | 9,400+（更新なし） |

### 9. 8月上旬の全体評価：「理解深化期」
2026年8月3日〜10日のMCP中国生態は、新規プラットフォーム発表やCVE開示といった「インパクトニュース」は確認されなかった。代わりに、以下のような**静かな質的進化**が進行:

1. **MCP Server開発者による自己反省**: Tool/Resource/Prompt三機能の理解が広まり、MCP Server開発の質が向上
2. **MCPツールの多様化**: iOSデバッグ、DBクライアント、ノートアプリ、コード知識庫など、ユースケースが拡散
3. **Agent Skills定義**: SKILL.mdの最適化、渐进式加载が実践され、面接テーマに
4. **安全意識**: LiteLLM脆弱性報告がMCP依存チェーンリスクを再認識
5. **教育コンテンツ成熟**: JSON-RPC 2.0、MCP安全境界など、技術的深みのある解説が登場

**結論**: 2026年8月上旬は、MCP中国生態にとって「**理解深化期**」と言える。新規インフラ発表ではなく、既存インフラの適切な使い方と理解が深まっているフェーズ。

**出典**: wiki既存情報およびweb調査結果に基づく

## 関連リンク
