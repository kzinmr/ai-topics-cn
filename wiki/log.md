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

### トレンド分析結果
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

### トレンド分析結果
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
- Qwen/通義千問（Qwen-3.5のCodingPlan統合）
- OpenClaw（17言及、急上昇トピック）
- AI安全（Anthropic Nature論文「潜意識伝染」）
- Cursor独立ページ（26言及）
