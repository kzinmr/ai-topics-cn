---
title: "Dify — オープンソースLLMOpsプラットフォーム"
created: 2026-04-19
updated: 2026-05-09
tags: [llmops, open-source, agent-platform, rag, workflow, china]
aliases: ["Dify", "Dify.ai", "Dify平台", "开源LLMOps"]
source_lang: zh-CN
---

# Dify — オープンソースLLMOpsプラットフォーム

> **重要度**: 🔥🔥 MEDIUM — 中国発OSS Agent/RAGプラットフォームの代表格
> **関連概念**: [[china-ai-agent-ecosystem]], [[rag]], [[mcp]], [[agent-skills]], [[coze]]
> **関連エンティティ**: [[qwen]], [[deepseek]], [[openclaw]]

## 概要

**Dify**は中国発の**オープンソースLLMアプリケーション開発プラットフォーム**。GitHubスター数138,000超（2026年4月）、フォーク3,000以上。扣子（Coze）の「ローコード」志向に対し、Difyは**「開発者向け宣言的アプローチ」**を掲げ、YAML/JSONによるAgent定義・API-first設計・CI/CD統合を特徴とする。

## 2026年主要アップデート（v1.3以降）

2025年末〜2026年初頭にかけ、Difyは1.0版本から重大なアーキテクチャアップグレードを経験。以下の5つが最も重要：

### 1. 原生MCP Protocolサポート（最重要）
AnthropicのModel Context Protocol（MCP）をネイティブサポート。600+外部ツール生态（Notion、Slack、GitHub、Stripe、Brave Search、ローカルファイル系统等）を**零コードで接続**可能。

### 2. 推論型RAG（Agentic RAG）
Dify v1.2以降、検索プロセスをLLM Agentが駆動する**推理型检索**に対応：
- **Query Decomposition**: 複雑なクエリを自動的に分解
- **Re-ranking**: 検索結果の再 ranking
- **Self-Correction**: 誤った結果に対する自己修正
- **Multi-round Retrieval**: 複数回の検索ラウンドで精度向上
- Dify核心貢献者によると「90%のユーザーが'检索'ノードのみ使用。'推理检索'ノードを使うのは10%以下だが、能力は基础版的10倍」

### 3. 新ワークフロー実行エンジン
- **並列ノード実行**: 独立ノードの並列実行で複雑ワークフローの処理時間を大幅短縮
- **条件分岐強化**: 正規表現マッチ・JSONパスクエリを含む複雑ロジック式
- **ループノード**: リストの各要素に対する反復処理
- **エラー処理**: 誤り捕獲・リトライロジックで堅牢性向上

### 4. 多智能体協業（Nested Agent）
Dify v1.3以降、**嵌套Agentノード**をサポート。一つのAgentが別のAgentをツールとして呼び出せる。例：「研究員」「プログラマー」「審査員」の専門Agentをパイプラインのように協業。

- **長期記憶**: 複数会話間でコンテキスト情報を維持
- **ツール呼び出し最適化**: 出力形式問題による実行失敗を削減
- **Chain-of-Thought可視化**: リアルタイムで推論過程を表示

### 5. LlamaFactory微調整集成
LlamaFactory（GitHub 73K star）をネイティブ統合：
- LlamaFactory微調整 → GGUFエクスポート → Difyカスタムモデル登録
- 3Bパラメータモデルの専門分野微調整は、特定タスクでGPT-4o-miniを上回る精度
- 推理コストを$0.15/千token → $0.003/千tokenに（50倍削減）

### 6. Dify v1.14 GA：Agent Skills & Sandbox Runtime（2026年5月）

2026年5月初旬、**v1.14.0 GA**（General Availability）が正式リリース。Agent Runtimeを完全再設計：
- **Sandboxed Runtime**: 隔離実行環境でセキュリティ向上
- **Skill Editor**: 再利用可能なSOPブロックをGUIで構築
- **@メンション**: ワークフロー内でインラインツール呼び出し（例 `@send_email`）
- **動的変数アセンブリ**: 会話履歴・外部データからの動的コンテキスト構築
- **コラボレーションBeta**: チーム共有ワークスペース

### 7. v1.13.x：Human-in-the-Loop
2026年3月のv1.13.0で**Human Inputノード**を追加。ワークフロー実行を一時停止し、人間の承認・編集・ルーティング判断を挟む「Human-in-the-Loop」が可能に。v1.13.3で安定性向上。

### 8. v1.9.2：双方向MCP対応
v1.9.2（2025年7月頃）で、MCPサポートを双方向に拡張：外部MCP Serverをツールとして呼び出すだけでなく、Dify上のAgent/WorkflowをそのままMCP Serverとして公開可能に。Claude、Cursor等のMCPクライアントから直接呼び出せる。

### 9. Creator Center & Template Marketplace
2026年3月、**Creator Center**と**Template Marketplace**をローンチ。コミュニティ作成のワークフローテンプレートを公開・共有・ワンクリック導入。PartnerStack連携でテンプレート経由のサブスクリプション収益分配も可能。

## 資金調達

2026年3月、**Dify（LangGenius）は3,000万ドルのPre-Series A資金調達**を発表。リード投資家は**紅杉（HSG）**。GL Ventures、Alt-Alpha Capital、五源資本（5Y Capital）、瑞穗力合投資、NYX Venturesが参加。累計調達額は4,150万ドル。企業評価額は約1.8億ドル。

