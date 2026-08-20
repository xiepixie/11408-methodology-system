# 数学一 Integration Layer

状态：框架已采用，Integration 正文未建。

## 1. 定位

Integration 是 Knowledge Plane 的组合验收层：它不创造新的基础接口，而是选一个完整 Canonical Problem，检查学习者能否识别并组合已经成熟的 Topic / Bridge。

统一主线：

$$
\boxed{\text{Problem}\rightarrow\text{Module Recognition}\rightarrow\text{Module Composition}\rightarrow\text{Execution}\rightarrow\text{Verification}}
$$

## 2. 当前 Canonical Problems

| ID | Integration | 主要调用 | 定位 |
|---|---|---|---|
| I01 | [二维正态分布](I01_二维正态分布_三科汇流验收/README.md) | B09 为核心方向结构，兼用 B03/B06/B07/B00/B02 | 三科汇流验收 |
| I02 | [二维随机变量线性变换](I02_二维随机变量线性变换/README.md) | B02 + B06 + B07 | 变量变换与概率质量守恒验收 |
| I03 | [线性常微分方程组](I03_线性常微分方程组/README.md) | B05 | 组合能力验收；超出数学一核心的矩阵系统内容标 Extension |

## 3. 新建规则

以后不预先规划几十个 Integration。只有同时满足以下条件才新建：

1. 是高频或高价值完整问题；
2. 至少调用两个成熟 Topic / Bridge，或能显著验收一个 Bridge 的迁移；
3. 能暴露“单模块都会但不会组合”的真实断点；
4. 不需要为了完整问题重新创造大量基础理论。

如果删掉具体问题后仍剩一条稳定的 A ↔ B 新接口，应回到 Bridge，而不是继续扩张 Integration。
