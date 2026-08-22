# 人工智能与机器学习 Subject Atlas：智能体、推理、学习与决策

> 类型：Atlas
> 状态：Area Boundary v1 + Leaf Boundary v1 已采用；八个 Core Area 的 Canonical Scope / Stop Boundary、Leaf Topic 归属与内部 Dependency DAG 已锁定。Bridge / Integration 深度正文仍按真实学习逐步建立。

> 设计依据见：[人工智能与机器学习领域结构设计依据](00_领域结构设计依据.md)；物理层级与 Leaf Topic 规范见：[文件夹与 Handbook 架构](人工智能与机器学习：文件夹与%20Handbook%20架构.md)。本 README 是当前唯一 Canonical Subject Atlas Source；两份设计文件只记录为什么这样切、怎样维护，不拥有具体算法知识。

## 0. Mother Question

当前不把人工智能理解成“很多模型的集合”，也不把 AI 与 Machine Learning 直接画等号。

我们先用一个更外层的问题统一整个领域：

> **一个系统面对复杂、未知或不确定的环境时，怎样表示它所知道的东西，推断世界状态，寻找或学习解决方案，并选择能够实现目标的输出或行动？**

最外层循环采用 rational-agent / modeling 双重视角：

```text
Environment / Task
        ↓ observation / data
Represent State / Belief / Knowledge
        ↓
Infer / Predict
        ↓
Search / Plan / Decide
        ↓
Output / Act
        ↓ feedback / experience
Learn / Update
        ↺
```

并非每个 AI 系统都会走完整闭环：一个分类器可能只做 `data → prediction`，一个搜索程序可能没有 learning，一个生成模型可能输出 sample 而不直接作用于环境。这个循环的责任只是回答：**一个算法在智能系统里到底承担哪一步。**

---

## 1. Atlas Foundation：先固定共同语言

### 1.1 Agent / Task Language

全领域反复使用：

- **Environment / Task**：系统面对的外部问题；
- **Observation / Percept / Data**：系统实际得到的信息；
- **State / Belief / Knowledge**：内部怎样表示世界；
- **Action / Output**：系统能产生什么结果；
- **Performance / Utility / Loss**：怎样判断好坏；
- **Experience / Feedback**：后续怎样获得新信息并更新。

### 1.2 Modeling Language

后续笔记必须稳定区分：

```text
Task ≠ Model ≠ Algorithm ≠ Objective ≠ Metric
Representation ≠ Inference ≠ Learning
Training ≠ Generalization
Prediction ≠ Decision
Search ≠ Continuous Optimization
Model Family ≠ Learning Setting
Application Domain ≠ Core Mechanism
```

例如：

- classification 是 **Task**，不是模型；
- neural network 是 **Model Family / Representation**，不是一种监督方式；
- SGD 是 **Optimization Algorithm**，不是模型；
- maximum likelihood 是 **Estimation Principle / Objective Construction**，不等于 linear regression；
- NLP / CV 是 **Application / Direction**，会调用很多不同机制。

### 1.3 Mathematical Foundation

优先 Use 现有考研数学 Owner，不复制基础定义：

| 数学语言 | AI 中的主要作用 | 当前路由 |
|---|---|---|
| Linear Algebra | representation、linear model、PCA、neural layer、attention、low-rank structure | `../../10_数学一/20_线性代数/` |
| Calculus / Multivariate Calculus | gradient、Taylor、backprop、Jacobian/Hessian | `../../10_数学一/10_高等数学/` |
| Probability / Statistics | uncertainty、likelihood、generalization、latent variable | `../../10_数学一/30_概率论/` |
| Optimization | learning / control 的计算引擎 | `50_优化与学习计算` Area 深化 |
| Information Theory | entropy、cross entropy、KL、mutual information | 按 Probability / Machine Learning / Generative Models 的真实需要补 |
| ODE / SDE / Dynamical Systems | control、Neural ODE、diffusion、flow matching | Extension / Candidate Bridge，按需补 |

### 1.4 Cross-cutting Validation

所有学习型算法都必须能回答：

```text
Data quality
Objective vs evaluation metric
Train / validation / test
Generalization
Uncertainty / calibration
Model comparison
Interpretability
Distribution shift / failure cases
Computation and memory cost
```

