# 空间对象与方向表示

> 状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## Hook

空间解析几何不是“线、面、距离、夹角公式表”，而是一条表示管线：先识别对象，再选择生成式或约束式表示，找出方向/法向/位移这些几何载体，最后把中文关系翻译成向量约束。

## Mother Question

空间中的点、方向、直线、平面、曲线和曲面，怎样转换成适合代数计算与后续微积分处理的表示？

主线：

$$
\boxed{
\text{Object}
\to\text{Representation}
\to\text{Carrier}
\to\text{Constraint}
\to\text{Measure / Construct}
\to\text{Calculus Handoff}}
$$

## Scope / Stop Boundary

本册负责点/向量、直线/平面、曲线/曲面的表示；方向、法向与位移载体；平行、垂直、相交、共面、角度、距离和构造；标准曲面的对称—截面—轴向变化重建；截面、投影、旋转和后续微积分接口。

本册停在空间对象语言：

- 内积、正交与投影的跨学科统一解释交给 [B00](../../50_桥梁专题/B00_内积正交与投影/README.md)；
- 梯度、可微、隐函数与切平面本体交给 Topic07/[B01](../../50_桥梁专题/B01_局部线性化_微分与线性映射/README.md)；
- 区域坐标与 Jacobian 交给 Topic08；曲线/曲面积分与定向交给 Topic09；
- 题目识别、表示选择、检查点和退出条件只在高等数学 Rules 中维护。

## Owns / Uses

- **Owns**：空间对象、生成/约束表示、方向/法向载体、空间关系翻译、角度距离生成法、标准曲面重建。
- **Uses**：基本向量代数、方程组与 Topic01–05 的函数/积分语言。
- **被调用**：Topic07 的梯度与切平面、Topic08 的区域投影、Topic09 的参数曲线曲面与定向。

## Read Next

1. [Topic07｜多元局部模型](../07_多元局部模型_可微梯度隐函数与极值/README.md)
2. [Topic08｜高维累积](../08_高维累积_区域坐标与Jacobian/README.md)
3. [Topic09｜定向积分](../09_定向积分与向量场/README.md)
4. [B00｜内积、正交与投影](../../50_桥梁专题/B00_内积正交与投影/README.md)

## Manual

- Canonical Source：[空间对象与方向表示.tex](空间对象与方向表示.tex)
- Published View：[空间对象与方向表示.pdf](../../../90_publish/math1/空间对象与方向表示.pdf)

## Status

归档笔记 II-00 已完成第一轮 Source Diff / Owner Diff；B00、B01、Topic07–09 的边界已明确。正文和候选 Rules 尚需使用者审阅与陌生题验证，当前不标记为“已采用”。
