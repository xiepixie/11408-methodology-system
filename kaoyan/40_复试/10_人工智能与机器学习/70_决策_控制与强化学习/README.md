# 决策、控制与强化学习 Area Atlas：从 belief 到长期行为

> 类型：Atlas
> 状态：已采用；Area Boundary v1 + Leaf Boundary v1 已锁定。Leaf Topic 仅建立 Canonical 归属与依赖，不批量创建深度正文。

## Mother Question

> **当系统必须采取行动，而行动会影响未来状态与后续信息时，怎样把 belief、utility / reward、dynamics 和 experience 组织成可改进的长期 policy？**

本 Area 负责从“知道/相信什么”进一步走到“应该做什么”，并把一次性 decision、known-model sequential decision、continuous control 与 reinforcement learning 放在同一条决策主线上。

## Canonical Ownership

本 Area 唯一拥有：

- decision theory 中 utility、loss/risk、Bayes action 等 action-selection 语义；
- MDP：state、action、transition、reward/cost、policy、return；
- value function、Q function、Bellman operator / equation；
- dynamic programming：policy evaluation / improvement、value iteration、policy iteration；
- POMDP / belief-state decision 中的 decision layer；
- continuous optimal control 的 trajectory / dynamics / cost 语义，以及 HJB、PMP 等控制最优性主线；
- model-free RL：Monte Carlo、TD、Q-learning 等 value-based learning；
- policy gradient、actor-critic 等 policy optimization；
- model-based RL、exploration / exploitation、planning-learning interaction 的 RL 责任。

## Stop Boundary

本 Area **不拥有**：

- 通用 state-space search / A* / game-tree search → Area 10；
- symbolic action schema / STRIPS / PDDL → Area 20；
- belief update、filtering、probabilistic inference 本身 → Area 30；
- architecture-agnostic supervised/unsupervised learning protocol → Area 40；
- generic numerical optimizer → Area 50；
- neural value/policy approximator 的 network mechanism → Area 60；
- generative world model / diffusion policy 等生成机制 → Area 80。

### 四条必须锁死的边界

```text
Planning Representation ≠ Sequential Decision
Search ≠ Dynamic Programming
MDP ≠ Reinforcement Learning
Deep RL ≠ New Neural Network Theory
```

- MDP / Bellman 是问题与最优性结构；RL 是在未知 value/model 或只能通过 experience 获得信息时学习。
- Deep RL 是 Area 70 调用 Area 60 的 Integration，不重新定义 MDP，也不重新定义 neural network。

## 边界判定

| 内容 | Owner | 判定理由 |
|---|---|---|
| Bayes action / expected utility | Area 70 | belief → action |
| MDP / policy / value / Bellman | Area 70 | sequential decision core |
| value iteration / policy iteration | Area 70 | dynamic programming for decision |
| A* 路径搜索 | Area 10 | frontier expansion |
| STRIPS planning | Area 20 | symbolic action semantics |
| POMDP belief update | Area 30；POMDP policy/value | Area 70 | inference 与 decision 分责 |
| HMM/Kalman filtering | Area 30 | state estimation，不直接选择 action |
| optimal control / HJB / PMP | Area 70 | continuous sequential decision |
| Q-learning / TD | Area 70 | experience-based value learning |
| policy gradient objective | Area 70；optimizer | Area 50 | decision objective 与 numerical solver 分责 |
| DQN / PPO network architecture | Area 60 Own network；Area 70 Own RL mechanism | Deep RL 为 Integration |
| AlphaZero-like system | `90_综合专题` / Direction | search + neural + RL 多 Area 组合 |

## Shared Object Language

```text
State / Belief
→ Action
→ Transition / Dynamics
→ Reward / Cost
→ Return
→ Value
→ Policy
→ Experience / Exploration
→ Policy Improvement
```

所有 Topic 都必须回答：当前决策影响哪个未来、价值函数在压缩什么未来信息、Bellman 为什么能递归、已知模型和未知模型的分界在哪里、exploration 为什么是学习独有问题。

## Leaf Topic Boundary v1

