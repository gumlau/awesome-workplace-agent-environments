#!/usr/bin/env python3
"""复核 data/ 下各张表里的仓库和论文。

- GitHub 仓库：是否还在、是否归档、许可是否和表里一致、星数、最近更新。
- arXiv 论文：编号是否存在，顺带打印标题。
- 把查到的星数写进 data/stars.json，README 里的星数徽章用的是这份快照。

用法：python3 scripts/verify.py
需要：curl。装了并登录了 gh 的话会优先用它（未登录的 GitHub API 每小时只有 60 次）。
"""
import csv
import json
import re
import shutil
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TABLES = ["environments", "training", "datasets"]
ATOM = {"a": "http://www.w3.org/2005/Atom"}


def run(cmd: list[str]) -> str:
    return subprocess.run(cmd, capture_output=True, text=True).stdout


def github_repo(slug: str) -> dict | None:
    if shutil.which("gh"):
        out = run(["gh", "api", f"repos/{slug}"])
    else:
        out = run(["curl", "-sS", "-m", "30", f"https://api.github.com/repos/{slug}"])
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        return None
    return data if "full_name" in data else None


def arxiv_titles(ids: list[str]) -> dict[str, str]:
    titles: dict[str, str] = {}
    for i in range(0, len(ids), 25):
        chunk = ids[i:i + 25]
        url = "https://export.arxiv.org/api/query?max_results=50&id_list=" + ",".join(chunk)
        out = run(["curl", "-sS", "-L", "-m", "40", url])
        if "<feed" in out:
            for entry in ET.fromstring(out).findall("a:entry", ATOM):
                aid = entry.findtext("a:id", default="", namespaces=ATOM).rsplit("/abs/", 1)[-1]
                title = re.sub(r"\s+", " ", entry.findtext("a:title", default="", namespaces=ATOM)).strip()
                if aid:
                    titles[re.sub(r"v\d+$", "", aid)] = title
        time.sleep(3)  # arXiv 要求每 3 秒最多一次请求
    return titles


def main() -> int:
    rows: list[dict[str, str]] = []
    for name in TABLES:
        with open(ROOT / "data" / f"{name}.csv", encoding="utf-8", newline="") as f:
            rows += list(csv.DictReader(f))
    # 相关清单只有仓库名，补成同样的字段
    with open(ROOT / "data" / "related_lists.csv", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            rows.append({"name": r["repo"], "code_url": f"https://github.com/{r['repo']}",
                         "paper_url": "", "repo_license": ""})
    problems = 0
    stars: dict[str, int] = {}

    print("== GitHub 仓库 ==")
    for row in rows:
        m = re.match(r"https://github\.com/([^/]+/[^/]+)/?$", row["code_url"])
        if not m:
            continue
        repo = github_repo(m.group(1))
        if repo is None:
            print(f"[缺失] {row['name']}: {row['code_url']}")
            problems += 1
            continue
        stars[m.group(1)] = repo["stargazers_count"]
        spdx = (repo.get("license") or {}).get("spdx_id") or "none"
        flags = []
        if repo.get("archived"):
            flags.append("已归档")
        if repo["full_name"].lower() != m.group(1).lower():
            flags.append(f"已改名为 {repo['full_name']}")
        expected = row["repo_license"]
        # 表里没填许可的不比对；GitHub 认不出的许可会返回 NOASSERTION，也不算不一致
        if expected and spdx not in ("NOASSERTION", expected):
            flags.append(f"许可不一致：表里是 {expected}，GitHub 是 {spdx}")
        if flags:
            problems += 1
        print(f"{'[注意]' if flags else '[正常]'} {row['name']}: ★{repo['stargazers_count']} "
              f"{spdx} 更新于 {repo['pushed_at'][:10]} {'；'.join(flags)}")

    if stars:
        # 没查到的仓库保留上一次的星数
        path = ROOT / "data" / "stars.json"
        old = json.loads(path.read_text(encoding="utf-8"))["stars"] if path.exists() else {}
        snapshot = {"updated": time.strftime("%Y-%m-%d"), "stars": dict(sorted({**old, **stars}.items()))}
        path.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")

    print("\n== arXiv 论文 ==")
    ids = {}
    for row in rows:
        m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{5})", row["paper_url"])
        if m:
            ids[m.group(1)] = row["name"]
    titles = arxiv_titles(sorted(ids))
    for aid, name in sorted(ids.items()):
        if aid in titles:
            print(f"[正常] {aid} {name}: {titles[aid][:80]}")
        else:
            print(f"[缺失] {aid} {name}")
            problems += 1

    print(f"\n共 {len(rows)} 条，需要处理的问题 {problems} 个。")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
