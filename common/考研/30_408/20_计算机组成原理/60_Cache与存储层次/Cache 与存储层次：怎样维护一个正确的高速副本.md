# Cache 与存储层次：怎样维护一个正确的高速副本

状态：Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建。

> **迁移提示**：本文件是旧 Markdown working source，不再承担 Handbook Owner。后续 Source Diff 后迁入本 Topic 的 Canonical `.tex`；最终 README 只保留 Landing Page。

## 1. 母问题

当快存储太贵、慢存储太远时，怎样在上层保留一小部分数据副本，使大多数请求更快，同时仍能判断副本属于谁、是否有效、是否已修改？

```text
locality
-> transfer in blocks
-> place candidate line
-> identify by tag
-> select bytes
-> maintain replacement/write state
```

Cache 的本质不是“小型主存”，而是带身份与状态的副本系统。

## 2. 为什么“按地址直接找数据”不够

Cache 容量远小于主存，多个主存块必须复用有限 cache lines。因此每次访问都要回答：

1. 这个块允许放在哪些位置？
2. 当前位置保存的究竟是哪一个主存块？
3. 块内请求的是哪一个字节/字？
4. 副本是否有效、是否比下一级更新？

这生成了 placement、tag、offset、valid、dirty 与 replacement。

## 3. 地址三分法

对字节编址、数据容量 $C$、块大小 $B$、相联度 $E$：

$$
S=\frac{C}{B\times E}
$$

若 $B,S$ 为 2 的幂：

$$
b=\log_2B,\quad s=\log_2S,\quad t=m-s-b
$$

物理地址分为：

```text
tag | set index | block offset
```

- offset 选择块内字节；
- index 选择候选集合；
- tag 与 valid 一起确认身份。

公式只适用于题设所给的寻址单位和 Cache 组织。若按字编址或块大小用字表示，必须先统一单位。

## 4. 三种放置策略是一条连续权衡

| 策略 | 候选位置 | 比较器/选择成本 | 冲突风险 | 替换选择 |
| ------------ | ----------: | --------------: | ------------: | ------------ |
| 直接映射 | 1 | 最低 | 最高 | 无选择 |
| $E$ 路组相联 | 同组 $E$ 行 | 中等 | 中等 | 组内 |
| 全相联 | 全部行 | 最高 | 无映射冲突 | 全局 |

提高相联度减少 placement 限制，但增加 tag 并行比较、数据选择、功耗与命中路径延迟。不能只写“命中率更高”。

## 5. Hit 与 Miss 的状态机

### Read hit

索引集合，比较 valid+tag，命中路经 MUX 选出数据，再由 offset 选目标字节/字。

### Read miss

```text
choose invalid line or victim
-> if dirty, write back victim
-> request block from lower level
-> fill data/tag/state
-> satisfy or retry original access
```

### Miss 分类

- compulsory：该块首次进入该 Cache；
- capacity：即使同容量全相联也装不下当前工作集；
- conflict：有限相联度造成额外互逐。

3C 是解释模型，必须在同一块大小、容量和访问序列下比较基线。

## 6. 写策略是两组独立选择

### Hit 时怎样向下传播

- write-through：同时更新下一层；一致关系直接，但流量大，常配 write buffer；
- write-back：只改 Cache 并置 dirty，逐出时写回；减少平均流量，但 miss 路径更复杂。

### Miss 时是否分配

- write-allocate：先取块再在 Cache 写；
- no-write-allocate：绕过 Cache 直接写下一级。

常见组合不是逻辑必然。题目必须读取明确策略，不能由 write-back 自动猜另一个选项。

## 7. 替换：精确信息有成本

直接映射无替换选择。组相联需要在候选路中选 victim：Random/FIFO/近似 LRU 等。

精确 LRU 需要维护组内相对新旧关系，其状态成本依具体编码与更新逻辑而定，不能笼统说“每行 $\log_2E$ 位”就足够。相联度增大时，工程实现常采用 pseudo-LRU 或随机近似。

## 8. 局部性不是保证

- 时间局部性：最近访问的块可能再次访问；
- 空间局部性：邻近地址可能很快访问。

块变大可利用空间局部性并降低 tag 数量，但同时：行数减少、无用数据更多、miss 传输时间和带宽压力上升。存在最优区间，没有“块越大越好”。

数组访问应先生成地址序列，再映射块号与组号。仅凭“行优先/列优先”口号无法处理起始偏移、行跨块、多个数组冲突等题目。

## 9. 性能模型

单级近似：

$$
AMAT=T_{hit}+MR\times MP
$$

多级递归：下一级 AMAT 可以成为上一级 miss penalty 的组成部分。

使用前声明：

- hit time 是否已包含并行 tag/data 访问；
- miss penalty 是否为额外时间；
- 写回脏块概率与成本是否计入；
- 指令/数据访问比例是否需要加权；
- stall 是否能被并行执行隐藏。

命中率高不必然总时间低：更高相联度可能增加 hit time，更大块可能增加 miss penalty。

## 10. 容量题：数据容量不等于物理总位数

每行至少包含：

```text
data bits + tag + valid + optional dirty + replacement/ECC metadata
```

$$
C_{physical}=N_{lines}\times bits_{per\ line}+shared\ metadata
$$

先确认题目所谓 Cache 容量是否只指 data store。替换信息可能按组共享，不应机械摊为每行固定公式。

## 11. 与地址翻译的接口

Cache 看到虚拟地址还是物理地址是独立设计选择：

- PIPT：翻译后用 PA 索引和比较，简单但 TLB 与 Cache 串行；
- VIPT：用页内偏移中的 VA 位先索引，同时查 TLB，再用 PA tag 比较；
- VIVT：速度路径短，但有 synonym/homonym 管理问题。

VIPT 能安全并行的关键是 index 不依赖会被翻译改变的 VPN 位；具体容量/相联度约束由 page offset 位数生成，不是背一个固定上限。

## 12. 母例：两个地址为什么互相驱逐

对直接映射 Cache：

1. 将两个地址除以块大小得到 block number；
2. $set=block\ number\bmod S$；
3. 若 set 相同而 tag 不同，它们竞争唯一一行；
4. 交替访问会反复 miss，即使 Cache 其他行空闲；
5. 提高相联度可让两块共存，但增加比较与选择成本。

这就是 conflict miss 的生成机制，而不是“Cache 太小”的泛化描述。

## 13. 做题调用协议

1. 统一字节/字、数据容量与块大小；
2. 算 line、set、offset/index/tag；
3. 把访问地址转为 `(block, set, tag, offset)`；
4. 逐次模拟 valid/tag/dirty/replacement 状态；
5. 写 miss 的 victim、write-back、fill、retry；
6. 性能题声明成本模型再算 AMAT；
7. 用边界地址与冲突序列验证。

## 14. 最小反例

- tag 相同但 $valid=0$，仍然 miss。
- write-through 不等于 write-no-allocate；它们是不同决策轴。
- Cache hit 不代表没有 TLB miss；一个是数据副本，一个是翻译副本。
- 增大 Cache 可能降低 miss rate，却因更慢 hit path 使总时间变差。

## 15. 压缩信号

> 先用 index 找候选，再用 valid+tag 证明身份；offset 只负责块内定位。

## 16. 来源处理

归档《Cache》《存储器层次》用于地址、替换和 AMAT 题型。固定两周期 hit、精确 LRU 位数、现代 CPU 一律整体 stall 等实现相关说法均未提升为稳定结论。
