# LeetCode 543 - Diameter of Binary Tree

---

## 🧠 Problem Summary | 题目概述

**EN:**  
Given the root of a binary tree, return the length of the diameter of the tree.  
The diameter is the length of the longest path between any two nodes in the tree.  
This path may or may not pass through the root.

**CN:**  
给定一棵二叉树的根节点，返回其直径长度。  
直径是树中任意两个节点之间的最长路径长度。  
该路径可以经过根节点，也可以不经过。

---

## ⚠️ Key Insight | 核心思路

**EN:**  
The diameter at any node = depth(left subtree) + depth(right subtree)  

We traverse every node and compute:
- left subtree depth
- right subtree depth
- update global maximum diameter

**CN：**  
任意节点的直径 = 左子树最大深度 + 右子树最大深度  

我们需要遍历每个节点，并计算：
- 左子树深度
- 右子树深度
- 更新全局最大直径

---

## ❌ Naive Approach (O(n²)) | 低效解法

**EN:**  
At each node, compute maxDepth separately → repeated calculations → O(n²)

**CN：**  
在每个节点重复计算 maxDepth，会导致大量重复计算 → 时间复杂度 O(n²)

---

## ✅ Optimal Approach (O(n)) | 最优解法

**EN:**  
Use one DFS traversal to:
- compute depth
- update diameter simultaneously

**CN：**  
通过一次 DFS：
- 同时计算深度
- 同时更新直径

---

## 🔁 Core Logic | 核心递归逻辑

**EN:**  
Post-order traversal (Left → Right → Node)

**CN：**  
后序遍历（左 → 右 → 当前节点）

---

## 💻 Code (Python)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        self.maxDiameter = 0
        
        def depth(node):
            if not node:
                return 0
            
            # 递归计算左右子树深度
            left = depth(node.left)
            right = depth(node.right)
            
            # 更新最大直径
            self.maxDiameter = max(self.maxDiameter, left + right)
            
            # 返回当前节点深度
            return 1 + max(left, right)
        
        depth(root)
        return self.maxDiameter
```

---

## 📊 Complexity | 复杂度分析

**Time Complexity:**  
O(n) → each node visited once  

**Space Complexity:**  
O(h) → recursion stack (tree height)

---

## 🔍 Example | 示例

```
        1
       / \
      2   3
     / \
    4   5
```

**Diameter = 3**  
Path: 4 → 2 → 1 → 3

---

## 🧩 Key Takeaways | 关键总结

**EN:**
- Diameter is NOT necessarily through root
- Combine depth calculation + diameter update in one recursion
- Avoid repeated depth computation

**CN：**
- 直径不一定经过根节点
- 深度计算 + 直径更新必须合并在一次递归中
- 避免重复计算 maxDepth

---

## 🚨 Common Mistakes | 常见错误

**EN:**
- Calculating depth separately → O(n²)
- Confusing diameter with height
- Forgetting global variable

**CN：**
- 单独计算 depth 导致 O(n²)
- 混淆“高度”和“直径”
- 忘记使用全局变量记录最大值

---

## 🧠 Pattern Recognition | 模式总结

**EN:**  
Tree DFS + Post-order traversal + Global state update  

**CN：**  
树 DFS + 后序遍历 + 全局变量更新

---

## 🔥 One-line Summary | 一句话总结

**EN:**  
Use DFS to compute depth and update diameter in one pass.

**CN：**  
用一次 DFS 同时计算深度并更新直径。
