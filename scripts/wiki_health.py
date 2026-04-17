#!/usr/bin/env python3
"""Wiki Health Digest for Chinese AI Topics wiki.

Generates a markdown report covering:
  1. Summary stats (entity / concept / comparison / raw counts)
  2. Skeleton entities needing enrichment
  3. Stale pages (>30 days since updated)
  4. Orphan pages (on disk but not in index.md)
  5. Unprocessed inbox items (not yet triaged)
  6. Raw articles not yet curated

Usage:  python scripts/wiki_health.py
        python scripts/wiki_health.py > report.md
"""

import datetime
import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore[assignment]

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

WIKI_ROOT = Path(__file__).resolve().parent.parent / "wiki"
REPO_ROOT = WIKI_ROOT.parent
ENTITIES_DIR = WIKI_ROOT / "entities"
CONCEPTS_DIR = WIKI_ROOT / "concepts"
COMPARISONS_DIR = WIKI_ROOT / "comparisons"
RAW_ARTICLES_DIR = WIKI_ROOT / "raw" / "articles"
INDEX_FILE = WIKI_ROOT / "index.md"

# Inbox directories — Chinese-source feeds
INBOX_ROOT = REPO_ROOT / "inbox"
INBOX_DIRS = [
    INBOX_ROOT / "v2ex",
    INBOX_ROOT / "juejin",
    INBOX_ROOT / "36kr",
    INBOX_ROOT / "zhihu",
    INBOX_ROOT / "wechat-media",
]

