#!/usr/bin/env python3
"""Render English and Chinese README tables from paired CSV files.

Usage: python3 scripts/build_readme.py [--check]
Edit data/*.csv and data/en/*.csv; generated blocks are replaced in place.
Link badges, category emoji, and the header count badges are generated too. Star badges use the
snapshot in data/stars.json, which scripts/verify.py refreshes.
"""
import argparse
import csv
import json
import re
from pathlib import Path
from urllib.parse import quote, urlparse

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ('environments', 'training', 'datasets', 'vendors', 'related_lists')
GITHUB = 'https://github.com/'
SHIELDS = 'https://img.shields.io'
# Category emoji, keyed by the English value; Chinese rows reuse the emoji of the aligned English row.
ICONS = {
    'Communication': '💬', 'Enterprise': '🏢', 'Personal / desktop': '🖥️', 'Real-session reconstruction': '🔁',
    'Training evidence': '📈', 'Environment + training': '🧩', 'Training framework': '🧰',
    'Environment generation': '🏗️', 'LLM simulation': '🤖', 'Trajectory synthesis': '🧵',
    'Experience distillation': '⚗️', 'Infrastructure': '🔧',
    'Real': '📬', 'Real email / synthetic QA': '🔀', 'Synthetic': '🧪',
}
# Header count badges: (label key, source, color, link target)
STATS = [('environments', 'environments', '1f6feb', '#environments'), ('training', 'training', '8250df', '#training'),
         ('datasets', 'datasets', '1a7f37', '#datasets'), ('vendors', 'vendors', '9a6700', '#providers'),
         ('papers', None, 'b31b1b', 'data/papers.bib')]
LABELS = {
    'en': {'code': 'Code', 'site': 'Website', 'paper': 'Paper', 'data': 'Data',
           'env': ['Resource', 'Category', 'Applications / scope', 'Release / license'],
           'env_details': ['Resource', 'Scale / data source', 'Evaluation / reported result', 'State backend'],
           'training': ['Resource', 'Category', 'Method', 'Release / license'],
           'training_details': ['Resource', 'Training setup', 'Reported result'],
           'datasets': ['Resource', 'Source / scale', 'Content', 'Processing / license'],
           'vendors': ['Provider', 'Offering', 'Data production', 'Public information'],
           'related_lists': ['Collection', 'Stars', 'Focus'],
           'stats': {'environments': 'environments', 'training': 'generation & training', 'datasets': 'datasets',
                     'vendors': 'providers', 'papers': 'papers'}},
    'zh': {'code': '代码', 'site': '官网', 'paper': '论文', 'data': '数据',
           'env': ['资源', '类型', '应用与任务范围', '开放情况与许可'],
           'env_details': ['资源', '规模与数据来源', '评测方式与报告结果', '状态后端'],
           'training': ['资源', '类别', '方法', '开放情况与许可'],
           'training_details': ['资源', '训练设置', '报告结果'],
           'datasets': ['资源', '来源与规模', '内容', '处理方式与许可'],
           'vendors': ['供给方', '产品与服务', '数据生产方式', '公开资料'],
           'related_lists': ['清单', 'Star 数', '收录重点'],
           'stats': {'environments': '环境', 'training': '生成与训练', 'datasets': '数据集',
                     'vendors': '供给方', 'papers': '论文'}},
}


def load(section, lang):
    path = ROOT / 'data' / ('en' if lang == 'en' else '') / f'{section}.csv'
    with path.open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f))
    if any(None in row or any(v is None for v in row.values()) for row in rows):
        raise ValueError(f'Malformed CSV: {path}')
    return rows


def cell(value):
    return (value or '—').replace('|', r'\|').replace('\n', '<br>')


def table(headers, rows):
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '|' + '---|' * len(headers)] +
                     ['| ' + ' | '.join(cell(v) for v in row) + ' |' for row in rows])


def combined(*values):
    return '<br>'.join(v for v in values if v and v != '—') or '—'


def badge(alt, label, message, color, url, logo=''):
    text = '-'.join(quote(v.replace('-', '--').replace('_', '__'), safe='') for v in (label, message))
    query = f'?logo={logo}&logoColor=white' if logo else ''
    return f'[![{alt}]({SHIELDS}/badge/{text}-{color}{query})]({url})'


def stars(alt, slug):
    """Static star badge from the snapshot; live star badges intermittently fail behind GitHub's image proxy."""
    path = ROOT / 'data' / 'stars.json'
    count = (json.loads(path.read_text(encoding='utf-8'))['stars'] if path.exists() else {}).get(slug)
    if count is None:
        return badge(alt, 'code', 'GitHub', '24292f', GITHUB + slug, 'github')
    text = str(count)
    if count >= 1000:
        text = (f'{count / 1000:.0f}' if count >= 10000 else f'{count / 1000:.1f}'.removesuffix('.0')) + 'k'
    return badge(alt, 'stars', text, '007ec6', GITHUB + slug, 'github')


