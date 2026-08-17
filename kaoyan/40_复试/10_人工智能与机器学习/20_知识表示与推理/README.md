# 知识表示与推理 Area Atlas：把世界结构变成可操作的显式知识

> 类型：Atlas
> 状态：已采用；Area Boundary v1 + Leaf Boundary v1 已锁定。Leaf Topic 仅建立 Canonical 归属与依赖，不批量创建深度正文。

## Mother Question

> **当系统需要显式表达事实、对象、关系、规则和动作条件时，怎样建立有语义的表示，并通过合法推理得到新的结论或计划？**

本 Area 关注“显式知识怎样表示、怎样推”，而不是所有形式的 inference。概率推断属于 Area 30，数据驱动学习属于 Area 40。

## Canonical Ownership

本 Area 唯一拥有：

- propositional logic / first-order logic 的 AI 表示与语义；
- knowledge base、model、entailment、satisfiability 等显式知识对象；
- inference rule、proof/search for proof、soundness / completeness；
- unification、resolution、forward/backward chaining 等符号推理机制；
- ontology、category/relation/event 等 knowledge representation 结构；
- default / non-monotonic reasoning 等显式规则推理扩展；
- classical symbolic planning 中的 state/action/goal representation、action schema、precondition/effect、planning language；
- 符号规划内部的 plan representation、planning graph 等属于“规划表示与推理”的机制。

## Stop Boundary

本 Area **不拥有**：

- BFS / DFS / A* 等通用搜索器 → Area 10；
- Bayes network、posterior、belief propagation → Area 30；
- 从样本学习规则/参数/表示 → Area 40；
- numerical optimization → Area 50；
- neural representation / Transformer → Area 60；
- MDP/POMDP、value、policy、utility-based sequential decision → Area 70；
- generative model 的 density / sampling → Area 80。

### 三条必须锁死的边界

```text
Symbolic Inference ≠ Probabilistic Inference
Planning Representation ≠ Search Algorithm
Classical Planning ≠ MDP / Reinforcement Learning
```

## 边界判定

| 内容 | Owner | 判定理由 |
|---|---|---|
| proposition / FOL / entailment | Area 20 | 显式语义与逻辑后承 |
| unification / resolution | Area 20 | 符号替换与证明机制 |
| theorem proving 中调用 DFS/A* | Area 20 Own proof representation；Area 10 Own generic search | 表示/推理与搜索器分责 |
| STRIPS / PDDL / precondition-effect | Area 20 | symbolic action semantics |
| planning graph | Area 20 | 计划结构与约束传播 |
| stochastic planning with transition probabilities and value | Area 70 | 长期效用与随机转移成为主对象 |
| knowledge graph embedding | Direction / Area 40/60 视机制而定 | graph facts 的符号语义不等于 embedding learning |
| neuro-symbolic system | Cross-Area Bridge / Direction | 不创建第二套 logic 或 neural Owner |

## Shared Object Language

```text
World
→ Symbol / Sentence / Relation / Action Schema
→ Semantics / Model
→ Knowledge Base
→ Inference Rule
→ Derived Statement / Plan
```

任何 Topic 都必须区分：**syntax、semantics、inference**。如果只会按符号变形而说不清“这些式子代表什么世界”，就没有建立这个 Area 的核心模型。

## Leaf Topic Boundary v1

| Leaf Topic | Canonical Owns | Explicit Stop Boundary |
|---|---|---|
| **01 命题逻辑与逻辑智能体** | proposition、connective、interpretation/model、truth、entailment、satisfiability、KB、propositional inference 的语义闭环 | SAT 求解中用到的 generic search 不重新定义 Area 10；一阶量词与关系结构转 02 |
| **02 一阶逻辑与关系表示** | object/relation/function/predicate、quantifier、interpretation、term/formula、FOL semantics，把“对象之间的关系”显式化 | 不展开完整 theorem-proving algorithm；unification/resolution/chaining 的主机制转 03 |
| **03 Unification / Resolution 与自动推理** | substitution、unification、forward/backward chaining、resolution、proof procedure、soundness/completeness 与推理计算代价 | 通用 DFS/A*/search control 回 Area 10；概率化规则与 belief inference 回 Area 30 |
| **04 知识表示、本体与默认推理** | category/property/relation/event、ontology/description-style organization、default/non-monotonic reasoning、显式 commonsense structure | knowledge graph embedding / neural representation 回 Area 40/60；不确定信念回 Area 30 |
| **05 经典规划与动作模型** | state/action/goal 的 symbolic semantics、precondition/effect、STRIPS/PDDL-style action schema、plan representation、planning graph / planning-specific inference | BFS/A* 等通用 solver 回 Area 10；transition probability + utility/value/policy 出现后转 Area 70 |

### Internal Dependency DAG

```text
01 命题逻辑
   ├──→ 02 一阶逻辑与关系表示
   │       └──→ 03 自动推理
   ├──→ 04 知识表示 / 默认推理
   └──→ 05 经典规划与动作模型

Area 10 Search ──Use──→ 03 proof search / 05 plan search
```

### 最容易混淆的三组 Leaf Boundary

```text
02 FOL Representation
= “一句话在什么世界中是什么意思？”

03 Automated Inference
= “给定这些句子，怎样机械地推出结论？”

05 Classical Planning
= “怎样用显式 action semantics 表示并构造达成 goal 的动作序列？”
```

SAT / theorem proving / planning 都可能调用 search，但 **search control 不获得 knowledge semantics 的 Ownership**。

## Dependency / Export

```text
Uses:
Area 10 search as generic solver when needed

Exports to:
90 Integrations: reasoning/planning agents
95 Directions: Agents / Robotics / Neuro-symbolic AI
Area 70: symbolic model may become a decision model input，但 value/policy 由 Area 70 Own
```

## Source Basis

AIMA 将 Knowledge, Reasoning, Planning 作为独立于 problem solving、uncertainty 与 machine learning 的主部分，并以智能体统一这些能力，因此本 Area 保留经典 AI 的显式知识主梁，而不把它压进 ML。

## Compression

> **Area 20 Own 的是“显式世界模型 + 语义 + 合法推理”。搜索器可以替它找证明或计划，但搜索器不拥有知识语义。**
