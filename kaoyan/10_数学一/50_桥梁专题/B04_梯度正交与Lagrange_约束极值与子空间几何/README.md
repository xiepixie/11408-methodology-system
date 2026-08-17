# B04｜梯度、正交与 Lagrange：约束极值 × 子空间几何

状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## Position

高数约束极值 × 线代内积/子空间几何 Bridge。依赖 B00 + B01。

## 两侧 Owner

- 高数：梯度、隐式曲面、Lagrange 乘子、多元极值；
- 线代：内积、正交、子空间与投影语言。

## Mother Interface

约束 $g(x)=c$ 限制可行方向，$\nabla g$ 属于法方向；极值时目标梯度不能在任何允许切向上继续增长，因此：

$$
\boxed{\text{Tangent Space}\perp\text{Normal Space}},
\qquad
\nabla f=\lambda\nabla g.
$$

## Owns

只拥有“允许方向/切空间—法空间—梯度平行”这一接口解释。

## Uses

B00、B01、高数隐函数与约束极值机制。

## Boundary / Anti-Bridge

- $\nabla f=\lambda\nabla g$ 需要正则约束等前提，不能脱离条件机械使用；
- “梯度垂直等值面”不能在梯度为零的奇异点无条件使用。

## Extension

多约束下的法空间、KKT 等只作未来方向，不进入数学一主干。

## Source Diff

旧多元微分/极值笔记和线代正交内容已完成 Owner 复核；正文只保留切空间—法空间—乘子接口。

## Manual

- Canonical Source：[梯度正交与Lagrange_约束极值与子空间几何.tex](梯度正交与Lagrange_约束极值与子空间几何.tex)
- Published View：[梯度正交与Lagrange_约束极值与子空间几何.pdf](../../../90_publish/math1/梯度正交与Lagrange_约束极值与子空间几何.pdf)

## Review v1
已核对可行切向、法空间、梯度平行和正则约束条件；保留奇异梯度与多约束 KKT 的边界。下一轮用梯度为零、约束梯度相关和边界约束题验证。
