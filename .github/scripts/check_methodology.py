#!/usr/bin/env python3
"""Lightweight methodology checker for GitHub issue and PR bodies.

The checker is intentionally conservative. It reports missing sections but does not
try to infer quality from natural language. It is designed for gradual adoption.

Rules can be loaded from a tiny YAML subset without external dependencies.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class CheckResult:
    name: str
    passed: bool
    message: str


DEFAULT_RULES = {
    "issue_required_sections": [
        "summary",
        "hierarchy",
        "scope / boundary",
        "business value",
        "review mode",
        "routing",
        "non-goals",
    ],
    "issue_required_business_value_fields": [
        "outcome",
        "value hypothesis",
        "who benefits",
        "how we know it worked",
        "risk if ignored",
    ],
    "issue_required_hierarchy_fields": [
        "parent",
        "children",
        "related",
    ],
    "issue_required_scope_boundary_fields": [
        "namespace",
        "owner scope",
        "in scope",
        "out of scope",
        "allowed dependencies",
        "forbidden dependencies",
        "contract exposed",
    ],
    "pr_required_sections": [
        "summary",
        "linked issue",
        "scope",
        "boundary contract",
        "business value",
        "review mode",
        "evidence",
        "acceptance criteria",
    ],
    "pr_required_boundary_fields": [
        "namespace affected",
        "contract changed",
        "expected dependencies touched",
        "dependencies intentionally avoided",
        "derived state kept derived",
    ],
    "research_markers": [
        "[research]",
        "type:research",
        "research note",
    ],
    "reference_artifacts": [
        "PRODUCT_PROJECT_OPERATING_MODEL.md",
        "OPERATING_GATES.md",
        "ISSUE_HIERARCHY.md",
        "BUSINESS_VALUE_TREE.md",
        "WORKFLOW_STATE_MACHINE.md",
        "COUPLING_SCOPING_NAMESPACE_PRINCIPLES.md",
    ],
}


def load_tiny_yaml_list_config(path: str | None) -> dict[str, list[str]]:
    """Load a tiny YAML subset of `key: [newline] - item` lists.

    This avoids requiring PyYAML in GitHub Actions and is sufficient for the
    methodology rules config.
    """

    rules: dict[str, list[str]] = {key: list(value) for key, value in DEFAULT_RULES.items()}
    if not path:
        return rules

    rules_path = Path(path)
    if not rules_path.exists():
        return rules

    current_key: str | None = None
    parsed: dict[str, list[str]] = {}

    for raw_line in rules_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        if line.endswith(":") and not line.startswith("-"):
            current_key = line[:-1].strip()
            parsed[current_key] = []
            continue

        if line.startswith("-") and current_key:
            value = line[1:].strip().strip('"').strip("'")
            if value:
                parsed[current_key].append(value)

    for key, values in parsed.items():
        if values:
            rules[key] = values

    return rules


def normalize(text: str) -> str:
    return text.lower().replace("\r\n", "\n")


def has_heading(body: str, heading: str) -> bool:
    pattern = rf"^#+\s+{re.escape(heading)}\s*$"
    return re.search(pattern, body, flags=re.IGNORECASE | re.MULTILINE) is not None


def has_field(body: str, field: str) -> bool:
    pattern = rf"^\s*{re.escape(field)}\s*:"
    return re.search(pattern, body, flags=re.IGNORECASE | re.MULTILINE) is not None


def is_rough_research(title: str, body: str, research_markers: Iterable[str]) -> bool:
    text = normalize(f"{title}\n{body}")
    return any(marker.lower() in text for marker in research_markers)


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


def run_checks(kind: str, title: str, body: str, rules: dict[str, list[str]]) -> tuple[str, list[CheckResult]]:
    if is_rough_research(title, body, rules["research_markers"]):
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
        results.extend(check_sections(body, rules["pr_required_sections"]))
        results.extend(check_fields(body, rules.get("pr_required_boundary_fields", []), "boundary"))
    else:
        results.extend(check_sections(body, rules["issue_required_sections"]))
        results.extend(check_fields(body, rules["issue_required_hierarchy_fields"], "hierarchy"))
        results.extend(check_fields(body, rules.get("issue_required_scope_boundary_fields", []), "scope-boundary"))
        results.extend(check_fields(body, rules["issue_required_business_value_fields"], "business-value"))

    return normalized_kind, results


def render_markdown(kind: str, results: list[CheckResult], reference_artifacts: Iterable[str]) -> str:
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
    for artifact in reference_artifacts:
        lines.append(f"- `{artifact}`")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=["issue", "pr"], required=True)
    parser.add_argument("--title", default="")
    parser.add_argument("--body", default="")
    parser.add_argument("--rules-path", default=None)
    parser.add_argument("--markdown-output", default="methodology-guard.md")
    parser.add_argument("--json-output", default="methodology-guard.json")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    rules = load_tiny_yaml_list_config(args.rules_path)
    kind, results = run_checks(args.kind, args.title, args.body or "", rules)
    failed = [result for result in results if not result.passed]

    markdown = render_markdown(kind, results, rules["reference_artifacts"])
    with open(args.markdown_output, "w", encoding="utf-8") as handle:
        handle.write(markdown)

    payload = {
        "kind": kind,
        "status": "pass" if not failed else "needs-attention",
        "passed": len(results) - len(failed),
        "total": len(results),
        "failed": [result.__dict__ for result in failed],
        "results": [result.__dict__ for result in results],
        "rules_path": args.rules_path,
    }
    with open(args.json_output, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)

    print(markdown)

    if args.strict and failed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
