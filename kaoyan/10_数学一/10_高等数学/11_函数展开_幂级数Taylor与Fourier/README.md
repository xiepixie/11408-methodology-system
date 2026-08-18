# 函数展开：幂级数、Taylor 与 Fourier

> 状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## Hook

函数展开不是把公式写长，而是先确认表示的有效域：幂级数的半径与端点、Taylor 的余项资格、Fourier 的延拓与跳跃点恢复。

## Mother Question

复杂函数如何被基函数坐标化；这种表示在哪些点恢复原函数，逐项运算何时仍然合法？

主线：

$$
\boxed{\text{基函数/系数}\to\text{半径或区间}\to\text{端点/跳跃审计}\to\text{逐项运算}\to\text{恢复}}
$$

## Scope / Stop Boundary

本册负责幂级数半径与端点、基本母函数、代换与逐项微积分、Taylor 从有限局部模型到无限表示的资格、Fourier 的正交系数、奇偶延拓、正弦/余弦级数和 Dirichlet 恢复。

- Topic10 提供数项级数判别与尾项控制；
- Topic03 Own 有限阶 Taylor 多项式与局部误差；
- B08 Own 正交投影的线代解释；
- Topic12 Own 级数递推与常微分方程解；
- 复分析、Hilbert 空间完备性和 PDE 谱理论不进入数学一主干。

## Owns / Uses

- **Owns**：幂级数收敛域与逐项运算，Taylor 无限化资格，Fourier 延拓/正交/恢复。
- **Uses**：Topic10 的数项级数、Topic03 的局部 Taylor、B08 的内积正交。

## 训练导航

- [幂级数求和与端点审计](幂级数求和与端点审计.md) —— 母级数识别、代换与逐项微积分、奇偶项筛选、积分常数恢复、特殊点补回、左右端点独立判敛，以及函数项交换/生成函数的扩展边界；
- [Fourier 展开与收敛点](Fourier展开与收敛点.md) —— 周期与延拓、对称/正交系数、连续点/跳跃点/周期端点的级数和判定。

## Read Next

1. [Topic10｜数项级数](../10_数项级数_尾部与敛散/README.md)
2. [B08｜Fourier 与正交投影](../../50_桥梁专题/B08_Fourier与正交基_函数表示与正交投影/README.md)
3. [Topic12｜常微分方程](../12_常微分方程_局部规律与整体轨迹/README.md)

## Manual

- Canonical Source：[函数展开_幂级数Taylor与Fourier.tex](函数展开_幂级数Taylor与Fourier.tex)
- Published View：[函数展开_幂级数Taylor与Fourier.pdf](../../../90_publish/math1/函数展开_幂级数Taylor与Fourier.pdf)

## Status

归档笔记 II-09（幂级数部分）、II-10（级数扩展）与 II-11（Fourier 级数）已完成逐文件 Owner/Source Diff。II-10 中积分型级数的交换资格、生成函数的形式/分析双视角、递推编码与单位根筛选已作为 Extension 明确保留，不扩张数学一默认工具箱；正文、Rules 与陌生题验证仍需人工审阅，当前不标记为“已采用”。
