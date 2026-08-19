# 《考研数学经典例子与反例精讲》Source Diff / Owner Diff

日期：2026-08-18  
Source：用户上传 Markdown《考研数学经典例子与反例精讲》，3446 行，48 个编号专题。  
状态：**48 个专题已完成第一轮 Owner / Correctness / Training 复审；高数与线代均已完成对应缺口更新，综合练习 23 题完成跨 Topic 回归路由。**

## 1. 本轮目标

本 Source 的价值不是补一份并行“反例大全”，而是为现有手册提供三类资产：

1. **特殊函数 Reference**：补当前主干中常见但未系统拥有的对象，如双曲/反双曲函数；
2. **Counterexample Unit Tests**：用最小反例压力测试已有蕴含链与资格门；
3. **Practice Pool**：把高价值选择题/判断题转成“触发信号 → 第一动作 → 边界”的训练证据。

采用四层去向：

- `Canonical Update`：改变或加厚稳定知识模型；
- `Practice Update`：主要用于训练调用/反例压力测试；
- `Covered / Evidence`：现有模型已拥有，仅增加来源证据，不重复写正文；
- `Correct / Reject / Route / Extension`：源表述需纠错、拒绝进入主干、转交其他 Owner，或仅保留扩展识别。

## 2. 逐专题路由

