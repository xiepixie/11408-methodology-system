# 一元累积：原函数、定积分与反常积分

> 状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## Hook

积分不是“求原函数再代上下限”的同义词，而是一套把局部贡献变成整体总量的构造：先确认对象和合法区间，再切分、变换与有限累加；若出现奇点或无穷端点，还要把无限对象还原为逐段截断极限。

## Mother Question

把无穷多个局部贡献累加成一个可解释的整体时，怎样同时控制对象、区间、有限计算、端点极限与独立验证？

主线：

$$
\boxed{
\text{Local Contribution}
\to\text{Domain / Regularity}
\to\text{Partition / Transform}
\to\text{Finite Accumulation}
\to\text{Boundary / Limit}
\to\text{Verification}}
$$

## Scope / Stop Boundary

本册负责原函数族与反导方法、定积分性质和结构计算、积分比较与估值、微元建模，以及反常积分的定义、拆分、计算与判敛。

本册停在一元累积本体：

- 原函数、Riemann 可积、变上限积分可导性的精细正则性接口交给 [H-B03](../50_桥梁专题/H-B03_微分与累积_基本定理及正则性边界/README.md)；
- 反常积分与数项级数的连续/离散尾部翻译交给 [H-B04](../50_桥梁专题/H-B04_连续无限累积与离散无限累积/README.md)；
- 有限 Taylor 归 Topic03，无限 Taylor 表示归 Topic11/[H-B05](../50_桥梁专题/H-B05_有限Taylor模型与无限Taylor表示/README.md)；
- 多重积分、曲线曲面积分与完整微分方程解法不在本册展开；
- 题目识别、预处理顺序和退出条件只在高等数学 Rules 中维护。

## Owns / Uses

- **Owns**：一元累积对象、有限区间结构、微元翻译、奇点拆分、截断极限与判敛机制。
- **Uses**：Topic01 的定义域，Topic02 的极限/等价，Topic03 的导数/Taylor，Topic04 的区间形状。
- **被调用**：H-B03 的微分—累积接口、H-B04 的连续—离散无限累积接口，以及后续多元积分专题。

## Read Next

1. [Topic03｜一元局部模型](../03_一元局部模型_导数微分与Taylor/README.md)
2. [Topic04｜局部到整体](../04_局部到整体_中值定理与函数形状/README.md)
3. [H-B03｜微分与累积](../50_桥梁专题/H-B03_微分与累积_基本定理及正则性边界/README.md)
4. [H-B04｜连续与离散无限累积](../50_桥梁专题/H-B04_连续无限累积与离散无限累积/README.md)

## Manual

- Canonical Source：[一元累积_原函数定积分与反常积分.tex](一元累积_原函数定积分与反常积分.tex)
- Published View：[一元累积_原函数定积分与反常积分.pdf](../../../90_publish/math1/一元累积_原函数定积分与反常积分.pdf)

## Status

I-08、I-08.1、I-09、I-10、I-10.1、I-11 与 I-12 已完成第一轮 Source Diff / Owner Diff；H-B03/H-B04 的主体边界已明确。正文和候选 Rules 尚需使用者审阅与陌生题验证，当前不标记为“已采用”。
