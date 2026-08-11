# B06B｜期望、联合概率与边缘化：概率的积分语言

状态：目录已建立，正文未建。

## Position

高数积分/重积分 × 概率联合分布与数字特征 Bridge。依赖 B06A。

## 两侧 Owner

- 高数：一元/高维累积、区域积分；
- 概率：期望、联合分布、边缘分布与条件结构。

## Mother Interface

期望：

$$
E[g(X)]=\int g(x)f_X(x)\,dx,
$$

联合概率：

$$
P((X,Y)\in D)=\iint_D f_{X,Y}(x,y)\,dx\,dy,
$$

边缘化：

$$
f_X(x)=\int f_{X,Y}(x,y)\,dy.
$$

统一理解：

$$
\boxed{\text{Probability Weight / Mass}\xrightarrow{\text{accumulate over what is retained or ignored}}\text{Target Probability or Summary}}
$$

## Owns

只拥有概率对象怎样调用一元/多元积分完成加权累积、区域汇总和“消去随机维度”的接口。

## Uses

B06A、高数累积 Topic、概率联合分布/数字特征 Topic。

## Boundary / Anti-Bridge

- 期望是概率加权平均，不是普通几何平均；
- marginalization 是汇总未观察维度，不等于条件化；
- 卷积若出现，需要从约束关系和概率贡献汇总解释，不能只记公式。

## Extension

一般测度积分和高维积分理论不进入主干。

## 待重构

以概率 Topic 和高数积分 Topic 的成熟正文为前置，再补最小母例。
