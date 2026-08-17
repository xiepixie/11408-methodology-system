# I02｜二维随机变量线性变换

状态：目录已建立，正文未建。

## Position

用于验收 B02 + B06 + B07 的概率变换 Integration。

## Canonical Problem

例如：

$$
U=X+Y,\qquad V=X-Y.
$$

目标不是记变换公式，而是完整处理：原 support、变换、逆变换、Jacobian、新 support、联合密度与后续边缘化。

## Module Recognition

- B02：Jacobian 与行列式；
- B06：概率的积分语言；
- B07：概率质量守恒；
- 概率联合分布 Topic。

## Composition Skeleton

$$
\text{Original Joint Model}
\to
\text{Choose New Coordinates}
\to
\text{Invert Map}
\to
\text{Transform Support}
\to
\text{Jacobian Correction}
\to
\text{New Joint Density}
\to
\text{Marginalize / Verify}
$$

## Verification

至少使用：总概率为 1、support 边界、对称性或逆变换回代中的一个独立检查。

## Boundary

本 Integration 不重新解释 Jacobian、联合密度或边缘化定义。

## 待重构

待 B02/B06/B07 正文成熟后，以一到两个代表问题完成 Composition 验收。
