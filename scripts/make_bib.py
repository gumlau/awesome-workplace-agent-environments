#!/usr/bin/env python3
"""从仓库里出现过的 arXiv 编号生成 data/papers.bib。

扫描所有 .md 文件和 data/ 下的 CSV，向 arXiv API 取标题、作者、年份。
条目内容全部来自 API，不手写。

用法：python3 scripts/make_bib.py
需要：curl。
"""
import re
import subprocess
import time
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "papers.bib"
ATOM = {"a": "http://www.w3.org/2005/Atom"}
ID_PATTERN = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{5})")


def collect_ids() -> list[str]:
    ids: set[str] = set()
    for path in [*ROOT.rglob("*.md"), *(ROOT / "data").glob("*.csv")]:
        ids.update(ID_PATTERN.findall(path.read_text(encoding="utf-8")))
    return sorted(ids)


def ascii_word(text: str) -> str:
    folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", folded.lower())


def fetch(ids: list[str]) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    for i in range(0, len(ids), 25):
        url = "https://export.arxiv.org/api/query?max_results=50&id_list=" + ",".join(ids[i:i + 25])
        out = subprocess.run(["curl", "-sS", "-L", "-m", "40", url], capture_output=True, text=True).stdout
        if "<feed" in out:
            for e in ET.fromstring(out).findall("a:entry", ATOM):
                aid = re.sub(r"v\d+$", "", e.findtext("a:id", default="", namespaces=ATOM).rsplit("/abs/", 1)[-1])
                title = re.sub(r"\s+", " ", e.findtext("a:title", default="", namespaces=ATOM)).strip()
                authors = [a.findtext("a:name", default="", namespaces=ATOM) for a in e.findall("a:author", ATOM)]
                year = e.findtext("a:published", default="", namespaces=ATOM)[:4]
                if aid and authors:
                    first_word = next((w for w in map(ascii_word, title.split()) if len(w) > 3), "paper")
                    key = f"{ascii_word(authors[0].split()[-1])}{year}{first_word}"
                    entries.append({"id": aid, "key": key, "title": title, "year": year,
                                    "author": " and ".join(authors)})
        time.sleep(3)  # arXiv 要求每 3 秒最多一次请求
    return entries


def main() -> None:
    ids = collect_ids()
    entries = fetch(ids)
    missing = sorted(set(ids) - {e["id"] for e in entries})
    lines = ["% 由 scripts/make_bib.py 从 arXiv API 生成，请勿手改。\n"]
    for e in sorted(entries, key=lambda x: x["key"]):
        lines.append("\n".join([
            f"@misc{{{e['key']},",
            f"  title = {{{e['title']}}},",
            f"  author = {{{e['author']}}},",
            f"  year = {{{e['year']}}},",
            f"  eprint = {{{e['id']}}},",
            "  archivePrefix = {arXiv},",
            f"  url = {{https://arxiv.org/abs/{e['id']}}}",
            "}\n",
        ]))
    _ = OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"写入 {len(entries)} 条到 {OUT.relative_to(ROOT)}")
    if missing:
        print("arXiv 没有返回这些编号：", ", ".join(missing))


if __name__ == "__main__":
    main()
