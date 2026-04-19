# Wiki Log

Chronological record of wiki operations.

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

## [2026-04-19] hot-topic-wiki-fill | ホットトピック分析で指摘されたwiki未作成トピックを8件作成

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
