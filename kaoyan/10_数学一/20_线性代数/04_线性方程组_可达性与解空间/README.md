# 线性方程组：可达性与解空间

> 状态：Canonical 第二轮心智模型深化与三本 Active Practice 优化已完成；待人工确认后同步正式发布版 PDF。

## 为什么值得读

“齐次方程、非齐次方程、基础解系、通解、无解/唯一/无穷多”看起来像很多章节，其实都来自同一个问题：

> **给定目标 $b$，它是不是 $A$ 能到达的输出；若能，所有到达它的输入长什么样？**

一旦把 $Ax=b$ 看成“求点 $b$ 的逆像”，全部结构会压成一个 fiber 模型：

$$
\mathcal F_A(b)=
\begin{cases}
\varnothing,&b\notin\operatorname{Im}A,\\
x_0+\ker A,&b\in\operatorname{Im}A.
\end{cases}
$$

更深一层，非空 fiber 正是 $\ker A$ 的陪集：

$$
\mathbb R^n/\ker A\cong\operatorname{Im}A.
$$

因此“是否有解、解集自由度、公共解/包含/同解”都只是对 fiber 的存在性、内部结构与集合关系进行不同询问。

## 母问题

> **给定输出 $b$ 是否可达；若可达，所有到达它的输入组成什么结构？**

主线是：

```text
Ax = b
-> b 是否属于 Im(A)
-> 若否：无解
-> 若是：找一个特解 x0
-> 全部解 = x0 + ker(A)
-> kernel 维数决定唯一 / 无穷多
-> 两个系统：比较 fiber 的交 / 包含 / 相等
-> 特殊结构：转 Topic02/03 取得 image/kernel 信息后再回来交付
```

## 本册覆盖到哪里

本 Topic 负责：

- $Ax=b$ 的可达性、增广 rank 与左零空间无解证书；
- 齐次方程、kernel 与基础解系；
- 非齐次解集的“特解 + kernel”结构；
- 多个已知非齐次解之间的差与仿射组合；
- 无解、唯一解、无穷多解的统一分类；
- 消元为何保持原未知量解集；
- 参数方程组；
- Cramer 法则的结构位置；
- $AX=B$、$XA=B$ 等矩阵方程；
- 齐次/非齐次系统的公共解、包含与同解关系；
- fiber / kernel 陪集模型、固定 $A$ 时不同右端 fiber 的平行与不交结构；
- 跨 Topic02/03 的高信号结构路由，而不重复拥有 rank、伴随、Gram 等理论。

本 Topic **不负责**：

- rank、kernel/image 的本体与矩阵等价；
- 特征值、相似与对角化；
- 二次型合同、惯性与正定。

## 训练导航

- [参数方程组与通解结构](参数方程组与通解结构.md) —— 普通/参数系统的相容性、无/唯一/无穷多分类、基础解系、特解 + kernel；新增参数位置分流、左零空间相容性证书、RREF 停止条件、命题量词审计、跨专题 Bridge 与 First Divergence；
- [矩阵方程与 Cramer 边界](矩阵方程与Cramer边界.md) —— $AX=B$ 看列空间、$XA=B$ 看行空间；新增矩阵空间线性映射、存在性/唯一性/自由度直接判定、Cramer 失败后的 fiber 回退与 First Divergence；
- [公共解与同解问题](公共解与同解问题.md) —— 把公共解/包含/同解统一为两个 fiber 的交/偏序/相等；新增 product-map 堆叠机制、交集方向 $\ker A\cap\ker C$、非齐次包含增广行空间判据、表示层级、跨 Topic Bridge 与 First Divergence。

## 与其他册怎样连接

- 上位地图：[线性代数 Subject Atlas](../README.md)
- 前置：[秩、基本子空间与等价](../03_秩_基本子空间与等价/README.md)
- 矩阵与 determinant：[线性映射、矩阵与行列式](../02_线性映射_矩阵与行列式/README.md)
- 下一册：[特征结构：相似与对角化](../05_特征结构_相似与对角化/README.md)

## 正文与发布

- Canonical LaTeX：[线性方程组_可达性与解空间.tex](线性方程组_可达性与解空间.tex)
- Published PDF：[线性方程组_可达性与解空间.pdf](../../../90_publish/math1/线性方程组_可达性与解空间.pdf)

旧 [Markdown 工作稿](线性方程组：可达性与解空间.md) 保留为 Source Diff 记录，不再作为正文 Owner。