TODAY = datetime.date.today()

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def parse_frontmatter(path: Path) -> dict:
    """Return the YAML frontmatter dict for a markdown file, or {} on failure."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}

    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    fm_text = parts[1]

    if yaml is not None:
        try:
            data = yaml.safe_load(fm_text)
            return data if isinstance(data, dict) else {}
        except Exception:
            return {}
    else:
        # Minimal fallback when PyYAML is unavailable
        data: dict = {}
        for line in fm_text.splitlines():
            if ":" in line:
                key, _, val = line.partition(":")
                data[key.strip()] = val.strip().strip('"').strip("'")
        return data


def collect_md_files(directory: Path) -> list[Path]:
    """Recursively collect all .md files under *directory*."""
    if not directory.is_dir():
        return []
    return sorted(directory.rglob("*.md"))


def slug_from_path(path: Path, base: Path) -> str:
    """Return the relative stem usable as a wiki slug (no .md extension)."""
    return str(path.relative_to(base).with_suffix(""))


def parse_date(val) -> datetime.date | None:
    """Best-effort parse of a date-like value from frontmatter."""
    if isinstance(val, datetime.datetime):
        return val.date()
    if isinstance(val, datetime.date):
        return val
    if isinstance(val, str):
        for fmt in ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
            try:
                return datetime.datetime.strptime(val.strip(), fmt).date()
            except ValueError:
                continue
    return None


def extract_tags(fm: dict) -> list[str]:
    """Return list of tags from frontmatter, handling both list and string."""
    raw = fm.get("tags", [])
    if isinstance(raw, list):
        return [str(t) for t in raw if t]
    if isinstance(raw, str):
        raw = raw.strip("[]").strip()
        if raw:
            return [t.strip().strip('"').strip("'") for t in raw.split(",") if t.strip()]
    return []


def has_source_lang_zh(fm: dict) -> bool:
    """Check whether frontmatter declares source_lang: zh-CN."""
    return str(fm.get("source_lang", "")).strip().lower() in ("zh-cn", "zh_cn", "zh")


# ---------------------------------------------------------------------------
# Data collection
# ---------------------------------------------------------------------------


def load_l2_pages() -> dict[str, list[tuple[Path, dict]]]:
    """Return {category: [(path, frontmatter_dict), ...]} for all L2 pages."""
    categories = {
        "entities": ENTITIES_DIR,
        "concepts": CONCEPTS_DIR,
        "comparisons": COMPARISONS_DIR,
    }
    result: dict[str, list[tuple[Path, dict]]] = {}
    for cat, d in categories.items():
        pages = []
        for p in collect_md_files(d):
            fm = parse_frontmatter(p)
            pages.append((p, fm))
        result[cat] = pages
    return result


def load_raw_articles() -> list[Path]:
    """Return all markdown files in wiki/raw/articles/."""
    if not RAW_ARTICLES_DIR.is_dir():
        return []
    return sorted(RAW_ARTICLES_DIR.glob("*.md"))


def load_inbox_items() -> dict[str, list[Path]]:
    """Return {source_name: [paths]} for all inbox markdown files."""
    result: dict[str, list[Path]] = {}
    for d in INBOX_DIRS:
        name = d.name
        if d.is_dir():
            result[name] = sorted(d.rglob("*.md"))
        else:
            result[name] = []
    return result


# ---------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------


def section_overview(l2: dict, raw_articles: list[Path], inbox: dict[str, list[Path]]) -> str:
    """§1 — Summary stats."""
    lines = ["## 📊 Overview Stats\n"]
    total_l2 = 0
    for cat in ("entities", "concepts", "comparisons"):
        n = len(l2.get(cat, []))
        total_l2 += n
        lines.append(f"- **{cat.title()}**: {n} pages")
    lines.append(f"- **Raw articles**: {len(raw_articles)}")

    skeleton_count = sum(
        1
        for _, fm in l2.get("entities", [])
        if str(fm.get("status", "")).strip().lower() == "skeleton"
    )
    zh_count = sum(
        1
        for pages in l2.values()
        for _, fm in pages
        if has_source_lang_zh(fm)
    )
    inbox_total = sum(len(files) for files in inbox.values())

    lines.append(f"- **Skeleton entities**: {skeleton_count}")
    lines.append(f"- **Pages with source_lang: zh-CN**: {zh_count}")
    lines.append(f"- **Total Layer 2 pages**: {total_l2}")
    lines.append(f"- **Inbox items (all sources)**: {inbox_total}")
    return "\n".join(lines)


def section_skeletons(l2: dict) -> str:
    """§2 — Skeleton entities needing enrichment."""
    lines = ["## 🦴 Skeleton Entities Needing Enrichment\n"]

    skeletons: list[tuple[str, str, Path]] = []
    for cat, pages in l2.items():
        for path, fm in pages:
            if str(fm.get("status", "")).strip().lower() == "skeleton":
                rel = f"{cat}/{slug_from_path(path, WIKI_ROOT / cat)}"
                title = fm.get("title", path.stem)
                skeletons.append((rel, str(title), path))

    if not skeletons:
        lines.append("_No skeleton pages found — all entities have been enriched._ ✅")
    else:
        lines.append(
            f"Found **{len(skeletons)}** skeleton pages that need research and enrichment:\n"
        )
        lines.append("| # | Page | Title |")
        lines.append("|---|------|-------|")
        for i, (rel, title, _) in enumerate(sorted(skeletons), 1):
            lines.append(f"| {i} | `{rel}` | {title} |")

    return "\n".join(lines)


def section_stale_pages(l2: dict) -> str:
    """§3 — Stale pages (>30 days since updated)."""
    lines = ["## 🕰️ Stale Pages (>30 days since update)\n"]
    stale: list[tuple[int, str, Path]] = []

    for cat, pages in l2.items():
        for path, fm in pages:
            d = parse_date(fm.get("updated") or fm.get("created"))
            if d is None:
                continue
            age = (TODAY - d).days
            if age > 30:
                rel = f"{cat}/{slug_from_path(path, WIKI_ROOT / cat)}"
                stale.append((age, rel, path))

    stale.sort(key=lambda x: -x[0])  # stalest first

    if not stale:
        lines.append(
            "_No stale pages found — everything updated within the last 30 days._ ✅"
        )
    else:
        lines.append(f"Found **{len(stale)}** stale pages. Top 10:\n")
        lines.append("| # | Page | Days since update |")
        lines.append("|---|------|-------------------|")
        for i, (age, rel, _) in enumerate(stale[:10], 1):
            lines.append(f"| {i} | `{rel}` | {age} |")

    return "\n".join(lines)


def section_orphan_pages(l2: dict) -> str:
    """§4 — Orphan pages (exist on disk but not referenced in index.md)."""
    lines = ["## 🔗 Orphan Pages (not in index.md)\n"]

    try:
        index_text = INDEX_FILE.read_text(encoding="utf-8", errors="replace")
    except OSError:
        lines.append("_Could not read index.md — skipping orphan check._")
        return "\n".join(lines)

    orphans: list[str] = []
    for cat, pages in l2.items():
        for path, fm in pages:
            # Wiki-link format: [[slug]] without category prefix or with prefix
            stem = path.stem  # e.g. "claude-code"
            rel = str(path.relative_to(WIKI_ROOT).with_suffix(""))  # e.g. "entities/claude-code"
            rel_md = str(path.relative_to(WIKI_ROOT))  # e.g. "entities/claude-code.md"
            # Check all common reference patterns
            if (
                f"[[{stem}]]" not in index_text
                and f"[[{rel}]]" not in index_text
                and f"[[{rel}|" not in index_text
                and rel not in index_text
                and rel_md not in index_text
                and stem not in index_text
            ):
                orphans.append(rel)

    if not orphans:
        lines.append("_All Layer 2 pages are referenced in index.md._ ✅")
    else:
        lines.append(
            f"Found **{len(orphans)}** orphan pages not referenced in `index.md`:\n"
        )
        for o in sorted(orphans):
            lines.append(f"- `{o}`")

    return "\n".join(lines)


def section_unprocessed_inbox(inbox: dict[str, list[Path]], l2: dict) -> str:
    """§5 — Unprocessed inbox items (articles not yet triaged into wiki pages)."""
    lines = ["## 📬 Unprocessed Inbox Items\n"]

    total_inbox = sum(len(v) for v in inbox.values())
    if total_inbox == 0:
        lines.append("_No inbox items found._")
        return "\n".join(lines)

    # Build blob of all L2 page content for reference checking
    l2_content_parts: list[str] = []
    for cat, pages in l2.items():
        for path, _ in pages:
            try:
                l2_content_parts.append(path.read_text(encoding="utf-8", errors="replace"))
            except OSError:
                pass
    l2_blob = "\n".join(l2_content_parts)

    lines.append("| Source | Total | Unprocessed |")
    lines.append("|--------|-------|-------------|")

    grand_total = 0
    grand_unprocessed = 0
    unprocessed_samples: list[tuple[str, Path]] = []  # (source, path) for sample listing

    for source_name in sorted(inbox.keys()):
        files = inbox[source_name]
        n_total = len(files)
        unprocessed = []
        for p in files:
            stem = p.stem
            name = p.name
            if stem not in l2_blob and name not in l2_blob:
                unprocessed.append(p)
                unprocessed_samples.append((source_name, p))
        n_unprocessed = len(unprocessed)
        grand_total += n_total
        grand_unprocessed += n_unprocessed
        lines.append(f"| {source_name} | {n_total} | {n_unprocessed} |")

    lines.append(f"| **Total** | **{grand_total}** | **{grand_unprocessed}** |")

    if unprocessed_samples:
        # Show most recent 15
        recent = sorted(unprocessed_samples, key=lambda x: x[1].name, reverse=True)[:15]
        lines.append(f"\nLatest {min(15, len(recent))} unprocessed items:\n")
        for source, p in recent:
            lines.append(f"- `[{source}]` {p.name}")
        if len(unprocessed_samples) > 15:
            lines.append(f"- _…and {len(unprocessed_samples) - 15} more_")

    return "\n".join(lines)


def section_unprocessed_raw(l2: dict, raw_articles: list[Path]) -> str:
    """§6 — Raw articles not yet curated into L2 pages."""
    lines = ["## 📄 Raw Articles Not Yet Curated\n"]

    if not raw_articles:
        lines.append("_No raw articles found._")
        return "\n".join(lines)

    # Build blob of all L2 page content for reference checking
    l2_content_parts: list[str] = []
    for cat, pages in l2.items():
        for path, _ in pages:
            try:
                l2_content_parts.append(path.read_text(encoding="utf-8", errors="replace"))
            except OSError:
                pass
    l2_blob = "\n".join(l2_content_parts)

    unprocessed: list[Path] = []
    for raw_path in raw_articles:
        stem = raw_path.stem
        name = raw_path.name
        if stem not in l2_blob and name not in l2_blob:
            unprocessed.append(raw_path)

    lines.append(
        f"**{len(unprocessed)}** of {len(raw_articles)} raw articles are not referenced "
        f"from any Layer 2 page.\n"
    )

    if unprocessed:
        unprocessed_sorted = sorted(unprocessed, key=lambda p: p.name, reverse=True)
        lines.append("Latest 20 uncurated:\n")
        for p in unprocessed_sorted[:20]:
            lines.append(f"- `{p.name}`")
        if len(unprocessed) > 20:
            lines.append(f"- _…and {len(unprocessed) - 20} more_")

    return "\n".join(lines)


def section_growth(l2: dict) -> str:
    """Bonus: Growth in the last 7 days (via git or mtime fallback)."""
    lines = ["## 🌱 Growth (Last 7 Days)\n"]

    new_files: list[str] = []
    git_ok = False

    try:
        result = subprocess.run(
            [
                "git",
                "log",
                "--diff-filter=A",
                "--since=7 days ago",
                "--name-only",
                "--pretty=format:",
            ],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=15,
        )
        if result.returncode == 0:
            new_files = [f for f in result.stdout.splitlines() if f.strip()]
            git_ok = True
    except Exception:
        pass

    if not git_ok:
        cutoff = datetime.datetime.now().timestamp() - 7 * 86400
        for p in WIKI_ROOT.rglob("*.md"):
            try:
                if p.stat().st_mtime >= cutoff:
                    new_files.append(str(p.relative_to(REPO_ROOT)))
            except OSError:
                pass
        lines.append("_(Using file modification time — git not available)_\n")

    # Categorise
    buckets: Counter[str] = Counter()
    for f in new_files:
        if f.startswith("wiki/entities/"):
            buckets["entities"] += 1
        elif f.startswith("wiki/concepts/"):
            buckets["concepts"] += 1
        elif f.startswith("wiki/comparisons/"):
            buckets["comparisons"] += 1
        elif f.startswith("wiki/raw/articles/"):
            buckets["raw articles"] += 1
        elif f.startswith("wiki/"):
            buckets["other wiki"] += 1
        elif f.startswith("inbox/"):
            buckets["inbox"] += 1
        else:
            buckets["non-wiki"] += 1

    total = sum(buckets.values())
    lines.append(f"**{total}** new files added in the last 7 days:\n")

    if buckets:
        lines.append("| Category | New files |")
        lines.append("|----------|-----------|")
        for cat in (
            "entities",
            "concepts",
            "comparisons",
            "raw articles",
            "inbox",
            "other wiki",
            "non-wiki",
        ):
            if buckets.get(cat, 0) > 0:
                lines.append(f"| {cat.title()} | {buckets[cat]} |")
    else:
        lines.append("_No new files in the last 7 days._")

    return "\n".join(lines)


def section_tag_distribution(l2: dict) -> str:
    """Tag distribution across all Layer 2 pages."""
    lines = ["## 🏷️ Tag Distribution (Top 15)\n"]

    tag_counts: Counter[str] = Counter()
    for cat, pages in l2.items():
        for _, fm in pages:
            for tag in extract_tags(fm):
                tag_counts[tag] += 1

    if not tag_counts:
        lines.append("_No tags found._")
        return "\n".join(lines)

    top = tag_counts.most_common(15)

    lines.append("| # | Tag | Count |")
    lines.append("|---|-----|-------|")
    for i, (tag, count) in enumerate(top, 1):
        lines.append(f"| {i} | `{tag}` | {count} |")

    unique = len(tag_counts)
    lines.append(f"\n_{unique} unique tags across all Layer 2 pages._")

    return "\n".join(lines)


def section_source_lang_audit(l2: dict) -> str:
    """Audit: pages missing source_lang: zh-CN frontmatter."""
    lines = ["## 🌐 Source Language Audit\n"]

    missing: list[str] = []
    has_zh: int = 0
    total: int = 0

    for cat, pages in l2.items():
        for path, fm in pages:
            total += 1
            if has_source_lang_zh(fm):
                has_zh += 1
            else:
                sl = fm.get("source_lang", "(missing)")
                rel = f"{cat}/{slug_from_path(path, WIKI_ROOT / cat)}"
                missing.append(f"`{rel}` — source_lang: {sl}")

    lines.append(
        f"**{has_zh}** of {total} pages have `source_lang: zh-CN`.\n"
    )

    if missing:
        lines.append("Pages missing `source_lang: zh-CN`:\n")
        for m in sorted(missing):
            lines.append(f"- {m}")
    else:
        lines.append("_All pages correctly declare `source_lang: zh-CN`._ ✅")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    l2 = load_l2_pages()
    raw = load_raw_articles()
    inbox = load_inbox_items()

    report_parts = [
        f"# 🩺 Wiki Health Digest — {TODAY.strftime('%Y-%m-%d')}\n",
        section_overview(l2, raw, inbox),
        section_skeletons(l2),
        section_stale_pages(l2),
        section_orphan_pages(l2),
        section_unprocessed_inbox(inbox, l2),
        section_unprocessed_raw(l2, raw),
        section_growth(l2),
        section_tag_distribution(l2),
        section_source_lang_audit(l2),
        "---\n_Generated by `scripts/wiki_health.py`_",
    ]

    print("\n\n".join(report_parts))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(
            f"# Wiki Health Digest — ERROR\n\n```\n{exc}\n```",
            file=sys.stderr,
        )
        sys.exit(1)
