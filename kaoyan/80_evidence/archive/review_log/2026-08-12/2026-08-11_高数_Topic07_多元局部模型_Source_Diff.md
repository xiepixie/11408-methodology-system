# 高数 Topic07《多元局部模型：可微、梯度、隐函数与极值》Source Diff

日期：2026-08-11  
场景：import  
结论：**Canonical Update + Candidate Rules + Bridge Routing**

## 输入与当前 Owner

- 主 Source：归档笔记 `II-01_多元微分概念.md`、`II-02_多元微分应用.md`、`II-02.1_隐函数微分与隐式曲面极值.md`、`II-03_多元极值.md`、`II-03.1_二次型条件极值与广义特征值.md`。
- Canonical Owner：`10_数学一/10_高等数学/07_多元局部模型_可微梯度隐函数与极值/多元局部模型_可微梯度隐函数与极值.tex`。
- Control Owner：`10_数学一/90_学科做题规则/高等数学.md`。
- Bridge Owners：B01（局部线性化）、B02（Jacobian 与局部体积）、B03（Hessian 与二次型）、B04（梯度正交与约束几何）。

## Observable Facts

1. 多元极限要求对允许集合中的所有趋近方式统一；路径法可以用来否定，但有限条路径不能证明存在。
2. 偏导和方向导数是局部探针；可微要求同一个线性映射解释全部小位移，且余项相对位移范数一致趋零。
3. 梯度是标量函数一阶线性模型的坐标表示；Jacobian matrix 是向量值映射的导数表示，determinant 只在方阵时定义。
4. 隐函数求导的真正资格是局部可解：被求解变量块的 Jacobian 可逆；导数公式只是该资格的后果。
5. 正则等值面的梯度是法向；切线、切平面与交线切向必须先过“点属于对象 + 梯度非零/独立”的资格门。
6. 一阶项在驻点消失后，Hessian 给二阶局部形状；退化只表示二阶信息不足。
7. Lagrange 条件由“允许切向上的一阶变化为零”产生，只生成正则候选；闭区域全局最值还需逐层覆盖边界与低维交界。

## Source / Owner 路由

| Source 内容 | 最终去向 | 判定 |
|---|---|---|
| II-01 联合极限与连续 | Topic07 + H-R45 | Canonical Update + Candidate Rule |
| II-01 偏导、方向导数、可微 | Topic07 + H-R46/H-R47 | 资格层级与操作协议 |
| II-01 梯度、Jacobian matrix、链式法则 | Topic07 + H-R48 | Canonical Update + Candidate Rule |
| II-01 逆/隐函数与分块求导 | Topic07 + H-R49 | 局部可解资格 |
| II-01 Hessian 与 Taylor | Topic07 + H-R51；跨域解释归 B03 | 机制 + Boundary |
| II-02 几何应用 | Topic07 + H-R50；空间对象表示调用 Topic06 | Canonical Update + Interface |
| II-02.1 隐式曲面与约束极值 | Topic07 + H-R49/H-R50/H-R52 | Canonical Update + Candidate Rules |
| II-03 无约束/约束/闭区域极值 | Topic07 + H-R51--H-R53 | 候选完备性协议 |
| II-03.1 二次型条件极值、Rayleigh 商、广义特征值 | Topic07 只保留接口；主体归 B03/线性代数 | 不复制 |
| Jacobian determinant 与积分换元 | B02/Topic08 | 不复制 |
| KKT 与一般非线性规划 | Extension | 不进入当前高数主干 |

## 提炼出的母模型

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

事实层含义：

- 基点与允许域决定“从哪里、沿哪些路径”观察；
- 单方向探针只能产生必要信息，不能替代统一局部模型；
- 可微把所有方向压缩成一个线性映射，梯度/Jacobian 是其坐标读法；
- 一阶模型产生切向、法向、链式与隐函数接口；
- 一阶消失后升级到二阶模型，退化时继续寻找首个有效阶；
- 约束削减允许方向，闭区域再要求候选集合覆盖所有维度层级。

## Candidate Rules

新增 H-R45--H-R53：

- 路径法只负责否定多元极限；
- 偏导/方向导数不能越级替代可微；
- 方向导数先统一单位方向约定；
- Jacobian 先做维度审计；
- 隐函数求导先过局部可解资格门；
- 切线切平面先验点与正则性；
- Hessian 退化只意味着二阶判别失效；
- Lagrange 只生成正则候选；
- 闭区域最值逐层补齐候选。

这些动作来自 Source Diff 与机制重建，尚无使用者陌生题证据，全部保持“待验证”。

## 拒绝进入稳定主干的说法

- “几条路径同值就证明联合极限存在”被统一控制要求阻断。
- “偏导存在/所有方向导数存在就可微”被统一线性余项资格阻断。
- “Jacobian 就是行列式”被导数矩阵与 determinant 的对象边界阻断。
- “隐函数求导只是代公式”被局部可解与可逆块资格门阻断。
- “梯度为零仍可直接写等值面法向”被正则点条件阻断。
- “Hessian 判别式为零说明没有极值”被二阶信息不足边界阻断。
- “解出 Lagrange 方程就是全局极值”被候选生成/边界完备性区分阻断。
- II-03.1 的广义特征值主体不复制进 Topic07，避免与 B03/线性代数形成第二 Owner。

## 状态与下一次检验

- 本次是 **Canonical Update + Candidate Rules + Bridge Routing**，不是已采用结论。
- 下一次最小检验：用陌生的分段多元函数攻击“方向导数存在但不可微”；用退化驻点题攻击 Hessian 退出条件；用非正则约束和分段边界题攻击 Lagrange 与候选全集。
- 建设 Topic08 时复核 Jacobian matrix/determinant、隐函数坐标与积分换元接口；建设 Topic09 时复核梯度、切向与定向对象接口。
