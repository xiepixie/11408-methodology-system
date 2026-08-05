# 408 计算机学科综合驾驶舱 (30_408 Cockpit)

> **学科研究本质**：
> $$
> \boxed{\text{Data (数据结构)}} \longrightarrow \boxed{\text{Program (汇编/指令)}} \longrightarrow \boxed{\text{Machine (计组/硬件)}} \longrightarrow \boxed{\text{OS (内核管理)}} \longrightarrow \boxed{\text{Network (跨机通信)}}
> $$

---

## 🎯 408 母模型 (Mother Model)

408 任意四科试题，统一表达为**状态机演化模型**：
$$
\boxed{S_t = (Objects, Relations, Queues)} \xrightarrow{Event + Mechanism + Policy} \boxed{S_{t+1}} \quad \text{s.t. } I(S_{t+1}) = \text{true}
$$

---

## 📊 当前专题完成度与索引 (Module Index)

| 模块 / 专题 | 对应目录 | 当前状态 | 唯一宿主 (Canonical Owner) | 发布态 PDF |
|---|---|---|---|---|
| **00 统一总图** | `00_统一总图/` | 已建构 | 全局数据-指令-操作系统-网络链路总图 | - |
| **10 数据结构** | `10_数据结构/` | 规划中 | 线性表、树、图、查找与排序算法复杂度 | - |
| **20 计算机组成原理** | `20_计算机组成原理/` | 规划中 | CPU 数据通路、Cache 一致性、BUS 与 DMA 硬件 | - |
| **30 操作系统** | `30_操作系统/` | **已打穿** | 进程、虚拟内存 (VM)、I/O 系统、文件系统 (FS) | 6 册已编译 |
| **40 计算机网络** | `40_计算机网络/` | 规划中 | 协议栈、TCP 状态机、拥塞控制、IP 路由 | 1 册已编译 |
| **50 桥梁专题** | `50_桥梁专题/` | **已打穿** | CPU $\times$ OS 软硬件协作边界 | 1 册已编译 |
| **60 综合专题** | `60_综合专题/` | **已打穿** | 内核状态机与跨子系统推演方法论 | 1 册已编译 |
| **90 做题规则** | `90_408做题规则/` | 运行中 | 408 八槽分析法与状态机推演控制规则 | - |

---

## 🔗 已成熟手册与发布视图链接 (Published Manuals)

已编译生成的 408 方法论精排讲义保存在 `90_publish/`：

