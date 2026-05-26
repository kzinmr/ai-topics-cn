# AI Topics China Wiki — Index

最終更新: 2026-05-26
エンティティ: 61, コンセプト: 118, ダイジェスト: 7, 比較: 2, ページ: 9
### 本日更新（2026-05-26 Newsletter Ingest: Zhihu Frontier Weekly — AI推論・エージェント・インフラ競争）
- `concepts/agentic-engineering.md` — **新規**: SE 3.0（Ahmed E. Hassan）、Tony Bai 7ルール、DeepSeek Harness `Model+Harness=Agent`、エージェント三巨頭サミット、価格階層型Agentアーキテクチャ。Vibe CodingからAgentic Engineeringへの第2世代移行を体系的に整理
- `concepts/diffusion-language-models.md` — **新規**: トークン不要の言語モデル探求。Cola DLM（@huMAnG0d）「連続的意味状態空間」仮説、ELFプロジェクト。自己回帰の逐次生成vs拡散の並列生成。評価基準・計算効率・エコシステム互換性の課題
- `entities/openai.md` — **更新**: OpenAI推論モデルが幾何学予想を証明（unit-distance-proof.pdf/remarks.pdf/cot.pdfの3ファイル公開）。数学界の反応（Will Sawin/Jacob Tsimerman/Daniel Litt）。「証明の希少性→潤沢性」パラダイム転換。GPT-5.5 vs DeepSeek価格戦略（非対称競争/約100倍価格差）
- `entities/anthropic.md` — **更新**: Andrej KarpathyがAnthropicでプリトレーニング部門に復帰。「スケーリング法則は終わっていない」シグナル。エージェントはツール調整できるが、ベースモデルの深いドメイン理解がなければ表面的知識の繋ぎ合わせに留まる
- `entities/gemini-google.md` — **更新**: Gemini 3.5 Flash発表への失望。価格が3.1 Proに近くトークン消費量も多い。コーディング能力への言及なし（LLM最大戦場で不在）。技術詳細不足
- `concepts/deepseek.md` — **更新**: Harnessチーム設立をAgentic Engineering文脈で位置づけ。`Model + Harness = Agent` パラダイムへのリンク追加
### 本日更新（2026-05-25 Active Crawl: Kimi/Local Deployment/Coding Assistants）
- `concepts/kimi.md` — **更新**: VIE構造解体正式開始(5/21-22/法務監査法人選定/A1提出Q3目標/年内上場)。さくらインターネットK2.6 API提供開始(5/20/Anthropic互換API/日本初本格展開/¥6.50-27.00 MTok)
- `concepts/china-local-deployment.md` — **更新**: llama.cpp MTP投機的デコーディング(1.7-2.2x)。Ollama v0.24.0 Codex App(iOS/Android)。Ollama v0.30.0-rc23(GGML廃止)。MiniCPM-V 4.6(9.6B/GPT-4o級1/50)。GLM-5ローカルデプロイ(400B-Q4)。SGLang v0.5.12 HiCache。TriAttention v0.2.0 GA
- `concepts/china-ai-coding-assistants.md` — **更新**: 通义灵码→QoderCNリブランド(5/20/Alibaba Cloud Summit)。Alibaba Cloud Summit Qwen3.7-Max発表(Agent-first/SWE-bench 70.6%)
### 本日更新（2026-05-24 Active Crawl: OpenClaw/MCP China/AI Model Filing）
- `entities/openclaw.md` — **更新**: v2026.5.19/5.20/5.22-beta.1週3回メジャーリリース(ブラウザモーダル/Policy/Discord/cron/プリウォーム5ms)。Hermes Agent OpenRouter日次トークン消費でOpenClaw逆転(458B vs 173B)。★374K。エコシステム拡大(DigitalOcean/MiniMax MaxClaw/Alibaba Cloud/Qwen 3.5蒸留)。脆弱性パッチ済み
- `concepts/mcp-china.md` — **更新**: Alibaba Cloud Summit全製品MCP化/Qwen3.7-Max/ModelScope MCP広場千種。ByteDance火山引擎MCP Server OSS(100+MCP)。Tencent MCP Gateway(ゼロコード)/MCP-FLOW(99.2%)。AAIF 43新メンバー。MCP STDIO脆弱性(200K+server)。SEC 8-K初開示。エコシステム9,400+Server
- `concepts/china-ai-model-filing.md` — **大幅更新**: 智能体規範応用意見(5/8/3省庁/AI Agent初政策/19シーン)。清朗行動(4/30〜8月/ByteDance3摘発)。補助金(上海徐匯最高500万/深圳模型券年200万)。擬人化互動服務管理暫行辦法(5省庁/7/15)。备案868件/登記530件
### 前日更新（2026-05-23 Active Crawl: Agent Ecosystem/VRAM Optimization/AI Regulation）
- `concepts/china-ai-agent-ecosystem.md` — **更新**: Agent三巨頭サミット(5/18/智譜AutoGLM 3.0+Qwen Agent v2+DeepSeek R2)、百度文心5.1(DAA指標/自律エージェント特化)、火山引擎Agent Plan、百融RaaS(硅基員工10万+)、360 Agent Studioを追加
- `concepts/vram-optimization.md` — **更新**: 209→341行へ大幅拡張。TriAttention v0.2.0、Ollama v0.30.0アーキテクチャ移行、SGLang v0.5.12 DeepSeek V4 HiCache、DeepSeek V4 vLLM最適化詳細、北大GQLA、昇騰910C FlashAttention、PagedEvictionを追加
- `concepts/china-ai-regulation.md` — **更新**: NDRC AI立法研究開始(5/22)、《人工智能应用伦理安全指引1.0》(5/19)、ATH 1.0(5/7)、清朗行動摘発・AI代写種草笔记判決を追加
### 前日更新（2026-05-21 Active Crawl: Qwen/Doubao/ChatGLM deepdive）
- `entities/qwen.md` — **更新**: Qwen3.7-Max(5/20/Agent-first自律実行最適化)、Qoder 1.0(自律開発Desktop)、Qwen3.5-LiveTranslate-Flash(音声同時通訳)、Qwen Code v0.16.0
- `concepts/doubao.md` — **更新**: MAU3.45億(訂正)、Agent Plan有料サブスク(月額68/200/500)、AI誤導訴訟(退改航)
- `concepts/chatglm.md` — **更新**: GLM-5.1 8時間自律実行ベンチマーク、ZCubeアーキテクチャ(推論15%向上)、「Chinese Anthropic」戦略(CEO張鵬5/13)、時価総額5000億HKD
- `concepts/vibe-coding-china.md` — **更新**: Karpathy Anthropic加入(5/19)、腾讯吐司(Toast/应用宝)、灵珠二测(DS V4統合)、36kr三阶段衰退曲线(Node.js 1.9万行AI生成PR事件)、KDD 2026 Workshop SE 3.0、通义灵码2.5+Qwen3-Coder-Next
- `concepts/kimi.md` — **更新**: Kimi WebBridgeリリース(5/15/ブラウザAgent)、国有資本参入(国智投・北京AI基金・中国移動/5/19)、Cursor Composer 2.5(Kimi K2.5ベース)、IPO紅籌架构拆除開始
- `concepts/mcp-chinese-tools.md` — **大幅更新**: 新华财经MCP(国家級金融)、钉钉MCP广场6000+、支付宝MCP Server(初決済)、同花顺iFinD MCP、天翼云MCP托管(3大キャリア初)、华为云Serverless+MCP
### 前日更新（2026-05-17 Active Crawl: OpenClaw / China AI Agent Ecosystem / China AI Coding Assistants）
- `entities/openclaw.md` — **更新**: 5月ベータ連鎖追加（v2026.5.10/5.12/5.14 Stable Release Branch分岐/パッケージManager型安全化/Gatewayヘルスチェック改善）。GitHub Stars 372K
- `concepts/china-ai-agent-ecosystem.md` — **更新**: 百度Create2026セクション追加（心響App/DAA指標/Token Factory/Harness Engineering）。36kr Agentファースト大分析（Token階層/Alibaba ATH/腾讯Agentインフラ戦略）
- `concepts/china-ai-coding-assistants.md` — **更新**: Trae SOLO Mobile三端同期（iOS/PhonePairing/飞书連携/Windows版）。腾讯CodeBuddy計費改定（WorkBuddy統合/CloudAgent/NES写一补十）。36kr「TRAE SOLO龙虾化」分析
### 前日更新（2026-05-16 Active Crawl: Tencent Hunyuan / AI Regulation / Yi（零一万物））
- `concepts/yi.md` — **更新**: Pre-IPO資金調達・香港上場準備（5/9/智譜AI・MiniMax上場後/2024年収益1億元+/2025年Q1が通年に迫る）。万智平台2.5→Super Employee 30+種/5大産業展開。棋譜元戦略:B端特化IPO経路
- `concepts/china-ai-regulation.md` — **更新**: 智能体规范应用与创新发展实施意见追加（5/8/CAC+NDRC+MIIT/中国初Agent専用政策/19シナリオ/2027年70%目標/5都市）。国務院2026年度立法計画でAI総合立法加速(5/11/初の中国版AI法公式表明)。亞信安全Agent Trust Framework(ATF)追加
### 前日更新（2026-05-16 Newsletter Ingest: Tech Taiwan MediaTek T-Glass / DeepSeek V4評価）
- `entities/mediatek.md` — **更新**: T-Glass（ガラス基板）供給囲い込み戦略セクション追加。Agentic AI台頭で基板供給逼迫、MediaTekがBroadcom/Nvidiaに先行しGoogle TPU・AI ASIC受注優位性確保
- `concepts/gpu-sanctions-china.md` — **更新**: DeepSeek V4性能評価（米国比8ヶ月遅れ）、Ascend推論適応・Blackwell密輸学習セクション追加。T-Glass供給戦略とMediaTek先行投資セクション追加
- `entities/qwen.md` — **更新**: 淘宝EC統合5/11、Qwen Code v0.15.11 5/13、Deep Research正式版5/6、overthinkingバグ5/12、QuestMobile MAU1.66億、Zhenwu AI韶関10K基
- `concepts/doubao.md` — **更新**: 有料サブスク全国議論5/11-15/Morgan Stanley年収1-15億ドル試算、豆包输入法Mac版5/13、火山引擎MaaSシェア49.5%、AI誤導訴訟5/14、栄威家越提携深化
- `concepts/chatglm.md` — **更新**: GLM-5.1継続最適化、Z.aiブランド海外正式運用、OpenClaw論争決着/Hermes SillyTavern対応、DeepSeek競合戦略

