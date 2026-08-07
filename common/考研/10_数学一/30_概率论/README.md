# 概率论与数理统计统一总图

> 工作标题：《概率论与数理统计：从随机世界到统计推断——随机对象、信息条件与分布变换的统一心智模型》
>
> 当前状态：Atlas 工作稿。本文先建立全书前 6--8 页所需的母模型；具体 Topic 尚未展开，考试动作另见[概率统计做题规则](../90_学科做题规则/概率统计.md)。

## Position

本 Atlas 回答三个问题：

1. 概率论与数理统计共同研究什么；
2. 事件、随机变量、分布、样本与统计量分别站在哪一层；
3. 各 Topic 怎样由同一组对象和操作生成。

概率论研究：随机机制已知时，数据会怎样生成；数理统计研究：随机机制未知而只看到有限样本时，数据能提供什么关于机制的信息。

$$
\boxed{\text{Probability}:\ \text{Model}\longrightarrow\text{Random Data}}
$$

$$
\boxed{\text{Statistics}:\ \text{Observed Data}\longrightarrow\text{Information about Model}}
$$

统计不是教材后半段突然出现的另一门课。它和概率论使用同一个生成模型，只是提问方向相反。

## Stop Boundary

本文只提供随机世界的地图，不展开：

- 组合计数、二重积分和变量代换的计算训练；
- 每一种常见分布的公式表；
- 每一类矩估计、最大似然估计、区间估计和检验的题型步骤；
- 考场时间分配、路径选择和得分表达。

前两类归具体 Topic 和专题训练，后两类归 Subject Rules。考试大纲每年的范围变化是外部约束，不参与定义本学科的母模型。

---

## 一、母模型不是单线阶梯，而是一张对象关系图

把全书压成

$$
\text{随机试验}\to\Omega\to\text{事件}\to\text{随机变量}
\to\text{分布}\to\text{联合分布}\to\text{数字特征}
$$

有导航价值，但不能把它当成严格的“对象升级链”。联合分布不是普通分布的更高版本，数字特征也不要求先经过联合分布。更准确的结构是：

$$
\boxed{(\Omega,\mathcal F,P)}
\xrightarrow{\text{选择观察函数}}
\boxed{X,\ (X,Y),\ T(X_1,\ldots,X_n)}
\xrightarrow{\text{诱导}}
\boxed{\text{Distribution}}
$$

分布建立以后，问题向不同方向分叉：

$$
\begin{aligned}
\text{Distribution}
&\xrightarrow{\text{Condition: 加入信息}}
\text{Conditional Distribution},\\
\text{Joint Distribution}
&\xrightarrow{\text{Marginalize: 忽略变量}}
\text{Marginal Distribution},\\
\text{Distribution of }X
&\xrightarrow{\text{Transform: 改变观察}}
\text{Distribution of }g(X),\\
\text{Distribution}
&\xrightarrow{\text{Summarize: 压缩}}
\text{Expectation / Variance / Other Features}.
\end{aligned}
$$

重复抽样又建立第二条轴：

$$
\text{Population Model}
\longrightarrow
(X_1,\ldots,X_n)
\longrightarrow
T(X_1,\ldots,X_n)
\longrightarrow
\text{Sampling Distribution}
\longrightarrow
\text{Inference}.
$$

因此，全书真正需要维护的是三层对象和两种方向：

| 层 | 核心对象 | 核心问题 |
|---|---|---|
| 随机世界 | $(\Omega,\mathcal F,P)$ | 哪些结果可能发生，哪些事件可讨论，概率怎样分配？ |
| 观察与分布 | $X,(X,Y),g(X,Y)$ 及其分布 | 我们观察什么，概率质量怎样被映射到取值空间？ |
| 样本与推断 | $X_1,\ldots,X_n,T,\theta$ | 有限随机样本能提供多少关于未知模型的信息？ |

正向是“模型生成数据”，反向是“数据约束模型”。

---

## 二、随机世界：先分清结果、事件与概率

### 1. 随机试验产生基本结果

样本空间 $\Omega$ 收集一次试验所有可能的基本结果。掷一次骰子时：

$$
\Omega=\{1,2,3,4,5,6\}.
$$

$\omega=3$ 是一次具体结果，不是事件的概率，也不是随机变量本身。

