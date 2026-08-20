# 地址翻译与虚拟存储硬件：VA 怎样成为可访问的 PA

状态：Canonical LaTeX 已完成本轮结构、术语与图示重审；现有 Published PDF 仍是上一版派生稿，待发布流程同步。

## Hook

本册只追踪硬件可观察的地址翻译：`Request(VA, access type, privilege) → VPN/offset → TLB/page walk → mapping/permission → PA or fault`。分页只替换页身份，页内偏移保持不变；形成合法 PA 后才把访问交给 Cache/Memory。

## Scope / Stop Boundary

本册 Owns VA/PA 拆分、PTE 硬件字段、TLB、单/多级 page walk、权限/valid、翻译缓存失效、PIPT/VIPT/VIVT 和精确异常边界。

页框分配、置换、工作集、COW、调页、阻塞和 OS handler 归 OS VM/Bridge，不在本册重复定义。

## Owns / Uses

- Uses CO-05 的存储访问与延迟；
- Uses CO-06 的 Cache 地址组织；
- 向 CO-B02 与 CO-I01 输出 PA、权限和 retry/fault 分支；
- TLB miss 不自动等于 Page Fault，Cache miss 也不是翻译失败。

## 训练导航

- [TLB 与硬件地址翻译](TLB与硬件地址翻译.md)：训练 VA/PA、VPN/PFN、Page Offset、PTE、TLB 全相联/组相联、替换、同步与硬件责任边界；不重讲 OS fault repair。
- [存储系统真题训练总索引](../90_做题规则/存储系统真题训练总索引.md)：按 2009—2026 真题连接地址翻译、Cache 与 OS VM。

## Read Next

- [CO-06 Cache 与存储层次](../60_Cache与存储层次/README.md)
- [OS-04 虚拟内存与地址翻译](../../30_操作系统/30_虚拟内存与页生命周期/README.md)
- [计组做题规则](../90_做题规则/README.md)

## Canonical Manual

- [Canonical LaTeX 正文](CO-07_地址翻译与虚拟存储硬件_方法论手册.tex)
- [Published PDF](../../../90_publish/408/CO-07_地址翻译与虚拟存储硬件_方法论手册.pdf)

## 当前状态

正文已改为单一翻译因果路径，不再先概述、后“补充细节”重复展开；VPN/offset、PTE、page walk、TLB、缺页与 protection fault、失效同步、PIPT/VIPT/VIVT 已统一用词与责任边界。页框分配、置换、工作集、COW 和 fault repair 留在 OS Owner。
