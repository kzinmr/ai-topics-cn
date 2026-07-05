---
title: "Dify — オープンソースLLMOpsプラットフォーム"
created: 2026-04-19
updated: 2026-07-05
tags: [llmops, open-source, agent-platform, rag, workflow, china, enterprise, security]
search_hints:
  - "Dify セキュリティ脆弱性 Imperva 2026"
  - "Dify v1.14.2 CVE-2026-41947"
  - "Dify みずほ 導入 全社展開 2026"
  - "Dify Enterprise 日本代理店 賽博威"
  - "Dify エージェントサーバー v1.15"
  - "Dify Docker pulls 10M"
  - "Dify Agent Server init"
  - "Dify Graphon 0.4.0"
  - "Dify Pyrefly 移行"
  - "Dify EdgeOne DeepResearch"
aliases: ["Dify", "Dify.ai", "Dify平台", "开源LLMOps"]
source_lang: zh-CN
---

# Dify — オープンソースLLMOpsプラットフォーム

> **重要度**: 🔥🔥 MEDIUM — 中国発OSS Agent/RAGプラットフォームの代表格
> **関連概念**: [[china-ai-agent-ecosystem]], [[rag]], [[mcp]], [[agent-skills]], [[coze]]
> **関連エンティティ**: [[qwen]], [[deepseek]], [[openclaw]]

## 概要

**Dify**は中国発の**オープンソースLLMアプリケーション開発プラットフォーム**。GitHubスター数147,000超（2026年7月）、Docker pulls 10M+、フォーク23,000以上。扣子（Coze）の「ローコード」志向に対し、Difyは**「開発者向け宣言的アプローチ」**を掲げ、YAML/JSONによるAgent定義・API-first設計・CI/CD統合を特徴とする。

## 2026年主要アップデート（v1.3以降）

2025年末〜2026年初頭にかけ、Difyは1.0版本から重大なアーキテクチャアップグレードを経験。以下のアップデートが最も重要：

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

### 6. Dify v1.14.0：協同編集 & HITL Service API（2026年4月29日）

**v1.14.0** はDify史上最大規模のアップデートの1つ。数百のコミットを含むメジャーリリース：

**新機能:**
- **リアルタイム協同編集（Collaboration）**: チームメンバーが同一ワークフローを同時編集可能。Difyが真のチーム生産性ツールに進化。
- **Human-in-the-Loop（HITL）Service API**: プログラマティックにHITLフローを制御可能に。外部システムから人工介入プロセスを駆動する統一インターフェース。
- **Quota v3**: 計測システムの全面刷新。Meterコンポーネント、ファイルアップロードのクォータ認識、障害回復機能を強化。

**アーキテクチャ変更:**
- **Graphon独立**: dify_graph パッケージがスタンドアロン **Graphon 0.2.2** に分離
- **OpenAPI v2**: 自動生成スクリプト公開
- **SQLAlchemy 2.0 select()移行**: データベースアクセス層を最新化
- **Pydantic BaseModel移行**: コンソール・サービスレスポンスをPydantic v2化
- **UIコンポーネント移行**: レガシーUIから `@langgenius/dify-ui` 共有コンポーネントライブラリへ大規模移行
- **Langfuse連携**: オプションでTTFT（Time-to-First-Token）メトリクスをLangfuseに報告可能

**GitHub Stars**: 142K+（v1.14.0リリース時）

### 7. Dify v1.14.2：セキュリティパッチ & エージェント基盤 & ワークフロー信頼性（2026年5月19日）

v1.14.0の約3週間後、v1.14.1の1週間後にリリースされた緊急パッチ。セキュリティ問題（CVE-2026-41947対応含む）とワークフロー安定性に集中。

**セキュリティ修正（CVE-2026-41947対応）:**
- **テナント分離強化**: app trace-configエンドポイントおよびFilePreviewテキスト抽出にテナントスコープを適用（GHSA-48xc-wmw8-3jr3, GHSA-2qwc-c2cc-2xwv）
- **ツール認証情報の保護**: デフォルト組み込みツール認証情報の更新をworkspace admin/ownerに制限
- **リセット時の認証情報クリーンアップ**: `reset-encrypt-key-pair`実行時に古いテナントツール認証情報を削除

