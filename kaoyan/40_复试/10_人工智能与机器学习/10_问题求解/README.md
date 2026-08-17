# 问题求解 Area Atlas：在显式候选空间中找到解

> 类型：Atlas
> 状态：已采用；Area Boundary v1 + Leaf Boundary v1 已锁定。Leaf Topic 仅建立 Canonical 归属与依赖，不批量创建深度正文。

## Mother Question

> **当问题规则、合法动作和目标基本已知，但候选解空间巨大时，怎样组织搜索过程，以有限计算找到满足条件或代价足够好的解？**

本 Area 的核心不是“智能 = 搜索”，而是研究一种稳定的求解范式：把问题显式表示为状态、动作、后继与目标，再决定**先扩展谁、保留谁、何时停止**。

## Canonical Ownership

本 Area 唯一拥有以下解释责任：

- 状态空间、搜索树/图、frontier、visited/explored 等搜索对象；
- 无信息搜索：BFS、DFS、Uniform-Cost 等；
- 启发式搜索：heuristic、Greedy Best-First、A* 及其完备性/最优性条件；
- 局部搜索中“candidate state + neighborhood + move”这一显式配置搜索机制；
- 对抗搜索：game tree、minimax、alpha-beta 等确定性/显式博弈树求解；
- CSP：变量、domain、constraint、constraint propagation、backtracking 等约束求解机制；
- 搜索算法的 completeness、optimality、time/space cost 与 heuristic quality。

## Stop Boundary

本 Area **不拥有**：

- 命题/一阶逻辑的语义、证明规则、知识库推理 → Area 20；
- action schema、STRIPS/PDDL 等符号规划语言 → Area 20；
- probability distribution、belief update、Bayesian inference → Area 30；
- 从数据估计模型参数 → Area 40；
- 连续参数空间上的梯度、Newton、KKT、proximal 等数值优化 → Area 50；
- neural architecture / representation learning → Area 60；
- MDP、Bellman、policy、长期回报、stochastic control → Area 70；
- 生成分布与 sampling mechanism → Area 80。

### 最重要的 Anti-Bridge

```text
Search ≠ Optimization
Search ≠ Planning Representation
Search ≠ Reinforcement Learning
```

判据不是“都在找最优解”，而是**谁拥有问题的核心状态与更新机制**。

## 边界判定

| 遇到的内容 | Owner | 判定理由 |
|---|---|---|
| BFS / DFS / UCS / A* | Area 10 | 核心是 frontier expansion |
| hill climbing / simulated annealing 用于显式配置搜索 | Area 10 | candidate + neighborhood 是主对象 |
| gradient descent | Area 50 | 参数向量与局部导数是主对象 |
| classical planning 中调用 A* | Area 20 Own planning model；Area 10 Own A* | 表示与求解器分责 |
| minimax / alpha-beta | Area 10 | 显式 game tree search |
| stochastic game / multi-agent utility decision | Area 70 | transition + utility + policy 是主对象 |
| CSP backtracking + arc consistency | Area 10 | constraint search/propagation 是主机制 |
| beam search 用于语言解码 | Area 10 Own search mechanism；Direction/Integration 解释调用 | 不因应用域改变 Owner |

## Shared Object Language

```text
Problem
→ State
→ Action / Successor
→ Frontier / Candidate Set
→ Evaluation / Heuristic
→ Expansion / Move
→ Goal Test
→ Solution
```

所有 Leaf Topic 都必须说明：搜索状态是什么、下一步候选怎样产生、选择策略依据什么、重复状态怎样处理、何时能保证找到/找到最优解、时间与空间为何爆炸。

## Leaf Topic Boundary v1

| Leaf Topic | Canonical Owns | Explicit Stop Boundary |
|---|---|---|
| **01 状态空间与无信息搜索** | problem/state/action/goal、tree search vs graph search、frontier、duplicate detection、BFS/DFS/UCS、completeness/optimality/time-space cost | 不拥有 heuristic；不拥有 complete-state neighborhood search；不拥有 game utility；不拥有 CSP constraint propagation |
| **02 启发式搜索与 A\*** | heuristic `h`、Greedy Best-First、A*、`g/h/f` 分工、admissibility、consistency、heuristic quality 与效率-保证权衡 | heuristic 可以来自人工或学习，但“怎样学 heuristic”回 Area 40/60；不拥有局部搜索的 neighborhood dynamics |
| **03 局部搜索与元启发式** | complete-state representation、neighborhood、move/operator、hill climbing、simulated annealing、local beam 等“不保留完整路径”的显式配置搜索 | 一旦更新由 gradient/Hessian 等连续局部微分信息主导，转 Area 50；一般 evolutionary optimization 先保留为 Extension，不自动扩成新 Owner |
| **04 对抗搜索与博弈树** | game state、player-to-move、utility/evaluation、minimax、alpha-beta、有限显式 chance tree 的 expectiminimax | stochastic game 中若核心变成 transition/value/policy 与长期效用，转 Area 70；不拥有一般 multi-agent learning |
| **05 约束满足问题 CSP** | variable/domain/constraint、constraint graph、backtracking、variable/value ordering、forward checking、arc consistency / propagation | 逻辑命题的语义与 entailment 回 Area 20；通用 search 技术只 Use 01/02；连续约束数值优化回 Area 50 |

### Internal Dependency DAG

```text
01 状态空间与无信息搜索
   ├──→ 02 启发式搜索与 A*
   ├──→ 03 局部搜索与元启发式
   ├──→ 04 对抗搜索与博弈树
   └──→ 05 CSP

02 / 03 / 04 / 05 是四种不同的“候选空间控制策略”，
不是从简单算法到高级算法的一条年表。
```

### Leaf 之间的最小判据

```text
保留 frontier / path cost          → 01 / 02
只维护当前完整候选 + neighborhood → 03
候选由对手行动交替产生            → 04
候选由变量-domain-constraint 定义 → 05
```

`03` 正式改名为“局部搜索与元启发式”，避免“组合优化”与 Area 50 的 optimization 语义冲突。

## Dependency / Export

```text
Uses:
Data Structures / Graph concepts

Exports to:
Area 20 symbolic planning：提供通用 search solver
Area 70 model-based planning / decision：提供 search subroutine，但不拥有 value/policy
Area 80 / NLP：提供 decoding search（如 beam search）的 search semantics
95 Directions: Robotics / Agents / Game AI
```

## Source Basis

AIMA 把 problem solving 独立组织为 search、adversarial search 与 CSP，这支持把“显式候选空间求解”作为稳定 Owner Domain；其他参考书主要从 ML/DL 角度展开，不应反向吞掉这一经典 AI 主干。

## Compression

> **Area 10 Own 的不是“所有寻找最优答案的方法”，而是：给定显式状态/动作/约束后，怎样组织候选空间的展开与选择。**
