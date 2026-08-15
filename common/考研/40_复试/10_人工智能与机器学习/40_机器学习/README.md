# 机器学习 Area Atlas：从经验中选择能泛化的模型

> 类型：Atlas
> 状态：已采用；Area Boundary v1 + Leaf Boundary v1 已锁定。Leaf Topic 仅建立 Canonical 归属与依赖，不批量创建深度正文。

## Mother Question

> **当规则或映射无法直接手写时，怎样利用有限数据/经验选择模型，使它不仅拟合已有样本，还能在未见样本上继续工作？**

本 Area 的核心是 **learning problem + estimation + generalization**。它不以“模型名字”组织，而先问任务、经验、假设空间、目标、估计器和泛化。

## Canonical Ownership

本 Area 唯一拥有：

- supervised / unsupervised / semi-supervised / self-supervised / transfer 等 learning setting 的一般语义；
- train / validation / test、empirical risk、expected risk、generalization、overfitting / underfitting；
- MLE、MAP、ERM、regularized ERM 等**模型学习/估计原则**；
- cross-validation、model selection、hyperparameter tuning、baseline、evaluation protocol；
- architecture-agnostic regularization 与 bias-variance / model complexity 的学习责任；
- 经典模型族及其学习机制：linear/logistic/GLM、kNN、kernel/SVM、trees/ensembles；
- classical dimensionality reduction / clustering / mixture-based learning 的“从数据学结构”责任；
- learning with fewer labels / transfer / semi-supervised / self-supervised 等数据与监督信号范式。

## Stop Boundary

本 Area **不拥有**：

- Bayes rule、conditional independence、posterior inference 的一般概率语义 → Area 30；
- 梯度下降、SGD、Newton、KKT 等优化算法 → Area 50；
- neural architecture、backprop、CNN/RNN/Transformer 的内部机制 → Area 60；
- sequential action / return / policy learning → Area 70；
- VAE/GAN/diffusion/flow 等专门生成模型族 → Area 80；
- NLP/CV/Robotics 等应用方向 → `95_研究方向/`。

### 最关键的边界：Learning Principle 与 Solver

```text
What objective / estimator should represent learning?
How do we evaluate generalization?
= Area 40

Given that objective, how do we numerically minimize it?
= Area 50
```

因此：

```text
MLE ≠ Gradient Descent
Regularization ≠ Weight Update Algorithm
Cross-validation ≠ Training Algorithm
```

## 边界判定

| 内容 | Owner | 判定理由 |
|---|---|---|
| linear / logistic regression 的模型与估计 | Area 40 | hypothesis + estimator + generalization |
| Gaussian likelihood 为什么导出 least squares | Area 40 Use Area 30 | learning objective 的构造 |
| closed-form least squares / numerical solve | Area 40 Own estimator；数学/Area 50 Own solver as needed | 估计原则与计算实现分责 |
| SVM / margin / kernel learning | Area 40 | learning model family |
| decision tree / random forest / boosting | Area 40 | classical learning model family |
| PCA 用作 data representation learning | Area 40 | 从样本估计低维结构；线代只提供机制 |
| GMM | Area 30 Own mixture distribution / latent-variable inference；Area 40 Own clustering / parameter-learning usage | representation / inference 与 learning protocol 分责 |
| self-supervised learning paradigm | Area 40 | supervision signal / learning setting |
| neural pretraining architecture | Area 60 Use Area 40 | neural mechanism 与 learning paradigm 分责 |
| deep generative model | Area 80 | generation responsibility 独立成域 |

## Shared Object Language

```text
Task
→ Data / Experience
→ Hypothesis / Model Family
→ Objective / Estimator
→ Fitting
→ Validation / Selection
→ Generalization
→ Prediction / Representation
```

每个 Topic 都必须区分：**task、model family、objective、optimizer、metric**。如果五者混成一句“这个算法就是……”，认知边界即视为失败。

## Leaf Topic Boundary v1

