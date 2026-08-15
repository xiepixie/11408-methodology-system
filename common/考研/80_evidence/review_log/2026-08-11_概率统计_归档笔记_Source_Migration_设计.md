# 概率统计归档笔记 Source Migration 设计

> 日期：2026-08-11  
> 类型：Evidence / Import Design，不是知识 Owner  
> 状态：首轮 Source Diff 与本轮整体结构审阅已完成；进入真题/陌生题 Rules 攻击与跨册参数化验证
> 输入：归档目录 18 份正文笔记 + 1 份 MOC，共 14,821 行  
> 输出 Owner：`10_数学一/30_概率论/` 下八个 Topic 的 Canonical `.tex`；动作性知识另入概率统计 Rules

## 1. 迁移原则

这次迁移不采用“压缩摘要”或“Pandoc 片段拼接”。每个源知识块必须得到且只得到一种处置：

1. **Core**：进入对应 Topic 的主推演链；
2. **Boundary**：保留定义边界、反例或适用条件，防止主干结论被误用；
3. **Extension**：完整保留超出数学一主线、但能解释机制或连接后续理论的内容；
4. **Use**：由其他 Owner 定义，本册只保留调用接口；
5. **Rule Candidate**：只抽取题面信号、动作、校验和停止条件，不复制理论正文；
6. **Merge**：与另一源块语义重复，合并到唯一 Owner，并在本表保留来源映射。

“不进入 Core”不等于删除。只有装饰性重复目录、同义速查表和重复知识结构图可以压缩；其中的独立语义仍须由前五类之一承接。

## 2. Source Pack 锁定

| Source ID | 源文件 | 行数 | 主要目标 Owner |
|---|---|---:|---|
| P-MOC | `_概率论与数理统计 MOC.md` | 44 | Subject Atlas（只作 Source Diff，不直接覆盖 Atlas） |
| P01-A | `随机事件与样本空间.md` | 697 | Topic 01 |
| P01-B | `概率的定义与性质.md` | 279 | Topic 01 |
| P02-A | `条件概率与独立性.md` | 323 | Topic 02 |
| P02-B | `全概率公式.md` | 500 | Topic 02 |
| P02-C | `贝叶斯公式.md` | 488 | Topic 02 |
| P03-A | `一维随机变量.md` | 1,131 | Topic 03；函数变换移交 Topic 04 |
| P03-B | `随机变量与事件构造.md` | 620 | Topic 03；联合/顺序结构分别移交 Topic 04/07 |
| P04-A | `多维随机变量.md` | 1,373 | Topic 04；数字特征移交 Topic 05；顺序统计量移交 Topic 07 |
| P04-B | `随机变量的函数与分布可加性.md` | 806 | Topic 04 |
| P05-A | `数字特征.md` | 844 | Topic 05 |
| P06-A | `极限定理.md` | 1,029 | Topic 06 |
| P07-A | `数理统计基本概念.md` | 728 | Topic 07 |
| P07-B | `抽样分布.md` | 786 | Topic 07；大样本理论调用 Topic 06 |
| P07-C | `常用统计量的数字特征.md` | 653 | Topic 07；总体数字特征调用 Topic 05 |
| P08-A | `点估计.md` | 1,178 | Topic 08 |
| P08-B | `估计量的评价标准.md` | 1,153 | Topic 08 |
| P08-C | `区间估计.md` | 1,081 | Topic 08 |
| P08-D | `假设检验.md` | 1,108 | Topic 08 |

源文件的 SHA-256 已在本次迁移终验时重新核对；源内容变化必须重做受影响文件的 Source Diff，不能沿用旧的“已覆盖”结论。

## 3. 全量知识路由

