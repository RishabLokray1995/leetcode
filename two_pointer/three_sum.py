from ast import List

class Solution:
    #Pattern: Two Pointer - O(N^2)/O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []  # Changed from set() to a standard list
        nums.sort()

        i = 0
        while i < len(nums):
            # Optimization: Skip duplicate anchor values to prevent duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            two_sum_results = self.two_sum(0 - nums[i], i + 1, nums)
            for pair in two_sum_results:
                # 'pair' is now a list, and we append a list directly to our results
                result.append([nums[i], pair[0], pair[1]])
            i += 1

        return result

    def two_sum(self, target: int, j: int, nums: List[int]) -> List[List[int]]:
        pairs = []  # Holds lists instead of tuples
        if j >= len(nums):
            return pairs

        k = len(nums) - 1
        while j < k:
            current_sum = nums[j] + nums[k]
            if current_sum == target:
                pairs.append([nums[j], nums[k]])  # Changed from tuple to list
                j += 1
                k -= 1

                # Optimization: Skip duplicate values for pointers to keep output unique
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
            elif current_sum > target:
                k -= 1
            else:
                j += 1
        return pairs
