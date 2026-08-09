# 地址翻译与虚拟存储硬件：VA 怎样成为可访问的 PA

状态：工作稿，待人工确认。

## 1. 母问题

程序产生的虚拟地址怎样经硬件可见的映射与权限检查，形成一个可送入 Cache/主存的物理地址？

```text
virtual address
-> translation lookup
-> permission / validity checks
-> physical address
-> cache / memory access
```

其中 $VA=VPN\mid page\ offset$，$PA=PFN\mid same\ offset$。

本 Topic 只拥有地址翻译硬件。页面从磁盘调入、页框分配、置换、COW 与进程阻塞是 OS Policy。

## 2. 为什么需要间接映射

若程序地址直接等于物理地址，代码必须知道自己装在哪里，不同程序难以隔离、共享和迁移。分页引入固定粒度的间接关系：VPN 选择映射，offset 在页内保持不变。

核心不变量：

$$
page\ size=2^p \Rightarrow offset=p\ bits
$$

合法映射下：

$$
PA=(PFN\ll p)\;|\;offset
$$

翻译只替换页号，不修改页内偏移。

## 3. 页表项不是单纯的 PFN

硬件可见 PTE 通常包含：

- valid/present 或叶子判定信息；
- PFN/PPN；
- read/write/execute 与 privilege 权限；
- accessed/dirty 等状态，更新方式依 ISA；
- 软件保留或体系结构扩展位。

具体字段和“硬件自动置 A/D 位”不能跨架构硬套。以 RISC-V 为例，规范明确存在硬件更新和通过异常交给软件更新的不同扩展/配置路径。

## 4. 单级页表为何不可扩展

若 VA 有 $v$ 位、页大小 $2^p$ B、PTE 大小 $e$ B，线性页表项数为 $2^{v-p}$，完整大小为：

$$
2^{v-p}\times e
$$

稀疏地址空间会让大量无效区也占用表项。多级页表把页表本身分页，只为被使用的子树分配页面，代价是 TLB miss 时需要多次依赖访存。

### 级数计算

若一页能容纳：

$$
N_{PTE}=\frac{page\ size}{PTE\ size}
$$

则满层索引位数为 $\log_2N_{PTE}$。将 VPN 位按各级索引容量分段；顶级可以不足一整层。不能用“总页表大小除页面大小”代替树索引计算。

## 5. Page Walk 是一条依赖链

对 $L$ 级页表，walker 从页表根开始：

```text
root base + level-1 index -> read PTE
-> next-table base + level-2 index -> read PTE
...
-> leaf PTE -> PFN + permission
```

每一级地址依赖上一级返回的 PTE，因此单次 walk 的访问通常难以完全并行。页表项自身也会经过 Cache/存储层次，所以“$L$ 级页表固定等于 $L+1$ 次主存”只是忽略缓存的题设模型。

页表页面不必全部常驻；至少根和当前遍历所需结构必须可用。其驻留与故障处理由体系结构和 OS 共同约束，不能笼统说“整个页表必须常驻”。

## 6. TLB：缓存的是翻译，不是数据

TLB 保存最近的 VPN -> PFN 与权限信息。

### Hit

匹配 VPN（以及必要的地址空间标识），检查权限，拼接 offset 形成 PA。

### Miss

需要 page walk。walk 可由硬件完成，也可由异常交给软件完成，取决于 ISA/实现。TLB miss 本身不等于 Page Fault：页表中可能有完全有效的映射，只是快表没有副本。

### Page Fault / Access Fault

若 PTE 无效、权限不允许或地址不满足规则，处理器报告同步异常。后续是否能修复、是否调页、是否终止进程由 OS 决定。

| 事件 | 缺什么/错什么 | 常见快路径处理 | 是否必进 OS |
|---|---|---|---|
| TLB miss | 翻译缓存项 | page walk + refill | 不一定 |
| page not present | 可用驻留映射 | 产生 page-fault 异常 | 是 |
| permission fault | 访问不被允许 | 产生异常 | 是 |
| Cache miss | 数据块副本 | 下一级取块 | 通常否 |

## 7. 地址空间切换与失效

