# 数学一 B00 至 B07 Cross-Subject Source Diff

日期：2026-08-11

## Source Pack

高数侧复核：`II-00` 空间对象、`II-01` 多元微分、`II-02/II-02.1` 隐函数与梯度、`II-03/II-03.1` 多元与二次型极值、`II-04/II-04.1` 重积分换元，以及一元/多元积分正文。线代和概率侧只读取对应 Canonical Topic 的接口，不搬运第二份本体定义。

## Owner Decisions

- B00 拥有内积、正交、投影在几何/线代/函数表示间的翻译，不拥有 Gram--Schmidt 或 Fourier 收敛。
- B01 拥有“可微即唯一最佳局部线性映射”，不拥有偏导判定细节或矩阵本体。
- B02 拥有 Jacobian matrix 到 determinant 局部体积因子的翻译，不拥有重积分换元算法或行列式计算法。
- B03 拥有 Hessian 二阶项到二次型符号结构的翻译，不拥有多元极值完整分类或合同理论。
- B04 拥有切空间、法空间与 Lagrange 乘子之间的正交接口，不拥有边界枚举算法。
- B06A/B06B 拥有 FTC 与概率质量累积、边缘化的接口，不重写概率分布与期望本体。
- B07 拥有概率质量守恒、support 迁移与 inverse Jacobian 的组合，不重写一般换元定理。

## Classification

上述项目均为 `Canonical Update`。来源中的考试动作另写入 Subject Rules；Hilbert space、一般流形、KKT、Radon--Nikodym 与一般多分支映射保留为 Extension，不进入数学一主干。
