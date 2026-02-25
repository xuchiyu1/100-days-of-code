# Two Pointer – Stable Partition Template

## 🧠 Pattern Overview

This template is used when:

- We need to modify the array **in-place**
- We want to move certain elements to the front
- We must **preserve relative order**
- We are doing a "filter / compression" operation

Examples:
- 26. Remove Duplicates from Sorted Array
- 27. Remove Element
- 283. Move Zeroes
- Move all even numbers to front
- Move all negatives to front

---

# 🎯 Core Idea

We divide the array logically into two parts:

[ Valid Area | Unprocessed Area ]

We use:

- `slow` → marks the boundary of valid elements
- `fast` → scans through the array

Whenever `nums[fast]` satisfies the condition,
we copy it to `nums[slow]` and move `slow` forward.

---

# 🔥 General Template

```python
slow = 0

for fast in range(len(nums)):
    if CONDITION(nums[fast]):
        nums[slow] = nums[fast]
        slow += 1
```

After loop:

- First `slow` elements are valid
- Remaining elements may need cleanup

---

# 📌 Example 1 – Remove Element

Problem:
Remove all occurrences of `val` in-place.

```python
slow = 0

for fast in range(len(nums)):
    if nums[fast] != val:
        nums[slow] = nums[fast]
        slow += 1

return slow
```

Here:
- `slow` represents number of valid elements.

---

# 📌 Example 2 – Move Zeroes

Move all non-zero elements to front, zeros to end.

```python
slow = 0

for fast in range(len(nums)):
    if nums[fast] != 0:
        nums[slow] = nums[fast]
        slow += 1

for i in range(slow, len(nums)):
    nums[i] = 0
```

---

# 📌 Example 3 – Move Even Numbers to Front

```python
slow = 0

for fast in range(len(nums)):
    if nums[fast] % 2 == 0:
        nums[slow] = nums[fast]
        slow += 1
```

---

# 🧠 What Does `slow` Represent?

`slow` always means:

> The number of elements that satisfy the condition  
> Or the next position to write a valid element

It is the boundary of the "valid region".

---

# 🔍 Why This Works

- `fast` scans every element once → O(n)
- `slow` builds the front part gradually
- No extra array needed → O(1) space

---

# ⚠️ Important Notes

This is called:

**Stable Partition**

Because the relative order of valid elements is preserved.

This differs from the two-pointer swap method used in quicksort partition.

---

# ⏱ Complexity

Time Complexity: O(n)  
Space Complexity: O(1)

---

# 🚀 Pattern Recognition Rule

If you see:

- In-place modification
- Keep order
- Remove / filter / compress elements

Think:

→ Stable Two Pointer Template

---

# 🧩 Mental Model

Imagine the array as:

Before:

[ ?, ?, ?, ?, ?, ? ]

After scanning:

[ valid, valid, valid | unknown, unknown ]

`slow` moves forward as valid elements are found.

---

# 📚 Summary

This template applies to many array problems.

Mastering it reduces complexity of:

- Filtering problems
- Compression problems
- In-place modification problems

---

# End