1. 📄 [OS 进程线程调度与控制权方法论手册](file:///Users/xpx/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/xpx/Documents/I.P.A.R.A/%E5%B7%A5%E4%BD%9C%E9%A2%86%E5%9F%9F/%E8%B5%84%E6%BA%90/common/%E8%80%83%E7%A0%94/OS_%E8%BF%9B%E7%A1%AE%E7%BA%BF%E7%258B%E8%B0%83%E5%BA%A6%E4%B8%8E%E6%8E%A7%E5%88%B6%E6%9D%83_%E6%96%B9%E6%B3%95%E8%AE%BA%E6%89%8B%E5%86%8C_v1.pdf)
2. 📄 [OS 内存虚拟化与页生命周期方法论手册](file:///Users/xpx/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/xpx/Documents/I.P.A.R.A/%E5%B7%A5%E4%BD%9C%E9%A2%86%E5%9F%9F/%E8%B5%84%E6%BA%90/common/%E8%80%83%E7%A0%94/OS_%E5%86%85%E5%AD%98%E8%99%9A%E6%8B%9F%E5%8C%96_%E5%9C%B0%E5%9D%80%E7%BF%BB%E8%AF%91%E4%B8%8E%E9%A1%B5%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E6%96%B9%E6%B3%95%E8%AE%BA%E6%89%8B%E5%86%8C_v1.pdf)
3. 📄 [OS 并发专题与信号量 PV 方法论手册](file:///Users/xpx/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/xpx/Documents/I.P.A.R.A/%E5%B7%A5%E4%BD%9C%E9%A2%86%E5%9F%9F/%E8%B5%84%E6%BA%90/common/%E8%80%83%E7%A0%94/OS_%E5%B9%B6%E5%8F%91%E4%B8%93%E9%A2%98_%E4%BF%A1%E5%8F%B7%E9%87%8FPV%E6%96%B9%E6%B3%95%E8%AE%BA%E6%89%8B%E5%86%8C_v1.pdf)
4. 📄 [OS I/O 系统请求搬运与等待完成手册](file:///Users/xpx/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/xpx/Documents/I.P.A.R.A/%E5%B7%A5%E4%BD%9C%E9%A2%86%E5%9F%9F/%E8%B5%84%E6%BA%90/common/%E8%80%83%E7%A0%94/OS_IO%E7%B3%BB%E7%BB%9F_%E8%AF%B7%E6%B1%82%E6%90%AC%E8%BF%90%E7%AD%89%E5%BE%85%E4%B8%8E%E5%AE%8C%E6%88%90%E6%96%B9%E6%B3%95%E8%AE%BA%E6%89%8B%E5%86%8C_v1.pdf)
5. 📄 [OS 文件系统对象索引与持久化手册](file:///Users/xpx/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/xpx/Documents/I.P.A.R.A/%E5%B7%A5%E4%BD%9C%E9%A2%86%E5%9F%9F/%E8%B5%84%E6%BA%90/common/%E8%80%83%E7%A0%94/OS_%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F_%E5%90%8D%E7%A7%B0%E5%AF%B9%E8%B1%A1%E7%B4%A2%E5%25引与持久化方法论手册_v1.pdf)
6. 📄 [CPU $\times$ OS 软硬件协作边界桥梁手册](file:///Users/xpx/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/xpx/Documents/I.P.A.R.A/%E5%B7%A5%E4%BD%9C%E9%A2%86%E5%9F%9F/%E8%B5%84%E6%BA%90/common/%E8%80%83%E7%A0%94/OS_%E8%AE%A1%E7%BB%84%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98_CPU%E4%B8%8E%E5%86%85%E6%A0%B8%E8%BD%AF%E7%25A1%E5%25AD%E4%BD%9C%E8%BE%B9%E7%95%8C_v1.pdf)
7. 📄 [408 三科统一方法论手册（网络·计组·OS）](file:///Users/xpx/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/xpx/Documents/I.P.A.R.A/%E5%B7%A5%E4%BD%9C%E9%A2%86%E5%9F%9F/%E8%B5%84%E6%BA%90/common/%E8%80%83%E7%A0%94/408%E4%B8%89%E7%A7%91%E7%BB%9F%E4%B8%80%E6%96%B9%E6%B3%95%E8%AE%BA%E6%89%8B%E5%86%8C_%E7%BD%91%E7%BB%9C_%E8%AE%A1%E7%BB%84_OS_v1.pdf)
8. 📄 [OS 内核状态机与跨子系统推演综合手册](file:///Users/xpx/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/xpx/Documents/I.P.A.R.A/%E5%B7%A5%E4%BD%9C%E9%A2%86%E5%9F%9F/%E8%B5%84%E6%BA%90/common/%E8%80%83%E7%A0%94/OS_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98_%E5%86%85%E6%A0%B8%E7%8A%B6%E6%80%81%E6%9C%BA%E4%B8%8E%E8%B7%A8%E5%AD%90%E7%B3%BB%E7%BB%9F%E6%8E%A8%E6%BC%94%E6%96%B9%E6%B3%95%E8%AE%BA_v1.pdf)

---

## ⚡ 推荐学习与复习顺序

$$
\text{OS 基础五专题} \arr \text{CPU} \times \text{OS 桥梁} \arr \text{408 三科统一} \arr \text{内核状态机综合推演}
$$
