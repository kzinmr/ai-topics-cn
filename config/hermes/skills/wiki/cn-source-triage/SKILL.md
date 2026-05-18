---
name: cn-source-triage
description: Triage crawled Chinese AI articles from inbox/ into structured Japanese wiki pages following SCHEMA.md conventions
category: wiki
version: 1.0.0
author: hermes
license: MIT
metadata:
  hermes:
    tags: [Wiki, Triage, Chinese-AI, Translation, Curation]
---

# Chinese Source Triage — inbox/ → wiki/ Pipeline

## Purpose

Process crawled Chinese-language articles from `inbox/{v2ex,juejin,36kr,zhihu,wechat-media}/` into structured Japanese wiki pages under `wiki/{entities,concepts,comparisons}/`.

This is the core curation pipeline: raw Chinese content → Japanese knowledge base.

## When to Use

- After a scheduled crawl run (`scripts/crawl_all.py`)
- When `inbox/` has unprocessed articles
- During the scheduled triage timer (every 12 hours)

## Steps

### 1. Scan inbox for new articles

```bash
# Count unprocessed articles per source
for dir in inbox/v2ex inbox/juejin inbox/36kr inbox/zhihu inbox/wechat-media; do
  echo "$dir: $(find $dir -name '*.md' -newer /tmp/last_triage_marker 2>/dev/null | wc -l) new"
done
```

Or run:
```bash
python3 scripts/trending_topics.py --days 1
```

### 2. Pre-filter spam, recruitment & duplicates

Run before identifying high-value articles:

**⚠️ WeChat Media Pattern**: WeChat articles are often daily re-distributions of the same 13-14 stub templates. Files with identical hash suffixes (e.g., `-aed7e3c9.md`, `-f691ec7c.md`) across different dates are duplicates. See `references/wechat-spam-pattern.md` for the full hash list and filtering guidance. When processing large WeChat backlogs (100+ files), batch-move all known spam hashes to `archive/spam/` before individual review.

```bash
# Create archive dirs
mkdir -p wiki/raw/articles/archive/{spam,duplicates}

# Spam/recruitment → archive/spam/
# Categories: recruitment ads, crypto promos, lotteries, invite links, VPN sellers
grep -rlE '招聘|内推|求人|直招|募集中|採用|Bitget|Uカード|U卡|crypto|NFT|エアドロップ|ブロックチェーン|抽選|discord\\.gg|加微信|扫码|QQ群' inbox/ --include='*.md' | while read f; do
  if [ "$(wc -c < "$f")" -gt 1500 ] && grep -qE 'RAG|LLM|Agent|Claude|DeepSeek|Qwen|MCP|vLLM|GGUF' "$f" 2>/dev/null; then
    echo "KEEP (technical): $(basename $f)"  # Has real AI discussion
  else
    mv "$f" wiki/raw/articles/archive/spam/
  fi
done

# Deduplicate by hash suffix (keep newest)
for hash in $(find inbox -type f | sed 's/.*-//' | sort | uniq -d); do
  files=($(find inbox -type f -name "*-$hash" | sort))
  keep="${files[${#files[@]}-1]}"
  for f in "${files[@]}"; do
    [ "$f" != "$keep" ] && mv "$f" wiki/raw/articles/archive/duplicates/
  done
done
```

### 3. Identify high-value articles

Prioritize articles that:
- Appear across **2+ sources** (cross-source signal)
- Discuss **hot-topics.yaml** topics (DeepSeek, Qwen, MCP, Agent, etc.)
- Have **high engagement** (comments, upvotes)
- Contain **original technical analysis** (not just news rehash)
- Come from **Tier 1 sources** (V2EX, Juejin, 36kr)

### 3. Classify article type

| Type | Wiki Location | Example |
|------|--------------|--------|
| Person/company/model profile | `entities/` | DeepSeek company, specific researcher |
| Technical concept/method | `concepts/` | RAG optimization, MoE architecture |
| Technical comparison | `comparisons/` | Qwen vs DeepSeek, Coze vs Dify |
| Raw article (curated) | `raw/articles/` | Full article translation for reference |

### 4. Create wiki page (Japanese)

Follow `wiki/SCHEMA.md` conventions:

```yaml
---
title: "ページタイトル"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
aliases: ["別名"]
source_lang: zh-CN
---
```

