from collections import defaultdict

#Q: https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     state = defaultdict(int)
    #     i,j = 0,0
    #     max_ = 0
    #     while j<len(s):
    #         if(s[j] in state):
    #             while(state[s[j]] != 0):
    #                 state[s[i]] -=1
    #                 if(state[s[i]] == 0): del state[s[i]]

    #                 i+=1

    #         state[s[j]] +=1
    #         max_ = max(max_, j-i+1)
    #         j+=1

    #     return max_

    # without loop much faster, jump to index
    def lengthOfLongestSubstring(self, s: str) -> int:
        state = defaultdict(int)
        i, j = 0, 0
        max_ = 0
        while j < len(s):
            if (s[j] in state and state[s[j]] >= i):  # means the repetion is inside the current window, repetitions can happen outside the window as we are not emptying the dict here
                i = state[s[j]] + 1

            state[s[j]] = j
            max_ = max(max_, j - i + 1)
            j += 1

        return max_

    #Another approach by not reducing the window index by 1, but just jumping to the index of the repetion + 1.
    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            char_index = {}
            i = 0

            for j, char in enumerate(s):
                if char in char_index:
                    # i can only move forward, never backward
                    i = max(i, char_index[char] + 1)

                char_index[char] = j

            # The maximum window size achieved is the final length minus i
            return len(s) - i







