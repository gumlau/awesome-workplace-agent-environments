# UniPat AI 档案

核实日期：2026-10-08。除特别标明的「报道」外，内容来自公司的博客、论文和数据集卡，属于公司自述。

| 项目 | 内容 |
|---|---|
| 成立 | 2025 年底，北京（[Dealroom 转述 The Information](https://dealroom.co/news/150873-chinas-unipat-hits-1b-valuation-on-just-30m-in-orders/)、[36氪](https://eu.36kr.com/zh/p/3977467794069126)） |
| 创始人 | 李宽：前阿里通义实验室，WebSailor 论文一作。陈亮：联合创始人兼 CTO，前 Qwen 和 Moonshot 多模态（[硅星人](https://www.163.com/dy/article/L7JI5DP20511N33R.html)） |
| 公开产出 | [11 篇技术博客](https://unipat.ai/blog)，[7 个数据集和 2 个开源模型](https://huggingface.co/UnipatAI)，[GitHub](https://github.com/UniPat-AI) |
| 客户（报道） | 阿里是主要合作方；阿里、字节、Moonshot、DeepSeek 买过它或其对手的数据 |

---

## 数据线

发布月份均为 2026 年。

| 产品 | 领域 | 规模 | 是否公开 |
|---|---|---|---|
| [BabyVision](https://arxiv.org/abs/2601.06521)（1 月） | 基础视觉推理 | 388 题，4 大类 22 子类；另有 1,400 条训练样本 | 公开，MIT |
| [UniScientist](https://unipat.ai/blog/UniScientist)（3 月） | 科研级开放问题，50 多个学科 | 4,700 多条，每条 20 条以上评分标准 | 只放模型和代码 |
| [Echo](https://unipat.ai/blog/Echo)（3 月） | 未来事件预测 | 3 月底有 967 道活跃题 | 排行榜和接口 |
| [Terminal-X](https://unipat.ai/blog/TerminalX)（5 月） | 终端里的编程 Agent | 50 题；26 个任务共 227 轮；115 个任务跨 17 个仓库 | 公开 |
| [Monthly-SWEBench](https://unipat.ai/benchmarks/MonthlySWEBench)（每月） | 真实仓库的修 bug 和加功能 | 每月约 100 题 | 公开，MIT |
| [ExpertEval](https://unipat.ai/blog/ExpertEval)（5 月） | 医疗、金融、法律的专业判断 | 3,213 个案例，207 个场景，平均每题 21.83 条评分标准 | 需申请 |
| [Vibe-Coding Arena](https://unipat.ai/blog/Vibe-Coding-Arena)（7 月） | 多轮人机协作编程 | 约 640 个任务，13 种语言 | 订阅制服务 |
| [SaaS-Bench](https://arxiv.org/abs/2605.15777)（9 月） | 跨业务软件的电脑操作 | 106 个任务，23 个系统 | 代码公开 |
| [PaperBenchX](https://unipat.ai/blog/PaperBenchX)（10 月） | 跨学科论文复现 | 93 个任务，3,168 个评分点 | 12 个公开，81 个留存 |

卖给客户的部分有两个报道口径：

- The Information：付钱请法律、金融、医疗、科学专家产出 RL 后训练数据，同时用自研算法做合成数据，另有编程、生物医学、视觉方向的评测。
- 硅星人：和阿里的合作以 RL 后训练数据为主，包括不同 Agent 框架下的编程轨迹和多工具任务。做法是先在小模型上低成本试验，筛出有效方案再扩大生产。

---

## 数据怎么获取

| 来源 | 做法 | 例子 |
|---|---|---|
| 真实代码仓库 | 每月新选约 20 个活跃仓库，取当月合并的 PR；或用真实跨版本 diff 当标准答案 | Monthly-SWEBench、RoadmapBench |
| 实时信号 | 预测市场合约；Google Trends 新话题加爬虫再由 Agent 出题；专家出题并在约定时间裁决 | Echo |
| 网络图片 | 人工挑约 100 张种子图，反向图搜和关键词检索扩到约 4,000 张 | BabyVision |
| LLM 合成、专家把关 | LLM 从多条已验证的科学论断出发生成研究题，专家每条审 1–2 小时 | UniScientist、SaaS-Bench |
| 专家直接生产 | 有资质的在职从业者写案例；专家选论断、搭环境、跑通参考流程 | ExpertEval、PaperBenchX、Vibe-Coding Arena |

专家怎么招、付多少钱、有多少人，没有公开。[招聘页](https://unipat.ai/joinus)只有一个「Expert Community Lead」的岗位名。

---

## 数据怎么清洗和质检

四类机制在各条线上反复出现。

### 机制一：可执行验证

- Monthly-SWEBench：不打补丁时回归测试通过、目标测试失败；打上参考补丁后全部通过。
- 测试必须真正执行代码、用多组输入。禁止匹配源码文本、只看退出码、只测单一输入。
- Terminal-X：参考解必须在任务容器里拿到满分。
- PaperBenchX：专家在干净环境里把参考流程重跑一遍。

### 机制二：难度校准

- Terminal-X 用多个模型各跑 4 次，所有模型全过或全挂的题调整或剔除。
- 其中一个子集只留 Claude Opus 4.6 四次里通过 1 到 3 次的题。

### 机制三：评分标准的筛选

UniScientist 对每条标准过三道筛：

- 客观一致性：同一份报告重复评多次，结果要一致。
- 区分度：分数要能拉开不同完成度。
- 原子性：一条只考一个知识点。

ExpertEval 的设计：

- 四条原则：具体、可验证、结构化、设关键负面项。
- 依赖外部知识的标准必须锚定权威一手来源并附链接。
- 关键负面项是负权重，通常 −3 到 −5。
- 前置条件没满足时，下游标准自动记零分。

### 机制四：双人独立复核

- BabyVision：两位专家独立判断答案是否唯一、是否主要靠视觉得出。两人都同意才收；有分歧退回修改；改完仍有争议的永久丢弃。
- PaperBenchX：两位独立领域专家审范围、公平性、可复现性和评分。
- SaaS-Bench：静态检查之后，专家亲自执行一遍任务，核对指令和验证器是否一致。
- Monthly-SWEBench：从解题者视角复核，看合理的另一种实现会不会被误判为错。

### 防污染

- Monthly-SWEBench 每月换新仓库和新 PR，删掉未来分支。
- RoadmapBench 剥掉目标版本之后的提交和标签，题面隐去仓库名和版本号。
- Echo 只用未来事件训练。

### 公开的漏斗

| 数据线 | 起点 | 终点 | 留存 |
|---|---|---|---|
| Monthly-SWEBench | 约 10,000 个 PR | 约 100 题 | 约 1% |
| BabyVision | 约 4,000 张候选图 | 388 题 | 约 10% |
| SaaS-Bench | 全部候选任务 | 106 题 | 45% |

Monthly-SWEBench 的逐级漏斗：10,000 → 合并到主分支 5,000 → 有测试改动 2,000 → 复杂度达标 800 → 过质量门 300 → 验证通过 150 → 对齐复核 100。

### Monthly-SWEBench 的筛选规则

- 仓库：500 星以上、30 天内活跃、有测试、至少 3 次发布、1 万到 100 万行代码。
- PR：必须含测试改动；至少改 1 个源文件、新增 30 行以上；不超过 100 个文件；排除纯界面调整、依赖升级、持续集成配置。

---

## 用训练证明数据有用

- UniScientist：在 Qwen3-30B-A3B 上做 SFT，约 1,200 个 H200 GPU 小时。训练用的参考答案按评分标准筛，分数过阈值才留。
- ExpertEval：约 2,500 条用于 SFT，90 条留作测试。Qwen3.5-35B-A3B 在自家测试集上从 54.76% 升到 66.22%。

这些是自报结果。ExpertEval 的测试集只有 90 题，且出题、训练、评测是同一家。

---

## 口径冲突和未证实的地方

**融资**

- Bloomberg（经 36氪、[Dealroom](https://dealroom.co/news/149924-alibaba-leads-300m-round-for-ai-testing-startup-unipat-at-2-5b/) 转述）：阿里拟领投约 3 亿美元，估值 25 亿美元，还在谈。
- The Information（经 Dealroom 转述）：已完成一轮，投前估值约 10 亿美元，截至 5 月底订单约 3,000 万美元。Dealroom 另一条标题把估值写成 6.47 亿美元，与正文不一致。
- 两者都是匿名信源，公司未确认。

**其他**

- ExpertEval 总数 3,213，测试 90，训练约 2,500，剩下约 620 条去向未说明。
- 既卖训练数据又做评测，客户可能质疑它的中立（[虎嗅](https://www.huxiu.com/article/4890186.html)的评论）。
