# 深度学习 Area Atlas：构造可训练的层级函数与表示

> 类型：Atlas
> 状态：已采用；Area Boundary v1 + Leaf Boundary v1 已锁定。Leaf Topic 仅建立 Canonical 归属与依赖，不批量创建深度正文。

## Mother Question

> **怎样用多层参数化函数形成高表达表示，并让信息与梯度能够穿过深层结构完成有效训练？**

本 Area 关注 neural network 作为 **function class + representation mechanism + trainable architecture**。它不等于 Machine Learning 全部，也不拥有所有训练目标或优化算法。

## Canonical Ownership

本 Area 唯一拥有：

- neural network / MLP 作为参数化函数族与 function approximator 的机制；
- depth、width、activation、composition 与 expressivity 的网络语义；
- neural computation graph 中 forward representation flow；
- backpropagation 作为神经网络中的 layer-wise credit assignment / gradient propagation；
- vanishing/exploding gradients、initialization、normalization、residual connection 等深网 trainability 机制；
- CNN 的 locality / parameter sharing / spatial inductive bias；
- RNN / gated recurrence 的 state-memory / sequence mechanism；
- attention / self-attention / multi-head / positional information 与 Transformer architecture；
- 只有真正改变 neural representation / information flow / inductive bias 的结构化网络机制，才可在本 Area 晋升 Topic。

## Stop Boundary

本 Area **不拥有**：

- supervised / self-supervised / transfer 等 learning setting 的一般定义 → Area 40；
- generalization、cross-validation、model selection 的一般协议 → Area 40；
- GD/SGD/Adam/Newton 与 generic AutoDiff → Area 50；
- probability / entropy / KL 的一般定义 → Area 30；
- MDP/Bellman/policy/value → Area 70；
- autoregressive / VAE / GAN / diffusion / flow 的生成原则 → Area 80；
- NLP/CV/Multimodal/LLM 作为任务与研究方向 → `95_研究方向/`。

### 三条必须锁死的边界

```text
Backprop ≠ Optimizer
Attention ≠ Transformer
Transformer ≠ LLM
```

- Backprop 负责“梯度怎样穿过网络”；optimizer 负责“拿到梯度后怎样更新参数”。
- Attention 是 information routing mechanism；Transformer 是围绕 attention 构造的 architecture family。
- LLM 是 Direction / Integration，会调用 Transformer、autoregressive modeling、optimization、decoding 等多个 Owner。

## 边界判定

| 内容 | Owner | 判定理由 |
|---|---|---|
| MLP / activation / depth | Area 60 | neural function class |
| universal approximation 的网络表达问题 | Area 60 | expressivity / approximation |
| reverse-mode AD 一般算法 | Area 50 | generic derivative computation |
| backprop in neural layers | Area 60 | neural gradient propagation |
| SGD / Adam | Area 50 | optimizer |
| dropout | Area 60 Own neural mechanism；Area 40 Own regularization/generalization concept | 机制与学习原则分责 |
| BatchNorm / LayerNorm / residual | Area 60 | trainability / information flow |
| CNN / RNN / Transformer | Area 60 | neural architecture |
| self-supervised objective | Area 40 | learning signal；具体 Transformer pretraining 为 Integration/Direction |
| GPT system | `90_综合专题` / `95_研究方向` | 多 Owner 组合，不另造 Transformer 真相 |
| VAE encoder/decoder network | Area 60 Own backbone；Area 80 Own VAE principle | architecture 与 generative objective 分责 |

## Shared Object Language

```text
Input
→ Parameterized Layers
→ Hidden Representation
→ Architecture / Inductive Bias
→ Objective Signal
→ Backward Credit Assignment
→ Trainability Dynamics
→ Learned Representation / Function
```

任何 neural Topic 都必须回答：信息怎样流、参数共享在哪里、结构假设是什么、梯度怎样流、深度为什么有用又为什么难训、该结构牺牲了什么。

## Leaf Topic Boundary v1

