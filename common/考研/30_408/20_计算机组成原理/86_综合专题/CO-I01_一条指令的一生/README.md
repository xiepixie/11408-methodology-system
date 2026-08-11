# CO-I01｜一条指令的一生

状态：目录已建立，正文未建。

## Canonical Problem
优先以 LOAD 为母指令，追踪一条指令从软件可见语义到最终体系结构状态提交的完整路径。

## Composition
`ISA Decode -> Datapath -> Pipeline Timing -> Effective Address -> Translation -> Cache/Memory -> Result -> Commit`

## Uses
CO01–CO08、CO-B01、CO-B02。

## Owns
完整单指令协作轨迹与 fast/slow path，不拥有任一局部硬件机制。

## Variants
ADD / STORE / BRANCH 用于检验母轨迹在哪些步骤被删减或改变。