**Language rules:**
- Page content in **Japanese** (日本語)
- Original Chinese terms preserved in parentheses: 例「深度求索（DeepSeek）」
- Technical terms keep English: RAG, MoE, GGUF, vLLM
- Chinese URLs preserved as-is for source attribution

### 5. Source attribution

All claims must link to source with tier noted:

```markdown
> 出典: [記事タイトル](https://v2ex.com/t/xxxxx) (T1: V2EX)
> 出典: [记事タイトル](https://juejin.cn/post/xxxxx) (T1: Juejin)
```

### 6. Update index and log

```bash
# After creating pages:
# 1. Add to wiki/index.md
# 2. Append to wiki/log.md
# 3. Git commit and push
cd ~/ai-topics-cn
git add wiki/ inbox/
git commit -m "wiki: triage — <summary>"
git push
```

## Large Batch Triage Workflow (300+ inbox items)

When processing large backlogs (>300 items), use this optimized flow:

### Phase 1: Bulk Spam Removal
1. Identify recurring hash patterns (especially WeChat daily redistributions)
2. Batch-move all known spam hashes to `archive/spam/`
3. Count remaining unique articles for triage

### Phase 2: Content Extraction & Wiki Creation
1. Prioritize 36kr and Juejin sources (highest signal-to-noise ratio)
2. Apply strict V2EX filtering (~20% pass rate — only deep technical discussions)
3. Create concept/entity pages following SCHEMA.md
4. Update existing entity pages with new information from articles

### Phase 3: Statistics Sync & Commit
1. Update `wiki/index.md` file counts to match actual disk state
2. Append detailed entry to `wiki/log.md` with:
   - New concepts created (list titles)
   - Entity updates (list entities + what changed)
   - Inbox cleanup stats (source: count)
3. Commit with structured multi-line message:
   ```
   wiki: inbox triage batch N — <primary actions>

   新規コンセプト:
   - <concept1>.md: <description>
   - <concept2>.md: <description>

   エンティティ更新: <list>
   index.md統計修正: <counts>
   log.md: トリアージバッチN記録
   ```

### Subagent Delegation Rules
- Use max 3 concurrent subagents for large batches
- Delegate by source: one for 36kr/Juejin, one for V2EX filtering, one for WeChat cleanup
- Consolidate results before commit

## Quality Checklist

- [ ] Frontmatter includes `source_lang: zh-CN`
- [ ] Tags follow taxonomy in SCHEMA.md
- [ ] Chinese source URLs are preserved
- [ ] Content is in Japanese, not machine-translated Chinese
- [ ] Cross-references use `[[wikilinks]]`
- [ ] index.md updated with new pages
- [ ] log.md updated with triage summary

## Source Reliability Tiers

| Tier | Sources | Reliability |
|------|---------|------------|
| T1 | V2EX, Juejin, 36kr | High — primary communities |
| T2 | Zhihu (targeted), 机器之心, PaperWeekly | High — expert/media |
| T3 | 新智元, 量子位 | Medium — news, some clickbait |
| T4 | WaytoAGI, OSS communities | Variable — reference only |
| ❌ | CSDN | Banned — SEO spam |

## Output

- New wiki pages in `entities/`, `concepts/`, or `comparisons/`
- Curated raw articles in `raw/articles/`
- Updated `index.md` and `log.md`
- Git commit with descriptive message

## Newsletter Triage Workflow (Pre-run Checkpoint)

When a pre-run script generates a `newsletter-triage` JSON checkpoint:

### Checkpoint Format
```json
{
  "checkpoint_run_id": "YYYYMMDDTHHMMSSZ",
  "processed_count": N,
  "summary_ja": "Japanese summary of the batch",
  "decisions": [
    {
      "item_id": "hash",
      "source": "newsletter",
      "title": "Article Title",
      "url": "https://...",
      "raw_path": "~/wiki/raw/articles/...",
      "digest_path": "~/ai-topics-cn/inbox/newsletters/...",
      "recommended_action": "take|reference|skip",
      "reason_ja": "Japanese justification for the decision",
      "candidate_wiki_path": "concepts/slug or entities/slug"
    }
  ],
  "_triage_checkpoint": { "ok": true, "output_path": "...", "checkpoint_path": "..." }
}
```

### Processing Steps
1. **Check `_triage_checkpoint.ok`**: If false, report the problem briefly and stop.
2. **Count decisions by action**: `take`, `reference`, `skip` — report summary.
3. **For each `take` decision**:
   - Read `raw_path` article content
   - Check if `candidate_wiki_path` already exists (`search_files` or `ls`)
   - Create new wiki page (concept or entity) OR update existing page
   - Use `reason_ja` as the Japanese justification for inclusion
   - Follow SCHEMA.md frontmatter conventions
