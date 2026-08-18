# 数学一认知体系总架构

> 类型：Atlas
> 状态：已采用；README 是 Canonical Course / Exam Atlas，Subject Topic / Bridge / Integration 正文分阶段建设中。

## 0. 系统目标

数学一不是按教材目录重新整理知识，而是建立一个能够支持**理解、生成、调用、迁移和更新**的认知系统。

本目录是数学一的 **Course / Exam Atlas**。它只负责三门 Subject 的地图、共享 Control Language、跨学科 Bridge 与 Integration；不强迫高数、线代、概率共享一个万能世界模型。

系统区分三个责任平面：Knowledge Plane 维护稳定数学模型，Control Plane 维护问题识别与执行控制，Learning Plane 用新题、错题与反例检验前两者。三者是职责划分，不是一条先后流水线。

Knowledge Plane 又包含四种不同解释责任：

- **Subject Atlas**：建立学科坐标系与 Owner 地图；
- **Topic / Depth**：完整解释单个机制；
- **Bridge / Interface**：解释两个 Owner 的稳定接口；
- **Integration / Composition**：追踪多个成熟模块怎样共同完成一个完整问题。

它们是产品类型与依赖关系，不默认构成“Atlas、Topic、Bridge、Integration 必须依次学习”的线性顺序。

## 1. 三个 Subject Atlas

### 1.1 [高等数学](10_高等数学/README.md)

母问题：怎样用极限刻画逼近与连续变化，建立局部模型、累积局部贡献，并在适当条件下由局部信息恢复整体性质或整体轨迹？

Subject Atlas 用六个生成坐标组织全科：Limit、Local Model、Accumulation、Local–Global、Infinite Construction、Dynamics；每一项的正式关系与成立条件见高数 Atlas，不在 Course Atlas 重复证明。

### 1.2 [线性代数](20_线性代数/README.md)

母问题：面对线性空间中的对象，怎样区分对象与坐标表示，选择不改变当前问题本质的表示变换，并从不变量读出结构？

贯穿模型使用五个坐标：Object、Representation、Allowed Transform、Invariant、Simplest Valid Form。先由对象与任务确定合法变换类，再只在该合法表示类中读取不变量与化简；这里是结构关系，不是一条逻辑蕴含链。

### 1.3 [概率论与数理统计](30_概率论/README.md)

概率论固定概率模型，研究随机对象及其分布怎样生成数据；数理统计观察有限样本后，研究这些数据能约束模型或未知参数到什么程度。前者是生成方向，后者是推断方向，统计并不是把概率模型做普通函数求逆。

Subject Atlas 以 Random Object、Distribution、Information Operation、Sampling、Inference 五类对象/操作组织全科。

## 2. Topic / Bridge / Integration 契约

### Topic

Topic 是单一核心机制的 Canonical Owner。机制叙事至少回答：原问题是什么；朴素方案为何不足；新机制解决了什么限制；它保持什么不变量；付出什么成本。这个次序服务解释，不自动构成逻辑蕴含。

### Bridge

Bridge 只在存在真实、稳定、可复用的共享机制时建立，并必须明确三项接口：A 输出什么、经过什么翻译/共享结构、B 接收什么。若需要画箭头，必须给接口关系加标签，而不是用裸箭头代替解释。

判断口诀：

$$
\boxed{\text{Bridge}=\text{两个模块为什么能接}}
$$

### Integration

Integration 不创造接口，只选择一个 Canonical Problem，明确需要哪些已有 Topic / Bridge、它们按什么条件与事件协作、怎样执行以及怎样独立验证。这里拥有的是组合过程，不重新拥有局部机制。

判断口诀：

$$
\boxed{\text{Integration}=\text{多个模块怎样一起工作}}
$$

详细判别与写作契约见 `00_system/handbook_contract.md`。

## 3. Core Bridge Atlas

跨三门 Subject 的稳定接口统一由 [50_桥梁专题](50_桥梁专题/README.md) 拥有。

当前架构：

