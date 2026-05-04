---
title: "混元 (Hunyuan) — 騰訊自研の大規模言語モデルシリーズ"
created: 2026-04-28
updated: 2026-05-04
tags: [company, llm, china, tech-giant, tencent, moe, multimodal]
aliases: ["Hunyuan", "混元", "Tencent Hunyuan", "腾讯混元", "HY"]
source_lang: zh-CN
---

# 混元 (Hunyuan) — 騰訊自研の大規模言語モデルシリーズ

> **開発元**: Tencent（騰訊）
> **首席AI科学家**: 姚順雨（Yao Shunyu、元OpenAI研究員）
> **最新モデル**: Hy3 Preview（2026年4月） / HY 2.0（2025年12月）
> **アーキテクチャ**: 混合專家（MoE）、快慢思考融合
> **重要度**: 高 — 騰訊AI生態全系の「底座（基盤モデル）」

## 概要

**混元（Hunyuan）**はTencentが全チェーン自研する大規模言語モデルシリーズ。2026年4月時点、腾讯元宝（C端AIアプリ）、WeChat検索、CodeBuddy、WorkBuddy、QQ、腾讯文档など腾讯エコシステム全域に統合されている。2025年末に姚順雨（元OpenAI研究員）が首席AI科学家としてLLMチームとAI Infraを再編し、「実用主義」路線に転換。2026年4月のHy3 Preview公開でオープンソースコミュニティにも参入した。

## モデル系譜

| バージョン | リリース | アーキテクチャ | パラメータ | 特徴 |
|-----------|---------|---------------|-----------|------|
| **Hunyuan-T1** | 2025年8月 | Mambaベース推論モデル | 超大型 | 腾讯初の旗幟推理モデル、32K入力/64K出力 |
| **HY 2.0 Instruct** | 2025年12月 | MoE | 406B総 / 32B活性 | 快思考モデル、128Kコンテキスト、文創写作に強み |
| **HY 2.0 Think** | 2025年12月 | MoE | 406B総 / 32B活性 | 深度思考モデル、128K入力/64K出力、数理・コード・Agentに強み |
| **Hunyuan-A13B** | 2025年6月 | MoE | 13B | 混元初の混合推理モデル、224K入力、Agent能力向上 |
| **Hy3 Preview** | 2026年4月23日 | MoE（快慢思考融合） | **295B総 / 21B活性** | 256Kコンテキスト、MTP Layer 3.8B、192 Experts（top-8活性） |
| **Hy3.0（正式版）** | 開発中 | MoE | 未公開 | Hy3 Previewのフィードバックを反映した正式版 |

## Hy3 Preview（2026年4月）— 最新詳細

### 技術仕様
- **総パラメータ**: 295B（MoE）
- **活性パラメータ**: 21B（推論時に実際に使用されるパラメータ）
- **Experts**: 192（top-8活性化）
- **コンテキスト長**: 最大256K
- **MTP Layer**: 3.8B（Multi-Token Prediction）
- **推論効率**: 前代比40%改善（同等精度で少ないトークン消費）
- **ライセンス**: オープンソース（GitHub / HuggingFace / ModelScope）
- **サービング**: vLLM / SGLang対応、OpenAI互換API

### ベンチマーク性能
| ベンチマーク | Hy3 Preview | 備考 |
|-------------|------------|------|
| **SWE-bench Verified** | 74.4% | Claude Opus 4.6は80.8%（追従圏） |
| **Terminal-Bench 2.0** | 54.4% | コードAgentタスク |
| **BrowseComp** | 競争力あり | 検索Agentタスク |
| **WideSearch** | 競争力あり | 検索Agentタスク |
| **IMO-AnswerBench** | 国内トップクラス | 国際数学オリンピック |
| **HMMT2025** | 国内トップクラス | ハーバード・MIT数学コンテスト |
| **HLE（Humanity's Last Exam）** | 大幅改善 | 汎化性テスト |
| **ARC-AGI** | 大幅改善 | 汎化AI推論 |

