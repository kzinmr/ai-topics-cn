---
title: "Function Calling（関数呼び出し）— LLMと外部APIを接続する核心メカニズム"
created: 2026-04-17
updated: 2026-04-17
tags: [concept, technique, llm, ai-agents, tooling, function-calling]
aliases: ["Function Calling", "函数调用", "工具调用", "Tool Calling"]
source_lang: zh-CN
---

# Function Calling（関数呼び出し）— LLMと外部APIを接続する核心メカニズム

## 概要

Function Calling（函数调用/工具调用）は、大規模言語モデルが自然言語の生成に加え、構造化された関数名とパラメータを出力することで外部APIやツールを呼び出す仕組み。[[ai-agent|AI Agent]]と[[mcp|MCP]]の基盤技術であり、「対話から行動へ（从对话到动作）」のパラダイムシフトを実現する。

> **トレンド順位**: NEW（2026-04-17集計、4言及）
> **ソース**: juejin, v2ex

## 技術原理

### 基本フロー
1. **関数定義の注入** — 利用可能な関数のスキーマ（名前、パラメータ、説明）をシステムプロンプトに渡す
2. **LLMの判断** — ユーザーの質問に対し、自然言語で回答するか関数呼び出しを生成するかをモデルが判断
3. **構造化出力** — `{"function": "get_weather", "arguments": {"city": "上海"}}` 形式のJSON
4. **実行と返却** — アプリケーション側で関数を実行し、結果をLLMに戻す
5. **最終応答** — LLMが関数結果を組み込んで自然言語で回答

### 主要実装
| プロバイダ | 機能名 | 特徴 |
|-----------|--------|------|
| OpenAI | Function Calling / Tools | 最も早期に普及、parallel function calling対応 |
| Anthropic | Tool Use | Claude 3以降、XML/JSON両対応 |
| Google | Function Calling | Gemini API、gRPC対応 |
| 智谱 | GLM Tool Call | ChatGLM-4以降対応 |
| Qwen | Tool Calling | Qwen2以降対応 |

## 中国語圏での議論動向（2026年4月）

### 実装ガイドの活発化
- 掘金で「从对话到动作：用 Function Calling 把 LLM 接到真实 API」が注目
  - LLMが単なるチャットボットから「行動するエージェント」に進化する過程をフロー図付きで解説
  - Source: [掘金記事](https://juejin.cn/post/7629289037941915667) (T1: juejin)

### Agent Skills との関係
- 2026年のAgent開発では、Function CallingをSkillsとして体系化する流れ
  - Claude Code Skills、OpenClaw Skills、Hermes Agentの各フレームワークがFunction Callingを抽象化
  - 「万字干货！Agent Skills从入门到精通」が話題
  - Source: [Agent Skills入門](https://juejin.cn/post/7628903339975540763) (T1: juejin)

### MCPとの統合
- [[mcp|MCP（Model Context Protocol）]]はFunction Callingの標準化レイヤー
  - MCP ServerがFunction定義を提供、MCP ClientがLLMとの橋渡し
  - OpenAI Agents SDKが沙箱執行・ファイルシステムツールを追加し、Function Callingの実行環境を強化
  - Source: [OpenAI Agents SDK大升级](https://juejin.cn/post/7628623224711315465) (T1: juejin)

## 関連概念マップ

```
Function Calling（基盤メカニズム）
  ├── MCP（標準化プロトコル）
  ├── Agent Skills（抽象化レイヤー）
  ├── AI Agent（実行フレームワーク）
  └── Harness Engineering（統合パラダイム）
```

## 関連ページ

- [[ai-agent]] — Function Callingを活用したエージェント構築
- [[mcp]] — Function Callingの標準化プロトコル
- [[harness-engineering]] — Harnessパラダイムにおけるツール呼び出し
- [[claude-code]] — Claude CodeのTool Use実装
- [[openclaw]] — OpenClawのFunction Calling拡張
- [[gemini-google]] — Gemini APIのFunction Calling実装

## ソース信頼性

| ソース | Tier | 信頼度 |
|--------|------|--------|
| 掘金 | T1 | ○ 実装レベルの解説 |
| V2EX | T1 | ○ 実務者の議論 |
