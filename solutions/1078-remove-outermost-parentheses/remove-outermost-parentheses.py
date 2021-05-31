# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
#
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A+B, with A and B nonempty valid parentheses strings.
#
# Given a valid parentheses string s, consider its primitive decomposition: s = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
#
# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
#
#  
#
# Example 1:
#
#
# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
#
#
#
# Example 2:
#
#
# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
#
#
#
# Example 3:
#
#
# Input: s = "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
#
#
#  
#
#
#
# Note:
#
#
# 	s.length <= 10000
# 	s[i] is "(" or ")"
# 	s is a valid parentheses string
#
#
#
#
#  
#
#
#


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        bracket = 0
        stack = []
        res = []
        for s in S:
            stack.append(s)
            if s == '(':
                bracket += 1
            elif s == ')':
                bracket -= 1
                
            if bracket == 0:
                # input_string_arr.append(''.join([for si in stack[1:len(stack) -1]]))
                res.append(
                    ''.join([ si for si in stack[1:len(stack) -1]])
                )
                # print(''.join([ si for si in stack[1:len(stack) -1]]))
                stack = []
        
        return ''.join(res)
