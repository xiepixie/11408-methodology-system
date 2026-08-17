# 2019 408｜题解审阅记录

> 本文件只记录 Derived Solution 审阅中发现的 Source/Profile Correction、Legacy Difference 与模型证据；正式题解保持干净。单题技巧不直接晋升 Rules；若独立确认 Canonical Handbook 存在事实、机制或边界硬错误，则按 Stable Write 修正唯一 Owner，并回归受影响题解。

## 本轮格式 Gate

Q1～Q40：

```text
Model Anchor
-> 解题链
-> 选项判断
-> Verification
-> Compression
-> 易错边界
```

Q41～Q47：

```text
Model Anchor
-> Problem Representation
-> Decision Points
-> Solution Chain
-> Verification
-> Compression
-> 易错边界
```

## Source / Profile / Legacy Review

### 2019｜发现第二类历史综合题路由变体

原 `exam_profiles/408.json` 只记录了 2016 综合题路由例外，而 2019 的真实题目内容再次证明“综合题题号 -> 学科”不能永远使用 default 映射。

2019 实际路由为：

```text
Q41-Q42  数据结构
Q43-Q44  操作系统
Q45-Q46  计算机组成原理
Q47      计算机网络
```

其中：

- Q43 是哲学家就餐/死锁预防；
- Q44 是 SSTF、簇到磁盘物理地址与设备驱动；
- Q45 是机器代码、相对寻址、字节序、整数溢出；
- Q46 直接承接 Q45，考分页与指令 Cache。

本轮已把 2019 写入 `exam_profiles/408.json -> routing_overrides`，并把年度 `exam.json` 路由改为 `profile-override-2019`。

年度综合题分值也恢复为：

```text
Q41 13
Q42 10
Q43  8
Q44  7
Q45 16
Q46  7
Q47  9
-------
    70
```

这同时保持四科学科总分：数据结构 45、组成原理 45、操作系统 35、网络 25。

### Q11｜再次确认 legacy 学科文件名不可靠

Q11 是 12 路外部归并中的虚段补齐，属于**数据结构**。Legacy 文件名仍为 `q11_计算机组成原理.md`。

本轮年度索引与 Derived Solution 已按 408 Profile 的客观题路由恢复为数据结构。跨 2020～2023 连续出现的 Q11 误路由说明：

```text
legacy filename / scraped category
!=
Canonical subject routing
```

### Q43｜legacy 解释含明显字符级错误

Legacy prose 曾写：当 `m>=n` 时“让碗的资源量等于 -1”。这在逻辑上不可能用于资源计数；其后代码实际写的是：

```c
bowl = min(m, n - 1);
```

新题解以资源环不变量重新证明：最多允许 `n-1` 位哲学家进入抢筷子阶段，才能破坏完整 circular wait；正确表达始终是 `n-1`，不是 `-1`。

### Q45｜旧解析“改成 float/double”不适合作为首选修复

题目要返回精确整数 `13! = 6227020800`。Legacy 把 `double/float/long double/long long` 并列当作修改方案，虽然部分浮点类型在这个具体数值上可能恰能表示，但这模糊了类型契约。

新题解采用：

```c
long long f1(int n)
```

并确保递归乘法在 64 位整数域中执行。这样保持“阶乘是整数”的语义，也直接解决 32 位 `int` 的可表示范围问题。

同时把 `imul` 溢出条件收敛为统一规则：

```text
OF=0 iff full product == sign_extend(low32)
```

比“高若干位是否全 0/1”的文字记忆更不易混乱。

### Q46｜VA 能推出 Cache 组号的真正原因

不能简单说“call 的虚拟地址组号是 0，所以物理 Cache 也是第 0 组”。真正的桥梁是：

- 页大小 4 KB -> VA/PA 低 12 位页内偏移保持不变；
- 64 B block -> offset 6 bit；
- 64 lines / 4-way -> 16 sets -> set 4 bit；
- `set + block offset = 10 bit < 12 bit page offset`。

因此 Cache set bits 完全落在页内偏移中，才允许在未知物理页框号时唯一确定 set=0。

## 综合题模型审阅

### Q41｜“首尾交替”首先是表示变换题

暴力每轮寻找尾结点会得到 $O(n^2)$。目标序列的生成结构直接提示：

```text
找中点
-> 后半段原地 reverse
-> zipper merge
```

得到 $O(n)$ 时间、$O(1)$ 空间。这里最值得保留的不是具体代码，而是：**当单链表目标访问方向与 next 方向冲突时，先修改表示，再执行目标遍历。**

### Q42｜从操作合同反推 Representation

四条要求共同排除了普通顺序队列和“出队立即 free 的普通链队列”。循环链式复用结构使：

```text
front==rear        -> logical empty
rear->next==front  -> allocated ring has no free slot -> grow one node
```

入队、出队均为最坏 $O(1)$，而不是只做到 amortized $O(1)$。

### Q43｜Deadlock Prevention = Admission Control

碗不是单纯额外资源，而可以成为进入“抢筷子状态”的 admission token：

```text
bowl = min(m,n-1)
```

这是一种非常典型的 Control Plane 思维：不改变每根筷子的互斥规则，而是控制多少执行流能同时进入有环依赖的资源竞争区。

### Q44｜簇号不能直接用于 SSTF

SSTF 的成本对象是磁头柱面移动，因此必须：

```text
cluster number
-> cylinder
-> compare seek distance
```

同一道题又要求 `cluster -> cylinder/track/sector`，进一步验证“文件系统逻辑块标识”和“设备物理几何标识”必须通过驱动层桥接。

### Q45/Q46｜机器代码题固定五步链继续成立

2019 再次验证：

```text
Instruction Boundary
-> Next PC
-> Operand / Control Role
-> Endian / Width
-> Memory Hierarchy Projection
```

Q45 的 call displacement、Q46 的 page-offset-preserved Cache set 都能由这条链生成，而不需要碎片口诀。

## Candidate Rule Evidence

### DS

- **目标遍历方向与底层链方向冲突时，优先做 Representation Transform**：Q41 的 split + reverse + zipper 是典型样本。
- **数据结构设计题先列 Operation Contract**：是否动态增长、是否复用、最坏还是摊还复杂度，会直接唯一化表示选择。
- **多路最佳归并先写叶结点同余条件**：`(n+d-1) mod (k-1)=0` 比死记“补几个虚段”更可迁移。

### CO

- **地址类综合题固定分层**：`EA -> byte order`、`VA page -> PA offset invariant -> Cache projection`。
- **PC-relative 永远先找 Next PC**：当前指令起始地址不是 displacement base。
- **有符号截断溢出统一看 sign-extension 可恢复性**：完整结果是否能由保留低位符号扩展还原。

### OS

- **Wakeup = wait condition resolved**，不是“发生了任何调度相关事件”。
- **Deadlock Prevention 可以通过 admission limit 打破 circular wait 的形成条件**。
- **I/O 题先找成本所在层**：SSTF 看 cylinder，而不是文件系统 cluster number。

### NET

- **序号空间题先写无歧义约束**：不要只记 SR/GBN 各自窗口公式。
- **广播题固定 `prefix -> network/broadcast -> router boundary`**。
- **设备选择题先划 L3 Scope，再决定 Router/Switch**；不要从拓扑图视觉位置反猜设备。

以上仍保持 Candidate Evidence。2019 加入后，若同一规则已经在多个独立年度稳定出现，可进入下一轮跨年 Evidence Promotion 审阅，但本轮不直接修改 Handbook/Rules。
