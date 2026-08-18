# 秩、基本子空间与等价

> 状态：待人工确认；已发布。Canonical LaTeX 第一版正文与 PDF 已建立，等待内容确认。

## 为什么值得读

rank 经常被学成“消元以后数主元”，但这只是计算表象。

真正的问题是：一个线性作用把输入送出去以后，**有多少独立自由度还能被输出看见，又有多少自由度被彻底压掉？** 一旦把这个问题说清，rank-nullity、矩阵等价、乘积 rank、$AB=0$、伴随矩阵 rank 都会落到同一张自由度账本上。

## 母问题

> **一个线性作用到底保留了多少独立自由度，又把多少自由度压掉了？**

主线是：

```text
输入空间
-> kernel：被抹除的方向
-> image：可见输出方向
-> rank-nullity
-> 主元 / 最大非零子式 / 行列秩
-> 矩阵等价标准形
-> 复合时 Im(B) 与 ker(A) 的碰撞
```

## 本册覆盖到哪里

本 Topic 负责：

- rank、kernel、image 与 nullity；
- rank-nullity 的生成证明；
- 行秩=列秩、主元数、最大非零子式阶数；
- 矩阵等价与 $\begin{pmatrix}I_r&0\\0&0\end{pmatrix}$ 标准形；
- 初等变换对 rank / row / column / kernel 的影响；
- row space 与 $N(A^T)$ 作为 kernel/image 的正交镜像；
- rank-one 结构；
- $r(A+B)$、$r(AB)$、Sylvester 下界、$AB=0$；
- $r(A^TA)=r(A)$、伴随矩阵 rank 分层；
- 含参数 rank 的结构跳变机制。

本 Topic **不负责**：

- 给定 $Ax=b$ 的相容性、通解、基础解系和同解问题；
- 相似、特征值、对角化；
- 二次型合同与惯性。

完整方程组结构由 Topic04 接管。

## 训练导航

- [秩的结构判断与乘积边界](秩的结构判断与乘积边界.md) —— 从独立方向、外积、参数跳变和 $\operatorname{Im}B\cap\ker A$ 判断 rank，并阻断“rank = 非零特征值个数”等误联想。

## 与其他册怎样连接

- 上位地图：[线性代数 Subject Atlas](../README.md)
- 前置：[线性映射、矩阵与行列式](../02_线性映射_矩阵与行列式/README.md)
- 基与维数：[向量空间：生成、基与坐标](../01_向量空间_生成基与坐标/README.md)
- 下一册：[线性方程组：可达性与解空间](../04_线性方程组_可达性与解空间/README.md)

## 正文与发布

- Canonical LaTeX：[秩_基本子空间与等价.tex](秩_基本子空间与等价.tex)
- Published PDF：[秩_基本子空间与等价.pdf](../../../90_publish/math1/秩_基本子空间与等价.pdf)

旧 [Markdown 工作稿](秩、基本子空间与等价.md) 保留为 Source Diff 记录，不再作为正文 Owner。