### 前日更新（2026-05-14 Active Crawl-47: DeepSeek V4.1 / MCP Chinese Tools）
- `concepts/deepseek.md` — **大幅更新**: V4.1正式発表セクション追加（2026年6月リリース予定/全モーダル画像+音声入力/MCPネイティブ対応/エンタープライズツールチェーン）。500億元大型調達セクション追加（評価額515億ドル/梁文鋒40%出資/Tencent60億元2%出資/大基金交渉中）
- `concepts/mcp-chinese-tools.md` — **大幅更新**: 飛書公式MCP（End user call remote MCP server/Beta）セクション追加。腾讯云MCP Serverマーケットプレイス追加。mcp-notify通知MCP Server追加。中国MCP生態の特徴を「コミュニティ→公式対応への急速移行」として更新し、番号振り直し

### 前日更新（2026-05-13 Active Crawl-46: MCP中国生態 / Vibe Coding / 大模型备案制度）
- `concepts/mcp-china.md` — **更新**: MCP 8大プラットフォーム比較（百度MCP World 56,757/魔搭10,000+/騰訊云/字節/Dify/Coze/Jina AI/FireCrawl/Tabby資産）、CVE-2026-30615、MCP Dev Summit Beijing、Gateway必須性追記
- `concepts/vibe-coding-china.md` — **更新**: Code w/ Claude 2026（5/7）Opus 4.7 SWE-bench 82%/Claude Code全自動成功率51%、Willison融合論、Claude Code 35%/Cursor 28%/Windsurf 17%（5月シェア調査）
- `concepts/china-ai-model-filing.md` — **大幅更新**: 清朗·整治AI应用乱象（4/30 4ヶ月行動/备案未実施第1目標）、第十七批深度合成服务算法备案（5/6 累計〜7,000件）、地方政府备案補助金7地区比較表（広州海珠/深圳各区/上海徐汇/南京玄武）、深圳市训力券年間最大1,000万元

### 前日更新（2026-05-12 Active Crawl-45: 国家Agent政策 / ローカル推論新ツール / 中国OSSコミュニティ最新動向）
- `concepts/china-ai-agent-ecosystem.md` — **更新**: セクション6新設「国家Agent政策とプラットフォームアップグレード」。中国初の智能体専項政策《智能体规范应用与创新发展实施意见》（5/8）、腾讯云全栈企業級Agent能力アップグレード（4/28）、BoAgent（5/8/金融向け）、百融智能RaaS 10万硅基員工
- `concepts/china-local-deployment.md` — **更新**: セクション追加「2026年5月上旬追加情報」。oMLX(Apple Silicon推論サーバー/M4 Maxで70B級Q4動作)、LocalClaw零配置Agentランタイム、ERNIE 5.1ローカル用GGUF/GPTQ公開、DeepSeek-V4 TCO分析
- `concepts/china-open-source-ai.md` — **更新**: セクション新設「2026年5月最新動向：魔乐発足・Ling-2.6-1T開源・太湖共识」。MoLeコミュニティ正式発足(4/29/Linux Foundation AAIF/37社)、蚂蚁Ling-2.6-1T MIT公開(4/30)、ERNIE 5.1発表(5/9)、太湖共识(4/25/7社)、中关村AI开源联盟(5/6/20社)

