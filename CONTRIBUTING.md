# Contributing

**English** | [简体中文](CONTRIBUTING.zh-CN.md)

Contributions that add resources, correct source interpretations, or improve translations are welcome.

## Inclusion criteria

Include environments, benchmarks, datasets, generation pipelines, training frameworks, and provider research relevant to workplace communication, collaboration, or agent post-training. Adjacent application, desktop, and customer-service resources should have a clear connection to that scope.

For resources focused solely on coding, general web browsing, or robotics, consider the broader collections linked in the README.

## Source requirements

- Prefer official repositories, papers, dataset cards, and product documentation.
- State what is actually released: a paper, trajectories, data, runnable environment code, or a training pipeline.
- Attribute benchmark scores, training gains, and cost estimates to the original authors. Include the evaluation setup when available.
- Distinguish company statements from independent reporting.
- Use `—` when a fact is unspecified or has not been verified. Avoid claims such as “the only,” “the best,” or “fully anonymized” without sufficient evidence.
- Record artifact-specific license terms. A missing repository license file is recorded as `none`; an unknown license is not an open license.

## Update workflow

README table blocks are generated. Edit the CSV records rather than the generated tables. Link badges, category emoji, and the count badges under the title are generated as well; to give a new category an emoji, add it to `ICONS` in `scripts/build_readme.py`.

1. Add or update a record in the appropriate `data/*.csv` file.
2. Update the matching row in `data/en/*.csv`. Keep the same row order, schema, URLs, dates, and `repo_license` values. Translate descriptions and explain unfamiliar local product names where useful.
3. Run `python3 scripts/build_readme.py` to regenerate both README versions.
4. Run `python3 scripts/build_readme.py --check` to check translation alignment and generated tables.
5. If paper references change, run `python3 scripts/make_bib.py` to refresh `data/papers.bib` from arXiv.
6. Run `python3 scripts/verify.py` to check repository metadata and arXiv identifiers. This requires network access and uses `gh` when available, otherwise `curl`. It also refreshes the star-count snapshot in `data/stars.json`; rerun step 3 afterwards so the star badges show the new counts.

When editing introductory text or section structure, update both `README.md` and `README.zh-CN.md` directly, outside generated markers. Keep `<details>` content separated by blank lines so GitHub renders the Markdown tables. Section headings carry explicit `<a id>` anchors that the navigation line links to; keep them when renaming a heading.

## Record schema

Environment, training, and dataset tables share these fields:

| Field | Meaning |
|---|---|
| `name`, `org` | Resource name and organization, if known |
| `date` | First paper publication year/month, when available |
| `code_url`, `paper_url`, `data_url` | Official source links; leave absent links empty |
| `repo_license` | GitHub license identifier; `none` if no license file is identified; empty if there is no repository |

Table-specific fields:

| File | Fields |
|---|---|
| `environments.csv` | `type`: category; `apps`: scope; `scale`: tools/tasks; `data_source`: provenance; `grading`: evaluation; `best_result`: reported score; `state_backend`: implementation; `availability`: release/license notes |
| `training.csv` | `category`: method type; `method`: approach; `training_setup`: model, algorithm, data, compute; `reported_result`: author-reported result; `released`: available artifacts; `license_note`: license notes |
| `datasets.csv` | `kind`: real/synthetic/mixed; `content`: corpus contents; `scale`: size; `privacy_or_generation`: processing or generation; `license_note`: license notes |
| `vendors.csv` | `name`, `founded`, `sells`, `data_source`, `openness`, `links` (Markdown links) |
| `related_lists.csv` | `repo` (`owner/name`), `covers` |

Some fields are retained in CSV for research use even when omitted from the compact README tables. The detailed survey and provider profiles are currently in Chinese; their language is labeled in the English README.

## Suggested submission notes

Explain why the resource fits, link the supporting sources, describe any uncertainty, and state which verification commands were run. For corrections, identify the previous claim and the evidence supporting the replacement.