| ID | Bridge | 核心接口 |
|---|---|---|
| B00 | 内积、正交与投影 | 空间几何 ↔ 线性代数 |
| B01 | 局部线性化 | 微分 ↔ 线性映射 |
| B02 | Jacobian 与行列式 | 坐标变换 ↔ 局部面积/体积缩放 |
| B03 | Hessian 与二次型 | 二阶局部形状 ↔ 正定性 |
| B04 | 梯度、正交与 Lagrange | 约束极值 ↔ 切空间/法空间 |
| B05 | 线性方程与线性微分方程 | 非齐次解 = 特解 + Kernel |
| B06A | PDF 与 CDF | 局部概率密度 ↔ 累积函数 |
| B06B | 期望、联合概率与边缘化 | 概率权重/联合质量 ↔ 积分累积 |
| B07 | 随机变量变换与 Jacobian | 坐标重表达 ↔ 概率质量守恒 |
| B08 | Fourier 与正交基 | 函数表示 ↔ 正交投影 |

当前依赖关系：B04、B08 使用 B00 的内积/正交接口；B02、B03、B04 使用 B01 的局部线性化接口；B06B 使用 B06A 的 density–accumulation 接口；B07 同时使用 B02 的 Jacobian 接口与概率侧的分布/质量守恒接口。B05 相对独立。这里的“使用”表示知识依赖，不表示前者逻辑蕴含后者。

## 4. Integration Layer

跨三门 Subject 的组合验收统一由 [60_综合专题](60_综合专题/README.md) 拥有。

当前只预建三个高价值 Canonical Problem：

- I01：二维正态分布——三科汇流验收；
- I02：二维随机变量线性变换——Jacobian、support、联合分布与边缘化协作；
- I03：线性常微分方程组——用于验证 B05 的组合能力；该对象超出数学一核心考纲的部分标记为 Extension，不反向扩张主干。

Integration 不按数量规划。只有完整问题确实能检验多个成熟模块的迁移能力时才新增。

## 5. Extension 与 Anti-Bridge

任何稳定关系进入系统时，除 Own / Use / Bridge / Integrate 外，还允许两种边界角色：

- **Extension**：真连接，但当前不展开；
- **Anti-Bridge**：表面相似但结构不同，必须阻断错误迁移。

它们不是新的 Handbook 类型，不建立平行目录树。

当前数学一优先保留的 Anti-Bridge：

- Probabilistic Independence ≠ Linear Independence；
- Variance ≠ Norm；
- Orthogonality ≠ Probabilistic Independence；只有特定结构（如联合 Gaussian 的额外条件）才能得到更强结论。

典型 Extension：

- 常系数 ODE 特征根 ↔ companion matrix eigenvalue；
- covariance matrix ↔ quadratic form；
- Fourier ↔ Hilbert space；
- generalized Stokes theorem；
- matrix exponential for linear ODE systems。

## 6. Control Plane

三门学科共享一组控制问题，但不共享本体：Object、Goal、Structure、Representation、Transformation、Invariant、Execute、Verify。它们是推荐检查职责；具体顺序可以由学科 Adapter 特化，不能把这组词当成统一数学因果链。

具体动作由 [90_学科做题规则](90_学科做题规则/README.md) 维护。

### 高数 Adapter

推荐检查：Object、Target、Model、Representation、Structure、Route、Execute、Verify。优先判断当前问题是在处理极限/逼近、局部化、累积、局部—整体、无限过程还是动态恢复。

### 线代 Adapter

推荐检查：Object、Space、Representation、Allowed Transform、Invariant、Simplest Valid Form。首问：当前矩阵到底代表什么对象？

### 概率统计 Adapter

推荐检查：Target、Random Object、Information、Representation、Operation、Route、Compute、Verify。优先判断：Condition、Marginalize、Transform、Approximate 还是 Infer？

### 三科共享的逻辑资格审计

本轮旧做题笔记逐章回收暴露出一个跨三科需要反复审计的风险：**把低强度信息越级解释成高强度结论**。因此任何二级结论、速算结论和跨模块迁移，在执行前统一追加四问：当前对象是什么；当前信息是必要、充分还是充要；这一步保留/丢掉了什么；结论是在声称存在、可表示还是可计算？

