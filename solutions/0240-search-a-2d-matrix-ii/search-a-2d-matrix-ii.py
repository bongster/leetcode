# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
#
#
# 	Integers in each row are sorted in ascending from left to right.
# 	Integers in each column are sorted in ascending from top to bottom.
#
#
#  
# Example 1:
#
#
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
#
#
# Example 2:
#
#
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false
#
#
#  
# Constraints:
#
#
# 	m == matrix.length
# 	n == matrix[i].length
# 	1 <= n, m <= 300
# 	-109 <= matrix[i][j] <= 109
# 	All the integers in each row are sorted in ascending order.
# 	All the integers in each column are sorted in ascending order.
# 	-109 <= target <= 109
#
#


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0]<=target and matrix[i][-1]>=target:
                lo = 0
                hi = n
                while lo < hi:
                    mid = lo + (hi - lo) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        lo = mid + 1
                    else:
                        hi = mid
        return False
