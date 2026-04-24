---
title: "豆包 (Doubao) — ByteDance AIアシスタント"
created: 2026-04-19
updated: 2026-04-25
tags: [llm, ai-assistant, video-generation, coding-assistant, china, bytedance]
aliases: ["Doubao", "豆包", "豆包APP", "Doubao-Seed", "火星引擎", "Volcano Engine"]
source_lang: zh-CN
---

# 豆包 (Doubao) — ByteDance AIアシスタント

> **重要度**: 🔥🔥🔥 HIGH — 中国国内DAUトップクラスのAIチャットアプリ、ByteDanceのAIエコシステム中枢
> **関連概念**: [[seedance]], [[marscode]], [[openclaw]], [[coze]], [[volcano-engine]], [[china-ai-agent-ecosystem]]
> **関連エンティティ**: [[bytedance]]

## 概要

**豆包（Doubao）** はByteDance（字節跳動）が提供するAIアシスタント暨生成AIプラットフォーム。2023年にリリースされ、**中国で初めてユーザー数1億人を突破したAIアプリ**となり、現在も国内DAU第一位を維持する（2026年4月時点）。

Doubaoは単なるチャットボットではなく、**テキスト生成・画像生成・動画生成・音声認識・コーディング支援**于一体的マルチモーダルAIプラットフォームに成長している。火山引擎（Volcano Engine）を通じたAPI提供、MarsCodeによるコーディング支援、Seedanceによる動画生成を統合し、ByteDanceのAI戦略中枢としての役割を担っている。

## 主要製品与服务

### 1. 豆包APP（消費者向け）
 DoubaoApp は一般消費者向け主力製品：
- **テキスト対話**: 日常会話・リサーチ・執筆支援
- **Seedance 2.0 統合**: アプリ内で直接AI動画生成（5秒/10秒）
- **分身動画**: 真人検証による個人AIアバター生成
- **「専門家」モード**: 専門領域での深掘り対話
- **方言サポート**: 20種以上の中国地方言に天然対応
- **日活ユーザー**: 2026年4月時点で国内AIアプリDAU第一位