**CVE-2026-41947（2026年5月18日公開）:**
- **深刻度**: HIGH（CVSS 7.4）/ CRITICAL（CVSS 9.1、機関により評価分岐）
- **内容**: Dify v1.14.1以前のトレース設定エンドポイントに認証バイパス脆弱性。認証済みエディターユーザーがテナント所有権チェックを迂回し、他テナントのアプリケーションのトレース設定を変更可能。被害アプリのメッセージを攻撃者管理のLLMトレースプロバイダにリダイレクト可能。
- **修正**: v1.14.2でテナント所有権検証を追加

**ワークフロー信頼性向上:**
- HITLワークフロー再開後のトレーシング復旧
- ワークフロー実行コールバック追跡の改善
- メッセージ更新のデータベースラウンドトリップ削減
- Flaskコンテキスト外でのメモリフェッチ修正
- base64ファイルルックアップセッションの適切なクローズ

**RAG/ナレッジ修正:**
- LLMノードが取得済み知識ファイルにアクセス可能に
- API更新後のドキュメントサマリー再生成
- パイプラインテンプレートレンダリング修正
- RAGパイプラインでの認証情報取得失敗のグレースフルハンドリング

**エージェント基盤（v1.15の布石）:**
- `feat(agent): init agent server` — 専用Agent Serverの初期実装をマージ（#36087）。Dify v1.15以降のAgent-nativeアーキテクチャの基盤。

**デプロイ改善:**
- plugin-daemon 0.6.1にアップグレード
- GraphEngine最小ワーカー数のデフォルト値増加
- 静的解析をPyrightからPyreflyに移行
- Graphon 0.4.0にアップグレード

**GitHub Stars**: 143K+（v1.14.2リリース時、2週間で+1K）

### 8. Dify v1.14.1：セキュリティ強化 & 安定性修正（2026年5月12日）

v1.14.0の2週間後にリリースされた重要なパッチ。セキュリティ・ワークフロー・ナレッジベースの安定性向上に焦点。

**セキュリティ強化:**
- **LiteLLMアップグレード**: CVE-2026-42208を含む複数の依存関係を更新（urllib3, gunicorn, gitpython, mako, Google SDK, OpenTelemetry他）
- **SECRET_KEY自動生成**: セルフホスト環境でSECRET_KEYが空の場合、ランタイムキーを自動生成・永続化（公開デフォルト値への依存を排除）
- **エンドポイント保護**: `/threads`・`/db-pool-stat` エンドポイントを認証必須化
- **IDOR修正**: `GET /account/avatar` の権限昇格脆弱性を修正
- **テナント分離**: 組み込みツールのデフォルト資格情報クリーニングを現在のテナントに限定

**ワークフロー修正（v1.14.0リグレッション）:**
- バックエンドAPI経由のワークフローバージョン読み込みを復旧
- 大規模アプリリストのオンラインユーザーポーリング問題を修正
- プレビューResizeObserverの無限ループを修正
- 変数参照セレクターがサブ変数を選択できない問題を修正
- 問題分類子に編集可能なカテゴリラベルを追加
- HITLフローが選択された操作値を外部に公開

**ナレッジベース修正:**
- 画像レンダリング失敗を修正
- 空ドキュメントのベクトル埋め込みスキップ処理
- RAG重複除去にdoc_idを使用（精度向上）

**デプロイ改善:**
- Docker環境変数を `docker/envs/**` にカテゴリ分割
- WebSocketサービスをメインサービスから分離（デプロイの柔軟性向上）
- SQLALCHEMY_POOL_RESET_ON_RETURN設定追加
- Exploreアプリのカテゴリ設定・カスタムソート対応

### 9. v1.13.x：Human-in-the-Loop
2026年3月のv1.13.0で**Human Inputノード**を追加。ワークフロー実行を一時停止し、人間の承認・編集・ルーティング判断を挟む「Human-in-the-Loop」が可能に。v1.13.3で安定性向上。

### 10. v1.9.2：双方向MCP対応
v1.9.2（2025年7月頃）で、MCPサポートを双方向に拡張：外部MCP Serverをツールとして呼び出すだけでなく、Dify上のAgent/WorkflowをそのままMCP Serverとして公開可能に。Claude、Cursor等のMCPクライアントから直接呼び出せる。

