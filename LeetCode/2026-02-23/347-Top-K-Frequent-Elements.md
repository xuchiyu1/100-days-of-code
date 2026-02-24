# LeetCode 347 – Top K Frequent Elements

## 🧩 Problem

Given an integer array `nums` and integer `k`,
return the `k` most frequent elements.

---

## 🎯 Core Idea

1. Count frequency of each number.
2. Use bucket sort (frequency as index).
3. Traverse from highest frequency to lowest.

---

## 🧠 Step-by-Step Thinking

Example:

nums = [4,4,4,6,6,7]  
k = 2

Frequency:

4 → 3  
6 → 2  
7 → 1  

Bucket structure:

index = frequency

bucket[1] = [7]  
bucket[2] = [6]  
bucket[3] = [4]  

Traverse from high to low:

3 → 4  
2 → 6  

Answer: [4,6]

---

## ✅ Code (Bucket Version)

```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        res = []

        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
```

---

## 🔍 Key Concepts

Counter(nums)  
→ counts frequency automatically

buckets = [[] for _ in range(n+1)]  
→ creates empty buckets

range(n, 0, -1)  
→ iterate from high frequency to low

---

## 🧠 Algorithm Pattern

This problem uses:

1. Counting Pattern
2. Bucket Sort Pattern
3. Accumulator Pattern

---

## ⏱ Complexity

Time: O(n)  
Space: O(n)

---

## 📌 Why Not Sort?

Sorting would be:

O(n log n)

Bucket approach avoids sorting.

---

## 💡 Reflection

This problem trains:

- Frequency counting
- Using index as classification tool
- Space-for-time optimization
