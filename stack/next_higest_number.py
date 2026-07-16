#Q: https://leetcode.com/problems/next-greater-element-i/

"""
Time complexity analysis : O(2N +M)

- The overall worst-case time complexity is actually O(n + m), not O(n^2).
Here is the explanation using amortized analysis:

While it is true that the inner while loop can pop up to n−1 elements in a single iteration (like when encountering 8), we must look at the total number of operations across the entire algorithm:

Pushes: Every element in the array is pushed onto the stack exactly once. (Total pushes = n)
Pops: An element can only be popped if it is currently on the stack. Once it is popped, it is never added back. Therefore, each element is popped at most once. (Total pops ≤n)
Even in your worst-case example (5, 4, 3, 2, 1, 8), the elements 5, 4, 3, 2, 1 are each pushed once and popped once when 8 is processed. The total number of stack operations (pushes + pops) for the entire array will never exceed 2n.

Since the total work done across all iterations is proportional to 2n, the time complexity simplifies to O(n). The heavy lifting done in one iteration is balanced out by the lack of work in the others.


"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map_ = defaultdict(lambda: -1)
        stack = []
        i = 0
        while i < len(nums2):
            if (not stack or (stack[-1] >= nums2[i])):
                stack.append(nums2[i])
            else:
                while (stack and stack[-1] < nums2[i]):
                    map_[stack.pop()] = nums2[i]
                stack.append(nums2[i])
            i += 1

        return [map_[k] for k in nums1]



"""
VARIATION with - repeating numbers in the nums2
https://www.hellointerview.com/learn/code/stack/monotonic-stack

DESCRIPTION
Given an array of integers, find the next greater element for each element in the array. The next greater element of an element x is the first element to the right of x that is greater than x. If there is no such element, then the next greater element is -1.
Example Input: [2, 1, 3, 2, 4, 3] Output: [3, 3, 4, 4, -1, -1]

Solution : use index, map cannot be used here as same keys can be overwritten due to duplicates.
"""

def nextGreaterElement(nums):
    ans = [-1] * len(nums)
    stack = []
    i = 0

    while i < len(nums):
        while(stack and nums[i] > nums[stack[-1]]):
            index = stack.pop()
            ans[index] = nums[i]
            pass

        stack.append(i)


"""
## NOTES
- 1st trick :  is to precompute for all elements of the input array.
- 2nd trick : store precomputed ones in hashmap for constant lookup. 
- 3rd trick : when repeated values in input list, try to use indexes as they are unique.
- 4th trick : a list with prefilled default values can be used, which will hold ans in the case we never calculate value for that index. 

"""