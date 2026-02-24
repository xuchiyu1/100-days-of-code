# LeetCode 205 – Isomorphic Strings

## 🧩 Problem

Given two strings `s` and `t`, determine if they are isomorphic.

Two strings are isomorphic if characters in `s` can be replaced to get `t`.

Each character must map to another character uniquely.

---

## 🎯 Core Idea

We must ensure:

1. Character → Character mapping is consistent.
2. No two characters map to the same character.

This is called a **bijective mapping** (one-to-one mapping).

---

## 🧠 Step-by-Step Thinking

Example:

s = "egg"  
t = "add"

Mapping:

e → a  
g → d  

Works ✔

But:

s = "foo"  
t = "bar"

f → b  
o → a  
o → r ❌ (conflict)

---

## 🔥 Solution Approach

We use TWO dictionaries:

- s_to_t
- t_to_s

Why two?

To guarantee two-way uniqueness.

---

## ✅ Code

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for c1, c2 in zip(s, t):

            if c1 in s_to_t:
                if s_to_t[c1] != c2:
                    return False
            else:
                s_to_t[c1] = c2

            if c2 in t_to_s:
                if t_to_s[c2] != c1:
                    return False
            else:
                t_to_s[c2] = c1

        return True
```

---

## 🔍 Key Python Syntax Explained

zip(s, t)  
→ pairs characters together

dict[key] = value  
→ creates mapping

if key in dict  
→ checks existence

---

## 🧠 Algorithm Pattern

This uses:

Double Hash Map Pattern  
Used when enforcing one-to-one mapping.

---

## ⏱ Complexity

Time: O(n)  
Space: O(n)

---

## 📌 Common Mistakes

❌ Using only one dictionary  
❌ Forgetting reverse check  
❌ Not checking length first  

---

## 💡 Reflection

This problem trains:

- Hash map mapping logic
- One-to-one relationship enforcement
- Pattern recognition skills
