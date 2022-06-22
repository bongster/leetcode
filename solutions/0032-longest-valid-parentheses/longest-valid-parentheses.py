# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
#  
# Example 1:
#
#
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
#
#
# Example 2:
#
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
#
#
# Example 3:
#
#
# Input: s = ""
# Output: 0
#
#
#  
# Constraints:
#
#
# 	0 <= s.length <= 3 * 104
# 	s[i] is '(', or ')'.
#
#


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        valid = [0] * n
        stack = deque()
        for i, c in enumerate(s):
            # print(i, c)
            if c == '(':
                stack.append((c, i))
            else:
                if len(stack) and stack[-1][0] == '(':
                    s = stack.pop()
                    # print(s, i)
                    valid[i] = 1
                    valid[s[1]] = 1
        ans = 0
        for i in range(n):
            x = 0
            for j in range(i, n):
                if valid[j] == 0:
                    break
                x += 1
            ans = max(ans, x)
        return ans
            
