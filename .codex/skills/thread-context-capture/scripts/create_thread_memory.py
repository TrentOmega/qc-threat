#!/usr/bin/env python3
"""Create reusable thread-memory note skeletons for project and portable context."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_ROOT.parents[2]
PROJECT_TEMPLATE_PATH = SKILL_ROOT / "references" / "project-memory-template.md"
PORTABLE_TEMPLATE_PATH = SKILL_ROOT / "references" / "portable-memory-template.md"
DEFAULT_PROJECT_DIR = REPO_ROOT / "notes" / "thread-memory"
DEFAULT_PORTABLE_DIR = REPO_ROOT / ".codex" / "memory" / "portable"


@dataclass(frozen=True)
class NoteSpec:
    output_path: Path
    template_path: Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create a project thread-memory note and, optionally, a reduced portable note."
        )
    )
    parser.add_argument("title", help="Human-readable topic title.")
    parser.add_argument(
        "--slug",
        help="Override the generated filename slug.",
    )
    parser.add_argument(
        "--date",
        dest="note_date",
        default=date.today().isoformat(),
        help="Date to record in the note (default: today, YYYY-MM-DD).",
    )
    parser.add_argument(
        "--project-dir",
        type=Path,
        default=DEFAULT_PROJECT_DIR,
        help=f"Directory for project-specific notes (default: {DEFAULT_PROJECT_DIR}).",
    )
    parser.add_argument(
        "--portable-dir",
        type=Path,
        default=DEFAULT_PORTABLE_DIR,
        help=f"Directory for portable notes (default: {DEFAULT_PORTABLE_DIR}).",
    )
    parser.add_argument(
        "--portable",
        action="store_true",
        help="Also create the reduced portable note.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing output files.",
    )
    return parser.parse_args()


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "thread-memory"


def render_template(template_path: Path, *, title: str, slug: str, note_date: str) -> str:
    template = template_path.read_text(encoding="utf-8")
    return (
        template.replace("{{TITLE}}", title)
        .replace("{{DATE}}", note_date)
        .replace("{{SLUG}}", slug)
    )


def write_note(spec: NoteSpec, content: str, *, force: bool) -> None:
    spec.output_path.parent.mkdir(parents=True, exist_ok=True)
    if spec.output_path.exists() and not force:
        raise FileExistsError(
            f"{spec.output_path} already exists. Use --force to overwrite."
        )
    spec.output_path.write_text(content, encoding="utf-8")


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def build_note_specs(args: argparse.Namespace, slug: str) -> list[NoteSpec]:
    specs = [
        NoteSpec(
            output_path=args.project_dir / f"{slug}.md",
            template_path=PROJECT_TEMPLATE_PATH,
        )
    ]
    if args.portable:
        specs.append(
            NoteSpec(
                output_path=args.portable_dir / f"{slug}.md",
                template_path=PORTABLE_TEMPLATE_PATH,
            )
        )
    return specs


def main() -> int:
    args = parse_args()
    slug = args.slug or slugify(args.title)
    specs = build_note_specs(args, slug)

    for spec in specs:
        content = render_template(
            spec.template_path,
            title=args.title,
            slug=slug,
            note_date=args.note_date,
        )
        write_note(spec, content, force=args.force)
        print(display_path(spec.output_path))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
