# 数学一 Core Bridge Atlas

> 类型：Atlas
> 状态：已采用；README 是 Canonical Bridge Atlas，下游 Bridge 仍按规划逐册建设。

## 1. 定位

本目录只拥有 **跨 Subject 的稳定接口**。高数、线代、概率各自的 Topic 继续拥有本体机制；这里解释它们为什么能接、怎样翻译、保持什么不变量。

判别标准：删掉具体题目后，若仍存在可复用的 A ↔ B 共享结构，才建立 Bridge；否则进入 Integration、Extension、Anti-Bridge 或不建稳定资产。

## 2. Bridge 地图

| ID | Bridge | 主要 Owner 接口 | 依赖 |
|---|---|---|---|
| B00 | [内积、正交与投影](B00_内积正交与投影/README.md) | 高数空间几何 ↔ 线代向量空间 | 基础 |
| B01 | [局部线性化](B01_局部线性化_微分与线性映射/README.md) | 高数微分 ↔ 线代线性映射 | 基础 |
| B02 | [Jacobian 与行列式](B02_Jacobian与行列式_坐标变换与局部体积缩放/README.md) | 多元微分/积分 ↔ 线代行列式 | B01 |
| B03 | [Hessian 与二次型](B03_Hessian与二次型_二阶局部形状与正定性/README.md) | 多元二阶模型 ↔ 线代二次型 | B01 |
| B04 | [梯度、正交与 Lagrange](B04_梯度正交与Lagrange_约束极值与子空间几何/README.md) | 多元约束极值 ↔ 正交/子空间几何 | B00 + B01 |
| B05 | [线性方程与线性微分方程](B05_线性方程与线性微分方程_一点加Kernel/README.md) | 线代方程 ↔ 高数线性 ODE | 相对独立 |
| B06A | [PDF 与 CDF](B06A_PDF与CDF_局部概率密度与累积/README.md) | 高数 FTC ↔ 概率分布 | 基础 |
| B06B | [期望、联合概率与边缘化](B06B_期望联合概率与边缘化_概率的积分语言/README.md) | 高数积分 ↔ 概率质量汇总 | B06A |
| B07 | [随机变量变换与 Jacobian](B07_随机变量变换与Jacobian_概率质量守恒/README.md) | B02 ↔ 概率变量变换 | B02 + B06 |
| B08 | [Fourier 与正交基](B08_Fourier与正交基_函数表示与正交投影/README.md) | 高数函数展开 ↔ 线代正交坐标 | B00 |

## 3. Dependency Graph

$$
B00\rightarrow\{B04,B08\}
$$

$$
B01\rightarrow\{B02,B03,B04\}
$$

$$
B06A\rightarrow B06B
$$

$$
B02+B06\rightarrow B07
$$

B05 相对独立。

## 4. Anti-Bridge Registry

当前优先阻断：

- 概率独立 ≠ 线性无关；
- 方差 ≠ 范数；
- 正交 ≠ 概率独立；
- “公式都含 determinant / quadratic form / integral”本身不能构成 Bridge。

Anti-Bridge 不单独建树。具体禁推条件写回最相关 Bridge 的 Boundary。

## 5. Extension Policy

真实但超纲的连接放入对应 Bridge 的 `Extension` 段，例如 Fourier ↔ Hilbert space、ODE ↔ matrix exponential。只有未来学习范围变化时，才重新评估是否升级为核心 Owner。
