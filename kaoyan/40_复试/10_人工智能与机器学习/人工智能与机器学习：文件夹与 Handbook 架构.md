# 人工智能与机器学习：文件夹与 Handbook 架构

> 状态：Area Boundary v1 + Leaf Boundary v1 已采用；八个 Core Area 的物理层级、Canonical Scope、Leaf Topic 归属与内部依赖已锁定。深度正文仍按真实学习逐步建立。  
> 责任：规定 AI / ML 这一超大板块的**物理目录层级、Area Atlas、Topic 粒度、内部正文骨架与晋升规则**。不拥有具体算法知识。

## 1. 为什么必须增加 Area Atlas 这一层

AI / ML 的规模明显大于单门考试科目。若直接采用：

```text
Subject Atlas
→ 9 个超大 Topic
```

会迅速出现两个问题：

1. `统计学习与经典机器学习` 会同时吞下 linear / kernel / tree / clustering / transfer 等完全不同的机制；
2. `Deep Learning` 会同时吞下 approximation、backprop、training、CNN、RNN、attention、Transformer 等多套可以独立解释的机制。

所以这里不能把当前 `AI-T01 ... AI-T09` 直接等同于“九本 Handbook”。它们更适合作为 **Area / Mechanism Cluster**。

本项目允许 Atlas 按观察范围分层，因此本板块采用：

```text
Course / Exam Atlas
    ↓
AI Subject Atlas
    ↓
Area Atlas
    ↓
Leaf Topic Handbook
    ↓
Bridge / Integration
```

其中：

- **Subject Atlas**：解释整个人工智能的母问题、能力地图与跨 Area Routing；
- **Area Atlas**：解释某一大片机制内部为什么还要继续切分；
- **Leaf Topic**：真正承担一个可以完整讲清的机制；
- **Bridge**：拥有两个已成熟 Owner 之间的接口；
- **Integration**：追踪多个机制怎样共同完成完整任务。

这层 Area Atlas 是整个大板块可长期扩展而不坍塌的关键。

---

## 2. 顶层物理目录：目录表达 Ownership，Atlas 表达关系图

AI 最大的结构风险不是“文件不够细”，而是试图让一棵目录树同时表达所有分类。这个领域至少同时存在：

```text
能力轴：Search / Reason / Learn / Decide / Generate
表示轴：Symbol / Probability / Vector / Function / Neural Representation
计算轴：Search / Inference / Dynamic Programming / Sampling / Optimization
任务轴：Prediction / Generation / Planning / Control / Perception / Language
研究方向轴：NLP / CV / Robotics / Scientific ML / Learning Theory / ...
```

这些轴互相交叉，不可能被一棵树无损表达。因此固定原则是：

> **物理目录只表达 Canonical Ownership；多视角分类、依赖关系和研究路线全部放在 Atlas 中表达。**

这也是为什么这里不继续增加“应用层 → 方法层 → 数学层 → 模型层”之类的超级嵌套。层级越多不一定越深，反而可能把同一机制拆成多份真相。

建议最终物理结构如下：

```text
40_复试/
└── 10_人工智能/                     # 建议采用后由当前 10_人工智能与机器学习 改名
    ├── README.md                    # AI Subject Atlas，唯一总入口
    ├── 00_领域结构设计依据.md        # 为什么这样切
    ├── 01_文件夹与Handbook架构.md    # 本文件
    │
    ├── 10_问题求解/
    │   └── README.md                # Area Atlas
    ├── 20_知识表示与推理/
    │   └── README.md
    ├── 30_概率推理与不确定性/
    │   └── README.md
    ├── 40_机器学习/
    │   └── README.md
    ├── 50_优化与学习计算/
    │   └── README.md
    ├── 60_深度学习/
    │   └── README.md
    ├── 70_决策_控制与强化学习/
    │   └── README.md
    ├── 80_生成模型/
    │   └── README.md
    │
    ├── 85_跨域桥梁/
    │   └── README.md                # Cross-Area Bridge Atlas
    ├── 90_综合专题/
    │   └── README.md                # Cross-Area Integration Atlas
    └── 95_研究方向/
        └── README.md                # Direction Atlas，只负责纵向研究路由
```

