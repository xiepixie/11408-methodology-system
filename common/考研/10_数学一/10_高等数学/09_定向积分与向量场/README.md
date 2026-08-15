# 定向积分与向量场

> 状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## Hook

曲线和曲面积分的第一动作不是代参数，而是辨认“什么场乘什么微元”，再确认方向、边界和奇点是否允许使用转换定理。

## Mother Question

标量/向量场如何与长度、面积、切向位移和法向面积结合；当边界和内部足够正则时，怎样在直接计算与 Green、Stokes、Gauss 之间选择最短路径？

主线：

$$
\boxed{
\text{Field Type / Carrier}
\to\text{Orientation / Parametrization}
\to\text{Microelement}
\to\text{Direct or Boundary Theorem}
\to\text{Domain / Singularity Audit}
\to\text{Invariant Check}}
$$

## Scope / Stop Boundary

本册负责第一型曲线/曲面积分、第二型曲线/曲面积分、参数化与投影、保守场与路径无关、Green、Stokes、Gauss 的定向和资格，以及补线、补面、挖洞与物理量复核。

本册停在定向积分与考试级向量场机制：

- 空间对象、参数域、法向表示由 [Topic06](../06_空间对象与方向表示/README.md) 提供；
- 无向二重/三重累积与坐标换元由 [Topic08](../08_高维累积_区域坐标与Jacobian/README.md) 提供；
- 梯度与局部可微语言由 [Topic07](../07_多元局部模型_可微梯度隐函数与极值/README.md) 提供；
- 内积、正交与投影的跨学科解释由 [B00](../../50_桥梁专题/B00_内积正交与投影/README.md) 提供；
- 一般微分形式、流形拓扑、同调和 PDE 不进入数学一主干；
- 题目触发信号、第一动作、检查点和退出条件只在高等数学 Rules 中维护。

## Owns / Uses

- **Owns**：四类积分的微元分类、定向协议、保守场资格、三大定理选择和奇点补偿。
- **Uses**：Topic06 的几何表示、Topic07 的梯度/散度/旋度语言、Topic08 的投影积分。
- **被调用**：物理量、边界环流/通量、曲线曲面定向与定理转换。

## Read Next

1. [Topic08｜高维累积](../08_高维累积_区域坐标与Jacobian/README.md)
2. [Topic07｜多元局部模型](../07_多元局部模型_可微梯度隐函数与极值/README.md)
3. [B00｜内积、正交与投影](../../50_桥梁专题/B00_内积正交与投影/README.md)

## Manual

- Canonical Source：[定向积分与向量场.tex](定向积分与向量场.tex)
- Published View：[定向积分与向量场.pdf](../../../90_publish/定向积分与向量场.pdf)

## Status

归档笔记 II-05、II-06、II-07、II-08、II-08.1 已完成第一轮 Source Diff / Owner Diff；Topic06–08、B00 的边界已明确。正文和候选 Rules 尚需使用者审阅与陌生题验证，当前不标记为“已采用”。
