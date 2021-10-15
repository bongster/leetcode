# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
#  
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]
#
#  
# Constraints:
#
#
# 	1 <= numRows <= 30
#
#


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        dp = [[] for _ in range(numRows)]
        dp[0] = [1]
        
        for i in range(1, numRows):
            # dp[i].append(1)
            j = dp[i -1]
            x = []
            for k in range(1, len(j)):
                x.append(j[k] + j[k -1])
            dp[i].extend([1] + x + [1])
        return dp
