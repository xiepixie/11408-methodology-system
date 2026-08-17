# 线性代数归档笔记 Source Migration 完成审计

> 日期：2026-08-11
>
> 性质：Evidence 层 Source Diff / Owner Diff 记录，不是新的知识 Owner。
>
> 来源：`I.P.A.R.A/学习领域/归档/线性代数/` 中 11 篇主题笔记，共约 9,000 行。

## 1. 审计口径

本轮不把旧笔记逐段搬运，也不以“原文全部出现”为完成标准。按 Handbook Contract，完成迁移需要同时满足：

1. 数学一主干中的机制进入唯一 Canonical Topic；
2. 题面信号、路径选择、检查与退出条件进入线性代数 Rules；
3. 重复解释不建立第二 Owner；
4. 超出数学一主干的高级内容只保留最小 Extension 指针，或继续留作 Source；
5. 旧笔记中的口诀、题型堆叠和未经真实做题验证的动作不直接晋升为已采用 Rule。

`_线性代数 MOC.md` 是旧导航，不计入 11 篇主题笔记；其地图职责已由 Canonical Subject Atlas 接管。`矩阵性质工具箱导图.canvas` 是派生视觉关系图，也不单独拥有知识。

## 2. 逐篇 Source Diff / Owner Diff

| Source | Canonical Owner / Control Owner | 迁入主干 | 保留为 Extension / Source |
|---|---|---|---|
| `行列式.md` | Topic02；Rules R-LA01--04 | determinant 的交替多线性、初等变换、Laplace/adjugate、具体与抽象 determinant 的合法计算边界 | 升阶法、Jacobi 公式、特殊行列式套路与记忆口诀不扩成机制主干 |
| `矩阵性质工具箱.md` | Topic02、Topic03、Topic05；Rules R-LA04--05、R-LA13、R-LA29 | adjugate、rank 分层与不等式、trace 的循环不变性、零化多项式、分块消元接口 | 一般 Schur 补与分块逆只留边界，不建立考试主干 |
| `常用矩阵.md` | Topic01、Topic02、Topic05、Topic06；Rules R-LA13、R-LA15、R-LA28 | 正交、对称/反对称、幂等/对合、数量/三角/初等矩阵按各自机制拆入 Owner | 大而全的矩阵类型目录不作为独立 Topic；正规矩阵仅保留 Extension 镜头 |
| `秩一矩阵.md` | Topic03、Topic05；Rule R-LA06；D-LA02 | 外积、image/kernel、$A^2=(\operatorname{tr}A)A$、谱与幂的 rank-one 主干 | SVD/伪逆及 Sherman--Morrison/Woodbury 继续留作 Extension / Source |
| `四大基本子空间与矩阵同解.md` | Topic03、Topic04；Rules R-LA07--09、R-LA22 | 四大子空间与正交补、$A^TA$ 的 kernel/rank/半定接口、齐次/非齐次同解与包含的拼接 rank 判据 | 正规方程与最小二乘不进入当前数学一主干，继续留作 Source |
| `相似对角化.md` | Topic05；Rules R-LA10--14 | 相似不变量、重数、可对角化判据、抽象表示矩阵、矩阵多项式与构造检查 | Jordan 完整分类不进入主干，只保留停止边界 |
| `矩阵可交换.md` | Topic05；Rule R-LA14 的共同换基边界 | 可交换矩阵保持特征子空间、同时对角化的充分条件与反例 | 中心化子、交换子、同时三角化与 Sylvester 接口只保留 Extension 指针 |
| `实对称矩阵.md` | Topic05、Topic06；Rules R-LA15、R-LA18、R-LA21 | 实对称谱定理、正交特征基、谱与二次型主轴、惯性/正定、Rayleigh quotient | Courant--Fischer、一般矩阵函数、范数与奇异值继续留作 Extension / Source |
| `实对称矩阵速解.md` | Topic05；Rules R-LA15--17 | 三阶实对称的任务分流、二重根平面、单根零空间叉乘、正交化与回代检查 | 速算动作全部保持待验证，不能凭旧笔记直接晋升为已采用 Rule |
| `二次型.md` | Topic06；Rules R-LA18--21、R-LA24 | 对称表示、合同、标准/规范形、惯性、正定、配方法失败分支、零点分类与球面极值 | 超出数学一主干的极小极大理论继续留作 Source |
| `Sylvester与Lyapunov方程.md` | Topic04、Topic05 的最小 Extension 指针 | 只保留“矩阵未知量仍服从逆像 + kernel”以及可交换/交换子通向 Sylvester 的接口 | Kronecker 向量化、谱分离、条件数、连续/离散 Lyapunov 稳定性与数值算法全部留作 Source |

## 3. Owner 结果

- Topic01：向量空间、子空间、基/坐标、内积、Gram--Schmidt 与正交矩阵基础。
- Topic02：线性映射、矩阵表示、矩阵运算、可逆、determinant 与 adjugate。
- Topic03：rank、kernel/image、四大基本子空间、低秩与 rank 运算。
- Topic04：$Ax=b$ 的可达性、仿射解集、同解/包含与矩阵方程 Extension。
- Topic05：相似、谱、对角化、实对称结构、矩阵多项式与可交换接口。
- Topic06：二次型、合同、惯性、正定、配方、零点与 Rayleigh quotient。
- 线性代数 Rules：29 条待验证动作与 5 条已否定规则；旧笔记本身不构成“已采用”证据。

## 4. 结论与下一步

本次迁移属于 **Canonical Update + Candidate Rules**：11 篇主题笔记的数学一主干已经拆入六册唯一 Owner，考试动作进入待验证 Rules，高级内容保留为 Extension / Source，没有建立平行正文。

下一步不是继续搬运旧稿，而是用使用者本人完成的真题/陌生题攻击 Rules，并重点检查 Topic02→03→04 与 Topic05→06 的跨册交接。只有真实题目暴露模型缺口时，才继续修改 Canonical Handbook。
