# 2024 年 408｜题解与 Source 审阅记录

> 本文件只记录 Derived Solution / Source 维护中的差异、疑点与 Evidence，不进入正式题面。

## 1. 年度结论

- Q1～Q47 已建立 `model-grounded-v1` 题解。
- 选择题统一通过 `Model Anchor -> 解题链 -> 选项判断 -> Verification -> Compression -> 易错边界`。
- 综合题统一通过 `Model Anchor -> Problem Representation -> Decision Points -> Solution Chain -> Verification -> Compression -> 易错边界`。
- Canonical Source 在本轮发现了较大范围的历史拼接/转写错误；已按 2024 legacy 原料、题图和外部结构化来源交叉恢复。

## 2. Canonical Source Corrections

### Q4｜邻接多重表

Canonical 旧选项顺序与题图/答案冲突。本轮恢复为：

```text
A 0,2
B 2,4
C 3,2
D 2,3
```

图中 b、d 的度为 2、4，答案 B。

### Q9｜两次删除大根堆堆顶

Canonical 旧选项不是该题真实选项。本轮恢复后答案 B：

```text
20,19,15,5,8,12
```

并用两次 `末元素补根 -> 下滤` 独立验证。

### Q10 / Q11｜题面错位

Canonical 旧版 Q10、Q11 分别混入了其它外排序/起泡排序题。本轮恢复真实 2024：

- Q10：三段 `(3,5)`、`(7,9)`、`(6)` 二路归并比较次数，答案 C=5；
- Q11：败者树冠军记录内容，答案 D=最小关键字所在归并段号。

Q11 的 legacy 文件名仍为 `q11_计算机组成原理.md`，这是旧文件名分科错误；新题解与 Profile 均按数据结构处理。

### Q12～Q32｜整段历史题面错位

Canonical 旧版 Q12～Q32 与 2024 legacy / 年度答案表明显不对应，属于系统性 Source 错位，而不是局部 OCR。已整体恢复为真实题面：

- Q12 `int -> short -> int`；
- Q13 伪指令/微指令/机器指令/汇编指令；
- Q14 整数/浮点表示选择；
- Q15 整数乘法实现；
- Q16 Cache—主存 vs 主存—外存；
- Q17 TLB Tag 位数；
- Q18 MMU 地址翻译检测事件；
- Q19 流水线数据冒险；
- Q20 存储器总线峰值带宽；
- Q21 中断响应/处理优先级；
- Q22 DMA 数据通路；
- Q23～Q32 恢复为对应 OS 真题。

### Q33～Q40｜恢复题图/条件完整度

Canonical 旧版 Q33～Q36 曾被简化为泛化题面，丢掉了真实图题中的链路、VLAN、RTS/CTS 等条件；本轮恢复正式图题。

Q40 选项恢复为 `4 / 9 / 14 / 16`，答案 D。

### 综合题分值

按年度真实总分重新统一：

```text
Q41 13
Q42 10
Q43 13
Q44 10
Q45 7
Q46 8
Q47 9
```

合计 70 分。`exam.json` 中原先 Q43=12、Q44=11 的旧值已改为 13/10。

## 3. Legacy Solution Corrections

### Q20｜峰值带宽 vs 有效事务带宽

legacy 同时算出了：

- 峰值：6.72 GB/s；
- 给定 7-cycle burst 的有效吞吐：3.84 GB/s。

题目明确问“总线带宽（最大传输速率）”，所以新题解把成本对象先锁定为 peak bandwidth，答案 B=6.72 GB/s；3.84 GB/s 只作为对比边界。

### Q24｜孤儿 / 僵尸概念

legacy 用“孤儿进程和僵尸进程”共同解释父进程结束后子进程可继续存在，其中 zombie 概念不适合作该论据。新题解只保留稳定对象生命周期判断：子进程是独立进程对象，父终止不必然级联终止子。

### Q30｜RR 周转时间

