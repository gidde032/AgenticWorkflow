#!/usr/bin/env python3
"""Verify that a disposition ledger's declared source fingerprints match reality.

The ledger asks each source to carry a fingerprint and a `scan_complete`
attestation. Without this script both are self-reported: an agent that never
re-read a source can still write a plausible-looking hash and pass every other
gate. Recomputing the digest is what makes the ledger evidence rather than
narrative, so run it wherever the ledger is treated as authoritative --
before migration writes, and again before the final draft PR.

Fingerprints are recorded as `sha256:<hex>`. A bare hex digest is accepted for
compatibility with ledgers written before the prefix convention.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ModuleNotFoundError:
    print("error: PyYAML is required to verify source fingerprints", file=sys.stderr)
    raise SystemExit(2)


CHUNK_BYTES = 1 << 20


def load_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"file does not exist: {path}") from None
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML: {exc}") from None


def digest(path: Path) -> str:
    sha = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(CHUNK_BYTES), b""):
            sha.update(chunk)
    return sha.hexdigest()


def normalize(fingerprint: str) -> str:
    value = fingerprint.strip().lower()
    return value.split("sha256:", 1)[1] if value.startswith("sha256:") else value


def resolve(raw_path: str, repository_root: str | None) -> Path:
    path = Path(raw_path)
    if path.is_absolute() or not repository_root:
        return path
    return Path(repository_root) / path


def verify(data: Any, repository_root_override: str | None) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["document root must be a mapping"]

    project = data.get("project")
    project = project if isinstance(project, dict) else {}
    repository_root = repository_root_override or project.get("repository_root")

    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        return ["sources must be a non-empty list"]

    for index, source in enumerate(sources):
        prefix = f"sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{prefix} must be a mapping")
            continue

        source_id = source.get("id") or prefix
        raw_path = source.get("path")
        recorded = source.get("fingerprint")

        if not isinstance(raw_path, str) or not raw_path.strip():
            errors.append(f"{source_id}: path is required to verify a fingerprint")
            continue
        if not isinstance(recorded, str) or not recorded.strip():
            errors.append(f"{source_id}: fingerprint is missing")
            continue

        resolved = resolve(raw_path, repository_root)
        if not resolved.is_file():
            errors.append(f"{source_id}: declared source is not a readable file: {resolved}")
            continue

        actual = digest(resolved)
        if normalize(recorded) != actual:
            errors.append(
                f"{source_id}: fingerprint does not match {resolved} "
                f"(recorded={normalize(recorded)[:16]}..., actual={actual[:16]}...)"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Recompute SHA-256 digests for every source declared in a disposition ledger."
    )
    parser.add_argument("ledger", type=Path)
    parser.add_argument(
        "--repository-root",
        default=None,
        help="Override project.repository_root when resolving relative source paths.",
    )
    parser.add_argument(
        "--print-actual",
        action="store_true",
        help="Print the computed digest for each source. Use when first filling a ledger.",
    )
    args = parser.parse_args()

    try:
        data = load_yaml(args.ledger)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.print_actual:
        project = data.get("project") if isinstance(data, dict) else {}
        root = args.repository_root or (project or {}).get("repository_root")
        for source in data.get("sources") or []:
            if not isinstance(source, dict):
                continue
            raw_path = source.get("path")
            if not isinstance(raw_path, str):
                continue
            resolved = resolve(raw_path, root)
            if resolved.is_file():
                print(f"{source.get('id', '?')}\tsha256:{digest(resolved)}\t{resolved}")
            else:
                print(f"{source.get('id', '?')}\tUNREADABLE\t{resolved}", file=sys.stderr)
        return 0

    errors = verify(data, args.repository_root)
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    count = len(data.get("sources") or [])
    print(f"verified {count} source fingerprint(s) against disk: {args.ledger}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
