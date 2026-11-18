#!/usr/bin/env python3
"""Check local SVG files for basic accessible naming semantics."""
import argparse
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

def local_name(tag): return tag.rsplit("}",1)[-1].lower()

def audit_svg_text(source):
    try: root=ET.fromstring(source)
    except ET.ParseError as exc: return [f"invalid-xml: {exc}"]
    if local_name(root.tag)!="svg": return ["not-svg: root element is not <svg>"]
    if root.attrib.get("aria-hidden","").lower()=="true": return []
    aria_label=root.attrib.get("aria-label","").strip()
    title_text=""
    for node in root.iter():
        if local_name(node.tag)=="title":
            title_text="".join(node.itertext()).strip()
            break
    issues=[]
    if not aria_label and not title_text: issues.append("missing-name: add aria-label or a non-empty <title>")
    if (aria_label or title_text) and root.attrib.get("role")!="img": issues.append('missing-role: add role="img" to the root <svg>')
    return issues

def collect_svg_files(paths,recursive=False):
    found=[]
    for raw in paths:
        path=Path(raw)
        if path.is_file() and path.suffix.lower()==".svg": found.append(path)
        elif path.is_dir():
            iterator=path.rglob("*.svg") if recursive else path.glob("*.svg")
            found.extend(item for item in iterator if item.is_file())
    return sorted(set(found))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths",nargs="+")
    parser.add_argument("--recursive",action="store_true")
    args=parser.parse_args()
    files=collect_svg_files(args.paths,args.recursive)
    if not files: print("No SVG files found.",file=sys.stderr); return 2
    total=0
    for path in files:
        try: issues=audit_svg_text(path.read_text(encoding="utf-8"))
        except OSError as exc: issues=[f"read-error: {exc}"]
        for issue in issues: print(f"{path}: {issue}"); total+=1
    print(f"Checked {len(files)} SVG file(s); found {total} issue(s).")
    return 1 if total else 0

if __name__=="__main__": raise SystemExit(main())