这部分不是某个具体模型的附录，而是判断“这个算法到底有没有真正工作”的共同检查语言。

---

## 2. Core Area Topology：大领域先分 Area，再分 Leaf Topic

这个板块不能直接用“Subject Atlas → 九本超大 Topic”。AI 的规模已经要求增加一层 **Area Atlas**：

```text
AI Subject Atlas
→ Area Atlas
→ Leaf Topic Handbook
```

一级 Core Area 锁定为八块：

| Area | Mother Question | Canonical Area Atlas |
|---|---|---|
| **10 问题求解** | 规则和合法动作基本已知，但候选空间巨大时，怎样组织显式搜索找到解？ | [问题求解](10_问题求解/README.md) |
| **20 知识表示与推理** | 怎样把事实、关系、规则和动作条件变成有语义的显式知识，并合法推出结论或计划？ | [知识表示与推理](20_知识表示与推理/README.md) |
| **30 概率推理与不确定性** | 不知道真实状态时，怎样用分布表示 belief、吸收 evidence 并回答 query？ | [概率推理与不确定性](30_概率推理与不确定性/README.md) |
| **40 机器学习** | 规则无法手写时，怎样从有限经验估计模型并判断它能否泛化？ | [机器学习](40_机器学习/README.md) |
| **50 优化与学习计算** | Objective 与约束已经明确后，怎样把它们变成稳定、可分析的数值更新？ | [优化与学习计算](50_优化与学习计算/README.md) |
| **60 深度学习** | 怎样构造高表达的神经函数与表示，并让信息和梯度穿过深层结构？ | [深度学习](60_深度学习/README.md) |
| **70 决策、控制与强化学习** | 行动会改变未来时，怎样把 belief、dynamics、reward/utility 与 experience 变成长期 policy？ | [决策、控制与强化学习](70_决策_控制与强化学习/README.md) |
| **80 生成模型** | 怎样学习生成规律，并明确区分分布表示、训练原则与 sampling path？ | [生成模型](80_生成模型/README.md) |

**这八个 Area 是 Canonical Owner Domain，不是八种同类概念。** 每个 Area 的 `README.md` 已锁定 Owns / Uses / Stop Boundary，并进一步锁定 Leaf Topic Boundary v1 与内部 Dependency DAG；以后新增算法先在现有 Leaf / Area 中做 Owner Diff，只有确实无法被现有 Mother Question 解释时才挑战拓扑。

跨 Area 接口、完整过程和纵向研究路线分别进入 [85_跨域桥梁](85_跨域桥梁/README.md)、[90_综合专题](90_综合专题/README.md)、[95_研究方向](95_研究方向/README.md)。完整物理目录、Leaf Topic 晋升规则和统一正文骨架见 [文件夹与 Handbook 架构](人工智能与机器学习：文件夹与%20Handbook%20架构.md)。

---

## 3. 四种 Routing Lens：遇到陌生算法时先定位，不先背名字

文件树只能选一种 Ownership，但面对算法时同时看四个轴。

### Lens A｜Problem / Environment

先问环境是什么：

```text
known / unknown
 deterministic / stochastic
fully observable / partially observable
one-shot / sequential
single-agent / multi-agent
static dataset / interactive experience
```

这些条件经常比算法名字更早决定应该调用哪个 Topic。

### Lens B｜Representation

算法把问题表示成什么：

```text
state graph
constraints
logic / symbols
probability distribution / graphical model
linear / kernel / tree function class
neural representation
latent variable
value / policy / dynamical state
```

### Lens C｜Computation

真正靠什么计算：

```text
search
constraint propagation
logical inference
dynamic programming
probabilistic inference
sampling
gradient / numerical optimization
learning / parameter estimation
```

### Lens D｜Output Responsibility

最终是要：

```text
infer / explain
predict
generate
plan
decide
act / control
```

遇到一个新算法时，先在四个 Lens 中回答它的位置，再决定它属于哪个 Owner。

---

## 4. Core Bridges：真正重要的是模块之间怎样接

当前只规划，不立即全部建册。

### AI-B01｜Probability → Estimation / Loss