### P01-A 随机事件与样本空间

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1 | 随机试验；样本点/样本空间；记录规则决定粒度；合理性；离散/连续类型 | Topic 01 Core：先定义记录协议，再定义世界 |
| 2 | 事件；事件域与 $\sigma$-代数；概率空间；特殊事件；概率为 0/1 与必然/不可能的区别 | Topic 01 Core + Boundary；测度论表述列为 Extension 但不得删除 |
| 3–4 | 并、交、差、补；教材简写；包含/相等/互斥；事件代数与 De Morgan | Topic 01 Core |
| 5 | 两事件、三事件、$n$ 事件的自然语言翻译 | Topic 01 Core；动作抽入 Rules Candidate |
| 6 | 事件关系向概率关系的传递及不可逆边界 | Topic 01 Boundary |
| 7 | 骰子贯穿示例 | Topic 01 Worked Example，重写为模型运行而非例题堆叠 |
| 8–9 | 易混概念；事件建模流程 | Topic 01 Boundary + Rules Candidate |
| 10–11 | 结论速查、知识结构图 | Merge 到 Topic 01 章节末压缩页，不作为独立知识 |

### P01-B 概率的定义与性质

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1 | 概率空间、Kolmogorov 公理、有限可加性 | Topic 01 Core；可数可加的形式边界保留 |
| 2 | 古典概型、几何概型、均匀模型统一形式 | Topic 01 Core；“等可能”前提进入 Boundary/Rule |
| 3–4 | 单调性、补集、差事件、加法、容斥、De Morgan 逆向计算 | Topic 01 Core，与 P01-A 合并 |
| 5 | Union Bound、Fréchet 界、Bonferroni、补事件乘积极值 | Topic 01 Extension + Boundary；保留适用条件 |
| 6 | 概率连续性 | Topic 01 Extension，作为极限与概率测度接口 |
| 7–8 | 模型选择、统一流程、边界与易错 | Topic 01 Rules Candidate + Boundary |
| 9 | 知识结构图 | Merge 到 Topic 01 总图 |

### P02-A 条件概率与独立性

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1–2 | 条件概率的缩小世界/重新归一化；条件测度；乘法链 | Topic 02 Core |
| 3–5 | 两事件独立；补事件封闭；多事件两两/相互独立；独立与互斥 | Topic 02 Core + Boundary |
| 6 | 事件正/负关联；指示变量协方差 | Topic 02 Extension，协方差定义 Use Topic 05 |
| 7 | 条件独立及其与无条件独立的非蕴含关系 | Topic 02 Extension + Boundary |
| 8 | Bernoulli 重复试验、串并联系统可靠性 | Topic 02 Worked Model；分布标签 Use Topic 03 |
| 9–10 | 七类陷阱、标准流程、结构图 | Boundary + Rules Candidate + Merge |

### P02-B 全概率公式

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1 | 分割、完备事件组、零概率分类、常见隐变量分割 | Topic 02 Core + Boundary |
| 2–3 | 事件分解；有限/二元/可数/条件形式的推导 | Topic 02 Core；可数形式列 Extension |
| 4 | 条件概率加权平均与上下界检查 | Topic 02 Core + Rule Candidate |
| 5 | 概率树；路径相乘、路径相加 | Topic 02 Core Representation |
| 6–7 | 好分割的选择、流程、产品/运输模型 | Topic 02 Method + Worked Examples |
| 8 | 全概率与 Bayes 的前向/反向接口 | Topic 02 Core Bridge |
| 9–11 | 边界、错误、公式索引、结构图 | Boundary + Merge |

### P02-C 贝叶斯公式

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1–2 | 逆向归因结构、适用条件、由乘法与全概率推导 | Topic 02 Core |
| 3–5 | 先验/似然/证据/后验；概率与赔率形式；二元 Bayes | Topic 02 Core；术语边界需与参数估计似然区分 |
| 6–7 | 基础率、自然频数、医学检测、质量追溯 | Topic 02 Worked Models + Boundary |
| 8 | 全概率生成证据、Bayes 重分配来源权重 | Topic 02 Core Compression |
| 9–12 | 流程、错误、公式与结构图 | Rules Candidate + Boundary + Merge |

