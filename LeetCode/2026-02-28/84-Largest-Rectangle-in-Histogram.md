# LeetCode 84 — Largest Rectangle in Histogram  
# 柱状图中最大的矩形（超详细逐步推演版）

---

# 1️⃣ 题目

给定一个整数数组 `heights`，表示直方图中每个柱子的高度（每个柱子宽度为 1），返回直方图中能够形成的最大矩形面积。

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

---

# 2️⃣ 输入示例

```
heights = [2, 1, 5, 6, 2, 3]
```

我们将用这个示例 **完整跑一遍算法的每一步**。

---

# 3️⃣ 核心思想（零基础解释）

对于任意一个柱子 i：

如果我们知道：

- 它左边第一个比它小的柱子位置
- 它右边第一个比它小的柱子位置

那么：

```
width = 右边界 - 左边界 - 1
area = height[i] * width
```

我们对所有柱子计算面积，取最大值。

---

# 4️⃣ 为什么用单调栈？

我们要找：

- 左边第一个更小的柱子
- 右边第一个更小的柱子

如果暴力找，会是 O(n²)。

单调栈可以：

- 每个元素最多入栈一次
- 每个元素最多出栈一次
- 总复杂度 O(n)

---

# 5️⃣ 完整代码

```python
class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        stack = []

        # Step 1: compute left boundary
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        # Step 2: compute right boundary
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        # Step 3: compute max area
        area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = max(area, width * heights[i])

        return area
```

---

# 6️⃣ Step 1 — 逐步计算 left 数组

初始化：

```
left  = [-1, -1, -1, -1, -1, -1]
stack = []
```

---

## i = 0, height = 2

stack 为空

while 不执行

left[0] 保持 -1

push 0

stack = [0]

---

## i = 1, height = 1

stack = [0]

判断：
heights[0] = 2 >= 1 ✔

pop 0

stack = []

while 结束

left[1] = -1

push 1

stack = [1]

---

## i = 2, height = 5

stack = [1]

判断：
heights[1] = 1 >= 5 ❌

left[2] = 1

push 2

stack = [1,2]

---

## i = 3, height = 6

stack = [1,2]

heights[2] = 5 >= 6 ❌

left[3] = 2

push 3

stack = [1,2,3]

---

## i = 4, height = 2

stack = [1,2,3]

判断：
heights[3] = 6 >= 2 ✔ pop 3
stack = [1,2]

heights[2] = 5 >= 2 ✔ pop 2
stack = [1]

heights[1] = 1 >= 2 ❌

left[4] = 1

push 4

stack = [1,4]

---

## i = 5, height = 3

stack = [1,4]

heights[4] = 2 >= 3 ❌

left[5] = 4

push 5

stack = [1,4,5]

---

最终：

```
left = [-1, -1, 1, 2, 1, 4]
```

---

# 7️⃣ Step 2 — 逐步计算 right 数组

初始化：

```
right = [6,6,6,6,6,6]
stack = []
```

---

## i = 5, height = 3

stack 为空

right[5] = 6

push 5

stack = [5]

---

## i = 4, height = 2

stack = [5]

heights[5] = 3 >= 2 ✔ pop 5
stack = []

right[4] = 6

push 4

stack = [4]

---

## i = 3, height = 6

stack = [4]

heights[4] = 2 >= 6 ❌

right[3] = 4

push 3

stack = [4,3]

---

## i = 2, height = 5

stack = [4,3]

heights[3] = 6 >= 5 ✔ pop 3
stack = [4]

heights[4] = 2 >= 5 ❌

right[2] = 4

push 2

stack = [4,2]

---

## i = 1, height = 1

stack = [4,2]

heights[2] = 5 >= 1 ✔ pop 2
stack = [4]

heights[4] = 2 >= 1 ✔ pop 4
stack = []

right[1] = 6

push 1

stack = [1]

---

## i = 0, height = 2

stack = [1]

heights[1] = 1 >= 2 ❌

right[0] = 1

push 0

stack = [1,0]

---

最终：

```
right = [1, 6, 4, 4, 6, 6]
```

---

# 8️⃣ Step 3 — 计算面积

公式：

```
width = right[i] - left[i] - 1
area  = height[i] * width
```

---

## i = 2（高度 5）

```
left[2]  = 1
right[2] = 4

width = 4 - 1 - 1 = 2
area  = 5 × 2 = 10
```

---

# 9️⃣ 所有面积计算表

| i | height | left | right | width | area |
|---|--------|------|-------|-------|------|
| 0 | 2 | -1 | 1 | 1 | 2 |
| 1 | 1 | -1 | 6 | 6 | 6 |
| 2 | 5 | 1 | 4 | 2 | 10 |
| 3 | 6 | 2 | 4 | 1 | 6 |
| 4 | 2 | 1 | 6 | 4 | 8 |
| 5 | 3 | 4 | 6 | 1 | 3 |

最大面积 = **10**

---

# 🔟 关键理解

- stack 存索引
- pop 表示该柱子已找到边界
- >= 是为了合并相同高度
- 每个元素最多入栈一次出栈一次
- 时间复杂度 O(n)

---

# 结束

这份文件是完整逐步可复习版本。
