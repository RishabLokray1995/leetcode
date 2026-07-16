#Q: https://leetcode.com/problems/valid-parentheses/ -> pattern: Nested patterns
# T: O(N): S:O(1)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        pair_map = {')': '(', ']': '[', '}': '{'}
        close = [')', ']', '}']
        i = 0
        while i < len(s):
            if s[i] in close:
                if (len(stack) == 0) or stack[-1] != pair_map[s[i]]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
            i += 1

        return len(stack) == 0





