# X-B02｜Hardware Address Translation × OS Virtual Memory

状态：目录已建立，正文未建。

## Owners
CO07 地址翻译硬件 ↔ OS03 Virtual Memory。

## Mother Interface
`OS Mapping Decision -> PTE/Page Table State -> MMU/TLB Consumption -> Translation Success or Fault -> OS Repair -> Retry`

## Owns
OS 怎样把地址空间策略编码成硬件可消费 mapping；硬件何时能继续翻译、何时必须以 fault 把控制权交回 OS；修复后为什么可以 retry。

## Responsibility Split
- 计组：TLB、page walk、PTE 硬件可见字段、VA->PA path；
- OS：address space、page allocation/residency、fault handling、replacement、COW。

## Anti-Bridge
`TLB miss != Page Fault`；`Hardware Cache != OS Page Cache`。
