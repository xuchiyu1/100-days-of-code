# Algorithm Templates Collection

This document summarizes core algorithm templates learned so far.

The goal is not to memorize problems, but to recognize reusable patterns.

---

# 1️⃣ Stable Two-Pointer (Compression Pattern)

## When to Use
- Remove elements
- Remove duplicates
- Move zeroes
- Partition by condition
- In-place modification with order preserved

## Template

```python
slow = 0

for fast in range(len(nums)):
    if CONDITION(nums[fast]):
        nums[slow] = nums[fast]
        slow += 1

# Optional cleanup step
for i in range(slow, len(nums)):
    nums[i] = FILL_VALUE
```

## Key Idea
- `slow` marks the boundary of valid elements.
- `fast` scans through the array.
- Preserves relative order (stable partition).

Time Complexity: O(n)  
Space Complexity: O(1)

---

# 2️⃣ Two-Pointer (Opposite Ends)

## When to Use
- Sorted arrays
- Two Sum II
- 3Sum
- Pair-based problems

## Template

```python
nums.sort()
left = 0
right = len(nums) - 1

while left < right:
    total = nums[left] + nums[right]

    if total == target:
        # process result
        left += 1
        right -= 1
    elif total < target:
        left += 1
    else:
        right -= 1
```

## Key Idea
- Requires sorted array.
- Moves inward based on comparison.
- Efficient for sum problems.

Time Complexity: O(n) per layer

---

# 3️⃣ Sliding Window (Fixed Size)

## When to Use
- Substring matching
- Anagram detection
- Fixed-length window problems

## Template

```python
# initialize window
for i in range(k):
    update_window()

# check initial window
check_condition()

# slide window
for i in range(k, len(arr)):
    remove_left()
    add_right()
    check_condition()
```

## Key Idea
- Window size is constant.
- Update incrementally instead of recomputing.
- Often used with frequency arrays.

Time Complexity: O(n)

---

# 4️⃣ Sliding Window (Variable Size)

## When to Use
- Longest substring problems
- Minimum window substring
- Dynamic interval problems

## Template

```python
left = 0

for right in range(len(s)):
    expand_window()

    while condition_invalid:
        shrink_window()
        left += 1

    update_answer()
```

## Key Idea
- Window grows and shrinks dynamically.
- Maintains a valid condition.

Time Complexity: O(n)

---

# 5️⃣ Double Hash Map (Bijection Pattern)

## When to Use
- Isomorphic strings
- Word pattern
- One-to-one mapping problems

## Template

```python
map1 = {}
map2 = {}

for a, b in zip(s, t):
    if a in map1 and map1[a] != b:
        return False
    if b in map2 and map2[b] != a:
        return False

    map1[a] = b
    map2[b] = a
```

## Key Idea
- Enforces bidirectional uniqueness.
- Prevents many-to-one mappings.

Time Complexity: O(n)

---

# 6️⃣ Frequency Counting Pattern

## When to Use
- Majority element
- Top K frequent
- Character counting
- Duplicate detection

## Template

```python
count = {}

for x in nums:
    count[x] = count.get(x, 0) + 1
```

## Key Idea
- Use dictionary for counting.
- Efficient O(n) frequency tracking.

---

# 7️⃣ Bucket Sort Pattern

## When to Use
- Top K frequent elements
- Frequency-based grouping

## Template

```python
buckets = [[] for _ in range(n + 1)]

for num, freq in count.items():
    buckets[freq].append(num)

res = []
for i in range(n, 0, -1):
    for num in buckets[i]:
        res.append(num)
```

## Key Idea
- Frequency acts as index.
- Avoids full sorting.
- Space-for-time optimization.

Time Complexity: O(n)

---

# 8️⃣ Greedy Pattern

## When to Use
- Best Time to Buy and Sell Stock
- Interval scheduling
- Local optimal → global optimal problems

## Template

```python
min_value = float('inf')
best = 0

for x in nums:
    min_value = min(min_value, x)
    best = max(best, x - min_value)
```

## Key Idea
- Maintain best local state.
- Update answer incrementally.

Time Complexity: O(n)

---

# 9️⃣ Binary Search

## When to Use
- Sorted arrays
- Searching boundaries
- Logarithmic search problems

## Template

```python
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

Time Complexity: O(log n)

---

# 🔟 Backtracking

## When to Use
- Permutations
- Combinations
- Subsets
- Search all possible solutions

## Template

```python
def backtrack(path, choices):
    if base_condition:
        result.append(path[:])
        return

    for choice in choices:
        path.append(choice)
        backtrack(path, updated_choices)
        path.pop()
```

Time Complexity: Exponential

---

# 1️⃣1️⃣ Monotonic Stack

## When to Use
- Next greater element
- Daily temperatures
- Stock span
- Range maximum problems

## Template

```python
stack = []

for i in range(len(nums)):
    while stack and CONDITION:
        index = stack.pop()
        # update result

    stack.append(i)
```

Time Complexity: O(n)

---

# Final Notes

Mastering patterns is more powerful than memorizing individual problems.

Recognize the structure → Apply the template → Adjust conditions.

Algorithm learning is about pattern abstraction.
