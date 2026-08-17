# B06A｜PDF 与 CDF：局部概率密度 × 累积

状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

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

## Source Diff

概率一维分布 Topic 与高数 FTC 相关材料已完成 Owner 复核；正文只保留 CDF/PDF 层级和正则性边界。

## Manual

- Canonical Source：[PDF与CDF_局部概率密度与累积.tex](PDF与CDF_局部概率密度与累积.tex)
- Published View：[PDF与CDF_局部概率密度与累积.pdf](../../../90_publish/math1/PDF与CDF_局部概率密度与累积.pdf)

## Review v1
已核对 CDF、PDF、区间概率和 FTC 正则性，明确密度值不是点概率。下一轮用含跳点 CDF、无密度分布和端点概率题验证。
