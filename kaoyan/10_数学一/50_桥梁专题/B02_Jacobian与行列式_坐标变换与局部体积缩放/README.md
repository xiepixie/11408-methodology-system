# B02｜Jacobian 与行列式：坐标变换 × 局部体积缩放

状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## Position

高数多元局部模型/高维累积 × 线代行列式的核心 Bridge。依赖 B01。

## 两侧 Owner

- 高数：多元可微、坐标变换、重积分换元；
- 线代：线性映射、矩阵表示、行列式。

## Mother Interface

$$
\boxed{\text{Nonlinear Coordinate Change}\xrightarrow{\text{localize}}\text{Linear Map}\xrightarrow{\det}\text{Local Area/Volume Scaling}}
$$

## Owns

只拥有 Jacobian matrix 到 determinant 体积因子的接口，以及换元公式中绝对值因子的几何解释。

## Uses

B01、线代行列式、高数重积分。

## Boundary / Anti-Bridge

- Jacobian matrix 与 Jacobian determinant 不得混同；
- 行列式为 0 表示局部维度压缩，不能机械套换元公式；
- “出现 determinant”本身不能证明存在本 Bridge。

## Extension

一般流形上的坐标变换不进入当前主干。

## Source Diff

高数 II-01/II-04 与线代行列式 Topic 已完成 Owner 复核；正文只保留变换方向、体积因子和失效边界。

## 训练导航

- [Jacobian 换元的方向与逆像](Jacobian换元的方向与逆像.md) —— 正/逆变换、新区域、覆盖分支与 determinant 方向的联合审计。

## Manual

- Canonical Source：[Jacobian与行列式_坐标变换与局部体积缩放.tex](Jacobian与行列式_坐标变换与局部体积缩放.tex)
- Published View：[Jacobian与行列式_坐标变换与局部体积缩放.pdf](../../../90_publish/math1/Jacobian与行列式_坐标变换与局部体积缩放.pdf)

## Review v1
已核对 Jacobian matrix、determinant、变换方向和绝对值因子的分层；保留零行列式与非一一变换的停止条件。下一轮用逆变换方向和 support 变化题验证。