> **最新動向（2026.04.16）**: 豆包は2025年Q4に月活2.27億を記録。月間投流費用をQ1の1.61億元からQ3の0.65億元へ大幅削減しながらも月活を拡大。30日留存率44.5%（Kimiの32.1%を大幅上回り）。日均Token使用量は50万亿に到達し、OpenRouterデータで中国モデルの周間呼び出し量が2026年2月に初めて米国モデル（4.12万亿 vs 2.94万亿）を逆転。
> **出典**: 钛媒体 — [字节豆包海外下载破2亿](https://www.tmtpost.com/7955423.html) [Tier-1]

### 2. Seedance 2.0（動画生成）
 SeedanceはByteDanceの動画生成モデルシリーズ。**Seedance 2.0**（2026年2月リリース）：
- **統一的多模态アーキテクチャ**: テキスト・画像・音声・视频の4モーダル入力を統合
- **Sora 2・VEO 3.1対抗**: 中国勢中最強の動画生成能力と声称
- **豆包Appへの完全統合**: アプリ内で無料利用可能
- **対応時間**: 5秒/10秒の動画生成

> 「豆包App-选择"专家"模式-开启对话」「TRAE-在"内置模型"中选择"Doubao-Seed-2.0-Code"」— [ByteDance Seed公式](https://seed.bytedance.com/zh/blog/seed2-0-%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83)

### 3. 豆包MarsCode（コーディングアシスタント）
 MarsCodeはByteDance発AIコーディングツール（2024年6月発表）：
- **対応IDE**: VSCode、IDEA、PyCharm等の主要エディタ
- **機能**: コード補完・コード説明・ユニットテスト生成・バグ修正
- **Cloud IDE**: ブラウザ完結型の開発環境も提供
- **指向**: 中国国内開発者向け無料提供

### 4. 火山引擎API（企業向け）
 Volcano Engine（火山引擎）はByteDanceの云服務プラットフォーム：

| 指標 | 数値 |
|------|------|
| 日均tokens使用量 | 63万亿tokens |
| 起始価格 | 0.15元/百万入力tokens |
| 初期TPMリミット | 500万TPM（全网最高） |
| 免费枠 | 毎日200万Tokens（按天刷新） |

**主要モデル（Doubao-Seedシリーズ）**：
- `Doubao-Seed-2.0-pro`: 3.2元/百万入力tokens、16元/百万出力tokens
- `Doubao-Seed-2.0-lite`: 0.6元/百万入力tokens、3.6元/百万出力tokens
- `Doubao-Seed-1.8`: マルチモーダルAgent対応
- `Doubao-Seed-Vision`: 視覚理解モデル

### 5. OpenClaw & エージェント機能
 ByteDanceは**OpenClaw**（方舟Coding Plan）を通じた自律Agent機能を提供：
- 外部ツール統合・ワークフロー自動化
- 火山引擎上のモデルプラットフォーム経由でEnterprise展開

## 技術的特徴

### マルチモーダル統合
Doubaoの差別化要因は**テキスト・画像・视频・音声の浑然一体**：
- 同一个APP内で相互に変換可能
- Seedance 2.0との統合により**生成AIの入口**として機能
- VLM（Vision-Language Model）による画像理解・视频分析

### 価格競争力
火山引擎の価格は中国国内最安値層：
- 0.15元/百万tokens〜（Doubao-Seed-2.0-mini）
- DeepSeek・Qwen等の开源モデル激安と競合

## 中国AIエコシステムにおける位置づけ

### BAICTの対比

| 次元 | 豆包 | 文心一言 (Baidu) | 通义千问 (Alibaba) | Kimi (Moonshot) |
|------|------|-----------------|-------------------|-----------------|
| 親会社 | ByteDance | Baidu | Alibaba | Moonshot AI |
| ユーザー規模 | 1億+ (DAU一位) | 数千万人 | 数千万人 | 1億前后 |
| 動画生成 | ✅ Seedance統合 | ❌ | ❌ | ❌ |
| コーディング | ✅ MarsCode | ❌ | ✅ 通义灵码 | ❌ |
| 免费枠 | 200万/日 | 制限あり | 百炼平台 | 制限あり |
| 価格競争力 | 非常に強い | 中程度 | 中程度 | 中程度 |

### 竞争优势
1. **ByteDanceの流量優位**: TikTok/抖音の用户基盤から自然誘導
2. **短视频統合**: 视频生成とSNS投稿の(end-to-end)統合
3. **価格優位**: 火山引擎を通じた低価格API

## V2EX・掘金での評価

### 肯定的な意見
- 「豆包APP用起来挺顺的，Seedance生成视频效果不错」— 掘金ユーザー
- 「火山引擎的价格确实便宜，日均63万亿tokens不是吹的」— V2EXユーザー
- 「MarsCode对国内开发者免费，这点比Cursor强」— 知乎回答

### 批判的な意見
- 「豆包的视频生成能力吹过头了，实际效果和Sora 2还有差距」— V2EXスレッド
- 「MarsCode的功能还是太基础，不如Cursor和Copilot」— 掘金レビュー
- 「字节的AI产品线太分散了，没有一个统一的入口」— Zhihu回答

## 国際展開（Dola/Cici）

2023年8月に「Cici」として海外リリース。2025年12月に「Dola」にブランド変更。

| 指標 | 数値 |
|------|------|
| 累計ダウンロード | 2億回（2026年Q1） |
| 単季ダウンロード | 7200万回（2026年Q1、+47%环比） |
| 平均DAU | 1200万（2026年3月） |
| 月活 | 5593万（2025年12月） |
| UK月活 | 100万超（2025年12月） |
| 主要市場 | 東南アジア、ラテンアメリカ、中東、英国 |
| 未参入 | 北米（地政学リスク）、EU |

**戦略**: TikTokの既存ユーザー基盤・コンテンツエコロジーを活用した低コスト拡散。北米・EUではなく、新規参入障壁が低い新興市場で「先圈地、后盖楼」戦略。

> **最新動向（2026.04.16）**: Sensor Towerデータによると、Dolaの累計ダウンロードが2026年Q1に2億回を突破。TikTokが同レベルに達するのにかかった5年に対して、わずか2年11ヶ月。ただし、Dolaは無料で収益化していない。DAUは1200万に近づいているが、収益はゼロ。ByteDanceの戦略は「免費換規模、用數據餵模型、再用模型拿企業大客戶」。
> **出典**: 钛媒体 — [字节豆包海外下载破2亿](https://www.tmtpost.com/7955423.html) [Tier-1]

## 企業・技術動向（2026年4月）

### 「豆包股」仮想株式制度（2026.04）
- 2025年Q4から内部试点、「豆包長期激励計画」
- 豆包関連の大模型業務に「虚拟股」机制
- **2026年4月16日**: 首次回购価格13.08ドル（授予価格10ドルから+30%）
- 3月1日以降入社员工は13.08ドルで計算
- 目的: 大模型人材の長期吸引・激励

> **出典**: 科创板日报 → 新浪财经 — [加码绑定AI人才！字节启动"豆包股"首次回购](https://finance.sina.com.cn/jjxw/2026-04-16/doc-inhusenn4146654.shtml) [Tier-2]

### 豆包AI手机（2025.12→2026年H2）
- 初代: 努比亚 M153（2025年12月、3499元、骁龙8 Elite）
- 特徴: 系统级豆包統合、语音対話（非ASR+TTS）、跨アプリ自動操作
- 二代: 2026年Q2中〜下旬に予定

### Doubao-Seed-2.0 ベンチマーク
- **SuperGPQA**: GPT-5.2を上回る
- **IMO/CMO数学オリンピック金牌**
- **HLE-text**: 54.2点（人類の最終試験）、GPT-5.2・Gemini 3 Pro相当
- **Doubao-Seed-Code**: GPT-5を9項目で凌駕（Terminal-Bench 27% vs 13%、AI智能指数34 vs 22）
- **健康Bench**: 第一位
- **価格**: GPT-4比50倍安、業界平均比62.7%安

## 関連リンク

### 内部リンク
- [[seedance]] — ByteDance動画生成モデル
- [[marscode]] — 豆包MarsCodeコーディングアシスタント
- [[openclaw]] — ByteDance Agentプラットフォーム
- [[volcano-engine]] — 火山引擎
- [[coze]] — 扣子（ByteDance発ローコードAgentプラットフォーム）
- [[china-ai-agent-ecosystem]] — 中国Agentエコシステム全景

### 外部ソース
| ソース | URL | ティア | 概要 |
|--------|-----|--------|------|
| 豆包公式サイト | [doubao.com](https://www.doubao.com) | T1 | 製品ページ |
| 火山引擎/豆包大模型 | [volcengine.com/product/doubao](https://www.volcengine.com/product/doubao) | T1 | APIプラットフォーム |
| MarsCode | [marscode.cn](https://www.marscode.cn) | T1 | コーディングツール |
| Seedance 2.0 | [seed.bytedance.com](https://seed.bytedance.com) | T1 | 動画生成 |
| 知乎 — MarsCode紹介 | [zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/29175342477) | T2 | ユーザー評価 |
| 钛媒体 — Dola海外2億ダウンロード | [tmtpost.com/7955423](https://www.tmtpost.com/7955423.html) | T1 | 海外展開分析 |
| 新浪财经 — 豆包股回购 | [finance.sina.com.cn/jjxw/2026-04-16/doc-inhusenn4146654.shtml](https://finance.sina.com.cn/jjxw/2026-04-16/doc-inhusenn4146654.shtml) | T2 | 人材激励制度 |
| DataGlobeHub — Doubao指標比較 | [dataglobehub.com/zh/doubao-metrics](https://dataglobehub.com/zh/doubao-metrics/) | T2 | GPT-5対比ベンチ |