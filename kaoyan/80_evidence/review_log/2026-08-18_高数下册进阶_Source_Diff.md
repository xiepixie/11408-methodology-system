# 《高数下册进阶》Source Diff / Owner Diff

日期：2026-08-18  
场景：import / review correction  
状态：**Source 原子已逐项路由；Canonical / Practice 已修正，待人工审阅与陌生题验证**

## 1. 输入、边界与本轮目标

- 输入 Source：用户在会话中上传的 `高数下册进阶(1).md`。
- Source 身份：外部会话附件，不是当前仓库内可直接回修的 Canonical Source；因此已确认的原文错误在本台账登记为 `Conflict / Challenge`，不伪装成稳定知识。
- 本轮目标：只把 Source 中可靠的新机制、问题表示、训练动作和边界补入高数 Topic / Integration；**不处理 Subject Rules 下沉**。
- 主要 Owners：Topic07（多元局部模型）、Topic08（高维累积）、Topic12（常微分方程）、H-I01（微积分建模）。
- 判定词：
  - `Covered`：现有 Owner 已完整拥有，只补索引或不重复；
  - `Update`：Source 暴露真实缺口，本轮已补入 Canonical / Practice；
  - `Route`：内容真实，但唯一 Owner 在别处；
  - `Challenge`：Source 表述过强、分类不准、资格不完整，需要保留修正版边界；
  - `Reject`：硬错误、题面笔误或无法在当前定义域下稳定成立，不进入稳定模型。

## 2. Topic07｜多元微分与极值

| Source 原子 | 证据状态 | Owner / 落点 | 判定与处理 |
|---|---|---|---|
| 显函数偏导、特殊点按定义求偏导 | Material-explicit + established | `多元极限与可微判定.md` + Canonical | Covered；不重复造新规则 |
| 偏导符号不能当普通分数；固定变量决定导数含义 | Material-explicit + logically-derived | Canonical“偏导三层资格” + `复合偏导与变量变换.md` | **Update**；补“固定变量是导数身份的一部分”，禁止符号约分代替链式/隐式证明 |
| 多层复合偏导 | Material-explicit | `复合偏导与变量变换.md` | Update；依赖图 + Jacobian 组织 |
| 高阶复合偏导 | Material-explicit | Canonical 二阶链式 + `复合偏导与变量变换.md` | Update；补“外层曲率 + 内层曲率”两类项 |
| Source 标题“隐函数的高阶偏导”下实际例题为复合高阶链式 | Conflict（分类错误） | Topic07 复合偏导训练 | Challenge；按数学对象重新分类，不沿用 Source 标题 |
| 单方程隐函数一阶/二阶求导 | Material-explicit | `隐函数与多元极值.md` | Covered + Update；二阶先保留完整一阶导，再代目标点条件 |
| 多约束共同确定多个未知函数 | Material-explicit | Canonical 隐函数接口 + `复合偏导与变量变换.md` | Update；统一写成 Jacobian 线性系统 |
| 已知 $f_x,f_y$ 或全微分恢复函数 | Material-explicit | Canonical + `已知偏导与全微分反求函数.md` | Update；补函数型积分常数与相容性审计 |
| 已知混合偏导与边界迹恢复函数 | Material-explicit | `已知偏导与全微分反求函数.md` | Update；逐次积分 + 边界数据裁剪自由函数 |
| 沿路径/射线由梯度恢复函数差 | Material-explicit + logically-derived | Canonical + 反求函数训练 | Update；用一元基本定理解释 |
| 齐次函数 Euler 恒等式及逆向恢复 | Material-explicit + logically-derived | Canonical + `复合偏导与变量变换.md` | Update；补射线定义域边界 |
| PDE 线性变量变换 | Material-explicit | Canonical + `复合偏导与变量变换.md` | Update；先搬运微分算子再组合二阶项 |
| “先代后导更快” | Needs-qualification | Topic07 训练边界 | Challenge；只能先固定**非目标变量**到目标值后做相应一元切片求导，不能把所有变量先代成常数再求导 |
| 可微 / 全微分判定 | Material-explicit | `多元极限与可微判定.md` | Covered + boundary update |
| Source 把 $[f(x,y)-f(0,0)]/\sqrt{x^2+y^2}\to0$ 写成一般可微充要条件 | Conflict（数学错误） | `多元极限与可微判定.md` | **Reject 原结论**；修正为“可微且一阶线性主部为零”的充分条件；反例 $f(x,y)=x$ 阻断一般必要性 |
| 无约束极值 / Hessian | Material-explicit | `隐函数与多元极值.md` + B03 interface | Covered + Update |
| 首个非零齐次主部判极值 | Material-explicit + logically-derived | Canonical + `隐函数与多元极值.md` | Update；Hessian 是二阶特例 |
| 隐函数极值 | Material-explicit | `隐函数与多元极值.md` | Covered |
| Lagrange 乘子 | Material-explicit | `隐函数与多元极值.md` | Covered；保留正则约束资格 |
| 用 Cauchy / AM-GM 等全局不等式证书判极值 | Material-explicit | `隐函数与多元极值.md` | Update；等号条件必须与可行域闭合 |
| 闭区域全局最值与候选全集 | Material-explicit | `隐函数与多元极值.md` | Covered |
| $x^a y^b$ 在任意正实指数下直接用于含负坐标区域 | Conflict（定义域不完整） | 不进入 Canonical | Reject；除非题面补正值域/整数指数/绝对值等资格 |
| Source 个别例题定义 $z$ 却在问题中写“求 $u$” | Conflict（题面笔误） | 不进入稳定模型 | Reject typo；只迁移可确认的数学结构 |

