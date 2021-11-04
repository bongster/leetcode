# You are given an m x n integer array grid where grid[i][j] could be:
#
#
# 	1 representing the starting square. There is exactly one starting square.
# 	2 representing the ending square. There is exactly one ending square.
# 	0 representing empty squares we can walk over.
# 	-1 representing obstacles that we cannot walk over.
#
#
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.
#
#  
# Example 1:
#
#
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
#
#
# Example 2:
#
#
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
#
#
# Example 3:
#
#
# Input: grid = [[0,1],[2,0]]
# Output: 0
# Explanation: There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.
#
#
#  
# Constraints:
#
#
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 20
# 	1 <= m * n <= 20
# 	-1 <= grid[i][j] <= 2
# 	There is exactly one starting cell and one ending cell.
#
#


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_point = None
        m = len(grid)
        n = len(grid[0])
        v = m * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_point = [i, j]
                if grid[i][j] == -1:
                    v -= 1
        
        direction = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
        ]
        self.ans = []
        def solve(x, y, paths):
            # print(grid)
            if grid[x][y] == -1 or grid[x][y] == 3:
                return

            if grid[x][y] == 2:
                if paths not in self.ans and len(paths) == v -1:
                    self.ans.append(paths)
                return
            
            for dx, dy in direction:
                xx, yy = x + dx, y + dy
                if 0 <= xx < m and 0 <= yy < n:
                    # print(xx, yy, paths + [[xx, yy]])
                    temp = grid[x][y]
                    grid[x][y] = 3
                    solve(xx, yy, paths + [[xx, yy]])
                    grid[x][y] = temp
        # print(start_point)
        solve(start_point[0], start_point[1], [])
        # print(self.ans)
        return len(self.ans)
        
