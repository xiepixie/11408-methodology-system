# B06A｜PDF 与 CDF：局部概率密度 × 累积

状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## 定位

高数积分基本定理 × 概率一维分布 Bridge；是 B06B、B07 的概率积分前置。

## 为什么会想到这座桥

- **表面现象**：连续型随机变量总在 $F(x)=\int_{-\infty}^x f(t)dt$ 与 $F'(x)=f(x)$ 之间切换。
- **解释断点**：为什么 PDF 不是点概率？为什么离散/混合分布不能机械求导？为什么 CDF 总存在而 PDF 不总存在？
- **抽象提升**：概率侧的 $F$ 是累计质量账本，$f$ 是绝对连续情形下的局部质量密度；高数 FTC 只负责在相应正则性下把“局部密度”和“累计量”接起来。

B06A 因而来自“概率里反复调用微积分，但对象资格并不相同”的断点；它的核心不是求导技巧，而是**累计对象与局部密度的资格边界**。

## 两侧 Owner

- 高数：定积分、变上限积分、FTC；
- 概率：随机变量、一维分布、CDF/PDF。

## 母接口

$$
F(x)=\int_{-\infty}^{x}f(t)\,dt,
$$

适当条件下：

$$
F'(x)=f(x).
$$

因此：

$$
\boxed{\text{Local Density}\rightarrow\text{Accumulation Function}\rightarrow\text{Recover Density}}
$$

## 本桥拥有

只拥有 PDF 与 CDF 之间“局部密度—累积—恢复”的 FTC 接口。

## 调用的上游

高数一元累积 Topic、概率一维分布 Topic。

## 边界与反桥

- CDF 总存在，但 PDF 不一定存在；
- $F'(x)=f(x)$ 需要相应正则性，不能把离散分布硬写成普通密度；
- density 值不是概率本身。

## 扩展

测度/Radon–Nikodym 视角不进入当前主干。

## 源资料核对

概率一维分布 Topic 与高数 FTC 相关材料已完成 Owner 复核；正文只保留 CDF/PDF 层级和正则性边界。

## 训练导航

- [CDF 与 PDF 的局部累积切换](CDF与PDF的局部累积切换.md) —— 先辨 CDF/密度/原子，再在连续段调用 FTC 做局部—累积切换。

## 手册

- Canonical Source：[PDF与CDF_局部概率密度与累积.tex](PDF与CDF_局部概率密度与累积.tex)
- Published View：[PDF与CDF_局部概率密度与累积.pdf](../../../90_publish/math1/PDF与CDF_局部概率密度与累积.pdf)

## 第一轮审阅
已核对 CDF、PDF、区间概率和 FTC 正则性，明确密度值不是点概率。下一轮用含跳点 CDF、无密度分布和端点概率题验证。