| # | Source 专题 | 状态 | 唯一 Owner / 去向 | 决策 |
|---|---|---|---|---|
| 01 | 符号函数 | Covered / Evidence | Topic01 基本函数结构；Topic02 连续；Topic03 导数定义 | `sgn` 已作为有界跳跃、单调不连续、差商伪装的最小对象；不复制专题正文 |
| 02 | 取整函数 | Covered / Evidence | Topic01 基本函数结构/单调/周期；Topic02；Topic05 | $\lfloor x\rfloor=x+O(1)$、阶梯间断、整数漂移已有 Owner；例题可继续作训练池 |
| 03 | 狄利克雷函数 | Covered / Evidence | Topic01；Topic02；H-B03 | 已拥有“有界但处处不连续、任意小有理周期、无最小正周期”等反例；$xD(x),x^2D(x)$ 可作连续/可导层级训练 |
| 04 | 绝对值及变形 | Covered / Practice | Topic03 导数定义与绝对值三结构；Topic04 极值 | $|x|$、$x|x|$、对称差商等是高价值最小反例；保留为压力测试，不再建立平行理论 |
| 05 | 处处连续但处处不可导 | Extension / Evidence | Topic03 正则性边界 | Weierstrass 例子用于阻断“连续函数大多可导”的直觉，但具体级数证明超出主干；只作存在性反例 |
| 06 | $x\sin(1/x)$ 型 | Covered / Practice | Topic02/03 | 已由 $|x|^p\sin(1/x)$ 正则性阶梯统一；具体例子继续用于最低阶训练 |
| 07 | 导函数不连续 | Covered / Practice | Topic03 导函数介值与极限边界 | $x^2\sin(1/x)$ 已是 Canonical 反例；可直接复用 |
| 08 | 点导数与邻域行为分离 | Covered / Practice | Topic03 / Topic04 | $x+x^2D(x)$ 可强化“点导数符号只给点两侧相对高低，不给邻域单调”；作为训练证据 |
| 09 | 有界函数反例 | Covered / Practice | Topic01 有界性；Topic04 MVT | 多数是“性质不封闭”的负例；只挑最小反例进入各 Owner，不建立列表式大全 |
| 10 | 奇偶/周期传播反例 | Covered / Evidence | H-B01 | 导数/原函数的奇偶与周期传播、积分常数、平均漂移已经系统拥有；Source 作为二次证据 |
| 11 | 反双曲正弦 | **Canonical + Practice Update / Corrected** | Topic01 + Topic03 + Topic05 | 补 $\sinh/\operatorname{arsinh}$ 对象—导数—积分接口；源稿导数公式错误，禁止原样迁移 |
| 12 | 反双曲余弦 | **Canonical + Practice Update** | Topic01 + Topic03 + Topic05 | 补 $\cosh/\operatorname{arcosh}$ 的非单射分支、端点无有限逆导数、根式积分接口 |
| 13 | 数列有界/收敛/单调 | Covered / Practice | Topic02 | 作为蕴含链反例池；现有数列极限/递推模型不需重写 |
| 14 | 两数列四则运算反例 | Covered / Practice | Topic02 | 训练“极限定理是正向带资格的封闭性，不是从结果反推部件” |
| 15 | $a_n$ 与 $f(a_n)$ | Covered / Practice | Topic02 数列极限结构转译 + Topic01 反函数 | 已有连续映射正向传递、逆函数连续的反向恢复边界 |
| 16 | 无穷小/无穷大/无界 | Covered / Practice | Topic02 | 强化“无界量 ≠ 无穷大量”“乘积结果不能反推因子状态”等边界 |
| 17 | 连续函数运算反例 | Covered / **Corrected** | Topic02 连续与间断 | 不连续量可抵消/压制已有模型；源中“两个连续函数的商可以不连续”的示例 $x/1$ 无效，真正资格是分母非零 |
| 18 | 导数定义反例 | Covered / Practice | Topic03 导数定义与分段点 | 对称差商、稀疏增量、$f(2x)-f(x)$ 等非常适合做“固定基点/覆盖全部 $h$”压力测试 |
| 19 | $|f|$ 可导推出 $f$ 可导的条件 | Practice Update candidate | Topic03 | 结论本身可由连续保号 + 零点极小值/差商推出；适合作为绝对值结构的综合训练，不需升格母模型 |
| 20 | $\lim f'$ 与 $f'(x_0)$ | Covered / **Corrected wording** | Topic03 | Source 开头“互相没有关系”过强；若两者都存在则必须相等。现有 Canonical 已正确处理 |
| 21 | 导数极限定理续 | Covered / Evidence | Topic03 + Topic04/H-B02 | 点连续 + 去心可导 + 导数极限存在的桥已完整拥有 |
| 22 | 导函数间断点 | Covered / **Corrected wording** | Topic03 + H-B03 | 真正定义在整个区间上的导函数无第一类/单向无穷间断，可有振荡；Source 后半例子目标点本身不可导，不能叫“导函数在该点的间断” |
| 23 | 极值反例上 | Covered / Practice | Topic04 函数形状 | 驻点非极值、不可导极值、局部/绝对最值边界均适合作反例单测 |
| 24 | 极值反例下 | Covered / Practice | Topic04 | “极值不要求整段左增右减”“连续接缝资格”等作为判定边界训练 |
| 25 | 拐点反例 | Covered / Practice | Topic04 | $f''=0$ 只是候选、不可导也可有拐点；应按凹凸定义/导数单调审计 |
| 26 | 多项式拐点个数 | **Corrected / Practice** | Topic04 函数形状 | Source 把“零点重数奇数且≥3 iff 拐点”泛化成定理是错误的；只能对具体多项式结合 $f''$ 符号/重数分析，不迁移该 iff |
| 27 | Rolle 条件反例 | Covered / Practice | Topic04 / H-B02 | 三个资格条件的不可删性与“充分非必要”非常适合作为定理资格压力测试 |
| 28 | L'Hospital 不能计算 | Covered / **Qualified** | Topic04 + Topic02 | 非未定式、导后极限不存在/变复杂/循环、数列直接套用等均可训练；所谓“广义洛必达”若无完整条件不进主干 |
| 29 | 连续/原函数/可积 | Covered / **Terminology corrected** | H-B03 | 现有资格网络已更完整；$1/x$ 在 $(0,1)$ 应明确为相应反常积分发散，而不是笼统写“不可积” |
| 30 | Gamma 函数 | Extension Update | Topic05 | 保留 $\Gamma(s)$、递推、整数/半整数识别为 Extension；不把反射公式等变成数学一默认前置 |
| 31 | 累次极限与二重极限 | Covered / Practice | Topic07 | 已明确“有限路径/累次极限不能证明联合极限”；Source 反例可直接做压力测试 |
| 32 | 偏导存在但不连续 | Covered / **Answer corrected** | Topic07 | $xy/(x^2+y^2)$ 已是 Canonical 例；Source 该选择题答案标 B 错，应为“偏导存在、不连续”的选项 C |
| 33 | 连续但偏导不存在 | Covered / **Definition qualified** | Topic07 | $|x|+|y|$、$\sqrt{x^2+y^2}$ 可用；“方向导数都不存在”必须先声明双侧 $t\to0$ 还是射线 $t\to0^+$ 定义 |
| 34 | 可微但偏导函数不连续 | Covered / Practice | Topic07 | 正好阻断“可微 ⇒ 一阶偏导邻域连续”，现有关系网已拥有 |
| 35 | 连续 + 偏导存在但不可微 | Covered / Practice | Topic07 | $xy/\sqrt{x^2+y^2}$ 适合训练“轴向探针 ≠ 统一线性余项” |
| 36 | 数项级数一般反例 | Covered / Practice | Topic10 | 通项归零非充分、部分和有界非收敛等应作为尾部模型的单元测试 |
| 37 | 收敛级数变形 | Covered / Practice | Topic10 | 条件收敛对绝对值、取子列、非线性变形不封闭；用于运算资格压力测试 |
| 38 | 条件/绝对收敛运算 | Covered / Practice | Topic10 | 强化“绝对收敛提供稳定运算，条件收敛依赖抵消”的母模型 |
| 39 | 矩阵运算反例 | Covered / **Practice Update** | 线代 Topic02 + Topic03 | 非交换、零因子、消去律已有 Owner；补“标量恒等式迁移到矩阵必须审计交换性”，统一 $(A+B)^2$、平方差、$(AB)^k$ |
| 40 | 行列式反例 | Covered / Qualified | 线代 Topic02 | 整矩阵多线性、$\det(kA)=k^n\det A$、奇异非零、反对称奇数阶均已有；分块“类二阶公式”拒绝，保留块三角与 Schur 补资格 |
| 41 | 对称矩阵反例 | **Practice Update / Corrected** | 线代 Topic02 + Topic05 | 补 $\operatorname{adj}(A)$ 对称性的正向与可逆反推边界；源稿把 $\operatorname{adj}(A)$ 与 $A^{-1}$ 的比例写反。对称矩阵乘积改写为“$AB$ 对称 iff $AB=BA$” |
| 42 | 相似/合同/等价 | Covered / **Practice Update** | 线代 Topic03/05/06 | 精化为“相似⇒等价、合同⇒等价；一般相似与合同互不推出；实对称场景相似⇒正交相似⇒合同”，不再用无条件强弱链 |
| 43 | 对合/幂等/幂零 | **Practice Update** | 线代 Topic05 | 新增 `特殊矩阵的多项式约束.md`；把特殊矩阵统一成 $p(A)=0$，并将加乘闭包归结为交换性/交叉项是否消失 |
| 44 | 其他矩阵反例 | Covered / **Practice Update** | 线代 Topic01/02/05/06 | 逆/转置逆序、正交 det 必要非充分、同特征多项式非相似已有；新增正定和/差/积边界及 $A\sim_c -A$ 的偶数阶必要条件 + 惯性反例 |
| 45 | 线性相关性反例 | **Canonical + Practice Update / Qualified** | 线代 Topic01 | 已有表示/相关性模型，新增“合并无关组看 span 交”“批量线性组合看系数矩阵”；零向量组是否有极大无关组依空集约定，不作为普遍反例；行/列向量组不同维时“等价”本身不具类型资格 |
| 46 | 线性相关经典结论 | **Canonical + Practice Update** | 线代 Topic01 | 不背奇偶结论；升级为 $B=AC$ 的系数矩阵 kernel 模型。循环相邻和由 $k_{i-1}+k_i=0$ 直接得到奇数无关、偶数相关 |
| 47 | 函数/导数/积分均值极限 | Practice Update / **Proof corrected** | Topic02 + Topic04 + Topic05/H-B03 | 适合做“信息能否反向恢复”的综合反例；Source 对 Cesàro 积分平均的证明段落错接成了导数极限论证，应重证 |
| 48 | 综合练习 | **Validation Completed (23/23 routed)** | 各 Topic Practice | 不进入 Canonical；23 题逐题完成 Owner/机制路由，答案键未发现新的实质错误；第 1 题凹凸术语按本库定义口径使用，不以术语字面代替二阶/割线判据 |

