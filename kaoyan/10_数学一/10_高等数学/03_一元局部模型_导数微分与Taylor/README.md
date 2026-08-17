# 一元局部模型：导数、微分与 Taylor

> 状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## Hook

导数、微分和 Taylor 不是三套公式。它们都在做同一件事：固定基点，把函数增量按某个尺度归一，提取稳定系数，并记录被丢掉的余项。

## Mother Question

一点附近怎样把复杂函数压缩成可计算的线性或有限阶多项式，同时知道这个替代保留了多少信息？

主线：

$$
\boxed{
\text{Anchor}
\to\text{Increment}
\to\text{Normalize}
\to\text{Coefficient}
\to\text{Residual}
\to\text{Order Upgrade}}
$$

## Scope / Stop Boundary

本册负责点导数、左右导数、微分、局部求导法则、高阶导数、有限阶 Taylor 模型、切线/法线与曲率。

本册停在局部有限阶模型：

- 区间单调、极值、凹凸、零点和中值定理交给 [Topic04](../04_局部到整体_中值定理与函数形状/README.md)；
- 区间余项和误差估计交给 [H-B02](../50_桥梁专题/H-B02_局部模型与区间定理_中值点余项与误差控制/README.md)；
- 变上限积分与原函数接口交给 [Topic05](../05_一元累积_原函数定积分与反常积分/README.md) 和 [H-B03](../50_桥梁专题/H-B03_微分与累积_基本定理及正则性边界/README.md)；
- 无限 Taylor series 与函数恢复交给 [Topic11](../11_函数展开_幂级数Taylor与Fourier/README.md) 和 [H-B05](../50_桥梁专题/H-B05_有限Taylor模型与无限Taylor表示/README.md)。

## Owns / Uses

- **Owns**：一元局部系数提取、线性主部、有限阶多项式与余项、高阶局部正则性、局部几何。
- **Uses**：[Topic01](../01_函数对象_表示与结构/README.md) 的函数对象/表示边界与 [Topic02](../02_极限与连续_邻域尺度与存在性/README.md) 的极限、小 $o$ 语言。
- **被调用**：Topic04/05/11/12、H-B01～H-B05，以及数学一 B01 局部线性化 Bridge。

## Read Next

1. [Topic02｜极限与连续](../02_极限与连续_邻域尺度与存在性/README.md)
2. [Topic04｜局部到整体](../04_局部到整体_中值定理与函数形状/README.md)
3. [H-B05｜有限 Taylor 模型与无限 Taylor 表示](../50_桥梁专题/H-B05_有限Taylor模型与无限Taylor表示/README.md)

## Manual

- Canonical Source：[一元局部模型_导数微分与Taylor.tex](一元局部模型_导数微分与Taylor.tex)
- Published View：[一元局部模型_导数微分与Taylor.pdf](../../../90_publish/math1/一元局部模型_导数微分与Taylor.pdf)

## Status

I-06 与 I-02 中相关片段已完成第一轮 Source Diff / Owner Diff。正文和候选 Rules 尚需使用者审阅与陌生题验证；当前不标记为“已采用”。
