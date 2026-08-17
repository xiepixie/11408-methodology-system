# DS-B01｜Frontier Traversal

状态：Canonical 正文已建立；Published PDF 见下方链接。

## Owners
DS02 栈/队列 ↔ DS04 Tree ↔ DS07 Graph。

## Mother Interface
`Visited State + Frontier -> Choose Next -> Visit -> Expand -> Update Frontier`

## Owns
递归、stack、queue 作为 frontier 管理方式时，如何改变展开顺序并形成 DFS/BFS 等遍历语义。

## Boundary
不重新定义 Tree/Graph 结构，也不重新定义 Stack/Queue 本体。

## Manual
- Canonical：[DS-B01_FrontierTraversal_方法论手册.tex](DS-B01_FrontierTraversal_方法论手册.tex)
- Published：[DS-B01_FrontierTraversal_方法论手册.pdf](../../../../90_publish/408/DS-B01_FrontierTraversal_方法论手册.pdf)

## Review v1
已核对 frontier、visited、发现时机和 DFS/BFS 顺序；明确容器实现不拥有图算法全局正确性。下一轮用重复边、断开图和发现/访问时机变化题验证。
