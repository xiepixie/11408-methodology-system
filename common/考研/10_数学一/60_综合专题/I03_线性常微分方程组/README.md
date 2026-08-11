# I03｜线性常微分方程组

状态：目录已建立，正文未建；部分内容属于 Extension 验收。

## Position

主要用于验收 B05“特解 + Kernel”结构。标准数学一只要求标量常微分方程，因此矩阵系统只作为真实结构 Extension，不反向扩张考纲主干。

## Canonical Problem

使用最简单二维系统：

$$
X'(t)=AX(t)+f(t)
$$

观察齐次/非齐次、解空间、初值选择和特征结构怎样共同工作。

## Module Recognition

- B05：线性方程与线性微分方程；
- 线代线性映射/特征结构 Topic；
- 高数 ODE Topic。

## Composition Skeleton

$$
\text{Evolution Law}
\to
\text{Homogeneous Operator}
\to
\ker L
\to
\text{Particular Solution}
\to
\text{Affine Solution Family}
\to
\text{Initial Data Selects One Trajectory}
$$

## Boundary

- 不把矩阵指数作为数学一必会求解工具；
- 不把有限维矩阵与微分算子混成同一对象；
- 只有线性结构才支持“特解 + 齐次核”的统一形式。

## Extension

companion matrix、matrix exponential 与一阶系统谱结构都留在本 Integration 的 Extension 段。

## 待重构

待 B05 和高数 ODE Topic 成熟后再决定保留到什么解释深度。
