# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.
#
# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.
#
#  
# Example 1:
#
#
# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6
# Explanation: 
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
#
#
# Example 2:
#
#
# Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# Output: -1
# Explanation: We need to eliminate at least two obstacles to find such a walk.
#
#
#  
# Constraints:
#
#
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 40
# 	1 <= k <= m * n
# 	grid[i][j] is either 0 or 1.
# 	grid[0][0] == grid[m - 1][n - 1] == 0
#
#


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        directions = [
            [-1, 0], # up
            [1, 0], # down
            [0, 1], # right
            [0,  -1], # left
        ]
        lives = [[-1] * N for _ in range(M)]
        q = deque()
        q.append([0, 0, k, 0]) # row, col, lives, distance
        while len(q):
            cr, cc, clives, cdist = q.popleft()
            if cr == M -1 and cc == N - 1:
                return cdist
            if grid[cr][cc] == 1:
                clives -= 1
            
            for dx, dy in directions:
                nr, nc = cr + dx, cc + dy
                if 0 <= nr < M and 0 <= nc < N and lives[nr][nc] < clives:
                    q.append([nr, nc, clives, cdist + 1])
                    lives[nr][nc] = clives
        return -1
        # m = len(grid)
#         n = len(grid[0])
#         def dfs(x, y, k, temp, res):
#             if x == m - 1 and y == n - 1:
#                 res.append(temp)
#                 return
#             direction = [
#                 [-1, 0], # up
#                 [1, 0], # down
#                 [0, 1], # right
#                 [0,  -1], # left
#             ]
#             for [dx, dy] in direction:
#                 x1 = x + dx
#                 y1 = y + dy
#                 if x1 < 0 or x1 > m - 1 or y1 < 0 or y1 > n -1:
#                     continue
                
#                 if [x1, y1] not in temp:
#                     if grid[x1][y1] == 1:
#                         if k > 0:
#                             dfs(x1, y1, k -1, temp + [[x, y]], res)
#                     else:
#                         dfs(x1, y1, k, temp + [[x, y]], res)
#         res = []
#         dfs(0, 0, k, [], res)

#         if not len(res):
#             return -1
#         else:
#             res = sorted(res, key=lambda x: len(x))
#             return len(res[0])
            
