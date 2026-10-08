#!/usr/bin/env python3
"""Render English and Chinese README tables from paired CSV files.

Usage: python3 scripts/build_readme.py [--check]
Edit data/*.csv and data/en/*.csv; generated blocks are replaced in place.
"""
import argparse
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ('environments', 'training', 'datasets', 'vendors', 'related_lists')
LABELS = {
    'en': {'code': 'Code', 'site': 'Website', 'paper': 'Paper', 'data': 'Data',
           'env': ['Resource', 'Category', 'Applications / scope', 'Release / license'],
           'env_details': ['Resource', 'Scale / data source', 'Evaluation / reported result', 'State backend'],
           'training': ['Resource', 'Category', 'Method', 'Release / license'],
           'training_details': ['Resource', 'Training setup', 'Reported result'],
           'datasets': ['Resource', 'Source / scale', 'Content', 'Processing / license'],
           'vendors': ['Provider', 'Offering', 'Data production', 'Public information'],
           'related_lists': ['Collection', 'Focus']},
    'zh': {'code': '代码', 'site': '官网', 'paper': '论文', 'data': '数据',
           'env': ['资源', '类型', '应用与任务范围', '开放情况与许可'],
           'env_details': ['资源', '规模与数据来源', '评测方式与报告结果', '状态后端'],
           'training': ['资源', '类别', '方法', '开放情况与许可'],
           'training_details': ['资源', '训练设置', '报告结果'],
           'datasets': ['资源', '来源与规模', '内容', '处理方式与许可'],
           'vendors': ['供给方', '产品与服务', '数据生产方式', '公开资料'],
           'related_lists': ['清单', '收录重点']},
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


def name(row, lang):
    labels = LABELS[lang]
    meta = ' · '.join(v for v in (row.get('org'), row.get('date')) if v and v != '—')
    links = []
    for field, label in [('code_url', 'code'), ('paper_url', 'paper'), ('data_url', 'data')]:
        url = row.get(field)
        if url:
            if field == 'code_url' and not url.startswith('https://github.com/'):
                label = 'site'
            links.append(f'[{labels[label]}]({url})')
    return combined(f"**{row['name']}**", meta, ' · '.join(links))


def render(section, lang, detail=False):
    rows, labels = load(section, lang), LABELS[lang]
    if section == 'environments':
        if detail:
            return table(labels['env_details'], [[f"**{r['name']}**", combined(r['scale'], r['data_source']),
                          combined(r['grading'], r['best_result']), r['state_backend']] for r in rows])
        return table(labels['env'], [[name(r, lang), r['type'], r['apps'], r['availability']] for r in rows])
    if section == 'training':
        if detail:
            return table(labels['training_details'], [[f"**{r['name']}**", r['training_setup'], r['reported_result']] for r in rows])
        return table(labels['training'], [[name(r, lang), r['category'], r['method'],
                      combined(r['released'], r['license_note'])] for r in rows])
    if section == 'datasets':
        return table(labels[section], [[name(r, lang), combined(r['kind'], r['scale']), r['content'],
                      combined(r['privacy_or_generation'], r['license_note'])] for r in rows])
    if section == 'vendors':
        return table(labels[section], [[f"**{r['name']}**", r['sells'], r['data_source'],
                      combined(r['openness'], r['links'])] for r in rows])
    return table(labels[section], [[f"[{r['repo']}](https://github.com/{r['repo']})", r['covers']] for r in rows])


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
        keys = [(s, s, False) for s in SECTIONS] + [('environment_details', 'environments', True), ('training_details', 'training', True)]
        for key, section, detail in keys:
            pattern = re.compile(rf'(<!-- BEGIN:{key} -->\n).*?(<!-- END:{key} -->)', re.S)
            if len(pattern.findall(text)) != 1:
                raise ValueError(f'Expected one marker pair for {key} in {filename}')
            body = render(section, lang, detail)
            text = pattern.sub(lambda m: m.group(1) + body + '\n' + m.group(2), text)
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
