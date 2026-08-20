# TLB 与硬件地址翻译

> 训练定位：面对 VA/PA 位划分、VPN/PFN、页内偏移、页表项、TLB 全相联/组相联、TLB tag/index、page walk、权限检查、TLB 替换与翻译同步题时，训练把“地址表示、翻译副本、页表状态、翻译结果”分开。  
> 模型归属：[CO-07 地址翻译与虚拟存储硬件方法论手册](CO-07_地址翻译与虚拟存储硬件_方法论手册.tex)。分页、PTE、TLB、page walk、权限、VA/PA 与翻译失效的稳定机制由 Canonical 正文拥有；本文件只负责硬件侧真题的字段推导、状态模拟和检查。OS 如何分配 frame、置换、处理 fault 与 COW 不在本文件重新解释。

## 母题表示：翻译只改变“页身份”，页内位置保持不变

若页大小为 $P=2^p$ B，则：

$$
VA=[VPN\mid PageOffset],
$$

$$
PA=[PFN\mid PageOffset].
$$

合法分页翻译可写成：

$$
VPN\xrightarrow{PTE/TLB}PFN,
$$

而低 $p$ 位页内偏移原样保留。

> [!idea] 地址翻译题第一动作
> **先由 page size 锁死 Page Offset。** 然后再问高位 VPN 被哪种结构消费；不要先画 TLB，也不要先算 Cache。

## 一、Stage 1：编址单位 → Page Offset → VPN / PFN

页大小本质上是“一个页包含多少个可寻址单元”。

若按字节编址、页大小为 $2^p$ B，则 offset 为 $p$ 位。

若题目采用其他编址单位，先换算“每页包含多少个编址单位”，再取 $\log_2$；不能把页的字节数直接当地址单位。

给虚拟地址宽度 $V$、物理地址宽度 $M$：

$$
VPNBits=V-p,
$$

$$
PFNBits=M-p.
$$

### 页内偏移不变量

分页不是把整个 VA 重新编码，而是只替换页号：

$$
PA=(PFN\ll p)+PageOffset.
$$

因此：

- VA 和 PA 低 $p$ 位相同；
- 一页内部对象之间的相对偏移保持不变；
- 后续 Cache 若只使用这些不变低位，可以在翻译完成前得到部分定位信息。

最后一点的正式跨 Owner 推导进入 CO-B02，本文件只负责先证明 offset 不变量。

## 二、Stage 2：页表项不是“只有 PFN”

训练时把 PTE 至少拆成：

```text
Mapping Identity + Availability/Validity + Permission + Other State
```

题目可能给：

- present / valid / 装入位；
- PFN；
- R/W/X；
- user/supervisor；
- accessed/reference；
- dirty/modified；
- 其他架构/题设字段。

先按题目定义解释每个位，尤其不要把不同教材中的 `valid`、`present`、`P` 自动当成完全相同语义。

### 翻译结果必须带状态

成功不是“查到一个 PFN”就结束，而是：

```text
当前 PTE / TLB entry 可用
AND 本次访问权限允许
→ PFN + PageOffset
→ 合法 PA
```

若权限或映射状态不足，则不能把一个猜出来的 PA 继续交给 Cache。

## 三、Stage 3：TLB 是 VPN → PFN/Permission 的翻译副本

TLB 的 lookup key 是 VPN，而不是整个 VA；Page Offset 不参与 TLB 身份比较。

### 全相联 TLB

所有有效 entry 都是候选：

```text
VPN
→ 并行比较所有有效 Tag
→ 命中则得到 PFN/Permission
```

不存在 set index 字段。

### $E$ 路组相联 TLB

若 TLB 共 $N$ 项、$E$ 路，则：

$$
N_{set}=\frac{N}{E}.
$$

若 $N_{set}=2^s$，VPN 再拆为：

$$
VPN=[TLBTag\mid TLBSet],
$$

$$
TLBSetBits=s,
$$

$$
TLBTagBits=VPNBits-s.
$$

> [!idea] TLB 可以“借 Cache 的骨架思考”，但缓存对象不同
> 共同骨架是 `Index → Candidate → Tag → Valid → Payload`。Cache 的 payload 是 data block；TLB 的 payload 是 PFN/permission translation。不要因为组织相似就把 TLB miss 与 Cache miss 合成同一个状态机。

## 四、Stage 4：TLB 访问序列也要逐次维护状态

遇到一串 VPN 且给 LRU/FIFO：