它用于阻断三类典型错误：

1. **必要条件冒充生成器**：通项趋零不推出级数收敛；偏导存在不推出可微；对角元全正不推出正定；同 rank 不推出同解；
2. **摘要冒充完整对象**：同概率不推出同事件；零协方差不推出独立；同 trace/determinant/特征值摘要不自动推出相似；
3. **存在、表示与计算混同**：反函数存在不等于容易写出闭式；极限候选满足不动点方程不等于序列已收敛；似然内部驻点存在不等于已经找到全局极大值。

这不是新的 Topic 或 Bridge，只是 Control Plane 的共享验收镜头。具体反例、题目信号与第一动作仍由各专题训练 Markdown 承担，跨多个训练专题反复验证后才晋升学科做题规则。

## 7. Learning Plane 与更新路由

学习循环按控制过程依次完成 Observation、Diagnosis、Hypothesis、Candidate Rule、Test，最后根据证据决定 Promote / Revise / Reject。这个顺序描述维护流程，不是知识蕴含。

日常仍使用系统统一的五类诊断，不新增复杂标签树。若判断为“模型问题”，稳定更新前再定位：

- Topic mechanism 错误：修改对应 Topic；
- Bridge interface 错误：修改对应 Bridge；
- Integration composition 错误：修改 Integration 或综合训练；
- 单一问题族的识别/路径/执行/检查错误：回到对应专题训练 Markdown；
- 同一控制动作跨多个训练专题反复出现并经证据验证：进入 Subject Rules；
- 时间/退出/返回/风险错误：进入 Exam Control。

核心维护原则：

> 不是每遇到一道新题就增加知识节点。先判断它是在深化 Topic、暴露 Bridge、需要 Integration，还是只产生一条 Control Rule。

## 8. 模块状态与发布

| 模块 | Canonical 入口 | 当前正文 / 发布状态 |
|---|---|---|
| 高等数学 | [10_高等数学](10_高等数学/README.md) | Subject Atlas 已采用；Topic01–12、H-B01–H-B05、H-I01 均已建立 Canonical `.tex` 候选正文并按需发布 |
| 线性代数 | [20_线性代数](20_线性代数/README.md) | Subject Atlas 为 Canonical Map；Topic01–06 已建立并发布 Canonical `.tex` 候选正文，当前待人工确认 |
| 概率论与数理统计 | [30_概率论](30_概率论/README.md) | Subject Atlas 为 Canonical Map；Topic01–08 已建立 Canonical `.tex` 工作稿，Published View 依当前 TeX 环境逐步同步 |
| Cross-Subject Bridge | [50_桥梁专题](50_桥梁专题/README.md) | B00–B08 已建立 Canonical 工作稿并按需发布 |
| Integration | [60_综合专题](60_综合专题/README.md) | 作为跨模块组合层按成熟 Owner 逐步建立 |
| Control Rules | [90_学科做题规则](90_学科做题规则/README.md) | Markdown Control Rules；候选规则必须经真题/陌生题验证后再升级 |

历史 v2 总图及其旧 PDF 仅作为已完成 Source Diff 的 Git 历史，不再参与当前导航、Ownership、状态判断或发布判断。Atlas 是否 Canonical 只由当前 Atlas Owner 决定，Topic / Bridge / Integration 的正文状态只由当前 Canonical `.tex` 与 Landing Page 决定。

## 9. 当前建设顺序

1. 先完成本次数学一 Course Atlas、Core Bridge Atlas 与 Integration 骨架；
2. 高数从 Source Corpus 做逐项 Diff，再把内容分别路由到 Topic、internal Bridge 与 Rules；
3. Cross-Subject Bridge 只在两侧 Topic 已有足够稳定模型后补正文；
4. Integration 最后作为迁移验收层建设，不提前重讲基础理论；
5. 使用陌生题攻击 Control Rules，并让真实错题决定系统下一次更新位置。
