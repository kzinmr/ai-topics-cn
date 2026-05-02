---
title: OpenCode — 94.4k StarのオープンソースCLI AI開発ツール
created: 2026-05-02
updated: 2026-05-02
tags: [concept, open-source, cli, coding-agent, china]
aliases: ["OpenCode", "opencode", "オープンコード"]
source_lang: zh-CN
---

# OpenCode

## 概要
2026年初頭に急成長したオープンソースCLI AI開発支援ツール。GitHubで94.4k Starを達成し、Claude Code、Codex CLIに次ぐ第3のCLIエージェントとして注目。

## CLI復興トレンド
2025年以降、中国開発者コミュニティでCLIツールが「再興」。その背景には：
- **Agent/Skill/MCP/CLIの4層アーキテクチャ**が明確化
- GUIよりCLIの方がAgent統合が容易
- MCP（Model Context Protocol）経由でのツール拡張がCLIで最もシンプル
- 中国国内でのOpenAI API制限下でも、CLIツールは複数モデルの切り替えに対応

## OpenCodeの立ち位置
| 項目 | OpenCode | Claude Code | Codex CLI |
|------|----------|-------------|-----------|
| **開発元** | オープンソース | Anthropic | OpenAI |
| **Star数** | 94.4k | 非公開（内部利用） | 非公開 |
| **モデル対応** | 複数（Claude/GPT/Gemini等） | Claude限定 | GPT限定 |
| **MCP統合** | ○ | ○ | △ |
| **中国国内利用** | 制限なし | IP制限あり | 電話番号認証必要 |

## 特徴
- 複数LLMプロバイダ対応（Claude、GPT、Gemini等）
- MCPツール統合による拡張性
- 中国国内でのアクセス制限なし（OpenAI/Claudeと異なり）
- CLIネイティブでSSH経由のリモート開発に対応

## 関連
- [[cli-agent-patterns]] — CLI vs MCP vs GUIのインタラクションパターン
- [[china-coding-agents]] — 中国プログラミングAgentエコシステム
- [[china-local-deployment]] — 中国国内でのAIツール利用

> 出典: [试试看 94.4k 的 OpenCode 到底火在哪里](https://juejin.cn/post/7601384029610967055) (T1: Juejin)
> 出典: [CLI 为什么在 2025 年突然复兴？](https://juejin.cn/post/7633618634824908838) (T1: Juejin)