### 前日更新（2026-05-12 Newsletter Ingest: ChinAI #358 / 豆包有料化 / 面壁智能 / CAICTセキュリティ基準）
- `entities/doubao.md` — **大幅更新**: 有料サブスクリプション3段階発表（¥68/200/500月）。世論反応（「豆包 笨还收费」）。算力コスト圧力（日均120兆Token、年コスト数百億規模）。業界価格トレンド（智譜・騰訊は値上げ、DeepSeek・千問は無料/値下げ）。Token経済の課題。QuestMobileデータ（MAU3.45億、DAU1.5億）
- `entities/modelbest.md` — **新規**: 「AGI五小龍」の一角。密度定律（智能密度=能力/能耗、100日倍増）。端側モデル路線（MiniCPMシリーズ）。24億→80億→90億パラメータでGPT-4o級性能。清華THUNLP連携。車載AI・具身智能商用展開。国産チップ（華為昇騰/寒武紀等）最適化
- `concepts/on-device-ai-agent-security.md` — **新規**: CAICT AI Safety Benchmark 2026 Q1。端側AIエージェント安全基準テスト。内容安全率95%+、行為安全率に課題（実行率40%+）。1,200件テスト（6次元×2200件）。ソーシャル/EC/金融/Web検索シナリオ

### 前日更新（2026-05-11 Active Crawl-44: OpenClaw v2026.5.x / Cursor 3.3 / Kimi K2.6価格 / CodingPlan改定 / Lingma IDE独立）
- `entities/openclaw.md` — **更新**: v2026.5.7〜v2026.5.3全5リリース（SecretRef強検証/Foundation移行/OAuth修正/全文検索/file-transfer/steerコマンド/Commitments自動リフレッシュ）。36krセキュリティフォローアップ（サプライチェーンリスク/SOE生OpenClaw禁止/監査要求）
- `concepts/china-coding-agents.md` — **大幅更新**: Cursor 3.3/3.2/3.1全バージョン（Agents Window/Composer 2自研MoE 4倍速/best-of-n）。Kimi K2.6正式価格（¥39/159/559）。Trae SOLO MTCモード独立Web版（シェア41.2%首位）。Lingma IDE独立移行（Agentic Ask/NES/Inline Chat）。CodingPlan改定。主要比較表2026年5月版更新
- `concepts/coding-plan.md` — **更新**: Cursor+Lite Plan黄金パターン。二極分化（¥39-40 vs ¥99-559）。GLM-5.1統合遅延
### 前日更新（2026-05-10 Active Crawl-43: Qwen SAE/QwenPaw / Doubao wiki確認 / VRAM optimization確認）
- `entities/qwen.md` — **更新**: Qwen-Scope記述修正（Attention可視化→SAE Model Steeringに修正）、QwenPawセクション新設（CoPaw改名/GitHub★16.4K/v1.1.6/MultiAgent協調/QwenPaw-Flash-9B）
### 前日更新（2026-05-09 Active Crawl-42: Kimi $20B funding / Tencent Hunyuan OpenRouter #1 / Dify v1.14 GA）
- `concepts/kimi.md` — **更新**: 資金調達セクション新設（5月7日20億ドル調達完了、評価額200億ドル超、ARR 2億ドル突破、半年累計39億ドルで中国最大）
- `entities/tencent-hunyuan.md` — **更新**: OpenRouter週間ランキング再び1位（5月7日週、Hy2比10倍超、CodeBuddy/WorkBuddy 16.5倍急増、株価3%上昇、高盛Buy評価 HK$700）
- `concepts/dify.md` — **更新**: v1.14.0 GA正式リリース、Agent Skills/Sandbox Runtime/Skill Editor Production Ready
### 前日更新（2026-05-08 Active Crawl-41: China AI Regulation / DeepSeek V4 / Coze）
- `concepts/china-ai-regulation.md` — **更新**: 第17批深度合成服務算法备案（5月6日公開）セクション追加。CAC通過式監管モデル継続。デジタル仮想人草案パブコメ終了を反映。
### 前日更新（2026-05-07 Active Crawl-40: Qwen3.6 / Doubao Seed-2.0-lite全模态 / ChatGLM GLM-5-Turbo）
- `entities/qwen.md` — **更新**: Qwen3.6-235B-A21B-preview DeepSeek V4超え(OpenRouter)。Qwen Code v0.14.x Agent機能（子Agent自律実行・Telegram/钉钉連携）。Lingma IDE独立版（VS Codeプラグイン非推奨）。百煉Platform上Agent動的ツール呼び出し。Alibaba社内AI統制強化（20人CodeFreeze/OKR連動）
- `concepts/doubao.md` — **更新**: Seed-2.0-lite初の全模态理解モデル（5月6日: 音声/動画/画像/テキスト統合、19言語音声認識、14言語翻訳）。HiPhO/MedXpertQA Pro超え。GUI操作対応。有料サブスク3段階（68/200/500元/月）。車載AI 700万台。月活2.27億・DAU1億
- `concepts/chatglm.md` — **更新**: GLM-5-Turbo新登場（Agent/龙虾特化訓練層最適化）。Scaling Pain技術ブログ（Agent推論スループット132%向上・異常出力率万分の三未満）。GLM-5.1 SWE-bench Pro 58.4%（GPT-5.4超え）
### 前日更新（2026-05-06 Active Crawl: MCP 中国生態 / Vibe Coding → Agentic Engineering）
- `concepts/mcp-china.md` — **大幅更新**: Anthropic MCP実践ガイド（Tool Search 85%+削減、3パターン接続）。Cloudflare 2ツールx2500エンドポイント。SDK月間DL 3億回。中国コミュニティ成熟評価。MCP+A2A+AP2+ACPエコシステム拡大。
- `concepts/vibe-coding-china.md` — **大幅更新**: Karpathy@Sequoia AI Ascent 2026「思考外注可但理解不可」「LLM是幽灵不是動物」。Agentic Engineering第2世代へ移行。Ahmed E. Hassan SE 3.0(SASE)体系化。Tony Bai移行サバイバルガイド7ルール。

