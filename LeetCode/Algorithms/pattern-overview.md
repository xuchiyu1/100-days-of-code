# Algorithm Pattern Overview

This document summarizes core algorithm patterns learned so far.

---

# 1️⃣ Stable Two-Pointer (Compression Pattern)

## Used For:
- Remove Duplicates (26)
- Remove Element (27)
- Move Zeroes (283)
- Partition by condition (even, negative, etc.)

## Template:

```python
slow = 0

for fast in range(len(nums)):
    if CONDITION(nums[fast]):
        nums[slow] = nums[fast]
        slow += 1
```

## Key Idea:
- `slow` marks the boundary of valid elements.
- `fast` scans the array.
- Maintains relative order.

Time Complexity: O(n)  
Space Complexity: O(1)

---

# 2️⃣ Two-Pointer Opposite Ends

## Used For:
- 3Sum (15)
- Two Sum II (sorted)
- Pair problems in sorted arrays

## Template:

```python
left = 0
right = len(nums) - 1

while left < right:
    if condition:
        left += 1
    else:
        right -= 1
```

## Key Idea:
- Requires sorted array.
- Moves inward from both ends.
- Used for sum-based problems.

Time Complexity: O(n) per iteration layer.

---

# 3️⃣ Sliding Window (Fixed Size)

## Used For:
- Longest Substring Without Repeating Characters (3)
- Find All Anagrams (438)

## Template:

```python
initialize window

for right in range(len(s)):
    update window

    while condition violated:
        shrink window

    update answer
```

## Key Idea:
- Maintain window state.
- Update incrementally instead of recomputing.

Time Complexity: O(n)

---

# 4️⃣ Hash Map Mapping Pattern

## Used For:
- Isomorphic Strings (205)
- Word Pattern (290)

## Template:

```python
map1 = {}
map2 = {}

for a, b in zip(s, t):
    if conflict:
        return False
```

## Key Idea:
- Enforce one-to-one mapping.
- Double hash map ensures bijection.

Time Complexity: O(n)

---

# 5️⃣ Frequency Counting Pattern

## Used For:
- Majority Element (169)
- Top K Frequent (347)

## Template:

```python
count = {}

for x in nums:
    count[x] = count.get(x, 0) + 1
```

---

# 6️⃣ Bucket Sort Pattern

## Used For:
- Top K Frequent Elements (347)

## Template:

```python
buckets = [[] for _ in range(n+1)]

for num, freq in count.items():
    buckets[freq].append(num)
```

Time Complexity: O(n)

---

# 7️⃣ Greedy Pattern

## Used For:
- Best Time to Buy and Sell Stock (121)

## Template:

```python
min_price = float('inf')
max_profit = 0

for price in prices:
    min_price = min(min_price, price)
    max_profit = max(max_profit, price - min_price)
```

---

# Summary

These patterns form the foundation of:
- Array manipulation
- Hash-based problems
- Window-based substring problems
- Partitioning logic
- Frequency analysis

Mastering patterns is more important than memorizing individual problems.
