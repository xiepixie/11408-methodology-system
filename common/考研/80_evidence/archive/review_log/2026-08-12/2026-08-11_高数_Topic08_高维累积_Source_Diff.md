# 高数 Topic08《高维累积：区域、坐标与 Jacobian》Source Diff

日期：2026-08-11
场景：import
结论：**Canonical Update + Candidate Rules + Bridge Routing**

## 输入与当前 Owner

- 主 Source：归档笔记 `II-04_重积分计算.md`、`II-04.1_重积分综合题型.md`。
- Canonical Owner：`10_数学一/10_高等数学/08_高维累积_区域坐标与Jacobian/高维累积_区域坐标与Jacobian.tex`。
- Control Owner：`10_数学一/90_学科做题规则/高等数学.md`。
- Bridge Owners：B02（Jacobian 与行列式）、B07（随机变量变换与概率质量守恒）；Topic09 接收定向边界接口。

## Observable Facts

1. 重积分的关键是把真实几何域编码为可扫描的区域，而不是机械交换微分符号。
2. 一根扫描针必须在每个子区域内只穿过一个连续线段；边界交点、孔洞、绝对值和最大/最小分界会触发分区。
3. 换序保持同一区域；换元则同时搬运边界、被积函数和面积/体积微元。
4. 对称性必须同时检查区域保持、函数变换和 Jacobian；只看函数奇偶不足以判零。
5. 三维累积在投影穿针与截面切片之间选择，$f=f(z)$ 时可降为截面积加权的一维积分。
6. 极/柱/球坐标的主要错误是漏微元因子、混淆角度约定或重复覆盖。
7. 收缩区域积分先由平均值和面积锁定首阶；点值消失后才用尺度换元、Taylor 与区域矩。
8. 未知整体积分可设为常数降为标量方程；混合偏导在矩形上可由二维基本定理降至四角边界值。

## Source / Owner 路由

| Source 内容 | 最终去向 | 判定 |
|---|---|---|
| II-04 重积分对象/面积体积质量 | Topic08 + H-R54/H-R64 | Canonical Update + Candidate Rules |
| II-04 区域表示、扫描与分区 | Topic08 + H-R55 | Canonical Update + Candidate Rule |
| II-04 换序与可积性 | Topic08 + H-R56 | 机制 + 资格边界 |
| II-04 对称性 | Topic08 + H-R57 | 机制压缩 |
| II-04 极柱球与一般换元 | Topic08 + H-R58/H-R60 | Canonical Update + Bridge Routing |
| II-04 三重投影/切片 | Topic08 + H-R59 | Canonical Update + Candidate Rule |
| II-04 物理量与量纲 | Topic08 + H-R64 | 建模与验证 |
| II-04.1 收缩区域极限 | Topic08 + H-R61 | Canonical Update + Candidate Rule |
| II-04.1 参数积分求导 | Topic08 只保留合法性接口；导数机制接 Topic05/Topic07 | 不复制 |
| II-04.1 未知整体积分 | Topic08 + H-R62 | 低维代数降维 |
| II-04.1 混合偏导积分 | Topic08 + H-R63 | 矩形四角与分部入口 |
| II-04.1 Green 公式与定向边界 | Topic09 | 不复制 |
| B02 Jacobian determinant/局部体积缩放 | B02 | 唯一机制 Owner |
| B07 概率密度变换/support | B07 | 不复制 |

## 提炼出的母模型

$$
\boxed{\text{Quantity / Region}\to\text{Geometric Encoding}\to\text{Scan / Coordinate Choice}\to\text{Bounds / Measure}\to\text{Accumulate}\to\text{Dimension Reduction}\to\text{Invariant Check}}
$$

事实层含义：

- 区域是第一对象，积分限只是它在某种扫描下的编码；
- 换序重写域，换元重写局部网格，二者都不能省略几何核对；
- Jacobian 是微元搬运的计算因子，行列式为何给体积缩放属于 B02；
- 复杂综合题优先追求降维：平均值主阶、固定区域、整体常数、边界值；
- 计算结果必须回到面积/体积、量纲、对称性、粗界和覆盖次数检查。

## Candidate Rules

新增 H-R54--H-R64：

- 重积分先确认对象与合法性；
- 区域扫描要求一根针只穿过一个连续线段；
- 交换次序先重建同一几何域；
- 对称性同时过域—函数两道门；
- 换元同步搬运域、函数与微元；
- 三重积分比较投影法与切片法的降维成本；
- 极柱球坐标先定约定和角度范围；
- 收缩区域先用平均值主阶；
- 未知整体积分先降为标量方程并检查退化；
- 混合偏导先辨认矩形边界；
- 最终用不变量做重积分闭环检查。

这些动作来自 Source Diff 与机制重建，尚无使用者陌生题证据，全部保持“待验证”。

## 拒绝进入稳定主干的说法

- “换序只是把 $dx,dy$ 调换”被同一区域重建要求阻断。
- “对称区域必然积分为零”被区域保持与函数变换双门阻断。
- “Jacobian 非零就能直接换元”被分支、覆盖和全局一一性边界阻断。
- “所有三重积分都先投影”被投影/切片降维比较替代。
- “球坐标只需记 $\rho^2$”被完整微元和角度约定阻断。
- “收缩积分点值为零就立刻洛必达”被平均值、尺度和区域矩优先级阻断。
- “设整体积分常数后必有唯一解”被退化方程分类阻断。
- “矩形混合偏导四角公式适用于任意区域”被移动边界与 Topic09 接口阻断。
- B02 的 determinant 体积缩放和 B07 的概率守恒不在 Topic08 重复定义。

## 状态与下一次检验

- 本次是 **Canonical Update + Candidate Rules + Bridge Routing**，不是已采用结论。
- 下一次最小检验：用边界交叉和孔洞题攻击扫描分区；用非一一双曲变换攻击覆盖审计；用角度范围易错的球坐标题攻击微元协议；用收缩区域点值为零和退化整体积分攻击综合降维。
- 建设 Topic09 时复核曲面积分的无向微元、Green/Gauss/Stokes 的边界方向与 Topic08 的体积分接口。
