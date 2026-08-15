# 数学一认知体系总架构

> 类型：Atlas
> 状态：已采用；README 是 Canonical Course / Exam Atlas，Subject Topic / Bridge / Integration 正文分阶段建设中。

## 0. 系统目标

数学一不是按教材目录重新整理知识，而是建立：

$$
\boxed{
\text{可理解}+\text{可生成}+\text{可调用}+\text{可迁移}+\text{可更新}
}
$$

的认知系统。

本目录是数学一的 **Course / Exam Atlas**。它只负责三门 Subject 的地图、共享 Control Language、跨学科 Bridge 与 Integration；不强迫高数、线代、概率共享一个万能世界模型。

数学一沿三层运行：

$$
\boxed{\text{Knowledge Plane}+\text{Control Plane}+\text{Learning Plane}}
$$

其中 Knowledge Plane 使用：

$$
\boxed{\text{Subject Atlas}\rightarrow\text{Topic}\rightarrow\text{Bridge}\rightarrow\text{Integration}}
$$

- Topic = Depth：打穿单个机制；
- Bridge = Interface：解释两个 Owner 为什么能接；
- Integration = Composition：让多个成熟模块共同解决完整问题。

## 1. 三个 Subject Atlas

### 1.1 [高等数学](10_高等数学/README.md)

母问题：变化怎样被极限定义、被局部模型描述、被连续累积，并怎样由局部规律恢复整体行为。

$$
\boxed{
\text{Limit}+\text{Local Model}+\text{Accumulation}+\text{Local}\leftrightarrow\text{Global}+\text{Infinite Construction}+\text{Dynamics}
}
$$

### 1.2 [线性代数](20_线性代数/线性代数%20Subject%20Atlas：空间、映射、表示与不变量.md)

母问题：面对线性空间中的对象，怎样区分对象与坐标表示，选择不改变当前问题本质的表示变换，并从不变量读出结构？

贯穿阅读协议：

$$
\boxed{\text{Object}\rightarrow\text{Representation}\rightarrow\text{Allowed Transform}\rightarrow\text{Invariant}\rightarrow\text{Simplest Valid Form}}
$$

最后一步指“当前关系允许的最简表示”，不意味着所有矩阵都能对角化。

### 1.3 [概率论与数理统计](30_概率论/README.md)

概率研究正向生成：

$$
\boxed{\text{Model}\rightarrow\text{Random Data}}
$$

统计研究逆向推断：

$$
\boxed{\text{Observed Data}\rightarrow\text{Information about Model}}
$$

世界模型：

$$
\boxed{\text{Random Object}+\text{Distribution}+\text{Information}+\text{Sampling}+\text{Inference}}
$$

## 2. Topic / Bridge / Integration 契约

### Topic

Topic 是单一核心机制的 Canonical Owner。默认生成链：

$$
\boxed{\text{Problem}\rightarrow\text{Naive Approach}\rightarrow\text{Failure}\rightarrow\text{Mechanism}\rightarrow\text{Invariant}\rightarrow\text{Cost}}
$$

### Bridge

Bridge 只在存在真实、稳定、可复用的共享机制时建立：

$$
\boxed{A\text{ 输出什么}\rightarrow\text{怎样翻译}\rightarrow B\text{ 怎样接收}}
$$

判断口诀：

$$
\boxed{\text{Bridge}=\text{两个模块为什么能接}}
$$

### Integration

Integration 不创造接口，只选择一个 Canonical Problem，让多个已有 Topic / Bridge 按顺序协作：

$$
\boxed{\text{Problem}\rightarrow\text{Module Recognition}\rightarrow\text{Module Composition}\rightarrow\text{Execution}\rightarrow\text{Verification}}
$$

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

依赖主干：

$$
B00\rightarrow\{B04,B08\},
\qquad
B01\rightarrow\{B02,B03,B04\},
$$

$$
B06A\rightarrow B06B,
\qquad
B02+B06\rightarrow B07.
$$

B05 相对独立。

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

三门学科共享一个控制镜头，但不共享本体：

$$
\boxed{
\text{Object}\rightarrow\text{Goal}\rightarrow\text{Structure}\rightarrow\text{Representation}\rightarrow\text{Transformation}\rightarrow\text{Invariant}\rightarrow\text{Execute}\rightarrow\text{Verify}
}
$$

