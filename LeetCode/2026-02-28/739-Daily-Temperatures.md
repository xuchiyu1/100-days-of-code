# LeetCode 739 – Daily Temperatures  
# 每日温度（单调栈）

---

## 🧩 Problem Description  
## 题目描述

Given an array of daily temperatures, return an array `answer` such that:

`answer[i]` is the number of days you have to wait after day i to get a warmer temperature.

If there is no future day for which this is possible, keep `answer[i] = 0`.

给定一个温度数组，返回每一天需要等待多少天才能遇到更高温度。  
如果之后没有更高温度，则为 0。

---

## 🎯 Core Idea  
## 核心思路

This is a classic **Next Greater Element** problem.

We use a **monotonic decreasing stack** to solve it in O(n) time.

这是典型的“下一个更大元素”问题。  
使用单调递减栈可以在线性时间解决。

---

## 🧠 Algorithm Steps  
## 算法步骤

1. Initialize result array with zeros.  
2. Use a stack to store indices.  
3. Traverse the array.  
4. While current temperature is greater than stack top temperature:
   - Pop index
   - Calculate difference
5. Push current index into stack.

1. 初始化结果数组  
2. 栈存索引  
3. 遍历数组  
4. 当前温度更高时弹栈并计算距离  
5. 入栈当前索引  

---

## ✅ Python Implementation

```python
class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        n = len(temperatures)
        ans = [0] * n
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        
        return ans
```

---

## ⏱ Complexity  
## 时间复杂度

Time: O(n)  
Space: O(n)

Each index is pushed and popped at most once.

每个索引最多入栈一次，出栈一次。

---

## 🔥 Key Insight  
## 关键理解

We store indices, not temperatures, because:

- We need to compute distance
- Duplicate temperatures must be handled separately

栈里存索引而不是温度，因为：

- 要计算天数差
- 可能有重复温度

---

## 📌 Pattern Used  
## 使用的算法模式

Monotonic Stack (Next Greater Element)

单调栈（寻找右侧第一个更大元素）

---

# End
