# B05｜线性方程与线性微分方程：一点 + Kernel

状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## Position

线性代数方程组 × 高数线性 ODE 的结构 Bridge，相对独立。

## 两侧 Owner

- 线代：线性映射、核、线性方程组与解空间；
- 高数：线性常微分方程、齐次/非齐次解结构。

## Mother Interface

线代：$Ax=b$；ODE：$L[y]=f$。共同结构：

$$
\boxed{\text{Solution Set}=\text{Particular Solution}+\ker L}
$$

## Owns

只拥有“非齐次解集为何是一个齐次核的仿射平移”这一共享结构，以及初始条件如何从解族中选定唯一轨迹的接口。

## Uses

线代 kernel/image、ODE 线性叠加与初值机制。

## Boundary / Anti-Bridge

- “特解 + 齐次解”依赖线性算子结构，不能推广到一般非线性 ODE；
- scalar differential operator 与普通有限维矩阵不是同一对象。

## Extension

常系数 ODE 特征根 ↔ companion matrix eigenvalue、matrix exponential 都是真连接，但不作为数学一主干展开。

## Source Diff

I-13 与线代 Topic04 的解空间正文已完成 Owner 复核；正文只保留“一点 + Kernel”接口。

## Manual

- Canonical Source：[线性方程与线性微分方程_一点加Kernel.tex](线性方程与线性微分方程_一点加Kernel.tex)
- Published View：[线性方程与线性微分方程_一点加Kernel.pdf](../../../90_publish/math1/线性方程与线性微分方程_一点加Kernel.pdf)

## Review v1
已核对非齐次解集是特解加齐次核的仿射平移，并区分有限维矩阵与微分算子。下一轮用非线性 ODE 反例、初值唯一性和解空间维数题验证。
