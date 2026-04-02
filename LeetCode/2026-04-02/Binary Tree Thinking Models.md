# 🌳 Binary Tree Thinking Models（树的两种核心思维）

---

## 🧠 Overview（总览）

When solving binary tree problems, there are **two fundamental thinking patterns**:

1. **Divide & Conquer（分解问题）**
2. **Traversal（遍历）**

👉 Mastering both is essential for LeetCode and technical interviews.

---

# ① Divide & Conquer（分解问题）

## 📌 Core Idea（核心思想）

> “Assume subproblems are already solved, and use their results to build the solution.”

> 「假设子问题已经解决，我只需要利用结果来组合答案」

---

## 🧠 Function Definition（函数定义）

For a function like:

```python
def invertTree(root):
```

We define it as:

```text
Given a root node, return the inverted tree rooted at this node
给定一个节点 root，返回以它为根的翻转后的二叉树
```

---

## 💻 Example (LC 226 - Invert Binary Tree)

```python
def invertTree(root):
    if root is None:
        return None

    left = invertTree(root.left)
    right = invertTree(root.right)

    root.left = right
    root.right = left

    return root
```

---

## 🔍 Step-by-Step Understanding（逐步理解）

1. 递归调用 `invertTree(root.left)`  
   👉 左子树已经被翻转完成

2. 递归调用 `invertTree(root.right)`  
   👉 右子树已经被翻转完成

3. 当前节点交换左右子树  
   👉 完成当前节点的翻转

---

## 🧠 Key Insight（核心理解）

```text
Subtrees solve themselves → I combine results
子树自己解决 → 我负责拼接
```

👉 你只关心：
- 子树结果是什么
- 如何组合

---

## 📊 Characteristics（特点）

| Feature | Description |
|--------|------------|
| 思维方式 | 利用子问题结果 |
| 英文 | Use subproblem results |
| 是否有返回值 | 有 |
| 关注点 | return |
| 难度 | 较抽象 |
| 使用场景 | 树DP / 深度 / 路径问题 |

---

## ✅ Typical Problems（适用题目）

- 104. Maximum Depth of Binary Tree  
- 543. Diameter of Binary Tree  
- Path Sum 系列  
- Tree DP

---

# ② Traversal（遍历）

## 📌 Core Idea（核心思想）

> “Visit every node and perform an operation”

> 「遍历每个节点，在每个节点做一件事」

---

## 🧠 Function Definition（函数定义）

```text
Visit each node and perform an action
遍历整棵树，对每个节点执行操作
```

---

## 💻 Example (LC 226 - Invert Binary Tree)

```python
def invertTree(root):
    def traverse(node):
        if node is None:
            return
        
        # 对当前节点操作
        node.left, node.right = node.right, node.left

        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return root
```

---

## 🔍 Step-by-Step Understanding（逐步理解）

1. 到达一个节点  
2. 交换它的左右子树  
3. 递归处理左右子节点  

👉 每个节点都被“访问并处理”

---

## 🧠 Key Insight（核心理解）

```text
I visit every node → I do something at each node
我走到每个节点 → 在这里做操作
```

---

## 📊 Characteristics（特点）

| Feature | Description |
|--------|------------|
| 思维方式 | 遍历所有节点 |
| 英文 | Visit all nodes |
| 是否有返回值 | 通常没有 |
| 关注点 | 过程 |
| 难度 | 更直观 |
| 使用场景 | 修改 / 打印 / 统计 |

---

## ✅ Typical Problems（适用题目）

- 226. Invert Binary Tree  
- 144 / 94 / 145（遍历）  
- Count nodes  
- Sum of nodes  

---

# ⚖️ Comparison（核心对比）

| Aspect | Divide & Conquer | Traversal |
|--------|-----------------|-----------|
| 思维方式 | 子问题解决 | 遍历每个节点 |
| 英文 | Use subproblems | Visit nodes |
| Return | 有返回值 | 通常无返回 |
| Focus | 结果 | 过程 |
| 难度 | 抽象 | 直观 |
| 面试常见 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

---

# 🎯 When to Use Which？（什么时候用哪种）

## ✅ 使用 Traversal（遍历）：

```text
当你需要对每个节点做操作
When you need to operate on every node
```

Examples：
- 修改树结构
- 打印节点
- 统计数量

---

## ✅ 使用 Divide & Conquer（分解）：

```text
当你需要子树的计算结果
When you need results from subtrees
```

Examples：
- 树的深度
- 路径问题
- Tree DP

---

# ⚠️ Important Insight（重要认知）

> ❗不是所有题都能两种方法都用

- 有些题必须用分解（如最大深度）
- 有些题两种都可以（如226）

---

# 🧠 Final Summary（终极总结）

```text
Traversal = I go and do things
遍历 = 我主动做事

Divide & Conquer = Let subproblems do the work
分解 = 让子问题帮我做
```

---

# 🚀 Learning Strategy（学习建议）

For beginners：

```text
1. 先掌握 Traversal（更直观）
2. 再理解 Divide & Conquer（更抽象但更强）
```

---

# 📌 One Sentence Takeaway（一句话总结）

> These are not competing methods — they are two perspectives of thinking about trees.

> 这不是两种对立方法，而是看待二叉树的两种视角
