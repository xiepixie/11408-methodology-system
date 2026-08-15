# 高数 Topic05《一元累积》Source Diff

日期：2026-08-11  
场景：import  
结论：**Canonical Update + Candidate Rules + Bridge Routing**

## 输入与当前 Owner

- 主 Source：`I-08_不定积分.md`、`I-09_积分计算.md`、`I-11_反常积分计算.md`、`I-12_反常积分判敛.md`。
- 机制补充：`I-08.1_原函数黎曼积分与变上限积分.md`、`I-10_微积分应用.md`、`I-10.1_定积分比大小：完整方法论总结.md`。
- Canonical Owner：`10_数学一/10_高等数学/05_一元累积_原函数定积分与反常积分/一元累积_原函数定积分与反常积分.tex`。
- Control Owner：`10_数学一/90_学科做题规则/高等数学.md`。
- Bridge Owners：H-B03（微分—累积正则性）与 H-B04（连续—离散无限累积）。

## Observable Facts

1. I-08 与 I-09 共同显示：原函数是反向变化率工具，定积分是区间累积；定积分计算的第一动作通常是区间/对称/分段审查，不是求原函数。
2. I-08.1 明确区分“存在原函数、Riemann 可积、变上限积分可导”三种资格；其精细反例与正则性分类具有独立接口，应由 H-B03 拥有。
3. I-10 的积分应用共享同一微元机制：先确定切片和局部贡献，再累加；单位检查是独立于代数计算的验证通道。
4. I-10.1 的定积分比较可压缩为“统一区间—比较完整密度—保序/放缩—主部相消则升阶”，无需复制长题型表。
5. I-11 与 I-12 的共同核心是“奇点清单—单点拆分—有限截断—局部判敛/计算—逐段极限—一票否决”。
6. 反常积分与级数共享尾部稳定思想，但连续/离散判别的翻译是独立 Bridge，不应由 Topic05 重复拥有。

## Source / Owner 路由

| Source 内容 | 最终去向 | 判定 |
|---|---|---|
| 原函数族、积分常数与区间分支 | Topic05 + H-R28/H-R36 | Canonical Update + Candidate Rules |
| 凑微分、换元、分部、部分分式与递推 | Topic05 + H-R30/H-R36 | 机制压缩，不复制公式库 |
| Riemann 累积、定积分性质与区间结构 | Topic05 + H-R29 | Canonical Update + Candidate Rule |
| 原函数/Riemann/变上限正则性反例 | H-B03 | Bridge Routing |
| 定积分比较、保序与局部放缩 | Topic05 + H-R31 | Canonical Update + Candidate Rule |
| 面积、弧长、旋转体、功、压力与形心 | Topic05 + H-R32 | 微元统一机制 |
| 奇点定义、拆分与截断计算 | Topic05 + H-R33/H-R35 | Canonical Update + Candidate Rules |
| 幂/幂对数、比较、Dirichlet/Abel 判敛 | Topic05 + H-R34 | Canonical Update + Candidate Rule |
| 反常积分—数项级数尾部翻译 | H-B04 | Bridge Routing |
| 多重积分、曲线曲面积分 | 后续多元积分 Topic | 不复制 |
| Taylor 级数与无限表示 | Topic11/H-B05 | 不复制 |

## 提炼出的母模型

$$
\boxed{
\text{Local Contribution}
\to\text{Domain / Regularity}
\to\text{Partition / Transform}
\to\text{Finite Accumulation}
\to\text{Boundary / Limit}
\to\text{Verification}}
$$

事实层含义：

- 被积函数与微分因子共同构成局部贡献，换元必须搬运完整密度；
- 定义域、可积性与奇点决定“能不能积”，先于“怎么算”；
- 对称、分段、保序和换元都在有限累积层降低结构复杂度；
- 反常积分必须先截断为正常积分，再逐个端点取极限；
- 结果必须接受反向求导、符号、单位、数量级或数值近似的独立验证。

## Candidate Rules

新增 H-R28--H-R36：

- 积分对象先分层；
- 定积分先扫描区间和结构；
- 换元搬运完整密度、上下限与分支；
- 积分比较先统一区间和平均高度；
- 微元应用先写局部贡献与单位；
- 反常积分逐奇点拆分；
- 判敛先分最终保号与持续振荡；
- 反常换元/分部只在截断区间执行；
- 不定积分只走复杂度下降路径并反向求导。

这些动作来自 Source Diff 和机制重建，尚无使用者陌生题证据，全部保持“待验证”。

## 拒绝进入稳定主干的说法

- “积分与求导可以无条件抵消”被对象/正则性边界阻断。
- “定积分都应先求原函数”被区间结构和保序机制阻断。
- “换元只替换函数本体”被完整密度与 Jacobian 阻断。
- “内部奇点两侧可以抵消”被普通收敛/主值边界阻断。
- “被积函数趋零就收敛”被幂模型和振荡反例阻断。
- “绝对收敛失败就必发散”被 Dirichlet/Abel 抵消机制阻断。
- “不能写成初等函数就没有原函数”被对象/表达性边界阻断。

## 状态与下一次检验

- 本次是 **Canonical Update + Candidate Rules + Bridge Routing**，不是已采用结论。
- 下一次最小检验：用陌生定积分攻击区间翻转、分段和换元密度；用应用题攻击微元与单位；用多奇点/振荡反常积分攻击逐点拆分、主值边界和 Dirichlet 条件。
- 后续建设 H-B03 时复核“导数—原函数—变上限函数”的资格矩阵；建设 H-B04 时复核“连续尾部—离散尾部”的 Cauchy 接口。
