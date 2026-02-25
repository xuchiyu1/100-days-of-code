# LeetCode 283 – Move Zeroes

## 🧩 Problem

Given an integer array `nums`, move all `0`s to the end of it while maintaining the relative order of the non-zero elements.

You must do this in-place without making a copy of the array.

Example:

Input:
[0,1,0,3,12]

Output:
[1,3,12,0,0]

---

# 🎯 Core Idea

We do NOT delete elements.

We compress all non-zero elements to the front,
then fill the remaining positions with zero.

This is a classic **Stable Two-Pointer Partition** problem.

---

# 🧠 Step-by-Step Thinking

### Step 1 – Understand the structure

We want:

[ Non-zero area | Zero area ]

We use:

- `slow` → next position to place non-zero
- `fast` → scans through the array

---

### Step 2 – Move non-zero elements forward

When we see a non-zero:

- Copy it to nums[slow]
- Increase slow

This compresses all non-zero values to the front.

---

### Step 3 – Fill remaining positions with zero

After the first loop:

- First `slow` elements are valid non-zero
- The rest must become zero

---

# ✅ Code

```python
class Solution:
    def moveZeroes(self, nums):
        slow = 0

        # Step 1: Move non-zero elements forward
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1

        # Step 2: Fill remaining positions with zero
        for i in range(slow, len(nums)):
            nums[i] = 0
```

---

# 🔍 Key Variables Explained

`slow`:
- Represents the number of non-zero elements found so far
- Marks the boundary of the valid region

`fast`:
- Scans every element
- Finds valid elements

---

# 🧠 Why This Works

We never disturb the relative order of non-zero elements.

We simply overwrite from left to right.

Example:

[0,1,0,3,12]

After first loop:

[1,3,12,?,?]

After second loop:

[1,3,12,0,0]

---

# 📌 Pattern Used

Stable Two-Pointer Compression Pattern

Used when:

- In-place modification required
- Order must be preserved
- Filtering or compressing elements

---

# ⏱ Complexity

Time Complexity: O(n)  
Space Complexity: O(1)

---

# ⚠️ Common Mistakes

❌ Swapping immediately when seeing zero (breaks order)  
❌ Using extra array  
❌ Forgetting to fill trailing zeros  

---

# 🧩 Template Extracted

```
slow = 0
for fast in range(len(nums)):
    if CONDITION:
        nums[slow] = nums[fast]
        slow += 1
```

Afterwards:
Handle remaining elements if necessary.

---

# 📚 Reflection

This problem reinforces:

- Two pointer thinking
- Boundary control
- In-place modification
- Stable partition logic

---

# End
