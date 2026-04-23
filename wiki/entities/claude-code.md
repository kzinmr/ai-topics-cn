---
title: "Claude Code — AIコーディングエージェント"
created: 2026-04-15
updated: 2026-04-17
tags: [claude, ai-agents, coding-agents, tooling, closed-source]
aliases: ["Claude Code", "CC", "claude-code"]
source_lang: zh-CN
---

# Claude Code — AIコーディングエージェント

## 概要

Claude Codeは、[[anthropic]]が開発したターミナルベースのAIコーディングエージェントである。2026年4月15日時点の中国語圏AIディスコースにおいて**最も言及頻度の高いトピック**であり、3つの主要ソースタイプ（36kr、掘金/Juejin、V2EX）すべてにわたって合計**42件の言及**が確認された。これは単一エンティティとしては突出した数値であり、中国の開発者コミュニティにおけるClaude Codeへの関心の高さを如実に示している。

Claude Codeは従来のIDE補完型AIツール（GitHub Copilot、[[cursor]]等）とは異なり、ターミナル上でエージェント的に動作し、ファイルの読み書き・コマンド実行・Git操作などを自律的に行う。中国の開発者コミュニティでは「编程智能体」（プログラミングインテリジェントエージェント）あるいは「AI码农」（AIコーダー）として認知されている。

## 最新動向（2026年4月17日）

### Codex — OpenAIのコーディングAgentが「Codex for almost everything」に进化

2026年4月16日/V2EXで「Codex 又更新了」と报告された。OpenAIはCodexを「Codex for almost everything」として定位を変え、Mac桌面应用として「超级龙虾」（超级龙虾 = Super Lobster）と稱されるほどの大规模アップデートを実施した。

36krは「史诗级进化，OpenAI上线Mac版「超级龙虾」：Codex进化成赛博同事」（史詩級進化、OpenAIがMac版「超级龙虾」を上线：Codexがサイバー同事に進化）と报じた。その内容：

- **Mac原生应用**: 桌面上直接运行、ターミナルとの紧密統合
- **GPT-5.4 Harness全面開放**: 7つのサンドボックス环境がCodexにネイティブ統合
- **「赛博同事」**: 従来の「ツール」から「同事」（同事 = 仲間/同僚）への概念変化

Codexの进步は[[claude-code]]にとって直接的な竞合关系であり、SWE-bench Proでのスコア竞争が激化している ([[claude-opus-4-7]]参照)。

