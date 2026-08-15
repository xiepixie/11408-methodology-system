# 高数 Topic04《局部到整体》Source Diff

日期：2026-08-11  
场景：import  
结论：**Canonical Update + Candidate Rules + Bridge Routing**

## 输入与当前 Owner

- 主 Source：归档笔记 `I-07_零点定理与微分中值定理.md`（602 行）。
- 补充 Source：`I-06_一元微分：定义、计算、判定与几何应用.md` 的函数形状段落（单调、极值、凹凸、拐点、零点重数）。
- Bridge Source：`I-07.1_多中值点与中值点参数.md`（371 行）与 `I-07.2_插值余项与导数估计.md`（455 行），主体分流至 H-B02。
- Canonical Owner：`10_数学一/10_高等数学/04_局部到整体_中值定理与函数形状/局部到整体_中值定理与函数形状.tex`。
- Control Owner：`10_数学一/90_学科做题规则/高等数学.md`。

## Observable Facts

1. I-07 的核心不是定理名表，而是“待证导数表达式 → 辅助函数 → 端点等值/多零点 → Rolle 链 → 回译”。
2. I-07 同时收录乘积、商、对数导数、积分因子和变上限积分等构造接口；其中乘积/商是 Topic03 的机制，变限积分与 ODE 解族属于其他 Owner。
3. I-06 的函数形状段落把导数符号、极值候选、拐点、零点重数与 Rolle 数轴法放在同一组区间机制中，适合迁入 Topic04。
4. I-07.1 的插点法、中值点参数和 I-07.2 的 Lagrange/Hermite 余项、导数估计具有独立的“局部模型—区间误差”接口，不能在 Topic04 重复拥有。

## Source / Owner 路由

| Source 内容 | 最终去向 | 判定 |
|---|---|---|
| 介值/零点定理 | Topic04 | Canonical Update |
| Rolle、Lagrange、Cauchy 资格与定理链 | Topic04 | Canonical Update |
| 目标标准化、辅助函数反推、端点等值设计 | Topic04 + H-R21/H-R22/H-R23 | 机制 + Candidate Rules |
| 乘积/商/对数导数构造 | Topic04 的辅助函数接口；本体调用 Topic03 | Boundary / Use |
| 积分因子、变上限积分构造 | Topic04 最小接口；正则性和积分机制归 Topic05/H-B03 | Boundary / Use |
| 高阶 Rolle、零点与重零点 | Topic04 + H-R26 | Canonical Update + Candidate Rule |
| 多中值点插点法 | H-B02 + H-R24 | Bridge + Candidate Rule |
| 中值点参数渐近位置 | H-B02 | 不在 Topic04 重写 |
| Lagrange/Hermite 插值余项与导数估计 | H-B02 | 不在 Topic04 重写 |
| 导数符号到单调性 | Topic04 + H-R25 | Canonical Update + Candidate Rule |
| 驻点/不可导点/极值候选 | Topic04 + H-R25 | Canonical Update + Candidate Rule |
| 凹凸/拐点/零点重数 | Topic04 | Canonical Update |
| 曲率与局部二阶几何 | Topic03 | 不复制 |
| 一阶 ODE 整体解族 | Topic12 | 只保留积分因子调用接口 |

## 提炼出的母模型

$$
\boxed{
\text{Target}
\to\text{Auxiliary Function}
\to\text{Qualification}
\to\text{Boundary/Zero Design}
\to\text{Witness}
\to\text{Translate Back}}
$$

事实层含义：

- 中值定理把边界约束转成区间内部的存在性见证；
- 辅助函数必须同时解决导数匹配和端点/零点约束；
- 多零点或重零点经过反复 Rolle 产生高阶导数见证；
- Lagrange 把导数符号运输成函数值差异，因而产生单调性和形状；
- 驻点、二阶零点和中值点都是候选/存在性输出，必须经过符号、区间和资格确认。

贯穿母例选择 $f(x)=x^3-3x$：同一对象上运行导数符号→单调极值、二阶符号→拐点、割线修正→Lagrange 中值点，并展示“候选点直接当结论”的失败路径。

## Candidate Rules

新增 H-R20--H-R27：

- 中值定理逐项资格门；
- 目标表达式反推辅助函数；
- 常数导数优先减割线；
- Cauchy 先保留交叉相乘式；
- 多中值点先分割区间；
- 函数形状按候选—符号—端点；
- 高阶目标按零点/重零点计数；
- 直接积分不能替代边界设计。

这些动作来自 Source Diff 和机制重建，尚无使用者陌生题证据，全部保持“待验证”。

## 拒绝进入稳定主干的说法

- “找到原函数就能用 Rolle”被边界等值要求阻断。
- “$f'=0$ 就是极值、$f''=0$ 就是拐点”被候选/确认边界阻断。
- “Cauchy 总能写导数比”被分母资格阻断。
- “重复在同一区间套中值定理就有不同中值点”被 H-B02 插点边界阻断。
- “一个点的导数符号代表整个区间单调”被 Lagrange 的全区间要求阻断。

## 状态与下一次检验

- 本次是 **Canonical Update + Candidate Rules + Bridge Routing**，不是已采用结论。
- 下一次最小检验：用陌生证明题攻击辅助函数反推、Cauchy 分母、多个中值点和高阶 Rolle；用形状题攻击驻点/拐点候选与闭区间端点比较。
- 后续 H-B02 导入时，复核 Topic03→Topic04 的“有限局部模型→区间余项”和 Topic04→H-B02 的“零点链→误差估计”交接。
