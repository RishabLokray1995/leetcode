from ast import List

# Q: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    #Pattern: Same direction pointers. O(N)/O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = i+1

        while j<len(nums):
            if(nums[i] == nums[j]):
                j+=1
            else:
                unique_member = nums[j]
                i+=1
                j+=1
                nums[i] = unique_member

        return i+1

"""
If you were allowed to keep up to two occurrences of each element 
instead of just one, how would your pointer logic need to change?: 
-> Keep a counter variable in equal case statement. Increment it by 2. And reset this counter in the not equal case block. 
"""