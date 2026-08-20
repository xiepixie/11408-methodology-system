# 地址翻译与 Cache 综合训练

> 训练定位：面对同一道题同时出现 VA、TLB、页表、PA、Cache、页内偏移、组号、Tag、PIPT/VIPT，以及 TLB miss / translation fault / Cache miss 等慢路径时，训练只做**跨 Owner 交接**，不重讲 CO-06 或 CO-07 的内部机制。  
> 模型归属：[CO-B02 地址翻译与 Cache 访问桥梁手册](CO-B02_地址翻译与Cache访问_桥梁手册.tex)。CO-07 Owns 翻译；CO-06 Owns Cache；本文件只训练两者如何通过地址位、权限、状态与重试点接起来。

## 母题表示：只有合法访问身份成立，Cache 命中才是有效结果

一次数据访问可压成：

```text
(VA, access type, privilege, size)
→ Translation
→ (PA, permission, attributes, status)
→ Cache address fields
→ Valid + Tag identity check
→ Hit / Miss
```

这条链表示**语义依赖**，不是固定硬件串行时序。VIPT 等实现可以并行做部分 TLB/Cache 工作，但若 translation / permission 最终失败，Cache 即使暂时读到了匹配数据，也不能把它当成本次访问的合法完成结果。

> [!idea] 综合题第一动作
> 先在纸上画两条竖线：**左边 Translation，右边 Cache**。每一个字段写清“来自 VA 还是 PA、属于页内 offset 还是被翻译的页号”。

## 一、先建立三层地址几何

典型分页 + Cache 题同时存在三个粒度：

```text
Byte / Addressable Unit
⊂ Cache Block
⊂ Page
```

若按字节编址：

- Cache block size $B=2^b$ B → block offset 为 $b$ 位；
- page size $P=2^p$ B → page offset 为 $p$ 位；
- 通常 $b\le p$，但仍以题设为准。

页内 offset 不变量给出：

$$
VA[0:p-1]=PA[0:p-1].
$$

因此 Cache 所需要的低位，只要完全落在 page offset 内，就不依赖 PFN。

## 二、核心桥梁：哪些 Cache 位可以直接从 VA 得到

PIPT Cache 的最终身份通常按物理地址解释：

$$
PA=[CacheTag\mid Set\mid BlockOffset].
$$

如果：

$$
b+s\le p,
$$

其中 $s$ 为 Cache set index 位数，则 `Set + BlockOffset` 完全落在 Page Offset 中。因为 Page Offset 在 VA→PA 时不变，所以：

- block offset 可直接从 VA 低位取得；
- set index 也可直接从 VA 的 page-offset 区取得；
- 最终 tag 身份仍按 Cache 组织所需的物理身份确认。

等价容量形式：

$$
N_{set}\times B\le PageSize.
$$

对于 $E$ 路 Cache，$N_{set}\times B$ 也就是每一路的数据容量，因此常写：

$$
\frac{CacheDataCapacity}{E}\le PageSize.
$$

> [!trap] “可以用 VA 求组号”不等于“Cache 用虚拟 Tag”
> 低位相同只证明 index/offset 可以提前得到；最终身份是否使用 PA Tag，要看 PIPT/VIPT/VIVT 组织。不要把“低位可提前使用”误写成“整个 Cache 都按 VA 访问”。

## 三、PIPT / VIPT / VIVT：训练时只问接口，不背口号

### PIPT

```text
VA
→ TLB/Page Walk
→ PA
→ Set/Tag/Offset
→ Cache
```

优点是物理身份直接；代价是查 Cache 通常等待翻译。

### VIPT

```text
VA page-offset bits ─────────→ Cache set/offset lookup
VA VPN ─→ TLB ─→ PFN ───────→ PA tag compare
```

两条线可并行的关键不是名称，而是：Cache index 是否完全来自 page offset。

### VIVT

可直接用 VA 查找，但会引入 homonym/synonym、地址空间切换与权限先后等额外问题。408 若题面不要求具体方案，不自行补一套工程一致性机制。

## 四、三类失败 / 慢路径严格分流

| 事件 | 当前缺失对象 | 下一步 | 是否必进 OS |
|---|---|---|---|
| TLB miss | translation cache entry | page walk / refill | 不一定 |
| Page/permission fault | 当前映射、驻留或权限不足 | precise fault handoff | 是 |
| Cache miss | data block copy | victim / fill / retry | 通常否 |

稳定顺序：

```text
TLB miss
→ page walk 可能成功
→ 得到 PA
→ Cache 仍可能 hit 或 miss
```

而：