4. **For `reference` decisions**: Add source URLs to existing wiki pages if relevant; no new pages needed.
5. **For `skip` decisions**: No action — but log duplicates for awareness.
6. **Update `wiki/index.md`**: Increment concept/entity counts, update `最終更新日`.
7. **Update `wiki/log.md`**: Append entry with checkpoint run_id, summary_ja, and page list.
8. **Commit**: `cd ~/ai-topics-cn && git add wiki/ inbox/newsletters/ && git commit -m "wiki: newsletter ingest YYYY-MM-DD — <key topics>" && git push`

### Pitfalls
- **Silent delivery**: If `_triage_checkpoint.ok` is false OR there are zero `take` decisions AND no useful raw/digest files, respond `[SILENT]`.
- **Duplicate URLs**: Newsletter crawls often capture the same article via multiple URL variants (email redirects, share URLs, app links). Skip these — only process the canonical `raw_path`.
- **Metadata stubs**: Substack app promo pages (115-357 bytes) are not real articles. Skip them.
- **Non-entity feeds**: OPML may have 84 feeds but only ~69 are blogger entities. Companies, products, and concepts use different formats — don't force entity-page structure on them.
- **Language consistency**: The checkpoint's `reason_ja` and `summary_ja` are in Japanese. All wiki output must be in Japanese (日本語). Keep technical terms in English.

## Entity Enrichment Workflow

When inbox articles relate to an **existing entity page** (not new page creation):

### Steps
1. **Locate entity**: `search_files` or `grep` in `wiki/entities/` for the entity slug
2. **Read existing page**: Note current structure, gaps, and last updated date
3. **Scan inbox for related articles**: `grep -rl "<entity>" inbox/{juejin,36kr,v2ex,wechat-media}/`
4. **Read & extract insights**: Read high-signal articles (T1 sources first)
5. **Write updates in place**:
   - Add new sections below existing content (don't restructure entire page unless necessary)
   - Use comparison tables when competitors are mentioned (see format below)
   - Add tier-tagged external source table at bottom
6. **Update wiki/log.md**: Append a structured log entry (see format below)
7. **Archive processed inbox**: `mv inbox/<source>/<article> archive/inbox/processed/`
8. **Commit**: `git add -A && git commit -m "wiki(<entity>): <summary>"`

### Comparison Table Format (for competitors)
```markdown
### 競合比較：EntityA vs EntityB

| 項目 | EntityA | EntityB |
|------|---------|---------|
| **定位** | 個人開発者向け | 企業級 |
| **強み** | 軽量アーキテクチャ | RealDocファイルシステム |
| **生态** | ClawHub（26,000+スキル） | OPT業界Skills + 釘釘/淘寶/支付宝統合 |
| **互換性** | — | EntityAスキル体系を完全互換 |

EntityBの最大優位性は**RealDoc**（AI改変のロールバック対応）。
一方EntityAは**並列ツール実行**が強み。
```

### Log Entry Format (for wiki/log.md)
```markdown
## [YYYY-MM-DD] entity-name-enrichment | inbox記事活用による拡充

### Wiki更新
1. **entities/<name>.md** — **エンリッチメント**:
   - <new section 1> (<source>)
   - <new section 2> (<source>)

### 処理inbox記事
- `inbox/<source>/<article1>` → <section>
- `inbox/<source>/<article2>` → <section>

### スコア
- take: N (<entity>.md更新)
- archive: M (関連inbox記事を処理済みアーカイブ)

### チェックポイント
- run_id: YYYYMMDDTHHMMSSZ
- source: inbox-enrichment
```

### Key Patterns
- **Inbox-first enrichment**: Always scan inbox BEFORE web search — inbox articles are pre-filtered by the crawl system and often contain the most relevant Chinese-language analysis
- **Incremental updates**: Add sections, don't rewrite entire page unless structure is broken
- **Tier attribution**: Every claim links to source with T1/T2/T3 tier
- **Dual archive**: Both processed inbox articles AND web search results should be tracked in log.md
- **Entity type handling**: Product/tool entities use different format than blogger entities (no "Core Ideas", "Key Quotes" — instead use "機能と設計思想", "中国語圏での立ち位置", "競合比較")
