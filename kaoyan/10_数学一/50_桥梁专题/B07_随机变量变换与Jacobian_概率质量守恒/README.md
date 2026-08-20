# B07｜随机变量变换与 Jacobian：概率质量守恒

状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## 定位

高数坐标变换/Jacobian × 概率随机变量变换 Bridge。依赖 B02 + B06。

## 为什么会想到这座桥

- **表面现象**：概率变量变换再次出现 Jacobian，而且公式常写成“原密度复合逆变换 × 逆 Jacobian”。
- **解释断点**：为什么概率密度会随坐标改变？为什么 support 必须同步变换？为什么多对一时还要把多个原像分支相加？
- **抽象提升**：概率本身属于事件/区域，不属于某一套坐标；坐标改变后，同一块概率质量必须不变，因此密度必须反向补偿微元的拉伸与压缩。

所以 B07 是 B02 的几何换元与概率质量观的真正汇合点：核心不变量是**同一原像区域承载的概率质量守恒**。

## 两侧 Owner

- 高数/线代接口：B02 Jacobian 与行列式；
- 概率：联合分布、随机变量变换与 support。

## 母接口

母命题：

$$
\boxed{\text{Probability Mass is Preserved under Re-expression}}
$$

一维：

$$
f_Y(y)=f_X(x)\left\lvert\frac{\mathrm{d}x}{\mathrm{d}y}\right\rvert.
$$

二维：

$$
f_{U,V}(u,v)=f_{X,Y}(x,y)\left\lvert\frac{\partial(x,y)}{\partial(u,v)}\right\rvert.
$$

## 本桥拥有

只拥有“概率质量守恒 + 坐标重表达 + Jacobian 体积因子”这一接口，以及 support 如何随变换同步迁移。

## 调用的上游

B02、B06A/B06B、概率联合分布 Topic。

## 边界与反桥

- 变量变换不只换公式，还必须同步变换 support；
- Jacobian 使用正变换还是逆变换必须与密度表达的方向一致；
- 密度数值可以改变，守恒的是对应区域上的总概率质量。

## 扩展

一般非一一变换、多分支变换只在考纲需要范围内讨论。

## 源资料核对

概率变量变换 Topic 与 B02 已完成 Owner 复核；正文只保留质量守恒、support 迁移和多分支边界。

## 训练导航

- [随机变量变换的逆像与 Jacobian](随机变量变换的逆像与Jacobian.md) —— 完整逆像、新支撑、局部逆分支与 probability Jacobian 的联合审计。

## 手册

- Canonical Source：[随机变量变换与Jacobian_概率质量守恒.tex](随机变量变换与Jacobian_概率质量守恒.tex)
- Published View：[随机变量变换与Jacobian_概率质量守恒.pdf](../../../90_publish/math1/随机变量变换与Jacobian_概率质量守恒.pdf)

## 第一轮审阅
已核对变量重表达、Jacobian 方向、support 迁移和多分支求和；明确守恒的是区域概率质量而非密度数值。下一轮用非一一变换和边界 support 题验证。