具体动作由 [90_学科做题规则](90_学科做题规则/README.md) 维护。

### 高数 Adapter

$$
\text{Object}\rightarrow\text{Target}\rightarrow\text{Model}\rightarrow\text{Representation}\rightarrow\text{Structure}\rightarrow\text{Route}\rightarrow\text{Execute}\rightarrow\text{Verify}
$$

优先判断：局部化、累积、局部—整体、无限过程还是动态恢复？

### 线代 Adapter

$$
\text{Object}\rightarrow\text{Space}\rightarrow\text{Representation}\rightarrow\text{Allowed Transform}\rightarrow\text{Invariant}\rightarrow\text{Simplest Valid Form}
$$

首问：当前矩阵到底代表什么对象？

### 概率统计 Adapter

$$
\text{Target}\rightarrow\text{Random Object}\rightarrow\text{Information}\rightarrow\text{Representation}\rightarrow\text{Operation}\rightarrow\text{Route}\rightarrow\text{Compute}\rightarrow\text{Verify}
$$

优先判断：Condition、Marginalize、Transform、Approximate 还是 Infer？

## 7. Learning Plane 与更新路由

学习循环：

$$
\boxed{\text{Observation}\rightarrow\text{Diagnosis}\rightarrow\text{Hypothesis}\rightarrow\text{Candidate Rule}\rightarrow\text{Test}\rightarrow\text{Promote/Revise/Reject}}
$$

日常仍使用系统统一的五类诊断，不新增复杂标签树。若判断为“模型问题”，稳定更新前再定位：

- Topic mechanism 错误 → 修改对应 Topic；
- Bridge interface 错误 → 修改对应 Bridge；
- Integration composition 错误 → 修改 Integration 或综合训练；
- 识别/路径错误 → Subject Rules；
- 执行/检查/表达错误 → Subject Rules；
- 时间/退出/返回/风险错误 → Exam Control。

核心维护原则：

> 不是每遇到一道新题就增加知识节点。先判断它是在深化 Topic、暴露 Bridge、需要 Integration，还是只产生一条 Control Rule。

## 8. 模块状态与发布

| 模块 | Canonical 入口 | 当前正文 / 发布状态 |
|---|---|---|
| 高等数学 | [10_高等数学](10_高等数学/README.md) | Subject Atlas 已采用；Topic01–12、H-B01–H-B05、H-I01 均已建立 Canonical `.tex` 候选正文并按需发布 |
| 线性代数 | [20_线性代数](20_线性代数/线性代数%20Subject%20Atlas：空间、映射、表示与不变量.md) | Subject Atlas 为 Canonical Map；Topic01–06 已建立并发布 Canonical `.tex` 候选正文，当前待人工确认 |
| 概率论与数理统计 | [30_概率论](30_概率论/README.md) | Subject Atlas 为 Canonical Map；Topic01–08 已建立 Canonical `.tex` 工作稿，Published View 依当前 TeX 环境逐步同步 |
| Cross-Subject Bridge | [50_桥梁专题](50_桥梁专题/README.md) | B00–B08 已建立 Canonical 工作稿并按需发布 |
| Integration | [60_综合专题](60_综合专题/README.md) | 作为跨模块组合层按成熟 Owner 逐步建立 |
| Control Rules | [90_学科做题规则](90_学科做题规则/README.md) | Markdown Control Rules；候选规则必须经真题/陌生题验证后再升级 |

历史 v2 总图及其旧 PDF 仅作为已完成 Source Diff 的 Git 历史，不再参与当前导航、Ownership、状态判断或发布判断。Atlas 是否 Canonical 只由当前 Atlas Owner 决定，Topic / Bridge / Integration 的正文状态只由当前 Canonical `.tex` 与 Landing Page 决定。

## 9. 当前建设顺序

1. 先完成本次数学一 Course Atlas、Core Bridge Atlas 与 Integration 骨架；
2. 高数按 Source Corpus → Topic / internal Bridge / Rules 的方式逐册重构；
3. Cross-Subject Bridge 只在两侧 Topic 已有足够稳定模型后补正文；
4. Integration 最后作为迁移验收层建设，不提前重讲基础理论；
5. 使用陌生题攻击 Control Rules，并让真实错题决定系统下一次更新位置。