不同进程可让相同 VPN 映射到不同 PFN。TLB 条目若只按 VPN 匹配，会出现 homonym。解决思路：切换时失效，或用 ASID/PCID 等标识区分地址空间。

当 OS 修改 PTE 后，旧 TLB/translation-cache 副本可能仍存在，必须按 ISA 的同步/失效规则建立可见性。写了 PTE 不代表所有处理器立刻停止使用旧翻译。

## 8. TLB 与 Cache 的组合路径

### PIPT

```text
VA -> TLB -> PA -> cache index/tag
```

逻辑直接，无虚拟别名，但 hit path 串行。

### VIPT

```text
VA page-offset bits -> cache set lookup
VA VPN -> TLB -> physical tag compare
```

两路可并行，前提是用于索引的位在翻译前后不变。若 set index 侵入 VPN，不同 VA 映射同一 PA 时可能把同一物理块放入多个位置，需要额外管理。

### 做题约束

若 page offset 为 $p$ 位，block offset 为 $b$ 位，则不越过 page-offset 的 VIPT set-index 位至多为 $p-b$。由此可生成每路 data capacity 上限：

$$
sets\times block\ size\le page\ size
$$

总容量还要乘 associativity。

## 9. 精确异常与重启

访存指令可能先形成 VA，再因翻译或权限失败而异常。精确异常要求较老指令状态正确，故障指令尚未产生不可撤销的可见副作用，处理后能按 ISA 指定位置恢复或重试。

“缺页后同一指令一定恰好执行两次”不是合适模型。一次架构指令可能被硬件多次尝试、walk、重放；应追踪的是其副作用只允许成功提交一次。

## 10. 机制边界表

| 机制 | Owns | Uses | Stop Boundary |
|---|---|---|---|
| VPN/offset 拆分 | 翻译粒度 | page size | 不决定 frame 分配 |
| page walk | 硬件可见树遍历 | PTE layout | 不决定换哪个页面 |
| TLB | 翻译副本 | locality | 不是数据 Cache |
| fault delivery | 精确异常入口 | CPU commit | 不拥有调页/阻塞 |
| TLB invalidation | 旧翻译失效与排序 | ISA 同步规则 | 不拥有进程调度 |

## 11. 母例：一次 Load 的三种“没找到”

1. VA 的 VPN 不在 TLB：TLB miss，开始 page walk；
2. walk 找到有效叶 PTE：refill TLB，形成 PA，继续原访问；
3. PA 在 Cache 中没有对应 line：Cache miss，向下一级取数据；
4. 若 walk 发现 invalid/not-present：产生 page fault，硬件不能自行从磁盘换页；
5. OS 修复映射并执行所需失效/同步后，指令重试；
6. 最终 load 数据只在无异常路径提交到目标寄存器。

## 12. 做题调用协议

1. 由地址宽度和 page size 拆 VPN/offset；
2. 由 PTE/page 计算每级索引位；
3. 画 TLB hit、TLB miss+walk、fault 三条分支；
4. 每级标地址来源、访问对象和权限检查；
5. 得 PA 后再做 Cache tag/index/offset；
6. 时间题声明 TLB 与 Cache 串行还是并行、PTE 是否可缓存；
7. 最后写检测者、处理者、重试点和提交点。

## 13. 最小反例

- TLB miss 但 PTE 有效：没有 Page Fault。
- Cache hit 但权限检查失败：数据不能提交给指令。
- VPN 改变而 offset 不变；若把整个 VA 都查表，位数计算必错。
- OS 更新 PTE 但未按架构要求同步旧 TLB：硬件仍可能使用旧映射。

## 14. 压缩信号

> 翻译查“地址属于哪里”，Cache 查“数据副本是否在这里”；先证明映射和权限，再允许数据提交。

## 15. 校验依据

- [RISC-V Supervisor-Level ISA](https://docs.riscv.org/reference/isa/v20260120/priv/supervisor.html)用于校验 PTE、walk、A/D 更新选择和 translation-cache 同步边界。
- 归档《虚拟存储》用于题型覆盖；页面置换、工作集、颠簸、页框分配与缺页修复未纳入本 Topic，它们属于 OS VM。
