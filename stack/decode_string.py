# O(N)
# Q: https://leetcode.com/problems/decode-string/ -> nested pattern
class Solution:
    def decodeString(self, s: str) -> str:
        k_stack = list()
        string_stack = list()
        i = 0
        while i < len(s):
            if (s[i].isdigit()):
                k = 0
                while (i < len(s) and s[i].isdigit()):
                    k = k * 10 + int(s[i])
                    i += 1
                k_stack.append(k)

            if (s[i] != ']'):
                string_stack.append(s[i])
            else:
                curr_s = ''
                while (string_stack[-1] != '['):
                    curr_s = string_stack.pop() + curr_s
                string_stack.pop()
                string_stack.append(k_stack.pop() * curr_s)
            i += 1

        return "".join(string_stack)









