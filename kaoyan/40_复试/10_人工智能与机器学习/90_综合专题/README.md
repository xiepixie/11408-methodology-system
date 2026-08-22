# AI Integration Atlas：把多个成熟机制跑成完整过程

> 类型：Atlas
> 状态：已采用；只拥有跨 Area 的完整过程，不拥有任何单点机制。

## Mother Question

> **当一个真实 AI 系统或任务同时调用多个 Area 时，这些模块按什么顺序交接，哪里发生状态变化，哪里最容易混淆责任？**

Integration 负责 Composition，不负责重新定义组件。

## 当前 Canonical Integration Candidates

```text
AI-I01 从数据到可用预测器
Problem / Task                         [Area40-T01]
→ Data / Split / Evaluation Contract  [Area40-T01]
→ Model Family                        [Area40-T02 → Area60-T01]
→ Probabilistic Assumption / Loss     [Area30 + AI-B01]
→ Estimation Principle                [Area40]
→ Numerical Optimization              [Area50]
→ Validation / Generalization         [Area40-T01]
→ Prediction

AI-I02 一个理性智能体闭环
Observe
→ Represent State / Belief
→ Infer
→ Search / Decide
→ Act
→ Receive Feedback
→ Learn / Update

AI-I03 一个现代语言模型训练与推理生命周期
Token / Context
→ Neural Representation
→ Transformer
→ Autoregressive Objective
→ Optimization
→ Decoding / Search
→ Output

AI-I04 现代 LLM 应用系统
Context Assembly
→ Retrieval / RAG
→ Model Generation
→ Tool Calling
→ Agent / Workflow State
→ External Capability via MCP
→ Evaluation / Security / Observability
```

AI-I04 的正式入口：

- [现代 LLM 应用系统：Context、Retrieval、RAG、Agent、Workflow 与 MCP](AI-I04_现代LLM应用系统/README.md)

## Ownership Rule

Integration 中只允许写：

- 哪一步调用哪个 Owner；
- 模块之间传递什么状态/对象；
- 完整生命周期中的顺序、分支和 failure；
- 跨模块 verification。

不允许在这里重新定义：Bayes、A*、SGD、Transformer、Bellman、Diffusion 等机制。

## Stop Boundary

- 单一机制的完整理论 → 对应 Area / Leaf Topic；
- 两个机制之间的稳定接口 → `85_跨域桥梁/`；
- 一个长期研究领域的地图、论文路线和研究问题 → `95_研究方向/`。

## Compression

> **Integration 的问题不是“它是什么”，而是“多个已经会的东西怎样在一次完整任务里接起来”。**
