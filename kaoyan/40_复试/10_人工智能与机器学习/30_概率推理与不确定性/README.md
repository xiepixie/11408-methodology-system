# 概率推理与不确定性 Area Atlas：用分布表示未知并吸收证据

> 类型：Atlas
> 状态：已采用；Area Boundary v1 + Leaf Boundary v1 已锁定。Leaf Topic 仅建立 Canonical 归属与依赖，不批量创建深度正文。

## Mother Question

> **当真实状态、观测或未来结果存在不确定性时，怎样用概率结构表示“我们不知道什么”，并在获得证据后更新 belief、回答 query？**

本 Area 的核心是 **uncertainty representation + probabilistic inference**。它不是“所有概率统计知识”的副本，也不自动拥有所有从数据学习参数的方法。

## Canonical Ownership

本 Area 唯一拥有：

- probability distribution 在 AI 中作为 belief / uncertainty representation 的语义；
- conditioning、Bayes rule、marginalization、posterior / predictive distribution；
- multivariate distribution、conditional independence、factorization；
- probabilistic graphical models 的表示语言；
- exact inference：variable elimination、message passing 等；
- approximate inference：Monte Carlo / importance sampling / MCMC / variational inference 的概率推断责任；
- temporal probabilistic models 中 filtering / prediction / smoothing / state estimation；
- entropy、cross entropy、KL divergence、mutual information 等信息论量的**定义、概率语义和一般性质**。

## Stop Boundary

本 Area **不拥有**：

- 数学一已经完整拥有的基础概率定义与考研计算套路 → Use `../../10_数学一/30_概率论/`；
- “如何从训练集选择模型并泛化”这一学习协议 → Area 40；
- MLE / MAP / ERM 作为模型拟合与 learning protocol 的 Canonical Owner → Area 40；
- gradient / SGD / Newton 等求解 posterior/objective 的数值方法 → Area 50；
- neural probabilistic parameterization → Area 60；
- belief 之上如何选 action / policy → Area 70；
- VAE / diffusion / flow 等专门生成机制 → Area 80。

### 最关键的边界：Inference 与 Learning

```text
Given model + parameters + evidence
→ infer unknown variables / belief
= Area 30

Given data
→ estimate parameters / choose hypothesis / assess generalization
= Area 40
```

Bayesian parameter learning天然跨越两者：posterior 的概率语义由 Area 30 Own；“把它作为学习器从数据估计模型”的协议由 Area 40 Own。若两边反复需要完整接口，再晋升 Cross-Area Bridge。

## 边界判定

| 内容 | Owner | 判定理由 |
|---|---|---|
| Bayes rule / conditioning | Area 30 | belief update 基本机制 |
| Bayesian network / factor graph | Area 30 | uncertainty factorization |
| variable elimination / belief propagation | Area 30 | probabilistic inference |
| HMM filtering / Kalman filtering | Area 30 | state estimation |
| POMDP belief update | Area 30 Own update；Area 70 Own decision | belief 与 action policy 分责 |
| MLE / MAP estimator | Area 40 | 参数学习/估计协议；概率语义 Use Area 30 |
| cross entropy / KL 的定义 | Area 30 | information measure |
| cross-entropy loss in classifier | Area 40/60 Use Area 30 | 具体 training responsibility 不改变定义 Owner |
| ELBO / VAE training | Area 80 | generative objective；调用 Area 30 的 KL/variational inference |

## Shared Object Language

```text
Unknown Quantity
→ Distribution / Factorization
→ Evidence
→ Condition / Marginalize / Approximate
→ Posterior / Belief
→ Query / Prediction
```

学习这一 Area 时始终问：随机变量是什么、已知什么、条件化什么、求哪个 query、哪些 independence 让计算变得可行、精确推断为何不可承受、近似引入什么误差。

## Leaf Topic Boundary v1

| Leaf Topic | Canonical Owns | Explicit Stop Boundary |
|---|---|---|
| **01 概率建模、Bayes 与条件化** | random quantity / event 的 AI 语义、prior/likelihood/posterior、conditioning、Bayes rule、marginalization、predictive distribution，以及“用分布表示不知道”这一母模型 | 多变量结构化 factorization 转 02；参数如何从训练集学出回 Area 40 |
| **02 多变量分布、条件独立与概率图模型** | joint distribution、conditional independence、factorization、Bayesian network / Markov-style graph 的 representation semantics | 不 Own inference algorithm；variable elimination / message passing 转 03，sampling / VI 转 04 |
| **03 精确推断：变量消元与消息传递** | query/evidence 下的 exact marginal / posterior computation、variable elimination、sum-product / tree message passing 等 exact computation contract | 图结构语义回 02；近似计算转 04；参数学习回 Area 40 |
| **04 近似推断：Monte Carlo、MCMC 与变分** | exact inference 不可承受时的 sampling / importance / MCMC / variational approximation，近似对象、误差来源与 inference-quality/cost 权衡 | generic numerical optimizer 回 Area 50；VAE 的 generative objective/composition 回 Area 80 |
| **05 时序概率模型与状态估计** | temporal latent state、transition/observation uncertainty、filtering/prediction/smoothing，HMM/Kalman/dynamic graphical model 的 state-estimation responsibility | 一旦 belief 之后继续选择 action/value/policy，转 Area 70；不 Own RL |
| **06 信息论语言：Entropy、Cross Entropy、KL、MI** | entropy、cross entropy、KL、mutual information 的定义、概率语义、一般性质与 information comparison language | classifier loss、ELBO、language-model objective 等具体“为什么在该任务里这样用”由下游 Owner 解释 |

### Internal Dependency DAG

```text
01 概率建模 / Bayes
   ├──→ 02 多变量结构 / PGM
   │       ├──→ 03 Exact Inference
   │       ├──→ 04 Approximate Inference
   │       └──→ 05 Temporal Models / State Estimation
   └──→ 06 Information Theory

04 Approximate Inference ──Uses──→ Area 50 optimization
05 belief state ──Exports──→ Area 70 decision
```

### Inference / Learning 的 Leaf 级边界

```text
02 defines factorization
03 / 04 compute latent/posterior queries
Area 40 estimates model/parameters from data
```

因此 GMM、Bayesian network、HMM 等同一个“模型名字”可能跨 Area：**representation / inference 回 Area 30，learning protocol 回 Area 40**。不因为模型名字相同就复制整套内容。

`Probabilistic Programming` 暂不晋升 Leaf Topic；当前视为 `02 representation + 03/04 inference + software abstraction` 的 Direction / Integration Candidate。

## Dependency / Export

```text
Uses:
数学一概率论与数理统计
线性代数（Gaussian / covariance / quadratic form 等）
Area 50 numerical optimization when approximate inference needs it

Exports to:
Area 40 estimation / probabilistic ML
Area 70 belief-state decision
Area 80 generative modeling
95 Directions: uncertainty / probabilistic programming / Bayesian ML
```

## Source Basis

Murphy 把 Probability、Statistics、Decision Theory、Information Theory 放在 ML Foundations，并用 probabilistic modeling 统一后续模型；AIMA 也把 uncertainty / probabilistic inference 与 learning、decision 分层组织。这支持把“概率表示 + 推断”锁为独立 Owner，同时把 learning 和 decision 留给下游 Area。

## Compression

> **Area 30 Own 的是：不知道真实世界时，怎样把未知变成 distribution，再用 evidence 把 distribution 变成新的 belief。**
