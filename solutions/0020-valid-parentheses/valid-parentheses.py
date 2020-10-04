# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# 	Open brackets must be closed by the same type of brackets.
# 	Open brackets must be closed in the correct order.
#
#
#  
# Example 1:
#
#
# Input: s = "()"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: s = "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: s = "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: s = "{[]}"
# Output: true
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 104
# 	s consists of parentheses only '()[]{}'.
#
#


class Solution:
    def isValid(self, s: str) -> bool:
        if not len(s):
            return True
        
        stack = []
        for c in s:
            if not len(stack):
                stack.append(c)
                continue
            
            last, stack = stack[len(stack) -1], stack[:len(stack) - 1]
            if last == '(' and c == ')':
                pass
            elif last == '{' and c == '}':
                pass
            elif last == '[' and c == ']':
                pass
            else:
                stack.append(last)
                stack.append(c)
        
        return False if len(stack) > 0 else True