### P03-A 一维随机变量

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1 | 随机变量；CDF；端点；分位数；分布类型；圆盘距离示例 | Topic 03 Core + Boundary |
| 2 | PMF；常见离散分布；参数/生成条件；分布联系；二项众数 | Topic 03 Core，数字特征只列接口 Use Topic 05 |
| 3–4 | PDF；概率/CDF；均匀、指数、正态及标准化结论 | Topic 03 Core |
| 5 | MGF 及常见分布 MGF | Topic 03 Extension；可加性调用 Topic 04 |
| 6 | 概率积分变换 | Topic 03 Extension/Bridge Note |
| 7–8 | 离散—连续分层；混合密度；缩放/仿射；密度乘积辨析 | Topic 03 Boundary；变换机制由 Topic 04 Own |
| 9–10 | CDF 法、密度变换、常值区间点质量、非单调多原像 | Topic 04 Core，Topic 03 只留路由 |
| 11–14 | 模型选择、检查、错误、公式、结构图 | Rules Candidate + Boundary + Merge |

### P03-B 随机变量与事件构造

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1–2 | 随机变量事件原像；CDF 端点公式 | Topic 03 Core，与 P03-A 合并 |
| 3 | 最大/最小事件恒等式、对偶 | Topic 03 Core Representation |
| 4–5 | 一般联合情形；独立乘积分解；i.i.d. 特例 | Topic 04 Own 联合依赖；Topic 03 留事件入口 |
| 6–7 | 顺序关系检查；均匀/指数极值模型 | Topic 07 Own 顺序统计量；Topic 03 留生成示例 |
| 8 | 系统可靠性 | Use Topic 02，不重复定义 |
| 9–12 | 触发信号、流程、检查、错误、公式、图 | Rules Candidate + Boundary + Merge |

### P04-A 多维随机变量

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1–3 | 随机向量、联合 CDF/PMF/PDF、边缘、条件及互相转换 | Topic 04 Core |
| 4 | 分层模型、Poisson 稀疏化、混合指数、条件均匀 | Topic 04 Core Worked Models；全概率 Use Topic 02 |
| 5 | 随机变量独立；等价表示；支撑集可分离性 | Topic 04 Core + Boundary |
| 6 | 二维正态、线性组合、条件正态、独立与不相关 | Topic 04 Core；不相关定义 Use Topic 05 |
| 7 | 条件期望、迭代期望、全方差、协方差、相关、关系辨析 | Topic 05 Own；Topic 04 只留依赖接口 |
| 8 | 离散—离散、连续—连续、混合型二维概率计算 | Topic 04 Core |
| 9–10 | CDF、Jacobian、常用变换、离散函数分布 | Topic 04 Core；特殊函数入口列 Extension |
| 11 | 极值、第 $k$ 顺序量、联合密度、指数间距 | Topic 07 Own；Topic 04 留联合变换接口 |
| 12 | 重要分布接口 | 按语义分别 Use Topic 03/05/07 |
| 13–16 | 边界、模型选择、检查、公式、结构图 | Boundary + Rules Candidate + Merge |

### P04-B 随机变量的函数与分布可加性

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1–2 | 卷积封闭；连续卷积；MGF/PGF/CF；工具选择 | Topic 04 Core + Extension（PGF/CF） |
| 3 | Gamma 加性；指数/Erlang/$\chi^2$；Poisson 计数—等待；亚指数 | Topic 04 Extension；$\chi^2$ 推断身份 Use Topic 07 |
| 4 | 负二项、几何、离散—连续类比 | Topic 04 Extension，分布定义 Use Topic 03 |
| 5 | 二项、Poisson、正态的独立可加性 | Topic 04 Core |
| 6 | Cauchy 重尾、可加稳定性、正态比值、稳定分布 | Topic 04 Extension + Topic 05 existence Boundary |
| 7 | 分布构造关系与家族图 | Topic 04 Integration Map，不复制各分布定义 |
| 8–10 | 应用、流程、一致性、错误、公式 | Rules Candidate + Boundary + Merge |