```text
Page / permission fault
→ 当前没有合法 PA 可交给普通 Cache 数据访问
→ 停止 Cache 分支
→ 转 OS 修复/拒绝
```

## 五、命中组合：不要把三个 Hit/Miss 当独立硬币

在 408 常见一致模型中：

### TLB hit ⇒ 当前翻译可用；408 经典模型下页面应处于可驻留状态

因为 TLB 缓存的是当前可用 translation，若页被换出或映射失效，应同步使旧 translation 不可继续命中。因此在 408 的简化一致模型中可写：

$$
TLBHit\Rightarrow CurrentMappingUsable\Rightarrow PageResident/Present.
$$

这里故意不用 `Page hit`：页面是否驻留是 VM 状态，不是 Cache 式命中事件。

### 页面不驻留 / 发生缺页 ⇒ 本次普通 Cache 判定不再继续

若页面当前不驻留，地址翻译会在缺页异常处停止并交给 OS。此时更精确的结论不是“Cache 一定 miss”，而是：

$$
PageNotResident\Rightarrow TranslationFault\Rightarrow CacheLookupNotReached
$$

因为本次访问尚未形成可供普通物理 Cache 路径消费的合法 PA。修复后 retry 是一次新的访问尝试，再重新进入翻译和 Cache 路径。

### 页面驻留 / PTE present ⇏ TLB hit

页可以在主存、PTE 有效，但 TLB 尚未缓存 translation。

### Cache hit ⇏ TLB hit

若题设允许翻译先完成 page walk，再查 Cache，TLB miss 后仍可能形成 PA 并 Cache hit。

2010 Q17 正是用“不可能组合”检查这些依赖，而不是要求死背八种情况。

## 六、完整一次访问：Fast Path 与 Slow Path

### Fast Path

```text
VA request
→ TLB hit
→ permission OK
→ PA
→ Cache set lookup + tag/valid hit
→ block offset 取数据
→ return
```

### TLB miss but page hit

```text
VA request
→ TLB miss
→ page walk
→ valid PTE + permission OK
→ PFN
→ refill/update TLB
→ PA
→ Cache hit/miss
```

### Page fault

```text
VA request
→ TLB miss / walk or direct PTE check
→ mapping/residency/permission cannot continue
→ precise fault
→ OS repair or reject
→ if repaired: mapping/TLB consistency
→ retry original access
```

OS repair 的内部生命周期不在本文件拥有，转 X-B02 / OS-04。

### Cache miss

```text
translation success
→ PA
→ Cache miss
→ victim / dirty writeback if needed
→ lower-level block fetch
→ fill tag/data/state
→ retry/satisfy original access
```

内部细节回 CO-06。

## 七、把上传材料中的“大定位 + 小定位”收敛为跨层查询骨架

可以把 TLB 与 Cache 的相似组织压成：

```text
Key
→ Index / Candidate Location
→ Tag / Identity
→ Valid / State
→ Payload
```

### TLB

```text
Key = VPN
Index = TLB Set（若组相联）
Tag = TLB Tag
Valid = Translation entry 是否可用
Payload = PFN + Permission
```

### Cache

```text
Key = PA / Block Identity
Index = Cache Set
Tag = Cache Tag
Valid = Data line 是否可用
Payload = Data Block
```

这个类比的作用是**迁移 lookup 结构**；停止条件是：一旦进入 miss handler、payload 含义、失效原因或成本，两侧立即回自己的 Owner。

## 八、典型字段题：统一从“粒度 → 位预算”生成

### 2021 Q44 型 TLB

PA 24 bit，VA 30 bit，page 4KB，TLB 2-way、8 sets：

- PageOffset = 12 bit；
- VPN = 18 bit；
- TLBSet = 3 bit；
- TLBTag = 15 bit。

不是四个独立公式，而是：

```text
4KB page → 12-bit offset
30-bit VA - 12 → 18-bit VPN
8 TLB sets → 3-bit set
18 - 3 → 15-bit tag
```

### 2018 Q44 型 Cache

若 PA 28 bit，Cache block 32B、8 sets、2-way：

- block offset = 5 bit；
- set = 3 bit；
- tag = 20 bit。

若 page offset = 12 bit，则 set+offset 只占 8 bit，全部落在 page offset，因此虚拟地址低 12 位已经足以确定 Cache set 与 block offset。

## 九、Footprint 在桥梁题中的作用

同一个连续数组可能同时问：

- 跨多少 Cache block；
- 跨多少 page；
- 首元素在 block/page 内偏移多少。

对任一粒度 $U$：

$$
N_U=\left\lceil\frac{d+L}{U}\right\rceil.
$$

