# CO-B01｜ISA Semantic × Datapath

状态：目录已建立，正文未建。

## Owners
CO02 ISA 与机器级程序 ↔ CO03 CPU 数据通路与控制。

## Mother Interface
`Instruction Semantic -> Required Architectural State Change -> Micro-operations -> Datapath/Control`

## Owns
软件可见的 ISA 状态变化怎样被翻译成内部数据移动和控制需求。

## Boundary
ISA Topic Own 指令语义；CPU Topic Own 具体通路与控制。C 语言映射仍属于 ISA Topic，不由本 Bridge 扩张。