1. 把每个 VPN 投影为 TLB set；
2. 只在该 set 内比较 tag；
3. hit 后更新 replacement state；
4. miss 后若有 invalid entry 先填空位；
5. 否则按题设策略选择 victim；
6. 写入新 translation 后更新 valid/tag/PFN/permission/state。

2021 Q44 直接要求用 Cache 的方式手推 2 路 TLB：VPN 10、12、16、7、26、4、12、20 中，只有组 4 发生超过 2 个活跃翻译的竞争，最终 20 到来时替换 LRU 的 VPN 4。

### 虚拟地址位数变化

若 page size、TLB set 数和相联度不变，而 VA 从 $V$ 位增至 $V+k$ 位：

- Page Offset 不变；
- VPN 增加 $k$ 位；
- TLB set bits 不变；
- TLB tag 增加 $k$ 位；
- PFN 位数由物理地址决定，不因 VA 加宽自动变化。

## 五、Stage 5：TLB miss、缺页与权限 fault 分开

### TLB miss

缺的是**翻译副本**。下一步是 page walk / 查页表；页表可能给出完全合法的 mapping，然后 refill TLB。

### 缺页：408 经典模型中的 non-present / non-resident 分支

408 经典请求分页题里的“缺页异常”通常特指：目标虚页当前没有可直接使用的驻留页框，因此正常翻译不能继续，需要进入 OS 修复路径。这里缺的是**页面驻留/可用映射状态**，不是 TLB 副本。

### Page Fault：更广义的体系结构异常名称

真实 ISA/OS 中，page-fault exception 往往是“页式地址访问无法沿普通快路径完成”的异常入口；异常原因可以进一步区分 non-present、permission/protection、COW 等。不同架构的 fault 分类不同，因此做 408 时优先服从题面采用的经典“缺页”语义，做系统理解时再展开更广义 Page Fault。

### Permission / Protection fault

映射身份可能存在，页面也可能驻留，但本次 R/W/X 或 privilege 不被允许。它不是“没查到翻译副本”，也不是经典意义上的“页面不在主存”。

> [!trap] TLB miss ≠ 缺页
> TLB miss 之后必须继续查 PTE；只有当前映射、驻留或权限状态不能支持本次访问时，才进入相应 fault 分支。

## 六、TLB hit 与页表状态的一致性

若系统约定：TLB 只缓存当前有效 mapping，并且页表变更后会正确失效/隔离旧 TLB entry，则：

$$
TLBHit\Rightarrow CurrentMappingUsable.
$$

在 408 简化模型中通常进一步表现为：

$$
TLBHit\Rightarrow PageResident/Present.
$$

因此在 408 经典一致模型中，“TLB hit + 页面当前不驻留”通常是不可能组合。避免写 `Page hit / Page miss`，因为页面驻留不是 Cache 式命中状态。

2026 Q19 进一步考查同步：若页号 22 的 PTE 已同步为 $P=0$，对应 TLB entry 就不能还保持同一 VPN 的 `V=1` 且携带冲突 PFN。真正考的是：**翻译副本必须与当前权威映射状态一致。**

### 修改页表以后

只写 PTE 不等于所有旧翻译自动消失。若旧 TLB entry 仍可能被使用，就必须按题设/ISA：

- invalidate；
- flush；
- 用 ASID/PCID 等地址空间标签隔离；
- 或其他明确同步机制。

跨 OS 配置与硬件消费的完整责任链转 X-B02。

## 七、多级页表：先数索引容量，再数访问依赖

若一页能放 $N$ 个 PTE，则单级索引最多表达：

$$
\log_2N
$$

位。VPN 按页表层级拆分时，每一级 index 位数由“这一张页表能放多少表项”生成，不是把 VPN 平均切几份。

Page walk 是依赖链：

```text
Root + Index1
→ PTE1 / next-table address
→ Index2
→ ...
→ Leaf PTE
→ PFN
```

后一级地址依赖前一级返回；实际等待时间是否等于固定“几次主存”还要看 PTE 是否在 Cache、题设是否给 TLB/Page-walk cache 等条件。

2026 OS Q28 的三级页表题则训练另一类数量问题：顶层和中间层各能产生多少张下级页表；这属于 OS-04 的页表空间/分配视角，本文件只保留硬件索引结构。

## 八、硬件责任与停止边界

硬件侧稳定责任：

```text
使用当前 translation context
→ TLB lookup / page walk
→ 读取 PTE 硬件可见状态
→ 检查权限
→ 成功生成 PA 或报告 precise fault
```

OS 负责：

- 地址空间和页表内容如何建立；
- frame 分配与 residency；
- 缺页后 page-in / demand-zero / COW；
- replacement / working set；
- fault handler 如何修复或拒绝。

