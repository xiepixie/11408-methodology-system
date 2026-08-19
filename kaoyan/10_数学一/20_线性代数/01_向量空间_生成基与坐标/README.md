# 向量空间：生成、基与坐标

> 状态：整体逻辑重构已通过结构验收（2026-08-19）：Canonical 已改为“对象底座 → 三分支 → Basis 汇合 → Dimension/Coordinates 分叉 + 可选内积升级”，训练层已拆分 Core / Cross-topic Integration。现有 Published PDF 尚未同步本轮重构，发布前需用当前 LaTeX 重建。

## 为什么值得读

“这组向量能生成整个空间”和“这组向量能唯一表示每个对象”不是一回事。

只要求生成，你可以不断加向量；但一旦出现冗余，同一个对象就会有多套系数表示。基的意义，就是同时解决两个问题：**不遗漏 + 不重复**。

## 两个母问题与整体结构

> **母问题 A：怎样既覆盖目标空间，又消除表示冗余，使每个对象都有唯一编码？**
>
> **母问题 B：已经有唯一表示以后，如果还需要长度、角度、投影与方向解耦，怎样在不改变原 span 的前提下升级方向系统？**

Topic01 的第一部分不是单链，而是从“允许线性组合”分出三类问题：

```text
Vector Space
└─ Linear Combination
   ├─ 能到哪里？        → Span ───────────┐
   ├─ 有没有冗余？      → Independence ───┼→ Basis
   └─ 集合是否保持封闭？→ Subspace        │
                                          ├→ Dimension
                                          └→ Coordinates → Change of Basis
```

其中 `Span → Basis` 与 `Independence → Basis` 表示条件汇合；`Basis → Dimension` 和 `Basis → Coordinates` 是并行结果，不是“先有维数才有坐标”。

若任务还需要欧氏几何能力，再进入第二母问题：

```text
Vector Space
→ 增加 inner product
→ length / angle / orthogonality / projection
→ Gram-Schmidt（保持 span）
→ orthogonal basis
→ normalize
→ orthonormal basis / orthogonal matrix
```

这里“增加 inner product”是结构升级，不是从向量空间公理自动推出。

## 本册覆盖到哪里

本 Topic 负责：

- 线性组合、span、线性相关/无关；
- 极大线性无关组与向量组等价；
- 向量空间、子空间、基与维数；
- 坐标与换基；
- 内积、正交、投影；
- Gram-Schmidt 正交化与正交矩阵的基础性质。

本 Topic 不负责：

- 矩阵/线性映射 rank 的统一机制；
- kernel/image 的完整结构；
- 特征向量与对角化；
- 二次型主轴与惯性。

这些内容分别由 Topic03、Topic05、Topic06 接管。

## 训练导航：先 Core，再 Cross-topic Integration

### Core Training：只建立 Topic01 自己拥有的控制能力

- [线性表示与相关性判定](线性表示与相关性判定.md) 的 **Core 部分** —— 用 span、零组合、非零系数与生成骨架判断表示、冗余、替换与向量组等价；
- [基与坐标变换](基与坐标变换.md) —— 坐标求解、过渡矩阵列语义、新旧基方向、连续换基与“基矩阵 × 坐标”反向重构；
- [正交化与正交矩阵](正交化与正交矩阵.md) —— Schmidt 的 span 保持、规范正交基、正交矩阵与内积保持；determinant 仅保留为 Topic02 已学后的 Integration Check；
- [子空间求和、求交与维数](子空间求和求交与维数.md) —— Core-first：子空间判定、和/交、表示选择、维数公式与直和唯一性；rank/kernel 只作为 Topic03 已学后的计算压缩。

### Cross-topic Integration Training：在 Topic01 对象上调用后续工具

- [线性表示与相关性判定](线性表示与相关性判定.md) 的 **Integration 部分** —— 用 rank、kernel、determinant 与参数分类压缩 Core 判断；这些工具的统一机制分别回 Topic02/03；
- [向量关系与线性无关证明](向量关系与线性无关证明.md) —— 统一为“设零组合 → 制造零项 → 缩短关系 → 回代”，并调用矩阵作用、rank-nullity、特征结构与正交条件；对应完整理论分别 Bridge 到 Topic02/03/05。

因此训练顺序与 Canonical Owner 分开：**Topic01 可以先独立建立；考研综合训练再调用后续 Topic 的工具回头压缩它。**

## 第三章清稿覆盖路由

上传清稿中的相关内容不按原章节顺序机械复制，而按 Canonical Owner 分流：

