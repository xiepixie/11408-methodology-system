# B02｜Jacobian 与行列式：坐标变换 × 局部体积缩放

状态：目录已建立，正文未建。

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

## 待重构

以高数 II-01/II-04 与线代行列式 Topic 做 Source Diff。
