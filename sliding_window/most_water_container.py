from ast import List
#Q: https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    #Pattern: Opposite direction pointers. O(N),O(1)
    def maxArea(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        max_volume = -1
        while(i<j):
            cur_volume = (j-i)*min(height[j],height[i])
            max_volume = max(max_volume,cur_volume)
            if(height[i] < height[j]):
                i+=1
            else:
                j-=1
        return max_volume
