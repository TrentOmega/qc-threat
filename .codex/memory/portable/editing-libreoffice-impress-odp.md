# Editing LibreOffice Impress (.odp) Files Programmatically

**Date:** 2026-03-15
**Topic:** Modifying ODP presentations via Python/XML manipulation.

## Reusable Pattern

ODP files are ZIP archives containing XML. Slides, text, styles, and images can be modified by extracting the ZIP, editing `content.xml`, and repacking.

## Trigger Conditions

- Need to add, modify, or remove slides programmatically.
- Batch operations on presentations (e.g., adding reference slides from a data source).
- When manual editing in the GUI is impractical for repetitive content.

## Recommended Workflow

1. **Backup** the original file.
2. **Extract** the ODP as a ZIP.
3. **Examine existing slides** to understand styles (TN, grN, PN) and layout patterns.
4. **Modify** `content.xml` using Python string manipulation or XML parsing.
5. **Repack** with mimetype as first entry, uncompressed (`ZIP_STORED`).
6. **Validate** XML with `xml.etree.ElementTree.parse()`.
7. **Open in Impress** to visually verify.

## Failure Modes / Caveats

1. **Hyperlinks:** Use `<text:a xlink:href="URL" xlink:type="simple">visible text</text:a>` — do NOT wrap `text:span` inside `text:a`. It breaks rendering.
2. **mimetype:** Must be the first file in the ZIP and stored uncompressed, or LibreOffice won't open it.
3. **Style references:** Only use styles (grN, TN, PN) that already exist in `office:automatic-styles`. New styles must be defined before use.
4. **draw:name uniqueness:** Every element's `draw:name` must be unique across the entire presentation.
5. **Text overflow:** Max ~5 items with title + description + URL per slide at 12pt/9pt mixed sizes. Calculate body height as `items * 4 lines * 0.55cm`.
6. **Slide insertion point:** Insert new `<draw:page>` elements before `<presentation:settings>` tag.

## Minimal Checklist

- [ ] Backup original `.odp`
- [ ] Extract ZIP
- [ ] Identify existing text styles from content.xml
- [ ] Build new slide XML matching existing layout
- [ ] Insert before `<presentation:settings>`
- [ ] Repack with mimetype first + uncompressed
- [ ] Validate XML
- [ ] Open in Impress to verify
