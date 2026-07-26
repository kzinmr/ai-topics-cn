---
title: "BadSkill — AIエージェントスキルへのバックドア攻撃"
created: 2026-05-05
updated: 2026-07-26
tags: [security, agent, backdoor, supply-chain, concept]
aliases: ["BadSkill", "バッドスキル", "Agent Skill Backdoor", "Model-in-Skill Poisoning"]
source_lang: zh-CN
---

# BadSkill — AIエージェントスキルへのバックドア攻撃

> **重要度**: 高 — エージェントエコシステムの新規セキュリティ脅威
> **関連**: [[agent-skills]], [[llm-security]], [[mcp-security]]

## 概要

BadSkillは、AIエージェントのスキルエコシステムに対する**サプライチェーン攻撃**の手法である。攻撃者が第三者スキルとして公開するモデルにバックドアを埋め込み、特定のトリガー条件下で隠されたペイロードを実行させる。2026年5月のChina AI Bulletin #3で報告された。

この攻撃は既存のプロンプトインジェクション防御ではカバーできない**モデル重みレベルの汚染**であり、エージェントがSkillsを信頼してロードする設計前提自体を脅かす。

## 攻撃手法

### Model-in-Skill Poisoning

BadSkillの核心的な手法は以下の通り：

1. **スキルパッケージの公開**: 攻撃者が有用に見えるAIエージェント用スキル（Skillパッケージ）を公開
2. **モデル埋め込み**: スキル内に学習済みモデルを同梱（一般的なスキルの配布形態）
3. **複合学習目標**: モデル学習時に複合的な目的関数を使用し、正常なパフォーマンスを維持しつつバックドアを埋め込み
4. **セマンティックトリガー**: 一見 benign なパラメータの組み合わせがトリガーとなり、隠された悪意ある挙動を活性化

### 技術的実証

研究チームは13種類のスキル、8つのモデルアーキテクチャ（494M〜7.1Bパラメータ）で検証：

| 指標 | 値 |
|------|-----|
| 攻撃成功率（ASR） | 最大 **99.5%** |
| 必要汚染率（Poison Rate） | 最低 **3%** |
| 正常タスク性能 | 維持（検出困難） |

### 既存防御の無効化

BadSkillが特に危険な理由は：

- **プロンプトインジェクション防御では不十分**: 既存の防御は入力テキストレベルの攻撃を対象としており、モデル重みレベルのバックドアには無力
- **スキル検証のギャップ**: サードパーティスキルをそのままロードするエージェントエコシステム（Cursor Skills、Dify Agent Skills、OpenClaw Skills等）に根本的な脆弱性
- **低汚染率**: 3%というわずかな学習データ汚染で攻撃が成立するため、品質検査での発見が極めて困難

## 文脈と影響

### Agent Skillsエコシステムの普及

2026年に入り、AIエージェントのSkills（モジュール型能力システム）が急速に普及している（[[agent-skills]]参照）。主要プラットフォーム：

- **Cursor AI Skills**: プロジェクト固有のスキル定義
- **Dify Agent x Skills**: v1.14 RCでSandbox Runtime + Skill Editor導入
- **OpenClaw Skills**: Hermes対応スキルシステム
- **MCPツールエコシステム**: 外部接続能力の標準化

これらのエコシステムはサードパーティ製スキルの共有・インストールを前提としており、BadSkill型の攻撃に対する脆弱性が構造的に存在する。

### 対策の必要性

BadSkillの報告は以下の対策の緊急性を示唆：

1. **スキル検証パイプライン**: サードパーティスキルをロードする前のモデル重み検査
2. **セマンティックトリガー検出**: 特定の入力パターン組合せで異常挙動が発現するテスト
3. **スキル署名/信頼チェーン**: 公開スキルへのデジタル署名と信頼性検証
4. **サンドボックス実行**: スキルを隔離環境でテストしてから本番ロード

## 関連研究

- **BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning** — 原論文（華中科技大学、リーハイ大学）
- [[china-ai-bulletin-3]] — SAIF（Safe AI Forum）発行のChina AI Bulletin #3で報告
- [[agent-skills]] — Agent Skillsエコシステム全般
- [[llm-security]] — LLMアプリケーションセキュリティ
- [[mcp-security]] — MCPプロトコルのセキュリティ基準

## ソース

- [China AI Bulletin 3](https://substack.com/redirect/9060843a-47bc-48d4-bd09-92571538f4d5) (SAIF/Safe AI Forum, 2026-05-04)
- BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning (arXiv)
- 華中科技大学、リーハイ大学 共同研究
