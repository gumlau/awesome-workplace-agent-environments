# 面向办公场景的 Agent 后训练：数据供给、仿真环境与隐私处理综述

调研与核实日期：2026-10-08
说明：本文由 AI（Claude）辅助检索、阅读和撰写。方括号数字对应文末参考文献。

---

## 摘要

大模型的后训练数据正在从静态问答和单轮标注，转向可交互、可验证的工作环境。本文围绕办公场景（查邮件、查即时通讯、给人写信、处理文档）梳理三个问题：谁在供给这类数据，供给的是什么；办公环境怎么搭，在里面训练是否有效；带隐私的真实办公数据怎样变成可以交付的东西。

材料包括两家中国供给方（Copula Lab、UniPat AI）的公开资料，约 50 篇经 arXiv API 核对的论文，以及 23 个经 GitHub 和 Hugging Face API 核实的开源仓库。

主要发现有五条。第一，供给方卖的是环境、任务和验证器，不是语料。第二，邮件、消息、日历类的仿真办公环境在 2026 年集中出现，已有十几个公开实现，其中两个涉及飞书。第三，在这类环境里做强化学习有公开的正面结果，但所有结果都来自合成环境，真实数据是否更好没有对照实验。第四，处理真实办公数据的主流做法是只拿它当种子，正文重新合成；直接脱敏后公开的只有一例。第五，公开的、真实的、带即时通讯的中文办公数据集目前不存在。

---

## 术语

| 术语 | 含义 |
|---|---|
| 后训练 | 预训练之后的所有训练，包括下面两种 |
| SFT | 监督微调，给模型看示范轨迹 |
| RL | 强化学习，让模型自己试，按结果打分来更新 |
| GRPO | 一种常用的 RL 算法，同一个任务跑多条轨迹，按组内相对好坏更新 |
| rollout | 模型在环境里从头到尾跑完一次任务的完整记录 |
| 环境 | 一套可以调用、有状态、能重置的应用，加上任务和判分 |
| 验证器 | 判断任务有没有做对的程序，产出 RL 需要的奖励 |
| Rubric | 逐条列出的评分标准 |
| MCP | 一种把应用功能暴露成模型可调用工具的通用协议 |

---

## 1 引言

### 1.1 背景

前沿模型的落地正从写代码扩展到高门槛的专业工作，后训练所需的数据也随之变化：从静态问答、偏好标注、单轮任务，转向可交互、可验证的专家工作流环境 [5]。几个信号可以佐证：

- Scale AI 在 2026 年 2 月称，接近一半的新训练项目涉及强化学习环境 [18]。
- Mercor 在 2026 年 7 月收购 Deeptune，把专家网络和搭建训练环境的能力合到一起 [18]。
- Forbes 在 2026 年 4 月报道，AI 实验室通过中间商购买倒闭公司的 Slack、Jira 和邮件存档，用来搭「强化学习训练场」[23]。
- Epoch AI 在 2026 年 1 月访谈了 18 位从业者，给出的价格是：单个任务多在 200 到 2,000 美元，Slack 这类复杂产品的高保真仿真约 30 万美元，合同每季度六到七位数美元，独家约是非独家的 4 到 5 倍 [68]。

中国市场起步更晚。硅星人的判断是，专家数据、评测、RL 环境、自动验证之间还没有稳定分工，模型公司倾向于把核心后训练留在内部，把专家组织、任务生产和部分环境搭建外包 [17]。

### 1.2 本文回答的问题

- **问题一**：供给方聚焦哪些数据，怎么获取，怎么清洗？（第 3 节）
- **问题二**：办公通信类环境有哪些，怎么搭，在里面训练有没有用？（第 4、5 节）
- **问题三**：带隐私的真实办公数据怎样处理成可交付物？有哪些同类数据集？（第 6、8 节）

第 7 节盘点开源代码和数据，第 9 节讨论共识、分歧和空白，第 10 节给出面向实践的建议。

### 1.3 方法

- **公司资料**：读官网全部页面、技术博客、论文、数据集卡和招聘页，辅以媒体报道。
- **论文**：英文和中文关键词检索，每篇用 arXiv API 核对编号、标题、作者。重点论文读正文，其余读摘要。
- **开源仓库**：用 GitHub API 取星数、许可、最近更新，读 README 和目录结构；用 Hugging Face API 取数据集许可和下载量。没有实际运行任何仓库。
- **证据分三种口径**，正文会标明：公司或作者的**自述**；媒体的**报道**（多为匿名信源）；笔者的**推断**。

---

## 2 分类框架

### 2.1 四种数据形态

| 形态 | 交付的是什么 | 判分依据 | 代表 |
|---|---|---|---|
| 专家交付物 | 一个完整工作包，加人做出来的参考成果和评分标准 | Rubric | Copula 的金融和法律任务 [2]、ExpertEval [12]、UniScientist [8] |
| 可执行验证任务 | 代码仓库快照、指令、测试 | 测试是否通过 | Monthly-SWEBench [11]、Terminal-X [10] |
| 交互式仿真环境 | 应用、状态、工具、任务、验证器 | 状态比对或操作核对 | Gaia2 [25]、AppWorld [31]、ClawsBench [30]、Corecraft [40] |
| 真实会话重建 | 脱敏后的历史上下文、文件和任务 | 硬规则加语义 Rubric | EnterpriseClawBench [38]、DuMateBench [39] |

前两种的重点是任务和判分，后两种还要求有一个能反复运行的「世界」。本文的重心在后两种。

### 2.2 一个可训练环境的七个部件

