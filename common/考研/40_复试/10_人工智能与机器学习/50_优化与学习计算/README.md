# 优化与学习计算 Area Atlas：把目标函数变成可执行更新

> 类型：Atlas
> 状态：已采用；Area Boundary v1 + Leaf Boundary v1 已锁定。Leaf Topic 仅建立 Canonical 归属与依赖，不批量创建深度正文。

## Mother Question

> **当目标函数、约束和可计算信息已经明确时，怎样利用有限计算找到高质量参数或解，并理解收敛、稳定性与计算代价？**

本 Area 是跨 ML / DL / RL / Generative Modeling 复用的 **numerical solver layer**。它不决定“该学什么”，而负责“目标定了以后怎么算”。

## Canonical Ownership

本 Area 唯一拥有：

- optimization problem 的一般对象：variable、objective、constraint、feasible set；
- local/global、convex/nonconvex、smooth/nonsmooth、constrained/unconstrained 等问题几何；
- first-order methods：gradient descent、step size / line search、convergence；
- stochastic optimization：SGD、momentum、adaptive methods、variance/noise；
- second-order / quasi-Newton：Newton、BFGS、trust region 等；
- constrained optimization：Lagrange multiplier、KKT、projected methods；
- proximal / nonsmooth optimization；
- automatic differentiation 的一般计算责任：forward/reverse mode、JVP/VJP、computation graph differentiation；
- 算法级 convergence / conditioning / numerical stability / compute-memory trade-off。

## Stop Boundary

本 Area **不拥有**：

- “为什么要用这个 loss / estimator” → Area 40 或具体下游 Area；
- probability / posterior semantics → Area 30；
- neural architecture、gradient flow 的网络语义 → Area 60；
- value/policy/Bellman objective 的决策语义 → Area 70；
- ELBO、score matching、flow matching 的生成语义 → Area 80；
- BFS/A*/CSP 这类显式状态空间 search → Area 10。

### 两条必须锁死的 Anti-Bridge

```text
Objective Construction ≠ Objective Optimization
Automatic Differentiation ≠ Backpropagation as neural credit assignment
```

AutoDiff 的通用计算原理在 Area 50；Area 60 只 Own “神经网络层级中梯度怎样承载 credit assignment、为什么会 vanishing/exploding”等网络语义。

## 边界判定

| 内容 | Owner | 判定理由 |
|---|---|---|
| GD / SGD / Adam | Area 50 | numerical update rule |
| Newton / BFGS / trust region | Area 50 | curvature-based solver |
| Lagrange / KKT / proximal | Area 50 | constrained/nonsmooth optimization |
| reverse-mode AD / VJP | Area 50 | generic derivative computation |
| backprop through MLP | Area 60 Use Area 50 | neural credit assignment |
| cross-entropy 为什么是 classifier loss | Area 40/30 | objective semantics，不是 solver |
| weight decay 的 regularization meaning | Area 40 | generalization principle；Area 50只处理求解后果 |
| parameter initialization / residual connection | Area 60 | trainability / architecture mechanism |
| hill climbing over explicit discrete states | Area 10 | neighborhood search 是主对象 |
| policy optimization objective | Area 70；solver from Area 50 | decision semantics 与 numerical optimization 分责 |

## Shared Object Language

```text
Variable θ
→ Objective L(θ)
→ Local / Stochastic Information
→ Search Direction
→ Step / Update
→ Iterate
→ Convergence / Stop
→ Solution Quality + Compute Cost
```

任何优化 Topic 都必须说明：可用信息是什么、方向怎样来、步长怎样定、为什么可能下降/收敛、条件数和噪声如何影响、每步计算/内存代价是什么。

## Leaf Topic Boundary v1

| Leaf Topic | Canonical Owns | Explicit Stop Boundary |
|---|---|---|
| **01 优化问题、几何与最优性条件** | variable/objective/constraint/feasible set、local/global、convex/nonconvex、smooth/nonsmooth、first/second-order optimality、conditioning 的问题级语言 | 不 Own 具体迭代算法；learning / RL / generation 为什么产生这个 objective 回对应 Area |
| **02 一阶方法：Gradient Descent 与 Step Size** | descent direction、gradient method、fixed/adaptive step、line search、basic convergence rate 与 step-size trade-off | stochastic gradient noise 转 03；curvature/Newton 转 04；constraint/projection 转 05/06 |
| **03 随机优化：SGD、Momentum 与 Adaptive Methods** | finite-sum / stochastic objective、gradient estimator、SGD、momentum、Adam-style adaptive update、noise/variance 与 stochastic convergence | sampling 的概率语义回 Area 30；mini-batch neural training system 回 60/90；不 Own learning objective |
| **04 二阶与拟牛顿：Newton、BFGS、Trust Region** | Hessian/curvature-based step、Newton/quasi-Newton、trust-region logic、local convergence/compute-memory trade-off | Hessian 数学定义 Use 数学；深网中是否值得用二阶法是调用问题，不另建 DL Owner |
| **05 约束优化：Lagrange 与 KKT** | equality/inequality constraints、Lagrangian、KKT、duality/basic constrained optimality、feasible-vs-optimal distinction | sequential dynamics constraint + trajectory cost 的 control semantics 回 Area 70；CSP 离散约束回 Area 10 |
| **06 Projected / Proximal 与非光滑优化** | projection、subgradient/proximal operator、composite objective、L1-style nonsmooth structure 与 constrained first-order computation | regularizer 为什么合理回 Area 40；具体 sparse model family 不由 solver Own |
| **07 Automatic Differentiation 与计算图求导** | computation graph differentiation、forward/reverse mode、JVP/VJP、first/second derivative computation 与 compute-memory trade-off | 不 Own parameter update；神经网络中的 layer-wise backprop / credit assignment 回 Area 60 |

### Internal Dependency DAG

```text
01 Optimization Geometry / Optimality
   ├──→ 02 First-order Methods ──→ 03 Stochastic Methods
   ├──→ 04 Second-order / Quasi-Newton
   ├──→ 05 Constrained Optimization ──→ 06 Projected / Proximal
   └──→ defines what derivative information is needed

07 AutoDiff ──service──→ 02 / 03 / 04 / downstream Areas
```

`07 AutoDiff` 是**横向计算服务**，不是“最先进 optimizer”的下一章；它回答“导数怎样高效算”，02–06 回答“拿到数学信息后怎样更新变量”。

### EM / MM / Black-box 的当前边界

- **EM / variational-EM / MM**：暂不晋升独立 Leaf。它们天然连接 Area 30 latent inference、Area 40 parameter estimation 与 Area 50 bound/alternating optimization，先进入 Cross-Area Bridge Candidate；
- **coordinate / alternating methods**：先作为 02/06 的 Extension；
- **black-box / derivative-free optimization**：先作为 Extension。只有后续在 AI 学习中出现重复调用，才考虑独立晋升。

## Dependency / Export

```text
Uses:
微积分 / 多元微分 / 线性代数

Inputs from downstream Areas:
Area 40 / 60 / 70 / 80 提供 objective semantics 与 constraints

Exports:
parameter / decision update algorithms
convergence / stability / compute-memory analysis
Scientific ML Direction
```

## Source Basis

Murphy 把 Optimization 独立放在 Foundations，并覆盖 first-order、second-order、SGD、constraints、proximal 等；Ye 又把 Network Training 单独展开为 optimality、AutoDiff、deterministic/stochastic optimization。这说明优化是共享计算域，而不是 Deep Learning 的附属章节。

## Compression

> **Area 50 Own 的是：目标已经定了以后，怎样把数学目标转换成稳定、可计算、可分析的迭代过程。**
