# Pattern: Sliding Window - O(N)/O(K)
# Q:
class Solution:
  def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    i=0
    j=i
    seen = set()
    max_sum = 0
    curr_sum = 0
    while(j<len(nums)):
      if(nums[j] not in seen):
        seen.add(nums[j])
        curr_sum += nums[j]

        if(j-i+1 == k):
          max_sum = max(max_sum,curr_sum)
          seen.remove(nums[i])
          curr_sum -= nums[i]
          i+=1

      else: #nums[j] in seen
        while(nums[i]!=nums[j]):
          curr_sum-=nums[i]
          seen.remove(nums[i])
          i+=1
        seen.remove(nums[i])
        i+=1
        seen.add(nums[j])

      j+=1
    return max_sum