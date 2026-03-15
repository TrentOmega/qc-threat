# Quantum Threat to Bitcoin

Presentation project for a talk on quantum computing risks to Bitcoin, post-quantum migration, and Bitcoin-specific mitigation paths such as BIP-360 / P2MR.

## Project Layout

- [`qc-threat-pres.md`](/home/user/Documents/Projects/qc-threat/qc-threat-pres.md): talk outline, notes, and reference source of truth.
- [`scripts/build_preso.py`](/home/user/Documents/Projects/qc-threat/scripts/build_preso.py): generates the slide deck as `.pptx` and optionally converts it to `.odp`.
- [`scripts/append_odp_references.py`](/home/user/Documents/Projects/qc-threat/scripts/append_odp_references.py): appends generated reference slides onto the preserved Impress deck.
- [`assets/images`](/home/user/Documents/Projects/qc-threat/assets/images): images used in the talk.
- [`assets/charts`](/home/user/Documents/Projects/qc-threat/assets/charts): generated charts and supporting figures.
- [`assets/research`](/home/user/Documents/Projects/qc-threat/assets/research): local source papers and extracts used while preparing the talk.
- [`quantum-threat-bitcoin-bushbash.odp`](/home/user/Documents/Projects/qc-threat/quantum-threat-bitcoin-bushbash.odp): working LibreOffice Impress deck.
- [`quantum-threat-bitcoin-bushbash.pptx`](/home/user/Documents/Projects/qc-threat/quantum-threat-bitcoin-bushbash.pptx): generated PowerPoint deck.
- [`quantum-threat-bitcoin-bushbash.pdf`](/home/user/Documents/Projects/qc-threat/quantum-threat-bitcoin-bushbash.pdf): exported PDF version.

## How It Works

There are effectively two presentation tracks in this repo:

1. A generated slide deck built from Python in [`scripts/build_preso.py`](/home/user/Documents/Projects/qc-threat/scripts/build_preso.py).
2. A preserved LibreOffice Impress deck that may contain newer manual edits not represented in the generated `.pptx`.

Because of that, the current workflow for references is:

1. Generate updated reference slides into the `.pptx`.
2. Convert that generated `.pptx` to a temporary `.odp`.
3. Append only the reference slides from that temporary `.odp` onto the preserved Impress deck using [`scripts/append_odp_references.py`](/home/user/Documents/Projects/qc-threat/scripts/append_odp_references.py).

## Build

### Generate the PowerPoint deck

```bash
python3 scripts/build_preso.py --no-odp
```

### Generate PowerPoint and attempt ODP conversion

```bash
python3 scripts/build_preso.py
```

This conversion depends on LibreOffice / `soffice` being available.

### Refresh the final Impress deck with generated reference slides

Typical flow:

```bash
python3 scripts/build_preso.py --no-odp
soffice --headless --convert-to odp --outdir /tmp/qc-ref-src quantum-threat-bitcoin-bushbash.pptx
python3 scripts/append_odp_references.py \
  quantum-threat-bitcoin-bushbash.odp.bak \
  /tmp/qc-ref-src/quantum-threat-bitcoin-bushbash.odp \
  /tmp/quantum-threat-bitcoin-bushbash.merged.odp
mv /tmp/quantum-threat-bitcoin-bushbash.merged.odp quantum-threat-bitcoin-bushbash.odp
```

## Dependencies

- Python 3
- `python-pptx`
- `matplotlib`
- LibreOffice / `soffice` for `.odp` conversion

## Notes

- The reference section is sourced from the `## References` section in [`qc-threat-pres.md`](/home/user/Documents/Projects/qc-threat/qc-threat-pres.md).
- The build script also generates chart assets under [`assets/charts`](/home/user/Documents/Projects/qc-threat/assets/charts).
- The final `.odp` is intentionally treated as the presentation of record when it contains newer manual Impress edits.
