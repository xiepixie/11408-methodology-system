# X-B02｜Hardware Address Translation × OS Virtual Memory

状态：已采用；Canonical Bridge LaTeX 已完成本轮术语重审。现有 Published PDF 仍是上一版派生稿，待发布流程同步。

## Owners
CO07 地址翻译硬件 ↔ OS-04 虚拟内存与页生命周期。

## Mother Interface

OS 先把地址空间决策**编码为页表/PTE 状态**；MMU/TLB 再**消费这些状态完成翻译与权限检查**。成功时输出合法 PA 并进入后续数据访问；失败时以 fault 把原因与现场交给 OS，OS 修复或拒绝后，才可能在明确的 retry 点重新尝试原访问。

## Owns
OS 怎样把地址空间策略编码成硬件可消费 mapping；硬件何时能继续翻译、何时必须以 fault 把控制权交回 OS；修复后为什么可以 retry。

## Responsibility Split
- 计组：TLB、page walk、PTE 硬件可见字段与 VA 到 PA 的翻译路径；
- OS：address space、page allocation/residency、fault handling、replacement、COW。

## Anti-Bridge

- `TLB miss ≠ Page Fault`：前者缺翻译缓存副本，后者表示当前访问不能按现有映射/权限继续；
- `Hardware Cache ≠ OS Page Cache`：两者缓存的对象、Owner 与失效/填充事件不同。

## 训练导航

- [地址翻译软硬件交接](地址翻译软硬件交接.md)：把跨科题的完整落笔顺序、TLB miss / Page Fault / Cache miss 分流、旧翻译一致性与 retry 检查迁到训练层。

## Manual

- [Canonical deep body](X-B02_HardwareAddressTranslation与OSVirtualMemory_桥梁手册.tex)
- [Published PDF](../../../90_publish/408/X-B02_HardwareAddressTranslation与OSVirtualMemory_桥梁手册.pdf)
- [首轮调研证据包](../../../80_evidence/archive/review_log/2026-08-12/2026-08-12_X-B02_跨学科Bridge调研证据包.md)

## Current Model

首轮采用“配置—消费—失败—修复—重试”模型：OS 输出页表/PTE 状态，MMU/TLB 消费并输出 `PA + permission` 或 fault；可修复 fault 经现场保存、映射更新与旧翻译处理后回到明确 retry 点。不同 ISA 的寄存器与 page-walk 细节仍由各自 Owner 负责。

## Review v1

已核对 mapping/PTE、MMU/TLB、Page Fault、OS repair 与 retry 的责任链，并阻断 TLB miss、Page Fault、Cache miss 和 Page Cache 的混同。下一轮用不同 ISA 的 trap/translation 失效规则，以及 X-I01 的 LOAD 慢路径题验证。