### P05-A 数字特征

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1 | 数字特征作为有损压缩及分类 | Topic 05 Core Mother Model |
| 2 | 期望定义/存在性；LOTUS；线性；指示变量；尾和/尾积分 | Topic 05 Core + Extension（尾公式） |
| 3 | 原点矩/中心矩/绝对矩；存在层级；偏度/峰度 | Topic 05 Core + Extension |
| 4 | 方差、性质、均值最小二乘、标准化、变异系数 | Topic 05 Core + Extension |
| 5 | 协方差、相关、独立/不相关、协方差矩阵 | Topic 05 Core；矩阵形式列 Extension |
| 6 | 条件期望、迭代期望、全方差、全协方差 | Topic 05 Core + Extension |
| 7 | Cauchy–Schwarz、Jensen、Markov、Chebyshev、Cantelli | Topic 05 Core/Extension；极限定理 Use Topic 06 |
| 8 | 常见分布数字特征 | Topic 05 Reference Table，分布生成语义 Use Topic 03 |
| 9 | 样本数字特征接口 | Use Topic 07 |
| 10–13 | 触发、流程、错误、公式、结构图 | Rules Candidate + Boundary + Merge |

### P06-A 概率极限定理

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1 | 极限定理回答稳定位置与剩余波动 | Topic 06 Core Mother Model |
| 2 | a.s./概率/$L^p$/分布收敛；蕴含关系；连续映射 | Topic 06 Core + Extension，反向不成立保留反例 |
| 3 | Borel–Cantelli 两引理 | Topic 06 Extension |
| 4 | Chebyshev/Khinchin 弱 LLN；Kolmogorov 强 LLN；非同分布；Bernoulli 频率 | Topic 06 Core + Extension |
| 5 | 样本矩/样本方差相合；EDF | Topic 06 Mechanism，统计对象 Use Topic 07/08 |
| 6 | Lindeberg–Lévy、De Moivre–Laplace、Lyapunov、Lindeberg、Berry–Esseen | Topic 06 Core + Extension；误差界不得伪装考研必备 |
| 7–9 | Slutsky、Student 化、Delta、一二阶、$o_P/O_P$ | Topic 06 Extension；作为渐近推断接口 |
| 10–11 | 均值/比例/方差/插件估计接口；精确与渐近分流 | Topic 06 Boundary + Use Topic 07/08 |
| 12–16 | 定理选择、Cauchy/无限方差/依赖/矩不收敛反例、错误、公式、图 | Boundary + Rules Candidate + Merge |

### P07-A 数理统计基本概念

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1–3 | 总体两种表述；有限/无限；i.i.d. 样本；随机/观测二重性；联合分布；参数/统计量/估计量/估计值 | Topic 07 Core |
| 4 | 样本均值、样本矩、$S^2/B_2$；平方和；期望/方差/无偏；正态结构 | Topic 07 Core；评价术语 Use Topic 08 |
| 5 | 顺序统计量、极值、第 $k$ 个、Beta 变换 | Topic 07 Core + Extension |
| 6 | 随机/观测 EDF；固定点 Binomial；收敛；样本矩 | Topic 07 Extension，收敛证明 Use Topic 06 |
| 7–10 | 关系、触发、错误、公式、结构图 | Rules Candidate + Boundary + Merge |

### P07-B 抽样分布

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1 | 抽样分布；精确与渐近 | Topic 07 Core Boundary |
| 2–5 | $\chi^2,t,F$ 的构造、密度、性质、数字特征、上分位点关系 | Topic 07 Core；密度细节/高阶矩列 Extension |
| 6 | 单正态总体均值；Cochran 平方和分解；$t$ 统计量 | Topic 07 Core |
| 7 | 双总体均值差、方差比、合并方差 $t$、Welch、配对接口 | Topic 07 Core + Extension（按数学一范围分层） |
| 8 | 自由度与正交分解 | Topic 07 Core Mechanism |
| 9 | LLN/CLT 与近似 | Use Topic 06；Topic 07 保留选择接口 |
| 10–13 | 汇总、题型识别、检查、错误、结构图 | Rules Candidate + Boundary + Merge |

