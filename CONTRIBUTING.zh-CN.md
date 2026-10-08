# 贡献指南

[English](CONTRIBUTING.md) | **简体中文**

欢迎补充资源、纠正来源解读与改进翻译。

## 收录标准

收录与办公通信、协作或 Agent 后训练相关的环境、评测、数据集、生成管线、训练框架及供给方研究。相邻的应用、桌面和客服资源应说明与这一范围的联系。

纯编程、通用网页浏览和机器人方向的资源，可优先提交到 README 列出的相关清单。

## 来源要求

- 优先引用官方仓库、论文、数据卡与产品文档。
- 明确实际开放的内容：论文、轨迹、数据、可运行环境代码或训练管线。
- 评测分数、训练提升与成本估计注明为原作者报告；有实验设置时一并记录。
- 区分公司自述与独立报道。
- 未说明或未核实的事实写 `—`。缺乏充分证据时，避免使用“唯一”“最好”“完全匿名化”等表述。
- 区分代码、数据和模型的许可。仓库未发现许可文件时，`repo_license` 写 `none`；未知许可不等于开放许可。

## 更新流程

README 的表格区块由脚本生成。请修改 CSV 记录，不要直接修改生成的表格。

1. 在对应的 `data/*.csv` 文件中新增或更新记录。
2. 同步修改 `data/en/*.csv` 中的对应行。两个版本保持相同顺序、字段、链接、日期和 `repo_license` 值；翻译描述，并酌情解释国际读者不熟悉的本地产品名称。
3. 运行 `python3 scripts/build_readme.py`，重新生成两个 README。
4. 运行 `python3 scripts/build_readme.py --check`，检查翻译对应关系与生成表格。
5. 论文引用有变化时，运行 `python3 scripts/make_bib.py`，从 arXiv 更新 `data/papers.bib`。
6. 运行 `python3 scripts/verify.py`，核对仓库元数据与 arXiv 标识。该步骤需要网络，优先使用 `gh`，否则使用 `curl`。

介绍文字或章节结构有变化时，直接修改 `README.md` 与 `README.zh-CN.md` 中生成标记以外的内容。`<details>` 内容前后保留空行，确保 GitHub 正确渲染 Markdown 表格。

## 数据字段

环境、训练与数据集三张表共用以下字段：

| 字段 | 含义 |
|---|---|
| `name`、`org` | 资源名称与已知的机构信息 |
| `date` | 论文首发年月，未说明时写 `—` |
| `code_url`、`paper_url`、`data_url` | 官方来源链接；缺少的链接留空 |
| `repo_license` | GitHub 许可标识；未发现许可文件写 `none`，没有仓库留空 |

各表的专用字段：

| 文件 | 字段 |
|---|---|
| `environments.csv` | `type`：类别；`apps`：任务范围；`scale`：工具与任务数；`data_source`：数据来源；`grading`：评测方式；`best_result`：报告分数；`state_backend`：状态实现；`availability`：开放情况与许可 |
| `training.csv` | `category`：方法类别；`method`：方法概述；`training_setup`：模型、算法、数据、算力；`reported_result`：原作者报告结果；`released`：已开放内容；`license_note`：许可说明 |
| `datasets.csv` | `kind`：真实、合成或混合；`content`：语料内容；`scale`：规模；`privacy_or_generation`：处理或生成方法；`license_note`：许可说明 |
| `vendors.csv` | `name`、`founded`、`sells`、`data_source`、`openness`、`links`（Markdown 链接） |
| `related_lists.csv` | `repo`（`owner/name`）、`covers` |

部分字段为研究与检索保留在 CSV 中，不在精简后的首页表格中展示。长篇综述与供给方档案目前为中文，英文首页已标注语言。

## 提交说明建议

说明资源为何适合收录，附上支持来源，指出未确定的信息，并列出已运行的核对命令。纠错时写清原表述与修改依据。