| 部件 | 作用 | 参考实现 |
|---|---|---|
| 状态后端 | 存邮件、消息、日历的真实状态 | SQLite 或其他数据库 [30][42][43] |
| 工具接口 | 模型调用的入口 | MCP 服务 [40][41]，或照抄真实接口的 REST [30] |
| 种子数据 | 让世界看起来有人在用 | 按人设生成 [25]，或从真实数据提取后重写 [27] |
| 任务 | 给模型的指令 | 专家写 [40]，或沿工具依赖关系自动合成 [41] |
| 验证器和奖励 | 判对错，产出训练信号 | 数据库快照比对 [30]，写操作核对 [25]，Rubric 满足比例 [40] |
| 重置和隔离 | 每条 rollout 互不干扰 | 每条 rollout 一个容器 [40][41]，快照恢复 [30] |
| 训练框架 | 把 rollout 变成参数更新 | ART [42]、Agent Lightning [46] |

### 2.3 三条数据来源路线

- **路线一**：真实数据脱敏后直接做任务。
- **路线二**：真实数据只提供结构和分布，内容重新合成。
- **路线三**：完全虚构。

第 6 节展开。

---

## 3 供给方：两家中国公司的做法

### 3.1 概况

| | Copula Lab | UniPat AI |
|---|---|---|
| 成立 | 2026 年上半年，上海 [18][66] | 2025 年底，北京 [21][22] |
| 创始人 | 梁丽（前 MiniMax Agent 业务负责人）、蔡佳人（前 MiniMax 开源负责人和后训练工程师）[5] | 李宽（前阿里通义实验室）、陈亮（联合创始人兼 CTO，前 Qwen 和 Moonshot 多模态）[18] |
| 自我定位 | 为前沿模型提供专家构建的评测、数据和环境 [1] | 官网只有一句口号，实际产出是评测、训练数据和实验模型 [6] |
| 公开产出 | 8 个数据产品的样例页，2 个在研评测，无公开数据集 [2][3] | 11 篇技术博客，7 个 Hugging Face 数据集，2 个开源模型 [6][16] |
| 已知客户 | 未披露 | 报道称阿里是主要合作方 [18] |

### 3.2 Copula Lab

**聚焦的数据。** 8 个产品，6 个归在 Coding，2 个归在 Cowork [2]。它的 Coding 不是修 bug，而是有视觉和交互产出的生成式工程：前端（WebDev、Vision2Web）、游戏（Godot 2D）、三维（Blender、Three.js、游戏美术）。Cowork 是金融和法律的长程任务环境，一条数据就是一个完整工作包。逐项明细见 [Copula Lab 档案](vendors/copula-lab.md)。

**获取方式。**

- 主来源是付费专家网络 [4]。金融和法律专家是兼职，每月 2–3 万元，每周至少 8 小时，要求 3 年以上一线经验。
- 专家做五件事：和产品、工程团队对齐；把真实工作流拆成分难度的任务体系；设计有区分度的任务；写参考答案和 Rubric；复核质量并仲裁争议样本 [4]。
- 原始材料有两种来路 [2]。金融任务用真实上市公司的公开披露，样例是给爱迪特（301580.SZ）写首次覆盖报告，题目规定只能用截至某日的公开信息。法律任务用封闭的模拟文档库，样例自称「simulation」，禁止联网；文档是否改编自真实项目官网没说，笔者推断是专家主导构造的。
- 报道称它从模型在真实任务里的失败模式出发，反推任务、轨迹、Rubric、环境和奖励信号 [17]。

**清洗和质检。** 公开信息很少。能确认的只有环节名称（任务拆解、Rubric、标准交付物、质检、环境生成）[1]，以及专家复核加争议仲裁 [4]。题目里内置了一些约束：金融题有信息截止日和来源分级要求，法律题有「负面对照」，惩罚没有依据就下违法或无效结论的回答 [2]。清洗规则、淘汰率、专家人数、数据量都没有公开。

媒体报道里还有几个官网上找不到的说法，例如中国版 GDPval、Bad Pattern 数据集、「AI 启发式访谈」[19][20]。官网站点地图的 23 个页面里没有对应内容 [67]，核对结果见 [Copula Lab 档案](vendors/copula-lab.md)。

### 3.3 UniPat AI

**聚焦的数据。** 十条数据线，覆盖编程、科研、医疗金融法律、视觉、预测、数学、电脑操作 [6]。明细见 [UniPat AI 档案](vendors/unipat-ai.md)。其中 Vibe-Coding Arena 是订阅制服务，由专家和 Agent 多轮协作并打分 [13]。卖给客户的部分有两个报道口径：

- The Information：付钱请法律、金融、医疗、科学专家产出 RL 后训练数据，同时用自研算法做合成数据 [21]。
- 硅星人：和阿里的合作以 RL 后训练数据为主，包括不同 Agent 框架下的编程轨迹和多工具任务 [18]。

**获取方式**，按来源分五类：

| 来源 | 做法 | 例子 |
|---|---|---|
| 真实代码仓库 | 每月新选约 20 个活跃仓库，取当月合并的 PR；或用真实跨版本 diff 当标准答案 | Monthly-SWEBench [11]、RoadmapBench [10] |
| 实时信号 | 预测市场合约、Google Trends 新话题加爬虫、专家出题 | Echo [9] |
| 网络图片 | 人工挑约 100 张种子图，反向图搜扩到约 4,000 张 | BabyVision [7] |
| LLM 合成、专家把关 | LLM 从已验证的科学论断出发生成研究题，专家每条审 1–2 小时 | UniScientist [8]、SaaS-Bench [14] |
| 专家直接生产 | 有资质的在职从业者写案例；专家选论断、搭环境、跑通参考流程 | ExpertEval [12]、PaperBenchX [15] |