| Leaf Topic | Canonical Owns | Explicit Stop Boundary |
|---|---|---|
| **01 神经网络作为函数逼近器：MLP 与表达能力** | neuron/layer/composition、activation、depth/width、MLP、neural function class、universal-approximation-style expressivity question、architecture as parametric function | 不 Own gradient computation / optimizer；不展开 CNN/RNN/Attention 的结构归纳偏置 |
| **02 Backprop 与层级信用分配** | neural computation graph 上 forward cache、chain rule、reverse credit assignment、layer-wise gradient flow，以及“一个 loss signal 怎样分配到深层参数”的语义 | generic reverse-mode AD / JVP/VJP 回 Area 50；拿到 gradient 后的 SGD/Adam 回 Area 50 |
| **03 深网训练：初始化、归一化、残差与正则机制** | vanishing/exploding gradient、initialization、normalization、residual/skip connection、dropout 等 neural-specific trainability / optimization interaction | regularization/generalization 的一般原则回 Area 40；optimizer update rule 回 Area 50；具体 architecture branch 转 04–07 |
| **04 CNN：空间结构与参数共享** | convolution/pooling/common CNN block、local receptive field、translation-related inductive bias、parameter sharing、spatial feature hierarchy | image classification/detection/segmentation 任务体系进入 CV Direction；不 Own general convolution math outside neural role |
| **05 RNN：状态记忆与序列建模** | recurrence、hidden state、unrolling、BPTT 的 network semantics、gating/LSTM/GRU、long-term dependency 的 architecture problem | probabilistic temporal state estimation 回 Area 30；MDP state/policy 回 Area 70；autoregressive generative principle 回 Area 80 |
| **06 Attention 与 Transformer** | query/key/value、attention as information routing、self-/cross-attention、multi-head、positional information、Transformer block / architecture-level information flow | autoregressive LM objective 回 Area 80；self-supervised learning setting 回 Area 40；完整 LLM system 进入 90/95 |
| **07 结构化神经网络：GNN 等** **Candidate** | message-passing / graph-structured neural information flow，以及真正改变 representation topology 的结构化 neural mechanism | GraphML task ecosystem 回 95；若只是把已有 MLP/attention 应用到图数据，不足以晋升独立 Topic |

### Internal Dependency DAG

```text
01 Neural Function / MLP
   └──→ 02 Backprop / Credit Assignment
           └──→ 03 Deep Trainability

01 + 02 + 03 = shared neural base
   ├──→ 04 CNN
   ├──→ 05 RNN
   ├──→ 06 Attention / Transformer
   └──→ 07 Structured Neural Nets (Candidate)
```

04/05/06/07 是**不同 inductive bias / information-flow branches**，不是“CNN 过时以后换 RNN、再换 Transformer”的技术年表。06 也不要求先学会 05 才在知识结构上成立。

### Backprop / AutoDiff / Optimizer 三分契约

```text
Area 50 AutoDiff
= 给定 computation graph，怎样高效求 derivative

Area 60 Backprop
= neural loss 的信用怎样沿层级结构反向传播

Area 50 Optimizer
= 已知 gradient / curvature 后怎样更新 parameters
```

不再单独规划“Representation Learning”大 Topic：learning setting 与 supervision signal 回 Area 40；神经表示机制自然分布在各 architecture Topic。Embedding / pretraining 若形成稳定独立 Mother Question，再通过证据晋升。

## Dependency / Export

```text
Uses:
Area 40 learning / generalization contract
Area 50 optimization / AutoDiff
线性代数 + 微积分

Exports to:
Area 70：value / policy function approximator
Area 80：generator / encoder / decoder / score / vector-field backbone
95 Directions: CV / NLP-LLM / Multimodal / GraphML / Scientific ML
```

## Source Basis

Ye 从 Function Approximation → shallow/deep networks → Universal Approximation → Architecture Design → Training Criteria，再单设 Network Training；Murphy 将 DNN 独立为 Part III，并按 tabular / image / sequence 展开，序列部分继续到 attention / Transformer / language models。这支持把“神经函数与架构机制”锁为独立 Area，同时把 generic optimization 和 learning protocol 留给其他 Owner。

## Compression

> **Area 60 Own 的是：神经网络怎样表示复杂函数、信息怎样穿过层级结构、梯度怎样把学习信号传回这些表示。**
