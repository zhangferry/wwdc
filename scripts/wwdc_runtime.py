#!/usr/bin/env python3
"""Runtime-only helpers for the standalone WWDC skill."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

SKILL_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = SKILL_DIR / "data"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def keyword_in(text: str, keyword: str) -> bool:
    normalized_keyword = normalize(keyword)
    if re.search(r"[\u4e00-\u9fff]", normalized_keyword):
        return normalized_keyword in text
    return bool(re.search(rf"(?<![a-z0-9_]){re.escape(normalized_keyword)}(?![a-z0-9_])", text))


def domain_scores(query: str, domain_map: dict[str, dict[str, Any]]) -> list[tuple[int, str]]:
    normalized = normalize(query)
    scored = []
    for slug, domain in domain_map.items():
        score = sum(1 + len(keyword) // 5 for keyword in domain["keywords"] if keyword_in(normalized, keyword))
        if score:
            scored.append((score, slug))
    return sorted(scored, key=lambda item: (-item[0], item[1]))


def search_records(query: str, limit: int = 8) -> tuple[list[str], list[dict[str, Any]], list[dict[str, Any]]]:
    domain_map = read_json(DATA_DIR / "domains.json")
    routed = [slug for _, slug in domain_scores(query, domain_map)[:3]]
    normalized_query = normalize(query)
    terms = set(re.findall(r"[a-z][a-z0-9_@.+-]{1,}|[\u4e00-\u9fff]{2,}", normalized_query))
    session_results = []
    for session in read_jsonl(DATA_DIR / "sessions.jsonl"):
        haystack = normalize(" ".join([session["title"], session["titleZh"], session["track"], " ".join(session["tags"]), session["searchText"]]))
        score = sum(3 if term in normalize(session["title"] + " " + session["titleZh"]) else 1 for term in terms if term in haystack)
        score += 4 * len(set(routed) & set(session["domains"]))
        for slug in routed:
            score += sum(1 for keyword in domain_map[slug]["keywords"] if keyword_in(haystack, keyword) and keyword_in(normalized_query, keyword))
        if score:
            session_results.append((score, session))
    session_results.sort(key=lambda item: (-item[0], -item[1]["year"], item[1]["source"]))

    concept_results = []
    for concept in read_jsonl(DATA_DIR / "concepts.jsonl"):
        haystack = normalize(" ".join([concept["title"], concept["summary"], " ".join(concept["sources"])]))
        score = sum(2 for term in terms if term in haystack)
        score += 5 * len(set(routed) & set(concept["domains"]))
        if score:
            concept_results.append((score, concept))
    concept_results.sort(key=lambda item: (-item[0], item[1]["key"]))
    return routed, [dict(record, score=score) for score, record in session_results[:limit]], [dict(record, score=score) for score, record in concept_results[: min(5, limit)]]