### 2. 事件是结果的集合

若关心“点数为偶数”，则

$$
A=\{2,4,6\}\subseteq\Omega.
$$

严格地说，可讨论的事件组成事件族 $\mathcal F$。数学一通常不要求从公理构造 $\sigma$-代数，但必须保留对象边界：

$$
\boxed{\omega\in\Omega,\qquad A\in\mathcal F,\qquad \omega\neq A.}
$$

### 3. 概率是定义在事件上的规则

概率测度 $P$ 把事件映射到 $[0,1]$：

$$
P:\mathcal F\to[0,1].
$$

所以 $P(A)$ 的问题是“事件 $A$ 发生的可能程度”，而不是“结果 $A$ 的数值是多少”。

这三类对象构成概率论的地基：

$$
\boxed{\text{Outcome}\neq\text{Event}\neq\text{Probability}.}
$$

---

## 三、随机变量：选择怎样观察随机世界

随机变量不只是“取值随机的变量”。它是在基本结果上定义的数值观察函数：

$$
\boxed{X:\Omega\to\mathbb R.}
$$

掷两枚硬币时：

$$
\Omega=\{HH,HT,TH,TT\},
$$

定义 $X$ 为正面个数，则

$$
HH\mapsto2,\qquad HT\mapsto1,\qquad TH\mapsto1,\qquad TT\mapsto0.
$$

随机性原本存在于未知的试验结果 $\omega$。$X$ 没有制造新的随机性，而是完成一次有目的的信息压缩：

$$
\boxed{\text{复杂随机结果}\xrightarrow{X}\text{当前问题关心的数值}.}
$$

同一个随机世界可以选择不同观察函数。例如同一次抛硬币序列可以观察：

- 第一次是否成功；
- 成功总数；
- 第一次成功出现的位置；
- 最长连续成功段长度。

题目改变随机变量，通常不是改变底层试验，而是改变“我们保留什么信息”。

### 随机向量不是另一种随机世界

二维随机变量 $(X,Y)$ 是在同一个 $\omega$ 上同时进行两种观察：

$$
(X,Y):\Omega\to\mathbb R^2.
$$

二维真正新增的不是“多了一个字母”，而是两个观察量之间的依赖结构：知道 $Y$ 后，对 $X$ 的不确定性是否改变？

---

## 四、分布：观察函数把概率结构推到取值空间

给定随机变量 $X$，原来位于 $\Omega$ 上的概率通过 $X$ 被推到数轴上。对数轴集合 $B$：

$$
P_X(B)=P(X\in B)=P\bigl(\{\omega:X(\omega)\in B\}\bigr).
$$

这就是 $X$ 的分布。它回答：

> 概率质量怎样落在 $X$ 的取值空间上？

分布函数

$$
F_X(x)=P(X\le x)
$$

是通用表示；离散型可进一步用概率质量函数，具有密度的连续型可用概率密度函数。三者不是三个并列的新对象，而是描述分布的不同表示。

必须保留两个边界：

1. 不是每个分布都有密度，但每个实随机变量都有分布函数；
2. 连续型随机变量的密度值 $f_X(x)$ 是概率强度，不是点概率，通常 $P(X=x)=0$。

因此：

$$
\boxed{\text{Random Variable}\neq\text{its realization}\neq\text{its distribution}.}
$$

$X$ 是抽样前的随机对象，$x$ 是一次观察值，$P_X$ 或 $F_X$ 描述 $X$ 的概率规律。

---

## 五、分布计算的三种基本操作

Condition、Marginalize 和 Transform 不是全书全部计算动作，却是处理“分布与信息”的三种基本动作。求和、取极值、构造统计量等通常都可以看成 Transform；求期望和方差则属于从分布提取 Summary。

### 1. Condition：加入信息，重述当前世界

从 $P(A)$ 变为 $P(A\mid B)$，不是给公式多放一个分母，而是已知 $B$ 发生后，只在与 $B$ 相容的世界中重新归一化概率：

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)},\qquad P(B)>0.
$$

直观上：

$$
\boxed{\Omega\xrightarrow{\text{know }B}B\text{ becomes the effective world}.}
$$

全概率公式沿“原因的完备划分”正向汇总结果；Bayes 公式则在观察到结果后，重新分配对不同原因的相对相信程度：

