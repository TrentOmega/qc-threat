# AGENTS.md

## Purpose

This repository contains research, presentation source material, generated slide decks, and related website handoff documents for the "Quantum Threat to Bitcoin" project.

## Repository Map

### Core project files

- `README.md`
  Current human-readable project overview and build notes. Some paths may lag behind repo renames, so verify against the actual repo layout before editing workflows.

- `qc-threat-pres-v1.md`
  Main presentation outline, speaker notes, and numbered bibliography for the current presentation deck. Treat this as the source document for the live presentation content unless the user explicitly directs otherwise.

- `qc-threat-log.md`
  Tracking file for new sources, articles, and developments that may be added to a future presentation later. Use this as the intake/backlog for updates rather than inserting every new source directly into the active presentation bibliography.

- `increasing-qubit-size.md`
  Standalone write-up for the follow-up question about logical qubit scaling and ECDLP runtime limits.

### Presentation artifacts

- `quantum-threat-bitcoin-bushbash.odp`
  LibreOffice Impress deck. This is the editable presentation artifact when working in Impress.

- `quantum-threat-bitcoin-bushbash.pptx`
  Generated PowerPoint version of the deck.

- `quantum-threat-bitcoin-bushbash.pdf`
  Exported PDF version of the presentation.

### Website / handoff material

- `qc-threat-website-notes.md`
  Notes used for website adaptation of the presentation material.

- `qc-threat-website-specifiations.md`
  Website specification document. Keep the existing filename spelling unless the user explicitly asks for a rename.

- `lovable-handoff/`
  Bundle of website handoff material, including notes, selected assets, and reference exports.

### Research and notes

- `assets/research/`
  Local copies of papers, PDFs, and extracted text used during research.

- `assets/images/`
  Images used by the presentation and related materials.

- `assets/charts/`
  Generated chart outputs used in slides and related collateral.

- `notes/thread-memory/`
  Thread or session memory documents capturing research conclusions, decisions, and next steps.

- `.codex/`
  Local Codex memory and skills relevant to this repo.

### Scripts

- `scripts/build_preso.py`
  Main deck generation script.

- `scripts/append_odp_references.py`
  Utility for appending generated reference slides into the preserved Impress deck.

## Working Rules

### Source handling

- New source discoveries that are candidates for future deck updates should go into `qc-threat-log.md` first.
- Only add a source directly into `qc-threat-pres-v1.md` when the user clearly wants it incorporated into the active presentation bibliography now.

### Change workflow

- Any change made to this repository should be followed by `git add`, `git commit`, and `git push origin` automatically unless the user explicitly says not to commit or not to push.
- Prefer small, intentional commits with messages that describe the actual repo change.
- Do not leave completed repo edits uncommitted.
- GitHub pushes and other authenticated GitHub operations must use `gh`. If git auth is not already wired up for the current shell, run `gh auth setup-git` before pushing.

### Git expectations

- Primary branch is `main`.
- Remote of record is `origin`.
- Before making assumptions about missing files, check whether the local checkout is behind `origin/main`.
