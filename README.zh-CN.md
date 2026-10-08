# Awesome Workplace Agent Environments

[English](README.md) | **简体中文**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub Star 数](https://img.shields.io/github/stars/gumlau/awesome-workplace-agent-environments?style=flat&logo=github)](https://github.com/gumlau/awesome-workplace-agent-environments)
[![最近更新](https://img.shields.io/github/last-commit/gumlau/awesome-workplace-agent-environments?style=flat)](https://github.com/gumlau/awesome-workplace-agent-environments/commits/main)
[![欢迎提交 PR](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.zh-CN.md)
[![站点](https://img.shields.io/badge/website-gumlau.github.io-0a7ea4)](https://gumlau.github.io/awesome-workplace-agent-environments/README.zh-CN.html)

<!-- BEGIN:stats -->
[![环境](https://img.shields.io/badge/%E7%8E%AF%E5%A2%83-20-1f6feb)](#environments)
[![生成与训练](https://img.shields.io/badge/%E7%94%9F%E6%88%90%E4%B8%8E%E8%AE%AD%E7%BB%83-15-8250df)](#training)
[![数据集](https://img.shields.io/badge/%E6%95%B0%E6%8D%AE%E9%9B%86-9-1a7f37)](#datasets)
[![供给方](https://img.shields.io/badge/%E4%BE%9B%E7%BB%99%E6%96%B9-5-9a6700)](#providers)
[![论文](https://img.shields.io/badge/%E8%AE%BA%E6%96%87-41-b31b1b)](data/papers.bib)
<!-- END:stats -->

> 面向办公 Agent 的环境、评测、训练方法与数据集资源清单。

聚焦邮件、即时通讯、日历、文档与企业应用中的 Agent 任务，汇总任务范围、数据来源、评测方法、状态后端和开放条件，为环境选型与后训练研究提供参考。

📅 **调研快照：2026-10-08。** 当前收录 20 个环境、15 项生成与训练资源、9 个数据集和 5 条供给方资料。部分资源在不同类别中重复出现。

[🚀 快速导航](#quickstart) · [🌐 环境与评测](#environments) · [⚙️ 环境生成与训练](#training) · [🗂️ 数据集与隐私](#datasets) · [🏭 供给方](#providers) · [🔗 相关清单](#related) · [🤝 参与贡献](CONTRIBUTING.zh-CN.md)

## <a id="scope"></a>🔎 收录范围与证据说明

本清单关注办公通信与协作，以及与 Agent 后训练相关的环境和数据。具有参考价值的桌面操作、客服评测也纳入收录。收录为评测环境，并不意味着该项目已经具备强化学习（RL）训练所需的全部能力。

条目依据所链接的论文、仓库、数据卡与供给方资料整理。**报告结果来自原作者，本仓库未复现实验。** 不同评测的指标与设置不同，分数不能直接横向比较。`—` 表示原始资料未说明或尚未核实。仓库与论文标识曾在原始调研中核对；本清单未对运行行为和发布完整性作全面验证。Star 数是调研当日的快照，不是实时数值。

许可说明对应所引用的资源；代码、数据与模型可能适用不同条款。未发现许可文件不代表获得了使用授权。

## <a id="quickstart"></a>🚀 快速导航

| 研究需求 | 起点 | 重点查看 |
|---|---|---|
| 📧 邮件、消息与日历任务 | [Gaia2 / ARE](https://github.com/facebookresearch/meta-agents-research-environments)、[WorkBench](https://github.com/olly-styles/WorkBench) | 应用模型、任务定义与结果评测 |
| 🗄️ 数据库驱动的应用仿真 | [AppWorld](https://github.com/StonyBrookNLP/appworld) | 状态管理与合成数据构造 |
| 🏢 企业应用与业务流程 | [TheAgentCompany](https://github.com/TheAgentCompany/TheAgentCompany)、[SaaS-Bench](https://github.com/UniPat-AI/SaaS-Bench) | 应用部署、检查点与基础设施要求 |
| 🌏 飞书流程与中文任务 | [MCP-Persona](https://github.com/wwh0411/MCP-Persona)、[Workspace-Bench](https://github.com/OpenDataBox/Workspace-Bench) | 仿真接口与中文任务覆盖 |
| 🔁 从真实会话重建任务 | [EnterpriseClawBench](https://github.com/FrontisAI/EnterpriseClawBench)、[DuMateBench](https://dumatebench.com/) | 脱敏、任务筛选与开放范围 |
| 🏗️ 环境生成与初步 RL 实验 | [Agent World Model](https://github.com/Snowflake-Labs/agent-world-model)、[EnvScaler](https://github.com/RUC-NLPIR/EnvScaler)、[ART](https://github.com/OpenPipe/ART) | 生成管线、验证器与可运行的训练示例 |

## <a id="environments"></a>🌐 环境与评测

按通信协作、企业应用、个人与桌面、真实会话重建四类组织。概览表优先展示任务范围与开放情况，具体规模、数据来源和评测细节放在下方折叠表中。

<!-- BEGIN:environments -->
| 资源 | 类型 | 应用与任务范围 | 开放情况与许可 |
|---|---|---|---|
| **Gaia2 / ARE**<br>Meta · 2026-02<br>[![代码](https://img.shields.io/badge/stars-562-007ec6?logo=github&logoColor=white)](https://github.com/facebookresearch/meta-agents-research-environments) [![论文](https://img.shields.io/badge/arXiv-2602.11964-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.11964) [![数据](https://img.shields.io/badge/data-Hugging%20Face-ffd21e?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/meta-agents-research-environments/gaia2) | 💬 通信协作 | 邮件、消息、群聊、日历、通讯录、文件等 12 个 | 代码 MIT；数据 CC BY 4.0 |
| **ClawsBench**<br>BenchFlow · 2026-04<br>[![代码](https://img.shields.io/badge/stars-35-007ec6?logo=github&logoColor=white)](https://github.com/benchflow-ai/ClawsBench) [![论文](https://img.shields.io/badge/arXiv-2604.05172-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.05172) [![数据](https://img.shields.io/badge/data-Hugging%20Face-ffd21e?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/benchflow/ClawsBench) | 💬 通信协作 | Gmail、Slack、日历、文档、网盘 | CC BY-NC-SA 4.0；公开轨迹，服务端代码未公开 |
| **EmailBench**<br>Microsoft · 2026-09<br>[![论文](https://img.shields.io/badge/arXiv-2609.31906-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.31906) | 💬 通信协作 | 邮件、日历、联系人、待办、文件夹、过滤规则 | 尚未公开；作者表示计划发布 |
| **MCP-Persona**<br>2026-06<br>[![代码](https://img.shields.io/badge/stars-9-007ec6?logo=github&logoColor=white)](https://github.com/wwh0411/MCP-Persona) [![论文](https://img.shields.io/badge/arXiv-2606.02470-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.02470) | 💬 通信协作 | **飞书**、Slack、企业微信、Gmail、163 邮箱、Notion 等 12 个 | 未发现许可文件；使用授权需向作者确认 |
| **WorkBench**<br>2024-05<br>[![代码](https://img.shields.io/badge/stars-77-007ec6?logo=github&logoColor=white)](https://github.com/olly-styles/WorkBench) [![论文](https://img.shields.io/badge/arXiv-2405.00823-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.00823) | 💬 通信协作 | 邮件、日历、CRM 等 5 个库 | MIT |
| **AgentDojo**<br>ETH Zurich · 2024-06<br>[![代码](https://img.shields.io/badge/stars-898-007ec6?logo=github&logoColor=white)](https://github.com/ethz-spylab/agentdojo) [![论文](https://img.shields.io/badge/arXiv-2406.13352-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2406.13352) | 💬 通信协作 | 邮件、网银、订票等 | MIT |
| **OfficeBench**<br>2024-07<br>[![代码](https://img.shields.io/badge/stars-47-007ec6?logo=github&logoColor=white)](https://github.com/zlwang-cs/OfficeBench) [![论文](https://img.shields.io/badge/arXiv-2407.19056-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2407.19056) | 💬 通信协作 | 文档、表格、邮件等办公应用 | Apache-2.0 |
| **TheAgentCompany**<br>CMU · 2024-12<br>[![代码](https://img.shields.io/badge/stars-792-007ec6?logo=github&logoColor=white)](https://github.com/TheAgentCompany/TheAgentCompany) [![论文](https://img.shields.io/badge/arXiv-2412.14161-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2412.14161) | 🏢 企业软件 | 即时通讯、代码托管、网盘、项目管理 | MIT；磁盘需求超过 30 GB |
| **SaaS-Bench**<br>UniPat AI · 2026-05<br>[![代码](https://img.shields.io/badge/stars-102-007ec6?logo=github&logoColor=white)](https://github.com/UniPat-AI/SaaS-Bench) [![论文](https://img.shields.io/badge/arXiv-2605.15777-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.15777) | 🏢 企业软件 | 即时通讯、邮箱、文档、CRM、ERP、HR 等 23 个系统 | 代码 Apache-2.0；任务数据另有许可；约 120 GB 磁盘 |
| **Toolathlon**<br>HKUST · 2025-10<br>[![代码](https://img.shields.io/badge/stars-491-007ec6?logo=github&logoColor=white)](https://github.com/hkust-nlp/Toolathlon) [![论文](https://img.shields.io/badge/arXiv-2510.25726-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.25726) | 🏢 企业软件 | 邮件、日历、Notion、电商、k8s 等 32 个 | 未发现许可文件；使用授权需向作者确认 |
| **EnterpriseBench**<br>Fujitsu Research · 2025-10<br>[![代码](https://img.shields.io/badge/stars-13-007ec6?logo=github&logoColor=white)](https://github.com/ast-fri/EnterpriseBench) [![论文](https://img.shields.io/badge/arXiv-2510.27287-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.27287) [![数据](https://img.shields.io/badge/data-Hugging%20Face-ffd21e?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/AST-FRI/EnterpriseBench) | 🏢 企业软件 | 聊天、邮件、代码、CRM、HR、IT 工单 | MIT |
| **EnterpriseLab**<br>Fujitsu Research · 2026-03<br>[![代码](https://img.shields.io/badge/stars-3-007ec6?logo=github&logoColor=white)](https://github.com/ast-fri/EnterpriseLab) [![论文](https://img.shields.io/badge/arXiv-2603.21630-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.21630) | 🏢 企业软件 | 聊天、邮件、日历、代码、网盘、HR、ERP、工单 | 未发现许可文件；部署完整性尚未验证 |
| **DRBench**<br>ServiceNow · 2025-09<br>[![代码](https://img.shields.io/badge/stars-44-007ec6?logo=github&logoColor=white)](https://github.com/ServiceNow/drbench) [![论文](https://img.shields.io/badge/arXiv-2510.00172-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.00172) [![数据](https://img.shields.io/badge/data-Hugging%20Face-ffd21e?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/ServiceNow/drbench) | 🏢 企业软件 | 聊天、文档、邮件、网盘、公开网页 | Apache-2.0 |
| **Corecraft**<br>Surge AI · 2026-02<br>[![论文](https://img.shields.io/badge/arXiv-2602.16179-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.16179) | 🏢 企业软件 | 客服组织：订单、工单、知识库等 | 商业环境；未公开发布 |
| **τ²-Bench**<br>Sierra<br>[![代码](https://img.shields.io/badge/stars-2.2k-007ec6?logo=github&logoColor=white)](https://github.com/sierra-research/tau2-bench) | 🏢 企业软件 | 客服对话加工具调用 | MIT；多篇训练论文用它做外部评测 |
| **AppWorld**<br>Stony Brook · 2024-07<br>[![代码](https://img.shields.io/badge/stars-529-007ec6?logo=github&logoColor=white)](https://github.com/StonyBrookNLP/appworld) [![论文](https://img.shields.io/badge/arXiv-2407.18901-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2407.18901) | 🖥️ 个人与桌面 | 购物、音乐、支付、笔记、消息等 9 个 | Apache-2.0；提供 MCP 服务端与数据生成指南 |
| **MyPCBench**<br>CMU · 2026-06<br>[![代码](https://img.shields.io/badge/stars-9-007ec6?logo=github&logoColor=white)](https://github.com/ljang0/MyPCBench) [![论文](https://img.shields.io/badge/arXiv-2606.16748-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.16748) [![数据](https://img.shields.io/badge/data-Hugging%20Face-ffd21e?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/ljang0/mypcbench-qemu-baseline) | 🖥️ 个人与桌面 | 邮件、聊天、日历、银行、购物、打车等 17 个网站加桌面 | MIT；数据修改能力尚未验证 |
| **Workspace-Bench**<br>2026-05<br>[![代码](https://img.shields.io/badge/stars-78-007ec6?logo=github&logoColor=white)](https://github.com/OpenDataBox/Workspace-Bench) [![论文](https://img.shields.io/badge/arXiv-2605.03596-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.03596) [![数据](https://img.shields.io/badge/data-Hugging%20Face-ffd21e?logo=huggingface&logoColor=white)](https://huggingface.co/Workspace-Bench) | 🖥️ 个人与桌面 | 文件系统，含邮件和会议纪要文件 | MIT；提供中文版本 |
| **EnterpriseClawBench**<br>FrontisAI · 2026-06<br>[![代码](https://img.shields.io/badge/stars-49-007ec6?logo=github&logoColor=white)](https://github.com/FrontisAI/EnterpriseClawBench) [![论文](https://img.shields.io/badge/arXiv-2606.23654-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.23654) | 🔁 真实会话 | 企业协作平台里的 Agent 任务，产出文档、表格、网页等 | 未发现许可文件；公开构造管线与一条脱敏样例，完整数据未公开 |
| **DuMateBench**<br>2026-08<br>[![官网](https://img.shields.io/badge/website-dumatebench.com-0a7ea4)](https://dumatebench.com/) [![论文](https://img.shields.io/badge/arXiv-2608.26546-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2608.26546) | 🔁 真实会话 | 文档、表格、演示、检索、编程 | 数据已发布；许可参见官网 |
<!-- END:environments -->

<details>
<summary>🔬 技术细节：规模、数据来源、评测方式与状态后端</summary>

报告分数对应原始资料中的实验设置，仅用于了解各项目的评测背景，不构成跨评测排名。

<!-- BEGIN:environment_details -->
| 资源 | 规模与数据来源 | 评测方式与报告结果 | 状态后端 |
|---|---|---|---|
| **Gaia2 / ARE** | 101 个工具，1,120 个场景<br>全合成，按人设生成 | 只核对写操作：编号精确比对，文字按评分标准判<br>42% | Python 内存对象 |
| **ClawsBench** | 198 个接口，44 个任务<br>接口行为用真实账号校准；种子数据来源未说明 | 比对数据库快照<br>53–63%，不安全操作 7–23% | SQLite（据论文） |
| **EmailBench** | 46 个工具，206 个场景<br>从 Enron 取主题和组织关系，正文重写 | 可执行断言加评分标准<br>33.5% | 内存 mock |
| **MCP-Persona** | 140 个工具，173 个任务<br>在真实服务上用测试账号录调用，再生成仿真器 | LLM 判检查点，增删改用执行器核实<br>38.66 分（满分 100） | Python 仿真工具加上下文 |
| **WorkBench** | 26 个工具，690 个任务<br>合成，按模板生成 | 比对结果状态<br>43%（GPT-4，2024 年） | CSV |
| **AgentDojo** | 97 个任务，629 个注入攻击用例<br>合成 | 程序判分 | YAML 加内存 |
| **OfficeBench** | — | — | — |
| **TheAgentCompany** | 175 个任务<br>合成企业数据与模拟同事 | 检查点加执行结果<br>24–30% | Docker 中的真实应用 |
| **SaaS-Bench** | 106 个任务<br>LLM 生成任务，经专家修订 | 加权检查点，直接读应用的数据库<br>完全解决 31.1% | Docker 中的真实 SaaS |
| **Toolathlon** | 604 个工具，108 个任务 | 执行结果验证 | 容器中的真实应用 |
| **EnterpriseBench** | 500 个任务<br>合成的企业数据 | 41.8% | JSON 文件 |
| **EnterpriseLab** | 15 个服务，140 多个工具<br>仿真数据，9 位专家核对 | 执行结果加 LLM 评审<br>0.45（GPT-4o） | 真实软件加 MCP 服务 |
| **DRBench** | 100 个任务<br>合成管线加人工核对 | 洞察召回率、事实准确性与报告连贯性 | Docker 服务 |
| **Corecraft** | 2,500 多个实体，23 个工具，1,150 个任务<br>合成，专家搭建 | LLM 按专家评分标准判，奖励是满足比例<br>约 30% | JSON 加 MCP |
| **τ²-Bench** | — | — | — |
| **AppWorld** | 457 个接口，750 个任务<br>全合成，约 100 个虚构用户 | 检查数据库状态 | SQLite，每应用一库 |
| **MyPCBench** | 184 个任务<br>合成，全部按一个人设生成并互相关联 | 评分标准<br>55.4% | 整机镜像 |
| **Workspace-Bench** | 388 个任务，20,476 个文件<br>任务场景来自字节内部**飞书**的 154 个真实工作流；文件是公开材料加合成 | Agent 评审逐条判 7,399 条评分标准<br>约 60%，人是 80.7% | 文件系统 |
| **EnterpriseClawBench** | 852 个任务，从 5,291 个里筛出<br>**真实会话**，内部实体、链接、编号、金额全部打码 | 硬规则加文本和视觉评审<br>0.663（满分 1） | 文件加沙盒 |
| **DuMateBench** | 200 个任务<br>**真实会话**，去掉个人信息和凭证后人工逐条复查 | 检查项占三成，LLM 评审占七成 | Docker 加工作区文件 |
<!-- END:environment_details -->

</details>

选型时需关注状态重置、并发运行与动作验证。数据库、内存对象、容器应用与整机镜像各有工程取舍，实际部署要求应结合已发布代码确认。

## <a id="training"></a>⚙️ 环境生成与 Agent 训练

覆盖环境生成、LLM 环境模拟、轨迹合成、经验提炼、训练框架、基础设施及公开训练实验。

<!-- BEGIN:training -->
| 资源 | 类别 | 方法 | 开放情况与许可 |
|---|---|---|---|
| **Corecraft**<br>Surge AI · 2026-02<br>[![论文](https://img.shields.io/badge/arXiv-2602.16179-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.16179) | 📈 训练实证 | 在高保真企业环境中进行 RL 训练 | 未开放<br>未公开 |
| **EnterpriseLab**<br>Fujitsu Research · 2026-03<br>[![代码](https://img.shields.io/badge/stars-3-007ec6?logo=github&logoColor=white)](https://github.com/ast-fri/EnterpriseLab) [![论文](https://img.shields.io/badge/arXiv-2603.21630-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.21630) | 🧩 环境加训练 | 依据工具依赖关系合成轨迹，用于后续训练 | 环境、任务生成管线、四种训练方法的代码<br>未发现许可文件 |
| **ART（含邮件 Agent 示例）**<br>OpenPipe · 2025-04<br>[![代码](https://img.shields.io/badge/stars-11k-007ec6?logo=github&logoColor=white)](https://github.com/OpenPipe/ART) [![数据](https://img.shields.io/badge/data-Hugging%20Face-ffd21e?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/corbt/enron-emails) | 🧰 训练框架 | GRPO 训练库；邮件示例使用 Enron、SQLite 全文检索和三个工具，最多执行 10 步 | 框架、notebook、数据<br>Apache-2.0 |
| **Agent World Model**<br>Snowflake · 2026-02<br>[![代码](https://img.shields.io/badge/stars-465-007ec6?logo=github&logoColor=white)](https://github.com/Snowflake-Labs/agent-world-model) [![论文](https://img.shields.io/badge/arXiv-2602.10090-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.10090) [![数据](https://img.shields.io/badge/data-Hugging%20Face-ffd21e?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/Snowflake/AgentWorldModel-1K) | 🏗️ 环境生成 | 依次生成场景、数据库结构、种子数据、工具与验证器；使用 SQLite 管理状态，通过 MCP 提供接口 | 管线、1,000 个环境、三个训好的模型<br>代码未发现许可文件；数据 CC BY 4.0 |
| **EnvScaler**<br>人大 · 2026-01<br>[![代码](https://img.shields.io/badge/stars-199-007ec6?logo=github&logoColor=white)](https://github.com/RUC-NLPIR/EnvScaler) [![论文](https://img.shields.io/badge/arXiv-2601.05808-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.05808) | 🏗️ 环境生成 | 先生成环境骨架，再生成场景和校验函数 | 191 个环境、SFT 和 RL 数据、训练代码、模型<br>MIT |
| **AgentScaler**<br>阿里通义 · 2025-09<br>[![论文](https://img.shields.io/badge/arXiv-2509.13311-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.13311) | 🏗️ 环境生成 | 自动构造全仿真的函数调用环境 | — |
| **Simia**<br>Microsoft · 2025-11<br>[![代码](https://img.shields.io/badge/stars-68-007ec6?logo=github&logoColor=white)](https://github.com/microsoft/Simia-Agent-Training) [![论文](https://img.shields.io/badge/arXiv-2511.01824-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.01824) | 🤖 LLM 模拟环境 | 以推理模型模拟环境反馈 | 代码<br>MIT |
| **DreamGym**<br>2025-11<br>[![论文](https://img.shields.io/badge/arXiv-2511.03773-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.03773) | 🤖 LLM 模拟环境 | 用一个经验模型合成 rollout，并自动出更难的任务 | 未发现官方代码 |
| **APIGen-MT**<br>Salesforce · 2025-04<br>[![论文](https://img.shields.io/badge/arXiv-2504.03601-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.03601) | 🧵 轨迹合成 | 先生成带标准动作的任务蓝图，再用模拟的人机对话展开成轨迹 | — |
| **Synthetic Computers at Scale**<br>Microsoft · 2026-04<br>[![论文](https://img.shields.io/badge/arXiv-2604.28181-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.28181) [![数据](https://img.shields.io/badge/data-Hugging%20Face-ffd21e?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/microsoft/synthetic-computers-at-scale) | ⚗️ 经验提炼 | 造 1,000 台合成电脑，每台模拟跑 8 小时以上；把经验提炼成技能文档 | 100 台合成电脑<br>MIT（数据） |
| **Agent Lightning**<br>Microsoft · 2026-08<br>[![代码](https://img.shields.io/badge/stars-19k-007ec6?logo=github&logoColor=white)](https://github.com/microsoft/agent-lightning) [![论文](https://img.shields.io/badge/arXiv-2608.17528-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2608.17528) | 🧰 训练框架 | 让线上实际使用的 Agent 框架直接参与训练，训练器只看模型的请求和响应 | 框架和完整示例<br>MIT |
| **ToolBrain**<br>2025-09<br>[![代码](https://img.shields.io/badge/stars-205-007ec6?logo=github&logoColor=white)](https://github.com/ToolBrain/ToolBrain) [![论文](https://img.shields.io/badge/arXiv-2510.00023-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.00023) | 🧰 训练框架 | 工具调用的 RL 框架，含邮件搜索 Agent 示例 | 代码<br>未发现许可文件 |
| **OpenEnv**<br>Hugging Face<br>[![代码](https://img.shields.io/badge/stars-2.7k-007ec6?logo=github&logoColor=white)](https://github.com/huggingface/OpenEnv) | 🔧 基础设施 | RL 后训练用的环境接口库 | 代码<br>BSD-3-Clause |
| **verifiers**<br>Prime Intellect<br>[![代码](https://img.shields.io/badge/stars-4.7k-007ec6?logo=github&logoColor=white)](https://github.com/PrimeIntellect-ai/verifiers) | 🔧 基础设施 | RL 环境与评测库 | 代码<br>MIT |
| **Harbor**<br>[![代码](https://img.shields.io/badge/stars-5.9k-007ec6?logo=github&logoColor=white)](https://github.com/harbor-framework/harbor) | 🔧 基础设施 | 任务格式和运行框架，UniPat 的 Monthly-SWEBench 用这个格式 | 代码<br>Apache-2.0 |
<!-- END:training -->

<details>
<summary>📊 实验细节：训练配置与报告结果</summary>

结果与成本估计均来自原作者，并受具体实验设置影响。将经验提炼为技能文档的工作不一定更新模型权重。

<!-- BEGIN:training_details -->
| 资源 | 训练设置 | 报告结果 |
|---|---|---|
| **Corecraft** | GLM 4.6，GRPO，1,000 个任务，每个任务 16 条 rollout，1 个 epoch | 留出任务 25.37% → 36.76%；三个外部评测 +4.5、+7.4、+6.8 |
| **EnterpriseLab** | Qwen3-8B；SFT 不到 1,000 条约 2 小时；GRPO 用 4 张 H200 跑 24–30 小时 | 自家环境 0.31 → 0.43，GPT-4o 是 0.45 |
| **ART（含邮件 Agent 示例）** | Qwen 14B；每步 12 题各 4 条 rollout；1 张 H100 不到一天，约 80 美元 | 作者报告：邮件问答的准确率、延迟与成本优于 o3 |
| **Agent World Model** | 多轮工具调用的大规模 RL | 作者报告：仅在合成环境训练，在三个评测中实现分布外泛化 |
| **EnvScaler** | Qwen3 的 1.7B、4B、8B；SFT 加 RL | 三个评测上明显提升 |
| **AgentScaler** | 两阶段微调：先通用能力，再垂直场景 | τ-bench、τ²-Bench、ACEBench 上提升 |
| **Simia** | 开源模型，SFT 和 RL 两条管线 | τ²-Bench 上超过 GPT-4o，接近 o4-mini |
| **DreamGym** | 在线 RL | WebArena 上比基线高 30% 以上 |
| **APIGen-MT** | xLAM-2 系列，1B 到 70B，SFT | τ-bench 和 BFCL 上超过 GPT-4o 和 Claude 3.5 |
| **Synthetic Computers at Scale** | 不更新权重；900 台用来提炼 | 自家评测 61.6% → 68.6% |
| **Agent Lightning** | Qwen3.5-9B，6,000 条样本 | SWE-bench Verified 41.8% → 56.4% |
| **ToolBrain** | — | — |
| **OpenEnv** | — | — |
| **verifiers** | — | — |
| **Harbor** | — | — |
<!-- END:training_details -->

</details>

## <a id="datasets"></a>🗂️ 数据集与隐私

区分真实记录、合成语料与附有合成标注的真实记录。处理方式一栏概述原作者的方法，不代表对匿名化效果的认证。

<!-- BEGIN:datasets -->
| 资源 | 来源与规模 | 内容 | 处理方式与许可 |
|---|---|---|---|
| **Enron（OpenPipe 整理版）**<br>[![数据](https://img.shields.io/badge/data-Hugging%20Face-ffd21e?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/corbt/enron-emails) | 📬 真实<br>10 万到 100 万条 | 安然员工邮件 | 监管调查时经法律程序公开<br>数据页面未注明 |
| **EnronQA**<br>2025-05<br>[![论文](https://img.shields.io/badge/arXiv-2505.00263-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.00263) [![数据](https://img.shields.io/badge/data-Hugging%20Face-ffd21e?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/MichaelR207/enron_qa_0922) | 🔀 真实邮件，问答由 LLM 生成<br>103,638 封，528,304 个问答 | 清洗后的邮件加问答 | 采用已应当事人请求删除部分记录的 2015 版本；经去重、质量、色情内容与毒性过滤，517,401 → 103,638 封<br>CC BY 4.0（据论文） |
| **Avocado**<br>LDC · 2015<br>[![数据](https://img.shields.io/badge/data-catalog.ldc.upenn.edu-6e7781)](https://catalog.ldc.upenn.edu/LDC2015T03) | 📬 真实<br>279 个账号 | 一家已停止运营的 IT 公司的邮件、附件与日历 | 通过协议限定使用范围，限制再分发<br>需签 LDC 协议 |
| **EnterpriseRAG-Bench**<br>Onyx · 2026-05<br>[![代码](https://img.shields.io/badge/stars-581-007ec6?logo=github&logoColor=white)](https://github.com/onyx-dot-app/EnterpriseRAG-Bench) [![论文](https://img.shields.io/badge/arXiv-2605.05253-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.05253) [![数据](https://img.shields.io/badge/data-Hugging%20Face-ffd21e?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/onyx-dot-app/EnterpriseRAG-Bench) | 🧪 合成<br>约 50 万份文档，500 个问题 | Slack、Gmail、Jira、Confluence 等 9 种来源 | 围绕共享项目与人员生成，加入错置、近似重复和矛盾信息<br>MIT；生成框架开源 |
| **HERB**<br>Salesforce · 2025-06<br>[![代码](https://img.shields.io/badge/stars-3-007ec6?logo=github&logoColor=white)](https://github.com/SalesforceAIResearch/HERB) [![论文](https://img.shields.io/badge/arXiv-2506.23139-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.23139) [![数据](https://img.shields.io/badge/data-Hugging%20Face-ffd21e?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/Salesforce/HERB) | 🧪 合成<br>39,190 份 | 文档、会议纪要、Slack 消息、代码仓库 | 模拟产品规划到售后的流程，生成互相关联的内容<br>CC BY-NC 4.0，禁商用 |
| **OrgForge**<br>2026-03<br>[![代码](https://img.shields.io/badge/stars-20-007ec6?logo=github&logoColor=white)](https://github.com/tenurehq/orgforge) [![论文](https://img.shields.io/badge/arXiv-2603.14997-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.14997) [![数据](https://img.shields.io/badge/data-Hugging%20Face-ffd21e?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/aeriesec/orgforge) | 🧪 合成<br>1 万到 10 万条 | Slack、JIRA、Confluence、邮件、工单等 | 确定性程序维护事件与时间线，LLM 生成文本；使用 MongoDB 管理状态<br>MIT |
| **Era by Eon**<br>2026-09<br>[![论文](https://img.shields.io/badge/arXiv-2609.09853-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.09853) | 🧪 合成<br>23 家公司 | 一家虚构公司在 CRM、客服、聊天等系统里的全部数据 | 同一批实体投射到 66 个业务产品；用检测器找合成痕迹 |
| **WinSyn**<br>2026-09<br>[![论文](https://img.shields.io/badge/arXiv-2609.12171-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.12171) | 🧪 合成<br>最多 25 个员工互动 | 模拟数月项目的往来邮件 | 刻意制造信息分散和前后矛盾 |
| **Vectrix ART-E**<br>[![数据](https://img.shields.io/badge/data-Hugging%20Face-ffd21e?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/TonicAI/vectrix-art-e) | 🧪 合成<br>1 千到 1 万条 | 邮件语料，定位是 Enron 的替代品 | Apache-2.0 |
<!-- END:datasets -->

所收录工作中的数据构造主要有三种方式：

- **真实会话脱敏后重建任务：** EnterpriseClawBench、DuMateBench。
- **沿用工作流结构或主题，重写内容：** EmailBench、Workspace-Bench。
- **生成虚构组织与关联记录：** Gaia2 / ARE、OrgForge、Era by Eon。

隐私行为评测可参考 [PrivacyLens](https://github.com/SALT-NLP/PrivacyLens) 和 [AgentDAM](https://github.com/facebookresearch/ai-agent-privacy)。清洗流程、隐私限制与证据缺口的详细讨论见[综述正文](docs/survey.md)。

## <a id="providers"></a>🏭 数据与环境供给方

依据公开产品介绍与报道整理，用于了解产业生态。涉及公司自述与媒体报道的内容在条目中注明来源性质。

<!-- BEGIN:vendors -->
| 供给方 | 产品与服务 | 数据生产方式 | 公开资料 |
|---|---|---|---|
| **Copula Lab** | 专家制作的工作成果：研究报告与财务模型、并购尽调、前端应用、游戏及三维工程 | 付费专家网络，金融和法律专家兼职每月 2–3 万元；金融用上市公司公开披露，法律用封闭的模拟文档库 | 公开样例页面；生产数量与筛选淘汰率未披露<br>[官网](https://www.copulalab.com/) · [档案](docs/vendors/copula-lab.md) |
| **UniPat AI** | 评测加训练数据，十条线：编程、科研、医疗金融法律、视觉、预测等；据报道还卖 RL 后训练数据 | 真实代码仓库、预测市场、网络图片、论文；LLM 合成后专家审核；高风险领域专家直接写 | 公开生产流程、筛选统计与多数数据集<br>[博客](https://unipat.ai/blog) · [GitHub](https://github.com/UniPat-AI) · [档案](docs/vendors/unipat-ai.md) |
| **Surge AI** | EnterpriseBench 系列 RL 环境，第一个是 Corecraft | 自有团队搭环境，领域专家写任务和评分标准 | 论文与榜单公开；环境未发布<br>[博客](https://www.surgehq.ai/blog/enterprisebench-corecraft) · [论文](https://arxiv.org/abs/2602.16179) |
| **智能知识** | 专家网络（一面千识）、数据生产软件（Xpert Studio）、RL 任务数据（Terminal RL Data、MCP Data） | 公司自述：连接 5 万多名领域专家，通过 AI 面试筛选 | 有公开的产品介绍<br>[硅星人报道](https://finance.sina.cn/stock/jdts/2026-08-16/detail-ininnkfv8014751.d.html) |
| **Scale AI、Mercor、AfterQuery** | 据报道：Scale 近一半新训练项目涉及 RL 环境；Mercor 收购了环境搭建公司 Deeptune；AfterQuery 搭数字办公「世界」 | — | [硅星人报道](https://www.163.com/dy/article/L7JI5DP20511N33R.html) · [Techmeme 条目](https://www.techmeme.com/260416/p46) |
<!-- END:vendors -->

供给方背景与行业分析见[综述正文](docs/survey.md)，以及 [Copula Lab](docs/vendors/copula-lab.md)、[UniPat AI](docs/vendors/unipat-ai.md) 专题档案。

## <a id="related"></a>🔗 相关清单

本清单与通用 Agent、RL 资源清单互为补充，重点整理办公任务覆盖、数据来源、评测方法与开放条件。组织方式参考了 [AgentsMeetRL](https://github.com/thinkwee/AgentsMeetRL) 的结构化比较、[Awesome-Agent-Environments](https://github.com/ZackZikaiXiao/Awesome-Agent-Environments) 的分类体系，以及 [Awesome-Agentic-Environments](https://github.com/TraceLite-AI/Awesome-Agentic-Environments) 的环境元数据呈现。

<!-- BEGIN:related_lists -->
| 清单 | Star 数 | 收录重点 |
|---|---|---|
| [thinkwee/AgentsMeetRL](https://github.com/thinkwee/AgentsMeetRL) | [![Stars](https://img.shields.io/badge/stars-1.9k-007ec6?logo=github&logoColor=white)](https://github.com/thinkwee/AgentsMeetRL) | 用 RL 训练 Agent 的开源仓库，按任务分 16 类，记录每个项目用的框架、算法、奖励和环境 |
| [HHHHHejia/Awesome-AgenticLLM-RL-Papers](https://github.com/HHHHHejia/Awesome-AgenticLLM-RL-Papers) | [![Stars](https://img.shields.io/badge/stars-1.9k-007ec6?logo=github&logoColor=white)](https://github.com/HHHHHejia/Awesome-AgenticLLM-RL-Papers) | 一篇 Agentic RL 综述的配套论文列表，含环境和框架两节 |
| [ZackZikaiXiao/Awesome-Agent-Environments](https://github.com/ZackZikaiXiao/Awesome-Agent-Environments) | [![Stars](https://img.shields.io/badge/stars-19-007ec6?logo=github&logoColor=white)](https://github.com/ZackZikaiXiao/Awesome-Agent-Environments) | 按任务、构造与执行层组织 Agent 环境，涵盖企业工作流与个人助理 |
| [TraceLite-AI/Awesome-Agentic-Environments](https://github.com/TraceLite-AI/Awesome-Agentic-Environments) | [![Stars](https://img.shields.io/badge/stars-5-007ec6?logo=github&logoColor=white)](https://github.com/TraceLite-AI/Awesome-Agentic-Environments) | 环境可复现性、沙盒基础设施、供给方与行业资料 |
| [Amithuz/awesome-rl-environments](https://github.com/Amithuz/awesome-rl-environments) | [![Stars](https://img.shields.io/badge/stars-0-007ec6?logo=github&logoColor=white)](https://github.com/Amithuz/awesome-rl-environments) | RL 环境供给方清单 |
| [wasiahmad/Awesome-LLM-Synthetic-Data](https://github.com/wasiahmad/Awesome-LLM-Synthetic-Data) | [![Stars](https://img.shields.io/badge/stars-1.6k-007ec6?logo=github&logoColor=white)](https://github.com/wasiahmad/Awesome-LLM-Synthetic-Data) | 用 LLM 合成数据的阅读清单 |
| [trycua/acu](https://github.com/trycua/acu) | [![Stars](https://img.shields.io/badge/stars-1.8k-007ec6?logo=github&logoColor=white)](https://github.com/trycua/acu) | 电脑操作类 Agent 的论文、项目、框架 |
| [philschmid/ai-agent-benchmark-compendium](https://github.com/philschmid/ai-agent-benchmark-compendium) | [![Stars](https://img.shields.io/badge/stars-197-007ec6?logo=github&logoColor=white)](https://github.com/philschmid/ai-agent-benchmark-compendium) | 50 多个 Agent 评测，按工具调用、通用助理、编程等分类 |
<!-- END:related_lists -->

## <a id="repo-guide"></a>📁 仓库导航

| 路径 | 用途 |
|---|---|
| [README.md](README.md) | 本清单的英文版本 |
| [docs/survey.md](docs/survey.md) | 中文综述正文与参考文献 |
| [docs/vendors/](docs/vendors/) | 中文供给方研究档案 |
| [data/](data/) 与 [data/en/](data/en/) | 结构化原始记录与对应英文译文 |
| [data/papers.bib](data/papers.bib) | 论文参考文献库 |
| [scripts/build_readme.py](scripts/build_readme.py) | 同时生成两种语言的表格；`--check` 检查是否需要更新 |
| [scripts/verify.py](scripts/verify.py) | 核对仓库元数据与 arXiv 标识，并更新 Star 数快照 |
| [scripts/make_bib.py](scripts/make_bib.py) | 从 arXiv 更新参考文献元数据 |

## <a id="contribute"></a>🤝 参与贡献

欢迎纠错、补充资源与改进翻译。收录标准、来源要求和中英同步流程见[贡献指南](CONTRIBUTING.zh-CN.md)。

## <a id="license"></a>⚖️ 许可状态

本清单尚未选定许可。所引用项目与数据集各自适用其原有许可和条款。

---

由 [Gan Liu](https://ganliu.blog) 维护。
