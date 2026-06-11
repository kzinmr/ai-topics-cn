# Trending Report → Hot Topics YAML Mapping

Methodology from 2026-06-08 session: mapping trending_topics.py output to hot-topics.yaml crawl candidates.

## Inputs

1. **trending_topics.py output**: `python3 /opt/data/ai-topics-cn/scripts/trending_topics.py --days 3`
   - Produces main section: "ホットトピック (4+ソース)" with source counts
   - Produces cross-section: "クロスソース (高シグナル)" with source type breakdown
2. **hot-topics.yaml**: `/opt/data/ai-topics-cn/config/hot-topics.yaml` — ~600 lines, 30+ topics
3. **Wiki pages**: `~/wiki/entities/` and `~/wiki/concepts/` directories

## Cross-Reference Methodology

### Step 1: Extract all trending topics with source_count >= 3

From the script output, parse the "全トレンディング" table. The lower topics (source_count 2-3) often include concepts that may or may not have wiki pages.

### Step 2: Check hot-topics.yaml coverage

For each trending topic, search `topics:` array in hot-topics.yaml for matching slugs:

| Trending Name | hot-topic slug | Status |
|--------------|----------------|--------|
| AI Agent/智能体 | china-ai-agent-ecosystem | ✅ Covered |
| Claude | — | ❌ Not tracked |
| OpenAI | — | ❌ Not tracked |
| DeepSeek | deepseek | ✅ Covered |
| GPT | — | ❌ Not tracked (has wiki page) |
| Cursor | cursor-china-adoption | ✅ Covered (monitor) |
| Vibe Coding | vibe-coding-china | ✅ Covered |
| MCP | mcp-china | ✅ Covered |
| OpenClaw | openclaw | ✅ Covered |
| Kimi/Moonshot | kimi | ✅ Covered |
| 豆包/ByteDance | doubao | ✅ Covered |
| 混元/Tencent | tencent-hunyuan | ✅ Covered |
| Qwen/通义千問 | qwen | ✅ Covered |
| ChatGLM/智谱 | chatglm | ✅ Covered |
| 量化/Quantization | vram-optimization | ✅ Covered (related) |

### Step 3: Check wiki page existence for uncovered topics

For each uncovered topic, search wiki directories:

```bash
ls ~/wiki/entities/ ~/wiki/concepts/
# Or use search_files(target='files', pattern='topic', path='~/wiki')
```

From 2026-06-08 session findings:

| Topic | Wiki Page | Status |
|-------|-----------|--------|
| OpenAI | ❌ No page | **New page recommended** |
| GPT | concepts/gpt.md ✅ | Exists, skip |
| Claude | entities/claude.md ✅ | Exists, skip |
| Anthropic | entities/anthropic.md ✅ | Exists, skip |
| Gemini/Google | entities/gemini-google.md ✅ | Exists, skip |
| Llama/Meta | entities/llama-meta.md ✅ | Exists, skip |
| 文心一言/Baidu | entities/baidu-ernie.md ✅ | Exists, skip |
| RAG | concepts/rag.md ✅ | Exists, skip |
| Function Calling | concepts/function-calling.md ✅ | Exists, skip |
| RLHF/对齐 | concepts/rlhf-alignment.md ✅ | Exists, skip |
| AI安全 | ❌ No page | **New page recommended** |
| オープンソースモデル | ❌ No page | **New page recommended** |

### Step 4: Evaluate crawl candidate quality

For the truly missing topics (no wiki page, no hot-topic entry), evaluate:

1. **Chinese AI relevance**: OpenAI heavily discussed but global. AI安全 directly relevant to regulation. オープンソースモデル relevant to ecosystem.
2. **Cross-source signal**: OpenAI appears on 4 platforms (highest cross-source count). Others appear on 1-2 platforms.
3. **Durability**: RAG is a durable technical concept but has a wiki page. AI安全 is emerging and lacks coverage.
4. **Ecosystem impact**: OpenAI's policy changes (API pricing, model access, Codex integration with Chinese models) directly affect Chinese AI startups and developers.

### Step 5: Structure YAML proposals

For each approved candidate:

```yaml
  - slug: openai
    title: "OpenAI — 中国AIエコシステムへの影響"
    crawl_policy: monitor
    priority: high
    search_hints:
      - "OpenAI 中国 最新 動向 2026"
      - "GPT-5.5 ProgramBench 中国 開発者"
      - "OpenAI Codex サードパーティ API DeepSeek Kimi GLM"
    wiki_pages:
      - entities/openai
    notes: "YYYY-MM-DD初登録。Nソース/Mプラットフォームのトレンド根拠。"
    added: YYYY-MM-DD
    last_crawled: ~
```

## Key Learnings

- **Many global entities have wiki pages but no hot-topics entry**: This is intentional — hot-topics.yaml focuses on Chinese-origin or China-significant topics. Global entities are documented in wiki but not actively crawled unless their China impact is material.
- **Wiki page names ≠ trending topic names**: e.g., "豆包/ByteDance" → `doubao.md` / `doubao-bytedance.md`. Always search, never guess.
- **source_count from different sources indicates different things**: 36kr = business impact. Juejin = developer/technical adoption. V2EX = developer friction/pain points. WeChat = expert long-form analysis. A topic with V2EX-only coverage may be a transient complaint that doesn't warrant a wiki page.
- **Zero-count sources should be noted**: zhihu = 0 in this session suggests a pipeline issue or genuinely low activity. Don't fabricate coverage.
- **The daily trending report is a SEPARATE pipeline from crawl triage**: Do NOT read `triage_latest.json` for trending report tasks. Use `trending_topics.py` output instead.
- **Report language**: Unless the task says otherwise, write the final analysis in Japanese (matches wiki language convention).