## 3. 本轮已经落地的更新

### Topic01：新增双曲函数对象 Owner

新增 Practice：

`10_数学一/10_高等数学/01_函数对象_表示与结构/双曲函数与反双曲函数.md`

母模型不是“像三角函数的一组新公式”，而是

$$
\boxed{
\cosh x=\frac{e^x+e^{-x}}2,
\qquad
\sinh x=\frac{e^x-e^{-x}}2
}
$$

即指数函数的偶部/奇部。由此生成奇偶、$\cosh^2-\sinh^2=1$、值域、单射与反函数分支。Canonical 只保存对象级骨架，完整训练留在 Practice。

### Topic03：双曲导数与有限 Taylor 接入原有“局部增益”模型

不新增求导法则：

- $\sinh,\cosh$ 从 $e^{\pm x}$ 求导；
- $\tanh$ 从商法则；
- $\operatorname{arsinh},\operatorname{arcosh},\operatorname{artanh}$ 从逆函数增益取倒数；
- 有限 Taylor 从 $e^x,e^{-x}$ 的奇偶分解、商与反函数导数重建。

特别保留

$$
\operatorname{arcosh}(1+h)\sim\sqrt{2h}
$$

作为“反函数存在但端点没有有限逆导数/普通整数幂 Taylor”的边界对象。