`10_人工智能与机器学习` 这个当前物理名不适合作为长期名称，因为 Machine Learning 已经是 AI 内部的一个 Area。若总目录继续使用这个名字，会在最顶层制造一次“AI 与 ML 并列、下层 ML 又再次出现”的语义重复。正式采用这版拓扑时应改为 `10_人工智能/`。

### 2.1 八个 Area 不是八种“同类东西”

这里的 Area 指 **Canonical Owner Domain**，不是严格分类学意义上的八个平级子学科。它们承担的角色本来就不同：

| Area | 主要角色 | 它拥有的解释责任 |
| ------------------ | --------------- | --------------------------- |
| 问题求解 | 求解机制 | 已知规则下怎样搜索巨大候选空间 |
| 知识表示与推理 | 显式表示 + 推理机制 | 怎样表示事实/规则并合法推出新结论 |
| 概率推理与不确定性 | 不确定表示 + 推断机制 | 怎样表示 belief、吸收 evidence、回答 query |
| 机器学习 | 学习/估计框架 | 怎样由有限经验选择可泛化模型 |
| 优化与学习计算 | 共享计算引擎 | Objective 已知后怎样高效更新参数 |
| 深度学习 | 可学习表示/函数族 | 怎样构造并训练高表达层级函数 |
| 序贯决策、控制与 RL | 长期决策框架 | 行动改变未来时怎样规划或学习 policy |
| 生成模型 | 分布学习 + 采样机制 | 怎样学习生成规律并产生新样本 |

这张表非常关键：**不要从文件夹并列误读成概念并列。** Optimization 可以被 DL、RL、Generative Models 反复调用；Deep Learning 可以成为 RL 和 Generative Models 的函数逼近器；Probability 又会穿过 ML、RL 和 Generative Models。目录只解决“谁 Own”，Atlas 的箭头才解决“谁依赖谁”。

### 2.2 为什么不再增加一个“超级分组层”

可以把八个 Area 再粗分成“推理 / 学习 / 决策 / 生成”四组，但当前不建议物理建这一层。原因是：

- Optimization 同时服务学习、控制和生成，很难只属于“学习组”；
- Probability 同时是推断语言、学习基础和生成基础；
- Deep Learning 同时是模型族、表示机制和多个方向的基础设施；
- Classical Planning 既能从 Search / Symbolic Reasoning 看，也能从 Sequential Decision 看。

所以“四大组”适合作为 **Atlas View**，不适合作为 Canonical 物理父目录。这样既有高层压缩，也不制造错误 Ownership。

### 2.3 最容易重复的内容先锁 Owner

| 内容 | Canonical Owner | 其他位置怎样处理 |
|---|---|---|
| Bayes rule、conditioning、belief update | Area 30 | ML / RL / Generative 只 Use |
| Entropy、Cross Entropy、KL、MI | Area 30 的信息论 Topic | Loss / VAE / LM 解释具体调用，不重定义 |
| MLE / MAP / ERM | Area 40 | Area 30 提供概率语义；Area 50 只负责怎么优化 |
| Gradient Descent / SGD / Adam / Newton | Area 50 | DL / ML 只描述训练时的调用与特殊行为 |
| Automatic Differentiation | Area 50 | Backprop 通过 Bridge 调用 |
| Backpropagation | Area 60 | 不把它写成 optimizer |
| CNN / RNN / Attention / Transformer | Area 60 | CV / NLP Direction 只 Use 并解释任务组合 |
| MDP / Bellman / Value / Policy | Area 70 | Search、Control、RL 关系通过内部 Bridge 表达 |
| Q-learning / Policy Gradient / Actor-Critic | Area 70 | Deep RL 组合 Area 60，不复制网络机制 |
| VAE / GAN / Diffusion / Flow Matching | Area 80 | Probability / DL / Optimization 只提供被调用机制 |
| GPT / Foundation Model / LLM system | Integration / Direction | Transformer 与 autoregressive modeling 分别回到 Area 60 / 80 |
| CV / NLP / Robotics / Scientific ML | `95_研究方向/` | 只组织真实任务如何调用 Core Areas |

