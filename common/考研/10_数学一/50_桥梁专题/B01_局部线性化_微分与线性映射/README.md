# B01｜局部线性化：微分 × 线性映射

状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## Position

高数微分 × 线性代数映射的基础 Bridge；B02、B03、B04 的前置接口。

## 两侧 Owner

- 高数：一元/多元局部模型 Topic；
- 线代：线性映射与矩阵表示 Topic。

## Mother Interface

$$
F(x+h)=F(x)+DF_x(h)+o(\lVert h\rVert),
$$

即：

$$
\boxed{\text{Differentiability}=\text{Existence of a Best Local Linear Map}}
$$

## Owns

只拥有“可微为什么等价于存在最佳局部线性映射，以及该映射怎样被矩阵表示”的翻译接口。

## Uses

导数/全微分、线性映射、矩阵表示、复合映射。

## Boundary / Anti-Bridge

- 偏导存在不等于存在统一局部线性映射；
- Jacobian matrix 是局部线性映射的表示，不等于原非线性函数本身。

## Extension

Fréchet derivative 的一般赋范空间版本只作方向提示。

## Source Diff

高数多元可微旧稿和线代映射 Topic 已完成 Owner 复核；正文只保留统一线性主部接口。

## Manual

- Canonical Source：[局部线性化_微分与线性映射.tex](局部线性化_微分与线性映射.tex)
- Published View：[局部线性化_微分与线性映射.pdf](../../../90_publish/局部线性化_微分与线性映射.pdf)

## Review v1
已核对可微到最佳局部线性映射、矩阵表示和误差项的接口；明确偏导存在不充分。下一轮用偏导存在但不可微、复合映射和坐标表示题验证。
