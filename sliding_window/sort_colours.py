#Q: https://leetcode.com/problems/sort-colors/

class Solution:
    # Pattern Sliding Window: O(N)/O(1)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        curr = 0
        j = len(nums) - 1

        while (curr <= j):
            if (nums[curr] == 0):
                nums[i], nums[curr] = nums[curr], nums[i]
                i += 1
                curr += 1
            elif (nums[curr] == 2):
                nums[j], nums[curr] = nums[curr], nums[j]
                j -= 1
            else:
                curr += 1