### 3つの核心突破方向
1. **複雑コンテキスト処理**: CL-bench及びCL-bench-Lifeで上下文学習と指令追随を評価
2. **複雑推論**: FrontierScience-Olympiad、IMO、清華大学数学博士試験などで高スコア
3. **コードとAgent**: SWE-bench、Terminal-Benchで実運用レベルの能力を獲得

## 価格戦略

| プラン | 入力価格 | 出力価格 | 備考 |
|-------|---------|---------|------|
| **従量課金（最低）** | ¥1.2/百万tokens | ¥4.0/百万tokens | 業界最安クラスの定价 |
| **TokenPlan（個人）** | ¥28/月〜 | — | 高頻度ユーザー向け |
| **QClaw海外版ベータ** | 1日4,000万token無料 | — | 最大$700/日の価値 |

## 製品統合状況

### 既に統合済み
- **腾讯元宝**（C端AIアプリ、主力モデルにHy3 Previewを採用）
- **腾讯云TokenHub**（APIサービス）
- **ima**（腾讯ナレッジプラットフォーム）
- **CodeBuddy** / **WorkBuddy**（開発者・企業ツール）
- **QQ** / **QQブラウザ** / **腾讯文档** / **腾讯乐享**

### 統合進行中
- **WeChat公众号**（WeChat公式アカウント）
- **和平精英**（ゲーム）
- **腾讯新闻** / **腾讯自选股** / **腾讯客服** / **微信读书**
- **微信Agent**（噂 — WeChatネイティブAIアシスタント）

## 組織再編と姚順雨のリーダーシップ

2025年末、TencentはAI研究開発体制を抜本的に再編：
- **姚順雨**（前OpenAI研究員）を首席AI科学家に任命、LLMチームとAI Infraを統括
- AI Labの主力メンバーを混元チームに統合、分散していたリソースを集約
- 「算力・データ・アルゴリズム」をAI Infraに一元管理
- 混元を「会社級底座（企業レベル基盤）」に格上げ

姚順雨の哲学：「モデルの価値はベンチマークスコアではなく、実際のワークフローでどれだけ使えるか」。AGI-NEXT峰会で「最高のモデルは月額$200で売れる。多くのユーザーは最高のモデルにプレミアムを支払う用意がある」と発言。

## 競合比較

| モデル | 開発元 | パラメータ | 特徴 |
|--------|--------|-----------|------|
| **Hy3 Preview** | Tencent | 295B/21B活性 | 実用主義、Agent最適化、¥1.2/百万tokens |
| **ERNIE 5.0** | Baidu | 2.4T MoE | 原生全模態、SOTAベンチマーク |
| **Qwen3.5** | Alibaba | 多种 | フルスタック、OSSリーダー |
| **GLM-5** | Zhipu AI | 744B MoE | SWE-bench 77.8、オープンソース |
| **Kimi K2.6** | Moonshot | 1T/384 Experts | SWE-Bench Pro 58.6% |
| **DeepSeek-R1** | DeepSeek | 671B MoE | 推論特化、オープンソース |
| **Claude Opus 4.7** | Anthropic | 非公開 | 推論スケーリング、SWE 80.8% |
| **GPT-5.5** | OpenAI | 非公開 | 最新フラグシップ |

## 2026年4月最近の動向

### OpenRouter API呼び出し量No.1（2026年4月29日）

4月29日、OpenRouterが発表した最新の全球大模型API呼び出し量ランキングで、Hy3 Previewが総合1位を獲得。ツール呼び出しで1位、コーディングで2位。DeepSeek V4の大量安価なAPIトラフィックを上回る実績で、実際の業務ワークロードでの浸透度を示した。

### Hy3 Preview、数字中国建設峰会に登場（2026年4月29日）

