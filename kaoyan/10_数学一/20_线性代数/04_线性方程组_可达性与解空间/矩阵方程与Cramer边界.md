# 矩阵方程与 Cramer 边界

> 训练定位：训练 $AX=B$、$XA=B$ 等矩阵方程的拆解、存在性、唯一性与通解，并明确 Cramer 法则只属于“方阵可逆、唯一解”的显式坐标公式。  
> 模型归属：[线性方程组：可达性与解空间](线性方程组_可达性与解空间.tex) 负责矩阵方程作为逆像问题、Cramer 法则结构位置的理论机制；本文只负责题面路由、第一动作、交付深度和错误边界。

## 1. 矩阵未知量并没有改变母问题

矩阵方程看起来比 $Ax=b$ 大很多，但本质只是把多个向量逆像问题装进同一个矩阵中。

对

$$
AX=B,
$$

把

$$
X=(x_1,\ldots,x_k),
\qquad
B=(b_1,\ldots,b_k),
$$

按列展开，就得到

$$
Ax_j=b_j
\qquad(j=1,\ldots,k).
$$

因此：

$$
\boxed{
AX=B\text{ 有解}
\iff
b_j\in\operatorname{Im}A\text{ 对所有 }j.
}
$$

---

## 2. $AX=B$：按列拆是默认第一动作

### 局部规则：先看 A 的可逆性决定是否值得直接乘逆

**触发信号**：$AX=B$，未知矩阵 $X$ 在右侧。

**第一动作**：

- 若已知 $A$ 可逆：直接写

$$
X=A^{-1}B;
$$

- 若 $A$ 未知是否可逆或明显奇异：按列拆成多个 $Ax_j=b_j$，分别做可达性判断。

**检查与退出**：若只问存在性，不必求出每一列的完整通解；只需确认每个 $b_j$ 都落在 $\operatorname{Im}A$ 中。

---

## 3. $AX=B$ 的全部解：一个矩阵特解 + 每列都在 kernel 的自由矩阵

若 $X_0$ 满足

$$
AX_0=B,
$$

则任意另一个解 $X$ 满足

$$
A(X-X_0)=0.
$$

令

$$
Z=X-X_0,
$$

则

$$
AZ=0.
$$

这等价于 $Z$ 的每一列都属于 $\ker A$。所以

$$
\boxed{X=X_0+Z,\qquad AZ=0.}
$$

### 局部规则：矩阵通解按列复用同一组 kernel 基

**触发信号**：$AX=B$ 且需要求出全部解（非唯一）。

**第一动作**：求出 $A$ 的基础解系 $\ker A=\operatorname{span}\{\xi_1,\ldots,\xi_s\}$，将自由部分 $Z$ 的每一列表示为这些基向量的线性组合。

**检查与退出**：验证

$$
AX_0=B,
\qquad
AZ=0.
$$

不要把“一个矩阵特解”误当唯一解；唯一性仍由

$$
\ker A=\{0\}
$$

决定。

---

## 4. $XA=B$：优先转置成按列问题

若

$$
XA=B,
$$

则转置后：

$$
A^TX^T=B^T.
$$

这重新变成标准的“已知矩阵左乘未知列块”的问题。

### 局部规则：A 不可逆时不要强写 $BA^{-1}$

**触发信号**：$XA=B$，但题目没有给 $A$ 可逆。

**第一动作**：转置为

$$
A^TX^T=B^T,
$$

按列检查 $B^T$ 的各列是否属于 $\operatorname{Im}A^T$。

**检查与退出**：若 $A$ 可逆，当然退化为

$$
X=BA^{-1}.
$$

若不可逆，存在性与自由度由 $A^T$ 的 image/kernel 控制，不能把标量“除法”直觉搬进来。

---

## 5. 一个最小例子：奇异 A 仍可能有矩阵方程解

取

$$
A=
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
2&3\\
2&3
\end{pmatrix}.
$$

$A$ 奇异，但 $B$ 的每一列都是 $(1,1)^T$ 的倍数，因此都属于 $\operatorname{Im}A$，所以 $AX=B$ 有解。

例如取

$$
X_0=
\begin{pmatrix}
2&3\\
0&0
\end{pmatrix}.
$$

因为

$$
\ker A
=
\operatorname{span}
\left\{
\begin{pmatrix}1\\-1\end{pmatrix}
\right\},
$$

全部解可写成

$$
X
=
X_0+
\begin{pmatrix}
\alpha&\beta\\
-\alpha&-\beta
\end{pmatrix}.
$$

这里每一列都有一个独立的 kernel 参数。

#### 母题：含参数矩阵方程要同时分类“可逆性 + 每列相容性”

考虑

$$
\begin{pmatrix}
1&-1&-1\\
2&k&1\\
-1&1&k
\end{pmatrix}X
=
\begin{pmatrix}
2&2\\
1&k\\
-k-1&-2
\end{pmatrix}.
$$

记左侧系数矩阵为 $A(k)$。安全消元后关键主元为

$$
k+2,
\qquad
k-1,
$$

因此只有 $k=-2,1$ 可能发生结构跳变；而

