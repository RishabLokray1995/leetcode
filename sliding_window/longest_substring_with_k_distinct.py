#: Q: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        i, j = 0, 0
        max_ = 0
        seen = defaultdict(int)
        if (k == 0): return 0
        while j < len(s):
            seen[s[j]] += 1

            while (len(seen) > k):
                seen[s[i]] -= 1
                if (seen[s[i]] == 0): del seen[s[i]]
                i += 1

            max_ = max(max_, j - i + 1)
            j += 1

        return max_



