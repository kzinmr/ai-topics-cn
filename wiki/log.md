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