这里最重要的不是编号，而是一级目录承担四种责任：

```text
Core Area
Cross-Area Bridge
Integration
Direction
```

NLP、CV、Robotics、Scientific ML、LLM Agents 等不直接和 Probability / Optimization 并列，而从 `95_研究方向/` 进入；完整训练/推理/智能体生命周期则进入 `90_综合专题/`。

---

## 3. 八个 Area 的内部切法

八个 Area 的 **Scope / Stop Boundary 与 Leaf Boundary v1 已锁定**，唯一边界入口分别是各 Area 的 `README.md`。下面只保留同步后的 Leaf Topic 总览与共同观察镜头；若这里与 Area README 出现冲突，以 Area README 的最新 Boundary 为准。Leaf Topic 已有 Canonical 归属，但仍不要求立刻批量建空目录。

### 10｜问题求解

**Area Mother Question**：当规则和目标基本已知，但候选解空间巨大时，怎样系统找到解？

建议 Leaf Topics：

```text
01_状态空间与无信息搜索
02_启发式搜索与A星
03_局部搜索与元启发式
04_对抗搜索与博弈树
05_约束满足问题_CSP
```

共同观察镜头：

```text
State
→ Action / Successor
→ Frontier / Search Tree
→ Evaluation / Heuristic
→ Expansion Policy
→ Completeness / Optimality / Cost
```

### 20｜知识表示与推理

**Area Mother Question**：怎样把事实、关系、规则和世界结构变成可以被机器操作的显式知识？

建议 Leaf Topics：

```text
01_命题逻辑与逻辑智能体
02_一阶逻辑与关系表示
03_Unification_Resolution与自动推理
04_KnowledgeRepresentation_本体与默认推理
05_经典规划与动作模型
```

共同观察镜头：

```text
World
→ Symbolic Representation
→ Semantics
→ Inference Rule
→ Derived Knowledge
→ Soundness / Completeness / Tractability
```

`经典规划` 暂时留在此 Area，拥有 action schema / symbolic planning；涉及 value、长期回报与 stochastic transition 时转入 Area 70。

### 30｜概率推理与不确定性

**Area Mother Question**：当真实状态不可完全知道时，怎样表示信念、吸收证据并完成推断？

建议 Leaf Topics：

```text
01_概率建模_Bayes与条件化
02_多变量分布_条件独立与概率图模型
03_精确推断_变量消元与消息传递
04_近似推断_MonteCarlo_MCMC与变分
05_时序概率模型与状态估计
06_信息论语言_Entropy_CrossEntropy_KL_MI
```

共同观察镜头：

```text
Unknown Quantity
→ Distribution / Factorization
→ Evidence
→ Posterior / Belief Update
→ Query / Prediction
→ Approximation Error / Computational Cost
```

基础概率定义优先 Use 数学一概率 Owner；本 Area只拥有“概率作为 AI 不确定表示与推断”的新增责任。**Given model/parameters + evidence → infer belief** 属于 Area 30；**given data → estimate parameters / choose model / assess generalization** 属于 Area 40。

### 40｜机器学习

**Area Mother Question**：规则无法直接写出时，怎样从有限经验中选择能在新样本上继续工作的模型？

建议 Leaf Topics：

```text
01_学习问题_估计_泛化与模型选择
02_线性预测模型_LinearRegression_Logistic_GLM
03_生成式分类_LDA_QDA_NaiveBayes
04_实例方法_KNN与非参数学习
05_Kernel_SVM与大间隔方法
06_决策树_森林_Bagging与Boosting
07_降维_PCA与经典潜变量表示
08_聚类_KMeans_混合模型与谱方法
09_数据与监督机制_迁移_半监督_自监督_少标签学习
```