| Leaf Topic | Canonical Owns | Explicit Stop Boundary |
|---|---|---|
| **01 学习问题、估计、泛化与模型选择** | task/experience/performance、supervised vs unsupervised 基本 learning contract、ERM/MLE/MAP/regularized estimation、train/val/test、bias-variance、overfitting、generalization、CV/model selection/evaluation | 不展开具体 model family；objective 的 numerical minimization 回 Area 50；概率量定义回 Area 30 |
| **02 线性预测模型：Linear Regression、Logistic 与 GLM** | linear predictor、regression/classification link function、least-squares / likelihood-based fitting 的 model-level semantics、regularized linear models | Gaussian/Bernoulli 等 distribution primitive 回 Area 30；solver 回 Area 50；LDA/Naive Bayes 等“建模 class-conditional density”的路线转 03 |
| **03 生成式分类：LDA、QDA、Naive Bayes 与判别边界** | class-conditional modeling、Bayes classifier、LDA/QDA、Naive Bayes，以及 generative-vs-discriminative classification 的模型比较 | 一般 Bayesian inference 回 Area 30；Logistic/GLM 主体回 02；现代 deep generative modeling 回 Area 80 |
| **04 实例方法与非参数学习** | nearest-neighbor / exemplar-based prediction、distance/metric、KNN、kernel density/regression 的 classical nonparametric learning responsibility | Mercer kernel / margin machine 转 05；deep metric representation 回 Area 60 / Direction |
| **05 Kernel、SVM 与大间隔方法** | feature-space / kernel trick、maximum-margin classification、soft margin、kernel SVM / kernel ridge 的 learning mechanism | kernel 线性代数/函数分析只按需 Use；numerical QP solver 回 Area 50 |
| **06 决策树、森林、Bagging 与 Boosting** | recursive partition、tree fitting/pruning、bagging/random forest、stagewise/gradient boosting、ensemble bias-variance intuition | gradient boosting 的“gradient”不把 Owner 迁到 Area 50；Area 50 只 Own generic optimizer |
| **07 降维、PCA 与经典潜变量表示** | PCA / low-dimensional representation、factor-analysis-style classical latent representation、reconstruction/variance view、dimensionality selection | SVD/EVD 本体回线代；neural autoencoder architecture 回 Area 60；VAE generative semantics 回 Area 80 |
| **08 聚类：K-Means、混合模型与谱方法** | clustering objective/assignment、K-Means、mixture-based clustering usage、hierarchical/spectral clustering 的 learning responsibility | mixture distribution/inference 回 Area 30；EM 的 generic optimization interface 视 Area 30/40/50 Bridge；不把 density-generation 全部迁入 Area 80 |
| **09 数据与监督机制：迁移、半监督、自监督与少标签学习** | supervision signal / data regime、transfer/fine-tuning protocol、semi-supervised/self-supervised/active/few-shot/meta-learning 的一般 learning contract | 具体 neural pretraining architecture 回 Area 60；具体 downstream NLP/CV system 进入 90/95 |

### Internal Dependency DAG

```text
01 Learning Contract / Generalization
   ├──→ 02 Linear / GLM
   ├──→ 03 Generative Classifiers
   ├──→ 04 Nonparametric / KNN
   ├──→ 05 Kernel / SVM
   ├──→ 06 Trees / Ensembles
   ├──→ 07 Dimensionality / Latent Representation
   ├──→ 08 Clustering
   └──→ 09 Data & Supervision Regimes

02–08 是 model/task-family branches，不构成“越来越高级”的线性阶梯。
09 是横切 learning regime，可调用 02–08，也可调用 Area 60 neural models。
```

### 三条 Leaf 级边界

```text
Learning Contract (01) ≠ Model Family (02–08)
Model Family ≠ Numerical Solver (Area 50)
Self-supervised / Transfer (09) ≠ Neural Architecture (Area 60)
```

`Representation Learning` 不单独由 Deep Learning 自动拥有：若重点是 **learning signal / data regime**，Owner 在 09；若重点是 **neural information flow / architecture**，Owner 在 Area 60。

## Dependency / Export

```text
Uses:
Area 30 probability / information theory / inference
Area 50 numerical optimization
数学一线代 / 概率 / 微积分

Exports to:
Area 60 neural learning：提供 learning contract / evaluation / generalization
Area 70：提供 function/model learning principles，但 policy semantics 不外包
Area 80：提供 estimation/generalization contract，但 generative mechanism 不外包
95 Directions
```

## Source Basis

Murphy 以 Foundations → Linear Models → DNN → Nonparametric → Beyond Supervised Learning 展开 ML，并明确讨论 supervised/unsupervised/generalization；《Models Demystified》又把 model、estimation、metrics、uncertainty、model selection 分开。这支持把“学习协议与经典模型族”从 Optimization 和 Deep Learning 中独立出来。

## Compression

> **Area 40 Own 的不是“所有从数据跑出来的算法”，而是：怎样定义学习问题、从经验估计模型，并判断它是否真的泛化。**
