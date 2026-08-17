# B03｜Hessian 与二次型：二阶局部形状 × 正定性

状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## Position

高数多元二阶局部模型 × 线代二次型的核心 Bridge。依赖 B01。

## 两侧 Owner

- 高数：多元局部模型、Hessian、多元极值；
- 线代：二次型、合同、惯性与正定。

## Mother Interface

在驻点附近：

$$
f(x+h)=f(x)+\frac12 h^T H h+o(\lVert h\rVert^2),
$$

因此：

$$
\boxed{\text{Local Second-Order Shape}\rightarrow\text{Quadratic Form}}
$$

## Owns

只拥有 Hessian 作为二阶局部模型时，怎样翻译成二次型符号结构来判断局部形状。

## Uses

B01、多元 Taylor、线代二次型与正定性。

## Boundary / Anti-Bridge

- Hessian 是点处二阶导数信息，二次型是其局部模型中的代数表示；两者不是同一对象；
- Hessian 判别失效时不能把“半正定”直接解释成极小值。

## Extension

Rayleigh quotient、广义特征值与更一般约束二次型只保留必要接口。

## Source Diff

旧 `II-03.1` 和线代二次型 Topic 已完成 Owner 复核；正文只保留二阶局部模型到二次型符号结构的翻译。

## Manual

- Canonical Source：[Hessian与二次型_二阶局部形状与正定性.tex](Hessian与二次型_二阶局部形状与正定性.tex)
- Published View：[Hessian与二次型_二阶局部形状与正定性.pdf](../../../90_publish/math1/Hessian与二次型_二阶局部形状与正定性.pdf)

## Review v1
已核对 Hessian 二阶局部模型到二次型符号判定的交接；明确半正定时判别可能失效。下一轮用退化驻点、方向限制和合同变换题验证。