共同观察镜头：

```text
Task / Data
→ Hypothesis / Model Family
→ Objective / Estimator
→ Fitting
→ Validation
→ Generalization
→ Prediction / Representation
```

这里必须持续区分：

```text
Task ≠ Model Family ≠ Objective ≠ Optimization Algorithm ≠ Metric
```

### 50｜优化与学习计算

**Area Mother Question**：当目标函数已经明确时，怎样以有限计算得到高质量参数或决策？

建议 Leaf Topics：

```text
01_优化问题_几何与最优性条件
02_一阶方法_GradientDescent与StepSize
03_随机优化_SGD_Momentum_AdaptiveMethods
04_二阶与拟牛顿_Newton_BFGS_TrustRegion
05_约束优化_Lagrange_KKT
06_Proximal_Projected与非光滑优化
07_AutomaticDifferentiation与计算图求导
```

共同观察镜头：

```text
Objective Landscape
→ Local Information
→ Search Direction
→ Step / Update
→ Convergence / Stability
→ Compute / Memory Cost
```

`AutoDiff` 放在本 Area 的原因：它拥有“如何高效得到导数”的计算责任；`Backprop` 在 Area 60 解释神经网络语义，两者通过 Bridge 连接。

### 60｜深度学习

**Area Mother Question**：怎样构造可学习的高表达函数，并让层级表示在大规模数据和计算下可训练？

建议 Leaf Topics：

```text
01_神经网络作为函数逼近器_MLP与表达能力
02_Backprop与层级信用分配
03_深网训练_初始化_归一化_残差与正则机制
04_CNN_空间结构与参数共享
05_RNN_状态记忆与序列建模
06_Attention与Transformer
07_结构化神经网络_GNN等              # Candidate，证据足够后再晋升
```

共同观察镜头：

```text
Input Structure
→ Architecture / Inductive Bias
→ Representation Flow
→ Objective
→ Gradient Flow
→ Training Dynamics
→ Generalization / Scaling / Failure
```

这一 Area 不按“网络名字年表”组织。新架构只有改变了 representation、information flow、trainability 或 inductive bias，才值得晋升成新的 Leaf Topic。`self-supervised / transfer` 等 learning setting 回 Area 40；Embedding / pretraining 若只是具体训练组合，不单独抢占 Core Owner。

### 70｜决策、控制与强化学习

**Area Mother Question**：行动会改变未来状态，且反馈可能延迟时，怎样选择或学习长期行为？

建议 Leaf Topics：

```text
01_决策论_Utility_Risk与BayesAction
02_MDP_状态转移_回报_价值与策略
03_Bellman递推与DynamicProgramming
04_POMDP_BeliefState与不完全可观测决策
05_OptimalControl_HJB_PMP与连续系统
06_ValueBasedRL_MC_TD_Qlearning
07_PolicyGradient与ActorCritic
08_ModelBasedRL_Exploration与Planning          # Candidate
```

共同观察镜头：

```text
State / Belief
→ Action
→ Transition
→ Reward / Cost
→ Value
→ Policy
→ Exploration / Learning
→ Long-term Return
```

Area 70 把 AIMA 的 decision / sequential decision、Murphy 的 decision/RL 和 Ye 的 optimal control → RL 接成一条完整主线。`Deep RL` 默认是 `Area 70 RL mechanism + Area 60 function approximator + Area 50 optimizer` 的 Integration，不另建 Core Topic。

### 80｜生成模型

**Area Mother Question**：怎样学习数据的生成规律，并据此计算 likelihood、表示 latent structure 或生成新样本？

建议 Leaf Topics：

```text
01_生成建模统一语言_Density_Likelihood与Sampling
02_AutoregressiveModels与序列分解
03_潜变量生成模型_VAE与ELBO
04_GAN_隐式分布与对抗训练
05_Diffusion_Score与逆过程
06_NormalizingFlows_可逆变换与精确Likelihood
07_FlowMatching与连续输运
```

