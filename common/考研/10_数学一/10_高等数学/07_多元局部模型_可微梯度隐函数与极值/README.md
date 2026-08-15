# 多元局部模型：可微、梯度、隐函数与极值

> 状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## Hook

多元微分不是把一元公式添上下标，而是在许多可能的逼近方向中寻找一个对所有小位移都成立的统一线性模型；一阶模型失效后，再升级到 Hessian 描述的二阶形状。

## Mother Question

当输入可以沿无穷多条路径变化时，怎样从局部探针升级为统一模型，并把它用于几何读取、隐式求解和极值候选的完整审计？

主线：

$$
\boxed{
\text{Anchor / Domain}
\to\text{Joint Approach}
\to\text{Directional Probes}
\to\text{Uniform Linear Model}
\to\text{Geometry Readout}
\to\text{Quadratic Upgrade}
\to\text{Constraint / Boundary Audit}}
$$

## Scope / Stop Boundary

本册负责多元极限与连续、偏导和方向导数、可微与全微分、梯度与 Jacobian matrix、链式法则、隐函数资格与求导、切向/法向读取、Hessian 与多元 Taylor、无约束/等式约束极值及闭区域候选全集。

本册停在高数局部模型及其考试应用：

- “最佳局部线性映射”的跨学科解释交给 [B01](../../50_桥梁专题/B01_局部线性化_微分与线性映射/README.md)；
- Jacobian determinant 的体积缩放与换元机制交给 [B02](../../50_桥梁专题/B02_Jacobian与行列式_坐标变换与局部体积缩放/README.md) 和 Topic08；
- Hessian 的二次型、正定性、Rayleigh 商与广义特征值交给 [B03](../../50_桥梁专题/B03_Hessian与二次型_二阶局部形状与正定性/README.md)；
- 梯度正交、切/法空间与约束几何接口交给 [B04](../../50_桥梁专题/B04_梯度正交与Lagrange_约束极值与子空间几何/README.md)；
- 题目触发信号、第一动作、检查点和退出条件只在高等数学 Rules 中维护。

## Owns / Uses

- **Owns**：联合逼近、可微资格层级、一阶/二阶局部模型、隐函数局部可解、梯度几何、多元极值候选生成与边界完备性。
- **Uses**：Topic02 的极限语言、Topic03 的一元局部模型、Topic06 的空间对象与方向表示。
- **被调用**：Topic08 的局部坐标变换与积分微元、Topic09 的标量场/向量场局部变化，以及 B01--B04。

## Read Next

1. [Topic08｜高维累积](../08_高维累积_区域坐标与Jacobian/README.md)
2. [Topic09｜定向积分与向量场](../09_定向积分与向量场/README.md)
3. [B01｜局部线性化](../../50_桥梁专题/B01_局部线性化_微分与线性映射/README.md)
4. [B03｜Hessian 与二次型](../../50_桥梁专题/B03_Hessian与二次型_二阶局部形状与正定性/README.md)

## Manual

- Canonical Source：[多元局部模型_可微梯度隐函数与极值.tex](多元局部模型_可微梯度隐函数与极值.tex)
- Published View：[多元局部模型_可微梯度隐函数与极值.pdf](../../../90_publish/多元局部模型_可微梯度隐函数与极值.pdf)

## Status

归档笔记 II-01、II-02、II-02.1、II-03、II-03.1 已完成第一轮 Source Diff / Owner Diff；Topic06、Topic08、B01--B04 的边界已明确。正文和候选 Rules 尚需使用者审阅与陌生题验证，当前不标记为“已采用”。