### Topic05：特殊原函数与 Gamma Extension

新增 Practice：

`10_数学一/10_高等数学/05_一元累积_原函数定积分与反常积分/双曲型根式与特殊原函数.md`

把

$$
\int\frac{dx}{\sqrt{x^2+a^2}},\qquad
\int\frac{dx}{\sqrt{x^2-a^2}},\qquad
\int\frac{dx}{a^2-x^2}
$$

分别接到 $\operatorname{arsinh}$、正分支 $\operatorname{arcosh}$、中间分支 $\operatorname{artanh}$，并解释何时改用带绝对值的对数闭式覆盖其他连通分支。

Gamma 只保留为 Extension：先完成反常积分判敛与尺度归一，再在标准核已经暴露时用 $\Gamma$ 压缩，不作为默认技巧。

## 4. Source 纠错清单

以下内容不得以 Source 原表述进入 Canonical：

1. **反双曲正弦导数错误**：$\ln(x+\sqrt{1+x^2})$ 的导数应为 $1/\sqrt{1+x^2}$，不是 $\sqrt{1+x^2}$。
2. **连续函数商的反例无效**：$x/1=x$ 连续；正确边界是分母在目标点/邻域非零。
3. **“$\lim f'$ 与 $f'(x_0)$ 互相没有关系”过强**：若二者都存在，则由导数极限定理/中值定理桥必须相等。
4. **导函数间断例的对象混淆**：若 $f$ 在目标点本身不可导，就不能把去心邻域的 $f'$ 叫作“定义在该点的导函数发生某型间断”。
5. **多项式零点重数与拐点 iff 错误泛化**：零点重数本身不足以给一般多项式的拐点充要判据，必须检查二阶主部/凹凸符号。
6. **广义 L'Hospital 条件省略**：只写“分母趋无穷即可”不足以授权使用，主干不采用这种简写。
7. **$(0,1)$ 上 $1/x$ 的“不可积”口径不清**：应明确相应反常积分发散；不要与闭区间 Riemann 可积性混写。
8. **多元偏导例答案错误**：$xy/(x^2+y^2)$ 在原点两个偏导存在但不连续，源答案标错。
9. **方向导数口径缺失**：$\sqrt{x^2+y^2}$ 是否“所有方向导数存在”依赖采用双侧向量定义还是 $t\to0^+$ 射线定义。
10. **积分均值结论的证明错接**：$f(x)\to L\Rightarrow x^{-1}\int_0^x f\to L$ 应用积分平均/Cesàro 论证，Source 所列证明实际在讨论导数极限。
11. **伴随矩阵与逆矩阵的比例写反**：可逆时正确关系是 $\operatorname{adj}(A)=(\det A)A^{-1}$；Source 在“伴随对称反推原矩阵”处写成了倒数比例。结论可以保留，但证明必须纠正。
12. **分块 determinant 不能类比二阶标量 determinant**：$\det\begin{psmallmatrix}A&B\\C&D\end{psmallmatrix}$ 一般不能写成 $\det A\det D-\det B\det C$。块三角可直接读对角块；一般情形若主块可逆，应使用 Schur 补等带资格公式。
13. **相似/合同/等价不能排成普遍强弱链**：相似与合同都能推出同型矩阵等价，但一般相似与合同彼此不能推出；“实对称且相似”是可升级为正交相似/合同的特殊场景。
14. **只含零向量的向量组是否“没有极大无关组”依定义约定**：若允许空集作为线性无关子组，则空集就是其极大无关组。该说法不作为普遍反例进入 Canonical。
15. **行向量组与列向量组的“等价”存在类型问题**：它们常位于不同维空间；本库的向量组等价定义比较同一环境空间中的 span，因此不同环境时应先说“不具同一等价关系的比较资格”，而不是简单写“同 rank 但不等价”。
16. **循环相邻和的奇偶结论不作为孤立口诀**：Source 的结论正确，但更稳定的 Owner 是 $B=AC$ 的系数矩阵模型；原组无关时 $\ker B=\ker C$，循环例只是其一个可手算 kernel 实例。

