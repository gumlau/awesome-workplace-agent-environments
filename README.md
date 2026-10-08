# Awesome Workplace Agent Environments

**English** | [简体中文](README.zh-CN.md)

> A curated collection of environments, benchmarks, training methods, and datasets for workplace agents.

Explore agents that work across email, messaging, calendars, documents, and enterprise applications. This collection brings together task coverage, data provenance, evaluation methods, state backends, and release terms to support environment selection and post-training research.

**Research snapshot: 2026-10-08.** The collection currently includes 20 environments, 15 generation and training resources, 9 datasets, and 5 provider entries. Some resources appear in more than one category.

[Quick start](#quick-start) · [Environments](#environments-and-benchmarks) · [Generation & training](#environment-generation-and-agent-training) · [Datasets](#datasets-and-privacy) · [Providers](#data-and-environment-providers) · [Related collections](#related-collections) · [Contributing](CONTRIBUTING.md)

## Scope and evidence

The focus is workplace communication and collaboration, together with environments and data relevant to agent post-training. Adjacent desktop and customer-service benchmarks are included when they offer useful construction or evaluation methods. A benchmark's inclusion does not imply that it is ready for reinforcement learning (RL).

Entries summarize linked papers, repositories, dataset cards, and provider materials. **Reported results come from the original authors and have not been reproduced here.** Metrics differ across benchmarks and are not directly comparable. `—` means unspecified or not verified. Repository and paper identifiers were checked in the original research; this collection does not certify runtime behavior or release completeness.

License notes describe the referenced artifacts; code, data, and models may have different terms. An absent license file does not establish reuse permission.

## Quick start

| Research need | Starting points | What to examine |
|---|---|---|
| Email, messaging, and calendar tasks | [Gaia2 / ARE](https://github.com/facebookresearch/meta-agents-research-environments), [WorkBench](https://github.com/olly-styles/WorkBench) | Application models, task definitions, outcome evaluation |
| Database-backed application simulation | [AppWorld](https://github.com/StonyBrookNLP/appworld) | State management and synthetic-data construction |
| Enterprise applications and workflows | [TheAgentCompany](https://github.com/TheAgentCompany/TheAgentCompany), [SaaS-Bench](https://github.com/UniPat-AI/SaaS-Bench) | Application deployment, checkpoints, infrastructure requirements |
| Feishu workflows and Chinese tasks | [MCP-Persona](https://github.com/wwh0411/MCP-Persona), [Workspace-Bench](https://github.com/OpenDataBox/Workspace-Bench) | Simulation interfaces and Chinese task coverage |
| Tasks reconstructed from real sessions | [EnterpriseClawBench](https://github.com/FrontisAI/EnterpriseClawBench), [DuMateBench](https://dumatebench.com/) | Sanitization, task selection, release boundaries |
| Environment generation and initial RL experiments | [Agent World Model](https://github.com/Snowflake-Labs/agent-world-model), [EnvScaler](https://github.com/RUC-NLPIR/EnvScaler), [ART](https://github.com/OpenPipe/ART) | Generation pipelines, verifiers, runnable training examples |

## Environments and benchmarks

Four categories organize the collection: communication, enterprise applications, personal/desktop tasks, and reconstruction from real sessions. The table below prioritizes task coverage and release status; implementation and evaluation details follow in a collapsible table.

<!-- BEGIN:environments -->
| Resource | Category | Applications / scope | Release / license |
|---|---|---|---|
| **Gaia2 / ARE**<br>Meta · 2026-02<br>[Code](https://github.com/facebookresearch/meta-agents-research-environments) · [Paper](https://arxiv.org/abs/2602.11964) · [Data](https://huggingface.co/datasets/meta-agents-research-environments/gaia2) | Communication | 12 apps: email, messaging, group chat, calendar, contacts, files, etc. | Code: MIT; data: CC BY 4.0 |
| **ClawsBench**<br>BenchFlow · 2026-04<br>[Code](https://github.com/benchflow-ai/ClawsBench) · [Paper](https://arxiv.org/abs/2604.05172) · [Data](https://huggingface.co/datasets/benchflow/ClawsBench) | Communication | Gmail, Slack, calendar, documents, cloud storage | CC BY-NC-SA 4.0; trajectories released, server code not released |
| **EmailBench**<br>Microsoft · 2026-09<br>[Paper](https://arxiv.org/abs/2609.31906) | Communication | Email, calendar, contacts, tasks, folders, filtering rules | Not released; publication planned by authors |
| **MCP-Persona**<br>2026-06<br>[Code](https://github.com/wwh0411/MCP-Persona) · [Paper](https://arxiv.org/abs/2606.02470) | Communication | 12 apps, including Feishu, Slack, WeCom, Gmail, 163 Mail, Notion | No license file identified; confirm permission with authors |
| **WorkBench**<br>2024-05<br>[Code](https://github.com/olly-styles/WorkBench) · [Paper](https://arxiv.org/abs/2405.00823) | Communication | 5 databases covering email, calendar, CRM, etc. | MIT |
| **AgentDojo**<br>ETH Zurich · 2024-06<br>[Code](https://github.com/ethz-spylab/agentdojo) · [Paper](https://arxiv.org/abs/2406.13352) | Communication | Email, banking, travel booking, etc. | MIT |
| **OfficeBench**<br>2024-07<br>[Code](https://github.com/zlwang-cs/OfficeBench) · [Paper](https://arxiv.org/abs/2407.19056) | Communication | Documents, spreadsheets, email, and other office apps | Apache-2.0 |
| **TheAgentCompany**<br>CMU · 2024-12<br>[Code](https://github.com/TheAgentCompany/TheAgentCompany) · [Paper](https://arxiv.org/abs/2412.14161) | Enterprise | Messaging, code hosting, cloud storage, project management | MIT; more than 30 GB disk space |
| **SaaS-Bench**<br>UniPat AI · 2026-05<br>[Code](https://github.com/UniPat-AI/SaaS-Bench) · [Paper](https://arxiv.org/abs/2605.15777) | Enterprise | 23 systems: messaging, email, documents, CRM, ERP, HR, etc. | Code: Apache-2.0; separate task-data terms; approx. 120 GB disk space |
| **Toolathlon**<br>HKUST · 2025-10<br>[Code](https://github.com/hkust-nlp/Toolathlon) · [Paper](https://arxiv.org/abs/2510.25726) | Enterprise | 32 apps: email, calendar, Notion, e-commerce, Kubernetes, etc. | No license file identified; confirm permission with authors |
| **EnterpriseBench**<br>Fujitsu Research · 2025-10<br>[Code](https://github.com/ast-fri/EnterpriseBench) · [Paper](https://arxiv.org/abs/2510.27287) · [Data](https://huggingface.co/datasets/AST-FRI/EnterpriseBench) | Enterprise | Messaging, email, code, CRM, HR, IT tickets | MIT |
| **EnterpriseLab**<br>Fujitsu Research · 2026-03<br>[Code](https://github.com/ast-fri/EnterpriseLab) · [Paper](https://arxiv.org/abs/2603.21630) | Enterprise | Messaging, email, calendar, code, storage, HR, ERP, tickets | No license file identified; deployment completeness not verified |
| **DRBench**<br>ServiceNow · 2025-09<br>[Code](https://github.com/ServiceNow/drbench) · [Paper](https://arxiv.org/abs/2510.00172) · [Data](https://huggingface.co/datasets/ServiceNow/drbench) | Enterprise | Messaging, documents, email, storage, public web pages | Apache-2.0 |
| **Corecraft**<br>Surge AI · 2026-02<br>[Paper](https://arxiv.org/abs/2602.16179) | Enterprise | Customer support: orders, tickets, knowledge base, etc. | Commercial environment; not publicly released |
| **τ²-Bench**<br>Sierra<br>[Code](https://github.com/sierra-research/tau2-bench) | Enterprise | Customer-service conversations and tool use | MIT; used for external evaluation in multiple training papers |
| **AppWorld**<br>Stony Brook · 2024-07<br>[Code](https://github.com/StonyBrookNLP/appworld) · [Paper](https://arxiv.org/abs/2407.18901) | Personal / desktop | 9 apps: shopping, music, payments, notes, messaging, etc. | Apache-2.0; MCP server and data-generation guide |
| **MyPCBench**<br>CMU · 2026-06<br>[Code](https://github.com/ljang0/MyPCBench) · [Paper](https://arxiv.org/abs/2606.16748) · [Data](https://huggingface.co/datasets/ljang0/mypcbench-qemu-baseline) | Personal / desktop | Desktop and 17 sites: email, chat, calendar, banking, shopping, rides, etc. | MIT; data-modification support not verified |
| **Workspace-Bench**<br>2026-05<br>[Code](https://github.com/OpenDataBox/Workspace-Bench) · [Paper](https://arxiv.org/abs/2605.03596) · [Data](https://huggingface.co/Workspace-Bench) | Personal / desktop | Filesystem with email and meeting-note files | MIT; Chinese version available |
| **EnterpriseClawBench**<br>FrontisAI · 2026-06<br>[Code](https://github.com/FrontisAI/EnterpriseClawBench) · [Paper](https://arxiv.org/abs/2606.23654) | Real-session reconstruction | Enterprise assistant tasks producing documents, spreadsheets, web pages, etc. | No license file identified; pipeline and one sanitized example released, full data withheld |
| **DuMateBench**<br>2026-08<br>[Website](https://dumatebench.com/) · [Paper](https://arxiv.org/abs/2608.26546) | Real-session reconstruction | Documents, spreadsheets, slides, retrieval, coding | Data released; see website for license |
<!-- END:environments -->

<details>
<summary>Technical details: scale, provenance, evaluation, and state backends</summary>

Reported scores refer to the source publication's evaluation setup. They are provided for context, not as a cross-benchmark ranking.

<!-- BEGIN:environment_details -->
| Resource | Scale / data source | Evaluation / reported result | State backend |
|---|---|---|---|
| **Gaia2 / ARE** | 101 tools; 1,120 scenarios<br>Fully synthetic, persona-based | Write actions only: exact ID matching and rubric-based text evaluation<br>42% | In-memory Python objects |
| **ClawsBench** | 198 APIs; 44 tasks<br>API behavior calibrated against real accounts; seed-data origin unspecified | Database snapshot comparison<br>53–63%; unsafe actions: 7–23% | SQLite (per paper) |
| **EmailBench** | 46 tools; 206 scenarios<br>Enron topics and organizational relationships; rewritten message bodies | Executable assertions and rubrics<br>33.5% | In-memory mocks |
| **MCP-Persona** | 140 tools; 173 tasks<br>Test-account API traces from real services used to generate simulators | LLM checkpoint evaluation; executor verifies mutations<br>38.66 / 100 | Python tool simulators and context |
| **WorkBench** | 26 tools; 690 tasks<br>Template-based synthetic data | Final-state comparison<br>43% (GPT-4, 2024) | CSV |
| **AgentDojo** | 97 tasks; 629 prompt-injection cases<br>Synthetic | Programmatic evaluation | YAML and memory |
| **OfficeBench** | — | — | — |
| **TheAgentCompany** | 175 tasks<br>Synthetic company data and simulated coworkers | Checkpoints and execution outcomes<br>24–30% | Real apps in Docker |
| **SaaS-Bench** | 106 tasks<br>LLM-generated tasks revised by experts | Weighted checkpoints evaluated against application databases<br>31.1% fully solved | Real SaaS apps in Docker |
| **Toolathlon** | 604 tools; 108 tasks | Execution-outcome verification | Real apps in containers |
| **EnterpriseBench** | 500 tasks<br>Synthetic enterprise data | 41.8% | JSON files |
| **EnterpriseLab** | 15 services; 140+ tools<br>Simulated data reviewed by 9 experts | Execution outcomes and LLM review<br>0.45 (GPT-4o) | Real apps and MCP services |
| **DRBench** | 100 tasks<br>Synthetic pipeline with human review | Insight recall, factual accuracy, report coherence | Docker services |
| **Corecraft** | 2,500+ entities; 23 tools; 1,150 tasks<br>Expert-built synthetic environment | LLM evaluates expert rubrics; reward is fraction satisfied<br>Approx. 30% | JSON and MCP |
| **τ²-Bench** | — | — | — |
| **AppWorld** | 457 APIs; 750 tasks<br>Fully synthetic; approx. 100 fictional users | Database-state checks | SQLite, one database per app |
| **MyPCBench** | 184 tasks<br>Synthetic, linked data for a shared persona | Rubrics<br>55.4% | Full VM image |
| **Workspace-Bench** | 388 tasks; 20,476 files<br>154 real internal Feishu workflows at ByteDance; public and synthetic files | Agent review of 7,399 rubric items<br>Approx. 60%; human: 80.7% | Filesystem |
| **EnterpriseClawBench** | 852 tasks selected from 5,291<br>Real sessions; internal entities, links, IDs, and amounts masked | Hard rules, text review, and visual review<br>0.663 / 1 | Files and sandbox |
| **DuMateBench** | 200 tasks<br>Real sessions; personal information and credentials removed, followed by manual review | 30% checklist; 70% LLM review | Docker and workspace files |
<!-- END:environment_details -->

</details>

When selecting an environment, inspect how it resets state, supports concurrent runs, and verifies actions. Database and in-memory backends offer different engineering tradeoffs from containerized applications or full VM images; deployment requirements should be checked against the actual release.

## Environment generation and agent training

Resources cover environment generation, LLM-based simulation, trajectory synthesis, experience distillation, training frameworks, infrastructure, and published training experiments.

<!-- BEGIN:training -->
| Resource | Category | Method | Release / license |
|---|---|---|---|
| **Corecraft**<br>Surge AI · 2026-02<br>[Paper](https://arxiv.org/abs/2602.16179) | Training evidence | RL in a high-fidelity enterprise environment | None<br>Not released |
| **EnterpriseLab**<br>Fujitsu Research · 2026-03<br>[Code](https://github.com/ast-fri/EnterpriseLab) · [Paper](https://arxiv.org/abs/2603.21630) | Environment + training | Generate trajectories from tool dependencies, then train | Environment, task-generation pipeline, code for four training methods<br>No license file identified |
| **ART (email-agent example)**<br>OpenPipe · 2025-04<br>[Code](https://github.com/OpenPipe/ART) · [Data](https://huggingface.co/datasets/corbt/enron-emails) | Training framework | GRPO library; email example uses Enron and SQLite full-text search, 3 tools, up to 10 steps | Framework, notebooks, data<br>Apache-2.0 |
| **Agent World Model**<br>Snowflake · 2026-02<br>[Code](https://github.com/Snowflake-Labs/agent-world-model) · [Paper](https://arxiv.org/abs/2602.10090) · [Data](https://huggingface.co/datasets/Snowflake/AgentWorldModel-1K) | Environment generation | Generate scenarios, schemas, seed data, tools, and verifiers; SQLite state and MCP interfaces | Pipeline, 1,000 environments, three trained models<br>Code: no license file identified; data: CC BY 4.0 |
| **EnvScaler**<br>Renmin University of China · 2026-01<br>[Code](https://github.com/RUC-NLPIR/EnvScaler) · [Paper](https://arxiv.org/abs/2601.05808) | Environment generation | Generate environment skeletons, then scenarios and verification functions | 191 environments, SFT/RL data, training code, models<br>MIT |
| **AgentScaler**<br>Alibaba Tongyi · 2025-09<br>[Paper](https://arxiv.org/abs/2509.13311) | Environment generation | Automatically construct simulated function-calling environments | — |
| **Simia**<br>Microsoft · 2025-11<br>[Code](https://github.com/microsoft/Simia-Agent-Training) · [Paper](https://arxiv.org/abs/2511.01824) | LLM simulation | Reasoning models simulate environment feedback | Code<br>MIT |
| **DreamGym**<br>2025-11<br>[Paper](https://arxiv.org/abs/2511.03773) | LLM simulation | Experience model synthesizes rollouts and generates harder tasks | Official code not identified |
| **APIGen-MT**<br>Salesforce · 2025-04<br>[Paper](https://arxiv.org/abs/2504.03601) | Trajectory synthesis | Generate task blueprints with reference actions, then expand into simulated dialogues | — |
| **Synthetic Computers at Scale**<br>Microsoft · 2026-04<br>[Paper](https://arxiv.org/abs/2604.28181) · [Data](https://huggingface.co/datasets/microsoft/synthetic-computers-at-scale) | Experience distillation | Build 1,000 synthetic computers, simulate 8+ h each, distill experience into skill documents | 100 synthetic computers<br>MIT (data) |
| **Agent Lightning**<br>Microsoft · 2026-08<br>[Code](https://github.com/microsoft/agent-lightning) · [Paper](https://arxiv.org/abs/2608.17528) | Training framework | Train agents within existing frameworks by observing model requests and responses | Framework and complete examples<br>MIT |
| **ToolBrain**<br>2025-09<br>[Code](https://github.com/ToolBrain/ToolBrain) · [Paper](https://arxiv.org/abs/2510.00023) | Training framework | RL for tool use; includes an email-search agent example | Code<br>No license file identified |
| **OpenEnv**<br>Hugging Face<br>[Code](https://github.com/huggingface/OpenEnv) | Infrastructure | Environment interface library for RL post-training | Code<br>BSD-3-Clause |
| **verifiers**<br>Prime Intellect<br>[Code](https://github.com/PrimeIntellect-ai/verifiers) | Infrastructure | Library for RL environments and evaluation | Code<br>MIT |
| **Harbor**<br>[Code](https://github.com/harbor-framework/harbor) | Infrastructure | Task format and execution framework; used by UniPat Monthly-SWEBench | Code<br>Apache-2.0 |
<!-- END:training -->

<details>
<summary>Experimental details: training configurations and reported results</summary>

Results and cost estimates are author-reported and specific to the listed setup. Experience distillation into skill documents does not necessarily update model weights.

<!-- BEGIN:training_details -->
| Resource | Training setup | Reported result |
|---|---|---|
| **Corecraft** | GLM 4.6; GRPO; 1,000 tasks; 16 rollouts per task; 1 epoch | Held-out tasks: 25.37% → 36.76%; three external benchmarks: +4.5, +7.4, +6.8 |
| **EnterpriseLab** | Qwen3-8B; SFT on <1,000 trajectories in approx. 2 h; GRPO on 4 H200s for 24–30 h | Internal score: 0.31 → 0.43; GPT-4o: 0.45 |
| **ART (email-agent example)** | Qwen 14B; 12 tasks × 4 rollouts per step; <1 day on 1 H100; reported cost approx. $80 | Authors report higher accuracy, lower latency, and lower cost than o3 on email QA |
| **Agent World Model** | Large-scale RL with multi-turn tool use | Authors report out-of-distribution generalization on three benchmarks after synthetic-only training |
| **EnvScaler** | Qwen3 1.7B / 4B / 8B; SFT and RL | Authors report improvements on three benchmarks |
| **AgentScaler** | Two-stage fine-tuning: general skills, then domain tasks | Improvements on τ-bench, τ²-Bench, ACEBench |
| **Simia** | Open models; SFT and RL pipelines | Above GPT-4o and near o4-mini on τ²-Bench |
| **DreamGym** | Online RL | Reported improvement of more than 30% over baseline on WebArena |
| **APIGen-MT** | xLAM-2, 1B–70B; SFT | Above GPT-4o and Claude 3.5 on τ-bench and BFCL |
| **Synthetic Computers at Scale** | No weight updates; 900 computers used for distillation | Internal benchmark: 61.6% → 68.6% |
| **Agent Lightning** | Qwen3.5-9B; 6,000 examples | SWE-bench Verified: 41.8% → 56.4% |
| **ToolBrain** | — | — |
| **OpenEnv** | — | — |
| **verifiers** | — | — |
| **Harbor** | — | — |
<!-- END:training_details -->

</details>

## Datasets and privacy

The collection distinguishes real records, synthetic corpora, and real records paired with synthetic annotations. Processing notes summarize reported methods rather than certify anonymization.

<!-- BEGIN:datasets -->
| Resource | Source / scale | Content | Processing / license |
|---|---|---|---|
| **Enron (OpenPipe version)**<br>[Data](https://huggingface.co/datasets/corbt/enron-emails) | Real<br>100,000–1,000,000 records | Enron employee email | Disclosed through legal proceedings during a regulatory investigation<br>Not specified on dataset page |
| **EnronQA**<br>2025-05<br>[Paper](https://arxiv.org/abs/2505.00263) · [Data](https://huggingface.co/datasets/MichaelR207/enron_qa_0922) | Real email / synthetic QA<br>103,638 emails; 528,304 QA pairs | Cleaned emails and generated QA pairs | 2015 version with requested removals; deduplication, quality, sexual-content, and toxicity filters: 517,401 → 103,638 emails<br>CC BY 4.0 (per paper) |
| **Avocado**<br>LDC · 2015<br>[Data](https://catalog.ldc.upenn.edu/LDC2015T03) | Real<br>279 accounts | Email, attachments, and calendars from a defunct IT company | Access governed by an agreement; redistribution restricted<br>LDC agreement required |
| **EnterpriseRAG-Bench**<br>Onyx · 2026-05<br>[Code](https://github.com/onyx-dot-app/EnterpriseRAG-Bench) · [Paper](https://arxiv.org/abs/2605.05253) · [Data](https://huggingface.co/datasets/onyx-dot-app/EnterpriseRAG-Bench) | Synthetic<br>Approx. 500,000 documents; 500 questions | 9 sources including Slack, Gmail, Jira, Confluence | Shared projects and people, with misplaced files, near-duplicates, and contradictions<br>MIT; generation framework released |
| **HERB**<br>Salesforce · 2025-06<br>[Code](https://github.com/SalesforceAIResearch/HERB) · [Paper](https://arxiv.org/abs/2506.23139) · [Data](https://huggingface.co/datasets/Salesforce/HERB) | Synthetic<br>39,190 items | Documents, meeting notes, Slack messages, code repositories | Linked content simulating workflows from product planning to after-sales support<br>CC BY-NC 4.0; noncommercial |
| **OrgForge**<br>2026-03<br>[Code](https://github.com/tenurehq/orgforge) · [Paper](https://arxiv.org/abs/2603.14997) · [Data](https://huggingface.co/datasets/aeriesec/orgforge) | Synthetic<br>10,000–100,000 records | Slack, Jira, Confluence, email, tickets, etc. | Deterministic event/timeline logic; LLMs generate surface text; MongoDB state<br>MIT |
| **Era by Eon**<br>2026-09<br>[Paper](https://arxiv.org/abs/2609.09853) | Synthetic<br>23 companies | Company-wide CRM, support, messaging, and other business data | Shared entities projected into 66 business products; detectors assess synthetic artifacts |
| **WinSyn**<br>2026-09<br>[Paper](https://arxiv.org/abs/2609.12171) | Synthetic<br>Up to 25 interacting employees | Project email spanning several months | Deliberate information fragmentation and contradictions |
| **Vectrix ART-E**<br>[Data](https://huggingface.co/datasets/TonicAI/vectrix-art-e) | Synthetic<br>1,000–10,000 records | Email corpus positioned as an Enron alternative | Apache-2.0 |
<!-- END:datasets -->

Three data-construction approaches appear in the collected work:

- **Sanitize real sessions and reconstruct tasks:** EnterpriseClawBench and DuMateBench.
- **Reuse workflow structure or topics with rewritten content:** EmailBench and Workspace-Bench.
- **Generate fictional organizations and linked records:** Gaia2 / ARE, OrgForge, and Era by Eon.

For privacy-focused evaluation, see [PrivacyLens](https://github.com/SALT-NLP/PrivacyLens) and [AgentDAM](https://github.com/facebookresearch/ai-agent-privacy). The [survey (Chinese)](docs/survey.md) discusses filtering pipelines, privacy limitations, and evidence gaps in more detail.

## Data and environment providers

These entries summarize public product descriptions and reporting. They are included for ecosystem context, with company statements and media claims attributed where applicable.

<!-- BEGIN:vendors -->
| Provider | Offering | Data production | Public information |
|---|---|---|---|
| **Copula Lab** | Expert-produced deliverables: research reports, financial models, M&A diligence, frontend apps, games, 3D projects | Paid expert network; reported part-time finance/legal compensation: RMB 20,000–30,000 per month; public financial disclosures and simulated legal document collections | Sample pages available; production volume and rejection rates not disclosed<br>[Website](https://www.copulalab.com/) · [Profile (Chinese)](docs/vendors/copula-lab.md) |
| **UniPat AI** | Evaluation and training data across ten areas including coding, science, medicine, finance, law, vision, and forecasting; RL data reported by media | Real repositories, prediction markets, images, papers; LLM synthesis with expert review; expert-authored high-stakes tasks | Processes, filtering statistics, and many datasets published<br>[Blog](https://unipat.ai/blog) · [GitHub](https://github.com/UniPat-AI) · [Profile (Chinese)](docs/vendors/unipat-ai.md) |
| **Surge AI** | EnterpriseBench RL environments, starting with Corecraft | Internal environment engineering; domain experts write tasks and rubrics | Paper and leaderboard public; environment not released<br>[Blog](https://www.surgehq.ai/blog/enterprisebench-corecraft) · [Paper](https://arxiv.org/abs/2602.16179) |
| **智能知识 (Chinese brand name)** | Expert network, Xpert Studio production software, Terminal RL Data and MCP Data | Company reports a network of 50,000+ experts screened through AI interviews | Public product descriptions<br>[Media report (Chinese)](https://finance.sina.cn/stock/jdts/2026-08-16/detail-ininnkfv8014751.d.html) |
| **Scale AI, Mercor, AfterQuery** | Media reports: RL environments in nearly half of Scale's new training projects; Mercor acquisition of Deeptune; digital workplace worlds from AfterQuery | — | [Media report (Chinese)](https://www.163.com/dy/article/L7JI5DP20511N33R.html) · [Techmeme](https://www.techmeme.com/260416/p46) |
<!-- END:vendors -->

Provider profiles and industry analysis are available in the [survey (Chinese)](docs/survey.md) and the [Copula Lab](docs/vendors/copula-lab.md) / [UniPat AI](docs/vendors/unipat-ai.md) profiles (Chinese).

## Related collections

This collection complements broader agent and RL lists by focusing on workplace task coverage, data provenance, evaluation, and release conditions. Its presentation draws on the structured comparisons in [AgentsMeetRL](https://github.com/thinkwee/AgentsMeetRL), the taxonomy in [Awesome-Agent-Environments](https://github.com/ZackZikaiXiao/Awesome-Agent-Environments), and the environment metadata in [Awesome-Agentic-Environments](https://github.com/TraceLite-AI/Awesome-Agentic-Environments).

<!-- BEGIN:related_lists -->
| Collection | Focus |
|---|---|
| [thinkwee/AgentsMeetRL](https://github.com/thinkwee/AgentsMeetRL) | Open-source agentic RL projects with framework, algorithm, reward, and environment details |
| [HHHHHejia/Awesome-AgenticLLM-RL-Papers](https://github.com/HHHHHejia/Awesome-AgenticLLM-RL-Papers) | Companion reading list for an agentic RL survey, including environments and frameworks |
| [ZackZikaiXiao/Awesome-Agent-Environments](https://github.com/ZackZikaiXiao/Awesome-Agent-Environments) | Agent environments organized by task, construction, and execution layers |
| [TraceLite-AI/Awesome-Agentic-Environments](https://github.com/TraceLite-AI/Awesome-Agentic-Environments) | Environment reproducibility, sandbox infrastructure, vendors, and industry reports |
| [Amithuz/awesome-rl-environments](https://github.com/Amithuz/awesome-rl-environments) | Companies building RL environments |
| [wasiahmad/Awesome-LLM-Synthetic-Data](https://github.com/wasiahmad/Awesome-LLM-Synthetic-Data) | Reading list on LLM-generated synthetic data |
| [trycua/acu](https://github.com/trycua/acu) | Computer-use agent papers, projects, and frameworks |
| [philschmid/ai-agent-benchmark-compendium](https://github.com/philschmid/ai-agent-benchmark-compendium) | Agent benchmarks grouped by tools, general assistance, coding, and other tasks |
<!-- END:related_lists -->

## Repository guide

| Path | Purpose |
|---|---|
| [README.zh-CN.md](README.zh-CN.md) | Chinese version of this resource collection |
| [docs/survey.md](docs/survey.md) | Detailed survey and references (Chinese) |
| [docs/vendors/](docs/vendors/) | Provider research profiles (Chinese) |
| [data/](data/) and [data/en/](data/en/) | Structured source records and aligned English translations |
| [data/papers.bib](data/papers.bib) | Paper bibliography |
| [scripts/build_readme.py](scripts/build_readme.py) | Generate both README versions; use `--check` to detect stale tables |
| [scripts/verify.py](scripts/verify.py) | Check repository metadata and arXiv identifiers |
| [scripts/make_bib.py](scripts/make_bib.py) | Refresh bibliography metadata from arXiv |

## Contributing

Corrections, new resources, and translation improvements are welcome. See the [contribution guide](CONTRIBUTING.md) for inclusion criteria, source requirements, and the bilingual update workflow.

## License status

A license for this collection has not yet been selected. Referenced projects and datasets retain their own licenses and terms.

---

Maintained by [Gan Liu](https://ganliu.blog).
