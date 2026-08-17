# AI Research Direction Atlas：纵向研究路线的调用地图

> 类型：Atlas
> 状态：已采用；这里只负责研究方向 Routing，不复制 Core Area 的机制。

## Mother Question

> **当未来决定深入某个研究方向时，这个方向真正解决什么研究问题，它调用哪些 Core Area，又有哪些只属于该方向的新机制？**

Direction Atlas 是“竖杠”，不是第二套 AI 教材。

## 当前候选方向

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

这些目录**现在不批量创建**。只有真实开始方向探索时再建立对应 Direction Atlas。

## Direction Ownership Rule

一个 Direction Atlas 可以 Own：

- 该方向独有的 Mother Question；
- 任务族、数据形态、benchmark / evaluation landscape；
- Core Area 的调用图；
- 该方向特有、无法合理归入现有 Core Area 的新机制；
- 论文阅读路线、研究问题树、开放问题与实验范式。

但它不能重新 Own：

- Transformer / CNN / GNN 等通用 neural architecture → Area 60；
- autoregressive / diffusion / VAE 等 generative principle → Area 80；
- SGD / Adam / KKT → Area 50；
- Bayes / KL / inference → Area 30；
- MDP / Bellman / RL → Area 70；
- search / CSP → Area 10。

## 方向晋升判据

建立独立 Direction Atlas 前至少确认：

1. 有稳定的研究母问题，而不只是一个产品名；
2. 会长期调用多个 Core Area；
3. 有自己的任务/数据/评价/研究文献生态；
4. 学习深度已经超过单个 Integration；
5. 建立后能减少混写，而不是复制 Core 机制。

## 示例：LLM 为什么不是 Core Area

```text
Language / Reasoning Task
+ Transformer Architecture          ← Area 60
+ Autoregressive Modeling           ← Area 80
+ Cross Entropy / Information       ← Area 30
+ Estimation / Generalization       ← Area 40
+ Optimization                      ← Area 50
+ Decoding / Search                 ← Area 10
+ RL / Preference-based Decision    ← Area 70 when applicable
= NLP / LLM Direction + Integrations
```

## Compression

> **Core Area 负责“可复用机制是什么”；Direction 负责“一个研究领域怎样组合这些机制，并产生自己的新问题”。**
