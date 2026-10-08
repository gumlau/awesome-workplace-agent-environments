# Copula Lab 档案

核实日期：2026-10-08。除特别标明的「报道」外，内容都来自公司官网，属于公司自述。

| 项目 | 内容 |
|---|---|
| 成立 | 2026 年上半年，上海（[硅星人](https://www.163.com/dy/article/L7JI5DP20511N33R.html)、[Preqin](https://www.preqin.com/data/profile/asset/copula-lab/813711)） |
| 创始人 | 梁丽：前 MiniMax Agent 业务负责人，搭过内部 Agent 评测。蔡佳人：前 MiniMax 开源负责人和后训练工程师，对接过 LMArena、Vals AI、Terminal-Bench 等（[公司页](https://www.copulalab.com/company)） |
| 定位 | 为前沿模型提供专家构建的评测、数据和环境（[首页](https://www.copulalab.com/)） |
| 四块业务 | 数据、环境、专家网络、评测 |
| 公开产出 | 8 个数据产品的样例页，2 个在研评测。没有论文，没有公开数据集 |
| 客户 | 未披露 |

---

## 数据产品

来源：[数据产品页](https://www.copulalab.com/products/data-products)。6 个归在 Coding，2 个归在 Cowork。

| 产品 | 类别 | 一条数据里有什么 |
|---|---|---|
| [WebDev](https://www.copulalab.com/products/data-products/webdev-aesthetics) | Coding | 自然语言需求、可运行的前端工程、成品截图、开发轨迹、专家分维度评分。样本按行业、产品形态、页面类型、视觉风格组织 |
| [Vision2Web](https://www.copulalab.com/products/data-products/vision2web) | Coding | 文字需求、页面截图、交互参考视频、可复用素材，加实现代码、运行与评测环境、制作轨迹。视觉还原度和功能行为分开评 |
| [Godot 2D · GameCraft](https://www.copulalab.com/products/data-products/godot-gamecraft) | Coding | 产品需求文档、运行环境、参考工程、制作轨迹、任务专属评测标准。回放输入可得到游戏状态记录、视频和关键帧 |
| [3D with Blender](https://www.copulalab.com/products/data-products/Web3D-with-blender) | Coding | Blender 源文件、可复现的制作脚本、导出资产、能独立运行的网页三维应用 |
| Web3D with Three.js | Coding | 用代码写的程序化三维应用，覆盖几何、材质、光照、动画、交互 |
| Game3D · Native Game Art | Coding | 原生美术工具里的可编辑工程：建模、绑定、动画、材质、贴图、场景、灯光 |
| [金融长程任务环境](https://www.copulalab.com/products/data-products/long-horizon-finance) | Cowork | 任务要求、多份参考材料、执行记录、逐项评分标准，以及人做出来的交付物（PDF 研报加可重算的表格模型） |
| [法律长程任务环境](https://www.copulalab.com/products/data-products/long-horizon-legal) | Cowork | 几十到上百份合同、邮件、会议纪要、账目和证据文件，要求产出多份互相勾稽的交付物 |

用途：SFT、偏好学习、RL、定向评测。

另有两个评测在开发中：三维生成，以及中文语境的金融长程 Agent（[Benchmark 页](https://www.copulalab.com/products/benchmark)）。

### 金融样例

- 任务：给爱迪特（301580.SZ）写首次覆盖报告。
- 约束：只能用截至 2026-08-06 的公开信息；要区分公司披露、监管文件、第三方材料和分析师假设；尚未落地的政策、产能、订单不得写成既成事实。
- 交付：PDF 报告和可重算的 XLSX 模型，版本号一致，关键数据要标期间、单位、来源和页码。
- 另两个样例：格力电器、桃李面包的预测估值模型。

### 法律样例

- 任务：买方并购尽调，审阅编号 VDR-001 到 VDR-100 的封闭数据室。
- 约束：自称「simulation」，规定了法律快照日期，禁止联网；缺材料不等于事情没发生，要标出不确定并给出核实路径。
- 负面对照：没有依据就下违法、终止、无效结论的回答会被扣分。
- 交付：红旗备忘录、问题清单（JSON）、同意与行动矩阵（CSV）、追问清单，四份文件的问题编号要一致。

---

## 数据怎么获取

**专家网络**（[专家页](https://www.copulalab.com/experts)）

| 岗位 | 条件 | 报酬 |
|---|---|---|
| 金融领域专家 | 3 年以上卖方研究、买方投资、PE 或估值经验，CFA 或 FRM 优先 | 兼职，每月 2–3 万元，每周至少 8 小时 |
| 法律领域专家 | 3 年以上顶级律所或头部企业法务经验，须有法律职业资格 | 同上 |
| Web3D 审美交互实习生、游戏技术美术实习生 | — | 实习 |

申请时要交代表性研报、建模或文书样本，涉密的先脱敏。

**专家做五件事**

1. 通过访谈、材料审阅、平台实操，和数据产品、工程团队对齐。
2. 把真实工作流拆成可枚举、分难度的任务体系。
3. 设计有区分度的任务。
4. 写可复现的参考答案和评分标准，写明得分点和判断边界。
5. 复核任务和标注质量，仲裁有争议的样本。

**原始材料**

- 金融用真实上市公司的公开披露。
- 法律用封闭的模拟文档库。文档是否改编自真实项目，官网没说。

**报道补充**：它从模型在真实任务里的失败模式出发，反推任务、轨迹、评分标准、环境和奖励信号（[硅星人](https://finance.sina.cn/stock/jdts/2026-08-16/detail-ininnkfv8014751.d.html)）。

---

## 数据怎么清洗和质检

能确认的：

- 环节名称：专家任务拆解 → 评分标准 → 标准交付物 → 质检 → RL 环境生成（[首页](https://www.copulalab.com/)）。
- 评分标准由专家写，定义评分维度和每道题的锚点。
- 专家复核加争议仲裁。
- 题目内置的约束：信息截止日、来源分级、负面对照。
- 可复现的验证手段：游戏用输入回放，三维评测用可运行的验证脚本。
- 工程岗位的招聘要求里列了质量目标：任务真实性、环境稳定性、答案可验证性、奖励合理性、数据有效性（[招聘页](https://www.copulalab.com/careers/agent-infra-engineer)）。这是招聘要求，不代表已经做到。

没有公开的：清洗规则、淘汰率、质检轮次、专家人数、数据量、脱敏规范。

---

## 报道里有、官网上没有的

| 说法 | 出处 | 核对结果 |
|---|---|---|
| 中国版 GDPval，按中国官方 GDP 产业结构加权，再按知识工作密度筛任务 | [虾蛄AI](https://www.aigc.bar/AI%E8%B5%84%E8%AE%AF%E6%96%87%E7%AB%A0/2026/08/08/ai-vocational-training-high-quality-data-startup)、[AI工具集](https://ai-bot.cn/copula-lab/) | [站点地图](https://www.copulalab.com/sitemap.xml)的 23 个页面里没有 |
| Bad Pattern 数据集，标注事实引用、数字一致性、证据匹配、隐性规则几类失败 | 同上 | 官网首页只出现了这个词，没有产品页 |
| WebDev 的评分维度是布局、字体、色彩、动效、场景契合度，另有「反 AI 味」 | 虾蛄AI | 官网只说有专家分维度评分 |
| AI 启发式访谈、多专家交叉质检 | 同上两处 | 官网只写了访谈、质检和争议仲裁 |

## 融资口径

三处说法不一致，都没有公司确认：

- 虾蛄AI：拿了一线机构首轮投资，估值千万美元级。
- 硅星人：8 月称未披露，9 月称已获投资但没说金额。
- Preqin：记了一笔 2026 年 8 月的风险投资。
