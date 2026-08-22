# Attention 与 Transformer

> 类型：Topic Landing  
> 状态：待人工确认；Canonical LaTeX 工作稿已建立，当前正文已把 Attention 语义、Transformer 组合、FlashAttention、recurrent/linear attention、Attention Residuals、Kimi K3 三轴架构、Triton 实现接口与 backward 重计算组织到各自正确的解释层。

## 为什么值得打开

Attention 解决的不是“怎样再加一种神经网络层”，而是：**一个位置怎样根据当前内容，动态选择并汇总其他位置的信息。** Transformer 则把这种信息路由机制与残差、归一化、前馈子层和位置信息组合成可堆叠架构。

当序列变长以后，同一个 Attention 映射又会遇到第二个问题：朴素实现虽然数学语义正确，却会反复物化 $N\times N$ 中间矩阵并产生大量 device-memory 流量。FlashAttention 正是在不改变标准 Attention 数学语义的前提下，重新安排数据流与计算顺序。

## Mother Question

> **怎样让序列中的每个位置根据当前内容，动态选择并汇总其他位置的信息；Transformer 又怎样把这种路由机制组织成可堆叠的网络架构？**

当这套数学语义已经固定以后，本册再进入一个由工程瓶颈触发的实现分支：**长序列下，怎样在保持标准 Attention 数学语义的同时，减少大型中间矩阵带来的数据搬运？** FlashAttention 回答的是这个实现问题，不重新定义 Attention 本身。

## Scope / Stop Boundary

本 Topic Own：

- query / key / value 与 scaled dot-product attention；
- self-attention / cross-attention / causal attention；
- multi-head attention 与 positional information；
- Transformer block 的 architecture-level information flow；
- full Softmax Attention 与 recurrent/linear attention 的结构边界，以及 hybrid attention 的设计动机；
- KDA 作为 finite-state recurrent attention 的当前实例，以及 Gated DeltaNet → KDA → Gated DeltaNet-2 所揭示的 forget / erase / write 控制问题；
- Attention Residuals 作为 cross-depth representation routing，以及 Full / Block / Delta AttnRes 对“路由哪种 depth representation”的不同回答；
- Kimi K3 作为 sequence / depth / channel 三条架构轴同时优化的当前案例；Stable LatentMoE 只保留理解组合架构所需接口，不在本 Topic 展开一般 MoE 理论；
- stable softmax、online softmax 与 tiled exact attention；
- FlashAttention forward 的 $(m,l,O)$ 状态与 backward recomputation；
- 理解 FlashAttention 所必需的 CUDA execution / memory hierarchy 与 Triton blocked-program 接口；
- attention-specific backward：$\bar V,\bar P,\bar S,\bar Q,\bar K$ 的组合关系；工程代码中常把这些量命名为 `dV/dP/dS/dQ/dK`。

本 Topic 不 Own：

- generic JVP / VJP / reverse-mode AD → [Automatic Differentiation 与计算图求导](../../50_优化与学习计算/07_AutomaticDifferentiation与计算图求导/README.md)；
- optimizer / parameter update → Area 50；
- self-supervised learning setting → Area 40；
- autoregressive generative principle → Area 80；
- 完整 LLM 训练、推理、RAG、Agent 生命周期 → Area 90 / 95；
- 通用 CUDA/Triton 系统编程大全。本文只保留理解 Attention kernel 所需的实现层。

## Manual

- Canonical LaTeX：[Attention与Transformer.tex](Attention与Transformer.tex)
- 阶段性阅读版：[Attention与Transformer.pdf](../../../../90_publish/interview/Attention与Transformer.pdf)

阅读版 PDF 的标题页提供返回本 Landing Page 的链接；因此正文维护入口与发布阅读入口保持双向可达。当前状态仍是 `待人工确认`，发布只表示已有可阅读快照，不表示内容已经冻结。

## Read Next

```text
MLP / neural function
→ Attention as information routing
→ Multi-head + position
→ Transformer block
→ sequence-axis vs depth-axis vs expert/channel-axis routing
→ full attention / recurrent-linear / hybrid boundary
→ long-sequence implementation pressure
→ FlashAttention
→ attention-specific backward
```

若问题只是在问“reverse mode 为什么计算 $J^{\mathsf T}v$”，回到 Area 50 AutoDiff；若问题是在问“Attention 内部如何利用这个接口得到 $\bar Q,\bar K,\bar V$”，留在本册。

## Compression

```text
语义层：Q 提问，K 决定匹配，V 提供被汇总内容
架构层：Attention + residual/norm + FFN + position → Transformer
扩展层：sequence 轴可用 recurrent/linear/hybrid mixer；depth 轴可用 AttnRes；channel/parameter 轴可用 MoE 稀疏激活，三者不能混写
实现层：标准 Softmax Attention 可用 FlashAttention 避免物化完整 S/P；tile K,V 并维护在线 softmax 状态
反向层：保存少量行统计量，backward 重算 $P$，再直接生成 $\bar Q/\bar K/\bar V$
```
