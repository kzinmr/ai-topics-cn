
## [2026-04-26] tongyi-lab-update | 通义实验室 (Tongyi Lab) 詳細追加

### 更新ページ（1件）

1. **entities/qwen.md** — 通义实验室セクション追加:
   - **沿革**: iDST (2014) → 达摩院 (2017) → 通义实验室 (2022) → M6プロジェクト (10兆パラメータ)。
   - **2026年4月組織再編**: 通义大模型事业部へ昇格。周靖人 (Zhou Jingren) を責任者に迎えた集团技术委员会 (Eddie Wu議長) の設立。
   - **研究アウトプット**: DeepResearch, Qwen-Agent, FunAudio, Qwen3-VL-Embedding (2026年1月)。

## [2026-04-26] entity-update-01 | Qwen — AlibabaのAI戦略大幅更新

### 更新ページ（1件）

1. **entities/qwen.md** — 大幅更新（Alibaba AI戦略 + Qwen3.6市場影響）:
   - **3800億元（$69B）3か年AI投資計画**の詳細追加
   - **Zhenwu AIチップ**: 中国电信と10,000チップデータセンター（広東省韶関市）、計画スケール100,000チップ
   - **フルスタック4層垂直統合**（シリコン→クラウド→モデル→アプリケーション）の構造図追加
   - **S字カーブ分析**: AlibabaのAI投資はS字カーブ早期段階、$200 vs $100株価予測
   - **Qwen3.6-Plus**詳細追加: agentic coding最適化、1Mコンテキスト、397B MoE（17B active）、Terminal-Bench 65.4%
   - **Qwen3.6-Max-Preview**詳細: 五大核心升级、6項ベンチマークでPlusを超越
   - **Qwen3.6-27B**詳細追加: denseモデル、SWE-bench Verified 77.2%、Terminal-Bench 2.0 59.3%（Opus 4.6と同等）、Thinking Preservation機能
   - **Qwen3.6-35B-A3B**詳細: sparse MoE、262K context、Claude Opus 4.7の~82%
   - **Qwen3-Coder**追加: 480B MoE / 35B active
   - **中国AIスーパーアプリ競争**（3Way: Alibaba vs ByteDance vs Tencent）の表追加
   - **価格競争**: Qwen3-Max 50%値下げ
   - **具身ロボティクス**: ABot-Worldモデル、Humanoid Robot Half Marathonデビュー
   - **関連リンク**: alibaba-cloud追加、外部ソース6件追加（Bitget, Simply Wall St, Silicon Report）

## [2026-04-26] active-crawl-02 | DeepSeek V4正式リリース / Qwen3.6シリーズ / Coze 2.5 — 3ページ更新

### 更新ページ（3件）

1. **concepts/deepseek.md** — 大規模更新（2026年4月24日V4リリース対応）:
   - DeepSeek-V4正式リリース日: 2026年4月24日（V4 Preview）
   - ベンチマーク詳細追加: MMLU 93.9、HumanEval 96.2、SWE-bench Verified 92.3、AIME 90.7、GPQA-Diamond 96.4
   - SWE-bench Verified 92.3%がClaude Opus 4.6 (80.9%)を大幅上回ることを明記
   - Webインターフェース新機能: 高速モード（快速模式）+ 専門家モード（专家模式）
   - mHC + Engramアーキテクチャの詳細をV4セクションに統合（既存セクションを削除、V4サブセクションに統一）
   - 核心人材流動: 羅福莉→Xiaomi、郭达雅→ByteDance
   - 2026年Q1大モデル資金調達前年比72%減少の追記
   - 価格戦略: $0.30/MTok推定

2. **concepts/qwen.md** — Qwen3.6シリーズ追加（2026年4月24日〜25日）:
   - Qwen3.6-Max-Preview: 旗舰预览版、preserve_thinking機能追加（DeepSeek-V4 Deep Thinkingに対抗）
   - Qwen3.6-Plus: 视觉语言モデル。Vibe Coding体験大幅改善
   - Qwen3.6-Flash: 高速・低成本定位。数学・コード推理・空間知性強化
   - Qwen3-VL-Plus: 视觉理解特化。空間認知・マルチモーダル思考強化
   - Qwen3-Coder: 235B（MoE 30B活性化）、119言語、36兆token訓練データ、混合思考模式
   - Qwen3.5-Plus: MMLU-Pro 87.8（GPT-5.2超）、GPQA 88.4（Claude 4.5超）、IFBench 76.5
   - 累計オープンソースモデル400+、グローバルダウンロード10億回突破、衍生モデル20万+
   - Qwen3.5の価格: 0.8元/MTok（約0.11ドル）

3. **concepts/coze.md** — Coze 2.5リリース対応（2026年4月）:
   - Coze 2.5正式リリースを明記
   - Agent World機能の詳細: 云电脑+云手机、7×24运转、技能商店、独立身份+长期记忆、多渠道连接
   - 扣子罗盘（Coze Compass）新ツール追加
   - OpenClaw Studioのオープンソース化詳細
   - 扣子编程の詳細（前端: React/Vue、后端: Node.js/Python、DB: MySQL/MongoDB/PostgreSQL）
   - WeChat統合教程（知更Ai）を維持

### hot-topics.yaml更新
- deepseek: last_crawled 2026-04-23 → 2026-04-26
- qwen: last_crawled 2026-04-23 → 2026-04-26
- coze: last_crawled 2026-04-22 → 2026-04-26

### メディアトレンド分析

**🔥 DeepSeek V4正式リリース — 最大のトレンド**

2026年4月24日、DeepSeekがV4 Previewを正式リリース。主要36kr記事（13+件）で以下が報じられた：

| メディア | 記事タイトル | 視点 |
|----------|-------------|------|
| 鏡相工作室 | 「DeepSeek-V4发布，黄仁勋的担忧成真了」 | NVIDIA依存からの脱却の現実化 |
| NEXT趋势 | 「黄仁勋说这是"灾难"：DeepSeek在华为芯片上跑通」 | 昇騰エコシステムの成熟 |
| 新立场pro | 「DeepSeek V4、GPT5.5会师：通向AGI的门票只有Coding？」 | AGI論争 |
| 硅基星芒 | 「DeepSeek-V4：中国AI应用寒武纪大爆发奇点降临」 | 新時代宣言 |
| 机器之心 | 「翻完DeepSeek报告，我们发现了中国AI的默契」 | 産業分析 |
| 豹变 | 「DeepSeek V4背后，梁文锋的转身」 | 企業戦略分析 |

**SWE-bench Verified 92.3%**はClaude Opus 4.6の80.9%を11.4ポイント上回り、コーディング能力で業界新記録。

**36krの論調**: 産業インパクト重視。「成本暴降73%」「寒武紀大爆发の奇点」と超肯定的。昇騰910C対応を中国AIの自立象徴として強調。

**V2EXの反応**: 「V4变强了，但是也太贵了」— コスト/実利用者の現実感ギャップが顕在化。

**Juejinの実測**: 「夯爆了还是拉完了？」結果は「夯爆了」（非常に強力）。OpenClawとの比較で「体验完阿里悟空，想把龙虾换掉了」。

**Coze 2.5 + Agent World**: ByteDanceのAgentプラットフォームが「满配就位，不止Claw」スローガンでデジタル存在の時代へ。扣子编程（Coze Programming）で全栈開発を自然言語で実現。

### Wiki統計
- **Entity Pages**: 38
- **Concept Pages**: 64（+0 — 更新のみ）
- **Comparison Pages**: 1
- **Total Pages**: 103
- **Last Updated**: 2026-04-26

---

## [2026-04-26] cn-media-analysis | DeepSeek V4波及 / Token価格転換 / 阿里悟空

### チェックポイント: 20260426T091413Z（自動トリアージ失敗）
- **収集数**: V2EX:15, Juejin:15, 36kr:15+, WeChat:10+（daily-digestベース）
- **Triage decisions**: ✅Take:1 / ⚠️Reference:0 / ❌Skip:10+（JSONパースエラーのため不完全）

