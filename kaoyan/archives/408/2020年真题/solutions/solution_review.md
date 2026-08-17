# 2020 408｜题解审阅记录

> 本文件只记录 Derived Solution 审阅过程中发现的 Source Correction、Legacy Difference 与模型证据；正式题解保持干净。单题经验不会直接晋升 Rules；若独立确认 Canonical Handbook 存在事实、机制或边界硬错误，则按 Stable Write 修正唯一 Owner，并回归受影响题解。

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

## Source / Legacy Review

### Q11｜学科路由仍存在 legacy 文件名错误

- Q11 是直接插入排序与简单选择排序比较，按 408 Profile 属于**数据结构**。
- Legacy 文件名仍为 `q11_计算机组成原理.md`；本轮年度索引与 Derived Solution 均按 Profile 路由到数据结构。
- 再次验证：raw 文件名和网站元数据都不能覆盖 Exam Profile 的稳定题号路由。

### Q41｜“正数”与题给负数示例发生硬冲突

- Canonical 题面原写“a、b、c 均为正数”，但题目随后给出的三个集合包含 `-1、-25、-10` 等负整数。
- 这不是解法边界，而是题面内部自相矛盾；结合题目目标函数与示例，显然应为“a、b、c 均为整数”。
- 本轮已把 Canonical Source 恢复为“整数”。算法核心恒等式
  $$D=2(\max-\min)$$
  对任意整数均成立，不依赖正性。

### Q41｜Legacy 解析不完整

- Legacy 只展开到“观察数轴”，没有完整给出可执行算法与复杂度。
- 本轮从目标函数压缩出“最短三色区间”模型，并证明只有推进当前最小值指针才可能缩短区间。
- 最终得到三指针 `O(n1+n2+n3)` / `O(1)` 解法，而不是三层枚举。

### Q42｜前缀特性必须双向检查

- Legacy 已指出二叉树/Trie 是自然表示，但“插入过程中遇到叶结点”只覆盖“旧编码是新编码前缀”。
- 新题解额外显式检查：新编码结束时当前位置若已有子结点，则“新编码是旧编码前缀”。
- 两个方向共同组成完整 Prefix-Free Invariant。

### Q43｜同一低位比特的 signed / unsigned 溢出语义不同

- 完整 64 位乘积为 `00000000 FFFFFFFEH`。
- `umul()` 的真实结果仍在 `UINT32_MAX` 范围内，不溢出；`imul()` 的真实数学结果超过 `INT32_MAX`，溢出，尽管二者低 32 位完全相同。
- 这强化了 CO 的固定动作：**先求完整数学/位级结果，再应用目标类型的 representability contract**。

### Q44｜Cache 几何先于地址运算

- 固定链：`capacity/block/ways -> line count -> set count -> offset/index/tag`。
- 本题得到 64 sets、6-bit offset、6-bit set、20-bit tag；Write Through 因为主存始终同步，不需要 dirty bit。
- 顺序扫描 4096 B 对齐数组只产生 64 次 compulsory miss；不应把每个写操作再算一次 miss。

### Q45｜四条同步边可压缩成两个 join-counter 信号量

- Legacy 使用 `SAC/SBC/SCE/SDE` 四个信号量逐边编码，逻辑正确。
- 本轮把信号量解释为“完成事件令牌计数器”：A/B 共用 `sAB=0`，C 连续 `wait` 两次；C/D 共用 `sCD=0`，E 连续 `wait` 两次。
- 这不是为了机械追求信号量少，而是把 DAG 中的 **AND-join** 显式建模成“收齐若干完成令牌”。

### Q46｜地址翻译必须逐层拥有 Owner

- `a[1][2]` 先由语言布局产生唯一 VA=`10801008H`；
- 再按 `10/10/12` 拆成 Dir=`42H`、PTIndex=`1`、Offset=`8`；
- PDE 物理地址=`00201108H`；PDE 给出的 `00301H` 是二级页表页框，故 PTE 物理地址=`00301004H`。
- 这是“语言地址生成”和“MMU 翻译”不能混算的又一个强样本。

### Q47｜Canonical 曾混入答案图，已清理

- 原 Canonical Q47 同时引用 `q47_fig1/fig2/fig3.svg`。
- `q47_fig3.svg` 实际已经填入：`203.10.2.2:80 -> 192.168.1.2:80`，属于第 (1) 问答案，而不是原始题面信息。
- 本轮已从 Canonical Source 删除该引用，只保留网络拓扑图和 NAT 表结构图；资产文件本身继续作为 legacy 证据保留，不再由正式题面引用。

### Q47｜重叠私网地址必须引入 Scope

- H2 与 Web 服务器都叫 `192.168.1.2`，但分别属于 R3、R2 后面的两个 NAT 域。
- 正确路径不是“同名 IP 直接路由”，而是：

```text
H2: 192.168.1.2 -> 203.10.2.2
R3 SNAT: 203.10.2.6 -> 203.10.2.2
R2 DNAT: 203.10.2.6 -> 192.168.1.2(Web)
```

- 这一题对 NET 的 `Scope -> State Owner -> Rewrite Event` 模型是非常强的真实证据。

## Candidate Rule Evidence

### DS

- **压缩目标函数后再选算法**：Q41 若先化简为 `2(max-min)`，三集合问题立即转化为最短覆盖区间；结构一旦出现，三指针是自然生成而非技巧记忆。
- **有序多指针题先找单调支配动作**：当最小值不动时，推进其他指针不能缩短 `[min,max]`，因此只推进当前最小值。
- **Trie 的前缀合法性是双向祖先约束**：`old terminal before end` 与 `children at new terminal` 缺一不可。

### CO

- **同一 bits 必须先问类型解释器**：Q13、Q43 都重复证明 signed / unsigned / float 不是“数值换个名字”，而是不同表示合同。
- **硬件性能题先分 ISA 与微体系结构**：无 MUL、迭代 MUL、阵列 MUL 分别属于软件序列、硬件状态机、专用组合结构三个层次。
- **Cache 题固定先 Geometry 后 Trace**：先算 Offset/Set/Tag，再追踪 compulsory/conflict/capacity 行为。

### OS

- **多前驱同步可建模为 completion-token join**：先从偏序 DAG 消去无关互斥，再决定是一边一信号量还是按 join 聚合计数。
- **地址问题先分语言对象连续性与物理页框连续性**：连续数组要求 VA 连续，不要求 PA 连续。

### NET

- **NAT 题的地址身份必须写成 `IP + scope`**：相同 RFC1918 地址可以在不同私网域同时存在。
- **逐跳只允许明确 Owner 改状态**：R3 做 SNAT、R2 做 DNAT，中间普通路由器不应被想象成任意改写地址。
- **时间题先画关键路径**：Q36/Q38/Q40 再次重复出现“对象发送时间、RTT 反馈、阶段状态”不能混成一个公式。

## Evidence Promotion 状态

2020～2026 已形成连续七年样本。若同一模式在更早年份继续重复，可开始对以下候选规则做跨年聚合审阅，但仍需检查 Handbook 中是否已经有唯一 Owner，避免重复建规则：

```text
Representation first
-> identify State/Cost Owner
-> perform minimal state transition
-> verify invariant / boundary
```

尤其值得继续统计的信号包括：

- DS：有序结构 -> 单调指针 / frontier；
- CO：位宽/字段 -> Owner -> 完整表示 -> 截断；
- OS：偏序/等待 -> token or state transition；
- NET：scope -> endpoint identity -> rewrite/timeline。