2026 OS Q24 直接验证这个 Owner 分工：地址转换由 MMU 硬件执行，页表状态由 OS 管理，fault 由硬件检测/触发而由 OS 处理。

## 九、概念边界

| 概念边界 | 为什么容易混淆 | 真正判据 | 题目信号 | 混淆后的错误 |
|---|---|---|---|---|
| VPN ≠ PFN | 都是页号高位 | 程序地址空间身份 vs RAM 页框身份 | VA/PA 拼接 | 把 VA 高位直接当 PA 高位 |
| Page Offset ≠ VPN | 都来自 VA | 页内位置保持不变，VPN 被翻译 | page size | 把整个 VA 拿去查页表 |
| PTE ≠ TLB entry | 都含 PFN/权限 | 权威/内存映射结构 vs 近期翻译副本 | 页表与快表同时给出 | 忽略失效与同步 |
| TLB miss ≠ 缺页 | 都表现为“快路径失败” | 缺翻译副本 vs 当前映射/驻留不能继续 | TLB miss + PTE | 直接算磁盘 I/O |
| 缺页 ≠ Permission fault | 都可产生同步异常 | 不驻留/不可继续映射 vs 本次访问类型越权 | P/RWX/privilege | 错写 OS 修复动作 |
| TLB set ≠ Cache set | 都用低若干位取组 | 前者来自 VPN，后者取决于 Cache 地址组织 | TLB+Cache 同题 | 把组号字段串层 |
| VA 加宽 ≠ PFN 加宽 | 地址位数都变长 | PFN 由 PA 位宽决定 | 修改 VA width | 错增 TLB payload 位数 |

## 十、真题证据链（2010—2026）

- **2010 Q17**：TLB、页面驻留状态与 Cache 命中组合的可行性约束，尤其 TLB hit 不应与“当前页面不驻留”同时成立；
- **2011 Q44**：VA/PA、page offset、页表翻译、4 路 TLB tag/set 与后续 Cache；
- **2013 Q16**：全相联 TLB，VPN 命中后 PFN + offset 拼接 PA；
- **2015 Q16**：TLB 与 write-through Cache 同题，训练“地址翻译副本”和“数据写传播”是不同责任；
- **2018 Q44**：TLB 全相联、页内 offset 保持、翻译后物理地址进入 Cache；
- **2019 Q14**：经典请求分页下缺页由 CPU/MMU 检测、OS 处理，修复后重试 faulting instruction；
- **2020 Q15**：TLB 与 Cache 都受局部性影响、都可由硬件处理 miss，但保存对象与实现不同；
- **2021 Q44**：30-bit VA、4KB page、2 路 8 组 TLB，VPN→set/tag、LRU 与 VA 加宽；
- **2022 Q15**：单级页表翻译，present/PFN + offset 得 PA；
- **2024 Q17**：32-bit VA、1KB page、32 项 4 路 TLB → 19-bit tag；
- **2024 Q18**：MMU 检测 translation/permission/TLB 状态，不负责 Cache miss；
- **2026 Q19**：组相联 TLB 与主存页表同步、一致性约束；
- **2026 OS Q24**：硬件地址转换与 OS fault handling 的职责边界；
- **2026 OS Q29**：TLB 可降低翻译平均成本，多级页表主要优化页表空间而非天然降低访问时间。

## 十一、陌生题调用协议

```text
1. 编址单位是什么？page size 对应几位 offset？
2. VA / PA 分别多少位？VPN / PFN 各多少位？
3. 当前查的是页表还是 TLB？它缓存/保存的对象是什么？
4. TLB 全相联还是组相联？set/tag 来自 VPN 哪几位？
5. hit/miss 后 replacement state 是否要更新？
6. PTE 当前 present/valid/permission 如何？
7. 成功时只替换页号并保留 offset；失败时准确分类 fault。
8. 页表修改后检查旧 TLB translation 是否仍可能被消费。
9. 得到合法 PA 后停止本文件；若要进入 Cache，转 CO-B02/CO-06；若要修复 fault，转 X-B02/OS-04；若题目开始计算 TLB/page-walk 的平均访问时间，先调用 [存储层次与 AMAT](../60_Cache与存储层次/存储层次与AMAT.md) 区分 translation EAT 与 Cache AMAT。
```

## 十二、最短压缩

> [!summary] 一句话
> **分页翻译只替换页身份，不改变页内位置；TLB 只是 VPN→PFN/权限的高速副本，miss 后仍可查页表，只有当前映射/权限不能继续时才进入 fault。**
