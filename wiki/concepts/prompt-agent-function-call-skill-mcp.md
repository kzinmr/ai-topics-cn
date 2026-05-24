---
title: "Prompt・Agent・Function Call・Skill・MCP — 用語整理"
created: 2026-04-21
updated: 2026-04-21
tags: [concept, terminology, prompt, function-calling, skill, mcp, ai-agents]
aliases: ["Prompt", "Agent", "Function Call", "Skill", "MCP", "用語整理", "傻傻分不清楚"]
source_lang: zh-CN
source: juejin
url: "https://juejin.cn/post/7614205951297732654"
---

# Prompt・Agent・Function Call・Skill・MCP — 用語整理

> **トレンド順位**: HIGH（2026-04-19/21 Juejin、113いいね→118に増加）
> **ソース**: Juejin
> **作者**: 苏三说技术
> **スコア**: 👍118 ⭐234（04-21時点）
> **関連**: [[mcp]], [[agent-skills]], [[function-calling]]

## 概要

AIエンジニアが混乱しやすい5つの概念——**Prompt**、**Agent**、**Function Call**、**Skill**、**MCP**——を整理した記事。高評価（118いいね・234收藏）を受けた入門的解説。

## 用語解説

### 1. Prompt（プロンプト）

> 「LLMへの入力指示文」

LLMとの対話窓口。タスク指示、制約条件、出力形式などを記述する。

```python
# Prompt例
prompt = """あなたは経験豊富なPythonエンジニアです。
以下の要件を満たす関数を書いてください：
- 入力: 数値リスト
- 出力: 平均値
- 型ヒントを含む"""
```

### 2. Function Calling（関数呼び出し）

> 「LLMが外部APIやツールを実行するメカニズム」

LLMに 함수 호출能力を追加し、外部システムとの連携を可能にする。

```python
# Function Calling設定例
functions = [
    {
        "name": "get_weather",
        "description": "都市の天気を取得",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            }
        }
    }
]
```

### 3. Agent（智能体）

> 「目標達成 위해自律的に行動するLLM応用」

Function Calling基础上，加入推理循环、记忆、工具选择等能力。

```
Agent = LLM + Function Calling + 推論ループ + 記憶 + ツール選択
```

### 4. Skill（技能）

> 「再利用可能ちな特定のタスク実行能力」

Anthropic Claude Codeで導入された概念で、一連的工具とプロンプトをパックagedして再利用やすくしたもの。

例：frontend-design skill（AIの審美能力向上）、code review skill（コードレビュー専用）

### 5. MCP（Model Context Protocol）

> 「AI助手と外部ツールの標準化接続プロトコル」

Anthropicが推出的AI工具接続標準規格。サーバー/クライアントアーキテクチャで、多ツール、多リソース対応。

## 相互関係

```
Prompt ─────┐
            ├──► Function Calling ──► 外部API実行
LLM ────────┤
            │
            └──► Agent（自律的推論ループ）
                    │
                    ├──► Skill（再利用可能な技能パッケジ）
                    │
                    └──► MCP（ツール接続の標準プロトコル）
```

## まとめ表

| 用語 | 役割 | 抽象レベル |
|------|------|-----------|
| Prompt | LLMへの指示 | 最低 |
| Function Calling | 外部連携の接口 | 低 |
| Agent | 自律的行動体 | 中 |
| Skill | 再利用可能な技能 | 中 |
| MCP | ツール接続標準 | 高 |

## 主要信息来源

- [Prompt、Agent、Function Call、Skill、MCP，傻傻分不清楚？](https://juejin.cn/post/7614205951297732654)