$$
\det A(k)=(k+2)(k-1).
$$

- $k\ne-2,1$：$A(k)$ 可逆，矩阵方程有唯一解；
- $k=-2$：增广块出现矛盾行，至少有一列右端不在 $\operatorname{Im}A$ 中，所以无解；
- $k=1$：系数 rank 降为 $2$，两列右端仍都可达，因此有无穷多矩阵解，每一列都沿同一个 $\ker A$ 方向带自由参数。

这道母题把参数题的正确顺序固定下来：

$$
\boxed{\text{先找 }A(k)\text{ 的结构跳变}\to\text{临界点再审计各右端列}\to\text{最后才写矩阵通解}.}
$$

不能只看 $\det A=0$ 就把两个临界参数都判成“无穷多解”。

---

## 6. Cramer 法则的资格：必须先确认“方阵 + det 非零”

对

$$
Ax=b,
\qquad A\in\mathbb R^{n\times n},
$$

只有当

$$
\det A\ne0
$$

时，Cramer 法则才给出

$$
\boxed{x_i=\frac{\det A_i}{\det A}},
$$

其中 $A_i$ 是把 $A$ 的第 $i$ 列替换为 $b$ 的矩阵。

### 局部规则：看到“用 Cramer”先做资格审计

**触发信号**：题目点名 Cramer，或给小阶方阵并要求某一个未知量的显式表达。

**第一动作**：先确认

1. $A$ 是方阵；
2. $\det A\ne0$。

**检查与退出**：若 $\det A=0$，Cramer 分母失效，不能继续套公式；此时转回 rank / 可达性 / kernel 语言。

---

## 7. Cramer 不是“求解线性方程组的总方法”

Cramer 的优势是：在已知唯一解的方阵情形中，能够直接给某个坐标的 determinant 表达式。

它不适合以下结构：

- 欠定系统；
- 超定系统；
- 奇异方阵；
- 只问有无解或自由度；
- 需要基础解系或通解结构；
- 矩阵规模较大、直接消元明显更便宜。

### 局部规则：先读交付目标，再决定是否值得 Cramer

**触发信号**：方阵可逆，但题目没有强制方法。

**第一动作**：比较目标：

- 只求一个分量、determinant 结构很简单 → Cramer 可有优势；
- 求全部未知量 → 消元或逆像结构通常更直接；
- 只问唯一性 → 只判 $\det A\ne0$ 即可。

**检查与退出**：不要为了展示公式，在 rank 已经给出结论后额外做 $n+1$ 个 determinant。

---

## 8. Cramer 与伴随矩阵/逆矩阵是同一个可逆结构的不同坐标展开

当

$$
\det A\ne0,
$$

有

$$
A^{-1}
=
\frac{1}{\det A}\operatorname{adj}(A),
$$

因此

$$
x=A^{-1}b
$$

的第 $i$ 个坐标整理后正是

$$
x_i=\frac{\det A_i}{\det A}.
$$

所以：

$$
\boxed{
\text{Cramer 不是新的世界模型，而是可逆方阵唯一逆像的坐标公式。}
}
$$

---

## 9. 左右位置边界：$AX=B$ 与 $XA=B$ 不可互换

若 $A$ 可逆：

$$
AX=B
\Longrightarrow
X=A^{-1}B,
$$

而

$$
XA=B
\Longrightarrow
X=BA^{-1}.
$$

### 局部规则：最后必须乘回原式

**触发信号**：已经求出候选 $X$。

**第一动作**：直接代回检查

$$
AX\stackrel{?}{=}B
$$

或

$$
XA\stackrel{?}{=}B.
$$

**检查与退出**：这是最便宜且独立的方向校验，尤其能抓出把 $A^{-1}$ 乘错侧的错误。

---

## 10. 矩阵方程的存在性与自由度可以不求 X 就直接读出

### $AX=B$：看列空间

设

$$
A\in\mathbb R^{m\times n},
\qquad
X\in\mathbb R^{n\times k},
\qquad
B\in\mathbb R^{m\times k}.
$$

因为 $AX=B$ 等价于 $k$ 个系统 $Ax_j=b_j$，所以

$$
\boxed{
AX=B\text{ 有解}
\iff
\operatorname{Col}(B)\subseteq\operatorname{Col}(A)
\iff
r(A\ B)=r(A).
}
$$

这里 $(A\ B)$ 表示把 $B$ 的列整体接在 $A$ 右侧。

若有解，每一列都有 $n-r(A)$ 个自由方向，而且各列参数彼此独立，因此整个矩阵解集的仿射维数为

$$
\boxed{k\bigl(n-r(A)\bigr).}
$$

所以给定 $B$ 时，$AX=B$ 唯一可解当且仅当系统相容且

$$
r(A)=n.
$$

### $XA=B$：看行空间

设

$$
A\in\mathbb R^{m\times n},
\qquad
X\in\mathbb R^{p\times m},
\qquad
B\in\mathbb R^{p\times n}.
$$

逐行看，每一行都在求

$$
y^TA=b^T,
$$

所以

