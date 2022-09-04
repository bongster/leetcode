# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
#  
# Example 1:
#
#
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.
#
#
# Example 2:
#
#
# Input: board = [["X"]]
# Output: [["X"]]
#
#
#  
# Constraints:
#
#
# 	m == board.length
# 	n == board[i].length
# 	1 <= m, n <= 200
# 	board[i][j] is 'X' or 'O'.
#
#


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R = len(board)
        C = len(board[0])
        queue = collections.deque()
        for x in [0, R -1]:
            for y in range(C):
                if board[x][y] == 'O':
                    board[x][y] = 'G'
                    queue.append([x, y])
        for x in range(R):
            for y in [0, C - 1]:
                if board[x][y] == 'O':
                    board[x][y] = 'G'
                    queue.append([x, y])
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while len(queue):
            x, y = queue.popleft()
            for dx, dy in directions:
                xx, yy = x + dx, y + dy
                if 0 <= xx < R and 0 <= yy < C and board[xx][yy] == 'O':
                    board[xx][yy] = 'G'
                    queue.append((xx, yy))
        
        for x in range(R):
            for y in range(C):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                if board[x][y] == 'G':
                    board[x][y] = 'O'
        
