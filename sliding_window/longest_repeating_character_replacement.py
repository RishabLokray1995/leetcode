#Q: https://leetcode.com/problems/longest-repeating-character-replacement/
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if (k >= len(s)): return len(s)
        i, j = 0, 0
        max_ = 0
        seen = defaultdict(int)
        curr_max_freq = 0
        while j < len(s):
            seen[s[j]] += 1
            curr_max_freq = max(curr_max_freq, seen[s[j]])

            if ((j - i + 1) - curr_max_freq > k):
                seen[s[i]] -= 1
                i += 1

            max_ = max(max_, j - i + 1)
            j += 1
        return max_