`Conditional Generation / Guidance` 已降为 Area 80 internal Bridge / Integration Candidate，不再作为独立 Leaf Topic。

共同观察镜头：

```text
Data Distribution
→ Representation of p(x) / p(x|c)
→ Training Principle
→ Inference / Sampling Path
→ Likelihood / Sample Quality / Coverage
→ Conditioning / Control
```

这个 Area 直接吸收 Ye 的 VAE → GAN → Diffusion → Probability Density Control → Flow Matching 主线，同时保留 Murphy 的概率建模视角。Plain deterministic autoencoder 不由生成模型 Own；只有 latent probabilistic generation（如 VAE）才进入 Area 80。

---

## 4. 为什么 Optimization、Deep Learning、Generative Models 要各自成为 Area

这三个地方最容易切错。

### Optimization 不是 ML 的一个小节

Murphy 把 Optimization 放在 Foundations，并覆盖 first-order、second-order、SGD、KKT、proximal、EM、black-box；Ye 整整一章讨论 optimality、AutoDiff、deterministic / stochastic optimization。这说明它是被多个模型族重复调用的独立机制域，而不是“训练神经网络时顺便学一下 GD”。

### Deep Learning 不是“Machine Learning 里的几个模型”

Murphy 把 DNN 单独设 Part III，并继续按 tabular / image / sequence 展开；Ye 更直接从 Function Approximation → Architecture → Training 形成自己的理论主线。其内部复杂度足够高，必须有自己的 Area Atlas。

### Generative Modeling 也不能只塞进 Deep Learning 的末尾

Ye 把 VAE、GAN、Diffusion、Flow Matching 独立成整章；而生成模型又会调用概率、信息论、优化、深网、ODE/SDE。因此它是典型的跨机制汇流 Area。

---

## 5. Leaf Topic 内部不要继续无限建文件夹

大板块需要分层，但**Leaf Topic 一旦成立，就应尽量在一份 Canonical `.tex` 中形成完整机制闭环**。

物理模板：

```text
<Area>/
└── 02_某LeafTopic/
    ├── README.md              # Landing，只负责定位、边界、路由、状态
    ├── 某LeafTopic.tex         # Canonical 深度正文
    └── assets/                # 只有确实需要图时才建
```

不要把一个 Topic 的每个 section 再建成文件夹。否则会把“阅读上的章节”误认为“知识 Ownership”。

---

## 6. 每一本 Leaf Topic 的统一认知骨架

AI 算法 Topic 不适合照教材目录机械抄。建议所有 Leaf Topic 用同一套观察镜头，但允许按内容调整顺序。

### Section 0｜Position：它为什么存在

回答：

```text
它解决哪一种 Failure？
如果没有它，最朴素的方法会在哪里失败？
它位于整张 AI Atlas 的哪一段？
它依赖谁，又被谁调用？
```

### Section 1｜Problem / Object：到底在操作什么对象

必须把对象说清：

```text
State?
Dataset?
Distribution?
Function fθ?
Policy π?
Value V/Q?
Latent variable z?
Search frontier?
```

对象不清，后面的公式就会变成符号记忆。

### Section 2｜Representation：为什么这样表示

回答“世界对象怎样变成可计算对象”。

例如：

```text
graph / tree
logical sentence
probability distribution
feature vector
parameterized function
neural representation
value function
vector field / score
```

### Section 3｜Naive → Failure → New Mechanism

这是主生成链：

```text
最简单方案
→ 具体失败
→ 必须新增哪一种状态 / 结构 / 目标 / 反馈
→ 新算法由此产生
```

新算法必须是 Failure 推出来的，而不是“下面介绍另一种方法”。

### Section 4｜Mechanism：状态怎样一步步变化

算法必须写成：

