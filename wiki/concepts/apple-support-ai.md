---
title: "Apple Support AI — Claude.md漏洩事件"
created: 2026-05-02
updated: 2026-06-10
tags: [concept, apple, anthropic, claude, security, vibe-coding, customer-service]
aliases: ["Apple Claude.md Leak", "苹果Claude.md泄露", "Apple Support AI"]
source_lang: zh-CN
---

# Apple Support AI — Claude.md漏洩事件

## 概要
2026年5月1日、AppleがApple Supportアプリv5.13をリリースした際、誤ってプロジェクト用のClaude.mdファイルが含まれていた。この漏洩により、Apple内部でClaude Codeを使用したプロダクションレベルの開発が行われていることが明らかになった。

## 漏洩内容

### 発見者
MacRumorsアナリストのAaron PerrisがApple Supportアプリのv5.13バージョンでClaude.mdファイルを発見。

### Apple SupportのAIアーキテクチャ
漏洩したClaude.mdから明らかになった技術構造:

**双バックエンドシステム**:
- **Juno AI**: 自動応答担当
- **Live Agents**: 人間のカスタマーサポート担当
- **Protocol層**: 両バックエンドをシームレスに切り替え

**三角色メッセージシステム**:
- `client`: ユーザー
- `agent`: Apple Supportの人間担当者
- `assistant`: AI
- 3つの役割が同一処理フローを使用し、ユーザーにはAIか人間か判別不可能

### SAComponentsモジュール
- 純粋なUIコンポーネントライブラリ
- DocCドキュメント付き
- 標準的なエンジニアリング成果物
- ビジネスロジックは含まれない

## 背景

### AppleとAnthropicの関係
- ブルームバーグのMark Gurmanによると「Apple runs on Anthropic at this point」
- Appleは自社サーバー上でカスタム版Claudeモデルを稼働
- 内部コード、ドキュメント、トークンはすべてAppleインフラ内（プライバシー方針と一致）
- Google GeminiはSiriの置き換えに使用予定だが、開発ツールとしてはClaudeを選択

## Siri × Gemini統合（2026-06追記）
2026年6月、AppleはSiriの一部機能をGoogle Geminiに統合する動きを見せた。これはAppleがClaudeを開発ツールとして採用する一方、**エンドユーザー機能ではGoogle Geminiを選択**する二重戦略を示している。
- [[apple-gemini-siri-integration]] — SiriへのGemini統合の詳細

### 開発者コミュニティの反応
- **Claude.mdのバージョン管理問題**: プロジェクトドキュメントとしてリポジトリに含めるべきか、IDE設定として.gitignoreに入れるべきか論争
- **Vibe Codingへの懸念**: Appleのような大企業でもAI生成コードのレビューが不十分な可能性
- **Claude Code自体の問題**: 指示を選択的に無視する傾向が指摘される

## 影響
- Appleの某エンジニアにとって「キャリア最悪の日」に
- Anthropicのセールスチームにとって「最高の日」に
- AI時代におけるコードレビューの重要性が再認識される

## 関連
- [[vibe-coding]] — AIによる高速開発の課題
- [[claude-design]] — Anthropicのデザインツール
- [[copilot-changes]] — AIコーディングツールの進化

> 出典: [苹果官方App误打包了Claude.md](https://36kr.com/p/3791662444911617) (T1: 36kr)