$$
\boxed{\text{Prior}\xrightarrow{\text{Evidence}}\text{Posterior}.}
$$

边界提醒：对连续型变量写 $X\mid Y=y$ 时，事件 $\{Y=y\}$ 往往概率为零，不能直接套事件条件概率分式。数学一范围内通常通过联合密度与边缘密度定义条件密度；直觉仍是“加入信息后重新描述分布”。

### 2. Marginalize：忘掉不再区分的信息

已知 $(X,Y)$ 的联合分布，只关心 $X$ 时，把所有与同一个 $X$ 相容的 $Y$ 情况加总：

$$
f_X(x)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dy.
$$

离散情形则是求和。其含义是：

$$
\boxed{\text{Joint World}\xrightarrow{\text{forget }Y}\text{Marginal World of }X.}
$$

积分上下限不是永远机械地写 $(-\infty,\infty)$。真正的计算对象是联合支撑集在固定 $x$ 截面上的允许 $y$ 范围。

### 3. Transform：改变观察函数

若 $Y=g(X)$，没有产生新的底层随机性，只是把观察函数从 $X$ 改成 $g\circ X$：

$$
\Omega\xrightarrow{X}\mathbb R\xrightarrow{g}\mathbb R.
$$

核心问题是概率质量怎样经过 $g$ 被搬运、合并或拉伸。对于 $Y=X^2$，$x$ 与 $-x$ 会落到同一个 $y$；若忽略多对一映射，机械的一元求导公式就会漏掉概率来源。

变量变换至少先问：

- 原变量支撑集是什么；
- 映射后的取值范围是什么；
- 映射是一对一还是多对一；
- 一个目标值有哪些原像；
- 是用 CDF、分区求和还是 Jacobian 更自然。

### 三种操作之间不能随意交换

先条件化再边缘化、先变换再条件化，可能得到不同对象。尤其是：

- 独立变量在给定它们的和后通常不再独立；
- 忽略一个共同原因，可能掩盖或改变可见依赖；
- 非单射变换会丢失原变量的符号等信息。

所以操作前必须同时写清“当前对象”和“保留的信息”。

---

## 六、多维世界的母模型：Joint → Marginal / Conditional → Dependence

联合分布回答“多个观察量一起怎样变化”；边缘分布回答“忽略其他量后，单独一个量怎样变化”；条件分布回答“知道一部分观察以后，剩余量怎样变化”。

依赖性则比较：信息加入前后，分布是否改变。

若 $X,Y$ 独立，则知道一个变量不会改变另一个变量的分布。在适当条件下可写为：

$$
f_{X,Y}(x,y)=f_X(x)f_Y(y),
$$

或

$$
f_{X\mid Y}(x\mid y)=f_X(x).
$$

“知道一个没有分布信息增益”是独立性的解释；乘积公式是可计算判据。

必须区分：

| 边界 | 真正区别 |
|---|---|
| 独立 vs 互斥 | 独立是不提供概率信息；互斥是不能同时发生。非零概率的互斥事件不独立。 |
| 独立 vs 不相关 | 独立是联合分布解耦；不相关只表示协方差为零，没有线性共同变化。 |
| 边缘 vs 条件 | 边缘是忘掉另一变量；条件是知道另一变量的信息后重述分布。 |

---

## 七、数字特征：有损压缩完整分布

完整分布可能很复杂，数字特征用少量数值压缩某些重要性质：

$$
\boxed{\text{Full Distribution}\longrightarrow\text{A few summaries}.}
$$

| 数字特征 | 回答的问题 | 不能回答什么 |
|---|---|---|
| $E[X]$ | 概率质量的加权中心在哪里？ | 不能单独描述波动和尾部 |
| $\operatorname{Var}(X)$ | 相对均值的平方偏离平均有多大？ | 不能唯一确定分布 |
| $\operatorname{Cov}(X,Y)$ | 两变量是否有线性共同变化趋势？ | 为零不能一般推出独立 |
| $\rho_{X,Y}$ | 无量纲的线性关联强弱与方向如何？ | 不能概括全部非线性依赖 |

“压缩”意味着信息会丢失。均值和方差相同的随机变量可以有完全不同的分布和尾部风险。

若只问 $E[g(X)]$，可以直接基于 $X$ 的分布求

$$
E[g(X)],
$$

