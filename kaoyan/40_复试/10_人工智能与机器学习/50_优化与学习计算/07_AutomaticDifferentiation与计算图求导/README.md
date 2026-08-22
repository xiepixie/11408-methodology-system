# Automatic Differentiation 与计算图求导

> 类型：Topic Landing  
> 状态：待人工确认；Canonical LaTeX 工作稿已建立，已完成 reverse-mode AD、JVP/VJP、计算图、算子级 VJP 与 compute-memory trade-off 的第一版机制闭环。

## 为什么值得打开

大型张量程序的 Jacobian 往往大到不可能显式构造，但训练、优化和可微编程仍然需要导数。本 Topic 解释 Automatic Differentiation 如何把“构造整个 Jacobian”改写成“沿计算图传播 JVP / VJP”，以及为什么 scalar loss 对大量参数求梯度时 reverse mode 特别合适。

## Mother Question

> **一个由大量张量算子组成的程序，怎样在不显式构造巨大 Jacobian、也不依赖符号化简的前提下，高效得到下游真正需要的导数？**

## Scope / Stop Boundary

本 Topic Own：

- computation graph differentiation；
- forward-mode / reverse-mode automatic differentiation；
- JVP / VJP 与隐式 Jacobian 乘积；
- local derivative 怎样沿计算图组合；
- reverse accumulation 与共享依赖的梯度累积；
- forward state 保存、recomputation、checkpointing 的 compute-memory trade-off；
- custom differentiable operator 的 forward/backward contract；
- matmul、softmax 等典型 operator-level VJP。

本 Topic 不 Own：

- 导数、梯度、Jacobian 的基础数学定义 → 数学一高等数学；
- neural network 中 layer-wise credit assignment 的网络语义 → [Area 60 深度学习](../../60_深度学习/README.md) 的 Backprop Leaf；
- 拿到 gradient 后怎样更新 parameters → Area 50 的一阶/随机/二阶优化 Topic；
- Attention / FlashAttention 的具体 backward 结构 → [Attention 与 Transformer](../../60_深度学习/06_Attention与Transformer/README.md)。

## Manual

- Canonical LaTeX：[AutomaticDifferentiation与计算图求导.tex](AutomaticDifferentiation与计算图求导.tex)
- 阶段性阅读版：[AutomaticDifferentiation与计算图求导.pdf](../../../../90_publish/interview/AutomaticDifferentiation与计算图求导.pdf)

阅读版 PDF 的标题页提供返回本 Landing Page 的链接；因此正文维护入口与发布阅读入口保持双向可达。当前状态仍是 `待人工确认`，发布只表示已有可阅读快照，不表示内容已经冻结。

## Read Next

```text
多元微分 / 链式法则
        ↓
JVP / VJP / Reverse Mode
        ↓
Area 60 Backprop
        ↓
具体复合算子的 backward
```

FlashAttention backward 是一个很好的下游调用例：它使用本 Topic 的 VJP / recomputation 语言，但 Attention 的 $Q,K,V$ 语义、online softmax 与 tiled backward 仍由 Attention Topic Own。

## Compression

```text
程序 = 局部算子的组合
完整 Jacobian 通常不是目标
forward mode 传播 Jv
reverse mode 传播 J^T v
scalar loss + many parameters → reverse mode
保存中间量 ↔ backward 重算，是计算与内存之间的交换
```