### 11. Creator Center & Template Marketplace
2026年3月、**Creator Center**と**Template Marketplace**をローンチ。コミュニティ作成のワークフローテンプレートを公開・共有・ワンクリック導入。PartnerStack連携でテンプレート経由のサブスクリプション収益分配も可能。

## 資金調達

2026年3月、**Dify（LangGenius）は3,000万ドルのPre-Series A資金調達**を発表。リード投資家は**紅杉（HSG）**。GL Ventures、Alt-Alpha Capital、五源資本（5Y Capital）、瑞穗力合投資、NYX Venturesが参加。累計調達額は4,150万ドル。企業評価額は約1.8億ドル。

Globalで140万台以上のデバイス、10M+ Docker pulls、2,000+チーム、280社のエンタープライズに採用（マースク、Anker等）。ARRは約300万ドル。

### セキュリティ脆弱性の開示（2026年5月18日）

Imperva Threat ResearchがDifyに2件の重大脆弱性を発見・公開：

**1. ファイルアップロード経由のアカウント乗っ取り（CVE未割り当て）**
- **影響**: Dify v1.13.0以前の全バージョン
- **手法**: 攻撃者がバーナーアカウントで悪意のあるSVGファイルをアップロード → サブドメイン（upload.dify.ai → cloud.dify.ai）を書き換えたリンクを管理者に送信 → クリックでXSS発動 → アカウント完全乗っ取り
- **根本原因**: Difyの全ファイルが認証なし・予測可能なURLパターンで公開。uploadサブドメインがcloud.dify.aiのDNSエイリアスだったため、サブドメイン書き換えだけで認証バイパス可能
- **修正**: 2026年3月17日、v1.13.1でContent-Typeをapplication/octet-streamに強制（全ファイルダウンロード化）
- **開示経緯**: 2026年1月14日にImpervaが報告 → Difyは無回答・サイレントパッチ → 2026年5月18日にImpervaが公開

**2. サンドボックステナント分離バイパス**
- **影響**: Dify v1.13.2以前
- **内容**: Difyサンドボックスが全テナントで同一の固定UIDでPythonコードを実行。全テナントのコードが共有の/tmpに書き出される。ファイルは脆弱なVigenere暗号（64バイト繰り返し鍵）で「暗号化」されていたが、実質的に解読可能
- **修正**: v1.13.3（2026年3月25日）でdify-sandbox 0.2.14にバンドル。実行ごとに一意のUIDを割り当て、ファイルパーミッションも0600に制限
## セキュリティ教訓

AIプラットフォームが機能追加を急ぐあまり、セキュリティ設計が追いついていない構造的問題を示す。特にセルフホスト環境では修正後も長期間パッチ未適用のインスタンスが残存するリスクあり。

## コミュニティ活用事例（2026年5月）

### Dify × EdgeOne DeepResearch再現（2026年5月25日）

掘金（juejin）コミュニティにて、**Dify × EdgeOne**（Tencent Cloud CDN/Edge Computing）を組み合わせてOpenAI DeepResearchを零コードで再現するハンズオン記事が公開された：