```text
Input
→ Internal State
→ Operation / Update
→ Invariant or Monotone Quantity
→ Stop / Output
```

如果是迭代算法，再回答：

```text
每一步看什么？
改什么？
为什么朝正确方向走？
什么时候停止？
```

### Section 5｜Mathematical Derivation：公式为什么只能这样来

只补这个 Topic 真正调用的数学：

```text
Assumption
→ Objective / Identity
→ Derivation
→ Algorithmic Consequence
```

数学一已有 Owner 时只 Use，不重新抄定义。

### Section 6｜Guarantee / Boundary / Cost

至少检查：

```text
Correctness / Optimality / Consistency
Convergence
Generalization
Approximation Error
Time / Space / Compute
Data Requirement
Failure Mode
Assumption Boundary
```

不是所有 Topic 都有所有 guarantee，但必须明确“这里到底能保证什么，不能保证什么”。

### Section 7｜Canonical Example + Minimal Implementation

至少一个母例贯穿：

```text
Problem Setup
→ Representation
→ One or several algorithm steps
→ Result
→ Why this example exposes the mechanism
```

必要时配最小代码实验，但代码只负责验证机制，不让框架/库 API 反过来拥有知识。

### Section 8｜Relations：它和邻居到底差在哪

至少包含：

```text
A ≠ B
Use
Bridge
Extension
Anti-Bridge
```

例如：

```text
MLE ≠ Gradient Descent
Backprop ≠ Optimizer
Attention ≠ Transformer
MDP ≠ Reinforcement Learning
Diffusion training ≠ Sampling
Prediction ≠ Decision
```

### Section 9｜Compression：最终压缩成什么心智模型

章末只保留：

```text
Mother Question
Core Object
State Transition / Computation Chain
Invariant / Objective
Failure Signal
Boundary
Next Routing
```

如果学完后仍只能背算法步骤，而无法从 Mother Question 和 Failure 重新推出机制，这本 Topic 就还没有完成。

---

## 7. 一个 Area Atlas 自己必须包含什么

Area Atlas 不是小教材。它只承担地图责任：

```text
1. Area Mother Question
2. Scope / Stop Boundary
3. Shared Object Language
4. Leaf Topic Map
5. Dependency DAG
6. Comparison Matrix
7. Internal Bridges
8. Canonical Integrations
9. Learning Route
10. Research Extension Routing
```

例如 `60_深度学习/README.md` 应能让人一眼看出：

```text
Function Approximation
        ↓
MLP / Computation Graph
        ↓
Backprop
        ↓
Training Dynamics
        ↓
Architecture Inductive Bias
   ┌────┼────┐
 CNN   RNN   Attention
              ↓
         Transformer
```

但 Universal Approximation Theorem 的证明、Backprop 推导、Attention 数学都不在 Atlas 展开。

---

## 8. Bridge 采用两级结构

### Area 内 Bridge

只有当两个 Leaf Topic 的接口反复出现且任一 Topic 都无法独占时，放在对应 Area 的：

```text
50_科内桥梁/
```

候选例子：

```text
Deep Learning:
Backprop × Optimization Update
CNN / RNN / Attention × Inductive Bias

Machine Learning:
Probability Model × Estimator × Loss
Regularization × Generalization
```

### Cross-Area Bridge

放在根级：

```text
85_跨域桥梁/
```

当前最有价值候选：

```text
AI-B01 Probability → Estimation / Loss
AI-B02 AutoDiff → Backprop → Optimization
AI-B03 Search / Planning → Dynamic Programming
AI-B04 Known-model Decision → RL
AI-B05 Probability → Generative Modeling
AI-B06 Function Approximation → Value / Policy Approximation
AI-B07 Continuous Dynamics → Control / Diffusion / Flow
```

Bridge 不因为“两个 Topic 有关系”就建；必须满足项目已有 Bridge Validity / Standalone Promotion Gate。

---

## 9. Integration 与 Research Direction 必须在语义和物理上都分开

