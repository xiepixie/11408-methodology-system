# X-I01｜一次 LOAD / Memory Access 的完整慢路径

状态：目录已建立，正文未建。

## Canonical Problem
一条 LOAD 已计算出有效虚拟地址后，从地址翻译到数据最终进入体系结构状态，fast path 与 slow path 怎样协作？

## Composition
`LOAD semantic -> VA -> TLB/page table -> PA -> Cache -> Memory -> data return -> commit`

Slow path：

`translation cannot continue -> Page Fault -> privileged OS entry -> VM repair/PTE update -> retry instruction -> translation/cache/memory -> commit`

## Uses
CO03/06/07、OS03、CO-B02、X-B01、X-B02。

## Owns
跨 CO × OS 的完整 memory-access composition，不拥有 TLB、Cache、Page Fault 的局部机制。

## Verification
逐层问：这是 translation state 缺失、cache copy 缺失，还是 page residency/mapping 无法继续？禁止把三类 miss 合并。