| Leaf Topic | Canonical Owns | Explicit Stop Boundary |
|---|---|---|
| **01 决策论：Utility、Risk 与 Bayes Action** | action space、utility/loss、expected utility/risk、Bayes action、prediction → action 的一阶段 decision contract | posterior/belief 怎样算回 Area 30；一旦 action 改变未来并出现 transition/return，转 02 |
| **02 MDP：状态转移、回报、价值与策略** | Markov state、action、transition kernel、reward/cost、discounted/finite-horizon return、policy、value/Q 的问题表示 | 不 Own 具体求解 algorithm；known-model Bellman/DP 转 03，experience-based learning 转 06/07 |
| **03 Bellman 递推与 Dynamic Programming** | Bellman operator/equation、policy evaluation/improvement、value iteration、policy iteration，以及 known-model sequential decision 的 recursive solution | A* frontier search 回 Area 10；未知 model/value 下从 experience 学习转 06/07/08 |
| **04 POMDP：Belief State 与不完全可观测决策** | partial observability 下 belief-as-state、belief-MDP decision semantics、observation-action-history 与 policy | filtering / Bayesian belief update primitive 回 Area 30；不复制 HMM/Kalman inference |
| **05 Optimal Control：HJB、PMP 与连续系统** | continuous state/control、dynamics/trajectory/cost、Euler-Lagrange/Hamiltonian/PMP/HJB 的 control optimality structure | generic constrained optimization 回 Area 50；Neural ODE / learned dynamics 只在 Integration/Direction 调用 |
| **06 Value-Based RL：MC、TD 与 Q-Learning** | return estimation、bootstrapping、MC/TD、SARSA/Q-learning、on/off-policy value learning、exploration 进入 value learning 的责任 | function approximator 回 Area 60；optimizer 回 Area 50；model-based planning 转 08 |
| **07 Policy Gradient 与 Actor-Critic** | policy parameterization 的 decision semantics、policy-gradient theorem/REINFORCE、baseline、actor-critic、value-policy coupling | gradient optimizer 回 Area 50；network architecture 回 Area 60；PPO 等具体算法先作为本 Topic section/extension，不自动新建 Leaf |
| **08 Model-Based RL、Exploration 与 Planning** **Candidate** | learned/known model 如何参与 policy improvement、planning-learning loop、exploration/exploitation 与 model usage 的 RL-level composition | environment model 的 supervised estimation回 Area 40；search planner 回 Area 10；world-model generative mechanism 回 Area 80 |

### Internal Dependency DAG

```text
01 One-step Decision
   └──→ 02 MDP / Sequential Decision
           ├──→ 03 Bellman / Dynamic Programming
           ├──→ 04 POMDP Decision
           └──→ 05 Continuous Optimal Control

02 + Bellman idea
   ├──→ 06 Value-Based RL
   └──→ 07 Policy Gradient / Actor-Critic

03 + 06/07 + learned model
   └──→ 08 Model-Based RL (Candidate)
```

这里要形成一个非常稳定的分叉：

```text
Model / transition known, solve decision problem → 03
Information must come from experience          → 06 / 07 / 08
Continuous trajectory / dynamics is主对象      → 05
Partial observability changes decision state   → 04
```

`Multi-armed Bandit` 暂不单独晋升 Leaf；它作为“01 decision → exploration/learning”的最小过渡模型，放在 06/08 的基础 section 中观察。若后续重复调用足够高再晋升。

`Deep RL` 不规划成独立 Core Topic；默认进入 Integration，因为它主要是 `Area 70 decision/RL mechanism + Area 60 function approximator + Area 50 optimizer`。

## Dependency / Export

```text
Uses:
Area 30 uncertainty / belief update
Area 40 model learning when dynamics/reward are learned
Area 50 optimization
Area 60 function approximation when deep
Area 10 search when model-based planning calls explicit search
ODE / dynamical systems mathematics when continuous

Exports to:
90 Integrations: Deep RL / AlphaZero-like systems / agent loops
95 Directions: Robotics / Agents / Game AI / Embodied AI
World-model research routes
```

## Source Basis

AIMA 用 rational agent 把 uncertainty 后的 decision、sequential decision、multi-agent decision 与 learning 接到行动；Murphy 把 Decision Theory 放在 ML Foundations 并在导论中保留 RL；Ye 更明确给出 Optimal Control → Deep Reinforcement Learning 的连续数学主线。因此这里用“Decision → MDP/Control → RL”统一，而不是把 RL 孤立成一堆算法。

## Compression

> **Area 70 Own 的是：行动会改变未来时，怎样把 dynamics、utility/reward、value 与 experience 压缩成 policy，并持续改进它。**