def links(row, lang):
    labels, out = LABELS[lang], []
    code, paper, data = row.get('code_url'), row.get('paper_url'), row.get('data_url')
    if code and code.startswith(GITHUB):
        out.append(stars(labels['code'], code[len(GITHUB):].strip('/')))
    elif code:
        out.append(badge(labels['site'], 'website', urlparse(code).netloc, '0a7ea4', code))
    if paper:
        arxiv = re.search(r'arxiv\.org/abs/([\d.]+)', paper)
        out.append(badge(labels['paper'], 'arXiv', arxiv.group(1), 'b31b1b', paper, 'arxiv') if arxiv
                   else badge(labels['paper'], 'paper', urlparse(paper).netloc, '6e7781', paper))
    if data:
        host = urlparse(data).netloc
        out.append(badge(labels['data'], 'data', 'Hugging Face', 'ffd21e', data, 'huggingface') if host == 'huggingface.co'
                   else badge(labels['data'], 'data', host, '6e7781', data))
    return ' '.join(out)


def name(row, lang):
    meta = ' · '.join(v for v in (row.get('org'), row.get('date')) if v and v != '—')
    return combined(f"**{row['name']}**", meta, links(row, lang))


def tag(value, key):
    return f'{ICONS[key]} {value}' if key in ICONS else value


def stats(lang):
    labels, out = LABELS[lang]['stats'], []
    for key, section, color, target in STATS:
        count = len(load(section, lang)) if section else len(
            re.findall(r'^@', (ROOT / 'data' / 'papers.bib').read_text(encoding='utf-8'), re.M))
        out.append(badge(labels[key], labels[key], str(count), color, target))
    return '\n'.join(out)


def render(section, lang, detail=False):
    rows, en, labels = load(section, lang), load(section, 'en'), LABELS[lang]
    if section == 'environments':
        if detail:
            return table(labels['env_details'], [[f"**{r['name']}**", combined(r['scale'], r['data_source']),
                          combined(r['grading'], r['best_result']), r['state_backend']] for r in rows])
        return table(labels['env'], [[name(r, lang), tag(r['type'], e['type']), r['apps'], r['availability']]
                                     for r, e in zip(rows, en)])
    if section == 'training':
        if detail:
            return table(labels['training_details'], [[f"**{r['name']}**", r['training_setup'], r['reported_result']] for r in rows])
        return table(labels['training'], [[name(r, lang), tag(r['category'], e['category']), r['method'],
                      combined(r['released'], r['license_note'])] for r, e in zip(rows, en)])
    if section == 'datasets':
        return table(labels[section], [[name(r, lang), combined(tag(r['kind'], e['kind']), r['scale']), r['content'],
                      combined(r['privacy_or_generation'], r['license_note'])] for r, e in zip(rows, en)])
    if section == 'vendors':
        return table(labels[section], [[f"**{r['name']}**", r['sells'], r['data_source'],
                      combined(r['openness'], r['links'])] for r in rows])
    return table(labels[section], [[f"[{r['repo']}]({GITHUB}{r['repo']})", stars('Stars', r['repo']), r['covers']]
                                   for r in rows])


def validate_pair(section):
    zh, en = load(section, 'zh'), load(section, 'en')
    if len(zh) != len(en):
        raise ValueError(f'Translation count mismatch: {section}')
    identity = ['repo'] if section == 'related_lists' else ['code_url', 'paper_url', 'data_url', 'repo_license', 'date']
    for i, (a, b) in enumerate(zip(zh, en), 1):
        if a.keys() != b.keys() or any(a.get(k) != b.get(k) for k in identity):
            raise ValueError(f'Translation identity/schema mismatch: {section}, row {i}')
        if any(re.search(r'[\u4e00-\u9fff]', v) for k, v in b.items() if k != 'name'):
            raise ValueError(f'Untranslated English field: {section}, row {i}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check generated blocks without writing')
    args = parser.parse_args()
    for section in SECTIONS:
        validate_pair(section)
    stale = []
    pending = []
    for lang, filename in [('en', 'README.md'), ('zh', 'README.zh-CN.md')]:
        path = ROOT / filename
        original = text = path.read_text(encoding='utf-8')
        blocks = {s: render(s, lang) for s in SECTIONS}
        blocks.update(environment_details=render('environments', lang, True),
                      training_details=render('training', lang, True), stats=stats(lang))
        for key, body in blocks.items():
            pattern = re.compile(rf'(<!-- BEGIN:{key} -->\n).*?(<!-- END:{key} -->)', re.S)
            if len(pattern.findall(text)) != 1:
                raise ValueError(f'Expected one marker pair for {key} in {filename}')
            text = pattern.sub(lambda m, body=body: m.group(1) + body + '\n' + m.group(2), text)
        if text != original:
            stale.append(filename)
        pending.append((path, text))
    if args.check and stale:
        raise SystemExit('Outdated generated tables: ' + ', '.join(stale))
    if not args.check:
        for path, text in pending:
            path.write_text(text, encoding='utf-8')
    print('Bilingual tables ' + ('checked' if args.check else 'updated') + ': ' +
          ', '.join(f'{s}: {len(load(s, "zh"))}' for s in SECTIONS))


if __name__ == '__main__':
    main()
