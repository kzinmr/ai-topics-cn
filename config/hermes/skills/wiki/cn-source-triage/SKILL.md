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