## 5. 反例如何真正进入心智模型

本 Source 最值得保留的不是反例数量，而是下面这条测试链：

$$
\boxed{
\text{拟议蕴含}
\to
\text{最小反例}
\to
\text{定位失效资格}
\to
\text{修正 Canonical 边界}
\to
\text{做成 Practice 压力测试}
}
$$

例如：

- “连续 $\Rightarrow$ 可导”用 $|x|$，缺的是统一一阶线性主部；
- “点上 $f'(a)>0\Rightarrow$ 邻域单调增”用稠密扰动，缺的是邻域可导/导数符号控制；
- “偏导存在 $\Rightarrow$ 连续/可微”用 $xy/(x^2+y^2)$，缺的是所有路径统一控制；
- “通项趋零 $\Rightarrow$ 级数收敛”用调和级数，缺的是部分和尾部 Cauchy 稳定；
- “Riemann 可积 $\Rightarrow$ 有原函数”用跳跃函数，缺的是导函数 Darboux 介值性。

因此反例库应成为各模型的 **unit test suite**，而不是第五种独立知识产品。

## 6. 线性代数 39--46 的模型级更新

### 6.1 Topic01：从“某几道相关性反例”升级为系数矩阵模型

若原无关组按列排成

$$
A=(\alpha_1,\ldots,\alpha_m),
$$

新向量组由固定线性组合产生：

$$
B=(\beta_1,\ldots,\beta_k)=AC,
$$

则

$$
Bx=0\iff A(Cx)=0\iff Cx=0,
$$

从而

$$
\boxed{\ker B=\ker C,\qquad r(B)=r(C).}
$$

这使 Source 第 45--46 节中的“两两无关不等于整组无关”“两个无关组合并后可能相关”“循环相邻和奇偶性”等都能挂回 span / kernel / coefficient matrix，而不是形成反例清单。

### 6.2 Topic02：标量代数公式迁移到矩阵时统一做“交换审计”

Source 第 39、44 节大量负例可以压缩成一个动作：先按原顺序展开，只有真正需要把 $BA$ 换成 $AB$ 时才询问 $AB=BA$。因此

$$
(A+B)^2=A^2+AB+BA+B^2,
$$

$$
A^2-B^2=(A+B)(A-B)\iff AB=BA,
$$

以及 $(AB)^k=A^kB^k$ 的稳定资格，都由同一个非交换模型生成。逆与转置的顺序反转则是“撤销/反向读取复合”的另一机制，不与交换性混为一谈。

### 6.3 Topic05：特殊矩阵统一读成低次多项式约束

新增 Practice `特殊矩阵的多项式约束.md`。对合、幂等、幂零不再按名字记闭包，而先写

$$
p(A)=0.
$$

再问谱、可对角化和运算后的交叉项：

- 对合 $A,B$ 的积仍对合 iff $AB=BA$；
- 幂等 $A,B$ 的和仍幂等 iff $AB=BA=0$；
- 幂零 $A,B$ 可交换时，$A+B$ 与 $AB$ 仍幂零；无交换资格时均可失败；
- 实对称再叠加 $A^2=0$ 时，由正交谱定理立刻得到 $A=0$。

### 6.4 Topic06：变换关系与正定运算改成“不变量 + 对象资格”