专家怎么招、付多少钱，没有公开。

**清洗和质检。** 四类机制在各条线上反复出现：

1. **可执行验证**：不打补丁时目标测试必须失败，打上参考补丁后必须全过 [11]。
2. **难度校准**：多个模型各跑 4 次，全过或全挂的题调整或剔除 [10]。
3. **Rubric 筛选**：重复评分要一致，要能拉开分数，一条只考一个点 [8]。
4. **双人独立复核**：两位专家都同意才收，改完仍有争议的永久丢弃 [7]。

防污染的手段是时间隔离：每月换新仓库 [11]，题面隐去仓库名和版本号 [10]，预测任务只用未来事件 [9]。

**用训练证明数据有用。** UniPat 习惯自己拿数据训小模型再去别人的评测上测。ExpertEval 约 2,500 条用于 SFT，Qwen3.5-35B-A3B 在自家测试集上从 54.76% 升到 66.22% [12]。这是自报结果，测试集只有 90 题，且出题、训练、评测是同一家。

### 3.4 比较

| 维度 | Copula Lab | UniPat AI |
|---|---|---|
| 数据重心 | 专家的完整交付物，以及审美和交互质量的判断 | 可自动验证的任务，加带 Rubric 的专家案例 |
| 原始材料 | 专家经验、上市公司公开披露、自建封闭文档库 | 代码仓库、预测市场、网络图片、论文 |
| 人机分工 | 专家定义、制作、复核 | LLM 生成、专家审核为主；高风险领域由专家直接写 |
| 公开程度 | 只有样例页 | 流程、漏斗、数据集大多公开 |

笔者的判断：差别主要来自创始人背景。Copula 的创始人做 Agent 产品和对外评测合作，盯的是交付物能不能用、好不好看。UniPat 的创始人做后训练和数据合成，每条线都配了自动验证和训练实验。

### 3.5 其他供给方

- **智能知识**：专家网络（一面千识）、数据生产软件（Xpert Studio）和 RL 任务数据的组合。公开产品包括 Terminal RL Data（Docker 环境、测试脚本、参考解法）和 MCP Data [17]。
- **Surge AI**：推出 EnterpriseBench 系列 RL 环境，第一个是 Corecraft，并发表了训练结果 [40][24]。
- **AfterQuery**：据报道为 AI 实验室搭建数字办公「世界」[23]。

---

## 4 办公通信类仿真环境

### 4.1 代表性环境

| 环境 | 里面有什么 | 规模 | 数据怎么来 | 怎么判对错 |
|---|---|---|---|---|
| Gaia2 / ARE（Meta）[25][26] | 12 个应用 101 个工具：邮件、消息、群聊、日历、通讯录、文件等 | 10 个「宇宙」，1,120 个场景 | 全合成，按人设生成 | 核对写操作 |
| ClawsBench [30] | Gmail、Slack、日历、文档、网盘五个仿真服务 | 198 个接口，44 个任务 | 接口行为用真实账号的请求响应校准 | 比较数据库快照 |
| EmailBench（微软）[27] | 类 Outlook 的邮件、日历、联系人、待办 | 46 个工具，206 个场景 | 从 Enron 取主题和组织关系，正文重写 | 可执行断言加 LLM Rubric |
| MCP-Persona [28] | 12 个个人化服务：飞书、Slack、企业微信、Gmail、163 邮箱等 | 140 个工具，173 个任务 | 在真实服务上录调用，生成仿真器 | LLM 判检查点 |
| EnterpriseLab（富士通）[41] | 15 个 MCP 服务：聊天、邮件、代码、HR、网盘等 | 140 多个工具 | 仿真企业数据，专家核对 | 执行结果核对 |
| SaaS-Bench（UniPat）[14] | 23 个开源 SaaS，含邮箱和即时通讯 | 106 个任务 | LLM 出题，专家修订 | 检查应用最终状态 |

其他相关环境：

| 环境 | 特点 |
|---|---|
| AppWorld [31] | 9 个日常应用、457 个接口、约 100 个虚构用户、750 个任务 |
| WorkBench [32] | 5 个数据库、26 个工具、690 个任务，按结果状态判分 |
| TheAgentCompany [33] | 仿真软件公司，有会回话的模拟同事，175 个任务 |
| Toolathlon [34] | 32 个应用、604 个工具、108 个长程任务 |
| EnterpriseBench（富士通）[35] | 企业沙盒，含聊天和邮件，500 个任务，考权限层级 |
| MyPCBench [36] | 桌面加 17 个仿真网站，全部按一个人设灌数据，184 个任务 |
| AgentDojo [37] | 邮件、网银、订票，97 个任务加 629 个注入攻击用例 |

### 4.2 与飞书相关的工作

- **MCP-Persona** 仿真了飞书的 14 个工具。做法是用专用测试账号在真实飞书上执行调用、记录响应，再让 LLM 写出仿真代码。在 50 条真实调用记录上，它判断成败的准确率是 94.0%，只看接口文档写的仿真器是 58.0% [28]。
- **Workspace-Bench** 的任务场景来自字节内部飞书上的 154 个真实工作流，通过内部问卷收集、专家筛选。但文件不是真的，是爬来的公开材料加 LLM 合成的邮件和会议纪要 [29]。它有中文版数据。

钉钉和企业微信方面，没有找到专门的评测环境论文。

### 4.3 判分设计

三种做法：

