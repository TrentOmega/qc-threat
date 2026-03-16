---
name: thread-context-capture
description: Distill AI agent threads into reusable project and cross-project memory notes with clear decisions, evidence, risks, and next actions.
---

# Thread Context Capture

Use this skill whenever a thread produces durable knowledge worth preserving, whether that happens after a single important exchange or much later in the thread.

## Goal

Produce two levels of memory from one thread:

- Project memory: enough detail for future work in this repo to resume accurately.
- Portable memory: a reduced, project-agnostic version containing reusable workflow, heuristics, failure modes, and tool patterns.

## What to capture

- Objective: what the thread was trying to achieve.
- Decisions: what was chosen, and why.
- Evidence: commands run, files touched, metrics, outputs, and observations that justify the decisions.
- Constraints: environment rules, assumptions, non-goals, and things intentionally not changed.
- Open questions: unresolved items or risks.
- Next actions: the shortest useful handoff for a follow-up thread.

## What to exclude

- Raw chat transcript dumps.
- Repetitive back-and-forth that did not affect the outcome.
- Secrets, tokens, private identifiers, or irrelevant repo-specific details in the portable copy.
- Large logs unless a short excerpt is necessary to explain a failure mode.

## Recommended structure

### Project memory

- Thread/topic title
- Date
- Goal
- Repo-specific context
- Key findings
- Decisions made
- Evidence
- Files/commands
- Risks/open questions
- Next steps

### Portable memory

- Topic title
- Date
- Reusable pattern or lesson
- Trigger conditions
- Recommended workflow
- Failure modes / caveats
- Minimal example or checklist

## Authoring rules

- Prefer facts over transcript-like narration.
- Keep each note short enough to reread in under two minutes.
- Link to repo files with repo-relative paths when useful.
- Mark inference vs confirmed evidence clearly.
- If a detail is likely to age quickly, include the exact date.

## Per-thread workflow

1. As soon as a memorable result appears, identify whether the outcome is:
   - repo-specific only: useful for one concrete task, file group, or workstream in the current repo,
   - reusable across this repo: still project-bound, but useful for multiple future tasks or threads in the current repo,
   - reusable across projects.
2. Create or update a project memory note with the concrete context needed to resume work.
3. If any lesson generalizes, create or update the portable memory note with sensitive and project-specific details removed.
4. Keep both notes additive and deduplicated:
   - append new findings when they materially change understanding,
   - rewrite existing summaries when the old version would mislead future work.
5. In the next thread, load the smallest relevant note first instead of pasting prior conversation history.

## Update Vs New Note

Update an existing note when:

- The thread is still working on the same underlying goal or decision.
- New evidence changes confidence, but not the core topic.
- You are adding implementation details, test results, file changes, risks, or next steps for the same workstream.
- The existing note would remain the right file for a future thread to read first.

Create a new note when:

- The thread has moved to a meaningfully different objective, even if it came from the same conversation.
- A new decision area appears that would be confusing if mixed into the existing note.
- The earlier note is now complete, and the thread has shifted into a separate phase with different questions or success criteria.
- A future thread would be better served by reading two focused notes rather than one combined note.

Rewrite rather than append when:

- A prior summary is now misleading.
- A decision was reversed.
- Earlier open questions are resolved and the old wording would waste time or create confusion.

Practical threshold:

- Do not update after every message by default.
- Update as soon as there is a durable change in understanding: a decision, confirmed finding, failed approach worth remembering, important constraint, or a materially better next-step plan.
- If the last 5-10 messages did not produce durable knowledge, do not write anything yet.
- If two updates in a row are about different objectives, split them into separate notes.

## Storage suggestion

If the repo does not already define locations, prefer:

- Project memory: `notes/thread-memory/`
- Portable memory source for copying into other repos: `.codex/memory/portable/`

Use stable filenames based on topic, for example:

- `notes/thread-memory/llm-thread-handoff.md`
- `.codex/memory/portable/thread-summarization-workflow.md`

## Helper command

Use the helper bundled with this skill to scaffold note files quickly. Run it from the active project environment:

- `python .codex/skills/thread-context-capture/scripts/create_thread_memory.py "Topic title"`
- `python .codex/skills/thread-context-capture/scripts/create_thread_memory.py "Topic title" --portable`

The helper creates the project note under `notes/thread-memory/` and, with `--portable`, the reduced note under `.codex/memory/portable/`. Override the output directories if a project uses different storage locations.

## Quality bar

A good note lets a new thread answer:

- What problem were we solving?
- What do we now believe is true?
- Why do we believe it?
- What remains uncertain?
- What should happen next?
