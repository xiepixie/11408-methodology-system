# I01｜二维正态分布：三科汇流验收

状态：目录已建立，正文未建。

## Position

数学一跨三科 Integration。目标不是重新教授二维正态，而是检查多个成熟 Topic / Bridge 能否围绕同一个对象协作。

## Canonical Problem

给定二维 Gaussian 的参数或密度，解释其几何结构，并完成区域概率、边缘/条件、线性变换或独立性相关任务。

## Module Recognition

主要调用：

- B09 协方差矩阵 / 正半定二次型 / 主波动方向（核心跨科接口）；
- B03 Hessian / 二次型结构（用于比较二次型语言，不替代 B09 的概率二阶结构）；
- B06 概率积分语言；
- B07 随机变量变换与 Jacobian；
- 必要时 B00 / B02；
- 概率联合分布、条件分布、独立性 Topic。

## Composition Skeleton

$$
\text{Gaussian Object}
\to
\text{Quadratic Geometry}
\to
\text{Density / Support}
\to
\text{Coordinate Change or Marginalize}
\to
\text{Probability Result}
\to
\text{Normalization / Boundary Verification}
$$

## Boundary

本 Integration 不拥有二次型、Jacobian、联合密度、边缘化的基础定义。

## Anti-Bridge

不把“零协方差”无条件升级为“独立”；需要明确 Gaussian 等附加结构。

## 待重构

待 B09/B06/B07 与概率相关 Topic 成熟后再写完整母例与验证链；B03 只作为二次型语言的辅助对照。
