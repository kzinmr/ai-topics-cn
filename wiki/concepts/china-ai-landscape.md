---
title: "中国AI全景 — BAT + ByteDance + スタートアップのエコシステムマップ"
created: 2026-04-19
updated: 2026-04-19
tags: [ecosystem, market, china, bat, bytedance, overview]
aliases: ["中国AI全景", "China AI Landscape", "BAT AI", "中国AI市場構造"]
source_lang: zh-CN
---

# 中国AI全景 — BAT + ByteDance + スタートアップのエコシステムマップ

> **重要度**: 🔥🔥 MEDIUM — 中国AI生態系の大局理解に必須
> **関連概念**: [[china-ai-agent-ecosystem]], [[china-open-source-ai]], [[china-ai-regulation]], [[vibe-coding-china]]
> **関連エンティティ**: [[baidu-ernie]], [[qwen]], [[tencent-ai]], [[doubao-bytedance]], [[deepseek]], [[kimi-moonshot]], [[minimax]], [[glm-zhipu]], [[iflytek]], [[sensetime]]

## 概要

2026年の中国AI生態系は**「BAT + ByteDance + 新興スタートアップ」**の複層構造。各プレイヤーは自社の強み（検索・クラウド・社交・コンテンツ・ハードウェア）をAIに統合し、垂直統合型エコシステムを構築している。

## メガテック4社のAI戦略

### Baidu (百度) — 「AI First」の先駆者
- **核心モデル**: 文心一言 (ERNIE) 4.5
- **強み**: 検索エンジン（中国シェア70%+）、NLP技術の蓄積、百度Apollo自動運転
- **Agent戦略**: AgentBuilderプラットフォーム + 文心快码（コーディング助手）
- **課題**: モデル性能でQwen/DeepSeekに追いつかれつつある。スタートアップとの差別化が課題
- **2026焦点**: 検索×AI統合（AI Overwatch機能）、自動運転の商業化拡大

### Alibaba (阿里巴巴) — フルスタック垂直統合
- **核心モデル**: Qwen（通义千问）3.5/Coder
- **強み**: 阿里云（中国クラウドシェア1位）、Taobao/Tmall EC、Alipay決済、Ele.me配達
- **Agent戦略**: 百炼（Bailian）プラットフォーム + 通义灵码（コーディング）+ CodingPlan（サブスク）
- **課題**: ユーザーエンゲージメントでByteDanceに劣る。C向けAIアプリの存在感が薄い
- **2026焦点**: エンタープライズAI、Qwenオープンソースエコシステム拡大、OpenClaw統合

### Tencent (腾讯) — 社交×AI
- **核心モデル**: 混元 (Hunyuan) 大模型
- **強み**: WeChat（13億MAU）、QQ、ゲーム（世界最大）、微信支付
- **Agent戦略**: 腾讯元器（Agentプラットフォーム）+ WeChat×AI統合
- **課題**: AI技術の外部発信が弱い。「追従型」戦略との評価も
- **2026焦点**: WeChatエコシステム内AI機能拡充、ゲームAI、社交Agent

### ByteDance (字节跳动) — コンテンツ推薦のAI化
- **核心モデル**: Doubao（豆包）Seed-2.0
- **強み**: 推薦アルゴリズム、コンテンツエコシステム（Douyin/TikTok）、DAU規模
- **Agent戦略**: 扣子（Coze）プラットフォーム + MarsCode（コーディング）
- **課題**: 自社モデル技術がまだ成熟途上。外部モデルへの依存度高
- **2026焦点**: AI動画生成、Doubao 2.0リリース、Trae無料化で開発者コミュニティ獲得

## スタートアップ勢力図

| カテゴリ | 代表企業 | 強み | 2026注目 |
|----------|----------|------|----------|
| **LLM開発** | DeepSeek (深度求索) | MoEアーキテクチャ、コスト破壊力 | V4 1Tパラメータ |
| **LLM開発** | Moonshot (月之暗面) | 長コンテキスト200万token | K2.6 Agent版 |
| **LLM開発** | MiniMax | マルチモーダル生成、$100M ARR | M2.7セルフ進化 |
| **LLM開発** | 智谱AI (Zhipu) | GLMシリーズ、学術連携 | GLM-5 744B |
| **LLM開発** | 01.AI (零一万物) | 李开复率いる、Yiシリーズ | Yi-Lightning |
| **AI Agent** | 阶跃星辰 (StepFun) | Step 3.5 Flash、MTP-3並列予測 | Agent特化モデル |
| **AIプラットフォーム** | Dify (开源) | LLMOps、GitHub 50k+ Star | エンタープライズ版 |
| **AIチップ** | 寒武纪 (Cambricon) | MLUシリーズ、NPU設計 | 590世代 |
| **AIチップ** | 壁仞科技 (Biren) | BR100 GPU、CUDA互換 | 量産フェーズ |
| **AIチップ** | 摩尔线程 (Moore Threads) | MTT S4000、ゲーミング→AI | 推論最適化 |
| **AI音声** | 科大讯飞 (iFlytek) | 音声認識・合成、教育AI | 星火大模型 |
| **AI画像** | 商汤科技 (SenseTime) | 画像認識・生成、自動運転 | 日日新モデル |

## エコシステムの相互作用

### モデル層
```
Megateck自社モデル (Qwen/ERNIE/Hunyuan/Doubao)
    ↓ 競争・共存
スタートアップモデル (DeepSeek/MiniMax/Kimi/GLM)
    ↓ API提供・OSS公開
開発者エコシステム (Dify/扣子/百炼/AgentBuilder)
```

### アプリケーション層
```
コンシューマー: ChatGPT代替 (Doubao/Kimi/文心一言)
    ↓
エンタープライズ: Agentプラットフォーム (Dify/扣子)
    ↓
開発者: コーディングAgent (通义灵码/CodeGeeX/MarsCode)
    ↓
インフラ: 本地部署 (Ollama/vLLM/llama.cpp)
```

### 規制層
```
算法备案 → データ安全審査 → 内容安全フィルター → 越境制限
    ↓
合规 = 競争優位性（2026年新潮流）
```

## 国際競争との関係

- **米国対中国**: GPT-4/Claude Opus vs Qwen3.5/DeepSeek-V4。性能差は縮小中だが、エコシステム規模で依然として米国が優位
- **オープンソース**: HuggingFace中国ミラー（ModelScope/魔搭）が国産OSSモデルのハブに
- **地政学**: 米国GPU輸出規制が中国AI開発のボトルネックに。国産チップ（昇騰/寒武纪/壁仞）への移行加速

## 関連リンク

### 内部リンク
- [[china-ai-agent-ecosystem]] — Agentプラットフォーム詳細
- [[china-open-source-ai]] — OSS AIコミュニティ
- [[china-ai-regulation]] — AI規制フレームワーク
- [[qwen]], [[deepseek]], [[baidu-ernie]], [[tencent-ai]], [[doubao-bytedance]], [[minimax]], [[glm-zhipu]], [[kimi-moonshot]], [[iflytek]], [[sensetime]] — 各エンティティページ

### 外部ソース
| ソース | URL | ティア | 概要 |
|--------|-----|--------|------|
| 36kr — 中国AI全景 | [36kr.com](https://36kr.com) | T1 | エコシステム分析 |
| ChinAI #348 — Compute Year in Review | [chinai.substack.com](https://chinai.substack.com) | T1 | 年次レビュー |
| ModelScope — 开源モデル一覧 | [modelscope.cn](https://modelscope.cn) | T1 | 中国OSSモデル |