### P07-C 常用统计量的数字特征

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1–2 | 假设条件；$\bar X$ 的期望、方差、标准误与分布 | Topic 07 Core；期望规则 Use Topic 05 |
| 3–5 | 平方和分解；$S^2$ 无偏与 $n-1$；一般总体方差；$B_2$ 与 $S^2$ | Topic 07 Core + Extension |
| 6 | 正态总体平方和与推断接口 | Topic 07 Core，与 P07-B 合并 |
| 7 | 二元总体样本均值协方差与相关 | Topic 07 Extension；总体协方差 Use Topic 05 |
| 8–11 | 题型、检查、错误、公式、结构图 | Rules Candidate + Boundary + Merge |

### P08-A 点估计

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1–2 | 参数/估计量/估计值；评价标准入口 | Topic 08 Core；详细评价与 P08-B 合并 |
| 3 | 矩估计：矩匹配、单/双参数、$B_2$、特点 | Topic 08 Core |
| 4–7 | 似然/对数似然；支撑是否含参；固定支撑求导；边界型 MLE；Bernoulli/正态/均匀模型 | Topic 08 Core + Boundary |
| 8 | MLE 不变性，一一与非一一变换 | Topic 08 Core + Boundary |
| 9–12 | 常见模型对照；充分统计量；MOM/MLE 比较；典型例题 | Topic 08 Core + Extension（充分性） |
| 13–16 | 流程、错误、公式、结构图 | Rules Candidate + Boundary + Merge |

### P08-B 估计量的评价标准

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1–4 | 评价层次；偏差/无偏；线性修正；方差/MSE/偏差方差分解；有效性/效率/UMVU | Topic 08 Core + Extension（UMVU） |
| 5 | 得分、Fisher 信息、Cramér–Rao、正则条件、达到下界 | Topic 08 Extension；保留正则性失败边界 |
| 6 | Rao–Blackwell、Lehmann–Scheffé、最优性工具 | Topic 08 Extension |
| 7 | 弱/强相合；LLN/连续映射/MSE/Chebyshev 证明 | Topic 08 Core + Extension；定理 Use Topic 06 |
| 8 | 渐近正态、渐近偏差、渐近效率 | Topic 08 Extension，机制 Use Topic 06 |
| 9–10 | 标准间非蕴含关系；正态总体结论 | Topic 08 Boundary + Reference |
| 11–14 | 判断/比较/证明流程、错误、公式、结构图 | Rules Candidate + Boundary + Merge |

### P08-C 区间估计

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1–4 | 随机区间、覆盖率、频率解释、长度；分位数；枢轴法；尾分配；精确/近似/保守 | Topic 08 Core + Boundary |
| 5–6 | 单正态总体均值、方差、标准差区间，已知/未知条件分流 | Topic 08 Core |
| 7–10 | 双总体均值差、Welch、配对、方差比及速查 | Topic 08 Core + Extension（按范围分层） |
| 11 | 单侧置信限 | Topic 08 Core/Extension |
| 12 | Wald、比例、Bootstrap | Topic 08 Extension |
| 13 | 区间与检验对偶 | Topic 08 Core Integration |
| 14 | 区间长度、样本量、精度因素 | Topic 08 Extension/Method |
| 15–18 | 构造流程、错误、公式、结构图 | Rules Candidate + Boundary + Merge |

### P08-D 假设检验

