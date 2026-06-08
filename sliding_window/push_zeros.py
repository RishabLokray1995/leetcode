from ast import List

#Q: https://leetcode.com/problems/move-zeroes/

class Solution:
    # Pattern: Same direciton two pointer: O(N)/O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = i

        while (j < len(nums)):
            if (nums[j] != 0):
                # put j in front of list where i was and move i by one
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1

