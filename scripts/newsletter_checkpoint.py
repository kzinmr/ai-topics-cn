#!/usr/bin/env python3
"""Load the latest Nana newsletter collection checkpoint for triage."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

MAX_CANDIDATES = int(os.environ.get("NEWSLETTER_TRIAGE_MAX_CANDIDATES", "25"))
MAX_EXCERPT_CHARS = int(os.environ.get("NEWSLETTER_TRIAGE_EXCERPT_CHARS", "200"))


def get_hermes_home() -> Path:
    hermes_home = os.environ.get("HERMES_HOME")
    if hermes_home:
        return Path(hermes_home)
    return Path.home() / ".hermes"


def make_item_id(message_id: str, url: str, index: int) -> str:
    raw = f"{message_id}:{url}:{index}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]


def trim_excerpt(value: str) -> str:
    value = (value or "").strip()
    if len(value) <= MAX_EXCERPT_CHARS:
        return value
    return value[:MAX_EXCERPT_CHARS].rstrip() + "..."


def build_candidates(checkpoint: dict) -> tuple[list[dict], int]:
    candidates: list[dict] = []
    total = 0
    for message in checkpoint.get("processed_messages", []):
        message_id = message.get("message_id", "message")
        for index, article in enumerate(message.get("articles", []), start=1):
            url = article.get("url", "").strip()
            raw_path = article.get("raw_path", "").strip()
            if not url or not raw_path:
                continue
            total += 1
            if len(candidates) >= MAX_CANDIDATES:
                continue
            candidates.append({
                "item_id": make_item_id(message_id, url, index),
                "source": "newsletter",
                "source_name": message.get("subject"),
                "title": article.get("title") or message.get("subject"),
                "url": url,
                "raw_path": raw_path,
                "digest_path": message.get("digest_path"),
                "message_id": message_id,
                "date": message.get("date"),
                "length": article.get("length"),
                "excerpt": trim_excerpt(article.get("excerpt", "")),
            })
    return candidates, total


def main() -> int:
    checkpoint_path = get_hermes_home() / "cron" / "data" / "newsletter" / "latest.json"
    if not checkpoint_path.exists():
        print(json.dumps({
            "ok": False,
            "error": "newsletter checkpoint not found",
            "checkpoint_path": str(checkpoint_path),
            "candidates": [],
        }, ensure_ascii=False, indent=2))
        return 0

    checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))
    candidates, total_candidates = build_candidates(checkpoint)
    payload = {
        "ok": checkpoint.get("ok", False),
        "run_id": checkpoint.get("run_id"),
        "collected_at": checkpoint.get("collected_at"),
        "processed_count": checkpoint.get("processed_count", 0),
        "skipped_count": checkpoint.get("skipped_count", 0),
        "errors": checkpoint.get("errors", []),
        "candidate_count": total_candidates,
        "candidate_count_emitted": len(candidates),
        "truncated": total_candidates > len(candidates),
        "limits": {
            "max_candidates": MAX_CANDIDATES,
            "max_excerpt_chars": MAX_EXCERPT_CHARS,
        },
        "candidates": candidates,
    }
    payload["_checkpoint"] = {
        "ok": True,
        "run_id": checkpoint.get("run_id"),
        "generated_at": checkpoint.get("collected_at"),
        "checkpoint_path": str(checkpoint_path),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
