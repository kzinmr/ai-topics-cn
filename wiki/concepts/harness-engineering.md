---
title: "Harness Engineering — LLM Agentの外化（Externalization）パターン"
created: 2026-04-18
updated: 2026-04-18
tags: [ai-agents, coding-agents, framework, llm, mcp]
aliases: ["エージェントハーネス", "LLM外化パターン", "Externalization in LLM Agents"]
source_lang: zh-CN
---

# Harness Engineering — LLM Agentの外化（Externalization）パターン

LLM Agent開発における**Harness（ハーネス）**パターン。モデル内部の能力を外部環境に「外化（Externalization）」することで、複雑なタスクを単純なタスクに変換する設計思想。

## 概要

2026年4月、arXiv論文「[Externalization in LLM Agents](https://arxiv.org/abs/2604.08224)」（54ページ）が発表された。認知科学のドナルド・ノーマン（Donald Norman）の「認知制品（Cognitive Artifacts）」理論をLLM Agentの設計に応用し、Memory・Skills・Protocols・Harnessといった各エンジニアリングトレンドを統一フレームワークで説明する。

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

## 代表的なHarness実装

| プロジェクト | 説明 | ソース |
|---|---|---|
| **Chorus** | coding agent用Harness。外部化論文の著者が開発 | [chorus-ai.dev](https://chorus-ai.dev/zh/blog/externalization-in-llm-agents/) |
| **Claude Code** | Anthropicのコーディングエージェント。ファイルシステム・シェル・gitをHarnessとして統合 | [[claude-code]] |
| **OpenClaw** | MCPプロトコルをベースとしたオープンソースAgent Harness | [[openclaw]] |

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

## 関連ページ

- [[ai-agent]] — AI智能体（Agent）全般
- [[mcp]] — Model Context Protocol（Harnessの通信基盤）
- [[agent-skills]] — エージェントのモジュール化スキル
- [[claude-code]] — Harness実装の代表例
- [[openclaw]] — オープンソースHarness実装

## 出典

- [V2EX: 啃了那篇54页的Agent Harness综述, 给大伙讲个省流版](https://www.v2ex.com/t/1206029) — fennu2333 (2026-04-15)
- [arXiv: Externalization in LLM Agents (2604.08224)](https://arxiv.org/abs/2604.08224) — Harness Engineering 論文
- [Chorus AI Blog: Externalization in LLM Agents](https://chorus-ai.dev/zh/blog/externalization-in-llm-agents/) — 詳細解説
- [36kr: 最新风口Harness，李开复、陆奇已重金入场](https://36kr.com/p/3768661067) — 中国投資動向 (2026-04-16)
