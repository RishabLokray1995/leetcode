# Q: https://leetcode.com/problems/longest-valid-parentheses/
#O(N) O(N) - nested stack solution
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        i = 0
        max_ = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if (len(stack) == 0): stack.append(i)
                max_ = max(max_, i - stack[-1])
            i += 1
        return max_


# Constant space solution - O(1) - 2 pass solution.
    """
    1. Left-to-Right Pass:

It counts ( as left and ) as right.
When left == right, it records a valid length (2 * right).
When right > left, there are too many ). This breaks any valid sequence, so it resets the counters to 0.
Blind spot: It fails if there are excess ( at the end (e.g., "(()"). Here, left is always greater than right, so it never records the inner "()".
2. Right-to-Left Pass:

This pass solves the blind spot by scanning backwards.
It uses the same logic but resets when left > right (too many ( from the right perspective).
This successfully catches valid sequences that were blocked by excess ( on their left side (like the "(()" example).
Why it's complete:
Any valid parentheses substring will be correctly bounded by either an excess of ) (handled by the first pass) or an excess of ( (handled by the second pass). By taking the maximum from both passes, you guarantee finding the longest valid substring using only O(1) extra space.

Try tracing the strings "(()" and ")()())" step-by-step with both passes to see exactly how they complement each other!
    
    """
    def longestValidParentheses(self, s: str) -> int:
        left, right, maxlength = 0, 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength, 2 * right)
            elif right > left:
                left = right = 0
        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength, 2 * left)
            elif left > right:
                left = right = 0
        return maxlength




