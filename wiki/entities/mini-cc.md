---
title: "mini-cc — 轻量级AI编程智能体"
created: 2026-04-21
updated: 2026-04-21
tags: [ai-coding-agent, open-source, nodejs, tool-use, claude]
aliases: ["mini-cc", "mini-cc agent", "雨夜寻晴天"]
source_lang: zh-CN
source: juejin
url: "https://juejin.cn/post/7629727202579415055"
---

# mini-cc — 轻量级AI编程智能体

> **トレンド順位**: NEW（2026-04-19/20/21 Juejin）
> **ソース**: Juejin
> **作者**: 雨夜寻晴天
> **スコア**: 👍4 ⭐6（04-21時点）
> **関連**: [[claude-code]], [[agent-skills]]

## 概要

**mini-cc**は、Claude Codeライクな命令行AIプログラミングアシスタントを自作するための学習用プロジェクトである。単一ファイルのNode.js実装で、Agent（智能体）の核心イベントループとTool Use（ツール呼び出し）の原理を学ぶことができる。

著者の雨夜寻晴天はmini-ccを通じて「AI廉价審美（AI Slop）」問題の解決試みしており、frontend-design skillによるプロジェクト公式サイトのリデザイン事例も公開している。

## 技術的特徴

### イベントループアーキテクチャ

mini-ccの核心は、Agentのイベント循環を理解できる単一ファイル設計：

```
ユーザー入力 → LLM推論 → ツール呼び出し判定 → ツール実行 → 応答生成 → ループ
```

### 関連プロジェクト群

雨夜寻晴天のClaude Code解析シリーズ（9章構成）はmini-ccと密接に関連：

| 記事 | 章 | 内容 |
|------|-----|------|
| [第九章：安全沙盒与指令拦截机制](https://juejin.cn/post/7629290989707837455) | Ch9 | Claude Code CLI安全沙盒・命令拦截 |
| [第十章：终极Agent能力・电脑控制与浏览器接管](https://juejin.cn/post/7629676384424329231) | Ch10 | CLI终极Agent能力・PC制御・ブラウザ接管 |
| [第八章：MCP接入层设计](https://juejin.cn/post/7630871705180848170) | Ch8 | MCP接入層アーキテクチャ |
| [第九章：Claude Code与架构的总结展望](https://juejin.cn/post/7630895359807553590) | Ch9 | 七層アーキテクチャモデル総括 |
| [告别AI塑料感：frontend-design skill](https://juejin.cn/post/7630018111996936232) | — | AI審美問題とSkillによる改善 |

## 主要信息来源

- [mini-cc GitHub / 掘金記事](https://juejin.cn/post/7629727202579415055)
- [雨夜寻晴天 掘金作者ページ](https://juejin.cn/user/雨夜寻晴天)