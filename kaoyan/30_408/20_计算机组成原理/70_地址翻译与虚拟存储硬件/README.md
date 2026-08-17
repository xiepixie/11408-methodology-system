# 地址翻译与虚拟存储硬件：VA 怎样成为可访问的 PA

状态：LaTeX 工作稿待人工确认；Canonical 深度正文已建立并发布。

## Hook

本册只追踪硬件地址翻译：`VA → VPN/offset → TLB/page walk → permission → PA → Cache/Memory`。分页只替换页号，页内偏移保持不变。

## Scope / Stop Boundary

本册 Owns VA/PA 拆分、PTE 硬件字段、TLB、单/多级 page walk、权限/valid、翻译缓存失效、PIPT/VIPT/VIVT 和精确异常边界。

页框分配、置换、工作集、COW、调页、阻塞和 OS handler 归 OS VM/Bridge，不在本册重复定义。

## Owns / Uses

- Uses CO-05 的存储访问与延迟；
- Uses CO-06 的 Cache 地址组织；
- 向 CO-B02 与 CO-I01 输出 PA、权限和 retry/fault 分支；
- TLB miss 不自动等于 Page Fault，Cache miss 也不是翻译失败。

## Read Next

- [CO-06 Cache 与存储层次](../60_Cache与存储层次/README.md)
- [OS-04 虚拟内存与地址翻译](../../30_操作系统/30_虚拟内存与页生命周期/README.md)
- [计组做题规则](../90_做题规则/README.md)

## Canonical Manual

- [Canonical LaTeX 正文](CO-07_地址翻译与虚拟存储硬件_方法论手册.tex)
- [Published PDF](../../../90_publish/408/CO-07_地址翻译与虚拟存储硬件_方法论手册.pdf)

## 当前状态

正文已核销《虚拟存储》《存储器层次》的硬件翻译部分：VPN/offset、PTE、page walk、TLB、fault 分层、失效同步与 Cache 组合进入 Canonical；页框分配、置换、工作集、COW 和调页留在 OS Owner。
