# AI Cross-Area Bridge Atlas

> 类型：Atlas
> 状态：已采用；Leaf Boundary v1 端点已登记。这里只登记跨 Area 稳定接口与 Candidate，不预建未成熟 Bridge 正文。

## Mother Question

> **当两个 Core Area 都已经有清楚 Owner，但一个概念链必须跨越两边才能说清时，接口到底传递什么？**

Bridge 不重新拥有两边机制，只拥有 **interface contract**。

## 当前 Core / Candidate Bridges

Leaf Boundary v1 已锁定后，Bridge 现在必须能指出**具体 Leaf 端点**；只写“Probability 和 ML 有关系”不再算合格接口。

| ID | Bridge | Canonical Endpoints | Interface Contract | 状态 |
|---|---|---|---|---|
| AI-B01 | Probability → Estimation / Loss | Area30-T01/T06 → Area40-T01/T02/T03 | distribution / likelihood / information measure → estimator / risk / learnable objective | Core Candidate |
| AI-B02 | AutoDiff → Backprop → Optimizer | Area50-T07 → Area60-T02 → Area50-T02/T03 | derivative computation → neural credit assignment → parameter update | Core Candidate |
| AI-B03 | Search / Symbolic Planning → Sequential Decision | Area10 + Area20-T05 → Area70-T02/T03 | explicit state/action/plan representation → value-aware sequential decision | Candidate |
| AI-B04 | Known-model Decision → Reinforcement Learning | Area70-T03 → T06/T07/T08 | Bellman / policy-improvement structure → experience-based estimation and improvement | Core Candidate |
| AI-B05 | Probability / Inference → Generative Modeling | Area30-T01/T04/T06 → Area80-T03/T05/T07 | latent / KL / posterior approximation / score-density language → generative objective and sampling path | Core Candidate |
| AI-B06 | Neural Function Approximation → Value / Policy Approximation | Area60-T01/T02/T03 → Area70-T06/T07 | parameterized neural function + gradient flow → approximated V/Q/π | Candidate |
| AI-B07 | Continuous Dynamics → Control / Diffusion / Flow | math ODE/SDE + Area70-T05 ↔ Area80-T05/T07 | trajectory/vector-field language → control or probability transport semantics | Extension Candidate |
| AI-B08 | Symbolic ↔ Probabilistic Representation | Area20 ↔ Area30-T01/T02 | explicit fact/relation semantics ↔ uncertain belief over facts/states | Extension Candidate |
| AI-B09 | Latent Inference ↔ Parameter Estimation / EM | Area30-T04 ↔ Area40-T01/T08 ↔ Area50 | infer hidden variables / construct bound → update model parameters → iterate | Candidate |

### 当前最重要的 Anti-Bridge

```text
Probability → Loss        ≠ “cross entropy 天生就是 classifier loss”
AutoDiff → Backprop       ≠ “reverse-mode AD 就是 optimizer”
Planning → Decision       ≠ “任何 plan 都等于 policy”
Bellman → RL              ≠ “MDP 就是 reinforcement learning”
Inference → EM            ≠ “E-step 和 M-step 都属于概率推断”
Neural Network → Deep RL  ≠ “用了网络以后 Bellman 结构失效”
```


## Bridge Promotion Gate

只有同时满足以下条件才建立独立 Bridge Handbook：

1. 两侧已有稳定 Owner；
2. 接口不是某个具体例子才成立；
3. 左侧输出、翻译过程、右侧输入可以明确写成 contract；
4. 该接口在多个 Topic / Integration 中重复出现；
5. 抽走具体应用后仍剩稳定机制。

否则只在相关 Area Atlas 中写 Use / Boundary。

## Stop Boundary

- 多个模块共同完成一次完整任务 → `90_综合专题/`，不是 Bridge；
- NLP/CV/Robotics/LLM 等纵向研究领域 → `95_研究方向/`；
- 两个概念只是“有点像” → Anti-Bridge，不建立文件夹；
- 单个模型的内部 section → 回对应 Leaf Topic。

## Compression

> **Bridge 只回答“为什么能接、接什么、保持什么”，不重新讲两边。**

## Review v1

本 Atlas 的 9 个候选已逐项核对端点和接口类型，暂不生成正文。AI-B01/B02/B04/B05 仍是 Core Candidate；AI-B03/B06/B09 是 Candidate；AI-B07/B08 是 Extension Candidate。下一步必须补足多个 Topic/Integration 的重复调用和竞争解释，再决定是否晋升独立 Handbook；当前不能把候选当作已完成 Bridge。