新题解显式利用“P 的 CPU 时间最短”保证 P 完成前其它 9 个进程不会提前离队，从而每轮固定 50 ms，P 第 5 轮末在 250 ms 完成。

### Q32｜C-SCAN 距离

legacy 文字漏写了 `160 -> 120` 的 40，但最终答案仍为 788。新题解逐段列出：

```text
200->160->120->110->0->399->300->210
```

总距离 788。

### Q40｜HTTP RTT 的成本来源

legacy 把 16 RTT 解释为“8 RTT 建连 + 8 RTT 关闭”。这会混淆截止条件。

新题解使用非持久 HTTP 的正确关键路径：

```text
每对象：1 RTT TCP 建连 + 1 RTT HTTP 请求/响应
8 个对象串行 -> 16 RTT
```

题目截止到“接收完所有内容”，连接关闭不是第二个 RTT 的来源。

### Q41｜拓扑唯一性

legacy 设计思想写“进行 numEdges 轮遍历”，这是对象计数错误。拓扑排序每轮删除一个**顶点**，最多进行 `numVertices` 轮。

新题解用 zero-indegree frontier 统一处理：

```text
frontier=0 -> 有环
frontier=1 -> 唯一合法选择
frontier>1 -> 拓扑序不唯一
```

并给出 $O(n^2)$ 邻接矩阵算法和正确性证明。

### Q42｜散列表

legacy 表格错误多列地址 11、12，而表长 11 的合法地址只有 0～10；正文还出现地址 2 上关键字误写成 18。

新题解重新逐 key 构表并锁定：

```text
0:11, 2:14, 3:7, 5:20, 6:9, 9:3, 10:18
```

查找 14 的关键字比较序列为 `3,18,14`；查找 8 首次空槽地址为 7。

### Q43｜位串与标志位

legacy 结果主值基本正确，但表达中混有字段位号 OCR 和 OF/CF 解释混写。新题解严格区分：

```text
F  = 1FDB9753H
OF = 1   # signed overflow
CF = 1   # unsigned carry
unsigned overflow -> 看 CF
```

`A040A103H` 的 12 位立即数 `A04H` 按补码为 -1532，有效地址 `FFFF9CD4H`。

### Q44｜数组索引与小端

legacy 中元素编号说明有错位，但最终关键答案可恢复。新题解从 `base+i*4` 独立重算：

```text
&a[5] = 0013E004H
a[5]  = FFFFECDCH
sum   = 0000000EH
VPN    = 0013EH
array 至少跨 2 页
slli r4,r2,2 = 00212213H
short -> slli r4,r2,1
```

### Q46｜信号量“尽可能少”

legacy 在第 (2) 问使用 `mutex + full` 两个信号量，且后续内容不完整。

本轮按题设“一次 C1 + 一次 C2”重新做最小化：

```text
full=0
P1: C1; signal(full)
P2: wait(full); C2
```

一个同步信号量已经同时排除 C1/C2 并发，无需额外 mutex。第 (3) 问两个 C3 只需 `mutex=1`。

## 4. Candidate Rule Evidence

以下仅登记 Evidence，不直接晋升 Rules：

- **DS**：结构操作选择题反复证明“先写 Representation / Invariant，再模拟状态变化”能减少指针、堆、开放定址错误。
- **CO**：2024 Q12/Q17/Q20/Q43/Q44 再次支持“先做位宽/单位/成本对象预算，再进入计算”。
- **OS**：Q23、Q31、Q46 支持“Event / Handler / Completion 分层”和“先区分 Ordering vs Mutual Exclusion，再最小化同步原语”。
- **NET**：Q35～Q40、Q47 支持“Scope first + timeline first”；尤其 Q40 说明成本截止条件必须先于公式。

## 5. 当前未决

本轮没有阻断 2024 完成的 open item。后续若获得官方/高清原卷，可对 Q12～Q40 本次恢复做逐字符 Fidelity Pass；当前答案、题意、图题逻辑和综合题计算均已形成自洽闭环。