Globalで140万台以上のデバイス、2,000+チーム、280社のエンタープライズに採用（マースク、Anker等）。ARRは約300万ドル。

### 日本展開

LangGeniusは2025年2月に日本法人（株式会社LangGenius、東京・日本橋）を設立。2026年4月より、教育・介護分野の京進グループと協業開始。Difyを活用した教育AI・介護現場のDX推進を目的とする。

## 核心機能

### 1. アプリケーション構築
- **Chat App**: 会話型AI（カスタムプロンプト + 知識庫）
- **Workflow App**: 条件分岐・ループ・並列実行を含むビジネスロジック
- **Agent App**: ツール呼び出し・自己修正・複数モデル協調

### 2. RAGパイプライン
DifyのRAGは業界最高水準の柔軟性：
- **ドキュメント処理**: PDF/Word/Excel/Webスクレイピング → テキスト抽出 → 分割 → エンベディング
- **検索戦略**: ハイブリッド検索（BM25 + ベクトル）、再ランキング（Cross-Encoder）、クエリ拡張
- **エンベディングモデル**: OpenAI/BGE（智源）/m3e（阿里）など複数選択可能

### 3. モデル管理
- **マルチプロバイダ**: OpenAI, Anthropic, Google, 智谱, 百度, 阿里, MiniMax, 月之暗面
- **ローカルモデル**: Ollama/vLLM/SGLang統合、GGUF/GPTQ/AWQ対応
- **フォールバック**: プライマリモデル失敗時にセカンダリへ自動切替

### 4. 観測・評価
- **ログ**: 全リクエスト/レスポンスの追跡（ユーザーID・セッションID・モデル・トークン数）
- **評価**: ヒューマン評価（1〜5点）+ 自動評価（回答精度・応答時間・トークンコスト）
- **分析**: ダッシュボードで利用傾向・コスト推移・モデル性能比較

## 開発者向けエコシステム

### Plugin Architecture
Dify Pluginは**Python製ツール**をAgentに追加可能。2026年4月時点でコミュニティPlugin数1,200超：
- **データソース**: MySQL/PostgreSQL/Redis/MongoDB
- **API連携**: WeChat Work/Feishu/DingTalk/Trello/Jira
- **AIツール**: 画像生成(Stable Diffusion)/音声合成(TTS)/動画生成

### API-first Design
```yaml
# Dify Agent定義例
app:
  name: "カスタマーサポートAgent"
  mode: "chat"
  model:
    provider: "qwen"
    name: "qwen2.5-72b"
  prompt_template: |
    あなたは企業のカスタマーサポートAgentです。
    知識庫の情報を参照し、丁寧に回答してください。
  tools:
    - type: "knowledge_retrieval"
      name: "FAQデータベース"
    - type: "api_call"
      name: "注文照会API"
      url: "https://api.example.com/orders"
  workflow:
    - step: "ユーザー入力"
    - step: "知識庫検索"
      condition: "score > 0.7"
    - step: "LLM回答生成"
```

## 企業導入事例

| 企業 | 規模 | 用途 |
|------|------|------|
| **途牛 (Tuniu)** | 旅行プラットフォーム | 顧客サポートAgent（Dify + Qwen） |
| **跨境电商A社** | 年商50億円 | 商品情報抽出Agent（Dify RAG + GPT-4） |
| **金融B社** | 地方銀行 | リスクレポート自動生成（Dify Workflow + GLM） |
| **京進グループ** | 教育・介護 | 教育AI・介護DX（2026年4月〜） |

## 扣子 (Coze) との比較

| 次元 | Dify | 扣子 (Coze) |
|------|------|-------------|
| **ライセンス** | オープンソース (Apache 2.0) | クローズド（ByteDance proprietary） |
| **対象ユーザー** | 開発者・エンジニア | ノンテクニカル・ビジネス |
| **構築方法** | YAML/API/コード | ドラッグ&ドロップ |
| **カスタマイズ性** | 非常に高い | 制限あり |
| **モデル選択肢** | 自由（ローカル含む） | プラットフォーム提供のみ |
| **デプロイ** | セルフホスト/クラウド | クラウドのみ |
| **コスト** | 無料（インフラ費のみ） | 無料枠→有料プラン |

## 課題

1. **学習曲線**: YAML/API設定は技術者向け。ノンテクニカルユーザーには敷居が高い
2. **ドキュメント**: 中国語ドキュメントは充実しているが、日本語・英語版は遅れ気味
3. **サポート**: コミュニティベース。エンタープライズSLAは提供中だが、中国国内中心

## 関連リンク

### 内部リンク
- [[china-ai-agent-ecosystem]] — 中国Agentプラットフォーム全景
- [[rag]] — 検索拡張生成
- [[mcp]] — Model Context Protocol
- [[coze]] — 扣子プラットフォーム
- [[agent-skills]] — Agentスキル定義

### 外部ソース
| ソース | URL | ティア | 概要 |
|--------|-----|--------|------|
| Dify公式サイト | [dify.ai](https://dify.ai) | T1 | プラットフォーム本体 |
| GitHub | [github.com/langgenius/dify](https://github.com/langgenius/dify) | T1 | OSSリポジトリ |
| 掘金 — Dify RAG活用 | [juejin.cn](https://juejin.cn) | T2 | ハンズオン記事 |
| IT之家 — 企业级AI智能体解析 | [ithome.com](https://www.ithome.com) | T2 | 業界分析 |
