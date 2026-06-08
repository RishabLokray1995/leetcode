from ast import List

#Q: https://leetcode.com/problems/valid-triangle-number/
#O(N^2)/O(1)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)  # nlogn
        result_count = 0
        i = 0
        while i < len(nums):
            hypotenous = nums[i]
            pairs = self.two_sum(i + 1, hypotenous, nums)
            result_count += pairs
            i += 1

        return result_count

    def two_sum(self, j, hypotenous, nums):
        if (j > len(nums)): return 0
        pairs = 0
        k = len(nums) - 1
        while (j < k):
            if (nums[j] + nums[k] > hypotenous):
                pairs += (k - j)
                j += 1
            else:
                k -= 1
        return pairs

# Note: if we shorten the left side window to find the smallest number that works, then all between j,k will work.

