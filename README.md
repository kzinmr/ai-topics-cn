# AI Topics CN

AI Topics CN is the knowledge base repository maintained by Hermes Agent for Chinese-language LLM and AI Agent discourse.

This README describes the repository layout and stable responsibilities only. Operationally volatile details, such as source counts, cron schedules, current job state, generated report dates, and recent topic lists, should be read from the relevant config files or generated reports instead.

## Path Policy

- Treat `~/ai-topics-cn` as the repository root.
- The canonical wiki path is `~/wiki`. Use this path in Hermes prompts and skills.
- The wiki content lives in this repository under `wiki/`, but prompts and skills should refer to destinations as `~/wiki/...`.
- Use `~/.hermes/scripts/...` in examples for Hermes-managed scripts. Cron script paths are interpreted relative to `~/.hermes/scripts`.
- Do not add environment-specific absolute paths or new alternate compatibility paths.

## Repository Layout

```text
ai-topics-cn/
|-- README.md
|-- AGENTS.md
|-- Makefile
|-- go.mod
|-- go.sum
|-- .githooks/
|   `-- pre-commit
|
|-- cmd/
|   `-- srv/
|
|-- srv/
|   |-- server.go
|   |-- templates/
|   `-- static/
|
|-- db/
|   |-- migrations/
|   |-- queries/
|   `-- dbgen/
|
|-- inbox/
|   |-- 36kr/
|   |-- daily_digests/
|   |-- juejin/
|   |-- newsletters/
|   |-- v2ex/
|   `-- wechat-media/
|
|-- wiki/
|   |-- SCHEMA.md
|   |-- index.md
|   |-- log.md
|   |-- concepts/
|   |-- entities/
|   |-- comparisons/
|   |-- pages/
|   |-- reports/
|   |-- raw/
|   |   |-- articles/
|   |   `-- archive/
|   `-- x-accounts/
|
|-- config/
|   |-- feeds/
|   |-- hermes/
|   |   |-- SOUL.md
|   |   |-- cron/
|   |   `-- skills/
|   `-- hot-topics.yaml
|
|-- scripts/
|-- systemd/
`-- docs/
```

## Main Areas

`inbox/` stores automatically collected inputs before wiki curation. Source-specific crawl outputs, daily digests, and newsletter artifacts are staged here for triage.

`wiki/` is the curated knowledge base. Follow `wiki/SCHEMA.md` for raw sources, concepts, entities, comparisons, pages, reports, and X account notes. When creating or updating pages, update `index.md` and `log.md` as well.

`wiki/raw/` stores source material and archived raw inputs so later wiki pages can cite the original material. Claims should retain links to original Chinese sources where available.

`config/` stores source definitions, Hermes configuration, cron definitions, and active crawl targets. Project-specific local skills live under `config/hermes/skills/`.

`scripts/` stores automation for crawling, newsletter processing, trend analysis, wiki health checks, X account page generation, cron sync, and git hook installation. When describing these scripts in Hermes runtime contexts, use `~/.hermes/scripts/...`.

`cmd/`, `srv/`, and `db/` contain the Go dashboard application and its database access layer. Build and test entry points are defined in `Makefile`.

`systemd/` stores unit and timer files for host integration. The actual enabled service state belongs to the runtime environment.

`docs/` stores setup, migration, and operational documentation.

## Data Flow

```text
Configuration
  config/feeds/
  config/hot-topics.yaml
        |
        v
Collection and preprocessing
  cron jobs
  ~/.hermes/scripts/...
        |
        |-- inbox/<source>/
        |-- inbox/daily_digests/
        |-- inbox/newsletters/
        `-- ~/wiki/raw/...
                |
                v
Curation
  Hermes Agent
        |
        |-- ~/wiki/concepts/
        |-- ~/wiki/entities/
        |-- ~/wiki/comparisons/
        |-- ~/wiki/pages/
        |-- ~/wiki/reports/
        `-- ~/wiki/x-accounts/
                |
                v
Index and history
  ~/wiki/index.md
  ~/wiki/log.md
```

## Cron and Config Sync

The versioned copy of Hermes cron state lives at `config/hermes/cron/jobs.json`. Use `scripts/sync_cron.sh` to sync it with the runtime cron state.

`.githooks/pre-commit` pulls the Hermes cron state into the repository before each commit when the runtime cron file exists. Run `scripts/install_hooks.sh` once in a new clone to install the hook.

When running Hermes cron commands from outside Docker, use the wrapper under the Hermes root. For Nana, use `bin/hermes-nana`; do not run `docker exec ... hermes ...` directly.

## Wiki Update Rules

- Wiki pages, summaries, and reports are written in Japanese.
- Preserve Chinese source text or terms when they matter, and translate or synthesize them in Japanese.
- Follow `wiki/SCHEMA.md` frontmatter, naming, source attribution, and classification rules for new pages and substantial updates.
- If raw source material exists, keep references under `~/wiki/raw/...`.
- Add new pages to `~/wiki/index.md`.
- Record changes in `~/wiki/log.md`.
- Use `~/wiki/...` as the wiki destination path in prompts, skills, SOUL files, and runbooks.