因此 2025 Q43 不需要为“129 blocks”和“3 pages”背两种技巧：只是在同一地址区间上分别令 $U=64B$ 与 $U=4KB$。

## 十、Page Fault 后的 retry：跨科边界必须保留

2019 Q14 明确：经典请求分页中 fault 修复后应重新执行 faulting instruction，而不是跳到下一条。

2014 OS Q45 更进一步揭示一个训练细节：若某次数据访问第一次查 TLB 后发生 page fault，OS 修复并返回后，原访问会重试，因此**同一逻辑访存可能出现第二次 TLB lookup**。这类“访问次数”必须按生命周期数事件，不能只按源码语句数。

这里本文件只保存 retry 对硬件访问次数的影响；为什么 task 是否 block、怎样 page-in、何时 Ready，转 X-B02 / OS-04 / OS-B01。

## 十一、概念边界

| 概念边界 | 为什么容易混淆 | 真正判据 | 题目信号 | 混淆后的错误 |
|---|---|---|---|---|
| Page Offset ≠ Block Offset | 都是地址低位 | 页内位置粒度 vs Cache 块内位置粒度 | page + block 同时出现 | 位数直接互换 |
| TLB Set ≠ Cache Set | 都是“组号” | 前者来自 VPN，后者来自 Cache 地址组织 | TLB+Cache | 用错位源 |
| VA 可求 Cache Set ≠ VIVT | 都用到 VA 位 | 低不变量可提前 index vs 整体虚拟身份 Cache | VIPT/低位不变 | 把 PA tag 丢掉 |
| TLB miss ≠ Page Fault | 都会让 translation fast path 失败 | 缺 translation copy vs mapping/permission 不能继续 | miss/fault | 无条件进 OS/磁盘 |
| Page Fault ≠ Cache miss | 都叫 miss/缺失 | 地址合法性/驻留 vs 数据副本 | 完整访存 | 未形成 PA 就算 Cache |
| Cache hit ≠ Permission OK | 都像“找到了” | data copy 存在 vs 本次访问合法 | 权限位 + Cache | 非法数据提交 |
| Retry ≠ 下一条指令 | 都是异常返回后的继续 | 重新执行 faulting access vs PC 前进 | page fault | 少算访问或破坏语义 |

## 十二、真题证据链

- **2010 Q17**：TLB/Page/Cache 三层可行组合；
- **2011 Q44**：页表翻译后使用物理地址查 Cache；4 路 TLB 字段；
- **2012 Q43**：Cache miss 后再引出 page-fault rate 与 DMA event rate，说明事件可跨层传播；
- **2014 OS Q45**：page fault 修复后的原指令重试导致额外 TLB lookup；
- **2016 OS Q45**：VA32/PA24、page8KB、TLB 全相联、Cache 2-way；比较 Cache miss 与 Page Fault 成本并区分写策略层次；
- **2018 Q44**：图示完整 VA→TLB→PA→Cache；valid/tag、LRU/dirty、低 page-offset 位推 Cache set；
- **2019 OS Q46**：利用 VA/PA 低 12 位相同，从虚拟地址直接确定 Cache 组；
- **2021 Q44**：TLB 组相联字段与 LRU；
- **2023 Q43**：page footprint + Cache group/index + hit rate 同题；
- **2024 Q16**：Cache—主存与主存—外存的共同层次结构及停止边界；
- **2024 Q17**：TLB tag 位预算；
- **2024 Q18**：MMU 不负责 Cache miss；
- **2025 Q43**：page offset 12 bit、Cache set 6 + offset 6 可由 VA 低位确定；同时考 block/page footprint 与成本；
- **2026 Q19**：TLB 与 PTE 同步约束。

## 十三、陌生综合题固定落笔协议

```text
1. 写 Request = (VA, R/W/X, privilege, size)
2. page size → PageOffset；VA/PA → VPN/PFN
3. TLB 组织 → TLB set/tag；走 hit/miss
4. PTE → mapping/present/permission；决定 PA 或 fault
5. 形成 PA 后再拆 Cache tag/set/block offset
6. 检查 Cache set/offset 是否完全落在 page offset，可否由 VA 提前得到
7. Cache valid/tag → hit/miss；miss 转 CO-06 生命周期
8. fault 转 X-B02/OS-04；修复后明确 retry 点
9. 若问次数/时间，先列 TLB/PTE/Cache/memory 的 event count，再定价
```

## 十四、最短压缩

> [!summary] 一句话
> **翻译先回答“这个 VA 合法地指向哪个 PA”，Cache 再回答“这个 PA 的数据副本是否在快层”；两层都可用 Index/Tag/Valid 思考，但 Page Offset 是它们之间最关键的不变量接口。**
