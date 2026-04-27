---
title: "Harness Engineering — LLM Agentの外化（Externalization）パターン"
created: 2026-04-18
updated: 2026-04-27
tags: [ai-agents, coding-agents, framework, llm, mcp]
aliases: ["エージェントハーネス", "LLM外化パターン", "Externalization in LLM Agents"]
source_lang: zh-CN
---

# Harness Engineering — LLM Agentの外化（Externalization）パターン

LLM Agent開発における**Harness（ハーネス）**パターン。モデル内部の能力を外部環境に「外化（Externalization）」することで、複雑なタスクを単純なタスクに変換する設計思想。

> **Humans steer. Agents execute.**（人類が舵取り。エージェントが実行。）— OpenAI Harness Engineering Blog

## 概要

2026年4月、arXiv論文「[Externalization in LLM Agents](https://arxiv.org/abs/2604.08224)」（54ページ）が発表された。認知科学のドナルド・ノーマン（Donald Norman）の「認知制品（Cognitive Artifacts）」理論をLLM Agentの設計に応用し、Memory・Skills・Protocols・Harnessといった各エンジニアリングトレンドを統一フレームワークで説明する。

同時にOpenAIが「Harness Engineering: leveraging Codex in an agent-first world」と題したブログ記事を公開。3人のエンジニアがCodexエージェントのみで、手書きコード0行・100万行超のプロダクトを5ヶ月で構築した実例を報告した。

> **TLDR: 外部ツールはモデルを強くするのではなく、難しいタスクを簡単なタスクに変える。** — [fennu2333/V2EX](https://www.v2ex.com/t/1206029)

## 認知制品理論の応用

ノーマンの洞察：外部ツールは能力を向上させるのではなく、**タスクの性質を変える**。

- **例: 買い物リスト** — 記憶力を高めるのではなく、「思い出す（recall）」タスクを「見る（recognition）」タスクに変換。認識は recall より格段に簡単。
- **LLM Agentへの応用** — Tool Use / Function Calling / MCP は、モデルに新しい能力を与えるのではなく、推論タスクを環境との相互作用タスクに変換する。

## Harnessの核心

Harness（ハーネス）はAgentの**実行フレームワーク**で、以下の責務を持つ：

1. **タスク分解** — 複雑な目標を小さなステップに分割
2. **Tool呼び出しの管理** — MCP・Function Callingなどの外部ツール呼び出しをオーケストレーション
3. **状態の外部化** — Agentの内部状態を外部環境（ファイルシステム、データベース、API）に保存
4. **エラー回復** — 失敗時のリトライ・フォールバック戦略
5. **フィードバックループ** — Tool実行結果を次の推論ステップに反映

## OpenAIによるHarness Engineering実践（2026-04）

OpenAIの内部チームは3人のエンジニアで、以下の制約の下でプロダクトを構築した：

- **0 lines of manually-written code** — アプリケーションロジック、テスト、CI設定、ドキュメント、監視、内部ツールすべてをCodexが記述
- **5ヶ月で約100万行** のコードを生成。1,500件のPRを3人のエンジニアで処理（1人あたり1日3.5PR）。チームが7人に拡大後もスループットは**増加**
- **「no manually-written code」** をコア哲学として堅持

### エンジニアの役割の再定義

人間のエンジニアはコードを書かなくなり、代わりに以下の作業に集中：

- **環境設計** — エージェントが有用な作業を行うためのスキャフォールディング構築
- **意図の仕様化** — 高レベルの目標を小さな構成要素に分解
- **フィードバックループの構築** — エージェントの出力を検証・是正する仕組み
- **エージェント間レビュー** — Codexが自身のPRをローカルでレビューし、追加のエージェントレビューを経て完了（Ralph Wiggum Loop）

### コンテキスト管理の教訓

1. **リポジトリをシステムの記録として扱う** — 巨大なインストラクションファイルではなく、構造化されたdocs/ディレクトリをソース・オブ・トゥルースに
2. **AGENTS.mdは目次として機能** — 約100行の短いファイルで、詳細は別ドキュメントを参照
3. **プログレッシブ・ディスクロージャー** — エージェントは小さい安定したエントリーポイントから始め、次を見る場所を教えられる
4. **ドキュメントのガーデニング** — 定期的に古いドキュメントをスキャンし、修正PRを自動作成

### アーキテクチャの強制

- 各ビジネスドメインを固定レイヤーに分割（Types → Config → Repo → Service → Runtime → UI）
- カスタムリンターで依存関係の方向を機械的に検証
- 「境界は中央で強制、実装はローカルで自由」— 大規模エンジニアリング組織のリーダーシップと同様

### 自動化レベルの向上

Codexは単一プロンプトで以下をエンドツーエンド実行可能に：

1. コードベースの現状検証
2. バグの再現とビデオ記録
3. 修正の実装
4. 修正の検証とビデオ記録
5. PRの作成
6. エージェント・人間の両方からのフィードバック対応
7. ビルド失敗の検出と修正
8. 判断が必要な場合のみ人間にエスカレーション
9. マージ

### エントロピーとガベージコレクション

- エージェントは既存パターン（最適でないものも含む）を複製するため、時間とともにドリフトが発生
- 「ゴールデンプリンシプル」をリポジトリに直接エンコード
- バックグラウンドのCodexタスクが定期的に変更を検出し、リファクタリングPRを自動作成
- 「技術的負債は高利貸し — 小額を継続的に返済するのが常に良い」

## 代表的なHarness実装

| プロジェクト | 説明 | ソース |
|---|---|---|
| **Chorus** | coding agent用Harness。外部化論文の著者が開発 | [chorus-ai.dev](https://chorus-ai.dev/zh/blog/externalization-in-llm-agents/) |
| **Claude Code** | Anthropicのコーディングエージェント。ファイルシステム・シェル・gitをHarnessとして統合 | [[claude-code]] |
| **OpenClaw** | MCPプロトコルをベースとしたオープンソースAgent Harness | [[openclaw]] |
| **OpenAI Codex (internal)** | 0行の手書きコードで100万行超のプロダクトを構築 | [OpenAI Blog](https://openai.com/index/harness-engineering/) |
| **MiniMax MaxClaw/MaxHermes** | OpenClaw/HermesベースのクラウドAIアシスタント。Alibaba ACK/ACSで運用 | [[minimax]] |

## Harnessと既存概念の関係

```
Harness Engineering
├── Memory（記憶の外部化） → Vector DB [[vector-db]]
├── Skills（能力のモジュール化） → Agent Skills [[agent-skills]]
├── Protocols（通信規約） → MCP [[mcp]]
└── Tool Use（関数呼び出し） → Function Calling [[function-calling]]
```

Harnessは個別の技術を**統合する実行フレームワーク**。Agent Harness論文は、これらがバラバラに見えたトレンドを「外化」という単一原理で説明する。

## 中国語圏での議論動向

- V2EXで高い関心（スコア463+）。Harnessは「造詞炒作」という批判もあるが、実装パターンとしての価値は認知されている
- 李開復（創新工場）、陸奇（奇绩創壇）がHarness関連プロジェクトに投資 reportedly
- 36kr報道によれば「小氷（Xiaoice）元チーム」がHarnessベースの「小蘭島」プロジェクトを発表予定
- **MiniMax**: MaxClaw・MaxHermesをAlibaba ACK/ACS上にデプロイし、エージェントのクラウド実行基盤を構築（2026年4月）

## CLI vs MCP vs GUI の関係

Harness Engineeringの文脈において、CLI・MCP・GUIの役割分担が明確化しつつある（詳細 → [[cli-agent-patterns]]）:

- **CLI** = エージェントの**実行層**。システム能力を構造化・パラメータ化・呼び出し可能なインターフェースとして暴露
- **MCP** = エージェントの**接入層**。ツールを統一プロトコルでシステムに接続
- **GUI** = **人間の理解・確認層**。情報量が大きいが、エージェントには不向き
- **Skills** = エージェントの**計画層**。SOP/ワークフローをタスク実行パスに組織化

## 関連ページ

- [[ai-agent]] — AI智能体（Agent）全般
- [[mcp]] — Model Context Protocol（Harnessの通信基盤）
- [[agent-skills]] — エージェントのモジュール化スキル
- [[claude-code]] — Harness実装の代表例
- [[openclaw]] — オープンソースHarness実装
- [[minimax]] — MiniMaxのHarness実装（MaxClaw/MaxHermes）
- [[cli-agent-patterns]] — CLI vs MCP vs GUI のエージェントインタラクションパターン

## 出典

- [V2EX: 啃了那篇54页的Agent Harness综述, 给大伙讲个省流版](https://www.v2ex.com/t/1206029) — fennu2333 (2026-04-15)
- [arXiv: Externalization in LLM Agents (2604.08224)](https://arxiv.org/abs/2604.08224) — Harness Engineering 論文
- [Chorus AI Blog: Externalization in LLM Agents](https://chorus-ai.dev/zh/blog/externalization-in-llm-agents/) — 詳細解説
- [36kr: 最新风口Harness，李开复、陆奇已重金入场](https://36kr.com/p/3768661067) — 中国投資動向 (2026-04-16)
- [OpenAI: Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/) — OpenAI公式ブログ (2026-04)
- [ChinAI #355: An Alliance for AI's "Harness Era" — MiniMax + Alibaba Cloud](https://substack.com/home/post/p-194618013) — Jeff Ding (2026-04-18)
- [机器之心: MiniMax + 阿里云 — AI Agent基础设施重构](https://mp.weixin.qq.com) — 深度技術解析 (2026-04)
- [叶小钗: CLI vs MCP vs GUI — AI時代のコマンドラインの復権](https://substack.com) — 開発者考察記事 (2026-04)
