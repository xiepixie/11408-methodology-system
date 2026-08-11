# B08｜Fourier 与正交基：函数表示 × 正交投影

状态：目录已建立，正文未建。

## Position

高数 Fourier 级数 × 线代正交基/坐标 Bridge。依赖 B00。

## 两侧 Owner

- 高数：函数展开、Fourier 系数与收敛；
- 线代：内积、正交基、坐标与投影。

## Mother Interface

线代：

$$
v=\sum_i c_i e_i.
$$

Fourier：

$$
f\sim\sum_n c_n\phi_n.
$$

共同思想：

$$
\boxed{\text{Coordinate}=\text{Projection onto an Orthogonal Basis}}
$$

## Owns

只拥有“Fourier 系数为什么由内积/积分投影得到”的理解接口，不重新拥有 Fourier 收敛定理或 Gram–Schmidt。

## Uses

B00、高数函数展开 Topic、线代向量空间 Topic。

## Boundary / Anti-Bridge

- 有限维正交基展开与无限函数级数不能无条件等同；
- 写出 Fourier 系数不等于已经证明级数在每点恢复原函数；
- 正交不意味着概率独立。

## Extension

Hilbert space、完备性、Parseval 的一般函数空间理论属于真实 Extension，不进入主干证明体系。

## 待重构

待高数 Fourier Topic 与线代正交内容确认后完成 Source Diff。
