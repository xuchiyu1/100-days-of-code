# LeetCode 205 – Isomorphic Strings (Index Pattern Version)

## 🧩 Problem

Given two strings `s` and `t`, determine if they are isomorphic.

Two strings are isomorphic if characters in `s` can be replaced to get `t`
while preserving order and maintaining a one-to-one mapping.

---

## 🎯 Core Idea (Index Pattern Approach)

Instead of using two hash maps, this solution compares the **index pattern** of both strings.

The idea:

If two strings are isomorphic,  
their "first occurrence index pattern" must be identical.

---

## 🧠 How It Works

Example:

s = "paper"
t = "title"

For string "paper":

p → first appears at index 0  
a → first appears at index 1  
p → first appears at index 0  
e → first appears at index 3  
r → first appears at index 4  

Pattern becomes:

[0, 1, 0, 3, 4]

For string "title":

t → first appears at index 0  
i → first appears at index 1  
t → first appears at index 0  
l → first appears at index 3  
e → first appears at index 4  

Pattern becomes:

[0, 1, 0, 3, 4]

Since both patterns are identical → True.

---

## ✅ Code (Your Version)

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = []
        map2 = []

        for idx in s:
            map1.append(s.index(idx))

        for idx in t:
            map2.append(t.index(idx))

        if map1 == map2:
            return True
        return False
```

---

## 🔍 Key Python Syntax Explained

### `.index(x)`

Returns the index of the **first occurrence** of `x`.

Example:

```python
"paper".index("p") → 0
```

Even the second "p" still returns 0.

---

## 🧠 Why This Works

This solution compares structural patterns.

If two strings have the same index pattern,
they follow the same character structure.

---

## ⏱ Complexity

Time Complexity: O(n²)  
(Each `.index()` scans the string again.)

Space Complexity: O(n)

---

## ⚠️ Limitation

This solution is less efficient than the double-hash-map approach.

However, it is very intuitive and good for understanding structural matching.

---

## 💡 Reflection

This approach teaches:

- Pattern transformation
- First occurrence tracking
- Structural equivalence checking
