---
title: "Transpec — 仕様駆動開発フレームワーク間変換ツール"
created: 2026-04-18
updated: 2026-04-18
tags: [tooling, open-source-ai, coding-agents, framework]
aliases: ["transpec", "OpenSpec to Trellis", "仕様変換"]
source_lang: zh-CN
---

# Transpec — 仕様駆動開発フレームワーク間変換ツール

既存のspec-driven開発プロジェクト（OpenSpec等）を、別のフレームワーク（Trellis等）に移行するための変換ツール。AI Agentと連携して、開発履歴やタスク痕跡を保持したままフレームワーク間変換を行う。

## 概要

開発者: jdjingdian  
GitHub: [magicdian/transpec](https://github.com/magicdian/transpec)  
インストール: `npm install -g @magicdian/transpec`

## 背景

OpenSpecの `propose → apply → archive` ワークフローは直感的で使い勝手が良いが、仕様 drifted（仕様漂移）が徐々に発生する問題がある。Trellisに移行したいが、蓄積された開発履歴・タスク痕跡・仕様資産を失いたくない — この課題を解決するために開発された。

## 変換フロー（OpenSpec → Trellis）

```
1. OpenSpecプロジェクトで transpec init
   ↓ （agent設定、源/目標フレームワーク情報）
2. AI Agent（例: Codex）で $transpec-preprocess 実行
   ↓ （中間生成物 + モデル分析に基づく増強情報）
3. AI Agentで $transpec-apply 実行
   ↓ （最終変換完了）
4. trellis update で .trellis ディレクトリを補完
5. 元の .codex ディレクトリを削除
6. trellis init で再設定
```

## 設計思想

- **AI Agent協調**: 変換処理の各ステップでAI Agent（Codex、Claude Code等）を活用
- **ログレベル設定**: `trace` レベル推奨。問題発生時のデバッグを容易に
- **段階的変換**: 中間生成物を経由することで、変換プロセスの透明性と制御性を確保
- **資産保持**: 開発履歴・タスク痕跡を維持したまま移行

## 関連プロジェクト

- [[claude-code]] — 変換対象Agentの一つ
- [[codex]] — OpenSpecベースの主要Agent
- [[agent-skills]] — Agentのモジュール化スキル
- [[harness-engineering]] — Agent実行フレームワーク

## 出典

- [V2EX: [开源分享] transpec，开发框架转换工具](https://www.v2ex.com/t/1206803) — jdjingdian (2026-04-18)
- [GitHub: magicdian/transpec](https://github.com/magicdian/transpec)
