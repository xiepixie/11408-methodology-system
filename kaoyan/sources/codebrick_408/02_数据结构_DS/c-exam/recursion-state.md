---
title: 递归与状态传递
source: https://www.codebrick.tech/ds-full/posts/c-exam/recursion-state.html
---

# 递归与状态传递

408 不会抽象地问“什么是递归”，而是给一棵树，让你求和、输出、判定。递归只是把“处理一棵树”拆成“处理根、左子树、右子树”的 C 表达方式。

历年最典型的三道题：2014·41 二叉树 WPL、2017·41 表达式树转中缀、2022·41 顺序存储二叉树判 BST。

## 每个递归函数只回答三个问题

- 什么情况立即结束？
- 当前结点做什么？
- 子问题的结果怎样交回来？

统计叶结点的模板：c

```
int countLeaves(TreeNode *root) {
    if (root == NULL) return 0;   /* ① 空树出口 */

    if (root->left == NULL && root->right == NULL)
        return 1;                 /* ② 当前结点是叶子 */

    return countLeaves(root->left)
         + countLeaves(root->right);  /* ③ 合并子问题 */
}
```

这四行已经包含大多数树题所需的递归语法。

## 出口要覆盖“空”和“命中”

最基本的出口是空树：c

```
if (root == NULL) return 0;
```

但题目可能还有提前结束条件，例如发现不合法后不必继续：c

```
if (root == NULL || !ok) return;
```

叶结点判定必须是左右孩子**都空**：c

```
root->left == NULL && root->right == NULL
```

写成 `||` 会把只有一个孩子的中间结点误判成叶子。

## 用返回值合并子树结果

2014·41 求 WPL，可以让函数直接返回当前子树的贡献：c

```
int wplDfs(TreeNode *root, int depth) {
    if (root == NULL) return 0;

    if (root->left == NULL && root->right == NULL)
        return root->weight * depth;

    return wplDfs(root->left, depth + 1)
         + wplDfs(root->right, depth + 1);
}
```

`depth` 是从父问题传给子问题的状态，返回值是子问题交回父问题的答案。两条方向相反，不要混在一个全局变量里。

## 访问语句的位置决定遍历顺序
c

```
void traverse(TreeNode *root) {
    if (root == NULL) return;

    visit(root);              /* 前序 */
    traverse(root->left);
    /* visit(root); */        /* 中序 */
    traverse(root->right);
    /* visit(root); */        /* 后序 */
}
```

2017·41 表达式树要按中序输出，因此操作符输出放在左右递归之间。括号则在进入、离开非根表达式时输出。

不要背三份完整代码，只记一份骨架和 `visit` 的三个位置。

## `void` 递归：状态放在哪里

有时递归不直接返回最终答案，而是修改状态：c

```
void inorder(TreeNode *root, int *prev, int *hasPrev, int *ok) {
    if (root == NULL || !*ok) return;

    inorder(root->left, prev, hasPrev, ok);

    if (*hasPrev && root->data <= *prev) {
        *ok = 0;
        return;
    }
    *prev = root->data;
    *hasPrev = 1;

    inorder(root->right, prev, hasPrev, ok);
}
```

这里用指针参数让所有递归层共享 `prev` 和 `ok`。也可以使用少量全局变量，但要在外层函数每次调用前重新初始化：c

```
static int prevValue;
static int hasPrev;
static int ok;

int isBST(Tree T) {
    hasPrev = 0;
    ok = 1;
    inorderCheck(T, 0);
    return ok;
}
```

卷面两种写法都能判分。指针参数更显式，全局变量更短；关键是初始化和语义一致。

## 顺序存储树：递归的不是指针，而是下标

若根结点在下标 `i`，按 0-based 顺序存储：c

```
left  = 2 * i + 1;
right = 2 * i + 2;
```

出口同时检查数组边界和空结点标记：c

```
if (i >= T.ElemNum || T.SqBiTNode[i] == -1) return;
```

递归主体仍然是“左—当前—右”，只是参数从 `TreeNode *` 换成了整数下标。

## 递归空间复杂度不要漏栈

递归代码即使没有 `malloc`，也会占用调用栈：

- 平衡树递归深度约为 `O(log n)`；
- 极端单支树递归深度为 `O(n)`；
- 因此一般写辅助空间 `O(h)`，`h` 为树高。

若题目只要求时间复杂度，也可不展开空间；一旦问空间，不能因为“没开数组”就写 `O(1)`。

## 立即写：统计叶结点

只补完 `countLeaves`。测试树有三个叶结点 4、5、3，正确输出为 `3`。

写完后思考：若把叶结点条件里的 `&&` 改成 `||`，这棵测试树为什么可能暂时看不出所有错误？考试时要主动补“只有一个孩子”的树进行脑测。

## 改错：`&&` 写成 `||` 会漏数

下面这段就把叶子判定写成了 `||`。测试树里根结点只有左孩子，真实叶子是 3 和 4 两个，但它会输出 `1`。只改一个字符让它输出 `2`，然后想清楚：为什么“只有一个孩子”的结点是这个 bug 唯一暴露得出来的地方。

## 对应真题练习

- [2014·41 二叉树 WPL](https://www.codebrick.tech/oj/problems/ds-2014-41-binary-tree-wpl)
- [2017·41 表达式树转中缀](https://www.codebrick.tech/oj/problems/ds-2017-41-expr-tree-to-infix)
- [2022·41 顺序存储判 BST](https://www.codebrick.tech/oj/problems/ds-2022-41-bst-validate-array)

## 本篇卷面检查

- 空树出口是否写在任何 `root->...` 之前？
- 叶结点条件是否为左右孩子都空？
- 当前结点的工作放在前序、中序还是后序位置？
- 向下传的是状态，向上返回的是答案，是否混淆？
- 共享状态是否在外层函数中初始化？
- 空间复杂度是否计入递归栈 `O(h)`？

下一篇：[动态内存、字符与输出](./memory-io.html)。