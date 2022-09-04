# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.
#
# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.
#
#  
# Example 1:
#
#
# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6
#
#
# Example 2:
#
#
# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12
#
#
#  
# Constraints:
#
#
# 	1 <= m, n <= 50
# 	0 <= maxMove <= 50
# 	0 <= startRow < m
# 	0 <= startColumn < n
#
#


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        directions = (
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        )
        # TLE
#         ans = 0
#         queue = deque()
#         queue.append([startRow, startColumn, maxMove])
#         visited = set()
#         while len(queue):
#             [i, j, c] = queue.pop()
#             if c < 0:
#                 continue
            
#             if 0 <= i < m and 0 <= j < n:
#                 for x, y in directions:
#                     xx, yy = i + x, y + j
#                     queue.append([xx, yy, c - 1])    
#             else:
#                 ans += 1
                
#         return ans
        # define the dp array
        dp = [[[-1]*(maxMove+1) for _ in range(n+1)] for _ in range(m+1)]
        
        DIR = [0, 1, 0, -1, 0]

        @lru_cache(None)
        def dp(r, c, k):
            if r < 0 or r == m or c < 0 or c == n: 
                return 1
            if k == 0:
                return 0
            ans = 0
            for i, j in directions:
                ans += dp(r + i, c + j, k - 1)
            return ans

        return dp(startRow, startColumn, maxMove) % 1_000_000_007
