# DS-B01｜Frontier Traversal

状态：目录已建立，正文未建。

## Owners
DS02 栈/队列 ↔ DS04 Tree ↔ DS07 Graph。

## Mother Interface
`Visited State + Frontier -> Choose Next -> Visit -> Expand -> Update Frontier`

## Owns
递归、stack、queue 作为 frontier 管理方式时，如何改变展开顺序并形成 DFS/BFS 等遍历语义。

## Boundary
不重新定义 Tree/Graph 结构，也不重新定义 Stack/Queue 本体。