```text
probabilistic assumption
→ likelihood / posterior
→ MLE / MAP / cross entropy / KL
→ learnable objective
```

回答：**概率模型为什么会变成训练损失？**

### AI-B02｜Differentiation / AutoDiff → Backprop → Optimization

```text
computation graph
→ local derivatives
→ reverse accumulation / backprop
→ gradient
→ optimizer update
```

回答：**“算出梯度”和“利用梯度更新参数”为什么是两个机制？**

### AI-B03｜Search / Planning → Dynamic Programming → Sequential Decision

回答：路径搜索、状态价值、未来回报和策略之间如何交接。

### AI-B04｜Known-model Decision → Reinforcement Learning

```text
known transition / reward
→ solve value / policy
──────── boundary ────────
unknown model or value
→ experience
→ estimate / improve policy
```

这是“已知模型下的序贯决策 → 从经验学习策略”的核心接口。

### AI-B05｜Probability → Generative Modeling

回答：density、likelihood、latent variable、sampling、score、flow 各自扮演什么角色。

### AI-B06｜Function Approximation → Value / Policy Approximation

回答：为什么 neural network 可以进入 RL，但“Deep RL”并没有推翻 MDP / Bellman 的基本结构。

### AI-B07｜Continuous Dynamics → Control / Neural ODE / Diffusion / Flow

当前标为 **Candidate / Extension**。它在 Xiaojing Ye 的结构中非常重要，但是否独立建册要等我们真实学习 optimal control、Neural ODE、diffusion/flow 后再判。

### AI-B08｜Symbolic Representation ↔ Probabilistic Representation

当前只保留 Candidate。等概率编程、Neuro-symbolic AI 或不确定知识表示真正进入学习范围后再判断 Standalone Promotion。

---

## 5. Integration Layer：把多个成熟机制跑成完整过程

### AI-I01｜从数据到可用预测器

第一条实际学习主线：

```text
Problem
→ Data
→ Model / Representation
→ Probabilistic Assumption or Objective
→ Estimation / Optimization
→ Validation / Generalization
→ Prediction
→ Decision / Communication
```

第一组 Canonical Problems：

```text
Linear Regression
→ Logistic Regression
→ MLP
```

这里不把三者理解成“模型升级史”，而是比较同一个 modeling pipeline 中：

- output 语义怎样变；
- model family 怎样变；
- loss 从哪里来；
- parameter 怎样估计；
- gradient 怎样传播；
- capacity 增大以后 generalization 问题怎样变化。

### AI-I02｜一个理性智能体的完整闭环

```text
Observe
→ Represent / Update Belief
→ Infer
→ Plan / Decide
→ Act
→ Receive Feedback
→ Learn / Update
```

未来用它验收 Search、Probability、Planning、RL、Perception 是否真正接上，而不是各学各的。

### AI-I03｜一个现代语言模型训练与推理生命周期

```text
Token / Context
→ Neural Representation
→ Transformer
→ Autoregressive Objective
→ Optimization
→ Decoding / Search
→ Output
```

### AI-I04｜现代 LLM 应用系统：Context、Retrieval、RAG、Agent、Workflow 与 MCP

```text
Context Assembly
→ Retrieval / RAG
→ Model Generation
→ Tool Calling
→ Agent / Workflow State
→ External Capability via MCP
→ Evaluation / Security / Observability
```

正式入口：[`90_综合专题/AI-I04_现代LLM应用系统/README.md`](90_综合专题/AI-I04_现代LLM应用系统/README.md)

---

## 6. Direction Layer：研究方向不与 Core Topic 混放

AIMA 把 NLP、CV、Robotics 单列大章；Murphy 还覆盖 recommender、graph embedding；Xiaojing Ye 强调 control、scientific computing、generative modeling。对我们而言，这些更适合作为**方向入口**：它们会组合多个 Core Topic，而不是重新定义底层机制。

当前候选：