> **出典**: V2EX — [https://www.v2ex.com/t/1206478](https://www.v2ex.com/t/1206478) [T1]
> **出典**: 36kr — [https://36kr.com/p/3770202199323136](https://36kr.com/p/3770202199323136) [T1]

### 1M Context Windowの议论

Claude Codeの**100万トークンコンテキスト窓**の利用法が掘金で论议されている。掘金记事「Claude Code 的 1M Context 怎么用？」が公式资料を解读：

- **长文解析**: 大规模代码base全体のコンテキストとして活用
- ** архитектура 设计**: 数万行のコードを同時に分析して設計决策
- ** огромный ログ处理**: ビルドログ全体をコンテキストに入れたままデバッグ

この機能はCursor ([[cursor]]) 等のIDE統合型ツールとの差別化要因となっている。

> **出典**: 掘金 — [https://juejin.cn/post/7629308995309322290](https://juejin.cn/post/7629308995309322290) [T2]

### LangChain Security Patch — CVE-2026-4539

2026年4月17日、LangChain-coreが**CVE-2026-4539**紧急セキュリティパッチをリリース。掘金の技术记事が报じた内容：

- **问题根源**: `PromptTemplate.str.format_map`がユーザー入力を二次テンプレート解析に引き起こす
- **影响範囲**: LangChainを使用する全AgentがPrompt Injection（プロンプト注入）攻击にさらわれる可能性
- **「越狱」风险**: 悪意のあるプロンプトにより、Agentが本来禁止された操作を実行可能になる

この问题是AI Agentセキュリティの新たな課題であり、Claude Code用户在LangChainベースのツールチェーン中使用する 경우에는特别注意が必要。

> **出典**: 掘金 — [https://juejin.cn/post/7629308995309322290](https://juejin.cn/post/7629308995309322290) [T2]

### Routines（定时任务）の発表（2026年4月前半）

Anthropicは2026年4月にClaude Codeの新機能「**Routines**」を正式に発表した。Routinesにより、Claude Codeは以下のトリガーに基づいてタスクを自動実行できるようになった：

- **スケジュール実行**（定时触发）：cronライクな定期実行
- **APIトリガー**（API触发）：外部サービスからの呼び出し
- **GitHubトリガー**（GitHub触发）：PR作成、Issue登録などのイベント駆動

中国メディアではこの機能を「云端员工」（クラウド従業員）と表現し、Claude Codeが24時間365日稼働する自律型開発エージェントへと進化したと報じている。

> **出典**: 36kr（新智元）[T1]、掘金 [T2]

### Opus 4.7のリリース（2026-04-16）

**[[claude-opus-4-7]]が正式リリースされた**。SWE-bench Verified 87.6%（+6.8pt）、CursorBench 70%（+12pt）と大幅な性能向上を達成。画像解像度も約3倍に向上。Claude Codeのバックエンドモデルとして直ちに利用可能となった。

同時にAnthropicが導入した**強制身分認証（実名制验证）**が中国ユーザーに大きな影響を与えている。政府発行の身分証明書と手持ち自撮りが要求され、中国大陸ユーザーのアクセスが大幅に制限される事態となっている。この問題は[[kimi-moonshot]]や[[coding-plan]]への移行を加速させている。

> **出典**: V2EX — [https://www.v2ex.com/t/1206484](https://www.v2ex.com/t/1206484) [T1]
> **出典**: 36kr — [https://36kr.com/p/3768647944307458](https://36kr.com/p/3768647944307458) [T1]

### 並列処理アーキテクチャの刷新

Claude Codeが並列処理（parallelization）のために内部アーキテクチャを再構築したとの報道があり、「IDE時代の終焉をもたらす可能性がある」と評されている。

> **出典**: 掘金 — [https://juejin.cn/post/7628827972272013353](https://juejin.cn/post/7628827972272013353) [T2]

## 主要機能

### Routines（ルーティン）

前述の通り、スケジュール・API・GitHubイベントをトリガーとする自動タスク実行機能。[[ai-agent]]としてのClaude Codeの自律性を大幅に拡張する中核機能である。

### Hooks（フック）

Claude Codeのワークフローにおけるライフサイクルの各段階にカスタムロジックを注入できるディープインテグレーション機能。掘金ユーザーのGeraldChenは、4ヶ月間の実用経験を経て「Hooksが自身のワークフローを根本的に変えた」と述べている。

> **出典**: 掘金（GeraldChen）— [https://juejin.cn/post/7628854568780464162](https://juejin.cn/post/7628854568780464162) [T2]

### Skills + MCPエコシステム

Claude Codeのエコシステムが急速に成熟していることを示す象徴的な記事が掘金で大きな反響を呼んだ：

> **「别再裸用 Claude Code 了！32 个亲测Skills + 8 个 MCP」**
> （Claude Codeを素のまま使うな！実証済み32 Skills + 8 MCPサーバー）

この記事は**434いいね・1,087スター**を獲得しており、掘金におけるAI開発ツール関連記事としては異例の反響である。内容は以下の通り：

- **32個のSkills**：実際にテスト済みのClaude Code用Skillsの包括的ガイド
- **8個の[[mcp]]サーバー**：Model Context Protocolを活用した外部ツール連携

この記事の人気は、中国開発者コミュニティにおいてClaude Codeが「設定・カスタマイズして使いこなすもの」として定着しつつあることを示している。

> **出典**: 掘金 — [https://juejin.cn/post/7620060655607857178](https://juejin.cn/post/7620060655607857178) [T2]

## 中国コミュニティでの評価

### 肯定的評価

- Routines機能により「真の自律型開発エージェント」として高く評価
- Skills + MCPエコシステムの充実により、実用性が大幅に向上
- Hooksによるカスタマイズ性が上級開発者から支持

### 性能に関する論争（パフォーマンスコントロバーシー）

一方で、Claude Codeの**キャッシュ管理**に関して深刻な批判が噴出している：

> **「5分钟缓存清零，性能打1折」**
> （5分間でキャッシュがクリアされ、性能が10分の1に低下）

キャッシュ・エビクション（cache eviction）により、実質的なコストが**12倍に膨れ上がる**事態が報告され、コミュニティから強い反発が起きた。Claude Codeの開発責任者が直接コミュニティに対して回答を行う事態にまで発展している。この問題は、Claude Codeの実用コストに対する中国開発者の敏感さを浮き彫りにした。

> **出典**: 36kr — [https://36kr.com/p/3767376468607494](https://36kr.com/p/3767376468607494) [T1]

### AI依存の隠れたコスト

36krでは「**不用则废**」（使わなければ廃れる）という観点から、AIコーディングツール全般への依存がもたらす隠れたコスト（スキル劣化、ベンダーロックインなど）についても警鐘が鳴らされている。

> **出典**: 36kr [T1]

## 身分認証問題

AnthropicがClaudeプラットフォームへのアクセスに**政府発行の身分証明書**（government ID）の提出を義務化し始めたことが、中国大陸のユーザーにとって重大な懸念事項となっている。

主な問題点：

- **中国大陸ユーザーのアクセス障壁**：中国の身分証（居民身份证）が認証に使用できるか不透明
- **プライバシー懸念**：政府IDを海外企業に提出することへの抵抗感
- **地政学的リスク**：米中関係の緊張下で、中国ユーザーデータの取り扱いに対する不安

V2EXコミュニティでは活発な議論が展開されており、代替手段や回避策についての情報交換が行われている。

> **出典**: V2EX — [https://www.v2ex.com/t/1206060](https://www.v2ex.com/t/1206060) [T2]、36kr [T1]

## 競合比較

### [[kimi-moonshot]] K2.5

中国国産のAIモデルであるKimi K2.5が、Claude Codeの代替として一部の中国開発者の間で支持を集めている。主な乗り換え理由：

- 身分認証問題を回避できる
- 中国国内からのアクセスが容易
- コスト面での優位性

> **出典**: 掘金 — [https://juejin.cn/post/7611432757572141096](https://juejin.cn/post/7611432757572141096) [T2]

### [[cursor]] / IDE統合型ツール

Claude Codeの並列処理アーキテクチャ刷新により、従来のIDE統合型AIツール（Cursor等）との差別化がさらに進む見込み。「IDE時代の終焉」という評価は、ターミナルベース・エージェント型アプローチの優位性を示唆している。

### [[glm-zhipu]] GLM-5

掘金では、Claude 4.6とGLM-5の「**有毒提问**」（毒のある質問）チャレンジによる比較記事が公開されている。モデルの安全性対応やエッジケース処理における両者の違いを検証する内容だが、コーディングエージェントとしての直接比較というよりも、基盤モデルの能力比較という位置づけである。

> **出典**: 掘金 [T2]

## Subagent & Agent Teams（2026-04-18更新）

掘金（唐旺仔）の「手撕 Claude Code-5：Subagent 与 Agent Teams」により、Claude Codeのマルチエージェントアーキテクチャが詳細に分析された。

### 3つのマルチエージェントモード

| モード | 説明 |
|--------|------|
| **普通 Subagent** | 指定タイプのサブエージェントを独立して生成。`subagent_type: 'general-purpose'`など。 |
| **Fork Subagent** | 親エージェントの完全なコンテキスト（会話履歴、システムプロンプト、ツールリスト）を継承。`subagent_type`を省略すると発動。 |
| **Agent Teams** | 複数のin-processチームメンバーを並列実行。mailbox通信と権限同期により協調動作。 |

### 技術的特徴

- **Async Generator**: サブエージェントは`async function*`で実装され、`for await...of`でリアルタイム進行を監視可能
- **AsyncLocalStorage隔離**: サブエージェントごとに独立したコンテキスト（agentId、Todoリスト、ツール権限）
- **Fork Subagent**: システムプロンプトのバイト級コピーにより再構築コストを回避。`permissionMode: 'bubble'`で権限要求を親に伝播
- **Agent Teams**: `TeamCreate → in-process teammates → mailbox communication`の3段階
- **Prompt Cache最適化**: Forkサブエージェントはバイトレベルで同一のメッセージプレフィックスを持つため、キャッシュ効率が劇的に向上
- **omitClaudeMd設計**: Explore/Plan等の読取専用エージェントはCLAUDE.mdを省略。1回 spawn 毎に 5-15 Gtok 節約、3,400万+ spawn で有意な効果

### アーキテクチャ階層

```
built-in → plugin → userSettings → projectSettings → flagSettings → policySettings
```

policySettings（managedエージェント）が最も高い優先度を持ち、全てのカスタムエージェントをオーバーライド可能。

### エージェント定義の4つのソース

| ソース | 説明 | 優先度 |
|--------|------|--------|
| `built-in` | Claude Codeに組み込み | 最下位 |
| `plugin` | プラグインシステム経由 | ↑ |
| `userSettings` | ユーザーの.claude/agents/ | ↑ |
| `projectSettings` | プロジェクト固有設定 | ↑ |
| `flagSettings` | 機能フラグ制御 | ↑ |
| `policySettings` | 管理者ポリシー（最上位） | 最上位 |

### Forkサブエージェントの発動条件

`isForkSubagentEnabled()` が true を返す3つの条件（すべて必要）：
1. `feature('FORK_SUBAGENT')` コンパイル時ゲートが有効
2. `!isCoordinatorMode()` — Coordinatorモードと排他
3. `!getIsNonInteractiveSession()` — 対話セッションでのみ有効

> **出典**: 掘金（唐旺仔）— [手撕 Claude Code-5](https://juejin.cn/post/7629598396504784948) [T2]

## Opus 4.7の品質問題とデスクトップ版批判（2026-04-18更新）

### デスクトップ版「100% AIコーディング」神話の崩壊

36kr（极客邦科技InfoQ）は「**Claude Code 桌面版烂爆了，Anthropic 终于把 "100% AI 编码"演砸了**」（Claude Codeデスクトップ版が酷すぎる、Anthropicは遂に"100% AIコーディング"を演じきった）と報じた。

**主要なBug報告（Theoの1時間試用で40+）**:
- iOS版でキーボードが突然フリーズ、入力欄が頻繁に消失
- Windows版で頻繁なクラッシュとフリーズ
- チャットウィンドウの点滅、ボタン位置の不備
- Routinesがデータベースに接続できない
- 分割画面でterminalが別のウィンドウに表示される
- 音声モードで全入力欄に同時入力される
- 「ファイルを開く」が実際に開かない

**コード品質問題**:
- `print.ts`: 1つの関数が**3,167行**、486個の分岐判断、ネスト深度12層
- `QueryEngine.ts`: 46,000行
- `Tool.ts`: 30,000行近く
- `commands.ts`: 25,000行
- `main.tsx`: 単一ファイル785KB
- 感情認識に正規表現 `\b(wtf|shit|fuck|horrible|awful|terrible)\b/i` を使用

**「100% AIコーディング」の変遷**:
| 日付 | 発言者 | 主張 |
|---|---|---|
| 2025年3月 | Dario Amodei（CEO） | 「3-6ヶ月でAIが90%のコードを書く」 |
| 2025年5月 | Boris Cherny | 「全体で80-90%がClaude製」 |
| 2025年9月 | Dario Amodei | 「70%、80%、90%」（幅を持たせる） |
| 2025年10月 | Dario Amodei | 「90%達成。ただし全てではない」 |
| 2025年12月 | Boris Cherny | 「100%」 |
| 2026年2月 | Mike Krieger（CPO） | 「大多数の製品が基本的に100%」 |
| 2026年3月 | Boris Cherny | 「Claude Codeは100% Claude Code製」 |

36krの批判:
> 「AIは元々のものを拡大するだけ。元々エンジニアリング規律があればより良い成果に、元々規律がなければ技術的負債をマシンの速度で拡大する」
> 「もし'构建未来'の会社で'100% AIコーディング'が486分岐・3167行の関数を意味するなら、その未来に必要なのはより速いエンジニアリングではなく、より良いエンジニアリングだ」

> **出典**: 36kr（极客邦科技InfoQ）— [https://36kr.com/p/3770700408701447](https://36kr.com/p/3770700408701447) [T1]
> **出典**: X — [@theo](https://x.com/theo/status/2044680030706663726)

### Opus 4.7性能低下と変相値上げ

36kr（量子位）は「**Claude降智实锤了，还变相涨价，Opus跌下神坛**」（Claudeの性能低下が確定、事実上の値上げ、Opusは神壇から転落）と報じた。

**AMD高级总监Stella Laurenzoの分析**:
- 6,852セッションファイル、17,871思考ブロック、230,000+ツール呼び出しを監査
- 2026年2月から推理深度が**断崖的に低下**
- BridgeBenchスコア: Opus 4.6が83.3%→68.3%に急落
- ランキング: 2位→10位に転落

**原因と背景**:
- Anthropicはモデルのデフォルト「努力レベル」を**85点の「中等努力」モード**に設定
- 公式説明: 速度とコストのバランスのため
- 思考プロセスの表示を2月に非表示化（キャッシュ節約のためと推測）
- 提示詞キャッシュ有効時間: **1時間→5分**に短縮
- 長会話中のキャッシュ失効でトークン消費が急増

**Enterprise価格改定**:
- 月額$200固定→ $20基本料+使用量課金へ変更
- 一部チームで支出が**3倍に急増**
- 原因: モデル推理コストが前年比3倍
- OpenClaw等高消費Agentツールの呼び出し制限も開始

**競合の動き**:
- OpenAIが$100のCodexサブスクリプションを投入（Anthropicからの顧客奪取狙い）

> **出典**: 36kr（量子位）— [https://36kr.com/p/3770641574838793](https://36kr.com/p/3770641574838793) [T1]
> **出典**: VentureBeat, The Information

## 関連リンク

### 内部リンク

- [[anthropic]] — Claude Code開発元
- [[mcp]] — Model Context Protocol（Claude Codeエコシステムの基盤）
- [[ai-agent]] — AIエージェント全般
- [[glm-zhipu]] — GLM-5との比較対象
- [[kimi-moonshot]] — Kimi K2.5（中国国産代替）
- [[cursor]] — IDE統合型競合ツール
- [[openclaw]] — 新興エンドポイント型ツールチェーン
- [[ai-safety-subconscious]] — AI Agentセキュリティの文脈
- [[claude-design]] — Claude CodeとのDesign-to-Code連携
- [[claude-opus-4-7]] — バックエンド最新モデル
- [[cc-monitor]] — コミュニティ製リアルタイムToken消費モニター
- [[claude-code-router]] — モデル切り替えルーター（ccr）

### 外部ソース（中国語原文）

| ソース | URL | タイプ | ティア |
|---|---|---|---|
| 36kr（新智元）Routines報道 | 36kr.com | ニュース | T1 |
| 36kr — 缓存性能问题 | [36kr.com/p/3767376468607494](https://36kr.com/p/3767376468607494) | ニュース | T1 |
| 36kr — Opus 4.7予告 | [36kr.com/p/3767982270661126](https://36kr.com/p/3767982270661126) | ニュース | T1 |
| 36kr — Codex超级龙虾 | [36kr.com/p/3770202199323136](https://36kr.com/p/3770202199323136) | ニュース | T1 |
| 36kr — Claude Codeデスクトップ版批判 | [36kr.com/p/3770700408701447](https://36kr.com/p/3770700408701447) | ニュース | T1 |
| 36kr — Claude降智・変相値上げ | [36kr.com/p/3770641574838793](https://36kr.com/p/3770641574838793) | ニュース | T1 |
| V2EX — Codex更新 | [v2ex.com/t/1206478](https://www.v2ex.com/t/1206478) | フォーラム | T1 |
| 掘金 — 32 Skills + 8 MCP | [juejin.cn/post/7620060655607857178](https://juejin.cn/post/7620060655607857178) | 技術ブログ | T2 |
| 掘金 — Hooks解説（GeraldChen） | [juejin.cn/post/7628854568780464162](https://juejin.cn/post/7628854568780464162) | 技術ブログ | T2 |
| 掘金 — 並列処理アーキテクチャ | [juejin.cn/post/7628827972272013353](https://juejin.cn/post/7628827972272013353) | 技術ブログ | T2 |
| 掘金 — Subagent & Agent Teams | [juejin.cn/post/7629598396504784948](https://juejin.cn/post/7629598396504784948) | 技術ブログ | T2 |
| 掘金 — Kimi K2.5代替 | [juejin.cn/post/7611432757572141096](https://juejin.cn/post/7611432757572141096) | 技術ブログ | T2 |
| 掘金 — 1M Context + LangChain CVE | [juejin.cn/post/7629308995309322290](https://juejin.cn/post/7629308995309322290) | 技術ブログ | T2 |
| V2EX — 身分認証議論 | [v2ex.com/t/1206060](https://www.v2ex.com/t/1206060) | フォーラム | T2 |
|| X — @theo（デスクトップ版Bug報告） | [x.com/theo/status/2044680030706663726](https://x.com/theo/status/2044680030706663726) | SNS | T2 |

## 04-23追加動向（2026-04-23クロール分）

### Claude Code Pro — サブスクリプションモデルの転換信号

36krは**「Anthropic偷偷移除Pro用户Claude Code访问权」**と報道。AnthropicがClaude CodeをProサブスクリプションページから一時的に削除し、開発者から大きな反発を招いた。数時間後に撤回（小規模テストの2%のみ）。

**重要な示唆**:
- **Claude Code**の長時間・多ターン・プロジェクトレベル使用は、Pro固定月額コストを大幅に超える
- Anthropicは既に「サブスク枠」と「実消費量」をExtra Usageで分離
- **エンタープライズ**: セート料金 + API使用量、分離課金
- **チームプラン**: $100追加セート、高い枠を付与
- **2026年3月**: Anthropicは無料/Pro/Max/Teamの5時間制限をオフピークに2倍化
- **2026年4月**: OpenClawの第三者ツールアクセス制限も開始

> 「これはAIプログラミングツールの『無制限月額サブスク』の終焉の始まりである」
> — 分析コメント

> **出典**: 36kr — [https://36kr.com/p/3777836165223426](https://36kr.com/p/3777836165223426) [T1]

### Claude Code → Kimi K2.5 / GLM-4.7 へのモデル切替

掘金的な実証記事が大きな反響を呼んだ：**「Claude Code 换成了Kimi K2.5后，再也回不去」**（Claude CodeをKimi K2.5に切り替えた後、もう戻れなくなった）。

**設定方法**（Anthropic公式API互換エンドポイント）:
```
GLM-4.7: ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic
         ANTHROPIC_MODEL=GLM-4.7
Kimi K2.5: ANTHROPIC_BASE_URL=https://api.moonshot.cn/anthropic
           ANTHROPIC_MODEL=kimi-k2.5
```

**切り替えツール**: `claude-code-router`（ccr use kimi / ccr use glm / ccr use claude）

**主なメリット**:
- 身分認証（KYC）不要
- 安定性向上（アカウント停止・タイムアウトが解消）
- パフォーマンス: Kimi K2.5はOpenRouterとOpenClawのベンチで**No.1**
- コスト: Claude Proより低コスト

**切り替え後のワークフロー変化**:
- 従来: Cursor 60% + Claude Code 40% → 切り替え後: Claude Code + 国産モデルに統一

> **出典**: 掘金 — [https://juejin.cn/post/7611432757572141096](https://juejin.cn/post/7611432757572141096) [T2]

### Skills + MCPエコシステムの進化 — 32 Skills + 8 MCP完全ガイド

掘金的な包括的ガイドがClaude Codeエコシステムの成熟を象徴している：

**Skillsのインストール**: `npx skills add <repo> -y -g`（-gでグローバル）

**主要Skillsカテゴリ**:
- **フロントエンド**: frontend-design, web-artifacts-builder, vercel-react-best-practices
- **ドキュメント**: technical-writer, docx/pptx/xlsx/pdf
- **アーキテクチャ**: planning-with-files, requesting-code-review, architecture-patterns
- **メモリ**: memory-intake, memory-audit
- **デバッグ**: systematic-debugging

**主要MCPサーバー**:
- Neural Memory（長期的構造化メモリ）
- Filesystem（ローカルファイルアクセス）
- Playwright（ブラウザ自動化/E2Eテスト）
- Figma（デザイン仕様の統合）

**注意点**:
- 20個以上のSkillsを同時にインストールしない（コンテキスト負荷増加）
- Skillsインストール後は必ずClaude Codeを再起動
- Filesystem MCPへのアクセスはルートディレクトリには許可しない

> **出典**: 掘金 — [https://juejin.cn/post/7620060655607857178](https://juejin.cn/post/7620060655607857178) [T2]