- **状态快照比对**：比较任务前后的数据库，不看模型说了什么。ClawsBench、WorkBench、SaaS-Bench 都这样 [30][32][14]。
- **写操作核对**：Gaia2 只核对模型的写操作，读操作不管。收件人、会议编号这类字段精确比对，信件正文交给 LLM 按 Rubric 判，另外检查因果顺序和时间窗口 [25]。
- **断言加 Rubric 混合**：EmailBench 用 258 条可执行断言加 211 条 LLM Rubric [27]；DuMateBench 的总分是三成检查项加七成评审分 [39]。

验证器的可靠性差别很大：

- Gaia2 的验证器在 450 条人工标注轨迹上和人的一致率是 0.98，纯 LLM 评分只有 0.72 [25]。
- EnterpriseClawBench 的评审模型和人相比，文本类产出的相关系数是 0.790，视觉类是 −0.259 [38]。
- ARE 的作者承认，模型偶尔能在消息里嵌条件逻辑来钻 LLM 评审的空子 [26]。2026 年 10 月有一篇论文专门找 AppWorld 和 WorkArena 验证器的盲区 [64]（笔者只核对了标题）。

### 4.4 模型现在的水平

| 环境 | 最好成绩 |
|---|---|
| Gaia2 | 42% [25] |
| EmailBench | 33.5% [27] |
| MCP-Persona | 没有模型超过 50% [28] |
| ClawsBench | 任务成功率 39–64%，不安全操作率 7–33% [30] |
| Workspace-Bench | 约 60%，人是 80.7% [29] |

EmailBench 有一个值得注意的现象：最好的模型 99.7% 的工具调用没有报错，但只通过了 33.5% 的场景 [27]。调用成功不等于任务完成。

---

## 5 在环境中训练

### 5.1 实证结果

| 工作 | 环境 | 训练做法 | 结果 |
|---|---|---|---|
| Corecraft（Surge AI）[40] | 虚构电脑配件店的客服组织：2,500 多个实体、23 个工具 | GLM 4.6，GRPO，1,000 个任务，每个任务 16 条 rollout，1 个 epoch | 留出任务 25.37% → 36.76%；外部评测 BFCL Parallel +4.5、τ²-Bench Retail +7.4、Toolathlon +6.8 |
| EnterpriseLab [41] | 15 个 MCP 服务 | Qwen3-8B，先 SFT 再 GRPO，4 张 H200 跑 24–30 小时 | 自家环境 0.31 → 0.43，GPT-4o 是 0.45 |
| ART·E（OpenPipe）[42] | Enron 邮箱，搜邮件、读邮件、交答案三个工具 | Qwen 14B，GRPO，1 张 H100 不到一天，约 80 美元 | 自称在这个任务上比 o3 准、快、便宜 |
| Agent World Model [43] | 1,000 个合成环境 | 多轮工具调用的大规模 RL | 只在合成环境训练，三个评测上分布外泛化好 |
| EnvScaler [44] | 191 个环境、约 7,000 个场景 | Qwen3，SFT 加 RL | 三个评测上明显提升 |
| AgentScaler（阿里通义）[45] | 自动构造的函数调用环境 | 两阶段微调 | τ-bench 等评测上提升 |

所有数字都是作者自报。Corecraft 的作者自己说明，只测了一个模型、一个 epoch，哪些环境属性起作用还是假说 [40]。

### 5.2 环境的规模化生成

两条技术路线：

- **代码加数据库**：AWM 用管线依次生成场景、数据库结构、样例数据、工具接口和验证代码 [43]；EnvScaler 先生成环境骨架再生成场景 [44]。两者都认为这样的状态转移比 LLM 模拟更可靠。
- **LLM 直接模拟**：Simia 让推理模型模拟环境反馈，不需要真环境 [47]；DreamGym 用一个经验模型合成 rollout [48]。优点是不用做环境工程。

还有一条只合成轨迹、不搭环境的路线。Salesforce 的 APIGen-MT 先生成带标准动作的任务蓝图，再用模拟的人机对话把蓝图展开成完整的多轮轨迹，用来做 SFT [50]。

### 5.3 训练框架

- **ART**（OpenPipe）：把 GRPO 包成可以嵌进任意 Python 程序的库 [42]。
- **Agent Lightning**（微软）：让线上实际使用的 Agent 框架直接参与训练，训练器只看模型的请求和响应。用 6,000 条样本把 Qwen3.5-9B 在 SWE-bench Verified 上从 41.8% 提到 56.4% [46]。

### 5.4 工程经验

ART·E 记录的几条 [42]：

- 先用现成大模型跑基线。分数很低往往是环境有问题。
- 给「找到了对的邮件」发部分奖励没有加速训练；给「多走几步」发奖励会让模型反复调同一个工具直到步数用完。
- 所有轨迹分数都一样就没有学习信号，要盯奖励的方差。
- 人工抽看输出，汇总指标看不出模型在钻奖励的空子。

### 5.5 不更新权重的路线

微软的 Synthetic Computers at Scale 造了 1,000 台合成电脑，每台模拟跑 8 小时以上、2,000 多轮。它没有更新权重，只把经验提炼成技能文档，自家评测从 61.6% 升到 68.6% [49]。

---

## 6 从真实数据到可交付物：隐私与清洗

### 6.1 三条路线

**路线一：真实会话脱敏后直接做任务。**

- **EnterpriseClawBench** [38]：来源是一家 100 多人 AI 公司内部的 Agent 使用记录，员工在企业协作平台的私聊和群聊里发起。内部实体、链接、员工和客户编号、项目名、金额全部打码。5,291 个原始任务实例最终留下 852 个。**数据不公开**，只公开构造方法和一条脱敏样例。
- **DuMateBench** [39]：来源是线上 Agent 平台的真实会话。先去掉个人身份信息、凭证、令牌、私有地址，再人工逐条复查，无法安全脱敏的整条剔除。最终 200 个任务，**数据公开**。论文没说用了什么脱敏工具，也没说法律依据。