| 源章节 | 语义内容 | 去向与角色 |
|---|---|---|
| 1–4 | 假设、等号归属、统计量/拒绝域、小概率原理、两类错误、尺寸/功效、方向、一般流程 | Topic 08 Core + Boundary |
| 5–10 | 单/双正态总体的均值、方差、合并方差、Welch、配对、方差比检验 | Topic 08 Core + Extension（按范围分层） |
| 11 | p 值定义、尾部和决策 | Topic 08 Core |
| 12 | 检验与置信区间对偶 | Topic 08 Core Integration |
| 13 | 功效函数、样本量、统计/实际显著 | Topic 08 Extension + Boundary |
| 14–15 | Neyman–Pearson、似然比、广义似然比、多重检验 | Topic 08 Extension |
| 16 | “拒绝”与“不拒绝”的合格表述 | Topic 08 Core Boundary + Rule Candidate |
| 17–20 | 模型识别、模板、检查、错误、公式、结构图 | Rules Candidate + Boundary + Merge |

## 4. 八本手册的重构蓝图

| Topic | 母问题 | 章节推进（不是源笔记顺序） | Stop Boundary |
|---|---|---|---|
| 01 随机世界 | 一次随机试验怎样成为可计算的概率模型？ | 记录协议 → $\Omega$ → 事件代数 → 概率测度 → 均匀模型 → 概率界与连续性 → 建模校验 | 条件化交给 02；数值观察交给 03 |
| 02 信息更新 | 新信息怎样限制世界、分解来源并反推原因？ | 条件化 → 路径乘法 → 分割/全概率 → Bayes 反演 → 独立性 → 条件独立/关联边界 → 可靠性模型 | 随机变量联合独立交给 04；似然估计交给 08 |
| 03 一维观察 | 怎样把随机世界压到数轴并完整描述质量？ | 观察函数/原像 → CDF 统一语言 → 离散/连续/混合 → 分布生成机制 → 端点/分位数 → 极值事件 → 表示校验 | 一维/多维函数变换交给 04；数字摘要交给 05 |
| 04 多维与变换 | 多维质量怎样表达依赖，并在映射下守恒搬运？ | 联合几何 → 边缘/条件 → 独立 → 分层生成 → 变换原像/Jacobian → 卷积 → 可加族与生成函数 → 二维正态 | 数字依赖摘要交给 05；顺序统计推断身份交给 07 |
| 05 数字特征 | 如何有意识地压缩分布，并知道压缩丢了什么？ | 期望/存在性 → LOTUS/指示变量 → 矩与形状 → 方差/最小二乘 → 协方差/相关 → 条件期望分解 → 不等式与边界 | 样本统计量交给 07；收敛交给 06 |
| 06 极限定理 | 大量重复为何同时产生稳定值和可描述的剩余波动？ | 收敛语言 → LLN → CLT → 精确/渐近分流 → Slutsky/Delta → 统计接口 → 重尾/依赖反例 | 统计量对象交给 07；推断程序交给 08 |
| 07 抽样世界 | 从总体复制出的样本函数为何有自己的分布？ | 总体/样本二重性 → 统计量 → 样本矩/平方和 → 自由度几何 → $\chi^2,t,F$ → 单/双总体结构 → 顺序量/EDF → 精确与渐近路由 | 估计与检验决策交给 08 |
| 08 统计推断 | 如何用抽样分布控制从数据反推参数时的错误？ | 逆问题 → 点估计生成 → 估计量评价 → 枢轴反演/区间 → 检验与两类错误 → CI 对偶 → 功效 → 高阶最优性扩展 | 概率生成机制回到 03/04；渐近合法性回到 06 |

## 5. 跨册冲突的唯一 Owner 决议

| 冲突 | 唯一 Owner | 其他位置保留什么 |
|---|---|---|
| 事件独立 vs 随机变量独立 | Topic 02 owns 事件层；Topic 04 owns 随机变量/联合分布层 | 双方互相给出定义接口，不复制完整推导 |
| 变量函数分布 | Topic 04 | Topic 03 只说明从一维分布路由到变换问题 |
| 极值事件 vs 顺序统计量 | Topic 03 owns 事件翻译；Topic 07 owns 样本顺序统计量分布 | Topic 04 提供联合变换工具 |
| 条件期望/协方差 | Topic 05 | Topic 04 只解释其如何从联合/条件分布计算 |
| $\chi^2,t,F$ | Topic 07 | Topic 03/04 仅保留分布构造关系，Topic 08 调用其分位点 |
| 常用统计量数字特征 | Topic 07 | Topic 05 只拥有一般随机变量数字特征定理 |
| LLN/CLT | Topic 06 | Topic 07/08 只保留抽样或推断调用条件 |
| 似然 | Topic 08 | Topic 02 的 Bayes 只定义“给定来源时证据概率”，不得混成似然函数优化 |
| 无偏性/相合性 | Topic 08 | Topic 07 可陈述 $S^2$ 的性质，但评价框架由 08 解释 |

