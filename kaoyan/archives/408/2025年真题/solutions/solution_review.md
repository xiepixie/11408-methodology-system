# 2025 年 408｜题解校准与模型反馈

本文件只记录 **Derived Solution Layer** 的校准结论，不修改 Canonical Exam Source。单题技巧不直接晋升 Rules；若题解独立确认 Canonical Handbook 存在事实、机制或边界硬错误，则另走 Stable Write 修正唯一 Owner，并重新验证受影响题解。

## 1. 校准结论

2025 已作为第一套完整的 model-grounded calibration year。Q1～Q47 均已按：

```text
Canonical Question
-> Model Anchor
-> Problem Representation
-> Decision / Solution Chain
-> Verification
-> Compression
-> Boundary
```

重写。旧 `qNN_*.md` 只作为 legacy reference，不再是高质量题解 Owner。

## 2. Legacy 解析中发现的具体问题

### Q43｜Cache AMAT 口径

旧解析给出约 `8.24 cycles`，其计算相当于把 miss 的一次访问总成本直接按 200 cycle 计入。

Canonical 题面使用的是：

```text
Cache 命中时间 = 2 cycles
缺失损失（miss penalty） = 200 cycles
```

按 CO-06 的成本合同，`miss penalty` 是在正常 lookup/hit-time 之外增加的缺失代价，因此：

$$
AMAT=2+\frac{129}{4096}\times200\approx8.30\text{ cycles}.
$$

**处理：新题解使用 8.30 cycles。**

分类：`Legacy Solution Correction`；当前不构成 Handbook Challenge，CO-06 已明确区分 hit time 与 miss penalty。

### Q44｜异常响应层次

旧解析把“CPU 自动响应”和“异常处理程序继续保存完整现场”混写在一起。新题解按 CO-08 Owner 边界拆开：

```text
硬件最小响应：保存断点/程序状态 -> 特权切换/必要屏蔽 -> 形成 handler 入口
软件 handler：继续保护通用寄存器等完整现场 -> 处理 -> 恢复/返回
```

同时固定 `x=0xff` 在题目 32 位 `int` 语境下的含义为 `000000FFH`，不能把它按 8 位补码误读为 `-1`。

分类：`Model Clarification`。

### Q45｜PV 临界区过宽

旧解析用 4 个信号量，数量本身合理，但把“放树苗、填土”整体放进铁锹互斥区。题面只有“挖坑、填土”使用铁锹，因此这会无谓降低并发度。

新题解把：

```text
放树苗()
```

移出 `shovel` 临界区，只让 `填土()` 占用铁锹；Safety 不变，并发度更符合题意。

分类：`Solution Quality Improvement`。

### Q47｜Legacy 解析不完整

旧 `q47_计算机网络.md` 只有部分第 (1) 问推导，后续内容缺失，不能作为完整解答依据。

新题解从 Canonical 图和题面独立完成：

- propagation / transmission / bottleneck 三种时间与速率对象分离；
- GBN 利用率反推发送窗口，再由 GBN 序号空间约束反推序号位数；
- 由 `10.10.10.33/26` 先恢复管理区网络号，再按主机容量做 VLSM。

分类：`Legacy Solution Incomplete`。

## 3. 从 2025 得到的题解写作证据

### Candidate Rule Evidence

以下模式在 2025 多题中重复出现，值得继续用 2024～2009 真题攻击，而不是现在直接晋升新 Rule：

1. **先命名成本对象再套公式**：Q10、Q18、Q20、Q33、Q43、Q47；
2. **先找状态 Owner 再判断字段/对象归属**：Q16、Q19、Q23、Q29～Q32、Q37、Q46；
3. **绝对命题优先最小反例/边界检查**：Q4、Q6、Q9、Q24、Q28；
4. **综合题先写中间状态表，再回答最终数值**：Q42、Q43、Q47；
5. **算法设计先从暴力基线找重复工作，再提炼可复用状态**：Q41。

这些均先保留为 Evidence；只有跨年份重复验证、边界稳定、真实降低错误率后，再进入正式 Rules。

## 4. Handbook Challenge

当前 2025 校准未发现需要立刻修改 Canonical Handbook 的系统性机制错误。

Q43、Q44、Q45 暴露的主要问题来自 legacy solution 的口径/表达，而现有 CO-06、CO-08、OS-03 Handbook 已能生成更稳健答案，因此分类为：

```text
No Immediate Handbook Update
```

后续若在其他年份出现同类冲突，再累计 Evidence 决定是否加强 Rules 的触发语句。