4月29日、第九届数字中国建設峰会（福州）でHy3 previewが実機展示初披露。WorkBuddy（1分でWeChat Work接続可能なデスクトップAgent）、QClaw（OpenClawベースConsumer Agent、Hermes対応、Hy3 preview + DeepSeek V4-Pro切り替え対応）が出展。腾讯が「会話から実行へのパラダイム遷移」をテーマにAgent生態を展示。WorkBuddy/QClaw/軽量OpenClaw/云桌面Claw/ClawProの5製品が中国信通院「安全体検」認証を首批通過。AI Skills社区「SkillHub」も発表。

### 和平精英AI NPCへの統合

Hy3 Previewは騰訊の人気ゲーム「和平精英（PUBG Mobile）」にも統合され、ゲーム内のAI NPC（ノンプレイヤーキャラクター）として動作。姚順雨の「モデルは刷榜（ベンチマーク追及）ではなく実業務で価値を出す」哲学を体現。

### 組織再編の詳細

姚順雨の指導下で混元組織は以下の5大ブロックに再編:
1. **事前訓練** - 基盤モデルの訓練
2. **事後訓練** - SFT/RLパイプライン
3. **ベースラインInfra** - 万卡クラスタ安定運用
4. **モデル評価** - 自社構築50以上の実業務評価ベンチマーク（業界標準ベンチマークを放棄し実業務に特化）
5. **Frontier** - 先端技術探索・予備研究

また、ByteDance・Alibaba・DeepSeek・Kimiから核心人材を大量に獲得。姚順雨は特にAGI信仰が強く技術実力のある若手人材を好み、多数の校招生・インターンを起用。

### 今後の展望

- **Hy3.0正式版（クローズドソース旗艦）**: 2026年5〜6月にリリース予定。Hy3 Previewより大幅に大規模なモデル
- **価格戦略**: 月額28元〜の個人プランなど、同級MoEモデル中最低価格帯を維持
- **内製Inference**: 50多種の実業務評価Benchmarkを独自構築し、本来の性能評価を実現

## 課題と展望

### 課題
- **C端での存在感**: 元宝でDeepSeekと混元が併存、混元単独でのブランディングが課題
- **微信Agent未発表**: 13億ユーザーのWeChat×AIは最大の潜在力だが、まだ「噂」段階
- **最高精度での差**: SWE-benchでClaude Opus 4.6に6.4ポイント差

### 展望
- 2026年下期にHy3.0正式版リリース予定
- WeChatエコシステムへの全面統合が実現すれば、中国最大のAIユーザーベースを獲得
- OpenClaw/QClawとの連携でAgentエコシステムを拡大中

## 関連

- [[tencent-ai]] — 親組織のAI戦略
- [[tencent-qclaw]] — 混元ベースのAgent製品
- [[openclaw]] — QClawのベースとなったオープンソースフレームワーク
- [[baidu-ernie]] — 競合：百度のERNIEシリーズ
- [[qwen]] — 競合：AlibabaのQwenシリーズ
- [[deepseek]] — 競合：DeepSeek（元宝に一時採用されたモデル）
- [[china-ai-superapp-race]] — 中国AIスーパーアプリ競争

## ソース

- [混元Hy3 Preview公式リリース（2026-04-23）](https://hy.tencent.com/hy3-preview)
- [腾讯云 HY 2.0 API ドキュメント](https://developer.cloud.tencent.com/article/2598835)
- [混元Hy3 preview技術仕様 — 字母AI](https://www.sohu.com/a/1013810561_116132)
- [Tencent QClaw海外版ベータ発表 — Tencent公式](https://www.tencent.com/en-us/articles/2202318.html)
- [HuggingFace Hy3 Preview評価](https://huggingface.co/tencent/Hunyuan-Hy3-Preview)
- [东方财富 — 混元HY3.0商用分析](https://wap.eastmoney.com/a/202604243717921415.html)