## 3. Topic08 / H-I01｜二重积分、高维累积与旋转体

| Source 原子 | 证据状态 | Owner / 落点 | 判定与处理 |
|---|---|---|---|
| 从累次积分恢复真实区域 | Material-explicit | Topic08 Canonical + `二重积分区域、坐标与换序.md` | Covered |
| 内层上下限反向时先用一元定积分方向性归一化 | Material-explicit + established | Topic08 Canonical + 二重积分训练 | **Update**；先提负号，再把较小/较大边界解释为无向区域；边界交叉先分段 |
| 换序不是交换 $dx,dy$，而是重写同一区域 | Material-explicit | Topic08 | Covered |
| 一元外积分中嵌变限积分，可恢复成二维区域再比较换序 | Material-explicit | `二重积分区域、坐标与换序.md`；变限求导机制 Route Topic05 / H-B03 | **Update + Route**；只在升维能降低复杂度时使用 |
| 对称：轴/原点/交换 $x,y$ 等 | Material-explicit | Topic08 | Covered |
| 平移后暴露中心对称/径向结构 | Material-explicit | 二重积分训练 | Covered |
| 极坐标不限于圆域 | Material-explicit | Topic08 Canonical + Practice | Update；按“边界族 + integrand × measure”选择，不把圆当必要条件 |
| 一般边界族诱导坐标，如 $x+y,x-y$ 或 $xy,y/x$ | Material-explicit | Topic08 Canonical | Update；Jacobian determinant 解释仍 Route B02 |
| 分段 integrand：绝对值、$\min$、$\max$、取整 | Material-explicit | Topic08 Canonical + Practice | Update；先找内部切换界面 |
| 参数曲线给区域边界 | Material-explicit | 二重积分训练 | Update；参数只是边界表示，不自动成为二维坐标 |
| “参数边界最终一定换成 $t$” | Conflict（过度绝对化） | 不作为稳定规则 | Challenge；只在消元成本高且参数分支可控时保留参数 |
| 未知整体积分量先设为常数回代 | Material-explicit | `未知整体积分量回代.md` + Canonical | Update；退化标量方程单独分类 |
| 二维 Riemann 双重和识别 | Material-explicit | Topic08 Canonical + Practice | Update；索引不等式恢复真实极限区域 |
| 用二重积分证明一维积分不等式 | Material-explicit | Topic08 Canonical + Practice | Update；乘积域 + 交换对称制造点态定号 integrand |
| 二重积分面积/体积等基础量 | Material-explicit | Topic08 / H-I01 | Covered |
| 平面区域绕任意不穿域直线旋转的体积 | Material-explicit + qualification needed | H-I01 Canonical | **Route + Update**；$dV=2\pi r\,dA$ 只在轴不穿域且覆盖按一次计数时使用 |
| 任意轴旋转公式无条件累加 | Needs-qualification | H-I01 | Challenge；轴穿域、两侧同半径或自重叠时回到覆盖审计/截面法 |
| “极坐标只适合圆” | Conflict | Topic08 | Reject；Source 自身后文已给非圆域反例，稳定模型保留更一般坐标适配原则 |

