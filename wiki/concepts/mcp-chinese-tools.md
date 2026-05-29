---
title: "中国MCPツールエコシステム — 中国語圏向けMCP Server/SDK一覧"
type: concept
tags: [mcp, chinese-ai, tool-integration, feishu, dingtalk, wecom, wechat, open-source, server]
created: 2026-04-27
updated: 2026-05-29
source_lang: zh-CN
aliases: ["中国MCP工具生态", "China MCP Servers", "中文MCP服务器"]
---

# 中国MCPツールエコシステム

> **関連エンティティ**: [[mcp-china]], [[mcp]], [[china-ai-agent-ecosystem]], [[feishu]], [[dingtalk]], [[wecom]], [[openclaw]]

中国国内向けに特化したMCP Server/SDKのエコシステム。2026年3月以降、中国の主要SaaSプラットフォーム（飛書、钉钉、企业微信等）がMCP Serverを提供開始。中国市場独自のチャネル要件（微信生態、QQ、通訊規制等）に対応したツール群が急速に整備されている。

## 主要MCP Server一覧

### 1. 飞书（Feishu/Lark）MCP Server

| 項目 | 詳細 |
|------|------|
| 開発元 | コミュニティ（huanglei288766/china-mcp-servers） |
| 言語 | TypeScript |
| 状態 | ✅ 実用可能 |
| ライセンス | MIT |
| リポジトリ | [github.com/huanglei288766/china-mcp-servers](https://github.com/huanglei288766/china-mcp-servers) |

**提供ツール**:
- `feishu_send_message` — テキスト/リッチテキスト/カードメッセージ送信（個人・グループ対応）
- `feishu_get_messages` — セッションメッセージ履歴取得
- `feishu_create_doc` — 飛書ドキュメント作成
- `feishu_get_doc` — ドキュメント内容読み取り
- `feishu_get_calendar` — スケジュール照会
- `feishu_create_event` — 会議/スケジュール作成
- `feishu_create_task` — タスク作成
| `feishu_list_tasks` — タスク一覧表示

**2026年5月更新: 飛書公式MCP（End user call remote MCP server / Beta）**

2026年5月、飛書（Lark）が**公式MCP機能**（End user call remote MCP server）を提供開始（Beta）。従来はコミュニティ版のみだったが、飛書公式が直接MCPサーバーをホスト・管理する新しいパラダイム。

**公式 MCP Server リスト（飛書内蔵）**:
- **飛書ドキュメント管理** — ドキュメント作成・編集・検索
- **飛書カレンダー** — スケジュール作成・照会
- **飛書メッセージ** — メッセージ送信・検索
- **飛書メール** — メール送信・受信
- **飛書スプレッドシート** — シート作成・編集
- **飛書AI Bot** — カスタムAI Botの管理

**設定方法（飛書管理画面）**:
1. **管理者**が飛書管理コンソールでMCPサーバーを登録
2. エンドユーザーは**クライアント設定**から飛書公式MCPサーバーを選択
3. 飛書自身が認証（OAuth 2.0）とトークン管理を一元化
4. エンドユーザーはAPIキー不要で利用可能

**意義**: 
- コミュニティ版と公式版の2系統が並存
- 公式版は飛書内のセキュリティ境界内で動作し、外部キー管理不要
- エンタープライズ向けに設計されたスケーラブルなMCP基盤

### 2. 钉钉（DingTalk）MCP Server

| 項目 | 詳細 |
|------|------|
| 開発元 | 钉钉公式（open-dingtalk/dingtalk-mcp） + コミュニティ版 |
| 言語 | TypeScript |
| 状態 | ✅ 実用可能（公式サポート） |
| ライセンス | MIT |
| 公式Doc | [open.dingtalk.com/document/ai-dev/dingtalk-server-api-mcp-overview](https://open.dingtalk.com/document/ai-dev/dingtalk-server-api-mcp-overview) |

**2系統のモード**:
1. **Webhookモード（5分でセットアップ）**: グループロボットメッセージ送信
2. **企業アプリケーションモード**: 全機能利用可能

**提供ツール（企業アプリケーションモード、活性化するProfileで制御）**:

| ProfileId | 機能 | 権限 |
|-----------|------|------|
| dingtalk-contacts | 連絡先管理 | qyapi_addresslist_search等 |
| dingtalk-department | 部門管理 | qyapi_get_department_list等 |
| dingtalk-robot-send-message | ロボットメッセージ/DING送信 | Premium.Ding.Write |
| dingtalk-honor | 企業文化栄誉 | OrgCulture.Honor.Read |
| dingtalk-tasks | ToDo管理 | Todo.Todo.Write/Read |
| dingtalk-calendar | スケジュール | Calendar.Event.Write/Read |
| dingtalk-checkin | 出退勤 | qyapi_checkin_read |
| dingtalk-notice | 仕事通知 | — |
| dingtalk-app-manage | アプリ管理 | qyapi_microapp_manage |
| dingtalk-service-window | サービス窓口 | OfficialAccount.* |
| dingtalk-teambition | プロジェクト管理 | Project.* |
| dingtalk-report | 日報管理 | qyapi_report_* |

**設定例**:
```json
{
  "mcpServers": {
    "dingtalk-mcp": {
      "command": "npx",
      "args": ["-y", "dingtalk-mcp@latest"],
      "env": {
        "DINGTALK_Client_ID": "your_client_id",
        "DINGTALK_Client_Secret": "your_client_secret",
        "ACTIVE_PROFILES": "dingtalk-contacts,dingtalk-calendar"
      }
    }
  }
}
```

### 3. 企业微信（WeCom）MCP Server

| 項目 | 詳細 |
|------|------|
| 開発元 | コミュニティ（china-mcp-servers） |
| 言語 | TypeScript |
| 状態 | ✅ 実用可能 |
| ライセンス | MIT |

**2系統のモード**:
1. **グループロボットWebhook（最も簡単）**: npx @china-mcp/wecom-mcp
2. **企業アプリモード（全機能）**: CorpID + Secret + AgentID で認証

**提供ツール**:
- `wecom_send_webhook` — グループロボットメッセージ（テキスト/Markdown）
- `wecom_send_message` — アプリメッセージ（text/markdown/textcard）
- `wecom_get_user` — ユーザー詳細情報取得
- `wecom_list_department_users` — 部門メンバー一覧
- `wecom_create_schedule` — スケジュール作成

### 4. OpenClaw China — 中国IMチャネル拡張

| 項目 | 詳細 |
|------|------|
| リポジトリ | [github.com/BytePioneer-AI/openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) |
| 対象 | OpenClaw Agentフレームワークへの中国IMチャネル追加 |

**対応チャネル一覧**:

| プラットフォーム | 状態 | 設定難易度 |
|----------------|------|-----------|
| 钉钉 | ✅ 可用 | 簡単 |
| QQロボット | ✅ 可用 | 簡単 |
| 企業微信（智能ロボット） | ✅ 可用 | 簡単 |
| 企業微信（自建アプリ→微信） | ✅ 可用 | 中 |
| 微信客服（外部微信ユーザー） | ✅ 可用 | 中 |
| 微信公众号（購読/サービス） | ✅ 可用 | 中 |
| 飛書（公式プラグイン） | ✅ 可用 | 中 |

**機能サポートマトリックス**:
- **テキスト**: 全チャネル対応
- **Markdown**: 微信客服以外対応
- **ストリーミング**: 钉钉/QQ/企業微信智能ロボット対応
- **画像/ファイル**: 大半対応（微信客服は開発中）
- **音声**: 钉钉/QQ/企業微信/公众号対応
- **グループチャット**: 钉钉/飛書/QQ/企業微信対応
- **マルチアカウント**: 大半対応

### 5. picoclaw MCP Tools統合

| 項目 | 詳細 |
|------|------|
| リポジトリ | [github.com/sipeed/picoclaw](https://github.com/sipeed/picoclaw) |
| 言語 | Go |
| 状態 | PR #282 — レビュー済み/マージ準備完了 |

軽量AgentフレームワークpicoclawへのMCPツールサポート追加：
- Go SDK v1.3.0を使用
- stdio/SSE/HTTP 3種類のトランスポート対応
- `mcp_{server}_{tool}` 命名規則で自動ツール登録
- Dockerフルランタイムサポート（Node.js/Python同梱）
- 軽量バイナリ（～15MB）で低リソースデバイスでもHTTP/SSE接続可能
- 設定例：

```json
{
  "tools": {
    "mcp": {
      "enabled": true,
      "servers": {
        "github": {
          "url": "https://mcp.example.com/github",
          "type": "sse"
        }
      }
    }
  }
}
```

### 6. Claude Code MCPツール統合実例（2026年4月）

Juejinで「MCP神器推薦：Claude Codeに画像閲覧・検索・ドキュメント参照を可能にする」という記事が公開された。Claude Codeに複数のMCPサーバーを統合し、以下の能力を付与した具体例：

- **画像認識**: 視覚情報に基づくコード生成・デバッグ
- **Web検索**: リアルタイムの情報取得とコンテキスト補完
- **ドキュメント参照**: APIドキュメントや技術資料の自動検索

これはMCPプロトコルが単なる仕様ではなく、実際の開発ワークフローに即座に統合可能な「ツールバス」として機能していることを示す好例。

📎 出典: [Juejin — MCP神器推薦](https://juejin.cn/post/7597709339982708776)（10いいね・23スター）`[Tier-2: 掘金/技術コミュニティ]`

## 2026年5月14日〜20日の重要アップデート

### 8. 新华财经 MCP 服务矩阵（2026-05-18）

| 項目 | 詳細 |
|------|------|
| 発表元 | 新华财经（中国金融信息网） |
| 発表日 | 2026-05-18 |
| ステータス | ✅ 正式公開 |

2026年5月18日、新华财经（Xinhua Finance）が**MCP服务矩阵**（MCPサービス行列）を正式発表。国家級金融データインフラにMCPプロトコルを導入し、AI智能体（Agent）に権威ある金融データ基盤を提供する取り組み。

**六大類MCP服务体系（6大カテゴリ、30+ MCPサービス）**:

| カテゴリ | 内容 |
|---------|------|
| 实时行情（リアルタイム相場） | 国内外取引所のリアルタイム価格データ |
| 金融市场（金融市場） | 株/債券/ファンド/商品データ |
| 宏观行业（マクロ・業界） | 中国マクロ経済・世界経済・業界指標 |
| 企业数据（企業データ） | 企業工商情報・株主構成・リスクスキャン |
| 资讯公告（ニュース・公告） | 7×24時間ニュース速報、上場企業公告 |
| 政策研报（政策・レポート） | 18万+政策法规、6000+発行機関、研究レポート |

**五大核心应用场景（5大コアユースケース）**:
1. **宏观研判与区域研究**: 中国マクロ・省市区県4級データを自然言語で即時取得
2. **政策合规与风险预警**: 18万+政策法规のセマンティック検索、履歴追跡
3. **企业全景尽调与股权穿透**: 1.5億件の企業「レッドブラックリスト」、45類部委监管データ直結
4. **投研决策与市场交易**: 5500+沪深北上場企業、2700+香港上場企業、12000+債券発行企業対応
5. **智能研报与资讯关联解读**: 日次1000+研報更新、業界・機関フィルタリング

**意义**: 国家レベルの金融データプラットフォームがMCPを採用した初の事例。金融AIのデータコンプライアンス（データソースの追跡可能性・監査可能性）を確保する「国家的金融AIデータ合规基盤」として位置づけられる。

📎 出典: [新华财经 — 解决金融AI数据合规痛点](https://m.cnfin.com/hg-lb//zixun/20260518/4413883_1.html) `[T1: 新华财经/国家級金融情報]`

### 9. 腾讯云 MCP广场 新サーバー群（2026年5月）

腾讯云 MCP广场に2026年5月、新たに4つのMCP Serverが追加公開された。

#### 9.1 实时音视频（TRTC）MCP Server — 2026-05-19

| 項目 | 詳細 |
|------|------|
| URL | [cloud.tencent.com/developer/mcp/server/11784](https://cloud.tencent.com/developer/mcp/server/11784) |
| 提供元 | 腾讯云TRTC团队 |
| パッケージ | `@tencent-rtc/mcp`（npm） |
| 状態 | ✅ 実用可能 |

Tencent RTC MCP Serverは、LLMがTRTC（Tencent Real-Time Communication）のSDK・APIを理解・操作できるようにするMCPサーバー。主な機能：
- **TUICallKit統合ドキュメント取得**: React/Vue/Android/iOS/Flutter各プラットフォームの最新ドキュメントを取得
- **テストUserSig生成**: SDKAppID + SecretKeyからUserSig自動生成
- **コード生成支援**: AIが自然言語からプロジェクト初期化・SDK統合コードを自動生成

**対応クライアント**: Cursor, Trae, CodeBuddy, Claude Code, Codex CLI

特に注目すべきはTRTC Migration Assistant MCP（2026-04-17公開）：Agora、Zego、Twilioなどの競合RTCベンダーからの移行コードをAIが自動変換するツール。

📎 出典: [腾讯云TRTC MCP Server](https://cloud.tencent.com/developer/mcp/server/11784) `[T1: 腾讯云公式]`

#### 9.2 容器服务（TKE）MCP Server — 2026-05-18

| 項目 | 詳細 |
|------|------|
| URL | [cloud.tencent.com/developer/mcp/server/11804](https://cloud.tencent.com/developer/mcp/server/11804) |
| 提供元 | 腾讯云TKE团队 |
| パッケージ | `tke-mcp-server`（PyPI） |
| 状態 | ✅ 実用可能 |

TKE（Tencent Kubernetes Engine）クラスタ管理のためのMCP Server。以下のツールを提供：
- クラスタ照会: `DescribeClusters`, `DescribeClusterStatus`, `DescribeClusterKubeconfig`
- エンドポイント管理: `CreateClusterEndpoint`, `DeleteClusterEndpoint`
- ノードプール管理: `DescribeNodePools`
- **動的ツール生成**: McpAPI YAMLファイルから自動ツール生成
- **CodeBuddy Skill対応**: MCP Server不要でCodeBuddy内で直接利用可能

📎 出典: [腾讯云TKE MCP Server](https://cloud.tencent.com/developer/mcp/server/11804) `[T1: 腾讯云公式]`

#### 9.3 且慢MCP（盈米基金投顾）— 2026-05-18

| 項目 | 詳細 |
|------|------|
| URL | [cloud.tencent.com/developer/mcp/server/11801](https://cloud.tencent.com/developer/mcp/server/11801) |
| 提供元 | 盈米且慢（Qieman） |
| 状態 | ✅ 実用可能（云托管） |

且慢MCP Serverは、基金分析・資産配置・投資ポートフォリオ診断のためのMCPサーバー。特徴：
- **云托管モード**: ローカルデプロイ不要、Streamable HTTP / SSEで直接接続
- **主なツール**: ファンド基本情報/履歴パフォーマンス/保有構成/配当記録、資産配分最適化
- **対応クライアント**: Claude Desktop, Cursor, Trae, Cherry Studio等

📎 出典: [且慢MCP Server](https://cloud.tencent.com/developer/mcp/server/11801) `[T1: 腾讯云MCP广场]`

#### 9.4 弹性伸缩（AS）MCP Server — 2026-05-07

| 項目 | 詳細 |
|------|------|
| URL | [cloud.tencent.com/developer/mcp/server/11730](https://cloud.tencent.com/developer/mcp/server/11730) |
| 提供元 | 腾讯云CVM团队 |
| パッケージ | `mcp-server-as`（PyPI） |
| 状態 | ✅ 実用可能 |

Auto Scaling（AS）のMCP Server。自動スケーリンググループの完全ライフサイクル管理を提供：
- `CreateAutoScalingGroup`, `DescribeAutoScalingGroups`, `ModifyAutoScalingGroup`
- `EnableAutoScalingGroup`, `DisableAutoScalingGroup`
- `ExecuteScalingPolicy`, `ModifyDesiredCapacity`

📎 出典: [腾讯云AS MCP Server](https://cloud.tencent.com/developer/mcp/server/11730) `[T1: 腾讯云公式]`

### 10. 钉钉（DingTalk）MCP 广场 — 6000+ 企業級MCPサービス

| 項目 | 詳細 |
|------|------|
| URL | [mcp.dingtalk.com](https://mcp.dingtalk.com/) |
| 公式Doc | [developers.dingtalk.com](https://developers.dingtalk.com/document/aipass/mcp-square-introduction) |
| 状態 | ✅ 実用可能 |

钉钉が**MCP广场**（MCPサービス廣場）として6000+の企業級MCPサービスを提供。中国最大規模の企業向けAIスキルマーケット。

**2つの供給源**:
1. **钉钉公式MCP**: ドキュメントAI、AI表格、会議、日程、TODO、審査など钉钉自身のSaaS機能
2. **生态MCP广场**: サードパーティ製MCPサービス（AIGC、OCR、音声認識、契約審査など）

**傳統MCP vs 钉钉MCP廣場の差別化要因**:

| 観点 | 傳統MCP | 钉钉MCP广场 |
|------|---------|------------|
| 接続 | 各社別にAPIキー管理 | 钉钉内でワンクリック有効化 |
| 課金 | 各社別課金 | 統一「算粒」従量課金 |
| 試用 | 前払い必須 | 全組織に週次無料枠 |
| 管理 | 権限・監査分散 | 統一指認・使用量管理・操作監査 |

**統合方式**: ①钉钉内Deap/AI Assistantに直接統合 ②標準RESTful APIで外部Agentと連携（阿里雲百煉等）

📎 出典: [钉钉开放平台 — MCP广场概述](https://developers.dingtalk.com/document/aipass/mcp-square-introduction) `[T1: 钉钉公式]`

### 11. 支付宝（Alipay）MCP Server — 国内初の決済MCP

| 項目 | 詳細 |
|------|------|
| 提供元 | 支付宝（Alipay）/ 蚂蚁集团 |
| 発表日 | 2026-04-15（支付宝）+ 2026-04-16（蚂蚁百宝箱） |
| 状態 | ✅ 実用可能（体験版+本番版） |

2026年4月15日、支付宝が**支付MCP Server**（国内初の決済MCP）を発表。4月16日には蚂蚁智能体平台「百宝箱」でMCP专区を開設。

**支付宝 MCP Server 5大核心インタフェース**:
| ツール名 | 機能 |
|---------|------|
| `create-mobile-alipay-payment` | モバイル決済リンク生成（Markdown形式） |
| `create-web-page-alipay-payment` | PC決済QRコードリンク生成 |
| `query-alipay-payment` | 注文ステータス照会 |
| `refund-alipay-payment` | 返金処理 |
| `query-alipay-refund` | 返金状況照会 |

**蚂蚁百宝箱 MCP专区**:
- 支付宝・高德地图・无影（Wuying Cloud Desktop）等30+ MCPサービス
- **2つのモード**: ①全周期托管（1分でMCP対応Agent構築）②快速部署（動的MCPロード）
- 対応モデル: DeepSeek、通义千问、Kimi、智谱等
- IIFAA智能体可信互联工作组によるセキュリティ連携

📎 出典: [支付宝支付MCP Server（同花顺）](https://www.smcphub.com/mcp-server/43), [蚂蚁百宝箱MCP专区（东方财富）](https://finance.eastmoney.com/a/202504163378770895.html) `[T1: 公式/報道]`

### 12. 同花顺 iFinD MCP（金融データMCP、2026年3月〜4月更新）

| 項目 | 詳細 |
|------|------|
| 提供元 | 同花顺（Hithink RoyalFlush） |
| 発表日 | 2026-03-12（初版）、2026-04-30（4大データツール追加） |
| 状態 | ✅ 実用可能 |

iFinD MCPは金融データ端末大手の同花顺が提供する金融データMCP。**4大核心モジュール**:
- A株分析: スマート選株、日/週/月相場、財務諸表、リスクモデル（Alpha/Beta/Sharpe/VaR）、ESG評価等
- 公募基金分析: ファンド選別、基本情報、履歴業績、保有構成、配当記録等
- マクロ経済・業界データ: 世界/中国/地域マクロ指標、業界データ、コモディティ全チェーン
- 公告とニュース: A株/基金/港美股公告意味検索、ニュース要約

**2026-04-30アップデート**: 債券、港美股、指数、板块の4大データツールを追加。

📎 出典: [同花顺 iFinD MCP正式上线（2026-03-12）](https://news.10jqka.com.cn/20260312/c675239015.shtml), [iFinD MCP新增数据工具（2026-04-30）](https://www.sina.cn/news/detail/5293360119545992.html) `[T2: 報道]`

### 13. 天翼云 MCP 托管服务（2026-04-21）

| 項目 | 詳細 |
|------|------|
| 提供元 | 天翼云（China Telecom Cloud） |
| 更新日 | 2026-04-21 |
| 状態 | ✅ 実用可能 |

天翼云が**云原生API网关**の「MCP管理」機能を正式リリース。AI网关を通じてMCP Serverの一元管理を実現：
- MCP服务直接代理モード（SSE / Streamable HTTP双方対応）
- MCP接入点のドメイン・パス管理
- MCPサービスの公開・停止・削除のライフサイクル管理

中国三大キャリア（中国電信）のクラウドがMCP対応に参入したことを示す。

📎 出典: [天翼云 托管MCP服务](https://www.ctyun.cn/document/11005917/11091632) `[T1: 天翼云公式]`

### 14. 华为云 Serverless + MCP 融合方案

| 項目 | 詳細 |
|------|------|
| 提供元 | 华为云 |
| 状態 | ✅ 実用可能 |

华为云が**AI原生应用运行平台 + MCP**の製品組合せ方案を発表。Serverless関数計算（FunctionGraph）とMCPを融合：
- MCP ServerをFunctionGraphにデプロイ→ミリ秒単位の弾性スケーリング
- 30秒でMCP Serverデプロイ（事前構築テンプレート）
- MCP注册/配置中心（CSE）+ Nacos自動登録・発見
- アプリケーションテンプレート: server-github等のプリセットMCP

📎 出典: [华为云 Serverless与MCP融合创新（博客园）](https://www.cnblogs.com/huaweiyun/p/18844849) `[T2: 华为云博客]`

### 15. その他注目アップデート

#### mcp-notify（通知MCP Server）

2025年末に登場した`mcp-notify`は、中国IMチャネルをネイティブサポートする通知MCP Serverとして注目を集めている。**対応チャネル**:
- 企业微信（WeCom）: グループロボット + アプリケーション
- 钉钉（DingTalk）: グループロボット
- 飞书（Feishu/Lark）: グループロボット
- Telegram, Bark, PushPlus, Ntfy, Home Assistant 等

GitHubスター26。`uvx mcp-notify`で即時利用可能。中国IM対応ツールとしてClaude Code等で活用されている。

📎 出典: [GitHub - iflow-mcp/mcp-notify](https://github.com/iflow-mcp/mcp-notify) `[T3: コミュニティ]`

#### 百度 MCP 生態の進展

百度搜索開放プラットフォーム「MCP广场」が2026年5月時点で**1.6万+のMCP Server**を収録。百度智能云千帆プラットフォームが国内最大のMCPエコシステムに成長。主なMCP Server:
- 百度搜索MCP（文心大模型联网搜索）— 市场最高と李彦宏が主張
- 百度地图MCP（10コアAPI、ルート最適化＋交通管制Agent連携）
- 百度电商MCP（国内初のEC決済対応MCP）
- 百度文库/百度网盘MCP（コンテンツ生成）
- AI开放能力13種MCP Server（文字認識・顔認識・音声認識等70ツール）

📎 出典: [36氪 — 百度搜索收录MCP server超1.6万](https://36kr.com/newsflashes/3334623759493377), [百度智能云千帆MCP广场](https://cloud.baidu.com/doc/qianfan/s/1mh4stp3t) `[T1: 公式/報道]`

### 7. その他の注目MCP Server

- **GitHub MCP Server**（github/github-mcp-server）: Go実装、29K Stars、Anthropic共同開発。中国開発者にも広く利用されている
- **Microsoft MCP Serverカタログ**: Azure MCP Server 2.0.0（2026-04-10）、84リリース
- **Docker MCP Toolkit**: コンテナ運用とMCPの統合を標準化
- **mcp-notify**（mcp-notify/mcp-notify）: デスクトップ通知MCP Server。Mac（terminal-notifier）、Windows（snoretoast）、Linux（notify-send）対応。MCP経由でAI Agentがユーザーに通知を送信できる。軽量バイナリ配布。Claude Code/Claude Desktop/Cursor連携実績
- **腾讯云 MCP Server マーケットプレイス**（2026年5月）: 腾讯云がMCP Serverの統一マーケットプレイスを開設。同プラットフォーム上で複数のSaaS/クラウドサービスのMCPサーバーを一元管理可能。中国クラウド事業者として初の取り組み

## 2026年5月22日〜29日の重要アップデート

### 16. MCPプロトコル無状態RC（Release Candidate）リリース（2026-05-21）

2026年5月21日、MCP仕様の新版Release Candidateが発表され、**無状態（Stateless）アーキテクチャへの移行**が主要変更として注目を集めた。

**主な変更点**:
- **ハンドシェイク廃止**: バージョン交渉・能力ネゴシエーションを各リクエストの `_meta` フィールドに統合
- **セッションID廃止**: ステートフルなセッション管理を完全排除 → 水平スケーリングが容易に
- **SSE長接続 → Streamable HTTP（Multi Round-Trip）**に置き換え
- **強制ルーティングヘッダー**: ゲートウェイがボディを解析せずにルーティング可能
- **認証強化**: OAuth 2.1 / OIDC準拠、iss検証の強制化
- **最終仕様**: 2026年7月28日リリース予定。12ヶ月の廃棄緩衝期間あり

📎 出典: [优码云 — 协议无状态架构深度拆解](https://www.umayun.com/blog/27981151) `[T2: 技術ブログ]`

中国の開発者コミュニティでもこの変更は大きな注目を集めており、stickyルーティングと共有状態ストレージがアーキテクチャから削除できる点が特に評価されている。

### 17. 阿里云「芯-雲-モデル-推論」全栈Agent化（2026-05-20）

2026年5月20日、阿里云峰会にてリージョンVP李飛飛が**32+のAgentic Cloud新製品**を発表。従来の雲製品をAgentが「関数呼び出しのように」使える標準化モジュールに改造：

- **雲製品のSkill化・MCP化・CLI化**: Agentから直接呼び出し可能なMCP Tool化
- **百煉（Bailian）推理平台全面開放**: 智譜GLM-5.1、MiniMax M2.7、Kimi K2.6など150+モデル統合
- **Agentic RL**: Agent実行フィードバックに基づく強化学習メカニズム
- **千問雲（qianwenai.com）**: 新AI製品サイト、一行の命令で全機能をAgentから呼び出し可能

阿里雲が自社クラウド製品をMCP化する方針は、中国クラウド市場におけるMCP標準化競争の新たな段階を示す。

📎 出典: [智東西 — 阿里李飛飛32新品](https://zhidx.com/p/559187.html), [和訊科技](https://tech.hexun.com/2026-05-20/224185662.html) `[T2: 業界報道]`

### 18. 腾讯云 MCP Gateway — 既存APIをゼロコードでMCP変換（2026-05-21）

腾讯云开发者社区が**MCP Gateway**を発表。RESTful APIをコード不要でMCP Toolに変換する基盤：

- **AI Gatewayの一部**: プロトコル変換・アクセス制御・監査を一括処理
- **「智能貸付顧問」**ユースケースでデモ公開
- **同時期の新MCP Server公開**: TKE（コンテナ管理）MCP、**联网搜索MCP（標準版）**、**MySQL智能服务MCP**
- **対応クライアント**: Cursor, Trae, CodeBuddy, Claude Code, Codex CLI

既存APIをMCP Tool化する「MCPラッピング」がゼロコードで可能になった点は、企業のMCP導入ハードルを大幅に下げる。

📎 出典: [腾讯云开发者社区 — MCP网关](https://developer.cloud.tencent.com.cn/article/2671873) `[T1: 腾讯云公式]`

### 19. 国家政策「智能体規範応用と創新発展実施意見」（2026-05-08）

2026年5月8日、国家网信办・国家発展改革委・工業情報化部の三部門が連名で**《智能体規範応用と創新発展実施意見》**を発表：

- 智能体（AI Agent）を公式定義：「自主感知・記憶・意思決定・対話・実行能力を持つ智能システム」
- **智能体相互接続プロトコル（AIP）**の国家標準・業界標準の普及を推進
- MCPのような標準化インターフェースを国家政策の一部として位置づけ
- 2026年は「中国智能体規模化元年」と業界認識

中国初のAI Agent向け国家政策であり、MCP/AIPなどのプロトコル標準化を国家レベルで推進することを宣言した点で極めて重要。

📎 出典: [中央网信办公式発表](https://www.cac.gov.cn/2026-05/08/c_1779979789523320.htm), [教育网まとめ](https://www.edu.cn/xxh/focus/zc/202605/t20260528_2738385.shtml) `[T1: 国家政策]`

### 20. MCPセキュリティベンチマーク MSB — 北京郵電大学がICLR 2026で発表

北京郵電大学の研究チームがMCPに特化したセキュリティベンチマーク**MSB（MCP Security Bench）**を発表（ICLR 2026採択）：

- **12種類の攻撃手法**を分類：名称衝突、設定操作、プロンプトインジェクション、パラメータ範囲外要求等
- **10の実環境シナリオ**、**405の実ツール**、**2,000攻撃インスタンス**で評価
- GPT-5、DeepSeek-V3.1、Claude 4 Sonnet、Qwen3等10モデルをテスト
- **平均攻撃成功率（ASR）40.35%** — 性能の高いモデルほど攻撃を受けやすい
- 新指標 **NRP（Net Resilient Performance）** を提案：セキュリティと実用性のバランス定量化

中国初のMCPセキュリティに関する学術ベンチマークであり、業界のセキュリティ実装に影響を与える可能性。

📎 出典: [36氪 — MSB: MCP安全基准发布](https://36kr.com/p/3768662327935747), [arXiv論文](https://arxiv.org/pdf/2510.15994) `[T1: 学術/報道]`

### 21. 钉钉「悟空」Agent OS発表（2026-05-21、成都钉峰会）

2026年5月21日、钉钉が成都で钉峰会を開催し**Agent OS（悟空）**を発表：

- 「人駆動からAgent駆動へ」の移行を掲げる
- MCP广场は**6,000以上のMCP能力**をカバー（引き続き中国最大の企業MCP市場）
- 4社（重慶富民銀行、西蔵薬業、山水集團、四川菊楽食品）と戦略契約
- OpenClawとの連携も深化（公式ドキュメントで連携手順を提供）

📎 出典: [IT之家 — 钉峰会](https://www.ithome.com/0/954/011.htm), [36氪](https://www.36kr.com/p/3610743632446728) `[T1: 報道]`

### 22. 字节跳动扣子（Coze）Space MCP拡張強化（2026年5月）

字节跳动のCoze SpaceがMCP拡張機能を強化：

- **新MCP拡張追加**: 音楽生成、水滴信用（企業信用情報）、飛常準（航空データ）
- **ワンクリックMCP拡張发布**: Cozeで作成したアプリを即座にMCP拡張として公開可能
- **ワークフロー→MCPツール化**: ワークフローをMCP Tool化し汎用Agentから呼び出し可能
- 実践チュートリアル多数公開

📎 出典: [扣子官方微信](https://mp.weixin.qq.com/s/7VhruC_F8q6vknekCNmMNQ), [火山引擎開発者社区](https://developer.volcengine.com/articles/7527890176979238948) `[T1: 公式]`

### 23. 中国MCPエコシステム統計（2026-05-20時点）

AgentScout MCP生態周度追踪報告より：

- MCPタグ付きGitHubリポジトリ：**420**（前週401から+19、週間成長率4.7%）
- トップ30リポジトリの合計スター数：**267,845**
- FastMCP（Python）：25,221スター、日間ダウンロード100万+
- mcp-use（全栈フレームワーク）：9,968スターで初登場6位
- Unity MCP統合が急成長（3つのUnity関連MCPがトップ30に）

📎 出典: [AgentScout MCP生態週度追踪](https://agentscout.live/zh/tech/dev-tools/data/mcp-ecosystem-weekly-20260520/) `[T2: データ分析]`

## 中国MCPツール生態の特徴

### 1. 中国IMチャネルの重要性
中国のMCP Serverエコシステムは、欧米とは異なり **IMプラットフォーム（微信/钉钉/飛書）** がハブの役割を果たす。欧米のSlack/Teams MCPと同様だが、複数IMの並存と微信生態の複雑性（个人微信・企業微信・公众号・微信客服）が中国独自の複雑さを生んでいる。

### 2. コミュニティから公式へ — 急速な公式MCP対応
2026年3月時点ではコミュニティ開発が主流だったが、5月には**飛書公式MCP（Beta）** と **钉钉MCP（公式）** の2大SaaSが公式MCP Serverを提供開始。従来の「コミュニティ駆動」から「プラットフォーマー公式対応」への急速な移行が進行中。

### 3. 腾讯云MCPマーケットプレイスの登場
2026年5月、腾讯云が中国クラウド事業者として初の**MCP Server統一マーケットプレイス**を開設。SaaS/クラウドサービスのMCPサーバーを一元管理できるプラットフォームで、中国におけるMCPエコシステムのインフラ化が加速。

### 4. 認証の複雑性
中国SaaSプラットフォームへのMCP接続には、各プラットフォーム固有の認証方式（ClientID+Secret、CorpID+AgentID、Webhook Token等）への対応が必要。MCP Auth仕様の標準化（2026年3月）により状況改善が見込まれる。

### 5. MCPツール呼び出し性能の中国モデル優位性
- **Qwen3.6-35B-A3B**: MCPMark 37.0%（Gemma 4-31Bの2倍以上）
- **GLM-5.1**: MCP Atlas 71.8%（世界最高、GPT-5.4の67.2%を上回る）
- 中国モデルはMCPツール呼び出し精度で世界最先端を走る

## 関連リンク

### 内部リンク
- [[mcp-china]] — MCP中国全体エコシステム
- [[mcp]] — MCPプロトコルの基本概念
- [[china-ai-agent-ecosystem]] — 中国AI Agent生態
- [[openclaw]] — OpenClawフレームワーク

### GitHubリポジトリ
| リポジトリ | Stars | 説明 |
|-----------|-------|------|
| [china-mcp-servers](https://github.com/huanglei288766/china-mcp-servers) | ★新規 | 飛書/钉钉/企微MCP |
| [open-dingtalk/dingtalk-mcp](https://github.com/open-dingtalk/dingtalk-mcp) | 钉钉公式 | 全機能カバー |
| [openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) | — | OpenClaw IMチャネル |
| [picoclaw](https://github.com/sipeed/picoclaw) | — | Go軽量Agent+MCP |
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | 29K | GitHub公式MCP |

### 外部情報源
| ソース | URL | 概要 |
|--------|-----|------|
| 钉钉MCP開発者Doc | [open.dingtalk.com](https://open.dingtalk.com/document/ai-dev/dingtalk-server-api-mcp-overview) | 钉钉公式MCPドキュメント |
| MCP公式Spec | [modelcontextprotocol.io](https://modelcontextprotocol.io) | プロトコル仕様 |
| TokenMix - MCP 2026 | [tokenmix.ai](https://tokenmix.ai/blog/mcp-protocol-guide-2026) | 97M DL, 10K Server分析 |
| MCP Playground | [mcpplaygroundonline.com](https://mcpplaygroundonline.com) | MCP Agent Studio |


## MCP Server実践開発ガイド（2026-04-28更新）

### 30分PDFリーダーMCP Server構築チュートリアル

Juejin開発者「HelloDong」が**30分で実用的なPDF読み取りMCP Server**を構築する手順を公開。以下の技術スタックを使用：

**使用技術**:
- `@modelcontextprotocol/sdk`: MCPプロトコルのTypeScript実装
- `pdf-parse`: PDFファイル解析ライブラリ（CJSモジュール）
- TypeScript (ESM): 型安全な開発環境

**核心ポイント**:
1. **StdioServerTransport**: MCP Serverは標準入出力で通信
2. **Tool登録**: `ListToolsRequestSchema`でAIに利用可能ツールを通知
3. **CallTool処理**: `CallToolRequestSchema`で実際のツール実行をハンドリング
4. **CJS/ESM互換**: `createRequire`でCJSモジュールをESMプロジェクトで利用

**提供ツール**:
- `read_pdf`: PDF全文抽出
- `get_pdf_info`: PDFメタデータ取得（タイトル、著者、ページ数）
- `search_in_pdf`: PDF内全文検索（大文字小文字区別オプション）

**重要注意点**:
- MCP Serverのログは**必ず`console.error`**を使用（`console.log`はstdio通信を破壊）
- ESMプロジェクトでCJSモジュールを使用する場合は`createRequire`でブリッジ
- `capabilities: { tools: {} }`でMCPクライアントに機能通知

```typescript
// 最小MCP Serverの骨格
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  { name: "mcp-pdf-reader", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

// Tool登録と処理はここで定義
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCP PDF Reader server running on stdio");
}

main().catch(console.error);
```

> **出典**: Juejin — [手把手写一个 MCP Server：从零到能用，只要 30 分钟](https://juejin.cn/post/7604881286038028340)（1いいね）[T2]