并不必然先求 $Y=g(X)$ 的完整分布。这个机制事实属于本文；何时在题中优先选择该路径，属于 Subject Rules。

---

## 八、大量重复：稳定位置与剩余波动

从单个随机变量进入 $X_1,\ldots,X_n$ 后，问题不再只是“一个量怎样随机”，而是大量随机性叠加后是否出现稳定结构。

### 大数定律：稳定到哪里

在相应条件下，样本均值趋近总体均值：

$$
\bar X_n\to\mu.
$$

它解释大量重复为什么能把平均波动压低，核心是 Stability。

### 中心极限定理：怎样围绕那里波动

在相应条件下，标准化后的和或均值趋近正态分布：

$$
\frac{\bar X_n-\mu}{\sigma/\sqrt n}\Rightarrow N(0,1).
$$

它描述剩余 Fluctuation 的尺度与形状。

因此：

$$
\boxed{\text{LLN: where it settles}\qquad\text{CLT: how it fluctuates}.}
$$

边界提醒：“大量重复”本身不是充分条件。不同版本的大数定律和中心极限定理有各自的独立性、同分布、矩存在或其他条件；极限结论也必须区分依概率收敛、依分布收敛等类型。

---

## 九、从概率到统计：同一生成模型的逆向提问

设模型由未知参数 $\theta$ 控制：

$$
\theta\longrightarrow X_1,\ldots,X_n.
$$

概率论固定模型，研究随机样本会怎样变化；统计学观察

$$
X_1=x_1,\ldots,X_n=x_n
$$

以后，反问哪些 $\theta$ 与这些数据相容，以及数据支持它们到什么程度。

“统计是逆向概率推理”是有效导航，但不是说存在一个普通反函数。不同参数可能生成相似数据，有限样本也不可能唯一恢复真实机制。统计推断必须依靠模型假设、抽样分布和错误风险来校准结论。

### 统计对象分层

$$
\boxed{
\theta
\longrightarrow
(X_1,\ldots,X_n)
\longrightarrow
T(X_1,\ldots,X_n)
\longrightarrow
T(x_1,\ldots,x_n)
}
$$

| 对象 | 抽样前的身份 |
|---|---|
| 参数 $\theta$ | 在经典统计模型中固定但未知 |
| 随机样本 $X_1,\ldots,X_n$ | 来自总体模型的随机变量 |
| 统计量 $T(X_1,\ldots,X_n)$ | 不含未知参数的样本函数，抽样前仍随机 |
| 估计量 $\hat\theta$ | 专门用于估计 $\theta$ 的统计量 |
| 估计值 $\hat\theta(x_1,\ldots,x_n)$ | 代入已观察样本后的具体数值 |

因此：

$$
\boxed{\text{Parameter}\neq\text{Statistic},\qquad
\text{Estimator}\neq\text{Estimate}.}
$$

### 抽样分布是推断的标尺

统计量由随机样本构成，所以抽样前也有分布。正态总体下，$\bar X$、$S^2$、标准化均值和方差比自然产生 Normal、$\chi^2$、$t$、$F$ 等抽样分布。

这些分布不是突然出现的公式清单，而是回答：

> 如果重复抽样，同一个统计量会怎样波动？

只有知道这种波动，才能评价估计误差、构造置信区间或判断一个观察值是否过于极端。

### 三类统计任务

| 任务 | 母问题 |
|---|---|
| 构造点估计 | 用样本的哪个函数代表未知参数？ |
| 评价与区间估计 | 这个估计怎样波动，误差有多大？ |
| 假设检验 | 若 $H_0$ 成立，当前统计量是否极端到应拒绝它？ |

置信区间和检验都依赖抽样分布，但回答不同问题。在经典频率学派表述中，参数固定而未知，区间端点在抽样前是随机的；置信水平校准的是构造方法在重复抽样中的覆盖率，不是观测后参数再次随机落入该固定区间的概率。

检验不是“证明 $H_0$ 错”，而是在预先控制错误风险的规则下作决策。

---

## 十、两个长期母例

### 1. Bernoulli 序列：从事件走到统计推断

设一次试验成功概率为 $p$，令

$$
X_i=\begin{cases}
1,&\text{成功},\\
0,&\text{失败}.
\end{cases}
$$

则