- Difyのワークフロー機能 + EdgeOne Functions（エッジ関数）でWebスクレイピング・情報集約を実装
- 外部APIを一切書かず、Difyの標準ツールのみでDeepResearch相当の複数ソース調査パイプラインを構築
- Difyが「アプリケーションテンプレート」としても活用され始めたことを示す事例
- Link: [juejin.cn/post/7642996161259159558](https://juejin.cn/post/7642996161259159558)

|> **注**: 2026年6月25日、Dify v1.15.0がリリース（確認済み: GitHub release）。UI刷新・オンボーディング改善・高速ナビゲーション等のUX向上が中心。詳細は下記v1.15.0セクションを参照。
|
|### 9. Dify v1.15.0：UX/UI全面刷新 & ナビゲーション高速化（2026年6月25日）
|
|v1.14.2（5月19日）の約5週間後、**v1.15.0**がリリースされた。セキュリティパッチや新機能追加ではなく、**ユーザー体験の大幅な改善**に焦点を当てたメジャーリリース。
|
|**主な改善点:**
|- **ランディング/オンボーディング再設計**: 初回利用体験を簡素化（#37433, #37844, #37800）
|- **高速ナビゲーション**: 「go to anything」パレット改善、検索入力の自動フォーカス（#32130, #37175）
|- **安全な削除**: アプリ削除前にワンクリック確認ダイアログを追加（#37263）
|- **クリーンなワークフローエディタ**: 折りたたみ可能なパネルで編集領域を最大化（#37276）
|- **通知改善**: 長いエラーメッセージを完全表示する一貫性のあるトースト通知（#37382, #37581）
|- **アクセシビリティ強化**: プラグイン権限ヒント、スキップナビゲーションリンク、キーボードフォーカスポリッシュ（#37319, #37879）
|- **より良い検索結果**: 検索結果の関連性ランキング改善とカテゴリフィルター
|
|**デプロイ・アーキテクチャ:**
|- SDK自動更新機能の追加
|- MCP/A2Aプロトコル対応の安定性向上（コミュニティプラグインの互換性改善）
|- 静的解析ツールチェーンのPyreflyベースへの完全移行（v1.14.2の布石を完成）
|
|**GitHub Stars**: 147K+（v1.15.0リリース時、5週間で+4K）
|
|**出典**: [GitHub Release v1.15.0](https://github.com/langgenius/dify/releases/tag/1.15.0)

LangGeniusは2025年2月に日本法人（株式会社LangGenius、東京・日本橋）を設立。2026年4月より、教育・介護分野の京進グループと協業開始。Difyを活用した教育AI・介護現場のDX推進を目的とする。

**みずほフィナンシャルグループ導入（2026年5月、最重要）:**
2026年5月上旬、**みずほFG**が金融機関として初めて「Dify Enterprise」を全社展開開始。金融機関基準の厳格なガバナンスを備えたAI開発基盤を構築：
- 非エンジニアでもAIエージェントを開発可能な環境を提供
- 部門ごとのアクセス権限制御、SSO、利用ログ取得による統制管理基盤
- 先行実証（法人営業領域）では平均41.8%の業務時間短縮（60分→35分）
- 若手層では平均52.2%の時間短縮（62分→29分）を達成
- 産業調査部：アナリスト業務のAI支援ワークフローを検証中
- 人材・組織開発部：AIキャリアナビゲーションを構築中
- 参考: みずほ銀行は2026年9月より対話型AIアシスタント「あおまるバンク」提供開始予定（OpenAI技術活用）
- **出典**: [産経ニュース](https://www.sankei.com/pressrelease/prtimes/S67PWWYWSNJLPGVYGHI3OTCE5Q/)、[PR TIMES](https://prtimes.jp/main/html/rd/p/000000003.000177612.html)

**Dify Enterprise日本代理店:**
2026年5月、**賽博威（Cyberway）** がDify Enterprise版の初の公式認定販売パートナーに。大消費業界向け「AIアプリケーションファクトリー」ソリューションを提供。

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
| **みずほFG** | メガバンク | 全社AI開発基盤「Dify Enterprise」（2026年5月〜、41.8%業務時間削減） |
| **賽博威（Cyberway）** | ITソリューション | Dify Enterprise公式販売パートナー（大消費業界向け） |

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
| v1.14.2 Release | [GitHub Releases](https://github.com/langgenius/dify/releases/tag/1.14.2) | T1 | 最新パッチノート |
| CVE-2026-41947 | [Feedly](https://feedly.com/cve/CVE-2026-41947) | T1 | 脆弱性詳細 |
| Imperva開示記事 | [Cybernews](https://cybernews.com/security/dify-critical-vulnerabilities-disclosed/) | T1 | セキュリティ開示 |
| Imperva技術詳細 | [Security Boulevard](https://securityboulevard.com/2026/05/dify-when-your-ai-platform-becomes-the-attack-surface/) | T1 | Imperva詳細分析 |
| みずほFG導入PR | [産経ニュース](https://www.sankei.com/pressrelease/prtimes/S67PWWYWSNJLPGVYGHI3OTCE5Q/) | T1 | エンタープライズ導入事例 |
| 賽博威パートナー発表 | [163.com](https://www.163.com/dy/article/KSAR9JC80517K28J.html) | T1 | 公式販売パートナー |
| 掘金 — Dify RAG活用 | [juejin.cn](https://juejin.cn) | T2 | ハンズオン記事 |
| IT之家 — 企业级AI智能体解析 | [ithome.com](https://www.ithome.com) | T2 | 業界分析 |
