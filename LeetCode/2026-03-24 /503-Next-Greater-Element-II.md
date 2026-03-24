# 503-Next-Greater-Element-II.md

## 📅 Date
2026-03-24

## 📂 Path
100-days-of-code / LeetCode / 2026-03-24 / 503-Next-Greater-Element-II.md

---

# 🧩 Problem
Next Greater Element II (Circular Array)

---

# ❓ My Questions (复习重点问题)

1. 为什么要遍历两轮？
2. i 和 n 分别代表什么？
3. 为什么只有 i < n 才写答案？
4. 第一轮到底在做什么？
5. 为什么第二轮才能找到答案？
6. 第一轮是不是只能看到一部分信息？

---

# 🧠 Step-by-Step Explanation（完整理解流程）

---

## 1️⃣ 题目本质

### 中文
给定一个循环数组 nums，对于每个元素，找到它右边第一个更大的数，如果不存在返回 -1。

### English
Given a circular array, find the next greater element for each number.

---

## 2️⃣ 为什么难（核心点）

普通数组：
只看右边

循环数组：
右边 = 后面 + 开头

---

## 3️⃣ 为什么要遍历两轮（Q1）

结论：

遍历两轮 = 模拟 nums + nums

---

举例：

nums = [1, 2, 1]

最后一个 1：

正常右边：没有  
循环后：可以看到前面的 2

---

如果只遍历一轮：

看不到数组开头 → 结果错误

---

所以：

必须遍历 2n → 才能看到完整一圈

---

## 4️⃣ i 和 n 是什么（Q2）

n = len(nums)

👉 n 表示原数组长度

---

for i in range(2*n-1, -1, -1):

👉 i 是“扩展索引”，用于模拟两倍数组

---

映射关系：

i → i % n → nums[i % n]

例如：

i=5 → nums[2]  
i=4 → nums[1]  
i=3 → nums[0]  
i=2 → nums[2]  
i=1 → nums[1]  
i=0 → nums[0]

---

## 5️⃣ 为什么 i < n 才写答案（Q3）

res = [-1] * n

👉 res 只存原数组结果

---

if i < n:
    res[i] = ...

👉 只有 i 在 0~n-1 时才是“真实位置”

---

本质：

i 是扩展索引  
res 只属于原数组

---

## 6️⃣ 第一轮到底做了什么（Q4）

核心结论：

第一轮 ≠ 找答案  
第一轮 = 构建“完整右侧信息”

---

具体做的事情：

while stack and curr >= stack[-1]:
    stack.pop()

---

作用：

删除所有“不可能成为答案”的元素

---

最终效果：

构建一个“干净的候选集合”（单调递减栈）

---

## 7️⃣ 为什么第二轮才能找答案（Q5）

因为：

第二轮时，栈已经包含：

“完整右侧信息（包括循环部分）”

---

举例：

nums = [1, 2, 1]

处理最后一个 1 时：

第一轮结束后：

stack = [2, 1]

---

经过处理：

pop 1 → stack = [2]

答案：

2 ✅

---

如果没有第一轮：

stack = []

结果：

-1 ❌

---

## 8️⃣ 第一轮是不是只能看到一部分（Q6）

错误理解：

第一轮只能看到末尾

---

正确理解：

第一轮是在“构建整个右侧世界”

---

一句话总结：

第一轮：准备未来  
第二轮：使用未来

---

## 9️⃣ 单调栈核心逻辑

while stack and curr >= stack[-1]:
    stack.pop()

---

作用：

保证栈是单调递减

---

含义：

栈顶 = 最近的更大元素

---

## 🔟 完整代码

class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        stack = []
        res = [-1] * n

        for i in range(2*n-1, -1, -1):
            curr = nums[i % n]

            while stack and curr >= stack[-1]:
                stack.pop()

            if i < n:
                res[i] = stack[-1] if stack else -1

            stack.append(curr)

        return res

---

# 🧠 最终总结（必须记住）

1. 单调栈：存候选答案（递减）
2. 从右往左：保证右侧信息已准备好
3. 两轮遍历：解决循环数组
4. 第一轮：构建未来（填栈）
5. 第二轮：计算答案

---

# 🧩 一句话总结

两轮遍历 + 单调栈  
= 让每个元素看到完整循环右侧  
= 得到正确答案

---

# 🔁 复习提示（考前快速看）

看到：

- Next Greater
- Circular Array

立即想到：

单调栈 + 从右往左 + 遍历2n
