# 🌳 LC 144 — Binary Tree Preorder Traversal

---

## 🧠 Problem Description（题目描述）

Given the root of a binary tree, return the **preorder traversal** of its nodes' values.

给定一个二叉树的根节点，返回它的**前序遍历结果**

---

## 📌 Preorder Definition（前序定义）

```text
Root → Left → Right
根 → 左 → 右
```

---

## 💻 Solution 1 — Recursive（递归）

### Code

```python
class Solution:
    def preorderTraversal(self, root):
        res = []

        def traverse(node):
            if not node:
                return
            
            # ✅ 前序位置（先处理当前节点）
            res.append(node.val)

            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return res
```

---

## 🧠 Key Insight（核心理解）

```text
Visit node → then go left → then go right
先访问当前节点 → 再左 → 再右
```

👉 当前节点处理位置决定是“前序”

---

## ⚠️ Common Mistakes（常见错误）

- ❌ 忘记 base case (`if not node`)
- ❌ 把 append 写错位置（会变成中序/后序）
- ❌ 不理解递归顺序

---

## 💻 Solution 2 — Iterative（迭代）

### Code

```python
class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)

            # ⚠️ 先 push 右，再 push 左
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res
```

---

## 🧠 Why push right first?（为什么先放右）

```text
Stack = LIFO（后进先出）
```

👉 为了让：
```text
Left 先被处理
```

所以：

```text
先压 right，再压 left
```

---

## 📊 Example（示例）

```
    1
     \
      2
     /
    3
```

### Output:

```text
[1, 2, 3]
```

---

## ⚖️ Recursive vs Iterative

| 方法 | 特点 |
|------|------|
| Recursive | 简洁，易理解 |
| Iterative | 更接近底层实现 |

---

## 📌 Complexity（复杂度）

- Time: `O(n)`
- Space: `O(n)`（递归栈 or 显式栈）

---

## 🎯 When to Use（什么时候用）

- Recursive → 面试优先（清晰）
- Iterative → 深入理解（加分）

---

## 🧠 Final Summary（总结）

```text
Preorder = Root first
前序 = 先处理当前节点

Recursive = 更直观
Iterative = 模拟栈结构
```

---

## 📌 One Sentence Takeaway

> Preorder traversal = process node before its children

> 前序遍历 = 在子节点之前处理当前节点
