# B06A｜PDF 与 CDF：局部概率密度 × 累积

状态：目录已建立，正文未建。

## Position

高数积分基本定理 × 概率一维分布 Bridge；是 B06B、B07 的概率积分前置。

## 两侧 Owner

- 高数：定积分、变上限积分、FTC；
- 概率：随机变量、一维分布、CDF/PDF。

## Mother Interface

$$
F(x)=\int_{-\infty}^{x}f(t)\,dt,
$$

适当条件下：

$$
F'(x)=f(x).
$$

因此：

$$
\boxed{\text{Local Density}\rightarrow\text{Accumulation Function}\rightarrow\text{Recover Density}}
$$

## Owns

只拥有 PDF 与 CDF 之间“局部密度—累积—恢复”的 FTC 接口。

## Uses

高数一元累积 Topic、概率一维分布 Topic。

## Boundary / Anti-Bridge

- CDF 总存在，但 PDF 不一定存在；
- $F'(x)=f(x)$ 需要相应正则性，不能把离散分布硬写成普通密度；
- density 值不是概率本身。

## Extension

测度/Radon–Nikodym 视角不进入当前主干。

## 待重构

以后用概率 Topic 与高数 B03/FTC 相关材料做 Source Diff。
