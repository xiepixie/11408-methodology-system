# 生成模型 Area Atlas：学习生成规律并把模型变成样本

> 类型：Atlas
> 状态：已采用；Area Boundary v1 + Leaf Boundary v1 已锁定。Leaf Topic 仅建立 Canonical 归属与依赖，不批量创建深度正文。

## Mother Question

> **怎样表示并学习数据的生成规律，使系统能够计算或逼近数据分布、建模 latent structure，并从模型中产生新的样本？**

本 Area 的核心责任不是“用了神经网络”，而是 **distribution modeling + generative training principle + sampling path**。

## Canonical Ownership

本 Area 唯一拥有：

- generative modeling 的统一对象：`p(x)`、`p(x|c)`、likelihood、latent variable、sampling；
- autoregressive factorization 与 sequential generation；
- VAE 中 generative model / inference model / ELBO / reparameterization 的组合机制；
- GAN 中 implicit distribution、generator/discriminator game 与 adversarial training principle；
- diffusion / score-based model 中 forward noising、reverse generation、score / denoising objective；
- normalizing flow 中 invertible transformation / change-of-variables 的生成责任；
- flow matching / probability-flow / vector-field based generation 的生成机制；
- conditional generation、guidance 等跨模型生成控制机制在证据足够时的统一解释。

## Stop Boundary

本 Area **不拥有**：

- probability / Bayes / KL / entropy 的一般定义 → Area 30；
- generic MLE/MAP/generalization/evaluation protocol → Area 40；
- optimizer / AutoDiff → Area 50；
- encoder、decoder、Transformer、U-Net 等 neural backbone 的一般架构机制 → Area 60；
- optimal control / HJB / policy learning → Area 70；
- language / image / multimodal application direction → `95_研究方向/`。

### 四条必须锁死的边界

```text
Generative Model ≠ Neural Architecture
Autoencoder ≠ VAE
Diffusion Training ≠ Reverse Sampling
Autoregressive Modeling ≠ Transformer
```

- Transformer 可以承担 autoregressive model 的 backbone，但 autoregressive factorization 的 Owner 在 Area 80。
- plain deterministic autoencoder 主要是 representation/compression mechanism；只有加入 latent probabilistic generative semantics 后，VAE 才进入 Area 80。

## 边界判定

| 内容 | Owner | 判定理由 |
|---|---|---|
| density / likelihood / sampling 的生成语义 | Area 80 | generative responsibility |
| KL / entropy 定义 | Area 30 | information theory primitive |
| MLE 一般估计原则 | Area 40 | learning protocol |
| autoregressive factorization | Area 80 | generative decomposition |
| Transformer architecture | Area 60 | neural information flow |
| GPT-like LM | Area 80 Own AR principle + Area 60 Own Transformer；系统进入 Integration/Direction | 多 Owner 组合 |
| deterministic autoencoder | Area 60/40 | representation learning |
| VAE | Area 80 | latent probabilistic generation |
| GAN | Area 80 | adversarial generative principle |
| diffusion / score model | Area 80 | noising/reverse generation |
| Neural ODE general dynamics | Candidate Bridge / math extension | 不因可用于 flow 就由生成模型重定义 |
| normalizing flow / flow matching | Area 80 | generative transformation / vector-field path |
| GMM/KDE classical density estimation | Area 30/40 | 概率表示或 classical learning；Area 80 可作前驱比较但不复制 |

## Shared Object Language

```text
Data Distribution
→ Representation of p(x) / p(x|c)
→ Training Principle
→ Learned Density / Implicit Generator / Score / Vector Field
→ Inference or Sampling Path
→ Generated Sample
→ Quality / Coverage / Likelihood / Control
```

任何生成 Topic 都必须分开回答：**模型怎样表示分布、训练时学什么、生成时怎样采样**。这三件事不能混成“训练好了就生成”。

## Leaf Topic Boundary v1

