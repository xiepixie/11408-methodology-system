# 高维累积：区域、坐标与 Jacobian

> 状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## Hook

重积分不是把一元积分机械加层，而是为同一个几何域选择可扫描、可换元、可验算的编码；每次表示变化都必须同步搬运边界、被积函数与面积/体积微元。

## Mother Question

局部贡献分布在平面或空间区域上时，怎样从真实边界出发选择扫描方向或坐标网格，使积分限、测度因子和最终不变量同时闭合？

主线：

$$
\boxed{
\text{Quantity / Region}
\to\text{Geometric Encoding}
\to\text{Scan / Coordinate Choice}
\to\text{Bounds / Measure}
\to\text{Accumulate}
\to\text{Dimension Reduction}
\to\text{Invariant Check}}
$$

## Scope / Stop Boundary

本册负责二重/三重积分对象与资格、区域扫描与分区、换序、对称性、极/柱/球坐标、一般变量变换、投影/切片、面积体积质量质心与矩，以及收缩区域、整体积分常数和混合偏导综合题。

本册停在高维累积的高数计算机制：

- 空间对象和曲面方程由 [Topic06](../06_空间对象与方向表示/README.md) 提供；
- 多元可微与 Jacobian matrix 的局部线性化由 [Topic07](../07_多元局部模型_可微梯度隐函数与极值/README.md) 提供；
- Jacobian matrix 到 determinant 的局部面积/体积缩放由 [B02](../../50_桥梁专题/B02_Jacobian与行列式_坐标变换与局部体积缩放/README.md) 唯一拥有；
- 概率质量守恒与随机变量变换由 [B07](../../50_桥梁专题/B07_随机变量变换与Jacobian_概率质量守恒/README.md) 拥有；
- 曲线/曲面积分、定向与 Green/Gauss/Stokes 由 Topic09 接收；
- 单一高维累积问题族的题目触发信号、第一动作、检查点和退出条件由同目录训练 Markdown 维护；跨多个训练专题稳定复用并经证据验证的控制才晋升高等数学学科做题规则。

## Owns / Uses

- **Owns**：区域编码、扫描/换序、坐标选择、积分限、微元搬运、三维降维和高维累积的结果审计。
- **Uses**：Topic02 的积分合法性、Topic06 的几何表示、Topic07 的可微/Jacobian matrix。
- **被调用**：物理量建模、Topic09 的无向面积/体积积分接口，以及 B02/B07 的桥梁接口。

## 训练导航

- [二重积分区域、坐标与换序](二重积分区域、坐标与换序.md) —— 从真实区域出发选择扫描方向、对称、平移、极坐标与换序；保留旧笔记中高价值的“先画域再选表示”经验，并补齐 Jacobian、覆盖与退出检查；
- [三重积分与特殊结构](三重积分与特殊结构.md) —— 投影/切片分流、柱球坐标、收缩区域、未知整体积分、混合偏导边界降阶与独立复核。

## Read Next

1. [Topic09｜定向积分与向量场](../09_定向积分与向量场/README.md)
2. [Topic07｜多元局部模型](../07_多元局部模型_可微梯度隐函数与极值/README.md)
3. [B02｜Jacobian 与行列式](../../50_桥梁专题/B02_Jacobian与行列式_坐标变换与局部体积缩放/README.md)
4. [B07｜随机变量变换与 Jacobian](../../50_桥梁专题/B07_随机变量变换与Jacobian_概率质量守恒/README.md)

## Manual

- Canonical Source：[高维累积_区域坐标与Jacobian.tex](高维累积_区域坐标与Jacobian.tex)
- Published View：[高维累积_区域坐标与Jacobian.pdf](../../../90_publish/math1/高维累积_区域坐标与Jacobian.pdf)

## Status

归档笔记 II-04、II-04.1 及《高数下册进阶》专题 2 已完成当前轮 Source Diff / Owner Diff；补充内容已进入“边界族诱导坐标—参数边界/分段密度—双重 Riemann 和—乘积域积分不等式”的 Canonical 与训练链，任意平面轴旋转体的微元建模分流到 H-I01。Topic06、Topic07、B02、B07、Topic09 的边界保持不变。正文与同目录训练文档仍需使用者审阅和陌生题验证，当前不标记为“已采用”。
