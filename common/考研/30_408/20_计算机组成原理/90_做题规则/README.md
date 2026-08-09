# 计组做题规则与性能工具箱

状态：工作稿，待验证规则已建立，尚无已采用规则。

## 已采用

暂无。以下规则仍需用真实题目校准。

## 待验证

### 先定位数据，再画通路

看到指令、微操作或 Cache/Memory 综合题时，先标出数据当前所在位置与目标位置，再决定经过哪些 MUX、总线、功能部件和寄存器。

### 区分可用时刻与提交时刻

流水线题同时标记 value ready 和 architectural commit，不能因为数据已被 forwarding 就认为指令已经完成。

### 每个 miss/fault 写处理者

TLB miss、Cache miss 和 Page Fault 必须分别写清检测者、处理者、是否需要 OS，以及完成后从哪里重试。

## 性能工具箱

性能计算先声明成本模型，再选择公式：

- CPU time：$IC\times CPI\times clock\ period$；
- Pipeline：$ideal\ CPI+stall$；
- Cache：$hit\ time+miss\ rate\times miss\ penalty$；
- Memory/Bus：latency、throughput、bandwidth 和 bottleneck；
- 加速比较：明确基准、受影响比例和不能加速的部分。

不能用频率、CPI、IPC、MIPS 或命中率中的单一数字直接宣告系统更快。

## 已否定

暂无。
