#!/usr/bin/env python3
"""Classify Claude Code Action results without exposing model output."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Iterable


ERROR_CLASSES = (
    (re.compile(r"oauth|unauthori[sz]ed|authentication|invalid token|token expired|\b401\b", re.I), "authentication"),
    (re.compile(r"quota|rate.?limit|billing|credit|\b429\b", re.I), "quota"),
    (re.compile(r"model.*(?:not found|unavailable)|entitle|\b404\b", re.I), "model-entitlement"),
    (re.compile(r"plugin|slash command|unknown command", re.I), "plugin-command"),
    (re.compile(r"overload|service unavailable|provider outage|\b(?:503|529)\b", re.I), "provider-outage"),
)


def load_records(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        value = json.loads(line)
        if isinstance(value, dict):
            records.append(value)
    return records


def _last_result(records: Iterable[dict[str, Any]]) -> dict[str, Any] | None:
    return next((item for item in reversed(list(records)) if item.get("type") == "result"), None)


def _error_class(result: dict[str, Any]) -> str:
    text = " ".join(str(result.get(key, "")) for key in ("subtype", "result", "error"))
    for pattern, classification in ERROR_CLASSES:
        if pattern.search(text):
            return classification
    return "provider-zero-turn"


def classify(records: Iterable[dict[str, Any]], action_outcome: str) -> dict[str, Any]:
    result = _last_result(records)
    if result is None:
        classification = "action-runtime-failure" if action_outcome != "success" else "missing-result"
        return {
            "classification": classification,
            "action_outcome": action_outcome,
            "result_subtype": "missing",
            "is_error": True,
            "num_turns": 0,
        }

    is_error = bool(result.get("is_error", False))
    num_turns = int(result.get("num_turns") or 0)
    if is_error and num_turns == 0:
        classification = _error_class(result)
    elif is_error:
        classification = "claude-execution-error"
    elif action_outcome != "success":
        classification = "action-runtime-failure"
    elif num_turns == 0:
        classification = "provider-zero-turn"
    else:
        classification = "review-completed"

    return {
        "classification": classification,
        "action_outcome": action_outcome,
        "result_subtype": str(result.get("subtype") or "unknown"),
        "is_error": is_error,
        "num_turns": num_turns,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("execution_file", type=Path)
    parser.add_argument("--action-outcome", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--github-output", type=Path)
    args = parser.parse_args()

    records = load_records(args.execution_file) if args.execution_file.is_file() else []
    diagnostic = classify(records, args.action_outcome)
    args.output.write_text(json.dumps(diagnostic, indent=2) + "\n", encoding="utf-8")

    if args.github_output:
        with args.github_output.open("a", encoding="utf-8") as stream:
            for key in ("classification", "num_turns", "is_error"):
                stream.write(f"{key}={str(diagnostic[key]).lower()}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