相似/合同/等价按各自对象分流：等价看 rank，相似看算子谱结构，实对称合同看惯性。正定矩阵的和由二次型值相加直接保持正定；差不保持；普通乘积若不交换甚至可能不再对称，因此不能直接套本册的正定对象定义。$A$ 与 $-A$ 合同的偶数阶条件只由 determinant 给必要条件，最终仍由惯性决定。

## 7. 综合练习 23 题回归验证

第 48 节不作为新的知识 Owner，而作为跨 Topic regression suite。逐题路由如下：

| 题号 | Owner | 主要压力测试 | 结果 |
|---|---|---|---|
| 1 | Topic04 函数形状 | 凹凸与割线斜率单调的等价读法 | Pass；“凹/凸”名称按本库符号约定解释 |
| 2 | Topic04 + Topic05 | FTC 后用首个非零局部项判极值/拐点 | Pass |
| 3 | Topic02 + Topic05 | 函数极限、导数极限与积分 Cesàro 平均不能随意反推 | Pass |
| 4 | Topic10 | 两个收敛一般项级数间的点态大小不控制绝对收敛关系 | Pass |
| 5 | Topic10 | 单调有界数列进入 telescoping 级数 | Pass |
| 6 | 线代 Topic01 | 三个循环差向量的系数矩阵有非零 kernel | Pass |
| 7 | Topic03 | 对称差商存在不等于固定基点差商存在 | Pass |
| 8 | H-B01 | 原函数奇偶传播、积分常数与周期漂移 | Pass |
| 9 | Topic10 | $na_n\to\lambda>0$ 与调和尺度比较 | Pass |
| 10 | Topic03 / Topic04 | $f'(0)>0$ 只给足够小单侧函数值序，不给整邻域单调 | Pass |
| 11 | 线代 Topic01 | 整组无关 iff 每个向量都不在其余向量 span 中 | Pass |
| 12 | Topic10 | $n^{-1/2}$ 主导有界振荡的 $n^{-2}$ 项 | Pass |
| 13 | Topic07 | 偏导存在与连续互不构成充分/必要关系 | Pass |
| 14 | 线代 Topic01 | 四个循环组合直接转系数矩阵 rank/kernel | Pass |
| 15 | H-B01 | 奇函数的任一原函数为偶函数；其他方向需常数/平均值资格 | Pass |
| 16 | Topic10 | 收敛级数做有限线性移位组合的稳定性 | Pass |
| 17 | Topic04 | 有界函数 + 导数极限存在迫使导数极限为 0 | Pass |
| 18 | Topic04 | $f'\to+\infty$ 给最终正增长并推出 $f\to+\infty$ | Pass |
| 19 | H-B01 | 变上限积分的奇偶由 integrand 奇偶反转 | Pass |
| 20 | Topic10 | 正项总和发散 + 交错和收敛时，奇偶子和都发散但差收敛 | Pass |
| 21 | Topic04 | 有界导数在有界开区间上给 Lipschitz 型函数有界 | Pass |
| 22 | Topic10 | 原顺序相邻分组保持收敛；反向不能由分组收敛恢复原级数 | Pass |
| 23 | H-B01 | 奇函数 $f$ 与偶函数 $f'$ 经过复合/积分后的奇偶传播 | Pass |

本轮未发现第 48 节答案键新的实质错误。第 1 题的“凹函数”术语在不同教材中存在上凸/下凸命名差异，因此只按割线斜率/二阶导符号判据验收，不把中文术语字面当证据。

## 8. 当前完成状态与仍待验证的层级

Source 层面现在可以声明：

- 48 个编号专题均已完成第一轮 Correctness / Owner / Training 路由；
- 39--46 的线性代数内容已不再只是 Route，而是完成现有 Owner 对照与真实缺口更新；
- 第 48 节 23 道综合题已全部作为跨 Topic 回归测试完成路由；
- 真正错误、缺条件或定义口径敏感的 Source 表述已在本底账显式隔离。

但这仍不等于所有 Handbook 已“教学完成”。尚待的是更高一层的**人工审阅与持续陌生题采用验证**：某个模型在更多新题上若检索困难，再按证据补 Practice；不为了 Source 覆盖数量预先制造重复反例文件。

因此当前准确状态是：

$$
\boxed{\text{Source-level first review complete}\quad\neq\quad\text{all manuals pedagogically frozen}.}
$$
