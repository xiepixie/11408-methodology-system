# B01｜局部线性化：微分 × 线性映射

状态：目录已建立，正文未建。

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

## 待重构

以高数多元可微旧稿和线代映射 Topic 为主要 Source Pack。
