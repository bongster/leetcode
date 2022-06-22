# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
#  
# Example 1:
#
#
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
#
#
# Example 2:
#
#
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
#
#
# Example 3:
#
#
# Input: matrix = [["0"]]
# Output: 0
#
#
#  
# Constraints:
#
#
# 	m == matrix.length
# 	n == matrix[i].length
# 	1 <= m, n <= 300
# 	matrix[i][j] is '0' or '1'.
#
#


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [ [0] * (n + 1) for _ in range(m + 1) ]

        max_size = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '1':
                    dp[r + 1][c + 1] = min([dp[r][c], dp[r + 1][c], dp[r][c + 1]]) + 1
                    max_size = max(dp[r + 1][c + 1], max_size)
        return max_size * max_size