### 前日更新（2026-05-05 Active Crawl: China AI Agent Ecosystem / AI Coding Assistants）
- `concepts/china-ai-agent-ecosystem.md` — **更新**: 2026年5月最新動向追加（推論爆発/Deloitte推論2/3/GPU高騰/DeepSeek V4 $0.30 vs GPT-5.5 $30/OpenClaw12脆弱性/SOE禁止/政府補助金1000万元）
- `concepts/china-ai-coding-assistants.md` — **更新**: 2026年5月最新動向追加（Trae SOLO独立Desktop+MTC/通义灵码Agentic Ask+NES/Lingma IDE正式版/VS Codeプラグイン非推奨）

### 前日更新（2026-05-05 Newsletter Ingest: HiFloat4 / BadSkill / Import AI 454 / China AI Bulletin 3）
- `concepts/hifloat4-format.md` — **新規**: 華為Ascendチップ用4bit訓練フォーマット。HiFloat4 vs MXFP4比較（BF16比≈1.0% vs ≈1.5%）。RHTのみでBF16損失1%以内。輸出規制下の中国ハード効率化トレンド。
- `concepts/badskill-agent-backdoor.md` — **新規**: AIエージェントスキルエコシステムへのサプライチェーン攻撃。Model-in-Skill Poisoning。攻撃成功率99.5%（汚染率3%）。既存プロンプトインジェクション防御では不十分。

