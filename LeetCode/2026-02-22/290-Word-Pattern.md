# LeetCode 290 – Word Pattern

## 🧩 Problem Description

Given:

- A string `pattern`
- A string `s`

Determine if `s` follows the same pattern.

Example:

pattern = "abba"  
s = "dog cat cat dog"  

Output: True

The rule:

Each character in `pattern` must map to exactly one word in `s`,  
and each word must map back to exactly one character.

This is a **bijective mapping problem** (one-to-one mapping).

---

## 🎯 Core Idea

We must ensure:

1. Character → Word mapping is consistent
2. Word → Character mapping is consistent

That means:

- A character cannot map to two different words
- A word cannot map to two different characters

To enforce this, we use **two dictionaries**.

---

## 🧠 Step-by-Step Logic

### Step 1: Split the string

```python
words = s.split()
```

Convert:

"dog cat cat dog"  
→ ["dog", "cat", "cat", "dog"]

---

### Step 2: Check length

If the number of characters and words differ:

Return False immediately.

```python
if len(pattern) != len(words):
    return False
```

---

### Step 3: Create two dictionaries

```python
char_to_word = {}
word_to_char = {}
```

Why two?

To guarantee two-way uniqueness.

---

### Step 4: Iterate using zip

```python
for c, w in zip(pattern, words):
```

zip pairs them:

('a', 'dog')  
('b', 'cat')  
('b', 'cat')  
('a', 'dog')

---

### Step 5: Validate mapping

Check Character → Word:

```python
if c in char_to_word:
    if char_to_word[c] != w:
        return False
else:
    char_to_word[c] = w
```

Check Word → Character:

```python
if w in word_to_char:
    if word_to_char[w] != c:
        return False
else:
    word_to_char[w] = c
```

---

## ✅ Full Code

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words):

            if c in char_to_word:
                if char_to_word[c] != w:
                    return False
            else:
                char_to_word[c] = w

            if w in word_to_char:
                if word_to_char[w] != c:
                    return False
            else:
                word_to_char[w] = c

        return True
```

---

## 🧠 Key Concepts Used

- Dictionary (hash map)
- Two-way mapping
- zip()
- split()
- Membership check (`in`)
- Conditional branching

---

## 🔍 Algorithm Pattern

This problem uses:

**Double Hash Map Pattern**

Used when:

- Enforcing bijection
- Ensuring one-to-one mapping
- Solving isomorphic string problems

---

## ⏱ Complexity

Time Complexity: O(n)  
Space Complexity: O(n)

Where n is the length of the string.

---

## 🧠 Technical Insight

The key idea is not just checking forward mapping.

We must check:

Character → Word  
AND  
Word → Character  

Otherwise, cases like:

pattern = "abba"  
s = "dog dog dog dog"

Would incorrectly pass.

---

## 📌 Reflection

This problem strengthened understanding of:

- Dictionary-based mapping
- One-to-one relationship enforcement
- Hash-based validation logic

It demonstrates how two hash maps enforce bijection constraints.

---

# End
