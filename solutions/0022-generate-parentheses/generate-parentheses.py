# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#  
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
#
#  
# Constraints:
#
#
# 	1 <= n <= 8
#
#


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                for x in dp[j]:
                    for y in dp[i - j - 1]:
                        dp[i].append('(' + x + ')' + y)
        return dp[n]
                
                
