# Given an m x n matrix, return all elements of the matrix in spiral order.
#
#  
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#  
# Constraints:
#
#
# 	m == matrix.length
# 	n == matrix[i].length
# 	1 <= m, n <= 10
# 	-100 <= matrix[i][j] <= 100
#
#


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        dp = [[False] * (col + 1) for _ in range(row + 1)]
        ans = []
        for i in range(math.ceil(row / 2)):
            # left -> right
            top = i
            left = i
            right = col - 1 - i
            bottom = row - 1 - i
            if right < 0 or bottom < 0:
                continue
            for x in range(left, right + 1):
                if not dp[top][x] and x >= 0:
                    dp[top][x] = True
                    ans.append(matrix[top][x])
            
            for y in range(top, bottom + 1):
                if not dp[y][right] and y >=0:
                    dp[y][right] = True
                    ans.append(matrix[y][right])
            
            for ry in range(right, left -1, -1):
                if not dp[bottom][ry] and ry >=0:
                    dp[bottom][ry] = True
                    ans.append(matrix[bottom][ry])
            
            for rx in range(bottom, top, -1):
                if not dp[rx][left] and rx >=0:
                    dp[rx][left] = True
                    ans.append(matrix[rx][left])
            
        return ans
                
