# Pattern Sliding window prefix sum : O(N)
# Q: https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        prefix_sum = [0] * (len(nums) + 1)
        index_map = {}

        psum = 0
        for i, val in enumerate(nums):
            prefix_sum[i] = psum
            index_map[psum] = i
            psum += val

        prefix_sum[-1] = psum
        index_map[psum] = len(prefix_sum) - 1

        max_sub_array = 0

        i = 0
        while i < len(prefix_sum):
            val = k + prefix_sum[i]  # main condition : prefix_sum[j]-prefix_sum[i] == k the window's sum
            if (index_map.get(val, None) != None):
                max_sub_array = max(max_sub_array, index_map.get(val) - i)
            i += 1
        return max_sub_array




