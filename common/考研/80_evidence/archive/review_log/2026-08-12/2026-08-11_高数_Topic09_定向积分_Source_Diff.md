# 高数 Topic09《定向积分与向量场》Source Diff

日期：2026-08-11
场景：import
结论：**Canonical Update + Candidate Rules + Bridge Routing**

## 输入与当前 Owner

- 主 Source：归档笔记 `II-05_第一型曲线曲面积分.md`、`II-06_第二型曲线积分.md`、`II-07_第二型曲面积分.md`、`II-08_曲线与曲面积分统一框架.md`、`II-08.1_格林斯托克斯与高斯公式.md`。
- Canonical Owner：`10_数学一/10_高等数学/09_定向积分与向量场/定向积分与向量场.tex`。
- Control Owner：`10_数学一/90_学科做题规则/高等数学.md`。
- Upstream Owners：Topic06（对象/参数/法向）、Topic07（梯度与局部场）、Topic08（无向区域积分）。

## Observable Facts

1. 四类积分由“标量/向量场 × 曲线/曲面载体”组成；第一型使用无向 $ds,dS$，第二型使用有向 $d\mathbf r,d\mathbf S$。
2. 参数化必须同步替换坐标、微元和方向；曲面投影公式必须区分上/下侧与外/内侧。
3. 第二型曲线的保守性需要旋度条件、定义域拓扑和单值势函数共同支撑；穿孔区域是零旋度非零环流的反例。
4. Green、Stokes、Gauss 具有同一母结构“内部微分量累积 = 边界积分”，但边界对象、方向协议和正则性条件不同。
5. 补线、补面、换面和挖洞不是技巧清单，而是处理边界不闭合、曲面复杂或内部奇点的对象变换。
6. 对称性在第二型积分中必须对完整有向微元判断，不能只看系数函数奇偶。

## Source / Owner 路由

| Source 内容 | 最终去向 | 判定 |
|---|---|---|
| II-05 第一型曲线/曲面 | Topic09 + H-R65/H-R66/H-R74 | Canonical Update + Candidate Rules |
| II-06 第二型曲线/路径无关 | Topic09 + H-R66/H-R69/H-R70/H-R71 | 机制 + 资格边界 |
| II-07 第二型曲面/投影/通量 | Topic09 + H-R67/H-R68/H-R72 | Canonical Update + Candidate Rules |
| II-08 四类统一框架 | Topic09 母模型与方法分流 | Canonical Owner |
| II-08.1 梯度/散度/旋度 | Topic09 局部场语言 | 一阶向量场接口 |
| II-08.1 保守场/穿孔反例 | Topic09 + H-R69 | 拓扑资格压缩 |
| II-08.1 Green | Topic09 + H-R70；计算目标调用 Topic08 | Canonical Update + Interface |
| II-08.1 Stokes | Topic09 + H-R71；曲面对象调用 Topic06 | Canonical Update + Interface |
| II-08.1 Gauss | Topic09 + H-R72；体积分调用 Topic08 | Canonical Update + Interface |
| 一般微分形式/流形/PDE 扩展 | Extension | 不进入数学一主干 |

## 提炼出的母模型

$$
\boxed{\text{Field Type / Geometric Carrier}\to\text{Orientation / Parametrization}\to\text{Microelement}\to\text{Direct or Boundary Theorem}\to\text{Domain / Singularity Audit}\to\text{Invariant Check}}
$$

事实层含义：

- 微元决定积分究竟测长度、面积、做功/环流还是通量；
- 定向是第二型积分和三大定理的符号协议；
- Green/Stokes/Gauss 只在各自边界和正则性资格下成立；
- 无旋、零散度是局部微分条件，不能绕过全局拓扑和奇点审计；
- 直接法、补线/补面、换面和挖洞都是围绕对象边界的重表达。

## Candidate Rules

新增 H-R65--H-R74：

- 先按场 × 载体分类微元；
- 参数化同步替换坐标、微元和方向；
- 投影公式先确认法向侧与投影平面；
- 对称性作用于完整有向 integrand；
- 保守场先过旋度—拓扑—势函数三门；
- Green 检查闭合、正向和孔洞方向；
- Stokes 配对边界方向与曲面法向；
- Gauss 只用于封闭外向曲面并处理内部奇点；
- 定理选择按边界对象分流；
- 结果用反向、量纲与简单场做不变量复核。

这些动作来自 Source Diff 与机制重建，尚无使用者陌生题证据，全部保持“待验证”。

## 拒绝进入稳定主干的说法

- “第一型和第二型只是记号不同”被微元与方向差异阻断。
- “代入曲线/曲面方程后可以把 $ds/dS$ 换成 $dx/dy$”被微元类型边界阻断。
- “无旋场必为保守场”被单连通与穿孔反例阻断。
- “散度为零意味着任意曲面通量为零”被封闭边界与奇点资格阻断。
- “三大公式只需记住代数形式”被方向、边界和光滑性资格门阻断。
- “复杂曲面只能直接参数化”被换面、补面、投影和 Gauss 分流替代。
- “第二型积分的奇偶性只看系数”被完整有向微元变换阻断。

## 状态与下一次检验

- 本次是 **Canonical Update + Candidate Rules + Bridge Routing**，不是已采用结论。
- 下一次最小检验：用同一几何对象分别计算第一型/第二型积分攻击微元分类；用穿孔旋转场攻击保守性；用非闭曲线补线、开曲面补面、内含奇点的封闭曲面攻击三大定理资格。
- 后续复核 Topic08 的投影/体积分接口、Topic06 的法向/参数接口，以及 B00 的内积投影边界。
