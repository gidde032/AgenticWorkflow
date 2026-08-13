#!/usr/bin/env python3
"""Validate a documentation/GitHub migration project profile."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ModuleNotFoundError:
    print("error: PyYAML is required to validate migration profiles", file=sys.stderr)
    raise SystemExit(2)


PROHIBITED_ACTIONS = {
    "merge_pull_request",
    "tag_or_create_release",
    "change_repository_visibility",
    "delete_branches",
    "weaken_quality_gates",
    "destructive_cleanup",
    "change_product_scope",
    "publish_internal_continuity_documents",
    "combine_unpublished_product_work_with_migration",
}
PLACEHOLDER_TOKENS = ("DECISION_REQUIRED", "TBD", "TODO", "<replace", "<absolute")


def load_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"file does not exist: {path}") from None
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML: {exc}") from None


def get(data: dict[str, Any], dotted: str) -> Any:
    value: Any = data
    for key in dotted.split("."):
        if not isinstance(value, dict) or key not in value:
            raise KeyError(dotted)
        value = value[key]
    return value


def is_absolute_path(value: Any) -> bool:
    return isinstance(value, str) and Path(value).is_absolute()


def find_placeholders(value: Any, path: str = "") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}" if path else str(key)
            found.extend(find_placeholders(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(find_placeholders(child, f"{path}[{index}]"))
    elif isinstance(value, str):
        upper = value.upper()
        if any(token.upper() in upper for token in PLACEHOLDER_TOKENS):
            found.append(path)
    return found


def validate(data: Any, allow_unratified: bool) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["document root must be a mapping"]

    required_paths = [
        "profile_version",
        "ratification.status",
        "project.name",
        "project.local_path",
        "project.github_repository",
        "project.default_branch",
        "project.maintainer_model",
        "migration.branch",
        "migration.checkpoint_policy.merge_automatically",
        "git_preflight.verify_snapshot_before_action",
        "git_preflight.combine_product_work_with_migration",
        "planning_migration.disposition_ledger_path",
        "planning_migration.require_complete_disposition_ledger",
        "planning_migration.require_strict_validation_before_writes",
        "planning_migration.require_strict_validation_before_pr",
        "public_readiness_audit.enabled",
        "artifact_retention.working_directory",
        "artifact_retention.profile_local_only",
        "artifact_retention.full_ledger_local_only",
        "artifact_retention.commit_full_ledger",
        "artifact_retention.pr_summary.public_safe",
        "artifact_retention.pr_summary.include_full_ledger",
        "automation_authority.prohibited_without_new_approval",
    ]
    for dotted in required_paths:
        try:
            get(data, dotted)
        except KeyError:
            errors.append(f"missing required field: {dotted}")

    if errors:
        return errors

    if data["profile_version"] != 1:
        errors.append("profile_version must be 1")
    if get(data, "project.maintainer_model") != "solo":
        errors.append("experimental skill supports only project.maintainer_model: solo")
    if not is_absolute_path(get(data, "project.local_path")):
        errors.append("project.local_path must be absolute")
    if not is_absolute_path(get(data, "planning_migration.disposition_ledger_path")):
        errors.append("planning_migration.disposition_ledger_path must be absolute")
    if not is_absolute_path(get(data, "artifact_retention.working_directory")):
        errors.append("artifact_retention.working_directory must be absolute")

    safety_bools = {
        "migration.checkpoint_policy.merge_automatically": False,
        "git_preflight.verify_snapshot_before_action": True,
        "git_preflight.combine_product_work_with_migration": False,
        "planning_migration.require_complete_disposition_ledger": True,
        "planning_migration.require_strict_validation_before_writes": True,
        "planning_migration.require_strict_validation_before_pr": True,
        "artifact_retention.profile_local_only": True,
        "artifact_retention.full_ledger_local_only": True,
        "artifact_retention.commit_full_ledger": False,
        "artifact_retention.pr_summary.public_safe": True,
        "artifact_retention.pr_summary.include_full_ledger": False,
    }
    for dotted, expected in safety_bools.items():
        if get(data, dotted) is not expected:
            errors.append(f"{dotted} must be {str(expected).lower()}")

    prohibited = set(get(data, "automation_authority.prohibited_without_new_approval"))
    missing_prohibitions = sorted(PROHIBITED_ACTIONS - prohibited)
    if missing_prohibitions:
        errors.append(
            "automation_authority.prohibited_without_new_approval is missing: "
            + ", ".join(missing_prohibitions)
        )

    if not allow_unratified:
        if get(data, "ratification.status") != "approved":
            errors.append("ratification.status must be approved for execute mode")
        if not get(data, "ratification.approved_by"):
            errors.append("ratification.approved_by is required for execute mode")
        if not get(data, "ratification.approved_on"):
            errors.append("ratification.approved_on is required for execute mode")
        placeholder_paths = find_placeholders(data)
        if placeholder_paths:
            errors.append(
                "unresolved placeholder values at: " + ", ".join(placeholder_paths)
            )
        resolved_string_fields = [
            "project.name",
            "project.github_repository",
            "project.default_branch",
            "migration.branch",
            "migration.objective",
            "git_preflight.unpublished_history_strategy",
            "documentation.internal_docs_policy",
            "github.milestone_strategy",
            "license.type",
            "visibility.current",
        ]
        for dotted in resolved_string_fields:
            try:
                value = get(data, dotted)
            except KeyError:
                errors.append(f"missing required decision field: {dotted}")
                continue
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{dotted} must be resolved for execute mode")

        nonempty_list_fields = [
            "planning_migration.audit_sources",
            "quality.required_commands",
            "safety.project_specific_boundaries",
        ]
        for dotted in nonempty_list_fields:
            try:
                value = get(data, dotted)
            except KeyError:
                errors.append(f"missing required list: {dotted}")
                continue
            if not isinstance(value, list) or not value:
                errors.append(f"{dotted} must be a non-empty list for execute mode")

        backup_directory = data.get("artifact_retention", {}).get("backup_directory")
        if not is_absolute_path(backup_directory):
            errors.append(
                "artifact_retention.backup_directory must be absolute for execute mode"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("profile", type=Path)
    parser.add_argument("--allow-unratified", action="store_true")
    args = parser.parse_args()

    try:
        data = load_yaml(args.profile)
        errors = validate(data, args.allow_unratified)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    state = "draft" if args.allow_unratified else "approved"
    print(f"valid {state} migration profile: {args.profile}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
