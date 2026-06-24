# LeetCode 127 — Word Ladder

- **Date:** 2026-06-23
- **Topic:** BFS (shortest path on an implicit graph)
- **Difficulty:** Hard

## Problem
Given `beginWord`, `endWord`, and `wordList`, return the number of words in the
shortest transformation sequence (change one letter at a time, each intermediate
word must be in `wordList`). Return 0 if no path exists.

## Idea
Shortest path → **BFS**. Each word is a node; two words are neighbors if they
differ by exactly one letter. BFS level by level; the level number = sequence length.

## Solution (single-direction BFS)
```python
from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)              # set -> O(1) lookup
        if endWord not in words:
            return 0

        queue = deque([beginWord])
        visited = {beginWord}
        length = 1

        while queue:
            for _ in range(len(queue)):    # freeze level size -> process one whole level
                word = queue.popleft()
                if word == endWord:
                    return length
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + c + word[i+1:]   # neighbor (strings immutable)
                        if new_word in words and new_word not in visited:
                            visited.add(new_word)
                            queue.append(new_word)
            length += 1                    # one whole level done -> one step deeper
        return 0
```

## Key insights
1. **Level-by-level BFS for shortest path.** Freeze `len(queue)` before the inner
   loop so you process exactly one level, then `length += 1`. Same pattern as LC 542.
2. **Generate neighbors by slicing.** Strings are immutable, so to change one letter:
   `word[:i] + c + word[i+1:]`. Each word has `len(word) * 26` candidates.
3. **`visited` + `set(wordList)`** prevent revisiting and give O(1) lookups.

## Complexity
- Time: O(N × L × 26), Space: O(N × L)

## Note
Bidirectional BFS (search from both ends, stop when frontiers meet) is an
optimization — learn it after the single-direction version is solid.