| Direction | 主要调用的 Core |
|---|---|
| **NLP / LLM / Agents** | Machine Learning + Optimization + Deep Learning + Generative Models；agent 系统还会调用 Search / Decision / RL |
| **Computer Vision / Multimodal** | Machine Learning + Optimization + Deep Learning + Generative Models |
| **Robotics / Embodied AI** | Search + Probability + Deep Learning + Decision / Control / RL |
| **Scientific Machine Learning** | Optimization + Deep Learning + Control；进一步连接 ODE/PDE/数值分析 |
| **Graph ML / Recommender** | Machine Learning + Deep Learning；recommender 还会进入 sequential decision |
| **Causal ML** | Probability + Machine Learning + Decision；当前作为方向候选，不先升 Core |
| **Learning Theory** | Machine Learning 为中心，深入 probability/statistics/optimization |
| **AI Safety / Alignment** | decision、RL、uncertainty、human objective 与系统级行为的 Integration |

### 方向选择判据

不按“哪个现在最火”选，而看：

> **当一个方向进入它最麻烦的数学、实验、失败案例与论文细节以后，我是否仍愿意继续研究？**

因此未来每个方向至少要做一次：

```text
核心论文/教材段落
+ 手推一个机制
+ 写一个最小实现
+ 看一个失败案例
+ 解释它调用了哪些 Core Topic
```

再决定是否建立独立 Direction Atlas。

---

## 7. 当前推荐学习路由

```text
Round 0  只读 Subject Atlas：建立 Agent Loop + 八个 Area 的位置感
    ↓
Round 1  AI-I01：Linear Regression → Logistic Regression → MLP
    ↓
Round 2  Probability + Machine Learning
    ↓
Round 3  Optimization + Deep Learning
    ↓
Round 4  Search + Symbolic Reasoning + Sequential Decision
    ↓
Round 5  Reinforcement Learning
    ↓
Round 6  Generative Models
    ↓
Round 7  NLP / CV / Robotics / Scientific ML / Learning Theory ... 方向体验
    ↓
选择一条纵向研究方向，再进入论文级深入
```

这个顺序服务“先泛化、后选方向”，不是唯一先修链。真实学习中一旦暴露数学或机制缺口，就局部补齐后返回主线。

---

## 8. 当前参考书怎样路由

这些 PDF 都是 Source / Reference，不自动成为 Canonical Owner。

| Source | 最适合作为哪一层参考 | 不能直接拿它做什么 |
|---|---|---|
| **Russell & Norvig, _Artificial Intelligence: A Modern Approach_** | 整个 AI Course Map；Agent、Search、Logic、Planning、Uncertainty、Decision、ML、NLP/CV/Robotics | 不能把 28 章机械变成我们的 28 个 Topic |
| **Kevin P. Murphy, _Probabilistic Machine Learning: An Introduction_** | Probability / Machine Learning / Optimization / Deep Learning；Probability + Bayesian Decision Theory 视角；model families | 不能代表整个 AI，也不能把 Foundation 与模型族当同一层 |
| **Xiaojing Ye, _Mathematical Foundations of Deep Learning: Theory and Algorithms_** | Optimization / Deep Learning / Control & RL / Generative Models；尤其 Function Approximation → Training → Control → RL → Generative | 不是 AI 全景，也不是经典 ML 算法百科 |
| **Clark & Berry, _Models Demystified_** | AI-I01 与 Cross-cutting Validation；Task/Model/Algorithm 区分、estimation、uncertainty、model comparison | 不承担 symbolic AI、planning、概率推理等完整 AI 主干 |

后续进入某个 Topic 时，再做 **Source Diff**：比较四本书对同一机制的解释责任、边界和生成链，不按任一本目录全文搬运。

---

## 9. Stop Boundary

当前 Atlas **不负责**：

- 展开 BFS、Bayes Network、SVM、Backprop、Bellman、Diffusion 等完整推导；
- 批量建立八个 Area 下几十个空 Topic 目录或空 LaTeX；
- 罗列所有深度学习架构；
- 把 NLP / CV / Robotics 与 Probability / Optimization 强行作为同层基础机制；
- 重新抄写数学一已经拥有的基础定义；
- 在尚未真实体验方向前替使用者确定研究方向。

下一次最小动作：先建设 **AI-I01《Linear Regression → Logistic Regression → MLP：到底什么叫学习？》**，用真实推导和代码第一次攻击 Probability / Machine Learning / Optimization / Deep Learning 四个 Area 的边界。
