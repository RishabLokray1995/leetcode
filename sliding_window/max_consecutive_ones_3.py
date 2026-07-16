#Q: https://leetcode.com/problems/max-consecutive-ones-iii/
#T: O(N)

from collections import defaultdict,deque


class Solution:
    # def longestOnes(self, nums: List[int], k: int) -> int:
    #     seen = defaultdict(int)
    #     i,j = 0,0
    #     max_ = float("-inf")
    #     if(k >= len(nums)): return len(nums)

    #     while j<len(nums):
    #         seen[nums[j]] +=1

    #         if(seen[0] > k):
    #             seen[nums[i]] -= 1
    #             i +=1

    #         max_ = max(max_,j-i+1)
    #         j+=1
    #     return max_

    # Alternate : Skip to 1 position after the first 0 in the current window.
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_indices = deque()
        left = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_indices.append(right)

            while len(zero_indices) > k:
                left = zero_indices.popleft() + 1

            max_len = max(max_len, right - left + 1)

        return max_len
