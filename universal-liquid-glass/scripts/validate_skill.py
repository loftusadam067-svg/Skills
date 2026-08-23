#!/usr/bin/env python3
"""Validate the Universal Liquid Glass Agent Skill package.

Stdlib-only so it can run locally or in GitHub Actions without installing deps.
Checks Agent-Skills-style structure, dangling internal references, required files,
frontmatter basics and progressive-disclosure size limits.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"

REQUIRED = {
    "SKILL.md",
    "README.md",
    "KIMI_INSTALL_PROMPT.md",
    "references/design-system.md",
    "references/optics-and-rendering.md",
    "references/apple-native.md",
    "references/web.md",
    "references/react-native.md",
    "references/flutter.md",
    "references/android.md",
    "references/desktop-hybrid.md",
    "references/accessibility-performance.md",
    "references/qa-checklist.md",
    "references/sources.md",
    "evals/evaluation-rubric.md",
    "evals/trigger-cases.md",
    "scripts/validate_skill.py",
    "LICENSE",
}

PATH_RE = re.compile(r"(?<![A-Za-z0-9_./-])((?:references|evals|scripts)/[A-Za-z0-9_.\-/]+)")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    result: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        if not raw or raw.startswith(" ") or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        result[key.strip()] = value.strip().strip('"\'')
    return result


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not SKILL.is_file():
        print("ERROR: SKILL.md is missing", file=sys.stderr)
        return 1

    text = SKILL.read_text(encoding="utf-8")
    lines = text.splitlines()
    fm = parse_frontmatter(text)

    if fm.get("name") != "universal-liquid-glass":
        fail(errors, "frontmatter name must be 'universal-liquid-glass'")

    description = fm.get("description", "")
    if not description:
        fail(errors, "frontmatter description is missing")
    else:
        trigger_terms = ("Liquid Glass", "refractive", "SwiftUI", "React Native")
        missing_terms = [term for term in trigger_terms if term.lower() not in description.lower()]
        if missing_terms:
            warnings.append("description may under-trigger; missing: " + ", ".join(missing_terms))

    if len(lines) > 500:
        fail(errors, f"SKILL.md has {len(lines)} lines; keep it <= 500 for progressive disclosure")

    # Agent Skills recommends <5000 tokens. We cannot tokenize model-specifically,
    # so use a conservative word-count warning rather than a false-precision failure.
    words = len(re.findall(r"\S+", text))
    if words > 3600:
        warnings.append(f"SKILL.md has ~{words} whitespace tokens/words; consider moving more detail to references")

    for rel in sorted(REQUIRED):
        if not (ROOT / rel).is_file():
            fail(errors, f"required file missing: {rel}")

    # Validate every explicit internal path mentioned by SKILL.md.
    referenced = {m.group(1).rstrip(".,;:)") for m in PATH_RE.finditer(text)}
    for rel in sorted(referenced):
        if not (ROOT / rel).exists():
            fail(errors, f"dangling SKILL.md reference: {rel}")

    # Avoid placeholder/template text accidentally shipping.
    forbidden = ("TODO", "TBD", "PASTE GITHUB LINK", "OWNER/REPO")
    for token in forbidden:
        if token in text:
            fail(errors, f"SKILL.md contains unresolved placeholder: {token}")

    # Check all markdown files are UTF-8-readable and not empty.
    for md in ROOT.rglob("*.md"):
        try:
            content = md.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            fail(errors, f"not UTF-8: {md.relative_to(ROOT)}")
            continue
        if not content.strip():
            fail(errors, f"empty markdown file: {md.relative_to(ROOT)}")

    for warning in warnings:
        print(f"WARNING: {warning}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"OK: {ROOT.name} validated ({len(lines)} SKILL.md lines, {len(referenced)} internal references).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
