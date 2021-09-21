# You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.
#
# Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.
#
# An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.
#
#  
# Example 1:
#
#
# Input: n = 5, mines = [[4,2]]
# Output: 2
# Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.
#
#
# Example 2:
#
#
# Input: n = 1, mines = [[0,0]]
# Output: 0
# Explanation: There is no plus sign, so return 0.
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 500
# 	1 <= mines.length <= 5000
# 	0 <= xi, yi < n
# 	All the pairs (xi, yi) are unique.
#
#


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1] * n for _ in range(n)]
        for [x, y] in mines:
            grid[x][y] = 0
        
#         ans = 0
#         upCache = [[-1] * n for _ in range(n)]
#         downCache = [[-1] * n for _ in range(n)]
#         leftCache = [[-1] * n for _ in range(n)]
#         rightCache = [[-1] * n for _ in range(n)]
#         def getUpMax(x, y):
#             if y < 0 or grid[x][y] == 0:
#                 return 0
#             if upCache[x][y] == -1:
#                 upCache[x][y] = 1 + getUpMax(x, y - 1)
#             return upCache[x][y]
        
#         def getLeftMax(x, y):
#             if x < 0 or grid[x][y] == 0:
#                 return 0
#             if leftCache[x][y] == -1:
#                 leftCache[x][y] = 1 + getLeftMax(x - 1, y)
#             return leftCache[x][y]
        
#         def getRightMax(x, y):
#             if x > n - 1 or grid[x][y] == 0:
#                 return 0
#             if rightCache[x][y] == -1:
#                 rightCache[x][y] = 1 + getRightMax(x + 1, y)
#             return rightCache[x][y]
        
#         def getDownMax(x, y):
#             if y > n -1 or grid[x][y] == 0:
#                 return 0
#             if downCache[x][y] == -1:
#                 downCache[x][y] = 1 + getDownMax(x, y + 1)
#             return downCache[x][y]
        
#         for x in range(n):
#             for y in range(n):
#                 if grid[x][y] == 0:
#                     continue
#                 upMax = getUpMax(x, y)
#                 leftMax = getLeftMax(x, y)
#                 rightMax = getRightMax(x, y)
#                 downMax = getDownMax(x, y)
#                 ans = max(ans, min(upMax, leftMax, rightMax, downMax))
        
#         return ans
        left = [[0 for j in range(n+2)]for i in range(n+2)]
        right = [[0 for j in range(n+2)]for i in range(n+2)]
        top = [[0 for j in range(n+2)]for i in range(n+2)]
        bottom = [[0 for j in range(n+2)]for i in range(n+2)]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if grid[i -1][j-1] == 0:
                    continue
                left[i][j] = left[i][j - 1] + 1
                top[i][j] = top[i -1][j] + 1
        ans = 0
        for i in range(n,0,-1):
            for j in range(n,0,-1):
                if grid[i-1][j-1] == 0:
                    continue
                
                right[i][j] = right[i][j+1] + 1
                bottom[i][j] = bottom[i+1][j] + 1
                
                tempans = min(left[i][j],right[i][j],bottom[i][j],top[i][j])
                ans = max(ans, tempans)
        return ans
