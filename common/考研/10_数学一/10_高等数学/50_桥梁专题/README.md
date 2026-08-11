# 高等数学 Internal Bridge Atlas

> 类型：Atlas
> 状态：已采用；README 是 Canonical Internal Bridge Atlas，下游 Bridge 仍按规划逐册建设。

本目录只拥有 **高数内部 Topic↔Topic 的稳定接口**，使用 `H-Bxx` 编号。凡涉及线性代数或概率的共享机制，统一上移到数学一 `../50_桥梁专题/`，避免重复 Owner。

## 当前 Internal Bridge

| ID | Bridge | 接口 |
|---|---|---|
| H-B01 | [函数结构在运算中的传播](H-B01_函数结构在运算中的传播/README.md) | Topic01 ↔ 02/03/05/11 |
| H-B02 | [局部模型与区间定理](H-B02_局部模型与区间定理_中值点余项与误差控制/README.md) | Topic03 ↔ 04 |
| H-B03 | [微分与累积](H-B03_微分与累积_基本定理及正则性边界/README.md) | Topic03 ↔ 05 |
| H-B04 | [连续无限累积与离散无限累积](H-B04_连续无限累积与离散无限累积/README.md) | Topic05 ↔ 10 |
| H-B05 | [有限 Taylor 模型与无限 Taylor 表示](H-B05_有限Taylor模型与无限Taylor表示/README.md) | Topic03 ↔ 11 |

## 上移到数学一 Core Bridge 的接口

- Jacobian ↔ 行列式：数学一 B02；
- Hessian ↔ 二次型：数学一 B03；
- 梯度/正交/Lagrange：数学一 B04；
- 线性 ODE ↔ kernel：数学一 B05；
- Fourier ↔ 正交基：数学一 B08。

## Extension

离散递推 ↔ 生成函数 ↔ ODE/代数方程目前标记为 Extension，不建立 H-B06。