| Leaf Topic | Canonical Owns | Explicit Stop Boundary |
|---|---|---|
| **01 生成建模统一语言：Density、Likelihood 与 Sampling** | explicit vs implicit density、likelihood tractability、latent variable、sampling、mode/coverage、training-vs-generation 三层责任，以及不同生成家族的统一比较坐标 | probability primitive 回 Area 30；MLE/generalization 一般协议回 Area 40；不替具体 family 展开机制 |
| **02 Autoregressive Models 与序列分解** | chain-rule factorization、teacher-forced next-step likelihood、causal/sequential generation、decoding distribution 与 sampling/search interface | Transformer/RNN backbone 回 Area 60；beam search 等 search algorithm 回 Area 10；语言任务进入 95 |
| **03 潜变量生成模型：VAE 与 ELBO** | latent generative model `pθ(x,z)`、inference model `qφ(z|x)`、ELBO、reparameterization、latent sampling / reconstruction-generation trade-off | KL/VI primitive 回 Area 30；encoder/decoder architecture 回 Area 60；plain autoencoder 不在此 |
| **04 GAN：隐式分布与对抗训练** | generator/discriminator game、implicit distribution、adversarial objective、distribution matching intuition 与 training pathology 的 generative semantics | generic min-max/numerical optimizer 回 Area 50；network backbone 回 Area 60 |
| **05 Diffusion / Score：加噪与逆生成过程** | forward noising、denoising/score learning、reverse-time generation、noise schedule、training objective 与 sampling solver 的分离 | SDE/ODE mathematics按需 Use；U-Net/Transformer backbone 回 Area 60；generic numerical integration不由生成模型重定义 |
| **06 Normalizing Flows：可逆变换与精确 Likelihood** | invertible transformation、change of variables、Jacobian determinant、exact likelihood 与 invertibility/expressivity-compute trade-off | Jacobian/概率变换基础回数学与 Area 30；不与 flow matching 合并为同一训练机制 |
| **07 Flow Matching 与连续输运** | time-dependent vector field、probability path / transport、flow-matching regression objective、ODE sampling path，以及与 probability-density control 的生成联系 | general Neural ODE / optimal control 回 Candidate Bridge / Area 70；generic ODE solver 不由本 Topic Own |

### Internal Dependency DAG

```text
01 Generative Modeling Language
   ├──→ 02 Autoregressive
   ├──→ 03 VAE / Latent Variable
   ├──→ 04 GAN
   ├──→ 05 Diffusion / Score
   ├──→ 06 Normalizing Flows
   └──→ 07 Flow Matching / Continuous Transport
```

这些 family 是对同一母问题的**不同分布表示 + 不同训练原则 + 不同 sampling path**，不是模型年代排序。

### 必须单独锁住的两组关系

```text
06 Normalizing Flow
= 可逆 map + change-of-variables + exact likelihood

07 Flow Matching
= learn vector field + probability path + ODE transport
```

二者共享“flow”一词，但不能因为名字相近合并 Owner。

`Conditional Generation / Guidance` 不再规划为独立 Leaf Topic。它跨 autoregressive、diffusion、flow 等多个 family，更适合作为 **Area 80 internal Bridge / Integration Candidate**：回答 condition 怎样进入 training / sampling，而不是建立第八套生成模型真相。

## Dependency / Export

```text
Uses:
Area 30 probability / information theory / inference
Area 40 estimation / generalization
Area 50 optimization
Area 60 neural architectures
ODE / SDE mathematics when required

Exports to:
90 Integrations: LLM generation / image generation / world models
95 Directions: NLP-LLM / Computer Vision / Multimodal / Scientific Generative Modeling
Area 70 world-model / generative-control interfaces
```

## Source Basis

Ye 把 VAE、GAN、Diffusion、Probability Density Control、Flow Matching 独立成 Generative Models 章节，并把信息论、SDE 放在补充材料；Murphy 则从概率模型、latent factors、VAE 与 sequence models 提供另一条路径。这支持把生成建模锁成独立 Area，但其概率、优化、网络骨架仍回到上游 Owner。

## Compression

> **Area 80 Own 的是：怎样把“数据来自什么生成规律”变成可学习模型，并明确区分训练原则与真正的 sampling path。**