$$
X_i\sim\operatorname{Bernoulli}(p),\qquad
S_n=\sum_{i=1}^nX_i\sim\operatorname{Binomial}(n,p),
$$

$$
E[S_n]=np,\qquad \operatorname{Var}(S_n)=np(1-p),
$$

$$
\bar X=\frac{S_n}{n}
$$

既是样本均值，也是成功比例。大数定律解释 $\bar X$ 为什么靠近 $p$，中心极限定理描述它围绕 $p$ 的近似波动；观察数据后，$\bar x$ 又可以用来估计 $p$。

该母例串联：

$$
\text{Event}\to\text{Random Variable}\to\text{Distribution}
\to\text{Sum}\to\text{Summary}\to\text{Limit}\to\text{Inference}.
$$

### 2. 正态总体：从统计量走到推断标尺

设

$$
X_1,\ldots,X_n\overset{\mathrm{iid}}{\sim}N(\mu,\sigma^2).
$$

该母例串联：

$$
\bar X,\quad S^2,\quad N,\quad\chi^2,\quad t,\quad F,
$$

以及 $\mu,\sigma^2$ 的点估计、区间估计和假设检验。

两个母例分工不同：Bernoulli 强调离散事件、重复试验和极限；Normal 强调连续分布、线性组合、抽样分布和推断。它们是导航例，不替代反例和其他分布。

---

## 十一、Topic 地图与规划 Ownership

| Part / Topic | 唯一母问题 | 规划 Owner |
|---|---|---|
| 0 随机世界 | 随机结果、事件与概率分别是什么对象？ | `01_随机世界_事件与概率/README.md` |
| I 信息改变概率 | 新信息怎样改变有效随机世界与概率分配？ | `02_条件概率_独立性与Bayes/README.md` |
| II 数值化随机性 | 观察函数怎样诱导分布？ | `03_随机变量与一维分布/README.md` |
| III 多维与变换 | 联合、边缘、条件与变量变换怎样重组信息？ | `04_联合分布_条件分布与变换/README.md` |
| IV 分布压缩 | 数字特征保留了什么，又丢失了什么？ | `05_数字特征与依赖摘要/README.md` |
| V 大量重复 | 大量随机量为何出现稳定位置与近似波动形状？ | `06_大数定律与中心极限定理/README.md` |
| VI 样本随机性 | 统计量为何随机，其抽样分布怎样产生？ | `07_总体样本与抽样分布/README.md` |
| VII 从样本反推总体 | 怎样构造、校准并使用统计推断？ | `08_参数估计与假设检验/README.md` |

当前只有 Atlas 建立工作态正文；Topic 文件均为规划归属，不把目录规划写成已经存在的 Owner。

## 十二、一页压缩：复原全书的七问

面对任一概率统计机制，先问：

1. 底层随机世界和概率模型是什么？
2. 当前观察对象是事件、随机变量、随机向量、样本还是统计量？
3. 它的分布由什么模型诱导？
4. 题目加入了什么信息，又忽略了什么信息？
5. 当前是在条件化、边缘化、变换、摘要，还是重复抽样？
6. 方向是模型生成数据，还是数据反推模型？
7. 结论依赖哪些条件，在哪个边界下会失效？

五句最小主干：

$$
\boxed{\text{事件是结果集合；随机变量是观察随机世界的数值函数。}}
$$

$$
\boxed{\text{分布是底层概率经观察函数诱导到取值空间的规律。}}
$$

$$
\boxed{\text{条件化加入信息，边缘化忽略信息，变量变换改变观察。}}
$$

$$
\boxed{\text{LLN 说明稳定位置，CLT 描述标准化后的剩余波动。}}
$$

$$
\boxed{\text{概率从模型推出数据；统计从数据提取关于模型的信息。}}
$$

## 待人确认的编辑决策

以下不是数学事实争议，而是本手册的长期表达选择：

1. 是否正式采用“随机世界 / 观察函数 / 信息操作”作为全书一级术语；
2. 是否保留“统计是逆向概率推理”，并始终附带“不是普通反函数”的边界；
3. 是否固定 Bernoulli 与 Normal 为两个长期母例；
4. 是否按当前八个 Topic 切分后续 30--40 页正文。

在人确认前，后续 Topic 不批量生成，避免让目录结构替代模型判断。
