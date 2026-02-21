# LeetCode 49 - Group Anagrams

## Problem Type
Hash Map + Sorting

---

## Core Logic

1. For each word, sort its letters.
2. Use sorted result as dictionary key.
3. Append original word into that group.

Example:

"eat" → sorted → "aet"
"tea" → sorted → "aet"

Both share same key → same group.

---

## Key Python Syntax

sorted(word)  
→ returns a list of characters

''.join(sorted(word))  
→ converts list into string

dict[key] = []  
→ create new group

dict[key].append(word)  
→ add word to group

list(dict.values())  
→ return all groups

---

## Algorithm Pattern

This problem uses:

1. Hash Map for grouping
2. Sorting for normalization
3. Classification based on transformed key

---

## Reflection

This problem trains:

- Dictionary grouping
- Transforming data before classification
- Understanding hash-based grouping pattern
