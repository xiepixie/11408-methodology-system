# CO-I01｜一条指令的一生

> 类型：Integration
> 状态：LaTeX 工作稿待人工确认；Canonical Integration 正文已建立并发布。

## Canonical Problem

一条 LOAD 怎样从软件可见语义出发，经过取指、译码、通路、流水时序、地址翻译、Cache/Memory，最终只在合法路径提交体系结构状态？

```text
ISA Semantic
-> Fetch / Decode
-> Datapath / Pipeline
-> Effective Address
-> Translation / Cache / Memory
-> Result Ready
-> Precise Commit
```

## Uses

CO01–CO08、CO-B01 与 CO-B02。ADD / STORE / BRANCH 只用于删改母轨迹，验证模型是否可迁移。

## Owns / Stops

本 Integration 只拥有完整单指令协作轨迹、fast/slow path、跨 Owner handoff 和停止条件；不重新定义任何局部机制。进入某个 Topic 的内部推导时，应跳回其 Canonical Owner。

## 训练导航

- [一条指令全过程推演](一条指令全过程推演.md)：训练值依赖线、ready/need 时间线与 exception/commit 线怎样共同组织 LOAD / STORE / ADD / BRANCH 的完整推演。

## 阅读

- [Canonical Integration 正文](CO-I01_一条指令的一生_综合手册.tex)
- [发布 PDF](../../../../90_publish/408/CO-I01_一条指令的一生_综合手册.pdf)
- [计组 Subject Atlas](../../README.md)
- [CO-B01 ISA 语义与数据通路](../../85_科内桥梁/CO-B01_ISA语义与数据通路/README.md)
- [CO-B02 地址翻译与 Cache 访问](../../85_科内桥梁/CO-B02_地址翻译与Cache访问/README.md)

## 当前状态

八个 Topic 与两册内部 Bridge 的 Canonical 候选正文均已存在，满足 Integration 成熟前提。正文仍待统一真题攻击与人工确认。