## 4. Topic12｜常微分方程与跨章节构造

| Source 原子 | 证据状态 | Owner / 落点 | 判定与处理 |
|---|---|---|---|
| $y'=F(ax+by+c)$ 等整体代换 | Material-explicit | `常微分方程结构分流.md` | Covered；新文件不重复 |
| Euler--Cauchy 指定换元 | Material-explicit | Canonical + `常微分方程结构分流.md` | Covered；对数尺度是稳定 Owner |
| 交换自变量/因变量 | Material-explicit | Canonical + `陌生型微分方程的结构变换.md` | Update；补局部可逆与 $y'=0$ 分支 |
| 只更换独立变量，如 $u=e^x$、$x=\sin t$ | Material-explicit | Canonical + `陌生型微分方程的结构变换.md` | **Update**；新增一般重参数化公式 $dy/dx=Y_t/x_t$ 与二阶搬运；要求新参数局部一一 |
| 隐藏全导数/商导数/对数导数 | Material-explicit | Canonical + 陌生结构训练 | Update |
| 算子因式分解逐层降阶 | Material-explicit | Canonical + 陌生结构训练 | Update |
| “合理分配”式降阶/状态重写 | Material-explicit | Topic12 | Update；统一解释为寻找低维状态，而非孤立凑式 |
| 分段自由项 / 分段右端 | Material-explicit | `常微分方程结构分流.md` | Covered；接口缝合已有唯一训练入口 |
| $f'(x)=f(1-x)$、$f'(x)=f(2/x)$ 等变换自变量消元 | Material-explicit | Canonical + 陌生结构训练 | Update；用对合 $\phi\circ\phi=\mathrm{id}$ 闭合 |
| 周期条件下 $f(x)+f'(x+\pi)=\sin x$ 一类平移消元 | Material-explicit | Canonical + 陌生结构训练 | **Update**；推广为“平移量与周期形成有限采样轨道时，平移/求导—回写—消元” |
| 平移量与周期不成有理比仍默认有限步闭合 | Logically contradicted | Topic12 边界 | Reject；$a/T$ 无理时采样轨道通常不有限闭合 |
| 由含任意常数解族反求微分方程 | Material-explicit | `由解族反求方程与周期解.md` | Update；求导到足以消参数并回代原解族 |
| 多个同一非齐次方程特解作差得到 kernel | Material-explicit | 同上 | Update；从差恢复齐次根/基础解块 |
| 周期强迫的一阶线性方程周期解 | Material-explicit + logically-derived | Canonical + `由解族反求方程与周期解.md` | Update；$a\ne0$ 唯一，$a=0$ 需一周期平均为零且不唯一 |
| 只检查 $y(T)=y(0)$ 就直接宣布全局周期 | Needs-proof | Canonical + 周期解训练 | Challenge 已修；用平移解满足同一 ODE + 初值唯一性证明全局周期 |
| 常系数稳定性把所有纯虚根都视为有界稳定 | Conflict | Topic12 Canonical | Challenge 已修；简单纯虚根给持续有界振荡，重复零实部根可出现多项式增长 |
| 变限积分 / 积分方程构造 ODE | Material-explicit | `跨章节信息构造微分方程.md` + Route Topic05/H-B03 | Update |
| 几何量/物理量构造 ODE | Material-explicit | 跨章节训练 + Route H-I01 | Update + Route |
| 函数方程 + 导数定义构造 ODE | Material-explicit | 跨章节训练 + Topic03 interface | Update |
| 多元函数/PDE 压成单组合变量 ODE | Material-explicit | 跨章节训练 + Route Topic07 | Update + Route |
| 二重积分含径向未知函数，先极坐标降成一维再求导 | Material-explicit | 跨章节训练 + Route Topic08 | Update + Route |
| ODE + 反常积分 | Material-explicit | 跨章节训练 + Route Topic05 | Update；先证尾部衰减/边界项资格，再积分方程 |
| “只要最后求 $f(x)$ 基本就是 ODE” | Conflict（过度泛化） | 不进入稳定模型 | Reject；只有未知函数与变化率/累积/参数局部量形成可闭合关系时才尝试压成 ODE |

