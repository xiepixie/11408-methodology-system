# 局部到整体：中值定理与函数形状

> 状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## Hook

中值定理不是四条孤立定理，而是一条“边界约束 → 内部见证”的运输链。辅助函数负责把题目目标翻译成可用的导数结构，导数符号再把局部信息恢复成整个区间的形状。

## Mother Question

已知端点、零点或局部导数信息，怎样严格地产生区间内部的见证点，并把它回译成单调、极值、凹凸和零点结论？

主线：

$$
\boxed{
\text{Target}
\to\text{Auxiliary Function}
\to\text{Qualification}
\to\text{Boundary/Zero Design}
\to\text{Witness}
\to\text{Translate Back}}
$$

## Scope / Stop Boundary

本册负责介值/零点、Rolle、Lagrange、Cauchy、高阶 Rolle、辅助函数构造、零点重数、单调性、极值、凹凸、拐点与区间形状。

本册停在中值定理和区间形状机制：

- 多中值点插点、插值余项、中值点参数和导数估计交给 [H-B02](../50_桥梁专题/H-B02_局部模型与区间定理_中值点余项与误差控制/README.md)；
- 导数、微分与有限 Taylor 本体交给 [Topic03](../03_一元局部模型_导数微分与Taylor/README.md)；
- 变上限积分与积分正则性接口交给 Topic05/H-B03；一阶 ODE 解族交给 Topic12；
- 题目识别、辅助函数选择和退出条件只在高等数学 Rules 中维护。

## Owns / Uses

- **Owns**：区间定理的资格链、内部见证、辅助函数反推、导数符号到整体形状的回译。
- **Uses**：Topic01 的函数对象/定义域、Topic02 的连续性、Topic03 的局部导数与有限模型。
- **被调用**：H-B02 的区间余项接口、Topic05 的积分接口、Topic12 的微分方程接口。

## Read Next

1. [Topic02｜极限与连续](../02_极限与连续_邻域尺度与存在性/README.md)
2. [Topic03｜一元局部模型](../03_一元局部模型_导数微分与Taylor/README.md)
3. [H-B02｜局部模型与区间定理](../50_桥梁专题/H-B02_局部模型与区间定理_中值点余项与误差控制/README.md)

## Manual

- Canonical Source：[局部到整体_中值定理与函数形状.tex](局部到整体_中值定理与函数形状.tex)
- Published View：[局部到整体_中值定理与函数形状.pdf](../../../90_publish/局部到整体_中值定理与函数形状.pdf)

## Status

I-07 与 I-06 函数形状片段已完成第一轮 Source Diff / Owner Diff；I-07.1/I-07.2 的主体已明确分流至 H-B02。正文和候选 Rules 尚需使用者审阅与陌生题验证，当前不标记为“已采用”。