**路线二：真实数据只提供「形状」，内容重新合成。**

- **EmailBench** [27]：从 Enron 取主题和组织关系，邮件正文全部新写。场景选题参考了一个产品原型的聚合意图统计。
- **Workspace-Bench** [29]：只有任务场景是真的。
- **WinSyn** [51]：自动生成模拟数月项目的邮件，最多 25 个员工互动，刻意制造信息分散和前后矛盾。

**路线三：完全虚构。**

- **Gaia2** [25]：人设取自公开的人设库，邮件按「用户人设加联系人人设」生成。
- **Era by Eon** [52][53]：给定行业、规模和随机种子，生成一家完整的虚构公司，同一批实体投射到多个业务系统里。配一个专门找合成痕迹的检测器，起初标出 55.2% 的记录，调优后一条都标不出。
- **OrgForge** [54]：用确定性的程序维护事件和时间线，LLM 只写表面文字，避免事实互相矛盾。

### 6.2 清洗流程比较

| 数据 | 起点 | 终点 | 留存 | 主要淘汰原因 |
|---|---|---|---|---|
| EnronQA [59] | 517,401 封邮件 | 103,638 封 | 约 20% | 重复、被其他邮件完整包含、质量不达标 |
| EnterpriseClawBench [38] | 5,291 个任务实例 | 852 个 | 约 16% | 太短、缺输入文件、打码后无法恢复、依赖外网、不自包含 |
| Monthly-SWEBench [11] | 约 10,000 个 PR | 约 100 题 | 约 1% | 无测试、改动太小或太大、验证不过、指令有歧义 |
| BabyVision [7] | 约 4,000 张图 | 388 题 | 约 10% | 文字多、需文化知识、专家意见不一 |
| SaaS-Bench [14] | 全部候选任务 | 106 题 | 45% | 有歧义、不可执行、不够专业 |

把各家流程叠在一起，可以归纳出八个环节（笔者的归纳）：

1. **去重**。EnronQA 光这一步就去掉一半以上。
2. **机械门槛**：长度、格式、必要文件是否齐全。
3. **自包含和可执行性**：任务能否脱离原始上下文独立完成。
4. **隐私和敏感内容处理**。
5. **改写和标准化**：把多轮对话改成单轮指令，统一格式。
6. **配验证器或 Rubric**。
7. **人工复核**，通常两人独立。
8. **难度校准**：太简单和太难的都去掉。

### 6.3 匿名化的限度

- Staab 等人指出，LLM 从文本推断个人属性的能力接近人类，传统的文本匿名化方法已经跟不上 [55]。
- EmailBench 的作者明确说，合成内容不应被当作匿名化数据，因为真实的人名、职位和组织关系还在语料里 [27]。
- 办公通信的难点在于，删掉姓名和手机号之后，职位、项目、时间线和说话习惯合在一起仍然可能指向具体的人。这是笔者的判断。

Agent 自己会不会泄露隐私也是一个研究方向。PrivacyLens 和 AgentDAM 分别评测模型在代人通信和网页操作时是否遵守隐私规范 [56][57]。买方很可能要求环境里包含这类任务。

### 6.4 真实数据的交易

Forbes 报道的做法是：关停服务商在公司清算流程里加一步，把 Slack 存档、邮件和代码打包卖给 AI 数据买家；中间商在转售前去掉个人身份信息；单笔成交价的说法从十万美元到数十万美元不等 [23]。争议集中在两点：当事员工没有同意也不知情；隐私专家认为匿名化后仍可能认出具体的人。笔者没能读到 Forbes 原文，以上来自二手转述。

### 6.5 中国的合规要点

以下是笔者的理解，不是法律意见，需要法务核对原文：

- 《个人信息保护法》里，匿名化后的信息不算个人信息，去标识化的仍然算。向其他处理者提供个人信息，需要告知并取得个人的单独同意。
- 《生成式人工智能服务管理暂行办法》要求训练数据涉及个人信息的，应取得个人同意或符合法律规定的其他情形。买方同样受约束。
- 相关国标：GB/T 42460-2023（去标识化效果评估）、GB/T 45652-2025（生成式 AI 训练数据安全规范）[58]。
- 邮件和即时通讯消息还涉及通信对方的个人信息和所在公司的商业秘密。

---

## 7 开源生态：源码、数据与状态后端

逐个仓库的对照表在 [README](../README.md)，对应的数据文件在 [data/](../data/)。这里只讲三个结论。

### 7.1 状态后端有四种做法

| 做法 | 代表 | 优点 | 缺点 |
|---|---|---|---|
| SQLite 或 CSV，自己写服务 | AppWorld、AWM、ART·E、WorkBench | 重置快，并行便宜，判分可以直接比库 | 接口行为要自己保证像真的 |
| 内存里的 Python 对象 | ARE、AgentDojo、MCP-Persona | 最轻，一个进程就能跑 | 状态复杂后难持久化和审计 |
| 真实开源软件装进 Docker | TheAgentCompany、SaaS-Bench、EnterpriseLab、Toolathlon | 行为就是真的 | 重，几十到一百多 GB 磁盘，并行贵 |
| 整机镜像 | MyPCBench | 环境完全一致 | 里面的数据改不了 |

大规模 RL 更适合前两种。Corecraft 每个任务跑 16 条 rollout [40]，ART·E 每步 48 条轨迹 [42]，这个量用整套真实软件很难撑住。

### 7.2 许可分三档

