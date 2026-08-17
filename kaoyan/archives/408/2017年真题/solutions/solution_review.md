# 2017 年 408｜Solution Review

> 目的：记录本年度题解生成过程中发现的 Source / Legacy / Model / Rules 证据。正式题解保持干净；只有经过跨题、跨年验证的稳定模式才允许晋升 Handbook / Rules。

## 1. Coverage / Format Gate

- Q1～Q47：47/47 已生成 `model-grounded-v1`。
- Q1～Q40：全部包含 `Model Anchor / 解题链 / 选项判断 / Verification / Compression / 易错边界`。
- Q41～Q47：全部包含 `Model Anchor / Problem Representation / Decision Points / Solution Chain / Verification / Compression / 易错边界`。
- 每题 Model Anchor 均显式包含 `Topic / 题目信号 / 第一动作`。
- 选择题答案与年度 legacy answer map 一致；综合题分值与 `exam.json` 的 `15/8/13/10/7/8/9` 一致，总分 70。
- Canonical Source Q1～Q47 连续完整；本年正式题面引用的 SVG 均存在。

## 2. Source Review

### No Canonical Rewrite Required

本轮逐题对照 Canonical Source、图形资产与 legacy 解析，没有发现需要修改 2017 正式题意的硬冲突。正式 Source 可继续作为唯一题面 Owner。

### Routing Correction

Q11 是排序/堆相关数据结构题，按共享 `408.json` Profile 属于 Q1～Q11 数据结构区间；legacy 文件仍名为 `q11_计算机组成原理.md`。年度索引已把 Q11 归回数据结构，旧文件名仅保留兼容，不拥有学科路由权。

## 3. Legacy Solution Corrections / Clarifications

### Q41｜函数名与真实遍历机制不一致

旧解析把核心函数命名为 `preorder`，但执行顺序实际是：

```text
left -> print root -> right
```

也就是中序遍历。新题解把机制明确为“表达式树结构 -> inorder skeleton -> 非根内部子树加括号”，避免函数名反向污染心智模型。

### Q42｜MST 唯一性的充分条件与一般判据分层

旧解析给出“任意环内边权均不相同”这一充分条件，本身可用，但容易被误记成唯一 MST 的必要条件。新题解区分：

```text
考试足够充分条件：所有边权互不相同 / 每个环边权互异
更一般判断：不存在可保持总权的等权 cycle exchange
```

从而避免把便捷判据绝对化。

### Q43｜C 语言与题设机器模型边界

题面明确给出 `f1(31)=-1`，因此本题按 32 位补码机器行为解释低 32 位全 1。新题解同时注明：严格 C 抽象语义中，有符号整数溢出不应被当作可移植的模 $2^{32}$ 规则。

另外把两个 float Gate 分开：

```text
n=24  -> precision / rounding boundary
n=127 -> finite range / overflow boundary
```

避免统一写成“float 精度不够”。

### Q44｜`shl` 的错误类比被压回 Representation Contract

整数左移乘 2 的前提是“位串按整数位权解释”；IEEE 754 位串由 `sign | exponent | fraction` 构成，整体 `shl` 会破坏字段。新题解用 `1.0f` 机器码左移后的最小反例独立验证。

### Q45｜Wakeup ≠ Running

旧解析虽然给出了 `Blocked -> Ready -> Running`，新题解把 Owner 进一步拆开：设备完成/中断只能使等待条件满足并把 P 唤醒到 Ready；是否进入 Running 仍由 scheduler 决定。该边界已在多个年份重复出现。

### Q46｜Legacy 常量抄写错误 + 粗粒度锁问题

Canonical thread3 明确为：

```c
w.a = 1;
w.b = 2;
```

旧解析实现误写成 `w.b = 1`，新题解以 Canonical 为准。

同时没有用一个全局 `y_mutex` 把 thread1 与 thread2 的两个 reader 串行化，而是先构造 R/W conflict graph：

```text
t1 R(y) <-> t3 W(y)
t2 R(y) <-> t3 W(y)
t2 R(z) <-> t3 W(z)
```