## 6. Rules 候选池（尚未晋升）

以下只是从旧笔记抽出的动作候选，均需真题/错题证据验证：

1. 先写“记录什么”，再写样本空间；检查互斥与穷尽。
2. 古典概型先证明有限、等可能，再计数。
3. 自然语言事件先做集合翻译，再做概率计算。
4. 看到“来源分类后发生结果”，先建分割并沿路径相乘、跨路径相加。
5. 看到“已知结果反问来源”，分母先用全概率生成，再做 Bayes 归一化。
6. 独立不能凭直觉；至少检查联合量是否分解为边缘乘积。
7. 随机变量题先写对象、支撑与目标表示（CDF/PMF/PDF/数字特征）。
8. 端点有原子时，用左右极限而不是连续型习惯替代。
9. 变量变换先求目标事件原像；非单调时枚举全部原像分支。
10. 二维积分、边缘化、条件化和 Jacobian 前先画支撑集。
11. 求和分布先核验独立与参数兼容，再用卷积或可加族。
12. 只求数字特征时，先检查 LOTUS、线性、指示变量和条件分解，避免求完整分布。
13. 展开和的方差时先写协方差项，再用独立/不相关证据删项。
14. 先区分“趋向常数”还是“标准化误差的分布”，再选 LLN 或 CLT。
15. 先判精确分布还是渐近近似；有限样本条件不足时不得套 $t/\chi^2/F$。
16. 统计推断先区分参数、估计量、估计值与统计量。
17. MLE 先写联合似然和参数可行域；支撑含参时先做边界优化，再考虑求导。
18. 区间估计先找分布不含未知参数的枢轴量，再反演不等式。
19. 假设检验由 $H_1$ 决定尾部；拒绝域概率在 $H_0$ 下校准。
20. “不拒绝 $H_0$”不得写成“证明/接受 $H_0$”。

## 7. 完成判据

每册只有同时满足下列条件才允许从“结构草稿”升级：

- 本表对应源章节全部核销，且 Core/Boundary/Extension/Use 去向可追踪；
- 主体按母问题重写，不沿源文件目录机械串联；
- 每个核心结论都有对象、前提、推导或解释、反例/失效条件、Worked Example 与恢复线索；
- 重复定义已收敛到唯一 Owner，跨册只保留最小接口；
- 动作性内容进入 Rules 候选，不在 Handbook 中堆成应试口令；
- 数学公式、参数化、支撑集、端点与自由度完成专项校验；
- Canonical `.tex` 编译成功，Landing 状态与物理资产一致；
- `progress --write`、`check`、`audit` 通过或债务已明确记录。

## 8. 当前事实与待验证判断

**仓库事实：**Topic 01 已按 P01-A/P01-B 重写为 8 页 Canonical 工作稿并通过 `publish`；Topic 02 已按 P02-A/P02-B/P02-C 重写为 6 页，Topic 03 已按 P03-A/P03-B 重写为 8 页，Topic 04 已按 P04-A/P04-B 重写为 6 页，Topic 05 已按 P05-A 重写为 8 页，Topic 06 已按 P06-A 重写为 6 页，Topic 07 已按 P07-A/P07-B/P07-C 重写为 6 页，Topic 08 已按 P08-A/P08-B/P08-C/P08-D 重写为 9 页，均通过 `publish`。已发布 PDF 仍是工作稿，不能替代人工确认。  
**设计判断：**八 Topic 拆分可以承接全部源知识，但 Topic 03/04、04/05、05/07、06/07/08 的边界必须按上表收紧。  
**尚未确认：**Atlas 中“随机世界 / 观察函数 / 信息操作”是否作为长期一级术语，仍保持待人工确认，不因本次导入自动晋升。