$$
\boxed{
XA=B\text{ 有解}
\iff
\operatorname{Row}(B)\subseteq\operatorname{Row}(A)
\iff
r\begin{pmatrix}A\\B\end{pmatrix}=r(A).
}
$$

若有解，每一行的自由度为

$$
m-r(A),
$$

故整个矩阵解集的仿射维数为

$$
\boxed{p\bigl(m-r(A)\bigr).}
$$

给定 $B$ 时，$XA=B$ 唯一可解当且仅当系统相容且

$$
r(A)=m.
$$

这两个结论把“未知矩阵有多少参数”也统一回 kernel / left-kernel 的自由度账本。

### 更高一层：把“左乘 A”本身看成线性映射

固定 $A$，定义矩阵空间上的线性映射

$$
\mathcal L_A(X)=AX.
$$

那么 $AX=B$ 就是在求

$$
\mathcal L_A^{-1}(B).
$$

它和向量方程完全同构：

$$
\ker\mathcal L_A
=
\{Z:AZ=0\},
$$

而 $Z$ 的每一列都能独立取 $\ker A$ 中的向量，因此

$$
\dim\ker\mathcal L_A
=k\dim\ker A
=k(n-r(A)).
$$

同时

$$
\dim\operatorname{Im}\mathcal L_A
=kr(A).
$$

这正好满足矩阵空间版本的 rank--nullity：

$$
kn
=
kr(A)+k(n-r(A)).
$$

所以“每列有一套独立参数”不是经验观察，而是矩阵空间上同一个 fiber + kernel 机制的必然结果。$XA=B$ 也可对右乘映射作完全平行的解释。

---

## 11. 什么时候不该显式求 X

| 交付目标 | 第一动作 | 停止条件 |
|---|---|---|
| 只问 $AX=B$ 是否有解 | 检查 $\operatorname{Col}(B)\subseteq\operatorname{Col}(A)$ | rank 不再增加即可停 |
| 只问 $XA=B$ 是否有解 | 检查 $\operatorname{Row}(B)\subseteq\operatorname{Row}(A)$ | 纵向拼接 rank 不再增加即可停 |
| 只问唯一性 | 先确认相容，再检查相应 kernel 是否为零 | 不必求具体矩阵 |
| 求自由参数个数 | 用列数/行数乘对应 nullity | 不必构造每个参数向量 |
| 求完整通解 | 找 $X_0$ 后再写齐次自由部分 | 验证原式与自由部分归零 |

矩阵方程比向量方程更容易出现“算得太多”：一旦题目只问存在性、唯一性或自由度，就应该停在子空间/rank 层。

---

## 12. Cramer 的边界要和 fiber 模型连起来

当 $A$ 为方阵且 $\det A\ne0$ 时，所有 fiber 都是单点：

$$
\mathcal F_A(b)=\{A^{-1}b\}.
$$

Cramer 只是把这个单点的各坐标写成 determinant 比值。

若 $\det A=0$，真正发生的不是“方程组不能求”，而是单点模型失效，需要回到：

$$
\mathcal F_A(b)=
\begin{cases}
\varnothing, & b\notin\operatorname{Im}A,\\
 x_0+\ker A, & b\in\operatorname{Im}A.
\end{cases}
$$

所以遇到 Cramer 资格失败时的下一动作非常明确：**转回可达性 + kernel，而不是停止思考。**

---

## 13. First Divergence：矩阵方程先定位“方向”和“资格”

| 节点 | 应问的问题 | 偏离后的可观察症状 |
|---|---|---|
| M0 乘法方向 | 未知矩阵在左还是在右？ | 把 $A^{-1}$ 乘到错误一侧 |
| M1 存在性 | 对应列/行是否落在可达子空间？ | 一看到 $A$ 奇异就直接判无解 |
| M2 唯一性 | 相容后相应 kernel 是否为零？ | 把“有解”直接写成“唯一” |
| M3 自由度 | 每列/每行有多少独立 kernel 参数？ | 只给一个参数却漏掉其他列/行的独立自由度 |
| M4 Cramer 资格 | 是否方阵且 $\det A\ne0$？ | 在奇异或非方阵情形继续套分式 |
| M5 验证 | 是否乘回原式？ | 公式看似正确但左右次序错 |

---

## 14. 一页调用链

```text
矩阵方程
→ 先看未知矩阵在左还是右
→ AX=B：列空间问题
   → existence: Col(B)⊆Col(A)
   → unique: 再看 ker(A)=0
   → full solution: X=X0+Z, AZ=0
→ XA=B：行空间问题
   → existence: Row(B)⊆Row(A)
   → unique: 再看 ker(A^T)=0
   → 不便时转置成 A^T X^T=B^T
→ Cramer：先审计“方阵 + det A≠0”
   → 资格失败：回到 fiber / rank / kernel
→ 只问存在、唯一、自由度：到子空间或 rank 层即停
→ 最后把 X 乘回原方程
```

核心：

$$
\boxed{
\text{矩阵方程仍是 fiber 问题：右未知量看列空间，左未知量看行空间，自由度由对应 kernel 决定。}
}
$$
