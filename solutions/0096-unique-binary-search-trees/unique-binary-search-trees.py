# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
#
#  
# Example 1:
#
#
# Input: n = 3
# Output: 5
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 19
#
#


class Solution:
    def numTrees(self, n: int) -> int:
        
        if n == 1 or n == 0:
            return 1
        
        dp = [1, 1]
        
        for i in range(2, n+1):
            
            numTreesI = 0
            for nLeft in range(i):
                nRight = i - 1 - nLeft
                numTreesI += dp[nLeft] * dp[nRight]
            
            dp.append(numTreesI)
        
        return dp[-1]