## 5. Source 级冲突与不进入 Canonical 的内容

1. **一般可微充要条件误写**：已由 Topic07 的统一线性主部定义与反例阻断。
2. **复合高阶偏导误标成隐函数高阶偏导**：已按对象重分类。
3. **任意正实指数幂的定义域未说明**：不导入不稳定例题结论。
4. **个别题面变量名错写**：只迁移可确认机制，不保存 typo 为训练资产。
5. **“参数边界一定用参数”“最后求函数就基本列 ODE”等绝对化经验**：降格为条件化候选或直接 Reject。
6. **旋转任意轴公式缺覆盖资格**：H-I01 已补“轴不穿域 + 一次覆盖”边界。
7. **周期解只验证单点端值**：已补全局充分性证明。

## 6. 本轮 Owner 变更与明确不变项

### Canonical / Practice 更新

- Topic07：偏导固定变量身份边界；复合高阶、函数恢复、PDE 换元、可微与极值主部沿既有补强链保留。
- Topic08：新增有向积分限归一化；新增“一元外积分嵌变限积分 -> 恢复二维区域 -> 比较换序”的局部接口。
- Topic12：新增一般独立变量重参数化；把函数采样消元从“对合”扩展到“周期平移有限轨道”。
- H-I01：继续拥有任意外部旋转轴的局部面积元建模与覆盖资格。

### 本轮明确不处理

- 不编辑 `10_数学一/90_学科做题规则/高等数学.md` 或其他 Subject Rules；Rules 下沉由用户单独负责。
- 不把 Source 的例题数量、章节标题或“高频”措辞当作知识拓扑证据。
- 不因本次 Source import 回滚工作区中其他独立改动；与本 Source 无关的 Topic07 切/法对象补强、Topic08 训练文件重构应在各自工作流审阅。

## 7. 验证状态与下一步证据

- Source 原子路由：本台账已完成逐项 Coverage / Update / Route / Challenge / Reject 登记。
- Knowledge Plane：本轮确认的缺口已进入唯一 Canonical Owner；不把 Source 硬错误导入稳定理论。
- Control Plane：新增动作留在同目录 Practice，不晋升 Subject Rules。
- Evidence Plane：当前证据来自 Source + 可复现数学推导，**尚无使用者陌生题表现证据**，所以各 Topic 继续标记“待人工确认 / 待陌生题验证”，不标“已采用”。
- 最小陌生题验证：
  1. Topic07：给三变量约束，改变“固定变量”检查偏导身份是否稳定；
  2. Topic08：给边界在外层区间内交换的反向积分限，检查是否先分段再恢复区域；
  3. Topic08：给外积分嵌变限积分，比较直接算与升维换序成本；
  4. Topic12：给 $x=\phi(t)$ 且 $\phi'$ 在端点为零的代换，检查是否主动分支；
  5. Topic12：分别给 $a/T\in\mathbb Q$ 与 $a/T\notin\mathbb Q$ 的周期平移采样关系，检查是否只在有限轨道时尝试有限消元。