## 9. 执行核销

| Topic | Source | 核销结果 | 发布 | 剩余检查 |
|---|---|---|---|---|
| 01 | P01-A、P01-B | 已覆盖记录粒度、事件域、特殊事件、完整事件代数、自然语言量词、公理推导、古典/几何模型、概率界与概率连续性；重复速查和结构图已重组 | 8 页，`publish` 通过 | 与 Topic 02 的完备事件组/独立边界；人工术语确认 |
| 02 | P02-A、P02-B、P02-C | 已覆盖条件测度、乘法链、完备分割、全概率、Bayes 概率/赔率形式、基础率、两两/相互独立、关联、条件独立、Bernoulli 与可靠性及错误边界 | 6 页，`publish` 通过 | Topic 01 分割接口；Topic 04 条件分布接口；人工术语确认 |
| 03 | P03-A、P03-B | 已覆盖观察函数、CDF/端点/分位数、离散/连续/混合型、常见分布生成机制、MGF、概率积分变换、极值事件、原像变换、多分支/点质量、分层计算与密度合法性 | 8 页，`publish` 通过 | Topic 04 变换/联合边界；Topic 07 顺序统计量边界；人工术语确认 |
| 04 | P04-A、P04-B | 已覆盖联合 CDF/PMF/PDF、支撑集、边缘/条件分布、分层生成、独立性边界、二维正态、CDF/Jacobian 变换、一般/独立卷积、可加分布族与极值接口 | 6 页，`publish` 通过 | Topic 05 条件数字特征；Topic 07 顺序统计量；人工参数化确认 |
| 05 | P05-A | 已覆盖期望存在性、LOTUS、示性变量、尾和/尾积分、矩存在层级、偏度峰度、方差最小二乘、标准化/CV、协方差相关、协方差矩阵、条件期望、全期望/全方差/全协方差、Cauchy--Schwarz/Jensen/Markov/Chebyshev/Cantelli 与统计接口 | 8 页，`publish` 通过 | Topic 06 不等式调用；Topic 07 样本数字特征；人工术语确认 |
| 06 | P06-A | 已覆盖收敛方式与蕴含边界、连续映射、Borel--Cantelli、弱/强大数律、样本矩/方差/经验分布相合性、经典与非同分布 CLT、De Moivre--Laplace、Lyapunov/Lindeberg/Berry--Esseen、Slutsky、Student 化、Delta、$o_P/O_P$、精确/渐近分流与重尾/依赖反例 | 6 页，`publish` 通过 | Topic 07 抽样分布；Topic 08 渐近推断；人工术语确认 |
| 07 | P07-A、P07-B、P07-C | 已覆盖总体/样本二重性、i.i.d. 与联合分布、统计量/估计量/估计值、样本矩与 $B_2/S^2$、顺序统计量、EDF、$\chi^2/t/F$ 生成与分位点、正态正交分解、单双总体/配对、自由度、精确/渐近分流与边界 | 6 页，`publish` 通过 | Topic 08 推断调用；人工自由度/分位点确认 |
| 08 | P08-A、P08-B、P08-C、P08-D | 已覆盖矩估计、MLE 固定/参数相关支撑与不变性、充分统计量、偏差/方差/MSE/效率/CR/Rao--Blackwell/Lehmann--Scheffé、相合与渐近正态、枢轴区间、单/双总体与配对区间、检验方向/两类错误/功效/p 值、区间检验对偶、Neyman--Pearson、多重检验及结论边界 | 9 页，`publish` 通过 | 与 Topic 06/07 抽样接口；人工术语确认 |
