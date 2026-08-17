# 高数 Topic03《一元局部模型》Source Diff

日期：2026-08-11  
场景：import  
结论：**Canonical Update + Candidate Rules + Boundary Routing**

## 输入与当前 Owner

- 主 Source：归档笔记 `I-06_一元微分：定义、计算、判定与几何应用.md`（1349 行）。
- 补充 Source：`I-02_函数极限理论与计算方法.md` 中导数定义型极限、有限 Taylor 主部和 $|x|^p\sin(1/x)$ 正则性阶梯。
- Canonical Owner：`10_数学一/10_高等数学/03_一元局部模型_导数微分与Taylor/一元局部模型_导数微分与Taylor.tex`。
- Control Owner：`10_数学一/90_学科做题规则/高等数学.md`。

## Observable Facts

1. I-06 同时包含点导数、求导法则、高阶导数、函数形状、曲率、导数公式表和原函数反查表，跨越多个当前 Owner。
2. 旧稿反复区分 $f'(a)$ 与 $\lim_{x\to a}f'(x)$，并提供对称导数、绝对值、振荡函数等高价值反例。
3. 旧稿的高阶导数部分同时混用了有限 Taylor 系数、无限幂级数逐项操作、微分方程递推和题型选择，必须拆开 Knowledge 与 Control。
4. Topic03 原目录只有短 README，没有 Canonical `.tex`，无法承担深度机制 Owner。

## Source / Owner 路由

| Source 内容 | 最终去向 | 判定 |
|---|---|---|
| 点导数、左右导数、微分与可导层级 | Topic03 | Canonical Update |
| 固定基点差商与对称导数反例 | Topic03 + H-R13 | 机制 + Candidate Rule |
| 分段点连续/左右差商 | Topic03 + H-R14 | 机制 + Candidate Rule |
| 点导数与导函数极限 | Topic03；中值定理桥只 Use Topic04/H-B02 | Owner Boundary |
| 和、积、商、链式法则 | Topic03 | Canonical Update |
| 反函数、隐式、参数求导 | Topic03 的局部计算机制 + H-R17 | 条件式 Own；存在性边界保留 |
| 变上限积分求导 | Topic05/H-B03 | 不复制 |
| 有限 Taylor、Peano 余项、最低非零项 | Topic03 + H-R19 | Canonical Update + Candidate Rule |
| Lagrange/Cauchy/插值余项 | H-B02 | Bridge Source |
| Taylor series、逐项微积分、收敛域 | Topic11/H-B05 | 不复制；Anti-Bridge |
| 高阶导数点值/通式、Leibniz、恒等式递推 | Topic03 + H-R18 | Canonical Update + Candidate Rule |
| ODE 解族与整体轨迹 | Topic12 | 只保留局部递推 Use |
| 单调、极值、凹凸、拐点、Rolle 数轴法 | Topic04 | 后续 Source Pack |
| 切线、法线、一元曲率 | Topic03 | Canonical Update |
| 原函数反查表 | Topic05 | 不复制 |
| 完整导数公式表 | Topic03 Appendix Coverage | 压缩为锚点，不作正文主结构 |

## 提炼出的母模型

$$
\boxed{
\text{Anchor}
\to\text{Increment}
\to\text{Normalize}
\to\text{Coefficient}
\to\text{Residual}
\to\text{Order Upgrade}}
$$

事实层含义：

- 导数是固定基点后，对一阶输入尺度归一得到的稳定系数；
- 微分是对应的线性主部；
- 有限 Taylor 是逐阶减去已知主部后继续提取稳定系数；
- 余项记录压缩丢失的信息，决定局部替代是否足以支持当前运算；
- 相消不是“结果为零”，而是当前精度已经用尽，必须升阶。

贯穿母例选择 $\sqrt{1+h}$：先由有理化重建一阶系数，再用关系 $f^2=1+h$ 匹配二、三阶系数，最后回代验证余项。边界母例使用 $|x|$、$(x-a)^k|x-a|$ 与 $|x|^p\sin(1/x)$。

## Candidate Rules

新增 H-R13--H-R19：

- 固定基点识别导数定义；
- 分段点先过连续门；
- 点导数与邻域导数极限分层；
- 长乘积先清点零因子与零点阶数；
- 反函数/隐式/参数求导先过资格门；
- 高阶导数先分点值与通式；
- Taylor 按相消后的第一幸存阶停止。

这些动作仅来自静态 Source Diff 和模型攻击，尚无使用者陌生题证据，因此全部保持“待验证”，不晋升为“已采用”。

## 拒绝进入稳定主干的说法

- “对称导数存在即可导”被 $|x|$ 否定。
- “可导即可推出导函数极限存在”被 $x^2\sin(1/x)$ 否定。
- “有任意阶导数就等于 Taylor series”被平坦函数 $e^{-1/x^2}$ 否定。
- “$f'(a)=0$ 就是极值、$f''(a)=0$ 就是拐点”只产生候选点，完整判定归 Topic04。
- “隐式求导公式自动证明局部分支存在”越过了存在性资格。

## 状态与下一次检验

- 本次是 **Canonical Update + Candidate Rules**，不是已采用结论。
- 下一次最小检验：用一组陌生题分别攻击固定基点、分段点、点/邻域导数、高阶点值与 Taylor 停止阶；记录规则是否减少误判与冗余计算。
- 后续 Topic04 导入时，接收 I-06 的函数形状段落，并复核 Topic03→Topic04 的“局部候选 → 区间符号/中值定理”交接。
