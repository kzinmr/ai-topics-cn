---
title: "中国MCPツールエコシステム — 中国語圏向けMCP Server/SDK一覧"
type: concept
tags: [mcp, chinese-ai, tool-integration, feishu, dingtalk, wecom, wechat, open-source, server]
created: 2026-04-27
updated: 2026-05-14
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

### 7. その他の注目MCP Server

- **GitHub MCP Server**（github/github-mcp-server）: Go実装、29K Stars、Anthropic共同開発。中国開発者にも広く利用されている
- **Microsoft MCP Serverカタログ**: Azure MCP Server 2.0.0（2026-04-10）、84リリース
- **Docker MCP Toolkit**: コンテナ運用とMCPの統合を標準化
- **mcp-notify**（mcp-notify/mcp-notify）: デスクトップ通知MCP Server。Mac（terminal-notifier）、Windows（snoretoast）、Linux（notify-send）対応。MCP経由でAI Agentがユーザーに通知を送信できる。軽量バイナリ配布。Claude Code/Claude Desktop/Cursor連携実績
- **腾讯云 MCP Server マーケットプレイス**（2026年5月）: 腾讯云がMCP Serverの統一マーケットプレイスを開設。同プラットフォーム上で複数のSaaS/クラウドサービスのMCPサーバーを一元管理可能。中国クラウド事業者として初の取り組み

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
