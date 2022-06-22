# Given a balanced parentheses string s, return the score of the string.
#
# The score of a balanced parentheses string is based on the following rule:
#
#
# 	"()" has score 1.
# 	AB has score A + B, where A and B are balanced parentheses strings.
# 	(A) has score 2 * A, where A is a balanced parentheses string.
#
#
#  
# Example 1:
#
#
# Input: s = "()"
# Output: 1
#
#
# Example 2:
#
#
# Input: s = "(())"
# Output: 2
#
#
# Example 3:
#
#
# Input: s = "()()"
# Output: 2
#
#
#  
# Constraints:
#
#
# 	2 <= s.length <= 50
# 	s consists of only '(' and ')'.
# 	s is a balanced parentheses string.
#
#


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # General Idea: use a stack to keep track of the open parenthesis and the score of parenthesis so far
        # Specifically, iterate through the string and cehck:
        #   + when face with a "(" --> just add it to the stack
        #   + when face with a ")" --> couple of scenarios:
        #     - if top of the stack is a "(", then pop the stack and add 1 to the stack
        #     - if top of the stack is a digit, find the sum of all the number on top of the stack until you meet an "(". At that point, follow rule #3, mutiply the local sum by 2 and then add that sum to the stack
        # final result is the sum of the stack
        
        stack = []
        
        for char in s:
            if char == "(":
                stack.append(char)
            else: # char ==")"
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    local_sum = 0
                    while type(stack[-1]) == int:
                        local_sum += stack.pop()
                    stack.pop()
                    stack.append(2 * local_sum)
        return sum(stack)
