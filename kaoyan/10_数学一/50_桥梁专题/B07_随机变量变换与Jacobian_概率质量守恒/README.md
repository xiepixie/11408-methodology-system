# B07｜随机变量变换与 Jacobian：概率质量守恒

状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## Position

高数坐标变换/Jacobian × 概率随机变量变换 Bridge。依赖 B02 + B06。

## 两侧 Owner

- 高数/线代接口：B02 Jacobian 与行列式；
- 概率：联合分布、随机变量变换与 support。

## Mother Interface

母命题：

$$
\boxed{\text{Probability Mass is Preserved under Re-expression}}
$$

一维：

$$
f_Y(y)=f_X(x)\left|\frac{dx}{dy}\right|.
$$

二维：

$$
f_{U,V}(u,v)=f_{X,Y}(x,y)\left|\frac{\partial(x,y)}{\partial(u,v)}\right|.
$$

## Owns

只拥有“概率质量守恒 + 坐标重表达 + Jacobian 体积因子”这一接口，以及 support 如何随变换同步迁移。

## Uses

B02、B06A/B06B、概率联合分布 Topic。

## Boundary / Anti-Bridge

- 变量变换不只换公式，还必须同步变换 support；
- Jacobian 使用正变换还是逆变换必须与密度表达的方向一致；
- 密度数值可以改变，守恒的是对应区域上的总概率质量。

## Extension

一般非一一变换、多分支变换只在考纲需要范围内讨论。

## Source Diff

概率变量变换 Topic 与 B02 已完成 Owner 复核；正文只保留质量守恒、support 迁移和多分支边界。

## Manual

- Canonical Source：[随机变量变换与Jacobian_概率质量守恒.tex](随机变量变换与Jacobian_概率质量守恒.tex)
- Published View：[随机变量变换与Jacobian_概率质量守恒.pdf](../../../90_publish/math1/随机变量变换与Jacobian_概率质量守恒.pdf)

## Review v1
已核对变量重表达、Jacobian 方向、support 迁移和多分支求和；明确守恒的是区域概率质量而非密度数值。下一轮用非一一变换和边界 support 题验证。