| 清稿内容 | 本系统归属 | 训练入口 |
|---|---|---|
| 知识点 1：向量、线性组合、span 与基本运算 | Topic01 Canonical Own | [Canonical LaTeX](向量空间_生成基与坐标.tex) |
| 知识点 2--5：相关/无关、线性表示、极大无关组、向量组等价 | Topic01 Own | [线性表示与相关性判定](线性表示与相关性判定.md) |
| 专题 13：线性相关、线性表示、非零系数、组间表示与 rank 关系 | Topic01 Own | [线性表示与相关性判定](线性表示与相关性判定.md) |
| 专题 14：$AB=0$、$AB=C$、$AB=E$、矩形满行/满列秩与消去 | Topic02 Use + Topic03 Own 乘积 rank | [矩阵乘法方向与初等变换](../02_线性映射_矩阵与行列式/矩阵乘法方向与初等变换.md)；[秩的结构判断与乘积边界](../03_秩_基本子空间与等价/秩的结构判断与乘积边界.md)；伴随矩阵 rank 回 Topic03 Canonical，特征值接口回 Topic05 |
| 专题 15：表示三分、参数等价、极大无关组大题 | Topic01 Own | [线性表示与相关性判定](线性表示与相关性判定.md) |
| 专题 16：向量证明题 | Topic01 Own 证明控制；Topic03/05 Bridge | [向量关系与线性无关证明](向量关系与线性无关证明.md)；kernel 维数回 Topic03，特征值定理回 Topic05 |

这张表的作用是防止“内容没写在 Topic01 就等于遗漏”：跨 Topic 的理论只保留接口和调用信号，完整机制仍由它的 Canonical Owner 负责。

## 新内容以后怎样长进来

新增定义、题型、证明或例题时，不按“看到向量就塞进 Topic01”处理，而按下面的增长协议判断：

1. 先问它是否改变母问题“覆盖 + 唯一坐标”。若会改变母模型，先回到 Subject Atlas 与 Canonical 重新审计，而不是直接追加章节。
2. 若不改变母模型，先判定 `Own / Use / Bridge`。span、相关/无关、基、坐标与正交本体由 Topic01 Own；矩阵作用、rank/kernel、特征结构分别回 Topic02/03/05。
3. 稳定定义、机制、不变量与概念边界进入 Canonical；只依赖 Topic01 本体的题面控制进入 Core Training；调用 rank/kernel、矩阵作用或特征结构的题面控制进入 Cross-topic Integration。
4. 新例题若只复用已有机制，不为了“覆盖数量”重复抄入 Canonical；只有它暴露新的分支、边界或失败模式时，才升级知识模型。
5. 一旦跨 Topic，先更新本 README 的覆盖路由，再由 Canonical Owner 接收完整机制，Topic01 只保留调用接口。

这样，新材料可以继续增长，而不会破坏“一条规则只有一个 Canonical Owner”的结构。

## 最终验收记录

| 测试 | 结果 | 依据 |
|---|---|---|
| Compression | 通过 | Canonical 压成“线性组合三分支 + Span/Independence 汇合成 Basis + Basis 分叉到 Dimension/Coordinates + 可选内积升级”，不再伪装成单链 |
| Generation | 通过 | 从“可达性 / 冗余性 / 封闭性”生成 span、无关与子空间；Span + Independence 汇合为 Basis；几何需求独立生成内积分支 |
| Mapping | 通过 | README 明确 Topic01 Own 范围、Core/Integration 学习阶段、清稿专题 13--16 路由与 Topic02/03/05/06/B00 接口 |
| Boundary | 通过 | Canonical 有完整概念边界表；训练稿继续补充“整组相关不等于末向量可表示”“同 rank 不等于同 span”等操作边界 |
| Lifecycle / Trajectory | 通过 | 本 Topic 使用结构依赖图而非伪时间链：对象底座 → 三分支 → Basis 汇合 → Dimension/Coordinates 分叉；内积是可选结构升级 |
| Cost | 通过 | Canonical 明确“先用满足目标的最弱结构”，并说明求全表示、换基、Schmidt、单位化各自新增的计算义务 |
| Exam | 通过 | Core 与 Integration 训练分层；各正式训练入口均保留题面信号、第一动作、停止条件与独立检查 |
| Growth | 通过 | 本节增长协议规定新内容如何在 Canonical、Core Training、Integration Training 与跨 Topic Bridge 之间分流 |

当前结论：**Topic01 的知识模型、数学依赖顺序、训练阶段与清稿覆盖路由已按分叉结构重新验收。**

## 与其他册怎样连接

- 上位地图：[线性代数 Subject Atlas](../README.md)
- 下一册：[线性映射、矩阵与行列式](../02_线性映射_矩阵与行列式/README.md)
- rank 接口：[秩、基本子空间与等价](../03_秩_基本子空间与等价/README.md)
- 跨学科正交/投影接口：[B00｜内积、正交与投影](../../50_桥梁专题/B00_内积正交与投影/README.md)

## 正文与发布

- Canonical LaTeX：[向量空间_生成基与坐标.tex](向量空间_生成基与坐标.tex)
- Published PDF：[向量空间_生成基与坐标.pdf](../../../90_publish/math1/向量空间_生成基与坐标.pdf)
