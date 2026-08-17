---
title: 动态内存、字符与输出
source: https://www.codebrick.tech/ds-full/posts/c-exam/memory-io.html
---

# 动态内存、字符与输出

动态内存和输入输出不是 408 代码题的主线。18 年真题里，核心答案真正需要动态辅助空间的典型题只有 2015·41 和 2018·41；字符输出集中在 2017·41 等少数题。

本篇的目标不是系统学习 C 标准库，而是避免少数用到它们的题出现致命错误。

## `malloc` 与 `calloc`

分配 n 个 `int`：c

```
int *B = (int *)malloc(n * sizeof(int));
```

分配 n 个并自动清零：c

```
int *B = (int *)calloc(n, sizeof(int));
```

标记数组通常依赖初值全 0，因此 `calloc` 更合适：c

```
char *mark = (char *)calloc(n + 1, sizeof(char));
if (mark == NULL) return -1;
```

`n+1` 是因为要使用下标 `0..n`。数组长度必须从实际最大下标反推，不能凭感觉写。

## 用完释放，释放后不再访问
c

```
int answer = n + 1;
/* 使用 mark 计算答案 */
free(mark);
return answer;
```

释放后不能再读取 `mark[i]`。链表删除同理：c

```
Node *temp = pre->next;
pre->next = temp->next;   /* 先读取并接好后继 */
free(temp);               /* 最后释放 */
```

卷面上漏写 `free` 通常不是整题归零，但写对只需一行；更严重的是先释放再访问，算法本身已经错误。

## 辅助空间不等于输入输出空间

题目给出的 `A` 和 `res` 不计入算法额外空间。下面函数即使写满整个 `res`，辅助空间仍可为 `O(1)`：c

```
void calMulMax(int A[], int res[], int n) {
    int curMax, curMin;   /* 只有常数个额外变量 */
    /* ... */
}
```

自己申请的 `mark[n+1]` 才计为 `O(n)` 辅助空间。

## 输出：按题面要求选最短方式

输出一个整数：c

```
printf("%d", value);
```

输出一个字符：c

```
putchar(ch);
```

输出结点中保存的字符串：c

```
printf("%s", root->data);
```

若题目只要求函数返回值，就不要额外 `printf`；若题面明确说“输出并返回 1”，两件事都要做。**返回和输出不是一回事。**

## 字符、字符数组和字符串
c

```
char op = '+';        /* 一个字符，用单引号 */
char word[10] = "+"; /* 字符串，用双引号 */
```

2017·41 的树结点使用 `char data[10]` 保存运算符或操作数，可以直接：c

```
printf("%s", root->data);
```

如果只是按遍历顺序输出表达式，没必要先拼出一个巨大字符串；递归过程中直接 `printf` 或 `putchar`，卷面更短，也避开缓冲区长度问题。

## `main`、`scanf` 为什么只出现在 Playground

Playground 必须有完整程序才能编译，所以练习代码会包含：c

```
int main(void) {
    /* 读取测试数据、调用目标函数、打印结果 */
    return 0;
}
```

这部分是测试壳，不是 408 答案。考试题已经通过函数参数给出数组、树或图，你只需要完成指定算法函数。主动补写输入和建表：

- 浪费时间；
- 引入无关错误；
- 让阅卷人更难找到真正答案。

## 立即写：标记数组与释放

只补完 `firstMissingPositive`。要求使用 `calloc`，只标记 `[1,n]` 内的值，并在返回前 `free`。默认输入答案为 `5`。

## 对应真题练习

- [2015·41 链表按绝对值去重](https://www.codebrick.tech/oj/problems/ds-2015-41-list-dedup-by-abs)：删除结点与标记数组。
- [2018·41 最小未出现正整数](https://www.codebrick.tech/oj/problems/ds-2018-41-min-missing-positive)：`calloc` 与范围过滤。
- [2017·41 表达式树转中缀](https://www.codebrick.tech/oj/problems/ds-2017-41-expr-tree-to-infix)：字符数组与递归输出。
- [2026·41 BST 最近关键字](https://www.codebrick.tech/oj/problems/ds-2026-41-bst-closest-key)：多个结果和并列输出。

## 本篇卷面检查

- 标记数组是否需要清零，应该用 `malloc` 还是 `calloc`？
- 分配长度能否覆盖最大合法下标？
- `free` 前是否已经保存所有仍需使用的信息？
- 题目要求的是返回、输出，还是二者都有？
- 是否把测试用的 `main/scanf` 误写进正式答案？

下一篇：[卷面答题模板与 18 题训练路线](./answering.html)。