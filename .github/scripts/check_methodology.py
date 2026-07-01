#!/usr/bin/env python3
"""Lightweight methodology checker for GitHub issue and PR bodies.

This checker is intentionally conservative. It reports missing sections but does not
try to infer quality from natural language. It is designed for gradual adoption.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class CheckResult:
    name: str
    passed: bool
    message: str


REQUIRED_IMPORTANT_SECTIONS = [
    "summary",
    "hierarchy",
    "business value",
    "review mode",
    "routing",
    "non-goals",
]

REQUIRED_BUSINESS_VALUE_FIELDS = [
    "outcome",
    "value hypothesis",
    "who benefits",
    "how we know it worked",
    "risk if ignored",
]

REQUIRED_HIERARCHY_FIELDS = [
    "parent",
    "children",
    "related",
]

REQUIRED_PR_SECTIONS = [
    "summary",
    "linked issue",
    "scope",
    "business value",
    "review mode",
    "evidence",
    "acceptance criteria",
]


ROUGH_RESEARCH_MARKERS = {
    "[research]",
    "type:research",
    "research note",
}


def normalize(text: str) -> str:
    return text.lower().replace("\r\n", "\n")


def has_heading(body: str, heading: str) -> bool:
    pattern = rf"^#+\s+{re.escape(heading)}\s*$"
    return re.search(pattern, body, flags=re.IGNORECASE | re.MULTILINE) is not None


def has_field(body: str, field: str) -> bool:
    pattern = rf"^\s*{re.escape(field)}\s*:"
    return re.search(pattern, body, flags=re.IGNORECASE | re.MULTILINE) is not None


def is_rough_research(title: str, body: str) -> bool:
    text = normalize(f"{title}\n{body}")
    return any(marker in text for marker in ROUGH_RESEARCH_MARKERS)


def check_sections(body: str, sections: Iterable[str]) -> list[CheckResult]:
    results: list[CheckResult] = []
    for section in sections:
        passed = has_heading(body, section)
        results.append(
            CheckResult(
                name=f"section:{section}",
                passed=passed,
                message=f"Required section `{section}` {'found' if passed else 'missing'}.",
            )
        )
    return results


def check_fields(body: str, fields: Iterable[str], group: str) -> list[CheckResult]:
    results: list[CheckResult] = []
    for field in fields:
        passed = has_field(body, field)
        results.append(
            CheckResult(
                name=f"{group}:{field}",
                passed=passed,
                message=f"Required field `{field}:` {'found' if passed else 'missing'}.",
            )
        )
    return results


def run_checks(kind: str, title: str, body: str) -> tuple[str, list[CheckResult]]:
    if is_rough_research(title, body):
        return "research-note", [
            CheckResult(
                name="mode:research-note",
                passed=True,
                message="Research note detected; full structured issue gate is advisory.",
            )
        ]

    normalized_kind = kind.lower().strip()
    results: list[CheckResult] = []

    if normalized_kind == "pr":
        results.extend(check_sections(body, REQUIRED_PR_SECTIONS))
    else:
        results.extend(check_sections(body, REQUIRED_IMPORTANT_SECTIONS))
        results.extend(check_fields(body, REQUIRED_HIERARCHY_FIELDS, "hierarchy"))
        results.extend(check_fields(body, REQUIRED_BUSINESS_VALUE_FIELDS, "business-value"))

    return normalized_kind, results


def render_markdown(kind: str, results: list[CheckResult]) -> str:
    passed_count = sum(1 for result in results if result.passed)
    failed = [result for result in results if not result.passed]

    status = "pass" if not failed else "needs-attention"
    lines = [
        "## Methodology Guard",
        "",
        f"Mode: `{kind}`",
        f"Status: `{status}`",
        f"Checks passed: `{passed_count}/{len(results)}`",
        "",
    ]

    if failed:
        lines.append("### Missing items")
        lines.append("")
        for result in failed:
            lines.append(f"- {result.message}")
        lines.append("")
        lines.append("Suggested action: add the missing sections or mark this as a `[Research]` issue if it is intentionally not ready for execution.")
    else:
        lines.append("All required methodology sections were found.")

    lines.append("")
    lines.append("Reference artifacts:")
    lines.append("- `PRODUCT_PROJECT_OPERATING_MODEL.md`")
    lines.append("- `OPERATING_GATES.md`")
    lines.append("- `ISSUE_HIERARCHY.md`")
    lines.append("- `BUSINESS_VALUE_TREE.md`")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=["issue", "pr"], required=True)
    parser.add_argument("--title", default="")
    parser.add_argument("--body", default="")
    parser.add_argument("--markdown-output", default="methodology-guard.md")
    parser.add_argument("--json-output", default="methodology-guard.json")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    kind, results = run_checks(args.kind, args.title, args.body or "")
    failed = [result for result in results if not result.passed]

    markdown = render_markdown(kind, results)
    with open(args.markdown_output, "w", encoding="utf-8") as handle:
        handle.write(markdown)

    payload = {
        "kind": kind,
        "status": "pass" if not failed else "needs-attention",
        "passed": len(results) - len(failed),
        "total": len(results),
        "failed": [result.__dict__ for result in failed],
        "results": [result.__dict__ for result in results],
    }
    with open(args.json_output, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)

    print(markdown)

    if args.strict and failed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