### 本日更新（2026-05-04 Active Crawl: DeepSeek識圖模式 / Hunyuan数字中国峰会 / Dify資金調達・v1.14 RC）
- `concepts/deepseek.md` — **大幅更新**: 識圖模式（Thinking with Visual Primitives, 7000倍圧縮）。36kr百度交渉失敗・V4学習障害・初自律収益。無錫AI基盤導入（500+模型）。WPS Office統合
- `entities/tencent-hunyuan.md` — **更新**: 数字中国建設峰会実機初展示（WorkBuddy/QClaw/OpenClaw等5製品）。WorkBuddy: 1分WeChat Work接続。QClaw: Hermes対応/DeepSeek V4-Pro切替可能。SkillHub AI Skillsコミュニティ
- `concepts/dify.md` — **大幅更新**: 3000万ドル調達（累計4150万ドル・評価額1.8億ドル）。v1.14 RC: Agent x Skills（Sandbox Runtime/Skill Editor）。v1.13.0: Human-in-the-Loop。v1.9.2: 双方向MCP。Creator Center。日本京進グループ協業
### 前日更新（2026-05-03 Wiki Health Auto-Fix: 孤児ページ2件修正）
- `index.md` — **孤児ページ登録**: `entities/mike-stonebraker` と `entities/tffinfer` をエンティティセクションに追加（エンティティ: 59 → 61）
- `concepts/kimi.md` — **大幅更新**: K2.6 OpenRouter週間1.88兆トークン処理（全球1位）。K3開発詳細（2.5Tパラメータ・KDA注意機構・Q3 2026予定）。KVV / PrfaaS新プロダクト。競合ポジショニング表（vs DeepSeek V4 Pro / Qwen3.6 Max）。企業指標（$18B評価額・$100M ARR）
- `concepts/coding-plan.md` — **大幅更新**: 2026年5月市場激変—阿里百煉Lite(¥40)完全廃止、智譜GLM二度値上げ(+40%)、火山方舟初回購入日次フラッシュセール化、MiniMax「Token Plan」リブランド、小米MiMo参入(4/3)。Kimi Code CLI料金(¥39/159/559)。おすすめ選択肢表
- `concepts/doubao.md` — **更新**: 豆包4.0リリース（動画分析・ローカルオフラインAI・一発购物EC統合）。月活2.27億・リテンション率44.5%（中国AIアプリ1位）。静默アップグレードで128Kコンテキスト対応
### 前日更新（2026-05-02 Wiki Health Audit + V2EXトリアージ + Zhihu Frontier統合）
- `concepts/ai-coding-reality.md` — **新規**: V2EX技術議論からAIコーディングの実態（会話モード主流、Agent自律はデモ段階、古法编程の存在、生成コード保守問題）
- `concepts/spec-driven-development.md` — **新規**: SDD実践課題（OpenSpec「正しい废话」問題、Spec-コード乖離、Harness文書矛盾）
- `concepts/rag-reality.md` — **新規**: RAG実用性問題（IT運用知識検索の精度不足、Obsidian/AnythingLLM比較、AI産業への懐疑論）
- `concepts/anthropic-ip-ban.md` — **新規**: AnthropicのIP封鎖実態とKYC導入（双ISP罠、ipapi.is/ipinfo矛盾、ToDesk副作用、中国政府ID認証問題）
- `concepts/copilot-changes.md` — **新規**: Copilot ProのOpus除外、年払廃止、新規課金停止、Microsoft「龙虾计划」
- `concepts/vibe-coding.md` — **新規**: Vibe Coding実践例（非開発者のゲーム開発、記録ツール開発、限界と展望）
- `concepts/local-inference-optimization.md` — **新規**: 8GB VRAMで30Bモデル（7倍高速化、3→21 tok/s、GGUF最適化）
- `entities/mediatek.md` — **skeleton→complete**: Tech Taiwan記事統合。MediaTek TSMC人材でGoogle TPU受託、Broadcom対抗戦略
- `entities/deepseek.md` — **enriched**: Zhihu Frontier分析統合。「修路人」メタフォア、Engram/TechLang詳細、CUDA→CANN移行戦略
- `entities/qwen.md` — **enriched**: Qwen3.6-35B-A3Bがツール呼び出しベンチマーク首位（69/72、96%精度）
- `entities/kimi-moonshot.md` — **enriched**: Zhihu Frontier K2.6分析統合。「人間のようなエージェント」評価、推論モード80K超過問題
- `concepts/gpu-sanctions-china.md` — **enriched**: DeepSeek V4 TileLang/Engramセクション追加。CUDA→CANN移行戦略
- `concepts/china-ai-landscape.md` — **enriched**: 2026年4月技術収束トレンド。基礎モデルモート消滅分析
- `x-accounts/boboceng.md`, `x-accounts/plantegg.md`, `x-accounts/ruanyf.md` — **修正**: source_lang: zh → zh-CN
### 前日更新（2026-05-02 Active Crawl: OpenClaw急成長・Cursor 3 Design Mode / 零一万物海外展開）
- `entities/openclaw.md` — **大幅更新**: 85K→367K★急成長追跡。SOUL.md/ClawHub/People Wiki/Commitments機能追加。NVIDIA/Cerebras/DeepInfraプロバイダ。Codex Computer Use。中国移動・通信学会公式セキュリティガイド。Gateway起動高速化(25→2s)
- `concepts/china-coding-agents.md` — **更新**: Cursor 3 Design Mode/Git Worktree/Agents Window。Cursor Composer 2(Kimi K2.5/$50B)。OpenClaw→Claude Code/Codex CLI/Gemini CLI 3Agent協調。K2.6 Claw Groups
- `concepts/yi.md` — **更新**: カザフスタン大統領会談。香港スマートガバメントラボ入選。2025年収益数倍成長確認。李開復CEOがto B営業最前線に
### 前日更新（2026-05-02 Newsletter Ingest: MediaTek Google TPU参入）
- `entities/mediatek.md` — **新規作成**: Tech Taiwan独占報道。MediaTekがTSMC CoWoSベテラン人材でGoogle TPUビジネスに参入、Broadcomに対抗。株価1ヶ月で86%急騰。AI半導体サプライチェーン構造変化の重要シグナル
### 前日更新（2026-05-01 Active Crawl: Qwen3.6戦略転換・Qwen Code / 中国ローカルデプロイ最新動向 / VRAM最適化新技術）
- `entities/qwen.md` — **更新**: Qwen3.6-Max-Previewクローズドウェイト化、Qwen Code v0.14.x子Agent機能、Qwen OAuth無料枠終了、Alibaba OSS→プロプライエタリ戦略転換
- `concepts/china-local-deployment.md` — **更新**: Ollama 169k Stars/v0.17.7、Qwen3.6-35B-A3Bローカル推論(アクティブ3B/RTX4090フル動作)、DeepSeek-V4 910C 8基~50tok/s
- `concepts/vram-optimization.md` — **更新**: Qwen3.6-35B-A3B MoE VRAM特性(~12GB/Q4)、DeepSeek-V4 Engram Memory(40%削減)、TriAttention(スループット2.5倍)
### 前日更新（2026-04-30 Active Crawl: DeepSeek V4値下げ・増資・CAICT / Tencent Hunyuan OpenRouter1位・組織再編 / ChatGLM-5.1詳細・決算）
- `entities/openai.md` — **大幅更新**: OpenAIのクラウド戦略転換（Microsoft Azure独占権終了→Amazon AWS移行）、AnthropicとのARR逆転（$25B vs $30B+）、OpenRouter Token使用量比較（ClaudeがGPTを32%上回る）、GPT-5.5リリース、Amazonとの$1,380億/8年契約
- `pages/openai-codex-infrastructure.md` — **セクション追加**: Codex AppのSSH遠隔開発機能（V2EX発見情報、`~/.codex/config.toml`設定）、中国国内でのCodexローカルインストールとGPT-5-Codex利用ガイド（`npm install -g @openai/codex`）
- `concepts/mcp.md` — **セクション追加**: Z.AI（智譜AI）製MCPサーバー（zai-mcp-server/GLM-4.6Vベース画像認識、web-reader、web-search-prime）のClaude Code統合事例
- `entities/tencent-ai.md` — **セクション追加**: 騰訊のAI不安と10年前のQQボット戦略分析、10億元投資の混元大モデル vs ユーザーは旧QQボットを好むパラドックス
### 前日更新（2026-04-29 Active Crawl: 认知债/規制詳細/OSSラッシュ）
- `concepts/vibe-coding-china.md` — **大幅更新**: 認知債務（Cognitive Debt）セクション追加。36kr三段階衰退曲線、Anthropic RCT（理解1.7倍低下）、Triple Debt Model（arXiv:2603.22106）、Collina 1.9万行PR事件
- `concepts/china-ai-regulation.md` — **大幅更新**: AI拟人化互动服务管理暂行办法（7/15施行）詳細：禁止行為8条・未成年保護・罰則体系。AI科技伦理审查与服务办法（工信部联科75号）詳細：4段階審査・3類型高リスクAI活動・国家科技倫理登記
- `concepts/china-open-source-ai.md` — **大幅更新**: 4月後半モデルリリースラッシュ追加。DeepSeek V4 Preview(1M ctx/Ascend)、腾讯Hy3(295B MoE)、Qwen3.6-35B-A3B、Qwen3(8モデル/4/29公開/AIME25=81.5 SOTA)、MiniMax 2.7。中国OSS勢力図（Alibaba vs DeepSeek二極化）
### 前日更新（2026-04-28 Triage Batch 2）
- `concepts/agent-team-swarm/index.md` — **セクション追加**: 4AIチーム協調開発の実装パターン詳細（ファイルシステム通信、強制チェックポイント、Token節約75%、agentGroupディレクトリ構造）
- `concepts/mcp-chinese-tools.md` — **セクション追加**: MCP Server実践開発ガイド（30分PDFリーダー構築、TypeScript+pdf-parse、StdioServerTransport、CJS/ESM互換処理）
- `concepts/agent-skills.md` — **セクション追加**: 「Prompt已死、Skill当立」パラダイムシフト議論、Cursor AI Skills×Flutter自動生成実戦
- `pages/industry-trends.md` — **セクション追加**: Claude 4.6 vs GLM-5「毒題」チャレンジ、Kimi→GLM→Claude競争図変化分析
- `concepts/china-coding-agents.md` — **セクション追加**: JetBrains IDEAでのClaude Code統合（claude-code-acp、Plan/Actモード、MCPツール対応）
- `concepts/china-ai-agent-ecosystem.md` — **セクション追加**: n8n自動化ワークフロー（複雑知識→小红书科普カード→ローカル保存）
- `concepts/china-local-deployment.md` — **セクション追加**: 中国国内でのGPT-5-Codexローカルインストール実用ガイド
- `entities/glm-zhipu.md` — **セクション追加**: GLM-4.7フロントエンド生成能力実測レビュー
- `concepts/model-pricing.md` — **セクション追加**: 複数LLMキー管理の経済性分析（GLM/MiniMax/Claude最適化）
- `entities/claude-code.md` — **セクション追加**: Claude Code効率化Tips 10選（Skills最適活用、コンテキスト境界、バッチ処理等）
- `concepts/vibe-coding.md` — **セクション追加**: Vibe Coding概念大全（LLM/ファインチューニング/推論文脈での位置づけ）
- `pages/rag-vector-db.md` — **セクション追加**: RAG技术全栈指南第一章（検索拡張生成の基礎と実装）
- `entities/tencent-ai.md` — **セクション追加**: 騰訊のAI不安と10年前のQQボット戦略分析
### 前日更新（2026-04-27）
- `concepts/mcp-china.md` — **大幅更新**: MCP月間DL 97M突破、GitHub公式MCP Server v1.0.2、GLM-5.1 MCP Atlas世界首位（71.8%）、MCP Auth標準化、Streamable HTTP、Docker MCP Toolkit、Azure MCP 2.0.0、Qwen3.6-35B-A3B MCPMark 37.0%
- `concepts/china-ai-agent-ecosystem.md` — **大幅更新**: 「百蝦大戦」深水区、Coding Agent OS基盤化、CLI復活トレンド、Hermes Agent中国急成長、マルチAgent主流化、市場データ（12.96兆Token/週）、3層構造確定版
- `concepts/mcp-chinese-tools.md` — **新規**: 中国MCPツールエコシステム（钉钉公式MCP OpenAPI/12 Profile、飞书MCP 8ツール、企微MCP、OpenClaw China 7チャネル、picoclaw MCP）

