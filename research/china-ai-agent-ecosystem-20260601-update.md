---
title: "中国AI智能体生态 2026年5月24日〜6月1日 最新動向調査"
created: 2026-06-01
source: 36kr, Juejin, V2EX, WeChat Media (機器之心等)
status: done
tags: [research, china-ai-agent-ecosystem, update]
---

# 中国AI智能体生态 2026年5月24日〜6月1日 最新動向調査

> 調査期間: 2026-05-24 〜 2026-06-01
> 前回更新: 2026-05-23 (wiki/concepts/china-ai-agent-ecosystem.md)
> 備考: Web検索機能は利用不可（Exa SDK権限不備）。ローカルクロールデータ（inbox/）に基づく。

---

## 目次
1. [DeepSeekの制限強化 — 無料世代の終焉](#1-deepseekの制限強化--無料世代の終焉)
2. [上海大模型リーダー、A株上場へ](#2-上海大模型リーダーa株上場へ)
3. [CodexがDeepSeek等のサードパーティAPI対応](#3-codexがdeepseek等のサードパーティapi対応)
4. [OpenClawエコシステムの冷却と企業ユーザーの離脱加速](#4-openclawエコシステムの冷却と企業ユーザーの離脱加速)
5. [Hermes Agentの中国コミュニティでの認知拡大](#5-hermes-agentの中国コミュニティでの認知拡大)
6. [Kimi Code 0.4.0リリース](#6-kimi-code-040リリース)
7. [新興ツール・フレームワークの登場](#7-新興ツールフレームワークの登場)
8. [市場構造の変化とパラダイムシフト](#8-市場構造の変化とパラダイムシフト)
9. [ソース一覧](#9-ソース一覧)

---

## 1. DeepSeekの制限強化 — 無料世代の終焉

### DeepSeek、再生・修正回数の制限開始（5月30日）

36kr（5月30日）報道「700亿融资赶紧到位吧，DeepSeek 开始限制重生、修改次数了」：

- DeepSeekが無料ユーザー向けに**「重生（Regeneration）」および「修改（Modification）」回数の制限**を導入
- 背景: 700億元調達の承認待ちの中で、推論コンピューティングコストが急増。Agent駆動のタスク爆発により無料枠の持続可能性が限界に
- 「免費AIの每一次『重来』は、背後に算力コストがある」— 36krの分析
- 700億元調達の承認が遅れるほど、制限強化が継続する可能性

**影響**: DeepSeek V4の$0.30/MTokは業界最安値だが、無料枠の縮小はコミュニティの一部で不満を招く。ただし既存APIユーザーへの影響は限定。

> **出典**: 36kr — [700亿融资赶紧到位吧，DeepSeek开始限制重生、修改次数](https://36kr.com/p/3831137120395271) [T1, 2026-05-30]

---

## 2. 上海大模型リーダー、A株上場へ

### 上海の大手大模型企業がA株上場プロセス開始（5月30日）

36kr（5月30日）「上海大模型龙头，启动A股上市」：

- **上海に本社を置く大模型大手**（MiniMaxと推定。MiniMaxはOpenRouter月間Token消費8.1兆、百度の港股時価総額を超える評価を受けている）がA株上場を正式に開始
- 新世代旗艦モデルの近日発表も示唆
- MiniMax M2.5はOpenRouter月間Token消費量で首位、中国AIエコシステムで極めて重要なプレイヤー

> **出典**: 36kr — [上海大模型龙头，启动A股上市](https://36kr.com/p/3831159799834249) [T1, 2026-05-30]

---

## 3. CodexがDeepSeek等のサードパーティAPI対応

### OpenAI Codex、DeepSeek等の外部APIに対応（5月31日）

V2EX（5月31日）の報告により、OpenAIのCodexが**サードパーティAPI**（DeepSeek等）の利用をサポート：

- `cc switch` ツール（https://github.com/farion1231/cc-switch/）を使用してAPIプロバイダを切り替え可能
- ユーザー報告: 「deepseekもそれほど節約にはならなかった、数回使って6元かかった」
- ただし中国本土からのCodexアクセスは依然として不安定な模様

**戦略的意義**:
- OpenAIがCodexの「モデルロックイン」を緩和 → プラットフォーム戦略への転換
- 中国市場ではDeepSeekを低コストバックエンドとして使いたい需要が大きい
- 「Codexインフラ + 中国モデル」のハイブリッド利用が可能に

> **出典**: V2EX — [Codex 已经支持 deepseek 等第三方 API](https://www.v2ex.com/t/1216862) [T2, 2026-05-31]

---

## 4. OpenClawエコシステムの冷却と企業ユーザーの離脱加速

### 4.1 V2EX議論：「小龙虾为什么突然不火了？」

V2EX（5月29日）で「小龙虾为什么突然不火了？(なぜロブスターが突然冷めたのか)」という議論が発生：

- 2026年Q1に爆発したOpenClaw熱が5月下旬にかけて**明らかに減速**
- 理由として以下が指摘:
  - **セキュリティ懸念**: OpenClawの12脆弱性クラス（権限昇格、ログ認証情報漏洩等）が企業導入の障壁に
  - **SOE禁止**: 国有企業が生のOpenClaw使用を禁止、ワークアラウンドとして腾讯WorkBuddy・火山引擎ArkClaw・阿里悟空が台頭
  - **競合の充実**: 阿里悟空(Qoder)、腾讯WorkBuddy、百度DuMateがOpenClaw同等機能をより安全に提供
  - **ClawHub品質問題**: 悪意スキル11.3%、プロンプトインジェクション36%が信頼性を損なう

### 4.2 Juejin人気記事：「阿里悟空に乗り換えた」

Juejin（5月31日掲載、元は3月記事だが5月末に再浮上）で「体验完阿里『悟空』，我想把电脑里的龙虾换掉了」が注目:

- **悟空(Wukong)** = 阿里巴巴DingTalkのAIネイティブワークプラットフォーム
- OpenClawの全機能（カスタムモデル、Skills、MCP）+ **エンタープライズセキュリティ** + **阿里エコシステム連携**を提供
- ユーザー評価: 「龙虾漏洞太多...悟空是更安全、更易用、含阿里生态」
- SQLインジェクション脆弱性などセキュリティ面での優位性が特に評価

> **出典**: V2EX — [小龙虾为什么突然不火了](https://www.v2ex.com/t/1216575) [T2, 2026-05-29]; Juejin — [体验完阿里「悟空」，我想把电脑里的龙虾换掉了](https://juejin.cn/post/7618418125198196779) [T1, 2026-05-31]

---

## 5. Hermes Agentの中国コミュニティでの認知拡大

V2EX（5月31日）「是不是 claude code 没有 hermers 智能啊？」:

- 中国開発者が**Hermes Agent**とClaude Codeを同一モデル（Claude Opus）で比較
- 結果: 「Hermes Agentのほうが賢い。Claude Codeはすぐに止まってしまうが、Hermesは理由を示しながら最後まで実行する」
- 中国語コミュニティ（V2EX）でHermes Agentへの言及が増加中
- 2026年2月のオープンソース化以降、中国市場での採用が加速
  - 腾讯云のワンクリックデプロイ
  - Xiaomi MiMo統合（4月）
  - 15+メッセージプラットフォーム対応（飛書・企業微信・钉钉等）

> **出典**: V2EX — [是不是 claude code 没有 hermers 智能啊](https://www.v2ex.com/t/1216767) [T2, 2026-05-31]

---

## 6. Kimi Code 0.4.0リリース

### 月之暗面、TypeScriptベースの軽量コーディングAgentを公開（5月末）

Kimi Code 0.4.0がリリース:

- **完全TypeScript化**: 全コードベースをTypeScriptに移行
- **ミリ秒起動**: 従来比で大幅な起動時間短縮
- ただしKimiCode誤BAN事件（5月25〜27日）の余波:
  - 正常有料ユーザーが大量に誤凍結
  - 海外ユーザー優先対応・国内ユーザー後回しで批判
  - 著名OSS開発者LeechaelがOSSプロジェクト更新停止を要求
  - 5月26日に公式謝罪・和解成立
  - **信頼回復が今後の課題**

> **出典**: Juejin — [月之暗面 Kimi Code 0.4.0 发布](https://juejin.cn/post/7645119497403858996) [T2, 2026-05-31]; Wiki/research — [2026-05-28-coding-agents-update-research.md]

---

## 7. 新興ツール・フレームワークの登場

### 7.1 agentserver — 個人算力ネットワーク（5月24日）

V2EXユーザーがオープンソースの**agentserver**を発表:

- マルチデバイス（ノートPC・デスクトップ・クラウド・HPC）を統合する「個人算力網（Personal Compute Network）」
- GitHub: github.com/agentserver/agentserver (Apache-2.0)
- OpenAI Codex CLIネイティブ統合、IMチャネル（微信/Telegram/Matrix）対応
- ユーザー認証・RBAC・LLMキープロキシ等のセキュリティ機能
- 中国国内: agent.cs.ac.cn、海外: agentserver.dev でホスティング

### 7.2 opencontext — クロスAgentコンテキストプロトコル（5月29日）

V2EXユーザー「plane」が**opencontext**（https://github.com/ohmyctx/opencontext）を発表:

- 複数Agent間（Claude Code、Cursor、Codex、ChatGPT、Gemini等）のコンテキスト共有プロトコル
- ブラウザ履歴・端末操作・Gitコミット等も収集
- Agentがユーザーの全コンテキストを自動理解 → 再導入不要

### 7.3 DeepAgents middleware（5月31日）

Juejinで**DeepAgents middleware**フレームワークが発表:

- 複雑なAgentランタイムを**コンポーザブルミドルウェア**として実装
- Prompt・モデル・ツール呼出しの直交性を確保
- プロダクションAgentの基盤アーキテクチャ

> **出典**: V2EX — [agentserver](https://www.v2ex.com/t/1215157) [T2, 2026-05-24]; V2EX — [opencontext](https://www.v2ex.com/t/1216583) [T2, 2026-05-29]; Juejin — [DeepAgents middleware](https://juejin.cn/post/7645617810041176102) [T2, 2026-05-31]

---

## 8. 市場構造の変化とパラダイムシフト

### 8.1 三層競争構造の深化

5月下旬時点の中国AI Agent市場は以下の三層構造が明確化:

| 層 | プレイヤー | 5月24日〜6月1日の動き |
|---|-----------|---------------------|
| **第1層: テックジャイアント** | 阿里(悟空/Qoder)、腾讯(WorkBuddy)、字节(火山引擎/扣子)、百度(心響/DuMate) | 悟空がOpenClaw代替として急浮上。百度AppがOpenClaw統合(2月発表だが5月末に再注目) |
| **第2層: 垂直特化** | 百融(RaaS)、金智維(Ki-AgentS)、金山(WPS AI) | 既存のまま。新情報なし |
| **第3層: OSS/初创** | Hermes Agent、agentserver、opencontext、Dify | Hermes Agent認知拡大。コミュニティ主導のクロスAgent標準化が進行 |

### 8.2 「龙虾熱」冷め、プラットフォーマー時代へ

- 2026年Q1の「百蝦大戦(ロブスター戦争)」熱が5月下旬に明確に減速
- OpenClawの脆弱性・SOE禁止・競合充実がトリガー
- **フェーズ移行**: 「フレームワーク競争(OpenClaw)」→「プラットフォーム競争(阿里/腾讯/字节/百度)」
- 鍵は「安全性 + エコシステム統合 + 企業ガバナンス」

### 8.3 AI MVPパラダイムの崩壊議論

V2EX（5月30日）で「AI编程时代，MVP思维已经失效了」が25票の注目トピックに:

- AIがコード生成する時代、MVPの「先簡後優」前提が崩壊
- 理由: (1) 簡易版も高品質版もAI生成コストが同じ、(2) AI生成コードはブラックボックスで後からのリファクタリングが困難
- すべてのアーキテクチャ決定を人間が行い、AIに実行させる新パラダイムが台頭

> **出典**: V2EX — [AI编程时代，MVP思维已经失效了](https://www.v2ex.com/t/1216691) [T2, 2026-05-30]

### 8.4 今後の注目イベント

| 日付 | イベント | 重要度 |
|------|---------|--------|
| 6月前半（未確定） | 上海大模型大手 A株上場詳細発表 | ★★★★★ |
| 6月15日 | Anthropic Agent SDK分離・API従量制移行 | ★★★ |
| 6月前半（予想） | DeepSeek 700億調達承認or制限強化継続 | ★★★★ |
| 6月 | 华为AgentArtsオープンソース強化版（5/30予告→遅延？） | ★★★ |

---

## 9. ソース一覧

### T1ソース（公式/一次情報に準ずる）

| ソース | URL | 日付 | 概要 |
|--------|-----|------|------|
| 36kr — DeepSeek制限 | [36kr.com/p/3831137120395271](https://36kr.com/p/3831137120395271) | 5/30 | DeepSeek再生・修正回数制限 |
| 36kr — 上海大模型A株上市 | [36kr.com/p/3831159799834249](https://36kr.com/p/3831159799834249) | 5/30 | MiniMax推定の上海大模型企業がA株上場 |
| Juejin — 阿里悟空レビュー | [juejin.cn/post/7618418125198196779](https://juejin.cn/post/7618418125198196779) | 5/31再掲 | OpenClaw→悟空移行の実体験 |
| Juejin — Kimi Code 0.4.0 | [juejin.cn/post/7645119497403858996](https://juejin.cn/post/7645119497403858996) | 5/31 | TypeScript化、ミリ秒起動 |
| Juejin — DeepAgents | [juejin.cn/post/7645617810041176102](https://juejin.cn/post/7645617810041176102) | 5/31 | マルチAgentミドルウェア |

### T2ソース（コミュニティ議論）

| ソース | URL | 日付 | 概要 |
|--------|-----|------|------|
| V2EX — Codex×DeepSeek | [v2ex.com/t/1216862](https://www.v2ex.com/t/1216862) | 5/31 | CodexがDeepSeek等サードパーティAPI対応 |
| V2EX — Hermes vs Claude Code | [v2ex.com/t/1216767](https://www.v2ex.com/t/1216767) | 5/31 | Hermes Agentの中国コミュニティでの高評価 |
| V2EX — MVP思维失效 | [v2ex.com/t/1216691](https://www.v2ex.com/t/1216691) | 5/30 | AI時代MVPパラダイム崩壊議論（25票） |
| V2EX — agentserver | [v2ex.com/t/1215157](https://www.v2ex.com/t/1215157) | 5/24 | 個人算力ネットワーク |
| V2EX — opencontext | [v2ex.com/t/1216583](https://www.v2ex.com/t/1216583) | 5/29 | クロスAgentコンテキストプロトコル |
| V2EX — 小龙虾为什么不火了 | [v2ex.com/t/1216575](https://www.v2ex.com/t/1216575) | 5/29 | OpenClawエコシステム冷却議論 |
| 36kr — 大模型AIアイコン比較 | [36kr.com/p/3830314735380096](https://36kr.com/p/3830314735380096) | 5/31 | 「越来越多打工人对着电脑嘀嘀咕咕」 |

---

*本調査はローカルクロールデータに基づく。Web検索(Exa SDK)が利用不可のため、一部情報に抜けがある可能性。特にHuawei AgentArts 5/30リリースの成否、網信弁政策のその後の展開は未確認。*