### Take処理済み
| アイテム | ソース | Wiki更新 |
|----------|--------|---------|
| Codex agentic loopコード膨張 | V2EX (#1208629) | `entities/deepseek.md` に統合（既存のCodexセクション） |

### Wiki更新（本レポート）
| ページ | 種別 | 更新内容 |
|--------|------|----------|
| `concepts/token-pricing-trend.md` | **新規** | Token価格上昇トレンドの包括的分析（計算力インフレ、按量计费移行、Copilot Opus排除） |
| `concepts/wukong.md` | **新規** | 阿里悟空（Wukong）企業級AIエージェントプラットフォーム（RealDoc、OPTスキル、セキュリティ） |
| `entities/deepseek.md` | **更新** | 36kr 15+件のV4関連記事を反映（梁文锋の转身、中国AIの默契、华尔街反応、GLM-5比較等） |
| `concepts/coding-plan.md` | **更新** | Wukong関連情報追記、トークン価格トレンドへの参照追加 |
| `index.md` | **更新** | エンティティ:38, コンセプト:79（+3）, 最新更新追記 |

### メディアトレンド分析概要

**1. DeepSeek V4正式リリース — 最大のトレンド**

2026年4月24日、DeepSeekがV4を正式リリース。主要36kr記事で15件以上言及。
- **SWE-bench Verified 92.3%**: Claude Opus 4.6 (80.9%) を11.4ポイント上回るコーディング能力
- **昇騰950対応**: 「黄仁勋说这是"灾难"」— 中国AIの自立象徴
- **3モデル同時アップデート**: GPT-5.5 / Opus 4.6 / DeepSeek V4が相次ぎリリース

**2. Token価格上昇トレンド — 計算力インフレの顕在化**

Juejinで「天下苦Token久矣」。主要サービスの価格転換：
- Copilot: Opus 4.5/4.6/4.7を全削除
- Qwen: パッケージ→按量计费（従量課金）移行
- GLM: 非コード使用制限
- Windsurf: $15→$20（直接値上げ）
- 阿里云/百度/腾讯云: AI算力产品5%-34%値上げ

**3. 阿里悟空（Wukong）— 企業級AIエージェント**

钉钉が2026年3月にリリースした企業級AIネイティブ作業プラットフォーム。
- OpenClawのセキュリティ問題（39万サイト公開）に対する代替として注目
- RealDocファイルシステム（外科手術的精准操作）
- 10のOPT（一人チーム）スキルセット
- 钉钉全面CLI化（AI钉钉 2.0）

### ソース間温度差

| トピック | V2EX（開発者視点） | 36kr（ビジネス視点） | 温度差 |
|----------|-------------------|---------------------|--------|
| **DeepSeek V4** | 「V4变强了，但是也太贵了」 | 「成本暴降73%」 | 🔴大 |
| **Token価格** | 「一个月多少token」— コスト意識 | 産業分析に集中 | 🟡中 |
| **昇騰950** | 実使用感ベース | 「黄仁勋灾难」 | 🟢小 |

### 新興トレンド

- **豆包2.0/豆包MarsCode**: Juejinで「中国版Trae免费用」として紹介
- **阿里悟空（MCP）**: Juejinで「体验完阿里悟空，想把龙虾换掉」
- **CopilotのOpus排除**: Juejin/V2EXで「Copilot下架opus」
- **Token価格上昇**: Juejinで「人还比Token便宜吗？」
- **GPT-Image-2生图**: V2EXで多数の実測報告

### 中国特有トレンド指標

| 指標 | 状態 | 説明 |
|------|------|------|
| **価格戦** | 🔴激化 | 「Token涨价」「一个月多少token」 |
| **开源熱度** | 🟡安定 | GLM-5开源のみ。DeepSeek V4は閉源 |
| **出海指数** | 🟢上昇 | GPT-5.5無料使用方法の共有 |
| **监管温度** | 🟠上昇 | 支付宝の余额宝/花呗規制新方針 |
| **国产替代度** | 🟡中 | 豆包2.0、阿里悟空、GLM-5 |
| **昇騰エコシステム** | 🟢上昇 | 「黄仁勋灾难」言説 |

---

# Wiki Log

Chronological record
## [2026-04-25] triage-11 | DeepSeek V4「寒武纪大爆发」、Codex SSH透明性、昇騰エコシステム

### インボックス状況
- **checkpoint**: 20260425T090223Z (ok=true)
- **総カウント**: v2ex:15, juejin:15, 36kr:13, wechat:15, newsletters:64, daily_digests:11

### 処理結果
- **take**: 4件（Codex SSH透明性、GPT 6.0待機議論、低价GPT脆弱性、daily-digest-2026-04-25）
- **reference**: 2件（Deep Research効果、Plusユーザー体験）
- **skip**: 9件（WeChat stale Sogou検索:2017〜2023年旧記事、Juejin stale:2023年旧記事）

### Wiki更新
| ページ | 更新内容 |
|--------|---------|
| `pages/industry-trends.md` | **Section 1.5 新規**: DeepSeek V4リリース（36kr 13+本記事一覧）、昇騰（Ascend）エコシステム進展、中国AI「寒武纪大爆发」。CodingPlan/阿里悟空/GLM-5/V2EX DeepSeek V4市場影響を追記 |
| `concepts/gpt.md` | 低価格GPT脆弱性議論確認済み（V2EX #1207040） |
| `pages/openai-codex-infrastructure.md` | SSH「偷偷加了」透明性懸念確認済み |
| `index.md` | ページセクション新規作成、ダイjest 2026-04-25追記、raw articles追記 |

### メディアトレンド分析

**🔥 DeepSeek V4 — 最大級のトレンドトピック**

36krでは13本以上の記事がDeepSeek V4関連で発表され、中国AIコミュニティで**最大級のトピック**となった。主な報道ライン：

| メディア | 記事 | 視点 |
|----------|------|------|
| 鏡相工作室 | 「DeepSeek-V4发布，黄仁勋的担忧成真了」 | NVIDIA対抗の現実化 |
| NEXT趋势 | 「黄仁勋说这是\"灾难\"：DeepSeek在华为芯片上跑通」 | **昇騰エコシステム**進展 |
| 新立场pro | 「DeepSeek V4、GPT5.5会师：通向AGI的门票只有Coding？」 | AGI論争 |
| 硅基星芒 | 「DeepSeek-V4：中国AI应用寒武纪大爆发奇点降临」 | **中国AIの新時代**宣言 |
| 最话FunTalk | 「不只DeepSeek，大厂都想\"抛弃\"英伟达」 | **去NVIDIA化**の潮流 |

**昇騰（Ascend）エコシステムの進展：**

黄仁勲（ジェン・ハーン）が「灾难」と表現した事実は、**DeepSeekが華為昇騰チップ上で正常に動作した**ことを意味する。これは以下の点で重要：

1. **NVIDIA依存からの脱却** — 中国AI企業が開発モデルを昇騰エコシステムにポート可能
2. **地政学的リスク低減** — 米中貿易摩擦によるGPU輸出制限の影響を緩和
3. **昇騰ハードウェアの成熟** — 実際のモデル動作検証により昇騰エコシステムの信頼性向上

**掘金的な新着トピック：**

- **DeepSeek V4 + Claude Code実測** — 「夯爆了还是拉完了？」結果は「夯爆了」（非常に強力）
- **GLM-5开源** — 「让高级程序员也危险了…」コード生成能力が高級プログラマーの仕事を脅かす可能性
- **阿里「悟空」MCP** — 「我想把电脑里的龙虾换掉了」Codex代替の有力候補
- **Claude Code 32 Skills + 8 MCP** — 「别再裸用Claude Code了！」実装ガイド

**Codex Appの透明性懸念：**

V2EXで「**以防你不知道 Codex App 偷偷加了 SSH 远程开发功能**」（V2EX #1207253）が報告された。「偷偷加了」（内密に追加）はOpenAIの透明性問題の新たな事例として重要。

**V2EXコミュニティの温度：**

- GPT-6.0待機議論：「gpt 6.0 到底什么时候发布呀」— 毎日のように噂が流れるがActualなリリースなし
- 低价GPT脆弱性：「怎么封了还有」— OpenAIが脆弱性を封じても新たな抜け道が発見される「猫と鼠」ゲーム

### ソース間温度差

| トピック | V2EX | 掘金 | 36kr |
|----------|------|------|------|
| DeepSeek V4 | 市場影響予測（美股冲击） | 実測評価（夯爆了） | 戦略分析・新時代宣言 |
| GPT 6.0 | 公開時期への不満・期待 | — | 公式発表待ち |
| CodingPlan/阿里悟空 | — | 実測「真NB」 | — |
| 低价GPT | セキュリティ脆弱性 | Token価格議論 | — |

### 新着信号（daily-digest-2026-04-25）

58件の収集候補を確認。実質的な新着信号は以下の通り：
- **V2EX**: Codex SSH、GPT 6.0待機、低价GPT脆弱性、DeepSeek V4美股冲击予測
- **掘金**: DeepSeek V4実測、GLM-5开源、阿里悟空MCP、Claude Code 32 Skills
- **36kr**: DeepSeek V4関連13本記事、黄仁勲「灾难」発言、中国AI「寒武纪大爆发」
- **WeChat**: 大半がstale Sogou検索アーティファクト（2017〜2023年）

### 中国特有の動向

- **昇騰エコシステム**: DeepSeekが华为昇騰チップ上で動作 — NVIDIA依存からの脱却が現実的な選択肢に
- **国産モデル競争**: Qwen/Kimi/GLM/DeepSeekの多角的競争が「寒武纪大爆发」状態
- **Token価格戦**: 阿里云CodingPlanの按请求计费、Qwen按量计费 — Tokenコスト競争が激化

---

## [2026-04-24] triage-10 | GPT-5.5正式評価・DeepSeek V4・MCPセキュリティ更新

### インボックス状況
- **checkpoint**: 20260424T042656Z (ok=true)
- **総カウント**: 36kr:109, juejin:215, v2ex:411, wechat:106, newsletters:63, daily_digests:10

### 処理結果
- **take**: 4件（Codex SSH, 低价GPT漏洞, GPT 6.0待機, 试用的路子）
- **reference**: 2件（Deep Research効果, Plusユーザー体験）
- **skip**: 4件（LangChain旧記事, LLM入門旧記事, 学習ルート記事, LLM安全入門旧記事）

### Wiki更新
| ページ | 更新内容 |
|--------|---------|
| `concepts/gpt.md` | GPT-5.5正式評価（全榜第一・Opus 4.7圧倒）、GPT 6.0待機議論追記 |
| `concepts/mcp-security.md` | GPTサブスクリプション脆弱性問題、Codex SSH機能の透明性懸念追記 |
| `entities/deepseek.md` | DeepSeek V4正式リリース、华为昇騰協業、GPT5.5/Opus4.6/V4同時アップデート追記 |
| `pages/openai-codex-infrastructure.md` | SSH远程开发機能のV2EX発見日追記 |

### メディアトレンド分析
- **GPT-5.5 vs Opus 4.7**: 36krが「更强更快更贵」と報じ、GPT-5.5が全榜第一でOpus 4.7を圧倒。V2EXはコスト増懸念
- **DeepSeek V4**: 华为昇騰協業で国産モデルの地位確立。昇騰适配がV4の遅延要因との推測
- **GPT 6.0待機**: V2EXでOpenAIのリリースペースへの不満が顕在化
- **ソース間温度差**: V2EX（実使用感・コスト）vs 36kr（戦略的意義・性能）で明確な乖離

## [2026-04-24] triage-09 | OpenClaw/MCPセキュリティ記事の確認

### インボックス状況
- **checkpoint**: 20260424T042656Z (ok=true)
- **総カウント**: 36kr:109, juejin:215, v2ex:411, wechat:106, newsletters:63, daily_digests:10

### 処理結果
- **take**: 1件（OpenClaw/MCPセキュリティ）→ **既に取り込み済み**。既存wiki `concepts/mcp-security.md` に統合済み、raw記事も `index.md` 参照済み
- **wiki新規**: 0 / **wiki更新**: 0
 of wiki operations.

## [2026-04-24] triage-08 | 概念ページ5件新規作成 — GPT, 多模态, 量化, 微调, RLHF/对齐

### インボックス状況
- **inbox/v2ex/**: トレンド集計済み（2026-04-10〜24、59日分）
- **inbox/juejin/**: トレンド集計済み
- **inbox/36kr/**: トレンド集計済み
- **inbox/wechat/**: トレンド集計済み

### trending-topics分析結果（2026-04-10〜24、59日分）

| # | トピック | 言及数 | 変化 | 対応 |
|---|---------|--------|------|------|
| 1 | Claude | 106 | 安定 | 既存entity更新済み |
| 2 | AI Agent/智能体 | 111 | ↑ | 既存concept更新済み |
| 3 | GPT | 74 | ⬆️ 上昇 | **新規concept** |
| 4 | 量化/Quantization | 59 | ⬇️ 低下 | **新規concept** |
| 5 | 微调/Fine-tuning | 59 | ⬇️ 低下 | **新規concept** |
| 6 | RLHF/对齐 | 59 | ⬇️ 低下 | **新規concept** |
| 7 | 多模态/Multimodal | 44 | ⬆️ 上昇 | **新規concept** |
| 8 | MCP | 42 | ⬆️ 上昇 | 既存concept |
| 9 | Gemini | 39 | 安定 | 既存entity |
| 10 | Cursor | 35 | 安定 | 既存entity |
| 11 | DeepSeek | 32 | 安定 | 既存entity |
| 12 | Vibe Coding | 31 | 安定 | 既存concept |
| 13 | ChatGLM | 30 | 安定 | 既存entity |
| 14 | Llama | 27 | 安定 | 既存entity |
| 15 | OpenClaw | 25 | 安定 | 既存entity |

### 新規作成ページ

| ページ | 種別 | 言及数 | 主要トピック |
|--------|------|--------|-------------|
| `concepts/gpt.md` | Concept | 74 | GPT-5.5漏洩、ChatGPT Images 2.0、GPT Pro速度4倍、Codex統合 |
| `concepts/quantization.md` | Concept | 59 | GGUF/GPTQ/AWQ、FP8/FP4新規格、GPU Cloud、HuggingFace Hub |
| `concepts/fine-tuning.md` | Concept | 59 | LoRA/QLoRA、Axolotl、Unsloth、TRL、GRPO微调 |
| `concepts/rlhf-alignment.md` | Concept | 59 | RLHF/DPO/GRPO、安全对齐、中国規制 |
| `concepts/multimodal.md` | Concept | 44 | GPT Image 2.0、Sora/Kling、Qwen3.5 VL、多模态理解 |

### trending-topicsの主要イベント（GPT, 多模态, 量化, 微调, RLHF/对齐）

#### GPT関連（74言及）
- **GPT-5.5漏洩事件（04-23）**: Codex内部テスト環境からGPT-5.5、「风速狗（Arcanine）」「海森堡」「Glacier」がリーク。Sam Altmanの「Transformerを超えるアーキテクチャ」発言と相まって巨大話題
- **ChatGPT Images 2.0（04-22）**: GPT-5の生図能力がChatGPTに統合。Nano Bananaを凌駕、デザイナー業界に衝撃
- **GPT Pro速度4倍（04-20）**: 「神级操作」で速度向上、GPT-5.5早期説浮上
- **Codex重构（04-15）**: GPT-5.4 HarnessがCodexに7つのサンドボックスとして統合
- **GPT低価格サブスク**: アングラ流通サブスクが公式に露見、V2EXで大炎上
- **GPT vs Claude Opus 4.6（04-16）**: コーディング比較でGPT-4oがClaudeに劣る報告
- **GPT Images生图性能（04-18）**: V2EXで「gpt-image-2 生图确实很顶啊」

#### 多模态関連（44言及）
- **GPT Image 2.0**: Nano Banana比較、大米刻字機能
- **Kling: 快手2026年最强视频生成**: 快手動画生成モデル
- **Sora vs Sora 2**: 動画生成進化
- **Sora 3D**: 3D動画生成
- **多模态AI産業応用**: 産業への統合
- **Qwen3.5 VL**: 通义千问のVision Languageバージョン
- **音频理解**: 音声理解技術
- **Sora**: OpenAI動画生成モデル
- **Qwen VL**: V2EX議論

#### 量化関連（59言及）
- **LLM推理优化**: 36krで推理最適化の包括的分析
- **GPU Cloud**: 中国GPUクラウドインフラ
- **GGUF/GPTQ**: ローカルLLM推論の主流フォーマット
- **FP8新規格**: 2026年の新量化形式

#### 微调関連（59言及）
- **微调: 从基础到高级**: 36krで微调の包括的解説
- **Qwen3.5微调**: 通义千问の社区微调
- **Qwen3.5 GRPO微调**: GRPOを活用した对齐
- **微调的産業応用**: 産業への適用
- **LoRA/QLoRA**: 低コスト微调手法

#### RLHF/对齐関連（59言及）
- **微调: 从基础到高级**: RLHF/DPO/GRPOの包括的分析
- **对齐: 安全与道德**: 安全对齐の議論
- **Qwen3.5 GRPO对齐**: GRPOを活用した对齐

### index.md更新
- 最終更新: 2026-04-23 → 2026-04-24
- エンティティ: 38 → 38
- コンセプト: 59 → 64（+5）
- 比較: 1 → 1
- 5新conceptリンク追加（gpt, quantization, fine-tuning, rlhf-alignment, multimodal）

### Wiki統計
- **Entity Pages**: 38（+0）
- **Concept Pages**: 64（+5: gpt, quantization, fine-tuning, rlhf-alignment, multimodal）
- **Comparison Pages**: 1（+0）
- **Total Pages**: 103（+5）
- **Last Updated**: 2026-04-24

## [2026-04-25] active-crawl-01 | アクティブ知識 crawl — 5ページ更新 + 新規作成

### 更新ページ（4件）
1. **china-ai-regulation.md** — 2026年4月新規定追加:
   - AI科技伦理审查与服务办法（试行）: 2026.04.02发布
   - AI拟人化互动服务管理暂行办法: 2026.07.15施行
   - テーブル形式統一（|| → |）

2. **coding-plan.md** — 阿里云 Coding Plan 最新比較追加:
   - Qwen-3.5 + Kimi-K2.5 + GLM-4.7 vs 火山云 Doubao-Seed-2.0-Code + GLM-4.7
   - リクエスト課金モデル vs 従量課金モデル比較
   - Claude Code顔認証強化で海外からCoding Plan需要急増

3. **chatglm.md** — GLM-5.1詳細追加:
   - GLM-5.1: 2000万Tokens無料登録、GLM Proプラン(120元/月)統合
   - z.aiプラットフォーム: MCP/RAG/智能体市场統合
   - GLM-5.1 codingベンチ: SWE-bench VerifiedでClaude Opus 4.5同等

4. **doubao.md** — 大規模追加（2026.04.16以降）:
   - Dola海外版累計2億ダウンロード突破（2026年Q1、7200万/单季）
   - 豆包股虚拟制度: 首次回购13.08美元（+30%）
   - Doubao-Seed-2.0 ベンチマーク: GPT-5を9基準で凌駕
   - 中国模型周间调用量2026年2月に米国モデルを初めて逆転（4.12万亿 vs 2.94万亿）

### 新規作成ページ（1件）
5. **china-ai-model-filing.md** — 大模型备案制度:
   - 大模型备案 + 大模型登记 + 算法备案 の3類型
   - 796款备案済み（2025.02時点）。北京225款で全国30%首位
   - 双备案制度、备案流程6ステップ詳細化
   - 2026年7月新標準施行

### hot-topics.yaml更新
- chatglm: last_crawled 2026-04-20 → 2026-04-25
- doubao: last_crawled 2026-04-21 → 2026-04-25
- coding-plan: last_crawled null → 2026-04-25
- china-ai-regulation: last_crawled 2026-04-21 → 2026-04-25
- china-ai-model-filing: last_crawled null → 2026-04-25

## [2026-04-15] init | Wiki initialized

Created wiki structure for Chinese-language AI topics monitoring.
Sources configured: V2EX, Juejin, 36kr, Zhihu, WeChat media.
Crawlers built and tested. Cron scheduling configured.

## [2026-04-15] triage-01 | 初回トリアージ — 5ページ作成

Originating conversation: cDIL7LE

### インボックス状況
- **inbox/v2ex/**: 40件（2026-04-15クロール分）
- **inbox/juejin/**: 32件
- **inbox/36kr/**: 21件
- **inbox/zhihu/**: 0件
- **inbox/wechat/**: 0件

### 趋势分析結果
`trending_topics.py --days 3` で19トピック検出。クロスソース（3ソース以上）トップ:
1. **Claude** — 42言及 (36kr+juejin+v2ex)
2. **AI Agent/智能体** — 21言及
3. **Anthropic** — 15言及
4. **GPT** — 11言及
5. **Cursor** — 10言及

### 作成ページ
| ページ | 種別 | 根拠 |
|--------|------|------|
| `entities/claude-code.md` | Entity | #1トレンド、42言及、Routines/Hooks/身分認証など多数の新展開 |
| `concepts/ai-agent.md` | Concept | #2トレンド、21言及、Harness概念の台頭 |
| `concepts/mcp.md` | Concept | 6言及、AI工程の基盤インフラとして重要性高 |
| `entities/glm-zhipu.md` | Entity | 中国発モデル、GLM-5(744B)オープンソース、実戦レビュー多数 |
| `concepts/harness-engineering.md` | Concept | 新興概念、arXiv 2604.08224の外化フレームワーク |

### 注目トピック（次回対応候補）
- Anthropic（身分認証問題の独立ページ化）
- DeepSeek（「早已变了」— 変貌の追跡）
- Cursor vs Claude Code比較
- Vibe Coding概念ページ
- Claude Mythos / OpenAI Spudの安全性議論

## [2026-04-22] triage-03 | 第3回トリアージ — 2ページ新規作成

Originating conversation: 定期Cron実行

### インボックス状況
- **inbox/v2ex/**: ~40件（04-22クロール分）
- **inbox/juejin/**: ~40件
- **inbox/36kr/**: 50件+
- **Newsletter**: ChinAI #347-354（04-18處理済み）、ChinAI #355（04-20、記事未取得）
- **Maildir**: 空（email-watcher処理済み）

### トレンド分析結果（04-22日次ダイジェスト51件）
1. **Claude Code** — 8件（Skills/MCP/封号論）
2. **DeepSeek** — 7件（設立後初の資金調達報道：100億估值・3億ドル）
3. **Kimi K2.6** — 4件（开源旗舰Agent軍団）
4. **Codex** — 3件（风评超過の声）
5. **GPT Images 2.0** — 2件（設計業界への影響）

### DeepSeek資金調達報道の文脈
36kr2件：
- 「DeepSeek的『下一步』」— 資金調達+商業化への転身
- 「梁文锋还是太保守了」— 100億估值3億ドルの報道解説

### 新規ページ作成
| ページ | 種別 | 根拠 |
|--------|------|------|
| `entities/kimi-k2-6.md` | Entity | K2.6开源旗舰Agent軍団指揮能力 |
| `entities/qwopus-3-5.md` | Entity | Qwen3.5-27B社区微调、Reasoning SFT |

### 既存ページ更新
| ページ | 更新内容 |
|--------|----------|
| `entities/deepseek.md` | トレンド順位6位へ上昇、04-22資金調達報道追加（トレンド15件） |
| `wiki/index.md` | エンティティ38に更新、kimi-k2-6追加 |

### Newsletter処理状況
- ChinAI #347-354: 04-18に処理済み（.eml/.mdファイルのみ存在、スクレイピングなし）
- ChinAI #355: 04-20着信、記事内容未取得
- blogwatcher DB: 未存在（スキップ）

## [2026-04-17] triage-02 | 第2回トリアージ — 4ページ新規作成、2ページ更新

Originating conversation: cDIL7LE

### インボックス状況
- **inbox/v2ex/**: 20件（2026-04-17クロール分）
- **inbox/juejin/**: 20件
- **inbox/36kr/**: 20件（16日・17日分）
- **inbox/zhihu/**: 0件
- **inbox/wechat/**: 0件
- **daily-digest**: 3件（04-15, 04-16, 04-17）

### 趋势分析結果
`trending_topics.py --days 3` で25トピック検出。前回（19トピック）から大幅増。

| # | トピック | 言及数 | 変化 |
|---|---------|--------|------|
| 1 | Claude | 117 | ↑↑ (前回42) |
| 2 | AI Agent/智能体 | 80 | ↑↑ (前回21) |
| 3 | GPT | 42 | ↑ (前回11) |
| 4 | Anthropic | 38 | ↑ (前回15) |
| 5 | MCP | 25 | ↑↑ (前回6) |
| 6 | Kimi/Moonshot | 11 | NEW |
| 7 | Vibe Coding | 7 | ↑ (前回5) |

### 主要イベント
1. **Claude Opus 4.7リリース** (04-16): SWE-bench 87.6%, CursorBench 70%達成
2. **Anthropic強制身分認証導入**: 政府ID+手持ち自撮りを要求、中国ユーザーに大打撃
3. **OpenAI GPT-5.4 Harness全面開放**: 7つのサンドボックスをネイティブ統合
4. **Harness投資ブーム**: 李開復・陸奇が重金入場
5. **中国Coding Plan需要急増**: Claude離脱組が国産プランに殺到

### 新規作成ページ
| ページ | 種別 | 根拠 |
|--------|------|------|
| `entities/claude-opus-4-7.md` | Entity | Opus 4.7リリース、身分認証問題、117言及の核心トピック |
| `entities/kimi-moonshot.md` | Entity | K2.5/K2.6がClaude代替として急成長、11言及 |
| `concepts/coding-plan.md` | Concept | 中国独自のAIコーディングサブスクモデル、市場構造の転換点 |
| `concepts/vibe-coding.md` | Concept | 7言及、Harness Engineeringの対極概念 |

### 更新ページ
| ページ | 更新内容 |
|--------|----------|
| `entities/claude-code.md` | Opus 4.7リリース・身分認証問題の反映、kimi-moonshot/coding-planリンク追加 |
| `concepts/harness-engineering.md` | GPT-5.4 Harness全面開放、李開復/陸奇投資、MiniMax事例、DeepAgents追加 |

### 次回対応候補
- DeepSeek（「早已变了」— 戦略転換の追跡）
- Qwen/通义千问（Qwen-3.5のCodingPlan統合）
- Cursor独立ページ（26言及）
- AI安全（Anthropic Nature論文「潜意識伝染」）

## [2026-04-17] triage-03 | 第3回トリアージ — 6ページ新規作成、2ページ更新

Originating conversation: Discord thread 1494586389843677287

### インボックス状況
- **inbox/v2ex/**: 15件（04-17クロール分）、約60件蓄積
- **inbox/juejin/**: 15件（04-17クロール分）、約55件蓄積
- **inbox/36kr/**: 12件（04-17クロール分）、約30件蓄積
- **inbox/zhihu/**: 0件
- **inbox/wechat/**: 0件

### 趋势分析結果（04-17 06:34時点）
`trending_topics.py --days 3` で26トピック検出。Claude言及が131件に増加（前回117件）、AI Agentも92件と急上昇。

| # | トピック | 言及数 | 変化 |
|---|---------|--------|------|
| 1 | Claude | 131 | ↑（117→131） |
| 2 | AI Agent/智能体 | 92 | ↑（80→92） |
| 3 | OpenClaw | 17 | NEW trending |
| 4 | Cursor | 28 | ↑（26→28） |
| 5 | AI安全 | 4 | NEW（Anthropic Nature論文） |
| 6 | LangChain | 5 | NEW（CVE-2026-4539） |
| 7 | RAG | 8 | 議論活発化 |
| 8 | DeepSeek | 9 | ↑（9→9） |
| 9 | Qwen/通义千问 | 11 | 安定 |
| 10 | Anthropic | 41 | ↑（38→41） |
| 11 | OpenAI | 40 | ↑（39→40） |

### 主要イベント
1. **Claude Opus 4.7続報** (04-17): 6ドルでMinecraftを作るデモ、OpenAI Codex「超级龙虾」と直接競合
2. **OpenAI Codex大更新**: 「Codex for almost everything」、Mac版超级龙虾、Harness全面開放
3. **Anthropic Nature論文**: 「潜意識伝染」— 合成データ時代の安全隐患を解明
4. **LangChain CVE-2026-4539**: プロンプト注入脆弱性、Agent越狱リスク
5. **OpenClaw 12類安全隐患**: MCPプロトコルの体系的脆弱性列表
6. **Anthropic KYC問題**: 強制身分認証で中国ユーザーアクセス制限

### 新規作成ページ
| ページ | 種別 | 根拠 |
|--------|------|------|
| `entities/openclaw.md` | Entity | 17言及、MCP安全問題の中心、Hermes Agentとの比較 |
| `entities/cursor.md` | Entity | 28言及、Opus 4.7のCursorBench 70%、IDE統合型ツール代表 |
| `concepts/ai-safety-subconscious.md` | Concept | Anthropic Nature論文「MCP安全隐患」、LangChain CVE |
| `concepts/open-source-death.md` | Concept | 4万Starプロジェクト閉源化、Mythosモデル抽出リスク |

### 更新ページ
| ページ | 更新内容 |
|--------|----------|
| `entities/claude-code.md` | Codex「超级龙虾」進化、1M Context議論、LangChain CVE-2026-4539追加 |
| `entities/claude-opus-4-7.md` | 04-17追加報道（6ドルMinecraft、OpenAI Codex競争、7億人就労者影響） |

### 関連ページ（Wiki外）
- `entities/deepseek.md` — 未作成（9言及。次回対応）
- `entities/openai.md` — 未作成（39言及。次回対応）
- `entities/anthropic.md` — 未作成（41言及。次回対応）

### 次回対応候補
- DeepSeek — 9言及、中国开源替代
- OpenAI entity — 39言及（GPT-5.4、Harness、超级龙虾）
- Anthropic entity — 41言及（Opus 4.7、身分認証、Nature論文）
- Qwen/通义千问 — 11言及
- LangChain concept — 5言及（CVE-2026-4539）
- RAG concept — 8言及（进化议论）

## [2026-04-17] triage-04 | 第4回トリアージ — 6ページ新規作成、index.md/log.md更新

Originating conversation: Discord thread 1494591317332721704

### インボックス状況
- **crawl_all.py**: 42アイテム収集（V2EX: 15, Juejin: 15, 36kr: 12）
- **trending_topics.py --days 3**: 26トピック検出
- Zhihu: 0件（403）、WeChat: 0件（API制限）

### 主要イベント
1. **Anthropic entity**: Opus 4.7、KYC問題、Nature論文を統合
2. **OpenAI entity**: Codex超级龙虾、GPT-5.4 Harness、競争分析
3. **DeepSeek entity**: 「算力通胀」パラドックス、戦略変貌
4. **Qwen entity**: Qwen3.5、Qwen3-Coder、阿里云統合
5. **LangChain concept**: CVE-2026-4539 Prompt Injection脆弱性
6. **RAG concept**: 「RAG过时了吗？」進化議論

### 新規作成ページ
| ページ | 種別 | 言及数 | 根拠 |
|--------|------|--------|------|
| `entities/anthropic.md` | Entity | 41 | #4トレンド、Anthropic全動向を統合 |
| `entities/openai.md` | Entity | 40 | #5トレンド、OpenAI全動向を統合 |
| `entities/deepseek.md` | Entity | 9 | 「算力通胀」議論の中心 |
| `entities/qwen.md` | Entity | 11 | 阿里云エコシステム中核 |
| `concepts/langchain.md` | Concept | 5 | CVE-2026-4539緊急セキュリティ |
| `concepts/rag.md` | Concept | 8 | RAG進化議論活発化 |

### 更新ページ
| ページ | 更新内容 |
|--------|----------|
| `index.md` | 新6ページ追加、トレンディングテーブル更新 |
| `log.md` | 本トリアージ記録追加 |

### Wiki統計
- **Entity Pages**: 10（+4）
- **Concept Pages**: 9（+2）
- **Comparison Pages**: 0
- **Total Pages**: 19（+6）
- **Last Updated**: 2026-04-17

### 次回対応候補
- Gemini/Google entity（30言及、セキュリティ問題あり）
- Llama/Meta entity（5言及）
- MiniMax entity（4言及）
- 文心一言/Baidu entity（4言及）
- 規制/コンプライアンス concept（5言及）
- Cursor vs Claude Code comparison page
- Claude Opus 4.7 追記（6ドルMinecraftデモ詳細）

## [2026-04-17] triage-05 | 第5回トリアージ — 3ページ新規作成、2ページ更新

Originating conversation: scheduled triage run

### インボックス状況
- **crawl_all.py 12:04実行**: 54アイテム収集（V2EX: 20, Juejin: 20, 36kr: 14）
- **trending_topics.py --days 3**: 28トピック検出（前回26→28）
- **WeChat**: 6件（復旦NLP Agent総説など）
- Zhihu: 0件（403継続）

### 趋势分析結果（04-17 12:00時点）
全体の言及数が大幅増加。Claude 146件、AI Agent 117件。WeChat含む4ソース横断トピックが増加。

| # | トピック | 言及数 | 変化 |
|---|---------|--------|------|
| 1 | Claude | 146 | ↑（131→146） |
| 2 | AI Agent/智能体 | 117 | ↑↑（92→117） |
| 3 | GPT | 56 | ↑（49→56） |
| 4 | Anthropic | 51 | ↑（41→51） |
| 5 | OpenAI | 46 | ↑（39→46） |
| 6 | Gemini/Google | 33 | ↑（30→33）**ページ新規作成** |
| 7 | Function Calling | 4 | **NEW** ページ新規作成 |
| 8 | Vector DB | 4 | **NEW** ページ新規作成 |

### 主要イベント
1. **Opus 4.7システムプロンプト漏洩**: 新智元が速報、底層設計が完全露出
2. **Opus 4.7「降智」論争激化**: 量子位「降智実錘了」、新智元「全網差評」
3. **Claude Codeデスクトップ版酷評**: 極客邦科技InfoQ「100% AI 编码」の失敗
4. **封鎖百万アカウント**: 掘金で大規模BAN + KYC複合効果の報道
5. **Agent Skills体系化**: 万字干货記事が話題、Skills＝2026年最重要AI技能
6. **Hermes vs OpenClaw論争**: Agent架構選択の商業矛盾が表面化
7. **復旦NLP 80頁Agent総説**: WeChat経由で大型サーベイ論文が拡散
8. **向量数据库選型**: 2026年版5製品比較ガイドが掘金で公開
9. **Transformer×RNN融合**: Google研究、超長コンテキスト解放

### 新規作成ページ
| ページ | 種別 | 言及数 | 根拠 |
|--------|------|--------|------|
| `entities/gemini-google.md` | Entity | 33 | #6トレンド、wiki未カバー最大トピック |
| `concepts/function-calling.md` | Concept | 4 | NEWトレンド、Agent/MCP基盤技術 |
| `concepts/vector-db.md` | Concept | 4 | NEWトレンド、RAG基盤インフラ |

### 更新ページ
| ページ | 更新内容 |
|--------|----------|
| `entities/claude-opus-4-7.md` | システムプロンプト漏洩、降智論争、デスクトップ版酷評、封鎖百万アカウント、Anthropic企業動向追加 |
| `concepts/ai-agent.md` | 言及数21→117更新、Agent Skills体系化、Hermes vs OpenClaw論争、復旦NLP総説、Function Calling基盤、OpenAI Agents SDK、Tokenコスト問題追加 |

### Wiki統計
- **Entity Pages**: 11（+1）
- **Concept Pages**: 11（+2）
- **Comparison Pages**: 0
- **Total Pages**: 22（+3）
- **Last Updated**: 2026-04-17

### 次回対応候補
- Llama/Meta entity（8言及、4ソース横断）
- 微調/Fine-tuning concept（5言及、NEW）
- 文心一言/Baidu entity（5言及）
- MiniMax entity（4言及）
- 規制/コンプライアンス concept（5言及）
- Cursor vs Claude Code comparison page
- Hermes Agent entity page（新興トレンド）

## [2026-04-18] triage-06 | 第6回トリアージ — 2ページ新規作成、3ページ更新

Scheduled triage run.

### インボックス状況
- **inbox/v2ex/**: 20件（04-18クロール分）、累計約260件
- **inbox/juejin/**: 20件（04-18クロール分）、累計約170件
- **inbox/36kr/**: 12件（04-17/18分）、累計約90件
- **inbox/wechat/**: 12件蓄積
- **inbox/zhihu/**: 0件（403継続）
- **daily-digest**: 04-17, 04-18の2件追加（計4件）
- **新規ファイル数**: 106件（前回トリアージ以降）

### 趋势分析結果（04-18 00:02時点）
`trending_topics.py --days 3` で28トピック検出。Claude 171件（前回146、+17%）、AI Agent 135件（前回117、+15%）。

| # | トピック | 言及数 | 変化 |
|---|---------|--------|------|
| 1 | Claude | 171 | ↑（146→171、+17%） |
| 2 | AI Agent/智能体 | 135 | ↑（117→135、+15%） |
| 3 | GPT | 63 | ↑（56→63） |
| 4 | Anthropic | 62 | ↑（51→62） |
| 5 | OpenAI | 55 | ↑（46→55） |
| 6 | Gemini/Google | 35 | ↑（33→35） |
| 7 | MCP | 31 | ↑（26→31） |
| 8 | Cursor | 31 | ↑（30→31） |
| NEW | 豆包/ByteDance | 4 | NEW — ページ新規作成 |
| NEW | RLHF/対齐 | 5 | NEW |

### 主要イベント
1. **Opus 4.7全面的否定評価の深化**: 「全網差評」「降智実錘」「桌面版烂爆了」の三重苦。Pro+限定＋7.5x消費のコスト問題も表面化
2. **Opus 4.7「GPT味」批判**: 量子位「公開モデルのSOTAだがGPT味が濃い」＝個性喪失への不満
3. **開発者による非推奨表明**: 掘金エンジニアが「Opus 4.7は升级を勧めない」と明言
4. **Claude Design発表**: V2EXで新プロダクト「Claude Design」の情報
5. **OpenAI Codex「独立鼠标」**: 完全リストラクチャリング、バックグラウンドで独立実行
6. **1300億NVIDIA代替**: OpenAIがNVIDIA依存脱却に1300億投資の報道
7. **Codexサブスク不正問題の激化**: 低価格悪用がOpenAI公式に通報、V2EXで大炎上
8. **豆包2.0 + Trae無料化**: ByteDanceがDoubao-Seed-2.0をリリース、中国版Trae無料提供
9. **Agent Skillsエコシステム本格化**: 「万字干貨」ガイド、32 Skills + 8 MCP実践記事
10. **Hermes Agent中国展開**: V2EXでWindows一鍵部署ガイドが話題

### 新規作成ページ
| ページ | 種別 | 言及数 | 根拠 |
|--------|------|--------|------|
| `entities/doubao-bytedance.md` | Entity | 4 | NEWトレンド、ByteDanceのAI戦略・Trae無料化 |
| `concepts/agent-skills.md` | Concept | — | Agent概念の細分化、2026年最重要AI技能として浮上 |

### 更新ページ
| ページ | 更新内容 |
|--------|----------|
| `entities/claude-opus-4-7.md` | 04-18追加報道（全面否定深化、Pro+限定7.5x問題、GPT味批判、Claude Design）、トレンド171言及に更新 |
| `entities/openai.md` | 04-18追加動向（Codex「独立鼠标」再構築、1300億NVIDIA代替、サブスク不正激化、Codexバグ）、トレンド55言及に更新 |
| `concepts/ai-agent.md` | 04-18更新（Agentエコシステム拡大、Skills新ページリンク、Hermes Agent展開、Open Computer Use、n8n統合） |

### Wiki統計
- **Entity Pages**: 12（+1）
- **Concept Pages**: 12（+1）
- **Comparison Pages**: 0
- **Total Pages**: 24（+2）
- **Last Updated**: 2026-04-18

### 次回対応候補
- Llama/Meta entity（8言及、4ソース横断）
- MiniMax entity（5言及）
- 文心一言/Baidu entity（6言及）
- RLHF/対齐 concept（5言及、NEW）
- 多模態 concept（4言及、NEW）
- 規制/コンプライアンス concept（5言及）
- Hermes Agent entity（V2EX展開加速）
- Cursor vs Claude Code comparison page
- Token成本 concept（AI編程コスト構造問題）

## [2026-04-18] triage-07 | ニュースレター定期トリアージ — 2件更新、4件新規作成

Scheduled newsletter triage run (cron). ChinAI #336, #345, #348, #352 の4通を処理。

### メールインボックス状況
- **Maildir/new/**: 4通のChinAIニュースレター（#336, #345, #348, #352）
- **Maildir/cur/**: 11通
- **Maildir/processed/**: 1通（#336）
- **inbox/newsletters/**: `.md` digestファイルなし、`.eml`ファイル4通
- **scripts/process_email.py**: 新規URL抽出、記事保存は未実施（メール本文が直接ニュースレター）

### 処理済みニュースレター

| # | タイトル | 日付 | 主要テーマ |
|---|---------|------|-----------|
| #336 | MiniMax as China's OpenAI | 2026-01 | MiniMax M1/M2、$100M ARR、資本効率 |
| #345 | China's AI Super-App Race | 2026-03 | ByteDance/Doubao vs Alibaba/Qwen vs Tencent |
| #348 | China's Compute Year in Review | 2025-12 | GPU制約、中国半導体動向 |
| #352 | China's Palantir Wannabes | 2026-04 | MiningLamp、4Paradigm、構造的要因 |

### 新規作成ページ
| ページ | 種別 | 根拠 |
|--------|------|------|
| `entities/doubao.md` | Entity | ChinAI #345、ByteDanceのAIチャット戦略 |
| `entities/tencent-ai.md` | Entity | ChinAI #345、WeChat×AI統合戦略 |
| `concepts/china-ai-superapp-race.md` | Concept | ChinAI #345、3Way競争分析 |
| `concepts/china-palantir.md` | Concept | ChinAI #352、エンタープライズAI分析 |

### 更新ページ
| ページ | 更新内容 |
|--------|----------|
| `entities/minimax.md` | ChinAI #336統合：M1/M2モデル、$100M ARR、資本効率分析、OpenAI比較 |
| `entities/qwen.md` | ChinAI #345追加：AIスーパーアプリ競争、Alibabaのフルスタック戦略、3Way比較表 |
| `wiki/index.md` | 新4ページ追加、統計更新 |
| `wiki/log.md` | 本トリアージ記録追加 |

### Wiki統計
- **Entity Pages**: 14（+2: doubao, tencent-ai）
- **Concept Pages**: 14（+2: china-ai-superapp-race, china-palantir）
- **Comparison Pages**: 0
- **Total Pages**: 28（+4）
- **Last Updated**: 2026-04-18

### 次回対応候補
- ChinAI #348（Compute Year in Review）の概念ページ化
- MiniMax vs Moonshot/Kimi 比較ページ
- 中国半導体/GPU制限 concept（H20、制裁影響）
- Llama/Meta entity（6言及継続）
- 文心一言/Baidu entity（6言及継続）

## [2026-04-18] triage-04 | 第4回トリアージ — 10ページ作成、inbox 618件処理

### 処理概要
inbox内の618件未処理記事（V2EX: 283, Juejin: 186, 36kr: 93, WeChat: 27, Newsletters: 29）から、スパム・求人・広告を除外し、技術的価値の高い40件を特定。10件の新規Wikiページを作成。

### 新規作成ページ
| ページ | 種別 | 根拠 |
|--------|------|------|
| `concepts/harness-engineering.md` | Concept | arXiv 2604.08224、Agent外化パターン |
| `entities/creatorweave.md` | Entity | ローカル優先ブラウザ創作ワークスペース |
| `concepts/ai-inner-os.md` | Concept | AI CLIインナーモノローグ可視化 |
| `concepts/ai-video-generation.md` | Concept | 一人開発・短视频自動生成パイプライン |
| `concepts/gomcp.md` | Concept | Go言語MCP Serverフレームワーク |
| `concepts/mcp-security.md` | Concept | OpenClaw事件・MSB安全基準 |
| `entities/soul-killer.md` | Entity | Claude Code用Galgame Agent作成器 |
| `entities/echoic.md` | Entity | オープンソースAI口语練習ツール |
| `concepts/transpec.md` | Concept | 仕様駆動開発フレームワーク間変換 |
| `entities/fudan-nlp-agent-survey.md` | Entity | 復旦大学80ページAgent総論 |

### 更新ページ
| ページ | 更新内容 |
|--------|----------|
| `wiki/index.md` | 63ページに更新、全Entity/Concept反映 |
| `wiki/log.md` | 本トリアージ記録追加 |

### Wiki統計
- **Entity Pages**: 33（+5: creatorweave, soul-killer, echoic, fudan-nlp-agent-survey, baidu-ernie, llama-meta, claude-design）
- **Concept Pages**: 29（+11: harness-engineering, ai-inner-os, ai-video-generation, gomcp, mcp-security, transpec, beike-ai-customer-service, cc-monitor, chinai-348-compute-year-review, claude-code-router, glory-ai-phone, gpu-sanctions-china, ollama-criticism, page-index, spokenwoz）
- **Comparison Pages**: 1（minimax-vs-kimi-moonshot）
| **Total Pages**: 63（+35）
| **Raw Articles**: 23（アーカイブ済み）
| **Last Updated**: 2026-04-18

## [2026-04-19] active-crawl-01 | 第1回アクティブクローリング — 3ページ新規作成

Scheduled active crawl (shelley-active-crawl). hot-topics.yamlから priority:high + last_crawled: null のトピックを抽出。

### 対象トピック（priority: high、deepdive）
1. **deepseek** — DeepSeek-V4 1Tパラメータ、Engram記憶、華為昇騰対応
2. **vibe-coding-china** — Karpathy「Vibe Coding終焉」宣言とAgentic Engineeringへの移行
3. **mcp-china** — MCP+A2Aプロトコル、中国Agent生態系の標準化

### 新規作成ページ
| ページ | 種別 | 根拠 |
|--------|------|------|
| `concepts/deepseek.md` | Concept | DeepSeek-V4（1T MoE、Engram、mHC、昇騰910C、$0.30/MTok）|
| `concepts/vibe-coding-china.md` | Concept | Vibe Coding→Agentic Engineering、Karpathy 2/4宣言、Cursor $293B |
| `concepts/mcp-china.md` | Concept | MCP+A2A標準化、Linux Foundation寄贈、Dify/Coze/百煉対応状況 |

### 主要発見
1. **DeepSeek-V4**: 1TパラメータMoE、Engram条件記憶（計算と記憶の分離）、mHC流形制約超連接。華為昇騰910C + Cambricon MLUで訓練（Nvidia非依存）。内部ベンチ: HumanEval 90%、SWE-bench 80%+（未検証）。Apache 2.0予定。
2. **Vibe Coding → Agentic Engineering**: 2026.2.4 KarpathyがVibe Coding終焉を宣言。中国メディアは「范式切换（パラダイムシフト）」として報道。「プロンプト書きだけ」の開発者は淘汰され、「エージェント群を指揮するアーキテクト」が新種として登場。Cursor估值$293B、Replit $90B期待。
3. **MCP中国生態**: 2025.12にLinux Foundation傘下AAIFへ寄贈、グローバル中立ガバナンスへ移行。DifyはMCP原生統合（消費者・提供者両対応）。A2AプロトコルがAgent間水平協同を標準化。途牛、電商跨境など業界適用が開始。
4. **阶跃星辰 Step 3.5 Flash**: 196B総パラメータ、11B活性化、MTP-3（3路並列予測）、256kコンテキスト。Agent専用最適化モデルとして注目。
5. **国産AI编程助手**: 通義灵码(Alibaba)、CodeGeeX(Zhipu)、MarsCode(ByteDance)、文心快码(Baidu)、腾讯云AI代码助手の5強。Agent協作時代へ移行、本地デプロイ需要急増。

### hot-topics.yaml 更新
- `deepseek`: last_crawled → 2026-04-19
- `mcp-china`: last_crawled → 2026-04-19
- `vibe-coding-china`: last_crawled → 2026-04-19

### Wiki統計
- **Concept Pages**: 31（+3: deepseek, vibe-coding-china, mcp-china）
- **Total Pages**: 66（+3）

## [2026-04-19] update | MiniMaxモデル情報拡充

MiniMax entityページおよびMiniMax vs Kimi比較ページをM2.5/M2.7モデル詳細で大幅更新。

### 更新ページ
| ページ | 更新内容 |
|--------|---------|
| `entities/minimax.md` | M2.5/M2.7追加、セルフ進化モデル特性、Vals AIベンチマーク、コスト比較、Token PlanマルチモーダルAPI一覧、実ユーザー課題報告 |
| `comparisons/minimax-vs-kimi-moonshot.md` | モデル比較をM2.7ベースに更新、中国主要モデル横断比較表（MiniMax/Kimi/Qwen/GLM/Claude）、タイムライン拡充 |

### 主要発見
1. **M2.7セルフ進化**: OpenClawフレームワーク上で100+自律訓練サイクル、人間介入なしに30%性能向上。初の「自己改善型」モデル
2. **コスト破壊力**: 10BアクティブパラメでOpus 4.6に肉薄、入力は1/50($0.30/M)、出力は1/60($1.20/M)、速度は3倍(100 TPS)
3. **実用上の課題**: V2EX報告で複雑な指示追従に弱点。「新兵蛋子のように突っ走る」傾向。単純タスクでは優秀
4. **マルチモーダル統合**: Token PlanでTTS(speech-2.8-hd)・音楽生成・画像生成・VLM・検索を一括提供

### Wiki統計
- **Entity Pages**: 33（更新: minimax）
- **Comparison Pages**: 1（更新: minimax-vs-kimi-moonshot）
- **Total Pages**: 66
- **Last Updated**: 2026-04-19

## [2026-04-21] triage-juejin | Juejinインボックストリアージ — 9ページ新規作成

Originating conversation: 手动トリアージ

### インボックス状況
- **inbox/juejin/**: 129件（的重複あり）
- **サイズフィルター**: 1500バイト以下はスタブと判定しスキップ
- **实质的コンテンツ**: 约65件（スタブ约64件）

### 处理结果

#### ❌ Skip（ короткие stubs / 純粋プロモ / 低品質）
- n8n工作流自动化连载（重复）
- n8n工作流-知识卡片（低score）
- AI-周刊（既存raw保存済み）
- Vibe Coding概念大全（既存concept覆盖済み）
- 深入浅出LLM大语言模型（2024年古い記事）
- Vite Coding基础（既存concept覆盖済み）
- LangChain 30天教程连载（参考程度）
- 试用了很多Go框架（AIとは无関系）
- Gmail/Gemini登录问题（トラブシューティングtips）
- 各类Skill连载（低score重复）

#### ✅ Take（Wiki新規作成）

| ページ | 種別 | 根拠 |
|--------|------|------|
| `entities/mini-cc.md` | Entity | Claude Code解析シリーズ作者の自作ツール、雨夜寻晴天の核心プロジェクト |
| `entities/springai-alibaba.md` | Entity | 阿里开源Java AI框架、80いいね・137收藏、Java Agent開発の標準ツール |
| `entities/openmythos.md` | Entity | 22歳天才がMythos逆推、MoE+DeepSeek技術統合、量子位報道 |
| `concepts/android-cli.md` | Concept | Google Agent-first開発時代向けAndroid CLI、新トレンド |
| `concepts/browser-use.md` | Concept | 86k StarsブラウザAgent DOM処理パイプライン |
| `concepts/graphiti.md` | Concept | LLMリアルタイム知識グラフ、新しい記憶システム |
| `concepts/mini-cc-claude-code-analysis-series.md` | Concept | Claude Code解析9章シリーズ、アーキテクチャ理解に 필수 |
| `concepts/openai-eval-skill-validation.md` | Concept | OpenAI Eval体系によるSkill検証方法論 |
| `concepts/prompt-agent-function-call-skill-mcp.md` | Concept | 用語整理高評価記事（118いいね）、AI Engineer必須知識 |

#### Raw Articles保存
- `2026-04-21-Prompt-Agent-Function-Call-Skill-MCP-傻傻分不清楚.md`
- `2026-04-21-别再裸用-Claude-Code-了-32-个亲测Skills.md`
- `2026-04-21-SpringAI-Alibaba-阿里又开源了一个顶级Java项目.md`

### Wiki統計
- **Entity Pages**: 36（+3: mini-cc, openmythos, springai-alibaba）
- **Concept Pages**: 58（+5: android-cli, browser-use, graphiti, openai-eval-skill-validation, prompt-agent-function-call-skill-mcp）
- **Concept Pages新規**: 1（mini-cc-claude-code-analysis-series）
- **Comparison Pages**: 1
- **Total Pages**: 95（+9）
- **Raw Articles**: 157（+3）
- **Last Updated**: 2026-04-21

### 主要发现

1. **mini-cc + Claude Code解析シリーズ**: 雨夜寻晴天の9章構成解析はClaude Code内部構造理解の最高資料
2. **Prompt/Agent/Function Call/Skill/MCP混乱**: 118いいねでAI Engineer必須の用語整理
3. **SpringAI Alibaba**: Java Agent開発的事实上標準、LangChain比对で企業適用优势
4. **OpenMythos**: 22歳天才のMythos逆推、DeepSeek技術統合の象徴
5. **browser-use / Graphiti**: LLM应用の新しい抽象化レイヤー

### 作成背景
ホットトピック分析で指摘されていた未作成の重要概念ページをまとめて作成。

### 新規作成ページ
| ページ | 種別 | 重要度 | 根拠 |
|--------|------|--------|------|
| `concepts/china-ai-agent-ecosystem.md` | Concept | 🔥🔥🔥 HIGH | 中国AIプラットフォーム全体図 |
| `concepts/china-local-deployment.md` | Concept | 🔥🔥🔥 HIGH | 国産モデルの本地部署エコシステム |
| `concepts/china-ai-regulation.md` | Concept | 🔥🔥🔥 HIGH | AI监管政策・算法备案・データ安全 |
| `concepts/china-coding-agents.md` | Concept | 🔥🔥🔥 HIGH | 中国プログラミングAgentツール比較 |
| `concepts/coze.md` | Concept | 🔥🔥 MEDIUM | ByteDanceのノーコードAgentプラットフォーム |
| `concepts/dify.md` | Concept | 🔥🔥 MEDIUM | オープンソースLLMOpsプラットフォーム |
| `concepts/china-ai-landscape.md` | Concept | 🔥🔥 MEDIUM | BAT + ByteDance + スタートアップ全景 |
| `concepts/china-open-source-ai.md` | Concept | 🔥🔥 MEDIUM | 中国OSS AIコミュニティ生態系 |

### 更新ページ
| ページ | 更新内容 |
|--------|----------|
| `wiki/index.md` | 8件新規コンセプト追加、カウント29→37に更新 |
| `wiki/log.md` | 本トリアージ記録追加 |

### Wiki統計
- **Entity Pages**: 33
- **Concept Pages**: 37（+8）
- **Comparison Pages**: 1
- **Total Pages**: 71（+8）
- **Last Updated**: 2026-04-19

---

## [2026-04-19] crawl-triage-04-19 | Multi-source crawl + wiki update

Originating conversation: auto-cron (crawl_all.py)

### 収集サマリー
| ソース | 収集数 |
|--------|--------|
| crawl_all (v2ex + juejin + 36kr + wechat) | 57件 |
| Newsletter ( inbox/newsletters/) | 0件 (すべて04-18以前) |
| blogwatcher RSS | DB利用不可 |
| **合計** | **57件** |

### トリアージ結果
| 判定 | 件数 | 備考 |
|------|------|------|
| ✅ Take | 19件 |  высокоприоритетные статьи |
| ⚠️ Reference | 11件 | 中優先度・補完的 |
| ❌ Skip | 1件 | SEO/低品質 |

### 主要✅ホットトピック
1. **Claude Design → Figma Killer** — 36kr×3件、AnthropicがデザインSaaSに参入、株安
2. **DeepSeek、梁文锋が\$100B估值で\$3億調達検討** — 36kr報道、商業化転換
3. **Claude Opus 4.7「全网差评」** — 中国開発者コミュニティで酷評継続
4. **Claude Code Skills + MCP実践** — Juejin高票(466👍) статья
5. **Kimi K2.5代替Claude Code** — Juejin 225👍、中国シフト
6. **OpenAI人事危機（Sora之父离职）** — 36kr報道
7. **Anthropic安全専門家大量退職** — 36kr「谁为AI竞赛踩刹车」
8. **智谱GLM-5开源** — 中国国産の強い競争力

### Wiki更新
| アクション | ページ |
|-----------|--------|
| 更新 | `entities/deepseek.md` — 資金調達・NVIDIA緊張関係追加 |
| 更新 | `entities/claude-opus-4-7.md` — Claude Design Figmaキラー・OpenAI危機・安全専門家退職追加 |
| 保存 | `raw/articles/daily-digest-2026-04-19.md` |

### Wiki統計
- **Entity Pages**: 33
- **Concept Pages**: 37
- **Comparison Pages**: 1
- **Total Pages**: 71
- **Last Updated**: 2026-04-19

## [2026-04-19 21:02] triage-evening | 夕方便新クロール — 新概念ページ作成

### ソース別収集数
- crawl_all: 57件 (V2EX 15, Juejin 15, 36kr 12, Zhihu 0, WeChat 15)
- Newsletter: 0件 (既処理済み Apr-18分のみ)
- RSS(blogwatcher): DBなし
- **合計**: 57件

### トリアージ結果
| 判定 | 件数 | 備考 |
|------|------|------|
| ✅ Take | 10件 | 新規Wikiページ作成・既存ページ更新 |
| ⚠️ Reference | 5件 | raw/articles/保存のみ |
| ❌ Skip | 42件 | プロモ・ゲーム・一般生活議論 |

### ✅ Take（Wiki更新対象）
1. **Claude Opus 4.7** — 安全専門家大量退職・Claude僧人インタビュー追加更新 (既存ページ)
2. **DeepSeek** — $100億估值$3億資金調達・黄仁勋慌了的戦略的対抗追加 (既存ページ)
3. **[[implicit-structure-collapse]]** — 新規コンセプトページ作成（LLM出力の隠れ構造塌縮分析）
4. **Claude Design** — Figma Killer機能・宗教とAI倫理言及 (既存ページ更新済み)
5. **OpenAI人事** — Sora之父离职・IPO前夜の組織動揺 (36kr)
6. **中美AI差距 2.7%** — Stanford HAI 2026レポート (Juejin週次摘要より)
7. **超算郑州节点** — 6万枚国产AIチップ・10EFLOPS (Juejin週次摘要)
8. **隐性结构塌缩** — Juejin獨自分析、平庸出力破解3手法 (新概念)
9. **Harness (Powerball)** — V2EX開発者自作ツール (V2EX)
10. **Claude僧人** — 弃码出家30年后回归、Anthropic人文的AI安全アプローチ (36kr)

### Wiki更新
| アクション | ページ |
|-----------|--------|
| 新規作成 | `concepts/implicit-structure-collapse.md` — LLM出力構造塌縮の理論と対策 |
| 更新 | `entities/claude-opus-4-7.md` — 安全専門家退職・Claude僧人追加 |
| 更新 | `entities/deepseek.md` — 資金調達詳細・黄仁勋対応追加 |
| 保存 | `raw/articles/2026-04-19-AI-Weekly-*.md` |
| 保存 | `raw/articles/2026-04-19-大模型输出隐性结构塌缩*.md` |
| 保存 | `raw/articles/2026-04-18-安全专家纷纷离职*.md` |
| 更新 | `wiki/index.md` — 新規コンセプト追加 |

### Wiki統計
- **Entity Pages**: 33
- **Concept Pages**: 41 (38→41 +implicit-structure-collapse)
- **Comparison Pages**: 1
- **Total Pages**: 75
- **Last Updated**: 2026-04-19 21:02

## [2026-04-20] triage-08 | 第8回トリアージ — 497件→290件重複削除後、Wikiトレンド更新

Originating conversation: kzinmr Discord — インボックス一括処理リクエスト（390件）

### インボックス状況（処理前）
- **inbox/36kr/**: 48件
- **inbox/juejin/**: 104件
- **inbox/v2ex/**: 238件
- **inbox/newsletters/**: 58件
- **合計**: 497件

### 重複削除
- 36kr: 23件重複削除（同一URL・タイトルで日時違い）
- Juejin: 41件重複削除
- V2EX: 34件重複削除
- **処理後**: 36kr=25, Juejin=63, V2EX=205

### トリアージ結果（サブエージェント並列処理）

#### 36kr（25件→重複後）
- ✅ Take: ~15件（DeepSeek資金調達報道、Claude/Anthropic安全性議論、Claude Design関連）
- ⚠️ Reference: ~5件
- ❌ Skip/重複: ~5件

#### Juejin（63件→重複後）
- ✅ Take: ~30件（MCPセキュリティ深堀、Claude Codeスキル集 браузер-agents、LangChain脆弱性补丁）
- ⚠️ Reference: ~20件
- ❌ Skip: ~13件（古いチュートリアル、。重複記事）

#### V2EX（205件→品質フィルタリング済み）
- ✅ Include（品質通過）: ~11件（Tellis v0.5、ferris-grad、Rust自動微分库、FluxTTY）
- ❌ Exclude: ~39件（求人広告、プロキシ業者投稿、仅为链接）

### トレンド分析結果（3日内）
| トピック | 言及数 | ソース |
|---|---|---|
| AI Agent/智能体 | 93 | 全ソース |
| Claude | 90 | 36kr+juejin+v2ex |
| Anthropic | 41 | 36kr+juejin+v2ex |
| OpenAI | 32 | 全ソース |
| DeepSeek | 10 | 36kr+juejin+v2ex |

### Wiki更新
- 更新: `entities/anthropic.md`（トレンド順位 #4→#3、41言及）
- 更新: `entities/deepseek.md`（トレンド順位 #14→#10、注目上昇）
- 更新: `entities/openai.md`（トレンド順位 #5→#4、32言及）
- 新規作成なし（既存のMCPセキュリティページがOpenClaw12類脆弱性を既にカバー）

### 新規ページ候補（次回合対応）
- **FluxTTY** — Vim風AIプログラミングTerminal（V2EX高质量）
- **ferris-grad** — Rust実装PyTorch風自動微分（教育価値高）
- **Graphiti** — LLM用リアルタイム知識グラフ（Juejin新規）
- **browser-use** — ブラウザAgent DOM処理パイプライン（Juejin新規）

### 関連リンク
- [36kr — DeepSeek百亿美元估值融资](https://36kr.com/p/3774394570982144)
- [V2EX Triage Report](inbox/v2ex/TRIAGE-REPORT-2026-04-20.md)

## [2026-04-20] active-crawl-01 | ホットトピック能動的クロール

Originating conversation: (scheduled cron)

### 対象トピック選択基準
- crawl_policy: prerequisites / laterals / deepdive
- last_crawled: null（未取得）
- priority: high 2件 + medium 1件

### 選択トピック
| slug | priority | crawl_policy | 選択理由 |
|------|----------|--------------|---------|
| qwen | high | deepdive | null、Alibabaの旗艦モデル |
| china-ai-agent-ecosystem | high | deepdive | null、中国Agent市場動向 |
| chatglm | medium | deepdive | null、Zhipu AI(GLM-5) |

### クロール結果

#### qwen — Qwen3.5 シリーズ新規追加
- **Qwen3.5-Plus** (开源): 3970B総パラメータ/MoE、170B活性化、原生多模态
- MMLU-Pro 87.8点（GPT-5.2超）、GPQA 88.4点（Claude 4.5超）
- API価格: **0.8元/MTok**（約$0.11）
- **Qwen3.5-Max** (旗舰推理)、Qwen3.6-Plus/Flash/VL最新系列
- **购物Agent**: 2026年1月发布、春節6日間で1.2億笔注文処理
- 累計10億ダウンロード、衍生モデル20万+
- **Qwen-Coder** (2025年4月): 119言語、235B MoE、Apache 2.0
- 混合思考模式（思考/非思考智能切替）
- 対応言語201種類に扩展

#### china-ai-agent-ecosystem — BATB四強戦略セクション追加
- **字节（豆包）**: MAU 2億突破、1600亿元投入、春晚独家、AIスマート眼鏡(Ola Friend)量产
- **阿里（通义千问）**: MAU 1億突破、购物Agent世界初大规模商业化验证、AgentKit
- **腾讯（元宝）**: 微信深度埋め込み、10亿现金推广、社交裂变戦略
- **百度（文心）**: 文心5.0上线、专业化戦略、几十万活跃Agent
- 「AI墙内竞争」時代の始まり（字节のApp调用に対して阿里・腾讯が护城河防御）

#### chatglm — GLM-5シリーズ・智谱の現状新規追加
- **GLM-5** / **GLM-5.1**: SWE-bench Verified开源SOTA、比肩 Claude Opus 4.5
- **AutoClaw（澳龙）**: PC一键安装Agent客户端、50+ Skills内置
- **AutoGLM**: 自主规划・推理・执行、长步骤・跨app対応
- **GLM-PC**: CogAgent-9B开源、画面截图のみでPC操作自动化
- 香港上場（02513.HK）— 中国大型独立LLM厂商初
- bigmodel.cn: 智能体市场・MCP対応・模型微调十分钟完了

### Wiki更新
- 新規作成: `concepts/qwen.md`（6382 bytes）
- 新規作成: `concepts/chatglm.md`（5378 bytes）
- 更新: `concepts/china-ai-agent-ecosystem.md`（BATB四強セクション追加、updated日付更新）
- 設定ファイル: `config/hot-topics.yaml` last_crawled 更新3件

### 関連リンク
- [阿里云开发者: Qwen3.5发布](https://developer.aliyun.com/article/1713691)
- [Qwen3-Coder公式サイト](https://www.qwen3coder.com/zh)
- [Zhipu AI](https://www.zhipuai.cn/zh)
- [BigModel.cn](https://open.bigmodel.cn/)
- [TechGG: 2026是Agent生死之年](https://www.techgg.com/article/237-1.html)

## [2026-04-20] triage-02 | 夜間クロール・トリアージ

Originating conversation: (scheduled cron)

### Phase 1: ソース別収集数
| ソース | 件数 | 備考 |
|--------|------|------|
| crawl_all | 57件 | 5ソース合計（v2ex:15, juejin:15, 36kr:12, wechat:15） |
| Newsletter | 2件 | 新規（ChinAI #355, Zhihu Frontier Weekly） |
| RSS(blogwatcher) | — | DB不存在 |

### Phase 2: トリアージ結果
- **✅ Take**: 14件（高価値）
  - Juejin: 9件（Claude/GLM比較、Codex攻略、GLM-5初体験、GLM-5开源、OpenAI Eval手法、Enterprise Vibe Coding、LangChain Agent実装、Skill作成、n8nワークフロー）
  - 36kr: 2件（CLAUDE.md現象、Mythos架构逆推开源）
  - WeChat: 3件（LLM-Agent包括解説、复旦80頁Agentサーベイ、Meta持続事前訓練）
- **⚠️ Reference**: 4件（中価値）
  - 36kr: Codex+终身记忆、Claude Mythos开源
  - WeChat: Agentエンジニア技術指南、AI软件演进成功率13.37%

### Phase 3: 発見事項
- **Newsletter処理失敗**: `process_newsletter.py` → ModuleNotFoundError: readability
- **blogwatcher DB不存在**: ~/.blogwatcher-cli/blogwatcher-cli.db なし
- **既存Wikiとの重複**:  معظم記事が前日までに処理済み

### Phase 4: ホットトピック（本日）
1. **CLAUDE.md現象** — Karpathy源流、GitHub TRENDING1位
2. **Mythos架构逆推** — 22歳天才がDeepSeek技術取り込みオープンソース
3. **LLM-Agent関係 包括的議論** — 中国全土でAgent定義議論が沸騰
4. **GLM-5开源** — 智谱のコード生成能力への警戒

### 次のアクション
- `pip install readability-lxml` でprocess_newsletter.py修復
- Mythos架构 → concepts/mythos-engineering.md 新規作成推奨
- CLAUDE.md現象 → concepts/claude-md.md 新規作成推奨

## [2026-04-21] triage-v2ex-04 | V2EXインボックストリアージ — 8ページ新規作成

Originating conversation: (scheduled cron)

### インボックス状況
- **inbox/v2ex/**: 292件（2026-04-15〜21クロール分）

### トリアージフィルター
- **INCLUDE**: 技術的AI/LLM議論、開発者ツール、中国AI業界分析
- **EXCLUDE**: 求人広告、ベンダー広告/SPAM、リンクだけ、汎用ツール共有

### 趋势分析結果
 топ тем из 292件:
1. **Claude Code** — アイデンティティ検証、KYC問題
2. **MCP** — プロトコル採用拡大、GoMCPフレームワーク
3. **Harness Engineering** — 概念の定着と実践
4. **RAG** — 実践での課題（幻觉、结构理解）
5. **Vibe Coding** — 開発パラダイムとしての定着

### 新規作成ページ
| ページ | 種別 | 根拠 |
|--------|------|------|
| `concepts/llm-hallucination-handling.md` | Concept | 大模型表格结构理解の限界に関する深い分析 |
| `concepts/specflow-ai-development.md` | Concept | AI时代设计驱动开发新范式 |
| `concepts/local-model-token-formula.md` | Concept | 本地部署VRAM/带宽计算实用公式 |
| `concepts/karpathy-obsidian-llm-wiki.md` | Concept | Karpathy LLM Wiki方法论实际落地 |
| `concepts/mini-cc-lightweight-coding-agent.md` | Concept | 轻量级TS编程Agent框架 |
| `concepts/vibe-coding-harness-synergy.md` | Concept | Harness适用场景与Blind Vibe Coding分析 |
| `concepts/clipimg-agent-cli-tool.md` | Concept | Agent CLI工具分享 |
| `concepts/claude-code-ip-ban-analysis.md` | Concept | Claude封号IP检测深度复盘 |

### 除外した主なカテゴリー
- AI中转站广告（OneXModel等）- ベンダー広告
- Claude/Plus订阅折扣广告 - ベンダー広告
- 求职帖子（AI相关求职除外） - 求人広告
- 金融/投资建议帖 - SPAM范畴
- 链接分享无实质内容 - リンクだけ

### 次回対応候補
- Kimi2Moon工具（Kimi接入Hermes-Agent）
- GoMCP（MCP Server框架）→ 既存gomcp.mdと統合
- Codex Computer Use权限交互复刻
- AI视频生成技术讨论 → 既存ai-video-generation.mdと統合

## [2026-04-21] cn-media-trend-041 | 中国語AIメディアトレンド — Kimi K2.6がトレンド

Originating conversation: (scheduled cron)

### ソース別収集数
- crawl_all: 55件 (V2EX:15, Juejin:15, 36kr:10, Zhihu:0, WeChat:15)
- Newsletter: 0件（ChinAI #355は前回処理済み）
- RSS(blogwatcher): DB不存在

### ホットトピック
1. **Kimi K2.6开源** — 杨植麟が300个Agent指挥の旗舰模型を発表
2. **Opus 4.7批判** — 「Anthropicの野心、输给了拉胯工程」
3. **Google布林「追杀队」** — DeepMindにClaude追杀专队设置
4. **Claude Code中囼封号** — IP検出の议论（V2EXで続く）
5. **Hermes+K2.6 Agent军团** — 掘金で実践ガイドが即座に投稿

### ソース間比較: Kimi K2.6
| ソース | 論調 | フォーカス |
|--------|------|-----------|
| 36kr | 好意的・産業分析 | 开源戦略、Agent集群能力 |
| 掘金 | 実践的・肯定 | K2.6+Hermesで7x24hワークフロー構築 |
| V2EX | 技術検証待ち | まだ话题になっていない |

### 温度差
- **36kr**: 「Anthropic vs Google」竞争激化報道、Opus 4.7批判
- **V2EX**: Claude Code封号・KYC问题が продолжается（数日起き続き）
- **掘金**: LangChain教程连载、K2.6実践ガイド即投稿

### Wiki更新
- 新規: `concepts/kimi-k2-6.md`
- 追加: 4件生記事raw保存
- 更新: index.mdにK2.6ページ追加

## [2026-04-22] shelley-active-crawl | 能動的クロール: Kimi K2.6, Coze Agent World, China Coding Agents

### 対象トピック
| トピック | crawl_policy | priority | last_crawled更新 |
|---------|-------------|----------|-----------------|
| [[kimi|Kimi（月之暗面）]] | deepdive | high | 2026-04-22 |
| [[coze|扣子/Coze]] | laterals | medium | 2026-04-22 |
| [[china-coding-agents|中国编程Agent工具]] | deepdive | high | 2026-04-22 |

### 主要発見事項

#### Kimi K2.6（2026-04-21発表・オープンソース化）
- **コード能力**: 13時間不停にコード生成、4000行以上修正・作成
- **ベンチマーク**: Humanity's Last Exam・SWE-Bench ProでGPT-5.4・Claude Opus 4.6・Gemini 3.1 Proと同等以上
- **Agent集群**: 最多300Agent並列、4000协作ステップ実行
- **ローカル推論**: Mac上でZig言語最適化、LM Studio比20%高速
- API価格: 入力¥6.50/MTok、而出力¥27.00/MTok
- パートナー: Vercel・OpenRouter・Windsurf・Cursor・Huawei等

#### Coze Agent World（2026年4月新機能）
- Agentが云电脑・云手机を保有し7×24自律実行
- 技能商店（Skills Store）でAgent同士が自己進化
- 扣子编程: 自然言語でWeb APP小程序智能体工作流を一気通貫開発
- OpenClaw一键部署: 飞书・微信へ即座デプロイ
- Kimi・Doubao・Qwen・GLM等多モデル選択可能

#### 中国Coding Agents市場（2026年4月版）
- **Claude Code中国離れ加速**: AnthropicのKYC制限で中国開発者がKimi K2.6等国産へ移行
- **3パラダイム対立**: Terminal-native (Claude Code) vs IDE統合 (Cursor) vs 异步委托 (Codex)
- **Zed**: Rust採用で极致性能も、AI機能ではVS Code系に劣る
- ツール選択ガイド（日常/重构/批量/コスト重視别）を整備

### Wiki更新
- **新規**: `concepts/kimi.md`（トップレベルページ、K2.6詳細）
- **更新**: `concepts/coze.md`（Agent World, OpenClaw, 扣子编程追加）
- **更新**: `concepts/china-coding-agents.md`（K2.6ベンチマーク、3パラダイム、ツール比較表更新）

### 次回対応
- Opus 4.7の批判的具体的内容深掘り（36kr記事の詳細解析）
- Claude Code封号事件の时间線整理
- 36kr Anthropic/Google布林記事の詳細解析

## 2026-04-23 Media Trend Analysis (cn-media-analysis skill)

**Analysis period:** 2026-04-20 to 2026-04-23 (3 days)
**Total articles:** 412 (V2EX: 185, Juejin: 132, 36kr: 63, Zhihu: 0, WeChat: 32)
**Cross-source trending topics:** 28 (topics appearing in 2+ independent sources)

### Key findings:
- **AI Agent/智能体** dominates with 123 sources across 4 platforms
- **Claude** (114 sources), **OpenAI** (35), **MCP** (26), **Vibe Coding** (22) are next tier
- **多模态** (10 sources, 4 platforms) — new cross-platform topic, no wiki page
- **Zhihu**: 0 articles (source gap)

### New Page Recommendations:
1. **多模态/Multimodal AI** — 10 sources, 4 platforms, NO wiki page (high priority)
2. **RLHF/对齐** — 4 sources, NO wiki page (medium priority)
3. **微调/Fine-tuning** — 3 sources, NO wiki page (medium priority)

### hot-topics.yaml additions:
- multimodal-ai (high priority)
- rlhf-alignment (medium priority)
- fine-tuning (medium priority)

## 2026-04-23 Triage — Raw Articles + Wiki Pages

### インボックス状況
- **inbox/juejin/**: 200件（クロール済み、一部重複）
- **inbox/36kr/**: 94件（全件rawに保存済み）
- **inbox/v2ex/**: 384件（未処理、スパム率高）
- **inbox/wechat-media/**: 90件（未処理）
- **inbox/newsletters/**: 32件（未処理）

### Raw Articles 追加
- **7件**を `wiki/raw/articles/` に追加（Juejin 7件）
  - 大模型训练参数调优（912B）
  - RAG架构设计深度解析（824B）
  - Claude Code架构总结展望（831B）
  - In-context Learning ICL解説（800B）
  - LangChain RAG安全加固（822B）
  - LangChain RAG评估实战（815B）
  - LangChain Agent Function Calling（816B）

### Wiki Pages 作成・更新
- **新規**: `concepts/in-context-learning.md` — ICLの基本概念解説ページ
- **更新**: `concepts/rag.md` — 掘金RAG架构设计深度解析記事を外部ソーステーブルに追加

### 次回対応
- V2EXトリアージ（20%フィルター適用、スパム・求人情報・広告を除外）
- Newsletters（58件）の処理
- WeChat media（28件）の処理
- 多模态/Multimodal AIの概念ページ作成（cn-media-analysis recommendation）

## 2026-04-24 Triage — Crawl & Triage + Media Trend Analysis

### チェックポイント
- **Run ID**: 20260424T090205Z
- **収集候補**: 15件（V2EX 9, Juejin 7, 36kr 1）

### トリアージ結果
| アクション | 件数 | 詳細 |
|------------|------|------|
| ✅ Take | 4件 | V2EX: 3件, 36kr: 1件 |
| ⚠️ Reference | 3件 | V2EX: 3件（GPT-6.0噂、Deep Research、GPT Plus） |
| ❌ Skip | 8件 | Juejin旧記事再生成5件、V2EX重複3件 |

### Wiki Pages 更新
1. **`concepts/ai-safety-subconscious.md`** — V2EX star7th氏による「開発者のAIプライバシー無関心」議論を追加（2026-04-24）
   - 開発者心理学としての意義（慣れによる安心感の誤認、便益とリスクの非対称評価）
   - 「防君子不防小人」論 — 形式的安全対策への不信
2. **`pages/openai-codex-infrastructure.md`** — SSH远程开发の「偷偷加了」透明性懸念を明記
3. **`concepts/mcp-security.md`** — 既知のトピック（OpenClaw 12隐患、GPT脆弱性）を既にカバー済

### Raw Articles 追加
- **1件**: `wiki/raw/articles/2026-04-24-v2ex-star7th-ai-privacy-concern.md`

### 本日の主要トピック（Daily Digest 2026-04-24）

| トピック | ボリューム | 主要ソース |
|----------|-----------|------------|
| **DeepSeek V4リリース** | 15+件 | V2EX, Juejin, 36kr, WeChat |
| **GPT-5.5リリース** | 10+件 | 36kr, Juejin, V2EX |
| **Claude→Kimi K2.5置換** | 3-5件 | Juejin |
| **OpenClawセキュリティ** | 2-3件 | 36kr, Juejin |
| **MCPプロトコル** | 3件 | Juejin |
| **AIプライバシー意識** | 1件 | V2EX（星7th） |
| **华为昇騰950対応** | 2件 | 36kr |
| **Coding Plan** | 2件 | V2EX |

### ソース間比較 — DeepSeek V4 vs GPT-5.5 同時リリース

| 指標 | V2EX（開発者） | Juejin（実装者） | 36kr（ビジネス） | WeChat（深層分析） |
|------|---------------|------------------|-------------------|-------------------|
| **DeepSeek V4** | 「V4变强了，但是也太贵了」「早点出coding plan」— コスト懸念強 | 「天下苦Token久矣，DeepSeekV4终于来了」— 歓迎論 | 「成本暴降73%」「华为昇腾950明示支持」— 産業分析 | AIAgent関連の文脈で言及 |
| **GPT-5.5** | 「天下苦Claude久矣，GPT就出招了」— Claudeユーザーの移行 | 「全榜第一碾压Opus 4.7」— ベンチマーク重視 | 「不卖Token了」「最强模型不是嘴炮」— ビジネスモデル変革 | Vision Bananaの生成理解 |
| **温度差** | コストと実使用感に焦点 | 実践的価値に焦点 | 市場インパクトに焦点 | 技術的新規性 |

### 温度差検出
1. **DeepSeek V4価格問題**: 36krは「成本暴降73%」とポジティブだが、V2EXは「太贵了、早点出coding plan」と実利用者の価格不満。国産モデルのマーケティング vs 実力ギャップ
2. **GPT-5.5 vs Claude**: V2EXでは「天下苦Claude久矣」とClaudeユーザーのGPT-5.5への移行関心が強い。JuejinではKimi K2.5をClaude Codeの代替として実践検証

## [2026-04-24] cn-media-analysis | DeepSeek V4 / GPT-5.5 同時リリース — 3モデル比較分析

### インボックス状況（スクリプトエラーあり）
- **checkpoint**: 失敗（ok=false — JSONパースエラー）
- **収集数**: V2EX:40, Juejin:38, 36kr:39, WeChat:17, 総計:134件（Daily Digest: 60件）

### 主要トピック
| トピック | ボリューム | 主要ソース |
|----------|-----------|------------|
| **DeepSeek V4リリース** | 50+件 | 全ソース（V2EX/Juejin/36kr/WeChat） |
| **GPT-5.5リリース** | 30+件 | 36kr/Juejin/V2EX |
| **3モデル同時アップデート** | 15+件 | V2EX |
| **Claude Code制限/Pro排除** | 5件 | Juejin/V2EX |
| **昇騰950対応** | 3件 | 36kr/V2EX |
| **Kimi K2.5代替** | 2件 | Juejin |
| **GPT-Image-2** | 3件 | Juejin/36kr |

### ソース間温度差

**1. DeepSeek V4価格問題**: 36krは「成本暴降73%」と超肯定的だが、V2EXは「V4变强了，但是也太贵了」と実利用者の価格不満。国産モデルのマーケティング vs 実力ギャップが顕在化。

**2. GPT-5.5 vs Claudeユーザー離れ**: V2EXで「天下苦Claude久矣」— Claudeの価格/制限問題に苦しんだユーザーがGPT-5.5に期待。Juejinで「手握GLM,MiniMax一堆Key，却只开一个Claude？太亏了」— 国産モデル活用の現実的提案。

**3. 昇騰エコシステム**: 36krで「黄仁勋说这是"灾难"」「DeepSeek-V4明确支持华为昇腾950芯片」— 米国GPU依存からの脱却を戦略的意義として強調。V2EXでは「之前难产真是适配昇腾?」— V4遅延の昇騰要因説が浮上。

### Wiki更新
| ページ | 更新内容 |
|--------|---------|
| `entities/deepseek.md` | V4技術特長（百万字コンテキスト、Agent能力、昇騰950）、データ品質懸念、ソース間比較表追加 |
| `entities/claude-code.md` | Proユーザー排除懸念、Kimi K2.5代替事例、OpenClaw IP Ban問題追記 |

### トレンド伝播パターン

| トピック | 初出ソース | 初出日 | 拡散先 | 変容 |
|----------|-----------|--------|--------|------|
| DeepSeek V4 | WeChat/36kr | 04-24 | Juejin→V2EX | 公式発表→ベンチマーク→実使用感 |
| GPT-5.5 | 36kr | 04-24 | Juejin→V2EX | ニュース→技術検証→比較論 |
| Claude Code制限 | Juejin | 04-24 | V2EX | 実践報告→懸念共有 |
|| キミ K2.5代替 | Juejin | 04-24 | — | 孤立トピック（エコーチェンバー懸念） |

## [2026-04-26] ingest-turboquant-dflash | TurboQuant + DFlash 新規概念ページ作成

### 新規ページ（2件）

1. **concepts/turboquant.md** — Google Researchの超高効率ベクトル量子化アルゴリズム
   - **TurboQuant**: KVキャッシュ6×圧縮 + 精度損失ゼロ
   - **PolarQuant**: 偏座標変換によるメイン圧縮（AISTATS 2026）
   - **QJL**: 1ビット残余補正によるattention scoreバイアス除去（AAAI 2025）
   - コミュニティ実装: turboquant-hf (PyPI), turboquant-model (GitHub)
   - vLLM/llama.cpp統合は開発中（2026年4月時点）

2. **concepts/dflash.md** — Z-Labのブロック拡散モデルによる6倍推論加速
   - **ブロック拡散**: 単一フォワードパスでブロック全体を並列生成
   - **KV注入イノベーション**: target featuresを全層のKV投影に注入（EAGLE-3の第一層注入を超える）
   - **最大6倍加速**（Qwen3-8B、lossless）
   - 対応モデル: Qwen3.5/3.6シリーズ、Kimi-K2.5、gpt-oss、LLaMA-3.1
   - バックエンド: vLLM、SGLang、Transformers、MLX

### Raw Articles（2件）

1. **raw/articles/google-research-turboquant-2026.md**
2. **raw/articles/z-lab-dflash-2026.md**

### Index更新

- コンセプト数: 79 → 81
- `turboquant.md` と `dflash.md` をアルファベット順にConceptsセクションに追加

## 2026-04-26 21:01 Triage Checkpoint (20260426T210139Z)

- **総収集**: 60件（実質11件、Sogou古記事49件）
- **Take**: 2件 — MCPセキュリティ基準（OpenClaw 12类隐患）、昇騰950対応（黄仁勋「灾难」反応）
- **Reference**: 2件 — Codex App SSH偷偷追加、低价GPT脆弱性
- **Skip**: 7件
- **Wiki更新状況**: 両ページとも既に対応済み（mcp-securityは04-18作成、deepseekは04-26更新）
- **温度差**: 36kr（新智元/NEXT趋势）がOpenClaw/MCPセキュリティとDeepSeek昇騰対応を先行報道。V2EXで実使用感ベースの評価が追従
