# Agent Instructions

This is a Chinese AI topics knowledge management system on exe.dev.

See README.md for full details, docs/MIGRATION-RUNBOOK.md for setup.

## Key Files

- `config/hermes/SOUL.md` — Hermes Agent persona & mission
- `config/hermes/skills/` — Agent skills (research, wiki, productivity)
- `config/feeds/x-accounts.yaml` — X/Twitter accounts to track
- `config/hot-topics.yaml` — Active knowledge crawling targets
- `wiki/SCHEMA.md` — Wiki structure conventions
- `scripts/` — Crawlers and analysis tools
- `systemd/` — Reference systemd unit files

## Data Sources (Tiered)

| Tier | Source | Notes |
|------|--------|-------|
| T1 | V2EX, Juejin, 36kr | Primary. Auto-crawled every 6h |
| T2 | Zhihu (targeted), 机器之心, PaperWeekly | Expert/media layer |
| T3 | 新智元, 量子位 | News, some clickbait |
| ❌ | CSDN | **Banned** — SEO spam |

## Language Rules

- Wiki pages: **Japanese** (日本語)
- Source material: Chinese (zh-CN)
- Original Chinese terms preserved in parentheses
- English technical terms kept as-is

## Automated Pipelines

1. `crawl-cn-ai.timer` — Crawl Chinese sources every 6h
2. `shelley-triage.timer` — Triage inbox → wiki every 12h
3. `shelley-trending-topics.timer` — Daily trending topics detection
4. `shelley-active-crawl.timer` — Daily active knowledge crawling
5. `shelley-wiki-health.timer` — Weekly wiki health digest
