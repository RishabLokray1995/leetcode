from ast import List


class Solution:
    # Dictionary Approach - O(N)/O(N)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     memo = {value: index for index,value in enumerate(nums)}

    #     for cur_i, cur_n in enumerate(nums):
    #         other_i = memo.get(target-cur_n)
    #         if other_i != None and other_i != cur_i: # handles `no solution` & `cannot repeat same value` case
    #             return [cur_i, memo.get(target-cur_n)]

    #     return list()

    # Pattern: Opposite direction Two pointer Approach - O(N)/O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(value, index) for index, value in enumerate(nums)]
        nums.sort()
        i, j = 0, len(nums) - 1
        while (i < j):
            if (nums[i][0] + nums[j][0] == target):
                return [nums[i][1], nums[j][1]]
            elif (nums[i][0] + nums[j][0] < target):
                i += 1
            else:
                j -= 1