- **能商用**：ARE、AppWorld、WorkBench、TheAgentCompany、AgentDojo、Workspace-Bench、EnvScaler、ART、Agent Lightning、Simia、OrgForge、EnterpriseRAG-Bench、DRBench，以及 AWM 的数据集。
- **禁商用**：ClawsBench、HERB。
- **仓库里没有许可文件**：MCP-Persona、Toolathlon、EnterpriseLab、EnterpriseClawBench、AWM 的代码。按惯例默认保留所有权利。

### 7.3 可得性

- **论文写得好但拿不到代码**：ClawsBench 只放了轨迹，五个仿真服务的代码没放；Corecraft 是 Surge AI 的商品；EmailBench 只说计划公开。
- **拿来就能训**：AWM 和 EnvScaler 把环境、数据、模型都放了；ART 的邮件示例一个 notebook 就能跑通；EnterpriseLab 最完整但没有许可，README 自己承认有写死的路径和端口冲突。

---

## 8 数据集

### 8.1 真实数据

| 数据集 | 内容 | 规模 | 怎么能用 |
|---|---|---|---|
| Enron（2015 版）[59] | 安然员工邮件，监管调查时公开，2015 版应当事人要求删过一批 | 517,401 封，150 个用户 | 公开 |
| EnronQA [59] | Enron 清洗后加问答 | 103,638 封邮件，528,304 个问答 | CC BY 4.0 |
| Avocado [60] | 一家倒闭 IT 公司的邮件、附件、日历 | 279 个账号 | 需签 LDC 协议，不得转发 |
| DuMateBench [39] | 真实 Agent 会话重建的任务 | 200 个 | 公开 |
| EnterpriseClawBench [38] | 真实企业 Agent 会话 | 852 个 | 不公开 |

### 8.2 合成数据

| 数据集 | 内容 | 规模 |
|---|---|---|
| EnterpriseRAG-Bench [61] | Slack、Gmail、Jira、Confluence 等 9 种来源，生成框架一并开源 | 约 50 万份文档 |
| HERB [62] | 文档、会议纪要、Slack 消息、代码仓库 | 39,190 份 |
| DRBench [63] | 办公软件、网盘、邮件、聊天 | 100 个任务 |
| Gaia2 宇宙 [25] | 邮件、聊天、日历、通讯录的完整应用状态 | 10 个，每个 40–80 万 token |
| Synthetic Computers [49] | 合成电脑的完整文件系统 | 公开 100 台 |
| Workspace-Bench [29] | 5 个角色的工作区，中英两版 | 20,476 个文件 |

### 8.3 空白

- 没有公开的真实飞书、钉钉、企业微信消息数据集。
- 没有公开的中文真实办公邮件语料。
- 邮件、即时通讯、文档、日历打通的真实数据，公开的只有 Avocado 部分做到，还要签协议。

---

## 9 讨论

### 9.1 共识

- **交付的是环境，不是语料。** 供给方的产品形态、学术界的评测、买方的采购，都指向「任务、状态、验证器」三位一体。
- **验证器是核心资产。** 没有可靠判分，环境既不能评测也不能训练。Epoch AI 的访谈里，买方最看重的也是防止模型钻判分的空子，其次是难度校准：通过率至少 2% 到 3%，接近 70% 的任务会被淘汰 [68]。
- **专家的价值在写任务和 Rubric。** Corecraft、Copula、UniPat 都把专家用在定义任务和评分标准上，而不是标注。
- **真实数据最稳妥的用法是当种子。** 微软、Meta、字节相关团队的做法一致。

### 9.2 分歧和证据缺口

- **真实数据是否比合成数据更能训出好模型，没有对照实验。** 买方愿意花钱买真实存档，理由是真实交流里有合成不出来的东西 [23]。但所有公开的正面训练结果都来自合成环境 [40][41][43][44]。唯一沾边的证据是一个合成邮件语料的数据集卡，自称用它训的模型在真实 Enron 上和 o3 打平 [65]，这是自报数字。
- **一个高保真环境和一千个合成环境，哪个更值。** Corecraft 用一个精心搭建的环境 [40]，AWM 用一千个自动生成的环境 [43]，都报告了分布外泛化，没有直接比较。
- **代码环境和 LLM 模拟环境。** 前者状态可靠但要做工程，后者省事但可能前后不一致 [43][47]。
- **既卖训练数据又做评测的独立性。** 如果同一家公司既训练又评测同一批模型，客户可能质疑它的中立 [22]。ExpertEval 就是出题、训练、评测同源 [12]。
- **LLM 评审靠不靠得住。** 文本类产出尚可，视觉类产出和人的判断几乎不相关 [38]。

### 9.3 尚未解决的问题

- 中文和飞书场景的真实数据空白。
- 多人、异步、长时间跨度的协作任务。Gaia2 刚开始做环境自己会变化的场景 [25]。
- 脱敏效果怎么度量。目前只有 Era by Eon 那种「找合成痕迹」的检测器 [52]，没有针对「能否认出真人」的公开验收方法。
- 安全。ClawsBench 里模型有 7–33% 的不安全操作 [30]。

---

## 10 给实践者的建议

以下是笔者的判断，针对手里有带隐私的真实办公数据、想做成环境交付给模型公司的团队。

**10.1 交付环境，不交付原文。**
真实数据的价值在于任务分布、组织关系、信息分散和矛盾的方式。这些可以提取出来，不必把原文交出去。

**10.2 先过法务，再谈交付。**
「带个人隐私的数据直接给大模型公司」这一步风险最大。买方也受训练数据来源合法的约束，会反过来查数据来源。

**10.3 一个比较稳的流程。**

