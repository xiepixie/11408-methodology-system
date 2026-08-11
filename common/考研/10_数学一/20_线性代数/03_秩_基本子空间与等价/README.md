# 秩、基本子空间与等价

> 状态：Markdown 工作稿待迁入 LaTeX；已完成自由度分解、四大基本子空间与等价机制的 Source 工作稿，待迁入 Canonical LaTeX 后再由使用者审查。

## 0. 本册定位

本 Topic 回答：**一个线性作用保留了多少独立方向，又把哪些方向压掉？**

- **Owns**：rank、rank-nullity、行/列/零/左零空间、矩阵等价、rank 不等式、低秩结构。
- **Uses**：[向量空间](../01_向量空间_生成基与坐标/README.md)与[线性映射](../02_线性映射_矩阵与行列式/README.md)。
- **Does not own**：给定右端项的完整解集、相似分类与二次型惯性。
- **Output**：输入自由度如何分解成不可见方向与可达输出，以及可供方程组调用的结构摘要。

## 1. 根本问题：rank 测量可见输出的维数

对 $A\in\mathbb R^{m\times n}$，视作映射

$$
A:\mathbb R^n\to\mathbb R^m.
$$

列空间是所有可达输出，零空间是所有被映射压成零的输入：

$$
\operatorname{Col}(A)=\operatorname{Im}A,
\qquad
N(A)=\ker A.
$$

于是

$$
\boxed{r(A)=\dim\operatorname{Col}(A)},
$$

并有

$$
\boxed{n=r(A)+\dim N(A).}
$$

这不是两个维数恰好相加，而是每个输入自由度最终要么形成一个可见输出方向，要么落入不可见的 kernel。

## 2. 行秩为什么等于列秩

消元找到主元数，它既给出列空间的独立方向数，也给出行空间的独立约束数。定理

$$
\dim\operatorname{Row}(A)=\dim\operatorname{Col}(A)
$$

使“rank”无需分成两个数。

但这不意味着行空间等于列空间：对非方阵它们甚至位于不同环境空间。相等的是维数，不是集合。

## 3. 四大基本子空间

| 子空间 | 所在空间 | 机制意义 | 维数 |
|---|---|---|---:|
| $\operatorname{Col}(A)$ | $\mathbb R^m$ | 可达输出 | $r$ |
| $N(A)$ | $\mathbb R^n$ | 被抹除的输入 | $n-r$ |
| $\operatorname{Row}(A)=\operatorname{Col}(A^T)$ | $\mathbb R^n$ | 真正参与输出的输入方向 | $r$ |
| $N(A^T)$ | $\mathbb R^m$ | 与所有可达输出正交的方向 | $m-r$ |

在标准内积下，

$$
N(A)=\operatorname{Row}(A)^\perp,
\qquad
N(A^T)=\operatorname{Col}(A)^\perp.
$$

因此输入空间和输出空间各自被拆成一对正交互补结构：

$$
\mathbb R^n=\operatorname{Row}(A)\oplus N(A),
$$

$$
\mathbb R^m=\operatorname{Col}(A)\oplus N(A^T).
$$

## 4. 初等变换保护什么

左乘可逆矩阵 $P$ 得 $PA$，不会改变列之间的线性关系和 rank，但一般会改变列空间在 $\mathbb R^m$ 中的具体位置；行空间保持为同一子空间。

右乘可逆矩阵 $Q$ 得 $AQ$，不会改变列空间和 rank，但会重组输入坐标，因此零空间按 $Q^{-1}$ 对应变换。

双侧可逆变换

$$
B=PAQ
$$

定义矩阵等价。rank 是这种关系的完全分类不变量：两个同型矩阵等价当且仅当 rank 相同，并都可化为

$$
\begin{pmatrix}I_r&0\\0&0\end{pmatrix}.
$$

## 5. 母例：rank-one 映射

令

$$
A=uv^T,\qquad u\ne0,\ v\ne0.
$$

则

$$
Ax=u(v^Tx).
$$

所有输出都是 $u$ 的倍数，所以

$$
\operatorname{Col}(A)=\operatorname{span}\{u\},\qquad r(A)=1.
$$

被压掉的输入满足 $v^Tx=0$，故

$$
N(A)=v^\perp.
$$

并且

$$
A^2=(v^Tu)A.
$$

这个例子说明低秩不是“元素少”，而是作用只通过少数标量通道传递信息。

## 6. 复合映射的 rank：中间瓶颈限制信息流

对可乘矩阵，

$$
r(AB)\le\min\{r(A),r(B)\}.
$$

因为 $B$ 先把输入压入 $\operatorname{Im}B$，$A$ 再作用，后续不可能恢复已经丢失的独立方向。

更精确地，

$$
r(AB)\ge r(A)+r(B)-n
$$

（中间维数为 $n$）。这一不等式表达：$B$ 的输出与 $A$ 的 kernel 最坏能重叠多少。

若 $AB=0$，则

$$
\operatorname{Im}B\subseteq\ker A,
$$

从而

$$
r(B)\le n-r(A),\qquad r(A)+r(B)\le n.
$$

## 7. 参数 rank：只在结构跳变点分类

含参数矩阵的 rank 通常在一般参数下稳定，只在主元或关键子式消失时下降。安全做法是：

1. 先做不需要除以含参数式的消元；
2. 收集可能为零的关键因子；
3. 分一般值与特殊值；
4. 每个分支重新数主元。

若未经分类就除以 $a-c$，相当于静默丢弃 $a=c$ 的结构分支。

## 8. 边界与最小反例

| 概念 A | $\ne$ | 概念 B | 真正区别 | 最小反例/后果 |
|---|:---:|---|---|---|
| 行空间 | $\ne$ | 列空间 | 所在环境空间不同，只保证维数相等 | 非方阵中不能写成同一集合 |
| 行变换保持 rank | $\ne$ | 行变换保持列空间 | 可逆左乘会移动输出方向 | 一列向量可被可逆矩阵旋转 |
| rank | $\ne$ | 非零行数 | 未化阶梯形时非零行可能相关 | 两个相同行均非零但只贡献一个方向 |
| 同 rank | $\ne$ | 相似 | 同 rank 只保证等价 | $I_2$ 与 $\operatorname{diag}(1,2)$ 等价但不相似 |
| $r(AB)=r(A)r(B)$ | $\ne$ | 正确乘积规律 | rank 受中间空间瓶颈限制 | 该乘法公式一般错误 |
| $AB=0$ | $\ne$ | $A=0$ 或 $B=0$ | 非零 image 可落入非零 kernel | 两个非零矩阵乘积可为零 |

## 9. 题目调用协议

1. 把矩阵看成 $\mathbb R^n\to\mathbb R^m$，先标输入和输出维数；
2. 判断目标是可达方向、被抹除方向、独立约束还是等价分类；
3. 通过消元找主元与自由变量，但解释回四个基本子空间；
4. 遇到乘积先写 $\operatorname{Im}B$ 与 $\ker A$ 的关系；
5. 含参数时先定位 rank 跳变点，再分支；
6. 用 $r+\operatorname{nullity}=n$ 和维数上界校验。

## 10. 一页压缩

$$
\boxed{\text{rank 是可见自由度；nullity 是被抹除自由度。}}
$$

$$
\boxed{\text{等价允许两端独立换基，因此只剩 rank。}}
$$

复原问题：输入经过这张矩阵后，哪些方向留下、哪些消失、输出最多占几维？