## エンティティ (Entities)

- [[anthropic|anthropic]]
- [[agi-bot|AgiBot（智元机器人）— 中国人形机器人出货No.1企業（5,168台/2025年）]]
- [[baichuan-ai|baichuan-ai]]
- [[baidu-ernie|Baidu（百度）— 文心一言/ERNIEと中国AI検索大手]]
- [[biren-technology|biren-technology]]
- [[cambricon|cambricon]]
- [[claude-code|Claude Code — AIコーディングエージェント]]
- [[claude-design|claude-design]]
- [[claude-opus-4-7|Claude Opus 4.7 — Anthropic最新フラグシップモデル]]
- [[coze|Coze（扣子）— Agent WorldプラットフォームとOSSエージェントエコシステム]]
- [[creatorweave|CreatorWeave — ローカル優先のブラウザ創作ワークスペース]]
- [[cursor|cursor]]
- [[dji|DJI（大疆创新）— ドローン市場支配の巨人（全球シェア70-80%）]]
- [[deepseek|deepseek]]
- [[doubao-bytedance|豆包/ByteDance（Doubao）— 字節跳動のAIモデル・コーディングプラットフォーム]]
  - [[doubao|doubao]]
  - [[echoic|Echoic — オープンソースAI口语練習ツール]]
  - [[fourier-intelligence|Fourier Intelligence（傅利叶智能）— リハビリ特化ヒューマノイド（GR-1/GR-3）]]
  - [[mini-cc|mini-cc — 轻量级AI编程智能体]]
  - [[openmythos|OpenMythos — Claude Mythosアーキテクチャ逆推开源]]
  - [[springai-alibaba|SpringAI Alibaba — Java向けAI Agent開発フレームワーク]]
- [[fudan-nlp-agent-survey|复旦NLP — 80ページ大模型Agent総合論文]]
- [[gemini-google|Gemini/Google — Google AI基盤モデルとオープンソースGemma]]
  - [[glm-zhipu|智谱GLM（ChatGLM）— 中国最大級オープンソースLLM]]
  - [[gpt-5-5|GPT-5.5 — OpenAI最新フラグシップモデル（2026年4月）]]
  - [[horizon-robotics|horizon-robotics]]
- [[iflytek|iflytek]]
- [[kimi-moonshot|Kimi（月之暗面/Moonshot AI）— Claude Code代替として急成長する中国国籍LLM]]
- [[kimi-k2-6|Kimi K2.6 — 月之暗面开源旗舰模型]]
- [[kilo|Kilo（キロコード）— オープンソースAIコーディングプラットフォーム、2.3M+開発者、500+モデル]]
- [[qwopus-3-5|Qwopus 3.5 — Qwen3.5-27Bベース社区微调モデル]]
- [[llama-meta|Llama（Meta）— Meta AIのオープンソースLLMファミリ]]
- [[metax|metax]]
- [[mike-stonebraker|Mike Stonebraker（マイク・ストーンブレーカー）— データベースの父、AI Agentへの警鐘]]
- [[mediatek|MediaTek（聯発科技）— TSMC CoWoSベテラン陣営でGoogle TPU参入、Broadcomに対抗]]
- [[minimax|minimax]]
- [[moore-threads|moore-threads]]
- [[openai|openai]]
- [[openclaw|openclaw]]
- [[qwen|qwen]]
- [[rockchip|rockchip]]
- [[sensetime|sensetime]]
- [[soul-killer|Soul Killer — Claude Code用Galgame Agent & Skill作成器]]
- [[stepfun|stepfun]]
  - [[tencent-ai|tencent-ai]]
  - [[tencent-hunyuan|腾讯混元 (Tencent Hunyuan) — 混元3.0/Hy3大模型、295B MoE架构]]
  - [[tencent-qclaw|Tencent QClaw — OpenClawベースの極簡AIエージェントプラットフォーム]]
- [[tffinfer|TFFInfer — C++製LLM推論フレームワーク]]
- [[ubtech-robotics|UBTECH Robotics（优必选）— 中国初の人形ロボット上場企業（HK.9566、1,079台/2025年）]]
- [[unitree-robotics|Unitree Robotics（宇树科技）— 世界No.1二足歩行ロボットメーカー（5,500台/2025年）]]
- [[mihoyo|miHoYo（米哈游）— 中国ゲーム・AI企業]]
- [[nowen-video|Nowen-Video — 軽量家庭メディアサーバー（Go+React+Docker）]]
- [[spacex|SpaceX — 宇宙輸送・AIインフラ企業]]
- [[verisilicon|verisilicon]]
- [[xiaoice|Xiaoice (小氷) — Microsoft発の中国チャットボット企業]]
- [[xiaomi-mimo|小米MiMo — 中国AIモデル企業]]
- [[xpeng|XPeng（小鹏汽车）— EV+ロボット+飛行車両統合企業（PX5/IRON/Land Aircraft Carrier）]]

## コンセプト (Concepts)