1. 原始数据留在自己这边，只提取任务场景、组织结构、话题分布、信息流转模式。
2. 用提取出的结构重新生成正文，人名、公司名、金额、项目名全部替换。
3. 做对抗验收：让一个强模型尝试从成品反推原始人物或公司，推得出就退回。
4. 交付环境、任务、验证器，以及一份说明清洗和验收方法的文档。

**10.4 各个部件可以参考谁。**

| 要做的事 | 参考 | 理由 |
|---|---|---|
| 邮件、消息、日历的应用和判分 | ARE | MIT 许可，有现成模块和写操作验证器 |
| 用 SQLite 存状态、按任务重置 | AppWorld | Apache-2.0，每应用一库，带造数据指南 |
| 飞书接口仿真 | MCP-Persona | 唯一公开的飞书仿真；无许可，要先问作者 |
| 真实会话变任务 | EnterpriseClawBench 的构造管线 | 唯一公开的实现；无许可，要先问作者 |
| 批量生成更多环境 | AWM 或 EnvScaler | 都验证过能训出效果 |
| 第一次训练验证 | ART | 有邮件场景的现成例子 |
| 中文办公文件 | Workspace-Bench 中文版 | 唯一带中文数据的 |

**10.5 用一次小规模训练证明数据有用。**
Corecraft、UniPat、EnterpriseLab 都这样做：拿一个开源小模型在自己的环境里训一轮，再去外部评测上测，用涨分说话。

---

## 11 局限

- 检索以英文 arXiv 为主。中文厂商的内部做法基本不发论文，肯定有遗漏。
- 长论文只读到前 10 万字符，附录内容可能缺失。AWM、EnvScaler、AgentScaler、Simia、DreamGym 只读了摘要。
- Copula Lab 的结论几乎全部来自官网自述。它没有论文和公开数据集，无法独立检验。
- UniPat 的流程和训练效果来自它自己的博客和论文，没有第三方复现。
- The Information、Bloomberg、Forbes 的原文都没能读到，相关内容来自转述。ART·E 的原始博客也打不开，细节来自 ZenML 的转述。
- 所有开源仓库都没有实际运行。「无许可」只代表仓库里没有许可文件。
- 法律部分没有逐条核对法条原文。
- 两家公司和这个领域都变化很快，本文只反映 2026-10-08 的状态。
- 两处数字口径：Gaia2 的 800 是人工标注的原始场景，1,120 含 320 个增强场景 [25]；DuMateBench 的摘要写 8 个大场景 17 个能力类别，正文写 5 个和 14 个 [39]。
- 两家公司的融资口径互相冲突，都来自匿名信源，见各自的档案页。

---

## 参考文献

**公司一手材料**

- [1] Copula Lab 官网首页. https://www.copulalab.com/
- [2] Copula Lab 数据产品页（含各产品子页）. https://www.copulalab.com/products/data-products
- [3] Copula Lab Benchmark 页. https://www.copulalab.com/products/benchmark
- [4] Copula Lab 专家招募页（含金融、法律岗位页）. https://www.copulalab.com/experts
- [5] Copula Lab 公司页与招聘页. https://www.copulalab.com/company
- [6] UniPat AI 博客目录. https://unipat.ai/blog
- [7] BabyVision: Visual Reasoning Beyond Language. arXiv:2601.06521. https://arxiv.org/abs/2601.06521
- [8] UniScientist. https://unipat.ai/blog/UniScientist ；https://github.com/UniPat-AI/UniScientist
- [9] Echo: Towards General AI Prediction. https://unipat.ai/blog/Echo
- [10] Terminal-X. https://unipat.ai/blog/TerminalX
- [11] Monthly-SWEBench. https://unipat.ai/benchmarks/MonthlySWEBench ；数据集卡 https://huggingface.co/datasets/UnipatAI/Monthly-SWEBench-2026-03
- [12] ExpertEval. https://unipat.ai/blog/ExpertEval
- [13] Vibe-Coding Arena. https://unipat.ai/blog/Vibe-Coding-Arena
- [14] SaaS-Bench. arXiv:2605.15777. https://arxiv.org/abs/2605.15777 ；https://github.com/UniPat-AI/SaaS-Bench
- [15] PaperBenchX. https://unipat.ai/blog/PaperBenchX
- [16] UniPat AI Hugging Face 组织页. https://huggingface.co/UnipatAI

**媒体报道**

- [17] 硅星人. 本周AI项目推荐｜智能知识、Copula Lab、UniPat…. 2026-08-16. https://finance.sina.cn/stock/jdts/2026-08-16/detail-ininnkfv8014751.d.html
- [18] 硅星人. AI的热钱与未来，此刻属于中国版Alexandr Wang们. 2026-09-24. https://www.163.com/dy/article/L7JI5DP20511N33R.html
- [19] 虾蛄AI（AIGC.BAR 转载）. https://www.aigc.bar/AI%E8%B5%84%E8%AE%AF%E6%96%87%E7%AB%A0/2026/08/08/ai-vocational-training-high-quality-data-startup
- [20] AI工具集. Copula Lab. https://ai-bot.cn/copula-lab/
- [21] Dealroom 转述 The Information. 2026-09-15. https://dealroom.co/news/150873-chinas-unipat-hits-1b-valuation-on-just-30m-in-orders/
- [22] 36氪、虎嗅转述 Bloomberg. https://eu.36kr.com/zh/p/3977467794069126 ；https://www.huxiu.com/article/4890186.html
- [23] Forbes 2026-04-16 报道（经 Techmeme、Fast Company 转述）. https://www.techmeme.com/260416/p46 ；https://www.fastcompany.com/91528808/shuttered-startups-are-selling-old-slack-chats-and-emails-to-ai-companies
- [24] Surge AI. EnterpriseBench Corecraft 博客. https://www.surgehq.ai/blog/enterprisebench-corecraft

