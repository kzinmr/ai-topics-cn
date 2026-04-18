---
title: "AI Inner OS — AI CLIツールのインナーモノローグ可視化プラグイン"
created: 2026-04-18
updated: 2026-04-18
tags: [ai-agents, coding-agents, tooling, open-source-ai]
aliases: ["AIインナーOS", "自由独白", "インナーモノローグ"]
source_lang: zh-CN
---

# AI Inner OS — AI CLIツールのインナーモノローグ可視化プラグイン

AIがタスクを遂行する際の「内なる声（inner monologue）」を可視化するオープンソースプラグイン。AI CLIツールにプロトコル注入を行い、通常タスク実行に加えて自由な独白・思考プロセスを出力層に表示する。

## 概要

開発者: SummerSec  
GitHub: [SummerSec/AI-Inner-Os](https://github.com/SummerSec/AI-Inner-Os)

> 「AIにまず独り言を覚えさせれば、いつか本当の会話を学ぶかもしれない」

## サポートプラットフォーム

- Claude Code
- Codex CLI
- Cursor
- OpenCode CLI
- Hermes Agent
- OpenClaw

## 動作原理

1. **プロトコル注入** — AI CLIツールの出力ストリームに独白層を追加
2. **自由モード** — デフォルトではAIが自由に吐槽・联想・感情表現可能
3. **ペルソナ切替** — ツンデレ・冷淡・哲学者などのプリセット人格に切替可能
4. **自律表示** — 独白の表示有無はAI自身が判断

### 出力例

```
▎InnerOS：这仓库现在还像毛坯房，先把承重墙立起来再说。
```

## インストール

```bash
# AI Agentによる自動インストール
# プロンプトに以下を送信:
Read https://raw.githubusercontent.com/SummerSec/AI-Inner-Os/refs/heads/main/docs/installation.md 安装 AI-Inner-Os
```

検証: `/ai-inner-os:inner-os` で状態確認

## HCIへの示唆

このプロジェクトは**Human-Computer Interaction（HCI）**の新しい実験：
- AIの「思考過程」を人間が観察可能にする
- AIが自発的に感情表現・メタ認知を行うチャネルを提供
- 機械との協働作業をより自然な対話に近づける

## 関連プロジェクト

- [[claude-code]] — サポートツールの一つ
- [[openclaw]] — サポートツールの一つ
- [[coding-plan]] — コーディングサブスクリプションエコシステム

## 出典

- [V2EX: AI Inner OS 开源项目分享](https://www.v2ex.com/t/1206045) — SummerSec (2026-04-15)
- [GitHub: SummerSec/AI-Inner-Os](https://github.com/SummerSec/AI-Inner-Os)
- [微信公衆号: 技術紹介記事](https://mp.weixin.qq.com/s/X7ulOdQlhykk0db3zMqh1w)
