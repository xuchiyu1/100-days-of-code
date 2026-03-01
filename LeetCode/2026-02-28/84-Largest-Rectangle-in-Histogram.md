# LeetCode 84 – Largest Rectangle in Histogram  
# 柱状图中最大的矩形（单调栈详解）

---

## 🧩 Problem Description

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

给定一个整数数组 `heights` 表示直方图中各柱子的高度（每个柱子宽度为 1），求能构成的最大矩形面积。

---

## 🎯 Core Idea

Use a **monotonic increasing stack** of indices.

For each bar `i`, find:
- `left[i]` → index of the first smaller bar on the left
- `right[i]` → index of the first smaller bar on the right

Then:

```
width = right[i] - left[i] - 1
area = heights[i] * width
```

使用单调递增栈：
- 找左边第一个更小的柱子
- 找右边第一个更小的柱子
- 根据边界计算最大面积

---

## 🧠 Implementation

```python
class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        stack = []

        # Compute left boundary
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []

        # Compute right boundary
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        # Compute max area
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            max_area = max(max_area, heights[i] * width)

        return max_area
```

---

# 📊 Step-by-Step Example

Input:

```
[2,1,5,6,2,3]
```

---

## Step 1 – Compute left boundary

After left pass:

```
left = [-1, -1, 1, 2, 1, 4]
```

Meaning:
- For index 2 (height 5), left boundary is 1 (height 1)
- For index 4 (height 2), left boundary is 1

---

## Step 2 – Compute right boundary

After right pass:

```
right = [1, 6, 4, 4, 6, 6]
```

Meaning:
- For index 2, right boundary is 4 (height 2)

---

## Step 3 – Compute area

For index 2:

```
width = 4 - 1 - 1 = 2
area = 5 × 2 = 10
```

Maximum area = **10**

---

## ⏱ Complexity

Time: O(n)  
Space: O(n)

Each index is pushed and popped at most once.

---

## 🔥 Key Insights

- Stack stores indices, not heights.
- `>=` ensures correct handling of equal heights.
- Width formula comes from exclusive boundaries.

---

# End
