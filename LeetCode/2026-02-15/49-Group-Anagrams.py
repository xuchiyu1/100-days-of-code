# =========================================================
# LeetCode 49 - Group Anagrams
# Date: 2026-02-15
# Difficulty: Medium
# Pattern: Hash Map + Sorting
#
# Core Idea:
# 1. Sort each word to create a key.
# 2. Words with the same sorted result belong to same group.
# 3. Store them in a dictionary.
#
# Time Complexity: O(n * k log k)
#   n = number of words
#   k = average length of word
#
# Space Complexity: O(nk)
# =========================================================

class Solution:
    def groupAnagrams(self, strs):
        anagram_dict = {}

        for word in strs:
            # Sort characters in word
            sorted_word = ''.join(sorted(word))

            # If key not exists, create empty list
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = []

            # Append word to corresponding group
            anagram_dict[sorted_word].append(word)

        return list(anagram_dict.values())
