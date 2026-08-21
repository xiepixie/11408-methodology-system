# DS10｜Hash 与直接定位

状态：Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接。

## Position
数据结构 Topic。

## Mother Problem
怎样把 key 映射到有限槽位，用空间和冲突管理换取接近直接访问的查找能力？

## Mother Model
`Key -> Hash Mapping -> Collision -> Resolution -> Load State -> Expected Cost`

## Owns
散列函数、冲突、开放定址/链地址、装填因子、查找成功/失败语义与重散列基础。

## Uses
Atlas Foundation；DS-B02 做索引策略比较。

## Does Not Own
有序索引、系统中的具体哈希表工程实现。

## Manual
- Canonical：[Hash与直接定位：方法论手册 (TeX)](DS10_Hash与直接定位_方法论手册.tex)
- Published：[Hash与直接定位：方法论手册 (PDF)](../../../90_publish/408/DS10_Hash与直接定位_方法论手册.pdf)
- 训练：[散列表探测、ASL 与删除](散列表探测、ASL与删除.md)：线性/二次探测账本、成功/失败 ASL、Empty/Deleted 区分、链地址与重散列。
- 完整实现：[`ds10_hash_table.hpp`](code/ds10_hash_table.hpp)
- 断言测试：[`ds10_hash_table_test.cpp`](code/ds10_hash_table_test.cpp)

## Code Contract
本册代码覆盖开放定址线性探测、Empty/Occupied/Deleted 三态、重复插入、删除墓碑、查找失败终止与装载因子触发的重散列。范围查询和有序遍历继续由 DS09/DS11 Own。
