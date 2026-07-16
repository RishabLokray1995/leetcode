from collections import defaultdict
#Q: https://leetcode.com/problems/fruit-into-baskets/
#Q: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters

"""
followups : 
How would your logic change if you had to find the longest substring with exactly k distinct characters instead of at most k?
- add this before calc max
   # Now window is valid: at most k distinct chars
    # So we can safely check for max length
    if len(seen) == k:
        max_len = max(max_len, right - left + 1)
"""
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        i, j = 0, 0
        basket = defaultdict(int)

        while (j < len(fruits)):
            basket[fruits[j]] += 1

            while len(basket.keys()) > 2:
                basket[fruits[i]] -= 1
                if (basket[fruits[i]] == 0): basket.pop(fruits[i])
                i += 1
            max_fruits = max(max_fruits, j - i + 1)
            j += 1
        return max_fruits

    # generalised to a large K - do not use while loop
    def totalFruit(self, fruits: List[int], k:int) -> int:
        basket = defaultdict(int)
        i = 0

        for j in range(len(fruits)):
            basket[fruits[j]] += 1

            # If we exceed k types, just shift the left pointer by 1.
            # The window size (j - i + 1) stays fixed at its historical maximum.
            if len(basket) > k:
                basket[fruits[i]] -= 1
                if basket[fruits[i]] == 0:
                    del basket[fruits[i]]
                i += 1  # Shift left boundary up by exactly 1

        # The maximum window size achieved is simply the final size of the window
        return len(fruits) - i