只为真实冲突建立信号量，保留 t1/t2 并发。

### Q47｜GBN 两个方向状态必须分账

旧解析的主要数值答案可用，但叙述容易把 $S_{x,y}$ 中发送序号和捎带 ACK 混在一起。新题解显式维护：

```text
send_base / next_seq
recv_next
```

并验证：

```text
ACK=3 -> 对方已按序收到 0..2
(a) outstanding 3,4 -> window 7 还剩 5 槽
    -> S5,2 ... S1,2
(b) seq2 timeout -> GBN 重发 2,3,4
    -> first S2,3
Umax = 50%
```

## 4. Candidate Rules Evidence

### 数据结构

**Candidate DS-E1｜先恢复“结构拥有的语义”，再选遍历/操作。**

2017 Q41 表达式树不是“看到二叉树就做遍历”，而是先识别树的祖先关系已经拥有运算优先级，随后中序只承担序列化任务。

**Candidate DS-E2｜贪心题每一步必须声明 Candidate Set。**

2017 Q42 Prim 的正确第一动作不是“找最小边”，而是先建立 cut $(S,V-S)$，只在 crossing edges 内找最小；这与后续多年的最小生成树/图算法证据一致。

### 计算机组成原理

**Candidate CO-E1｜同一个数值题至少区分 Math / Type / Machine 三层。**

2017 Q43 连续验证：数学值不变，但 unsigned 循环边界、signed int 可表示范围、float precision、float exponent range 会分别改变程序行为。

**Candidate CO-E2｜位级操作前先确认 Representation Owner。**

2017 Q44 的 `shl`、CF、指令长度都说明：只有先知道一个 bit field 属于 integer / float / instruction encoding / flag 哪个对象，位运算才有合法语义。

### 操作系统

**Candidate OS-E1｜事件只负责它有权造成的状态迁移。**

2017 Q45 再次出现：I/O completion 可以 `Blocked -> Ready`，但不能直接保证 `Ready -> Running`。事件机制与调度 Policy 必须分层。

**Candidate OS-E2｜互斥设计先画 conflict graph，再决定锁粒度。**

2017 Q46 表明“共享变量”不是自动等于“所有访问互斥”；R-R 可以并发，真正需要禁止的是 R-W/W-W 重叠。锁应覆盖冲突边，而不是粗暴覆盖整个变量使用者集合。

### 计算机网络

**Candidate NET-E1｜双向协议必须维护方向化账本。**

2017 Q47 的 $S_{x,y}$ 同时携带正向 seq 与反向 ACK；若不先区分两个 Owner，很容易把累计确认、下一期待序号和重发窗口混为一谈。

**Candidate NET-E2｜窗口题先检查 sequence-space invariant。**

3 bit GBN 必须先得到 $W_s\le2^3-1=7$，再进行发送槽位与利用率计算；窗口大小不是后置公式参数，而是协议安全不变量。

## 5. Handbook Challenge

本年度暂未发现需要立即改写四科 Canonical Handbook 的硬冲突。较值得继续累计的边界有：

1. DS：算法 Candidate Set / Invariant 是否应在 Rules 中进一步统一表达；
2. CO：Math -> Type -> Bits 的三层账本是否已在表示专题中足够显式；
3. OS：R/W conflict graph 到最小锁粒度的生成流程是否应晋升同步 Rules；
4. NET：双向可靠传输的 direction-specific state ledger 是否已有足够跨年证据晋升。

以上均保持 Candidate，不因单年样本直接晋升 Rules。若后续证据独立确认 Canonical Handbook 本身存在事实、机制或边界硬错误，则应立即进入 Stable Write，而不是继续把硬错误长期留作 Candidate。

## 6. 年度结论

2017 题解层已经达到：

```text
Complete
+ Answer-Consistent
+ Model-Grounded
+ Independently Verified
+ Format-Stable
```

本年没有 Canonical 题意级修复，但成功暴露并隔离了 Q11 legacy 路由错误、Q41 命名误导、Q43 语言/机器模型边界、Q46 legacy 常量错误，以及 Q47 双向状态账本这一高价值生成性模式。