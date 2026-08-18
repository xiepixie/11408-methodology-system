# 数项级数：尾部与敛散

> 状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## Hook

看到 `\sum u_n`，第一动作是问“部分和是否稳定、通项是否归零”，再选择比较尺度或抵消判别；不要把判别法当成互换的公式清单。

## Mother Question

无限项相加何时能由有限部分稳定逼近，尾项误差如何控制，哪些运算会因条件收敛而失效？

主线：

$$
\boxed{\text{部分和}\to\text{必要衰减}\to\text{基准尺度}\to\text{绝对/抵消}\to\text{尾项控制}\to\text{运算审计}}
$$

## Scope / Stop Boundary

本册负责部分和与 Cauchy 尾部准则、通项必要条件、正项基准级数、比较/等价比较、比值/根值、积分判别、Leibniz、Dirichlet、Abel、绝对/条件收敛、尾项误差和级数运算资格。

- Topic05 提供反常积分截断与无穷端点语言；
- Topic11 接管幂级数收敛域、Taylor 展开、逐项微积分与 Fourier 接口；
- Topic12 接管用级数/递推构造常微分方程解；
- Euler--Maclaurin、Stirling、生成函数为 Extension/Bridge，不在此承担主线；
- 单一级数问题族的题目触发信号、第一动作、检查点与停止条件由同目录训练 Markdown 维护；跨多个训练专题稳定复用并经证据验证的控制才晋升《高等数学做题规则》。

## Owns / Uses

- **Owns**：数项级数的收敛层级、判别分流、抵消机制、尾项估计和重排/运算边界。
- **Uses**：Topic05 的反常积分比较与极限；Topic11 的幂级数接口。

## 训练导航

- [级数判敛路线](级数判敛路线.md) —— 通项必要条件、正项尺度、绝对/条件收敛分流、判别法失效换路与旧口诀错误阻断。

## Read Next

1. [Topic05｜一元累积](../05_一元累积_原函数定积分与反常积分/README.md)
2. [Topic11｜函数展开](../11_函数展开_幂级数Taylor与Fourier/README.md)
3. [高等数学做题规则](../../90_学科做题规则/高等数学.md)

## Manual

- Canonical Source：[数项级数_尾部与敛散.tex](数项级数_尾部与敛散.tex)
- Published View：[数项级数_尾部与敛散.pdf](../../../90_publish/math1/数项级数_尾部与敛散.pdf)

## Status

归档笔记 II-09 已完成第一轮 Owner/Source Diff；正文与同目录训练文档仍需人工审阅和陌生题验证；跨专题候选规则继续按证据晋升流程处理，当前不标记为“已采用”。
