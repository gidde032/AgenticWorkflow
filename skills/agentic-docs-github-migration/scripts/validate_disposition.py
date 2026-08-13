#!/usr/bin/env python3
"""Validate a complete documentation/GitHub migration disposition ledger."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ModuleNotFoundError:
    print("error: PyYAML is required to validate disposition ledgers", file=sys.stderr)
    raise SystemExit(2)


ALLOWED_STATUSES = {
    "completed",
    "ported_to_issue",
    "retained_in_authoritative_doc",
    "rejected_with_rationale",
    "awaiting_human_decision",
}


def load_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"file does not exist: {path}") from None
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML: {exc}") from None


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(data: Any, allow_awaiting: bool, pre_write: bool) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["document root must be a mapping"]
    if data.get("ledger_version") != 1:
        errors.append("ledger_version must be 1")

    audit = data.get("audit")
    if not isinstance(audit, dict):
        errors.append("audit must be a mapping")
    elif not allow_awaiting and audit.get("complete") is not True:
        errors.append("audit.complete must be true for strict validation")

    sources = data.get("sources")
    findings = data.get("findings")
    if not isinstance(sources, list) or not sources:
        errors.append("sources must be a non-empty list")
        sources = []
    if not isinstance(findings, list):
        errors.append("findings must be a list")
        findings = []

    source_ids: set[str] = set()
    declared_findings_by_source: dict[str, set[str]] = {}
    for index, source in enumerate(sources):
        prefix = f"sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{prefix} must be a mapping")
            continue
        source_id = source.get("id")
        if not nonempty(source_id):
            errors.append(f"{prefix}.id is required")
        elif source_id in source_ids:
            errors.append(f"duplicate source id: {source_id}")
        else:
            source_ids.add(source_id)
        for field in ("path", "scope", "fingerprint"):
            if not nonempty(source.get(field)):
                errors.append(f"{prefix}.{field} is required")
        if source.get("scan_complete") is not True:
            errors.append(f"{prefix}.scan_complete must be true")
        declared_finding_ids = source.get("finding_ids")
        if not isinstance(declared_finding_ids, list):
            errors.append(f"{prefix}.finding_ids must be a list")
        elif nonempty(source_id):
            if any(not nonempty(item) for item in declared_finding_ids):
                errors.append(f"{prefix}.finding_ids must contain non-empty strings")
            declared_findings_by_source[source_id] = set(declared_finding_ids)

    finding_ids: set[str] = set()
    referenced_findings_by_source: dict[str, set[str]] = {
        source_id: set() for source_id in source_ids
    }
    for index, finding in enumerate(findings):
        prefix = f"findings[{index}]"
        if not isinstance(finding, dict):
            errors.append(f"{prefix} must be a mapping")
            continue
        finding_id = finding.get("id")
        if not nonempty(finding_id):
            errors.append(f"{prefix}.id is required")
        elif finding_id in finding_ids:
            errors.append(f"duplicate finding id: {finding_id}")
        else:
            finding_ids.add(finding_id)

        if not nonempty(finding.get("summary")):
            errors.append(f"{prefix}.summary is required")
        if not nonempty(finding.get("category")):
            errors.append(f"{prefix}.category is required")
        if not nonempty(finding.get("public_safe_summary")):
            errors.append(f"{prefix}.public_safe_summary is required")

        refs = finding.get("source_refs")
        if not isinstance(refs, list) or not refs:
            errors.append(f"{prefix}.source_refs must be a non-empty list")
        else:
            for ref_index, ref in enumerate(refs):
                ref_prefix = f"{prefix}.source_refs[{ref_index}]"
                if not isinstance(ref, dict):
                    errors.append(f"{ref_prefix} must be a mapping")
                    continue
                source_id = ref.get("source_id")
                if source_id not in source_ids:
                    errors.append(f"{ref_prefix}.source_id is unknown: {source_id}")
                elif nonempty(finding_id):
                    referenced_findings_by_source[source_id].add(finding_id)
                if not nonempty(ref.get("location")):
                    errors.append(f"{ref_prefix}.location is required")

        status = finding.get("status")
        if status not in ALLOWED_STATUSES:
            errors.append(f"{prefix}.status is invalid: {status}")
            continue
        if status == "awaiting_human_decision" and not allow_awaiting:
            errors.append(f"{prefix} still awaits a human decision")

        evidence = finding.get("evidence")
        rationale = finding.get("rationale")
        destination = finding.get("authoritative_destination")
        issue = finding.get("issue")
        issue = issue if isinstance(issue, dict) else {}

        # Dispatch on status alone. Folding a validity test into the first
        # branch happens to work today only because a valid `completed` finding
        # falls through a chain of conditions that are all false anyway -- it
        # would silently misroute the moment a sixth status is added.
        if status == "completed":
            if not (
                isinstance(evidence, list) and any(nonempty(item) for item in evidence)
            ):
                errors.append(f"{prefix}.evidence is required for completed")
        elif status == "ported_to_issue":
            if pre_write:
                if not nonempty(issue.get("proposed_title")):
                    errors.append(
                        f"{prefix}.issue.proposed_title is required before writes"
                    )
            elif not (
                issue.get("number") is not None or nonempty(issue.get("url"))
            ):
                errors.append(
                    f"{prefix}.issue number or url is required for ported_to_issue"
                )
        elif status == "retained_in_authoritative_doc":
            if not nonempty(destination):
                errors.append(
                    f"{prefix}.authoritative_destination is required for retained item"
                )
            if not (
                isinstance(evidence, list) and any(nonempty(item) for item in evidence)
            ):
                errors.append(f"{prefix}.evidence is required for retained item")
        elif status in {"rejected_with_rationale", "awaiting_human_decision"}:
            if not nonempty(rationale):
                errors.append(f"{prefix}.rationale is required for {status}")

    for source_id in source_ids:
        declared = declared_findings_by_source.get(source_id)
        referenced = referenced_findings_by_source.get(source_id, set())
        if declared is not None and declared != referenced:
            errors.append(
                f"source {source_id} finding_ids do not match finding source_refs "
                f"(declared={sorted(declared)}, referenced={sorted(referenced)})"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("ledger", type=Path)
    parser.add_argument("--allow-awaiting-decision", action="store_true")
    parser.add_argument("--pre-write", action="store_true")
    args = parser.parse_args()

    if args.allow_awaiting_decision and args.pre_write:
        parser.error("--allow-awaiting-decision and --pre-write are mutually exclusive")

    try:
        data = load_yaml(args.ledger)
        errors = validate(data, args.allow_awaiting_decision, args.pre_write)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    if args.allow_awaiting_decision:
        mode = "draft"
    elif args.pre_write:
        mode = "pre-write"
    else:
        mode = "final"
    print(f"valid {mode} disposition ledger: {args.ledger}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
