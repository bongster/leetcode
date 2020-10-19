# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
#
# 	Integers in each row are sorted from left to right.
# 	The first integer of each row is greater than the last integer of the previous row.
#
#
#  
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
# Output: true
#
#
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
# Output: false
#
#
# Example 3:
#
#
# Input: matrix = [], target = 0
# Output: false
#
#
#  
# Constraints:
#
#
# 	m == matrix.length
# 	n == matrix[i].length
# 	0 <= m, n <= 100
# 	-104 <= matrix[i][j], target <= 104
#
#


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
            return False
        l = 0
        r = len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if target in matrix[m]:
                return True
            elif matrix[m][0] < target and target < matrix[m][-1]:
                return False
            if matrix[m][0] < target:
                l = m + 1
            else:
                r = m - 1
        # return target in matrix[r]
                
