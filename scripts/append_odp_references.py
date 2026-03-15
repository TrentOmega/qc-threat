#!/usr/bin/env python3
"""
Append reference slides from one ODP into another ODP.

This preserves the target deck's existing slides and layout while copying only
the reference slides from the source deck to the end of the target deck.
"""

from __future__ import annotations

import copy
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "anim": "urn:oasis:names:tc:opendocument:xmlns:animation:1.0",
    "draw": "urn:oasis:names:tc:opendocument:xmlns:drawing:1.0",
    "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    "presentation": "urn:oasis:names:tc:opendocument:xmlns:presentation:1.0",
    "style": "urn:oasis:names:tc:opendocument:xmlns:style:1.0",
    "svg": "urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0",
    "table": "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
    "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    "xlink": "http://www.w3.org/1999/xlink",
}

for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)


DRAW_NAME = f"{{{NS['draw']}}}name"
STYLE_NAME = f"{{{NS['style']}}}name"


def read_content_xml(path: Path) -> ET.Element:
    with zipfile.ZipFile(path) as zf:
        return ET.fromstring(zf.read("content.xml"))


def slide_texts(page: ET.Element) -> list[str]:
    texts = []
    for para in page.findall(".//text:p", NS):
        text = "".join(para.itertext()).strip()
        if text:
            texts.append(text)
    return texts


def collect_reference_pages(root: ET.Element) -> list[ET.Element]:
    pages = root.findall(".//draw:page", NS)
    refs = []
    for page in pages:
        texts = slide_texts(page)
        if any(t.startswith("References") for t in texts):
            refs.append(page)
    if not refs:
        raise RuntimeError("No reference slides found in source ODP.")
    return refs


def build_style_map(source_auto: ET.Element, prefix: str) -> dict[str, str]:
    mapping = {}
    for style_el in list(source_auto):
        name = style_el.attrib.get(STYLE_NAME)
        if name:
            mapping[name] = f"{prefix}{name}"
    return mapping


def rewrite_attributes(node: ET.Element, mapping: dict[str, str], suffix: str | None = None) -> None:
    for el in node.iter():
        for attr, value in list(el.attrib.items()):
            if value in mapping:
                el.attrib[attr] = mapping[value]
            elif suffix and attr == DRAW_NAME:
                el.attrib[attr] = f"{value}{suffix}"


def strip_conversion_artifacts(page: ET.Element) -> None:
    junk = {
        "References sourced from qc-threat-pres.md.",
        "<number>",
        "Sources cited in the talk",
    }
    parent_map = {child: parent for parent in page.iter() for child in parent}
    for para in list(page.findall(".//text:p", NS)):
        text = "".join(para.itertext()).strip()
        if text in junk:
            parent = parent_map.get(para)
            if parent is not None:
                parent.remove(para)


def max_page_number(pages: list[ET.Element]) -> int:
    nums = []
    for page in pages:
        name = page.attrib.get(DRAW_NAME, "")
        m = re.fullmatch(r"page(\d+)", name)
        if m:
            nums.append(int(m.group(1)))
    return max(nums, default=0)


def merge_odp(target_path: Path, source_path: Path, output_path: Path) -> int:
    target_root = read_content_xml(target_path)
    source_root = read_content_xml(source_path)

    target_auto = target_root.find("office:automatic-styles", NS)
    source_auto = source_root.find("office:automatic-styles", NS)
    target_pres = target_root.find("office:body/office:presentation", NS)

    if target_auto is None or source_auto is None or target_pres is None:
        raise RuntimeError("Missing required XML sections in one of the ODP files.")

    ref_pages = collect_reference_pages(source_root)

    style_map = build_style_map(source_auto, "refimp_")
    for style_el in list(source_auto):
        cloned = copy.deepcopy(style_el)
        rewrite_attributes(cloned, style_map)
        target_auto.append(cloned)

    existing_pages = target_root.findall(".//draw:page", NS)
    next_page = max_page_number(existing_pages) + 1

    for idx, page in enumerate(ref_pages, start=1):
        cloned_page = copy.deepcopy(page)
        rewrite_attributes(cloned_page, style_map, suffix=f"_ref{idx}")
        strip_conversion_artifacts(cloned_page)
        cloned_page.attrib[DRAW_NAME] = f"page{next_page}"
        next_page += 1
        target_pres.append(cloned_page)

    with zipfile.ZipFile(target_path) as src_zip, zipfile.ZipFile(output_path, "w") as out_zip:
        for info in src_zip.infolist():
            data = src_zip.read(info.filename)
            if info.filename == "content.xml":
                data = ET.tostring(target_root, encoding="utf-8", xml_declaration=True)
            out_zip.writestr(info, data)

    return len(ref_pages)


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print("usage: append_odp_references.py <target.odp> <source.odp> <output.odp>", file=sys.stderr)
        return 2

    target = Path(argv[1])
    source = Path(argv[2])
    output = Path(argv[3])

    count = merge_odp(target, source, output)
    print(f"Appended {count} reference slides to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
