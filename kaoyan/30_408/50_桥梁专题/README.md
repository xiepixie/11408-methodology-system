# 408 Cross-Subject Bridge Atlas

> 类型：Atlas
> 状态：已采用；README 是 Canonical Cross-Subject Bridge Atlas，3 个 Core Bridge 与 1 个 Candidate Core 按当前边界逐册建设。

> 本目录只放跨越两个 Subject Canonical Owner 的稳定接口。单科 internal Bridge 留在对应 Subject 目录。

## 1. Promotion Rule

任何跨科连接先过两道 Gate：

```text
Gate 1: Bridge Validity
- two independent Owners
- stable handoff
- A output -> translation/shared structure -> B input

Gate 2: Standalone Promotion
- Ownership Pressure
- Reuse
- Current-Scope Relevance
- New Inference
```

“真连接”“经常一起出现”“讲起来漂亮”都不足以独立建 Core Bridge。

## 2. Core Bridge

### X-B01｜Privilege / Exception / System Call × OS Control

[入口](X-B01_PrivilegeExceptionSystemCall与OSControl/README.md)

计组 ISA/CPU ↔ OS Process/Control。拥有 user execution 怎样通过 exception/trap/system call 进入 privileged kernel control，再合法返回的软硬件 handoff。

### X-B02｜Hardware Address Translation × OS Virtual Memory

[入口](X-B02_HardwareAddressTranslation与OSVirtualMemory/README.md)

计组地址翻译硬件 ↔ OS VM。拥有 OS 构造 mapping/PTE、硬件消费 mapping、translation 无法继续时 fault 回到 OS 修复、随后 retry 的交接。首轮正文已按“配置—消费—失败—修复—重试”模型建立；[进入 X-B02](X-B02_HardwareAddressTranslation与OSVirtualMemory/README.md)。

### X-B03｜Interrupt / DMA × OS I/O

[入口](X-B03_InterruptDMA与OSIO/README.md)

计组 I/O 硬件 ↔ OS I/O/Process。拥有 request、DMA transfer、interrupt delivery、completion、wakeup 的软硬件责任边界。

## 3. Candidate Core

### X-B04｜Process / Socket × Transport Endpoint

[入口](X-B04_ProcessSocket与TransportEndpoint/README.md)

结构身份已经确认是真接口：process/system-call/socket object 与 port/TCP-UDP endpoint/transport state 存在稳定 handoff。

但独立 Core 优先级仍待 408 真题与 Coverage evidence；完整 kernel networking stack、NIC queue、driver ring 等工程细节只能作 Extension。

## 4. 当前不建立独立 Core 的连接

### Graph Algorithm × Routing

真实连接，但当前优先：

```text
Network Routing Topic
Uses
Data Structure Graph Algorithm
```

只有未来出现稳定 Ownership Pressure 与重复推理价值时再晋升。

### External-Memory Algorithm × Block I/O

当前由 DS12 使用 block-I/O cost model；不因为 B+ Tree / External Merge 与存储系统相关就自动建跨科 Bridge。

### Data Structure × Systems

过宽。Queue、Tree、Hash、Heap 等被 OS/Network 使用时，默认直接 `Use` 对应 Data Structure Owner。只有出现新的交接责任才建立具体 Bridge。

## 5. Anti-Bridge

```text
Hardware Cache != OS Page Cache
TLB miss != Cache miss != Page Fault
Routing uses graph algorithm != routing protocol is graph algorithm
Data structure appears in system != automatic cross-subject Bridge
```

## 6. Legacy Source

旧 `OS-B1_CPU与OS桥梁_方法论手册.tex` 不再是 Owner，接口骨架统一归入 X-B01–X-B04；但其中机制/策略、入口协议、DMA 与原子性等细节仍需逐项 Source Diff，因此旧 `.tex` / PDF 暂时保留，不作为平行总册使用。

## Review v1

X-B01、X-B02、X-B03 已完成首轮升级并发布；X-B04 通过接口有效性但继续 Candidate，已完成一次覆盖核对并保留 Promotion Evidence Gate。审阅统一采用“输出—翻译—输入—不变量—失败/恢复”模板，并保留旧总册等待逐项 Source Diff，不删除旧 Source。