**办公环境**

- [25] Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments. arXiv:2602.11964. https://arxiv.org/abs/2602.11964
- [26] ARE: Scaling Up Agent Environments and Evaluations. arXiv:2509.17158. https://arxiv.org/abs/2509.17158
- [27] EmailBench. arXiv:2609.31906. https://arxiv.org/abs/2609.31906
- [28] MCP-Persona. arXiv:2606.02470. https://arxiv.org/abs/2606.02470
- [29] Workspace-Bench 1.0. arXiv:2605.03596. https://arxiv.org/abs/2605.03596
- [30] ClawsBench. arXiv:2604.05172. https://arxiv.org/abs/2604.05172
- [31] AppWorld. arXiv:2407.18901. https://arxiv.org/abs/2407.18901
- [32] WorkBench. arXiv:2405.00823. https://arxiv.org/abs/2405.00823
- [33] TheAgentCompany. arXiv:2412.14161. https://arxiv.org/abs/2412.14161
- [34] The Tool Decathlon. arXiv:2510.25726. https://arxiv.org/abs/2510.25726
- [35] Can LLMs Help You at Work? A Sandbox for Evaluating LLM Agents in Enterprise Environments. arXiv:2510.27287. https://arxiv.org/abs/2510.27287
- [36] MyPCBench. arXiv:2606.16748. https://arxiv.org/abs/2606.16748
- [37] AgentDojo. arXiv:2406.13352. https://arxiv.org/abs/2406.13352
- [38] EnterpriseClawBench. arXiv:2606.23654. https://arxiv.org/abs/2606.23654
- [39] DuMateBench. arXiv:2608.26546. https://arxiv.org/abs/2608.26546

**训练与环境生成**

- [40] EnterpriseBench Corecraft: Training Generalizable Agents on High-Fidelity RL Environments. arXiv:2602.16179. https://arxiv.org/abs/2602.16179
- [41] EnterpriseLab. arXiv:2603.21630. https://arxiv.org/abs/2603.21630
- [42] OpenPipe. ART·E（博客，经 ZenML 转述）与 ART 仓库. https://www.zenml.io/llmops-database/building-art-e-reinforcement-learning-for-email-search-agent-development ；https://github.com/OpenPipe/ART
- [43] Agent World Model. arXiv:2602.10090. https://arxiv.org/abs/2602.10090
- [44] EnvScaler. arXiv:2601.05808. https://arxiv.org/abs/2601.05808
- [45] Towards General Agentic Intelligence via Environment Scaling. arXiv:2509.13311. https://arxiv.org/abs/2509.13311
- [46] Agent Lightning v1.0: Towards Harnessed Agentic RL. arXiv:2608.17528. https://arxiv.org/abs/2608.17528
- [47] Simulating Environments with Reasoning Models for Agent Training. arXiv:2511.01824. https://arxiv.org/abs/2511.01824
- [48] Scaling Agent Learning via Experience Synthesis. arXiv:2511.03773. https://arxiv.org/abs/2511.03773
- [49] Synthetic Computers at Scale for Long-Horizon Productivity Simulation. arXiv:2604.28181. https://arxiv.org/abs/2604.28181
- [50] APIGen-MT. arXiv:2504.03601. https://arxiv.org/abs/2504.03601

**合成企业数据与隐私**

- [51] WinSyn. arXiv:2609.12171. https://arxiv.org/abs/2609.12171
- [52] The Era by Eon Benchmark. arXiv:2609.09853. https://arxiv.org/abs/2609.09853
- [53] Generating a Consistent Enterprise. arXiv:2609.11286. https://arxiv.org/abs/2609.11286
- [54] OrgForge. arXiv:2603.14997. https://arxiv.org/abs/2603.14997
- [55] Large Language Models are Advanced Anonymizers. arXiv:2402.13846. https://arxiv.org/abs/2402.13846
- [56] PrivacyLens. arXiv:2409.00138. https://arxiv.org/abs/2409.00138
- [57] AgentDAM. arXiv:2503.09780. https://arxiv.org/abs/2503.09780
- [58] 中国生成式 AI 安全标准英译（CSET，含 GB/T 45652 征求意见稿）. https://cset.georgetown.edu/publication/translation-snapshot-chinese-generative-ai-safety-standards/

**数据集及其他**

- [59] EnronQA: Towards Personalized RAG over Private Documents. arXiv:2505.00263. https://arxiv.org/abs/2505.00263
- [60] Avocado Research Email Collection. LDC2015T03. https://catalog.ldc.upenn.edu/LDC2015T03
- [61] EnterpriseRAG-Bench. arXiv:2605.05253. https://arxiv.org/abs/2605.05253
- [62] Benchmarking Deep Search over Heterogeneous Enterprise Data (HERB). arXiv:2506.23139. https://arxiv.org/abs/2506.23139
- [63] DRBench. arXiv:2510.00172. https://arxiv.org/abs/2510.00172
- [64] Finding Blind Spots in AppWorld and WorkArena Task Verifiers. arXiv:2610.09142. https://arxiv.org/abs/2610.09142
- [65] Vectrix ART-E 合成邮件语料. https://huggingface.co/datasets/TonicAI/vectrix-art-e
- [66] Preqin. Copula Lab 资产档案. https://www.preqin.com/data/profile/asset/copula-lab/813711
- [67] Copula Lab 站点地图. https://www.copulalab.com/sitemap.xml
- [68] Epoch AI. An FAQ on Reinforcement Learning Environments. 2026-01-12. https://epoch.ai/gradient-updates/state-of-rl-envs
