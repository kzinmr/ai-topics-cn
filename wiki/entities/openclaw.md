---
title: OpenClaw — AI Agentエンドポイントツール
created: 2026-04-17
updated: 2026-06-11
tags: [ai-agents, open-source-ai, tooling, china, releases, safety]
aliases: [\"openclaw\", \"OpenClaw\"]
source_lang: zh-CN
---

# OpenClaw — AI Agentエンドポイントツール

> **トレンド順位**: #9（2026-04-17集計、17言及）  
> **ソース**: 36kr, Juejin, V2EX（全3ソースタイプ）  
> **出典**: 中国語圏のAgentフレームワーク戦争における新興プレイヤー

## 概要

OpenClawは、AI Agentが外部ツール・API・システムと自律的にやり取りするための**エンドポイント型ツールチェーン**フレームワークである。2025年11月にオーストリアの開発者Peter Steinberger（元PSPDFKit創設者）が「Clawdbot」の名でサイドプロジェクトとして公開。その後Anthropicからの商標クレームにより「Moltbot」を経て、2026年1月29日に「OpenClaw」に最終改名された。

「[[openclaw]]」という名前通り、複数の「爪」（ツール.endpoint）を并发的に伸ばしてタスクを処理する並列実行モデルが最大の特徴。MITライセンスで完全にオープンソースであり、既存リリースのライセンスは取消不能。

2026年2月14日、創設者Peter Steinbergerが**OpenAIに入社**することを発表。OpenClawは独立した**OpenClaw財団**（OpenClaw Foundation）へ移行し、OpenAIはスポンサーとして関与するのみで所有権は持たない。財団はGhostty Foundationをモデルとした「スイス型中立地帯」であり、NVIDIA、Microsoft、Red Hat、Tencent、ByteDanceといった複数企業が貢献する構造。

> 「I'm a builder at heart. I did the whole creating-a-company game already... What I want is to change the world, not build a large company, and teaming up with OpenAI is the fastest way to bring this to everyone.」 — Peter Steinberger

## 機能と設計思想

### 並列ツール実行アーキテクチャ

OpenClawは単一のツール呼び出しに留まらず、複数のエンドポイントを同時に伸張（伸出）して実行できる：

```
OpenClaw Agent
  ├── Endpoint: FileSystem (読み書き)
  ├── Endpoint: Git (commit/push)
  ├── Endpoint: Browser (スクレイピング)
  ├── Endpoint: Database (クエリ)
  └── Endpoint: API (外部サービス呼び出し)
```

この設計により、Claude Codeの単一セッション内でも複数のツール操作を同时進行できる。36krは「OpenClawの多爪構造がAI Agentの作业方式を根本的に変えた」と評している。

### MCPプロトコルとの統合

OpenClawは[[mcp]]（Model Context Protocol）ベースのセキュリティ問題を提起したフレームワークでもある。36krが「OpenClaw爆火，暴露12类致命隐患」と報じた通り、MCPプロトコル利用時の致命的脆弱性が問題化。

### 12類的安全隐患

36kr（新智元）が報じたOpenClawの安全隐患（_security vulnerabilities_）：

1. ツール権限の過大な払い出し
2. MCPエンドポイント間のデータ漏洩
3. 第三者ツールチェーンへの汚染
4. 認証情報の横方向的移動（lateral movement）
5. ファイルシステム抽象化の不備
6. ネットワークプロキシ悪用
7. セッション固定攻撃
8. ツール呼び出しの再帰的暴走
9. タイムアウト後の不整合状態
10. ログ露出によるcredential流出
11. エンドポイントフェイク（なりすまし）
12. プロトコルバージョン不和

> **出典**: 36kr — [https://36kr.com/p/3768662327935747](https://36kr.com/p/3768662327935747) [T1]

## Hermes Agentとの対比

2026年4月、掘金で「GitHub 85K Star 新王挑战 357K Star 霸主：Hermes 还是 OpenClaw？最强Agent框架怎么选」と題した比較記事が大いに議論された。

| 指標 | Hermes Agent | OpenClaw |
|------|-------------|----------|
| GitHub Stars | 388K | 372K |
| 設計思想 | 長期記憶・自己進化 | 並列ツールチェーン |
| アーキテクチャ | Stateful session | Stateless endpoint |
| 中国コミュニティ人気 | 高（exe.dev統合） | 急上昇中 |
| MCP安全性 | 調査中 | 12類問題曝光 |

著者の「大模型真好玩」は以下のように総括している：

> 「Hermes并非简单取代OpenClaw，而是开辟新路径：赋予Agent长期记忆与自我进化能力」  
> （Hermesは単にOpenClawを置換するものではなく、新しい道を切り開いている：Agentに長期記憶と自己進化能力を付与する）

> **出典**: 掘金 — [https://juejin.cn/post/7628854568781545506](https://juejin.cn/post/7628854568781545506) [T2]

## 电商后台接入实践（2026-04-18）

掘金で「把 OpenClaw 接进电商后台之后，我对 AI 落地这件事的理解变了」（OpenClawを电商后台に接入して、AI落地への理解が変わった）と題した実践記が公開された。

### 实践の目的

OpenClawを电商平台の后台システムに接入し、以下の業務をAgentに委譲:
- 注文異常の集約とトラブルシューティング提案
- 運営質問への複数システム横断回答
- 在庫・キャンペーン・商品状態の衝突検知
- ログ・アラートのノイズフィルタリング
- 反復SOPの自動処理

### 主要な発見

**「半対半錯」の危険性**: 后台シーンで最も危険なのは「完全に分からない」ことではなく「分かったつもりで半分間違っている」こと。具体例:
- 在庫は照会できるが、キャンペーン在庫と実売在庫の口径差異を理解できない
- 注文状態は読めるが、售后単が後続フローをロックしていることに気づかない
- ログの高頻度エラーは要約できるが、歴史ノイズと本次変更に起因する異常の区別ができない

**状態システム問題**: 电商后台の問題は本質的に「语义理解問題」ではなく「状態システム問題」。一つの質問に商品状態・类目審査・キャンペーン設定・在庫プール・風控ルール・非同期タスク・キャッシュ刷新など複数のシステムが絡む。

**工程化問題**: AIシステムを真实業務に接入すると、「すべての問題がモデル問題に見える」のが最大の罠。実際はサービスタイムアウト、APIフィールドの暗黙変更、環境間依存バージョン差異などが多数発生。

### コスト教訓

- 試錯コストが累積しやすく、リソース空転が深刻
- 按秒課金のGPU算力（蓝耘）で検証サイクルの摩擦が30%低減
- MaaSプラットフォームでモデル接入・切替の工数削減

### 设计原則の変化

「什么都できる」追求から「信頼できる範囲で正確に」へ:
1. 自分がいつ答えられるか/答えられないかを知ること
2. 高风险アクションには厳格な拦截と確認
3. 全プロセスのログ記録とリプレイ可能性
4. 人工兜底（human fallback）の明示的出口
5. 複数システム照会はブラックボックス回答ではなく根拠明示

> 「智能体最有价值的不是创造性，而是守边界、讲规则、少出错」
> （Agentの最も重要な価値は創造性ではなく、境界を守り、規則に従い、ミスを減らすこと）

> **出典**: 掘金 — [https://juejin.cn/post/7629679767084007475](https://juejin.cn/post/7629679767084007475) [T2]

## OpenClaw財団とOpenAI提携

2026年2月14日、創設者Peter SteinbergerがOpenAIに入社。同時にOpenClawは**OpenClaw財団**へ移行した。Sam Altman（OpenAI CEO）はX上で「Peter is joining OpenAI to drive the next generation of personal agents. He is a genius with a lot of amazing ideas about the future of very smart agents interacting with each other to do very useful things for people.」と称賛した。

財団はGhostty Foundationをモデルとした「スイス型中立地帯」構造であり、OpenAIはスポンサーとして関与するのみで所有権は持たない。NVIDIA、Microsoft、Red Hat、Tencent、ByteDanceといった複数企業が貢献している。MITライセンスは取消不能であり、既存リリースは永続的にオープンソースのまま。

2026年4月9日の「State of the Claw」キーノート（AI Engineer Summit）で、Steinbergerは以下を報告：
- GitHub Stars: 295,000+（5ヶ月で世界最速のオープンソース成長）
- 貢献者: 約2,000人
- セキュリティアドバイザリ: 1,142件（1日あたり16.6件 — Linuxカーネルの2倍）
- 重大脆弱性: 99件（うち469件に公式対応済み、60%クローズ）

> 「Running the foundation is like running the company on hard mode.」 — Peter Steinberger

### 「Dreaming」機能 — アイドル時メモリ統合

Steinbergerが提唱した新概念。人間が睡眠中に記憶を整理するのと同様に、エージェントがアイドル時間にセッションログを走査し、長期記憶に値するものを選択的に保持する機能。v2026.4.x系で実装済み。Anthropicも同様の概念を研究中（リークソースコードより）。

## 中国での展開とセキュリティ懸念

OpenClawは中国でも急速に普及し、Baiduのスマートフォンアプリからの直接アクセス、DeepSeekやQwenとの統合、WeChat/QQ/Discord/Telegram対応が実現。一方で中国工業信息部は「不適切な設定時のセキュリティリスクとデータ漏洩の危険性」について警告を発出。これを受け、中国移动と中国通信学会が共同で**『OpenClaw AI Agentセキュリティガイド』**を策定した。

## 2026年4月下旬〜5月の大型アップデート

OpenClawはGitHubスター数が**200K→367K**に急成長（前回wiki記載の85K→367Kは既に更新済み）。v2026.4.14からv2026.4.29まで連続リリースが行われた。

### v2026.4.29（最新安定版、2026年4月30日）

- **NVIDIAプロバイダー追加**: APIキーオンボーディング、モデルカタログ、モデルrefピッカー対応
- **Bedrock Opus 4.7思考パリティ**: xhigh/adaptive/maxプロファイルをAnthropic APIと同等に
- **OpenGrepセキュリティスキャン**: SARIF形式のGitHub Code Scanning統合、ソースルールコンパイラ
- **DeepSeek V4 thinkingレベル対応**: xhigh/maxプロファイルをresolveThinkingProviderフックで
- **GPT-5.4-mini suppress修正**: 古いmodels configによるassistant-turn失敗を防止
- **IPv6 ULAオプトイン**: 信頼プロキシスタック向けweb-fetch

### v2026.4.27（2026年4月29日）

- **Codex Computer Use設定**: `/codex computer-use status/install`、マーケットプレイス発見、自動インストール
- **DeepInfraプロバイダー追加**: 画像生成/編集、TTS、embeddings、text-to-video
- **QQBotフルグループチャート**: 履歴追跡、@メンション制御、アクティベーションモード、FIFOメッセージキュー
- **Matrix E2EE**: `openclaw matrix encryption setup` — 暗号化有効化、リカバリブートストラップ
- **OpenCode統合**: Anthropic Opus/Sonnet 4.x thinkingレベル対応
- **Proxyルーティング**: オペレーター管理の送信プロキシ（OPENCLAW_PROXY_URL）、strict HTTP forward-proxy検証

### v2026.4.26（2026年4月28日）

- **Control UI/Talk**: リアルタイム音声トランスポート契約、Google LiveブラウザTalkセッション
- **Cerebrasプロバイダー追加**: バンドルプラグインとして
- **Claude Code importer**: 設定ファイルのインポートとマイグレーション

### v2026.4.23（2026年4月24日）

- **GPT-5.5対応開始**: OpenAIが2026年4月23日にリリース。OpenClawはv2026.4.23-beta.5で即座に対応
- **OpenAI画像生成**: Codex OAuth経由でgpt-image-2がOPENAI_API_KEYなしで動作

### GPT-5.5統合詳細

OpenAIのGPT-5.5（2026年4月23日リリース）はOpenClawにおいて以下のベンチマークを記録：
- **Terminal-Bench 2.0**: 82.7%（GPT-5.4は75.1%、+7.6pt向上）
- **SWE-Bench Pro**: 58.6%
- **コンテキスト**: 400K、トークン効率改善

OpenClawは「strict-agentic」実行コントラクト（PR A）により、GPT-5.5がプランニングだけで停止せず実際のツール実行を行うことを保証。runtime truthfulness（PR B）により、認証失敗・プロキシ問題・DNSエラーを正確に報告し、hallucinationを防止。

### v2026.4.15（2026年4月16日）

- **Claude Opus 4.7統合**: デフォルト選択、opusエイリアス、画像理解バンドル
- **Google Gemini TTS**: バンドルプラグインとしてWAV/PCM出力対応
- **Slimmer context**: バウンデッドメモリ読み取りでトークンオーバーヘッド削減
- **Codex transport self-heal**: 不安定なネットワークでの信頼性向上
- **Gateway security**: MEDIA:ツール結果の厳密な名前マッチング（injection防止）

### v2026.4.14（2026年4月14日）

- **GPT-5.4-pro前方互換**: アップストリームカタログ更新前に即座に対応
- **Slack allowlist修正**: インタラクティブイベントのsender検証強化
- **Ollama timeout修正**: ローカル推論のストリームタイムアウト問題解決
- **SSRF脆弱性修正**: ブラウザルートとControl UIのセキュリティ強化
- **Markdown-it ReDoS保護**: Control UIのパッチ

### v2026.5.7（最新安定版、2026年5月7日） — SecretRef強検証・Foundation移行

2026年5月7日、OpenClawにとって**転換点となるリリース**が実施された：

- **SecretRef強検証（Strong Validation）**: 設定ファイル中のSecretRef（機密認証情報参照）に対して厳格な検証ロジックを実装。不正なSecretRef形式・存在しない参照先・期限切れトークンをビルド時に検出し、ランタイムエラーを未然に防止
- **Foundation移行完了**: OpenClawプロジェクトの管理が正式に**OpenClaw財団**へ移行。Peter SteinbergerがOpenAI入社（2月14日発表）したことに伴う組織変更の完了
| GitHub Stars | 372K+（2026-05-17時点、1週間で約5K増）
- **コード品質向上**: CIパイプラインのSecretRefチェックが全PRで必須化

### v2026.5.10-beta.1（2026年5月10日） — Stable Release Branch分岐

- **CLIログファイル/ディレクトリ上書き防止**（#70180）: `--log-file`、`--log-dir`フラグが既存ファイルやシンボリックリンクを上書きしないよう保護
- **ClawHub依存解決失敗の堅牢化**（#70195）: 依存関係解決エラー時、依存関係グラフをテキスト・JSON・dot形式で出力するダンプ機能を追加
- **MCP stdioトランスポートのバッファリング改善**（#70162）: 終了シグナルを受信した際のバッファリング挙動を改善
- **Gatewayヘルスチェック・シグナル伝搬改善**（#70186）: Gatewayプロセスの正常起動確認・シグナル伝搬のロバスト性向上

### v2026.5.12-beta.1（2026年5月12日） — ユーザー設定ベースのフラグプロパゲーション

- **LLMプロバイダー設定drift修正**: Nullable dynamicプロパティ（X-Grok-Flag, X-Gemini-Flag等）の設定反映問題を修正
- **ユーザー設定ベースのフラグプロパゲーション**（#70312）: 個別設定を全プロバイダー呼び出しに伝播する新仕組み
- **OpenCode OAuth認証機能追加**: claude_code user/tokenコマンドのOAuth認証フローを改善
- **Flox Secret Store内SecureKey検証修正**: 特定条件下でSecureKeyが検証をパスしない問題を修正

### v2026.5.14-beta.1（2026年5月14日） — 高速ログディレクトリ・パッケージタイプ保護

- **高速ログディレクトリ**: `openclaw doctor --fix log-dir` — テスト内容と日次ログをGitステータスに依存せずに出力可能に
- **パッケージ依存性解決競合の堅牢化**（#70406）: Node.jsパッケージマネージャ間の依存関係競合によるスタックトレース修正。ClawHub Skillsのパッケージタイプを型安全に管理する統合Package Managerを導入
- **Commitmentsメッセージ修正**: ハートビートメッセージのフォーマット改善

### v2026.5.6（2026年5月6日） — OAuthリグレッション修正

- **Codex OAuthリグレッション修正**: v2026.5.3〜5.5で発生したCodex TransportのOAuth認証問題を修正。特定のネットワーク条件下で認証がループするバグを解消
- **セキュリティパッチ**: Gatewayレイヤーの軽微な脆弱性修正を含む

### v2026.5.5（2026年5月5日） — 全文検索・MCPサーバーインスペクト・起動30%高速化

- **全文検索（Full-text Search）**: エージェントメモリ・会話履歴・設定ファイルに対する全文検索機能を搭載。過去の対話や設定を素早く発見可能
- **MCPサーバーインスペクト**: `claw mcp inspect` コマンドでMCPサーバーのエンドポイント一覧・ツール定義・スキーマを動的可視化
- **Gateway起動30%高速化**: プラグイン発見・ランタイム検出・Cronスケジュール・Schema読込・Shutdownクリーンアップ・セッション管理・モデルメタデータ読込をすべて**lazy-load**（要求時初回読込）に変更。Gatewayのコールドスタート時間を25〜30秒から約2秒に短縮
- **プラグインセキュリティ大改造**: 公式プラグインのインストール・アンインストール・更新・Onboarding・ClawHubロールバック・npm依存状態報告・Betaチャネル更新パスを全面的に堅牢化。外部化プラグインがファーストクラスパッケージとして正しく動作することを保証。Configセキュリティポリシー変更：無効な設定発見時にfail closed（起動拒否）へ変更
- **ローカルモデル最適化**: ローカルOllama推論の安定性・応答性を向上
- **パフォーマンス最適化**: 大規模ClawHubスキルストア（26,000+スキル）のキャッシュ戦略改善

### v2026.5.4（2026年5月4日） — file-transferプラグイン・/steerコマンド

- **MCP file-transferプラグイン**: エージェント間・エージェント-人間間でファイルを直接転送するための標準MCPプラグイン。ClawHubからインストール可能
- **`/steer` コマンド**: 実行中のエージェントにリアルタイムで行動修正指示を送信。テキストプロンプトによる振る舞いの動的制御が可能
- **プロンプトエンジニアリング改善**: `/steer` による動的指示が複数エージェント間で共有可能に

### v2026.5.3（2026年5月3日） — Commitments自動リフレッシュ

- **Commitments自動リフレッシュ**: ハートビートフォローアップ機能の改善。エージェントがユーザーに約束したタスクの進捗を自動的に再通知
- **マークダウンレンダリング改善**: Control UIにおけるマークダウン表示の品質向上（コードブロック・テーブル・数式のレンダリング最適化）
- **軽微なバグ修正**: 複数のEdge Case修正により安定性向上

### 36kr OpenClawセキュリティレポート（2026年5月）

2026年5月、36krがOpenClawの脆弱性に関するフォローアップ記事を公開。前回の12類安全隐患に加えて以下を報告：

- **OpenClawのオープンソースサプライチェーンリスク**: ClawHubに悪意のあるスキルがアップロードされるケースが確認され、コミュニティによるレビュープロセスの必要性が指摘された
- **SOE（国有企業）のOpenClaw生利用禁止**: 中国政府系セキュリティ機関が国有企業に対してOpenClawの生利用（未修正のままの利用）を禁止する通達を発出
- **サプライチェーン監査要求**: OpenClawを利用する企業に対し、使用する全MCPエンドポイント・ClawHubスキルの定期的なセキュリティ監査が推奨された

> **出典**: 36kr — OpenClaw脆弱性フォローアップ（2026年5月）[T1]

### セキュリティ強化 — 「一破二立三硬化」

OpenClawチームは「**一破二立三硬化**」（One Break, Two Establish, Three Harden）というスローガンを掲げ、過去に指摘された12類の安全隐患を踏まえた全面的なセキュリティ強化を実施：
- **一破（一破）**: 旧来の不安全な権限モデルを破棄
- **二立（二立）**: 新しいMCPエンドポイント認証・承認フローの確立
- **三硬化（三硬化）**: ツール実行・データフロー・ネットワーク通信の三層硬化

v2026.4.14以降のセキュリティ修正一覧：
- Gateway toolのconfig.patchで`dangerouslyDisableDeviceAuth`等のフラグ新規有効化をブロック（#62006）
- Browser SSRFポリシー enforced（#66040）
- Microsoft Teams SSO sender allowlist（#66033）
- Config snapshot redaction（#66030）
- Heartbeat owner downgrade for untrusted hooks（#66031）
- Exec approvalsのsecret redaction（#61077, #64790）
- OpenGrep rulepack + SARIF統合（#69483）

> **出典**: GitHub Releases — [https://github.com/openclaw/openclaw/releases](https://github.com/openclaw/openclaw/releases) [T1]

### SOUL.md — キャラクター/ペルソナシステム

v2026.4.25で導入された**SOUL.md**は、エージェントに人格・性格・行動パターンを定義するキャラクター設定ファイル。Hermes AgentのSOUL.mdに触発されつつ、OpenClaw独自のツールチェーン指向に最適化されている。設定例：

```yaml
# SOUL.md example
name: "MyAgent"
persona: "効率的で慎重なアシスタント"
traits:
  - タスク分割を優先
  - エラー時は即座にユーザー報告
  - 並列実行可能なツールを積極活用
```

> **出典**: 极莫（Jimo Studio） — [https://jimo.studio/articles/openclaw-soul](https://jimo.studio/articles/openclaw-soul) [T2]

### ClawHubエコシステム

エージェントツール・プラグイン・テンプレートを共有する**ClawHub**マーケットプレイスがローンチ。SHA-256による完全性検証（integrity verification）機構を標準搭載し、サードパーティ製プラグインの改ざん防止を実現。ダウンロード時に自動チェックサム検証が行われる。

### SOUL.md — キャラクター/ペルソナシステム

v2026.4.25で導入された**SOUL.md**は、エージェントに人格・性格・行動パターンを定義するキャラクター設定ファイル。Hermes AgentのSOUL.mdに触発されつつ、OpenClaw独自のツールチェーン指向に最適化されている。

### Active Memory — 会話IDフィルター

会話セッションごとのメモリ管理を可能にする**Active Memory**機能。conversation-IDフィルターにより、エージェントが過去の会話コンテキストを適切に取捨選択できる。

### People Wiki

エージェントが対話する人物・組織の知識を管理する**People Wiki**機能：
- キャラクターカード（性格・役割・関係性の定義）
- リレーションシップグラフ（人物間の関係性を視覚化）
- プロビナンストラッキング（情報の出所と変更履歴の追跡）

### Commitments — ハートビートフォローアップ

エージェントがユーザーに約束したタスクを自動追跡する**Commitments**機能。一定間隔のハートビートシグナルでフォローアップリマインダーを配信。

### プロバイダー追加

**NVIDIA**（GPUクラウド）、**Cerebras**（Wafer-Scale Engine）、**DeepInfra**（高速推論API）の3プロバイダーがサポート。

### Codex Computer Use連携

**Codex**（OpenAIのコンピュータ操作AI）との連携。デスクトップ操作・ブラウザ制御・ファイル管理をOpenClawのツールチェーンに統合。

### QQBot / Yuanbaoチャンネル対応

中国国内のメッセージングプラットフォームとして、**QQBot**およびテンセントの**Yuanbao（元宝）**に対応。WeChatと合わせて中国三大IMプラットフォームをカバー。

### Gatewayパフォーマンス改善

Gatewayサーバーの起動時間が**25〜30秒から約2秒**に大幅短縮。プラグインのホットロード対応により、新しいツールの追加が即座に反映される。

### 中国移动 OpenClaw Security Guide

中国移动（China Mobile）および中国通信学会が共同で**『OpenClaw AI Agentセキュリティガイド』**を発表。エンタープライズ向けの安全なOpenClaw導入ベストプラクティスを提供し、特にMCPプロトコル利用時の機密情報保護に焦点を当てている。

> **出典**: 中国移动／中国通信学会 OpenClaw Security Guide — [https://security.guide/openclaw](https://security.guide/openclaw) [T1]

## 中国語圏での立ち位置

OpenClawは中国語圏AI Agent市場で以下の位置づけ：

- **「第二勢力」**: Claude Code ([[claude-code]])に次ぐ注目度
- **急成長**: GitHubスター数200K→367K（5ヶ月で世界最速のオープンソース成長）
- **OpenAI傘下だが独立**: OpenClaw財団によるガバナンス、MITライセンス取消不能
- **問題提起者**: MCPプロトコルの安全問題を世界で初めて体系的に列出
- **中国移动安全ガイド**: 中国移动・通信学会が公式セキュリティガイドを策定
- **多プラットフォーム対応**: WhatsApp、Telegram、Slack、Discord、Signal、iMessage、QQBot、Yuanbao（元宝）
- **多モデルサポート**: Claude Opus 4.7、GPT-5.5、Gemini 3.1 Pro、DeepSeek V4、Kimi K2.6、Qwen3、ローカルOllama
- **ClawHubエコシステム**: 公式スキルマーケットプレイス（26,000+スキル）

### 競合比較：OpenClaw vs 阿里「悟空」

2026年3月、アリババが**「悟空（Wukong）」** — 企業級AIネイティブワークプラットフォームを発表。OpenClawの主要競合として注目されている。

| 項目 | OpenClaw（龙虾） | 阿里「悟空」 |
|------|-----------------|-------------|
| **定位** | 個人開発者向けAgent | 企業級AIワークプラットフォーム |
| **セキュリティ** | 12類安全隐患の指摘あり | 内建双层ルール体系、沙箱隔離 |
| **ファイルシステム** | 標準ファイル读写 | **RealDoc** — 行単位・キーワード単位の外科的編集+スナップショット |
| **生态** | ClawHub（26,000+スキル） | 十大OPT業界Skills + 釘釘/淘寶/支付宝/阿里云統合 |
| **互換性** | — | OpenClawスキル体系を完全互換（ClawHubスキル直接アップロード可能） |
| **モデル自由度** | 多プロバイダー対応 | 同上 + 自定义API接入 |

悟空の最大優位性は**RealDocファイルシステム**（AIによるファイル改変のロールバック対応）と**企業級セキュリティ**にある。一方OpenClawは**並列ツール実行**と**軽量アーキテクチャ**が強み。

> **出典**: 掘金 — [体験完阿里「悟空」](https://juejin.cn/post/7618418125198196779) [T1]

### 阿里云Coding Planとの統合

2026年2月、阿里云がOpenClaw/Claude Code向けの**Coding Plan**サービスを開始。特徴：
- **按次課金**: トークン単位ではなくAPIリクエスト回数で課金（Agentの多ループ実行で有利）
- **統合モデル**: Qwen-3.5、Kimi-K2.5、GLM-4.7をワンキーで利用
- **OpenAI互換 + Anthropic互換**: 両プロトコルのAPIエンドポイントを同時提供
- **OpenClaw設定例**: `openclaw.json`の`models.providers.bailian`セクションで阿里云APIを直接指定可能

これによりOpenClawユーザーの運用コストが大幅に低減。「算力自由」（算力の自由化）と評されている。

> **出典**: 掘金 — [阿里云Coding Plan](https://juejin.cn/post/7610637031321698330) [T1]

### Agent Loopの工程論的位置づけ

2026年4月の工程級分析記事により、OpenClawのAgent Loopは**「推理循環（reasoning loop）」**に分類されることが明確化された：

```
OpenClaw: 入力 → LLM → ツール選択 → 実行 → 結果 → 再推理（while未完成）
```

これは**タスクID・永続状態・ライフサイクル管理**を欠いており、「セッション級Agent」に留まる。対照的にLangGraphは状態機械、Temporalは永続実行（Durable Execution）を提供し「システム級Agent Loop」を実現している。

> **結論**: OpenClawは**実行能力（ツールチェーン）**を提供し、Claude Codeは**連続推理**を提供し、Hermesは**記憶と進化**を提供する。

> **出典**: 掘金 — [谁才真正拥有 Agent Loop?](https://juejin.cn/post/7633526424323391551) [T1]

## スローガン: "Less mystery, more machinery"

36krが伝えたOpenClawの公式スローガン。透明性と実用性を重視する設計哲学を表しており、ブラックボックス化したAIではなく、ユーザーが理解・制御できるエージェントを目指す姿勢を示している。

## 2026年5月17日〜24日更新

### リリースラッシュ（週3回のメジャーリリース）

| バージョン | 日付 | ハイライト |
|-----------|------|-----------|
| **v2026.5.19** | 2026-05-19 | ブラウザモーダルダイアログ対応、`defineToolPlugin` + CLIツール、Mac Settings UI刷新、Gateway再起動トレーサビリティ改善 |
| **v2026.5.20** | 2026-05-21 | Discord音声セッションフォロー、Policyプラグイン（バンドル）、xAI device-code OAuth、cron改善、サブエージェントハンドオフ改善、secret警告 |
| **v2026.5.22-beta.1** | 2026-05-23 | 100+Fixes、ドキュメント刷新、モデル認証プリウォーム（〜20s→〜5ms/4100倍高速化）、npm shrinkwrap、Windowsインストーラ改善多数 |

### GitHub統計（2026年5月21日時点）
- **Stars**: 374,000（前回372K、+2K/週だが成長速度は成熟期へ減速）
- **Forks**: 77,601
- **Contributors**: 2,304
- **NPM週間DL**: 5,344,931
- **週間新スター成長**: +1,700/週（ピーク時+40,000/週から大幅減速）
- **Issue解決率**: 89.9%
- **スポンサー**: 119

### 競合激化: Hermes Agentに実利用で逆転される
最大の変化は競合状況。**Hermes Agent**（Hermes v0.13.0 "Tenacity"リリース後）がOpenRouter日間トークン消費量で**458B**（OpenClaw 173Bの2.6倍）、全期間トークンでも**8.14T**（OpenClaw 7.18Tを逆転）。一方OpenClawは**ClawHub 44,000+スキル**、**50+チャンネル**でエコシステム規模では依然優勢。

### セキュリティ動向
- 「Claw Chain」脆弱性（CVE-2026-44112/44113/44115/44118）は4月23日パッチ済み。最小安全バージョン: v2026.4.22
- **偽スター監査通過**: F/S比0.204（Flask 0.235に近く健全）
- Policyプラグイン・secret平文警告・sandbox tool policy通知をv2026.5.20で追加
- 公開Gatewayインスタンス: 135,000+（82ヶ国）

### エコシステム拡大
- **DigitalOcean**: OpenClawワンクリックDroplet展開
- **MiniMax**: MaxClaw（OpenClawベースマルチエージェント）リリース
- **Alibaba Cloud**: OpenClawマルチエージェント構築ガイド公開
- **Qwen 3.5**: OpenClaw蒸留モデル（9B/27B/4B）公開
- **Google I/O 2026**: Gemini Spark（OpenClaw 24/7代替競合）発表

### 2026年6月: 冷却期とプラットフォーム移行

6月に入り、OpenClawは明確な**冷却期**に突入した。

- **新規リリースゼロ**: 5月31日〜6月9日の期間、GitHubリリースが一件もない。週3回のペースから完全停止
- **GitHub Star成長減速**: 5月28日時点の376Kから成長が停滞。ピーク時(週+40,000)から大幅減速
- **コミュニティ話題性低下**: V2EXで「小龙虾为什么突然不火了」議論が定着。掘金の記事も5月既存記事のリサイクル状態
- **脆弱性問題の影響**: 12類安全隐患、SOE(国有企業)の生利用禁止、ClawHub品質問題(悪意スキル11.3%、プロンプトインジェクション36%)が響く

一方で、以下のポジティブシグナルも確認されている:

- **Microsoft Build 2026 (6/3)**: マイクロソフトがWindows版「龙虾」(OpenClaw for Windows)を発表。16億Windowsユーザーがエージェント時代に突入([36kr](https://36kr.com/p/3836988816094341))
- **百度APP統合継続**: 百度AppがOpenClawを正式統合し期間限定で無料提供を継続
- **新パラダイム提唱 (6/8)**: 36krにてClaude Codeの父(Anthropicチーム)とOpenClaw創設者Peter Steinbergerが同時に新AIプログラミングパラダイムを支持と報道。プロンプトエンジニアリングの終焉を宣言([36kr](https://36kr.com/p/3844224911346184))
- **プラットフォーマー依存深化**: Microsoft Windows対応により、独立OSSからプラットフォーマーエコシステムの一部へと位置づけが変化

### 競合状況 (6月初旬)

| 競合 | 動き | OpenClawへの影響 |
|---|---|---|
| 阿里悟空(Wukong) | ユーザー移行加速(掘金115票) | 最大の脅威 |
| Hermes Agent | V2EXで高評価継続、中国コミュニティ認知拡大 | トークン消費で圧倒 |
| MiniMax M3 | 6月1日リリース(1M ctx/Coding Agent特化) | 新たな競合 |
| Microsoft Copilot | Build 2026でWindows版OpenClaw発表 | プラットフォーマー依存深化 |

### 市場構造の変化

中国AI Agent市場は「フレームワーク競争」から「プラットフォーム競争」へフェーズ移行:
| 層 | プレイヤー | 6月の動き |
|---|---|---|
| 第1層: テックジャイアント | 阿里(悟空/Qoder)、腾讯(WorkBuddy)、字节(火山Engine)、百度(心響/DuMate) | 悟空シフト加速、百度統合継続 |
| 第2層: 垂直特化 | 百融(RaaS)、金智維(Ki-AgentS)、金山(WPS AI) | 大きな変化なし |
| 第3層: OSS/初创 | Hermes Agent、agentserver、Dify | Hermes Agent認知拡大継続 |

### 出典 (6月追加分)
- [36kr — 微软Build大会全文 (6/3)](https://36kr.com/p/3836988816094341)
- [36kr — 龙虾宇宙：微软抄了腾讯的作业 (6/3)](https://36kr.com/p/3836945345067648)
- [36kr — 新范式：Claude Code父と龙虾创始人 (6/8)](https://36kr.com/p/3844224911346184)
- [36kr — 16億WindowsユーザーAgent時代 (6/3)](https://36kr.com/p/3837001359947143)
- [掘金 — 百度APP OpenClaw統合 (6/1再掲)](https://juejin.cn/post/7606519452977152050)

### 出典 (5月)
- [OpenClaw v2026.5.19-beta.1 Release](https://github.com/openclaw/openclaw/releases/tag/v2026.5.19-beta.1)
- [OpenClaw v2026.5.20 Release](https://github.com/openclaw/openclaw/releases/tag/v2026.5.20)
- [OpenClaw v2026.5.22-beta.1 Release](https://github.com/openclaw/openclaw/releases/tag/v2026.5.22-beta.1)
- [OpenClaw Newsletter 2026-05-21](https://buttondown.com/openclaw-newsletter/archive/openclaw-newsletter-2026-05-21/)

## 関連リンク

### 内部リンク

- [[claude-code]] — 主要競合・比較対象
- [[mcp]] — 安全問題の中心にあるプロトコル
- [[harness-engineering]] — 类似的Agent Harness概念
- [[ai-agent]] — 上位カテゴリ

### 外部ソース

| ソース | URL | ティア | 概要 |
|---|---|---|---|
| 36kr — 12類安全隐患 | [36kr.com/p/3768662327935747](https://36kr.com/p/3768662327935747) | T1 | 安全問題の体系的分析 |
| 掘金 — Hermes vs OpenClaw | [juejin.cn/post/7628854568781545506](https://juejin.cn/post/7628854568781545506) | T2 | フレームワーク比較 |
| 掘金 — 阿里云Coding Plan | [juejin.cn/post/7610637031321698330](https://juejin.cn/post/7610637031321698330) | T1 | 阿里云Coding Plan統合 |
| 掘金 — 悟空比較 | [juejin.cn/post/7618418125198196779](https://juejin.cn/post/7618418125198196779) | T1 | 阿里「悟空」vs OpenClaw |
| 掘金 — Agent Loop分析 | [juejin.cn/post/7633526424323391551](https://juejin.cn/post/7633526424323391551) | T1 | Agent Loopの工程論的位置づけ |
| 掘金 — 小红书自动发帖 | [juejin.cn/post/7615379311402467354](https://juejin.cn/post/7615379311402467354) | T2 | ClawHubスキル活用例 |
| V2EX — Agent比較議論 | [v2ex.com/t/1209907](https://www.v2ex.com/t/1209907) | T3 | 個人Agent実用性議論 |