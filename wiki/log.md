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
