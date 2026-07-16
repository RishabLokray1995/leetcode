#Q: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
#Pattern: Sliding Window : O(N) or O(k) if k is << N/2
class Solution:
    # find minimum subarray of size n-k instead
    # def maxScore(self, cardPoints: List[int], k: int) -> int:
    #     K = len(cardPoints)-k
    #     min_subarray_sum = float("inf")

    #     i,j=0,0
    #     curr_sum = 0
    #     if(K==0): return sum(cardPoints)
    #     while j < len(cardPoints):
    #         curr_sum += cardPoints[j]
    #         if(j-i + 1 == K):
    #             min_subarray_sum = min(min_subarray_sum,curr_sum)
    #             curr_sum -= cardPoints[i]
    #             i+=1

    #         j+=1

    #     return sum(cardPoints) - min_subarray_sum

    # Circular array implementation -> quicker than the n-k appraoch as we are only looking at the smaller k subarray
    #            # print(f"i:{i},j{j},curr_sum:{curr_sum}")
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        array_size = len(cardPoints)
        i = array_size - k
        j = i

        curr_sum = 0
        max_subarray_sum = float("-inf")
        if (k == array_size): return sum(cardPoints)

        steps = 0
        total_steps_needed = 2 * k

        while steps < total_steps_needed:

            curr_sum += cardPoints[j]
            steps += 1

            if (steps >= k):
                max_subarray_sum = max(curr_sum, max_subarray_sum)
                curr_sum -= cardPoints[i]
                i = (i + 1) % array_size

            j = (j + 1) % array_size

        return max_subarray_sum