上一版把二者共享在 `90_综合与研究方向/`，虽然文字上区分了解释责任，但物理入口仍会诱导后续混写。现在正式拆成：

```text
90_综合专题/    # Integration：追踪一次完整过程
95_研究方向/    # Direction Atlas：组织纵向研究领域
```

### Integration

追踪一个完整过程怎样调用多个成熟模块，例如：

```text
AI-I01 从数据到可用预测器
Linear Regression → Logistic Regression → MLP

AI-I02 一个智能体闭环
Observe → Belief → Infer → Decide → Act → Learn

AI-I03 一个现代语言模型训练/推理生命周期
Token → Representation → Transformer → Objective → Optimization → Decode
```

### Direction Atlas

统一从根级 `95_研究方向/` 进入，用于未来决定研究方向。例如：

```text
NLP_LLM_Agents/
ComputerVision_Multimodal/
Robotics_EmbodiedAI/
ScientificML/
GraphML/
CausalML/
LearningTheory/
AISafety_Alignment/
```

Direction Atlas 必须先回答：

```text
它在解决什么应用/研究母问题？
它调用哪些 Core Area？
哪些机制只是 Use？
哪些新机制足够独立，需要在该 Direction 内建立新 Topic？
```

因此 Direction 不是第二套 AI 知识库，而是纵向研究路由。

---

## 10. Topic 晋升规则：什么时候 section 值得变成独立文件夹

一个内容只有同时接近以下条件时，才从 section 晋升为 Leaf Topic：

1. 有自己的 **Mother Question**；
2. 有独立的 **Object / State / Mechanism**；
3. 有明显的 **Naive Failure → New Mechanism**；
4. 有自己的 **Boundary / Cost / Guarantee**；
5. 会被多个其他内容复用，或内部已经大到不能由父 Topic 清楚拥有；
6. 独立后能减少重复，而不是增加跳转成本。

反过来，以下内容通常只做 section：

```text
一个 activation function
一个 optimizer 变体
一个网络名字
一个 loss function
一个 benchmark
一个 implementation trick
一个历史人物/时间线
```

除非它真正改变了机制层。

---

## 11. 当前建设策略

当前已经锁定 **Area Topology + Leaf Ownership**，但仍不批量创建几十个空 Topic。

八个 Area Atlas 已全部物理建立；Leaf Topic 目前只存在于 Area README 的 Canonical Map 中。物理创建某个 Leaf Handbook 的触发条件改为：

```text
真实学习已经进入该机制
+ 需要长解释 / 推导 / 母例
+ Leaf Boundary v1 能确定唯一 Owner
→ 才创建 <Leaf>/README.md + Canonical .tex
```

第一条 Integration 仍采用：

```text
Linear Regression
→ Logistic Regression
→ MLP
```

它会首先调用并攻击：

```text
Area 30 Probability
Area 40 Learning / Estimation / Generalization
Area 50 Optimization
Area 60 Neural Representation
```

因此下一步应优先物理建立 **Area 40 / Leaf 01 与 Leaf 02**，再在进入 MLP 时建立 **Area 60 / Leaf 01**；Area 50 的 Leaf 只有当求解与梯度机制真正成为主问题时再建。这样目录继续由真实认知需求长出来，而不是把“已经锁定的 Leaf 名单”误解成“必须立刻生成的文件夹清单”。

---

## 12. 最终压缩

整个物理架构可以压成一句：

```text
Subject Atlas 负责“整个 AI 世界在哪里”；
Area Atlas 负责“一大片机制怎样分区”；
Leaf Topic 负责“一个机制为什么存在、怎样运转”；
Bridge 负责“两个机制为什么能接”；
Integration 负责“多个机制怎样一起完成任务”；
Direction Atlas 负责“研究方向怎样调用这套核心世界模型”。
```

如果未来新增 LLM Agent、Diffusion Transformer、World Model、Neuro-symbolic、Foundation Model 等新概念，优先先问它改变了哪一层，而不是立刻新建一级目录。