- [[agent-skills|Agent Skills — AIエージェントのモジュール型能力システム]]
- [[agentic-engineering|Agentic Engineering — Vibe Codingの第2世代（SE 3.0/Harness Engineering/自律開発パラダイム）]]
- [[ai-agent|AI Agent（智能体）— 中国語圏での議論動向]]
- [[agent-team-swarm|AI Agentチーム・スワームパターン — 複数AIエージェント協調開発]]
- [[ai-inner-os|AI Inner OS — AI CLIツールのインナーモノローグ可視化プラグイン]]
- [[ai-safety-subconscious|ai-safety-subconscious]]
- [[ai-video-generation|AI短视频自动生成 — 一人開発の技術スタックと実践知]]
- [[beike-ai-customer-service|贝壳AI客服 — MCP + Skillを活用したAIカスタマーサービス]]
- [[cc-monitor|cc-monitor — Claude Code リアルタイムToken消費モニター]]
- [[chatglm|ChatGLM (智谱清言) — Zhipu AIの中国語圏事情]]
- [[china-ai-model-filing|中国AI模型备案制度 — 大模型备案・算法备案]]
- [[china-ai-superapp-race|china-ai-superapp-race]]
- [[china-palantir|china-palantir]]
- [[chinai-348-compute-year-review|ChinAI #348 — 2025年中国計算力産業回顧：熱狂、成長の痛み、価値回帰]]
- [[chinai-newsletter|ChinAI Newsletter — 中国AI業界動向の英語翻訳・解説]]
- [[cli-agent-patterns|CLI vs MCP vs GUI — エージェント時代のインタラクションパターン]]
- [[claude-code-router|claude-code-router — モデル切り替えルーター]]
- [[claude-design|Claude Design — Anthropicのデザインツール（Figma/Canva競合）]]
- [[coding-plan|Coding Plan（编程计划）— 中国発AIコーディングサブスクリプションモデル]]
- [[dflash|DFlash — ブロック拡散モデルによる6倍推論加速（speculative decodingの新世代手法）]]
- [[diffusion-language-models|Diffusion Language Models — トークンを越える連続潜在表現]]
- [[function-calling|Function Calling（関数呼び出し）— LLMと外部APIを接続する核心メカニズム]]
- [[gpt|GPT — OpenAIの言語モデルシリーズ]]
- [[multimodal|多模态/Multimodal — 複数のモダリティを統合するAI]]
- [[quantization|量化/Quantization — LLMの効率的な推論技術]]
- [[rlhf-alignment|RLHF/对齐 — 人間のフィードバックによるLLMの対話最適化]]
- [[fine-tuning|微调/Fine-tuning — 大規模モデルの特定ドメイン適応]]
- [[glory-ai-phone|荣耀AI手机专访 — 端侧AIのキャリアと未来]]
- [[gomcp|GoMCP — Go言語MCP Serverフレームワーク]]
- [[gpu-sanctions-china|中国GPU制裁・半導体輸出制限 — 米中AI競争と国産化動向]]
- [[harness-engineering|Harness Engineering — LLM Agentの外化（Externalization）パターン]]
- [[implicit-structure-collapse|隐性结构塌缩 — LLM出力が平均的構造に塌縮する現象と対策]]
|- [[llm-security|LLM应用安全 — 大语言モデルセキュリティ入門]]
|- [[langchain|langchain]]
- [[mcp|MCP（Model Context Protocol）— AIツール連携の標準規格]]
- [[mcp-china|MCP中国生態 — 中国での採用状況と独自の発展パターン]]
- [[mcp-security|MCPセキュリティ — OWASP Top 10とMSB安全基準]]
- [[ollama-criticism|Ollama批判論争 — オープンソース倫理と代替ツール]]
- [[open-source-death|open-source-death]]
- [[page-index|PageIndex — ベクトルなし推論ベースRAGフレームワーク]]
- [[rag|rag]]
- [[spokenwoz|SpokenWOZ — 达摩院Dialogue Agents基盤]]
|- [[token-pricing-trend|Token価格上昇トレンド — 中国AI市場の計算力インフレ]]
|- [[transpec|Transpec — 仕様駆動開発フレームワーク間変換ツール]]
- [[turboquant|TurboQuant — Google Researchの超高効率ベクトル量子化アルゴリズム（KVキャッシュ6×圧縮）]]
- [[vector-db|Vector DB（向量数据库）— RAG・AI検索の基盤インフラ]]
- [[vibe-coding|Vibe Coding（氛围编程）— AIネイティブなソフトウェア開発手法]]
- [[wukong|悟空（Wukong）— 阿里企業級AIエージェントプラットフォーム]]
- [[world-model|World Model — AI環境生成モデル]]
- [[vram-optimization|显存优化（VRAM Optimization）— KVキャッシュ圧縮・量子化・推論効率化]]
- [[in-context-learning|In-context Learning（ICL）— コンテキスト内学習]]
  - [[vibe-coding-china|Vibe Coding中国 — 氛围编程受容とAgentic Engineeringへの進化]]
  - [[android-cli|Android CLI — Google Agent-first開発時代向けAndroid開発ツール]]
  - [[browser-use|browser-use — ブラウザAgentのDOM処理パイプライン]]
  - [[graphiti|Graphiti — LLM用リアルタイム知識グラフ]]
  - [[mini-cc-claude-code-analysis-series|Claude Code源码解析シリーズ — 雨夜寻晴天]]
  - [[openai-eval-skill-validation|OpenAI Eval — Agent Skill系统化検証方法論]]
  - [[prompt-agent-function-call-skill-mcp|Prompt・Agent・Function Call・Skill・MCP — 用語整理]]
- [[yi|Yi（零一万物）— 01.AI]]
- [[china-ai-agent-ecosystem|中国AI智能体生态 — 2026年プラットフォーム・アーキテクチャ・市場動向]]
- [[china-ai-coding-assistants|国产AI编程助手 — Trae・通义灵码・CodeGeeX・文心快码]]
- [[china-local-deployment|中国大模型本地部署 — 量子化・VRAM最適化・消費者GPUでの推論]]
- [[china-ai-regulation|中国AI监管政策 — 生成AI管理弁法、算法备案、データ安全規制]]
- [[china-coding-agents|中国编程Agent工具 — コーディングAIエージェントの生態系]]
- [[coze|扣子 (Coze) — ByteDanceのノーコードAI Agentプラットフォーム]]
- [[dify|Dify — オープンソースLLMOpsプラットフォーム]]
- [[china-ai-landscape|中国AI全景 — BAT + ByteDance + スタートアップのエコシステムマップ]]
- [[china-open-source-ai|中国开源AI社区 — ModelScope、HuggingFace中国、Giteeエコシステム]]
- [[badskill-agent-backdoor|BadSkill — AIエージェントスキルへのバックドア攻撃（サプライチェーンセキュリティ脅威）]]
- [[china-ai-bulletin|China AI Bulletin — SAIF発行の中国AI安全保障・ガバナンス情報"]]
- [[hifloat4-format|HiFloat4 — 華為Ascendチップ用4bit訓練フォーマット]]
- [[clipimg-agent-cli-tool|ClipImg — Agent CLI图片粘贴ツール]]
- [[llm-hallucination-handling|LLM幻觉処理 — 構造化ドキュメント理解の限界と解法]]
- [[karpathy-obsidian-llm-wiki|Karpathy式LLM Wiki — Obsidianで知识库を構築する方法論]]
- [[local-model-token-formula|本地模型部署 — Token出力性能計算公式]]
- [[mini-cc-lightweight-coding-agent|mini-cc — 軽量级AI编程智能体フレームワーク]]
- [[specflow-ai-development|SpecFlow — AI時代の設計駆動開発パラダイム]]
- [[vibe-coding-harness-synergy|HarnessとBlind Vibe Coding — 適用境界の分析]]
- [[claude-code-ip-ban-analysis|Claude Code封号分析 — IP検出メカニズム深掘り]]

- [[ai-uninstall-surge|ai-uninstall-surge]]

- [[codex-phone-verification|codex-phone-verification]]

- [[claude-perceive|claude-perceive]]

- [[glm-5|glm-5]]

- [[gpt-5-6|gpt-5-6]]

- [[gpt-image-2|gpt-image-2]]

- [[longcat|longcat]]

- [[mixture-of-thought|mixture-of-thought]]

- [[sense-nova-u1|sense-nova-u1]]

- [[openai-agents-sdk|openai-agents-sdk]]

- [[rag-reality|rag-reality]]

- [[spec-driven-development|spec-driven-development]]

- [[local-inference-optimization|local-inference-optimization]]

- [[copilot-changes|copilot-changes]]

- [[anthropic-ip-ban|anthropic-ip-ban]]

- [[agent-database-problem|agent-database-problem]]

- [[turing-award-criticism|turing-award-criticism]]

- [[skills|skills]]

- [[model-pricing|model-pricing]]

- [[mcp-chinese-tools|mcp-chinese-tools]]

- [[kimi|kimi]]

- [[agent|agent]]

- [[ai-coding-reality|ai-coding-reality]]

- [[opencode|opencode]]

- [[wukong-vs-openclaw|wukong-vs-openclaw]]

- [[opus-4-7-regression|opus-4-7-regression]]

- [[apple-support-ai|apple-support-ai]]

## ページ (Pages)

- [[industry-trends|行业趋势 — 中国AI業界動向・モデル競争・開発ツールトレンド]]
- [[openai-codex-infrastructure|OpenAI Codex — Mac版「超级龙虾」のインフラと機能進化]]

## ダイエスト (Daily Digests)

- [[daily-digest-2026-04-15|2026-04-15 — 52件]]
- [[daily-digest-2026-04-16|2026-04-16 — 45件]]
- [[daily-digest-2026-04-17|2026-04-17 — 52件]]
- [[daily-digest-2026-04-18|2026-04-18 — 57件]]
- [[daily-digest-2026-04-19|2026-04-19 — 57件]]
- [[daily-digest-2026-04-20|2026-04-20 — 57件]]
- [[daily-digest-2026-04-21|2026-04-21 — 52件]]
- [[daily-digest-2026-04-25|2026-04-25 — 58件]]

## 比較 (Comparisons)

- [[minimax-vs-kimi-moonshot|MiniMax vs Moonshot/Kimi — 中国生成AIスタートアップ比較]]
- [[coding-harness-benchmark|AI Coding Harness & Model Compatibility Benchmark — ハーネス・モデル性能比較大全]]

## 最新生記事 (Recent Raw Articles)

- [Codex App が偷偷にSSH远程开发機能を追加 — V2EX透明度懸念](raw/articles/v2ex-2026-04-25/codex-ssh-功能.md)
- [低价GPTの脆弱性議論 — 封じてまだ残る — V2EX](raw/articles/v2ex-2026-04-25/低价GPT-漏洞議論.md)
- [GPT-6.0何时发布 — 中国社区の期待と不安 — V2EX](raw/articles/v2ex-2026-04-25/gpt-6-0-待機議論.md)
- [Daily Digest 2026-04-25 — 58件の中国AIニュース](raw/articles/digests-2026-04-25/daily-digest-2026-04-25.md)
- [[AI 周刊 2026.04.13-04.19] 中美差距减小、Claude Opus 4.7发布、国产算力突围](raw/articles/2026-04-19-AI-Weekly-2026.04.13-04.19-中美差距-Claude-Opus-4.7-国产算力突围.md)
- [[大模型输出的隐性结构塌缩问题及对策] 码事漫谈](raw/articles/2026-04-19-大模型输出隐性结构塌缩问题及对策-码事漫谈.md)
- [[安全专家纷纷离职谁为AI竞赛踩刹车] 36kr](raw/articles/2026-04-18-安全专家纷纷离职谁为AI竞赛踩刹车-36kr.md)
- [[开源分享] transpec，开发框架转换工具](raw/articles/2026-04-18-开源分享-transpec-开发框架转换工具-29836536.md)
- [一个人搞了两个月，聊聊用 AI 做短视频自动生成的技术方案和踩坑](raw/articles/2026-04-18-一个人搞了两个月-聊聊用-AI-做短视频自动生成的技术方案和踩坑-dcd7d775.md)
- [复旦NLP团队发布80页大模型Agent综述,一文纵览AI智能体的现状与未来](raw/articles/2026-04-17-复旦NLP团队发布80页大模型Agent综述-一文纵览AI智能体的现状与未来-357bad68.md)
- [开源了一个 AI 口语练习工具，音素级发音评分，完全免费可自部署](raw/articles/2026-04-16-开源了一个-AI-口语练习工具-音素级发音评分-完全免费可自部署-3d7dd0e2.md)
- [OpenClaw爆火，暴露12类致命隐患，MCP协议安全基准发布](raw/articles/2026-04-16-OpenClaw爆火-暴露12类致命隐患-MCP协议安全基准发布-4c4e9d57.md)
- [CreatorWeave：一个本地优先的浏览器创作工作空间（工作区并行 + 多智能体探索）](raw/articles/2026-04-16-CreatorWeave-一个本地优先的浏览器创作工作空间-工作区并行-多智能体探索-1b65a1df.md)
- [啃了那篇 54 页的 Agent Harness 综述, 给大伙讲个省流版](raw/articles/2026-04-15-啃了那篇-54-页的-Agent-Harness-综述-给大伙讲个省流版-f121e212.md)
- [Claude Code 也能玩 Galgame —— 灵魂杀手 Agent 及 skill 创建器](raw/articles/2026-04-15-Claude-Code-也能玩-Galgame-灵魂杀手-Agent-及-skill-创建器-0ec16492.md)
- [RAG 架构设计深度解析：从向量数据库选型到生产级检索系统](raw/articles/2026-04-23-RAG-架构设计深度解析-从向量数据库选型到生产级检索系统-22c6986e.md)
- [从Claude Code泄露源码看工程架构：第九章 — Claude Code 与架构的总结展望](raw/articles/2026-04-21-从Claude-Code泄露源码看工程架构-第九章-Claude-Code-与架构的总结展望-aced9f43.md)
- [大模型根本不是“学会了”，它只是会“看例子”：一文讲透 In-context Learning（ICL）](raw/articles/2026-04-20-大模型根本不是-学会了-它只是会-看例子-一文讲透-In-context-Learning-ICL-bdfa5625.md)
- [大模型训练全流程实战指南工具篇（十一）—— 大模型训练参数调优实战](raw/articles/2026-04-19-大模型训练全流程实战指南工具篇-十一-大模型训练参数调优实战-从小白到调参高手-1995371e.md)