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
# Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
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
        if not board:
            return board
        R = len(board)
        C = len(board[0])
        for i in range(R):
            if (board[i][0] == 'O'):
                self.dfs(board, i, 0)
            if (board[i][C - 1] == 'O'):
                self.dfs(board, i, C - 1)

        for j in range(C):
            if (board[0][j] == 'O'):
                self.dfs(board, 0, j)
            if (board[R -1][j] == 'O'):
                self.dfs(board, R - 1, j)
        print(board)
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'

                
    def dfs(self, board, i, j):
        R = len(board)
        C = len(board[0])
        if i >= 0 and i < R and j >= 0 and j < C and board[i][j] == 'O':
            board[i][j] = 'A'
            self.dfs(board, i + 1, j)
            self.dfs(board, i - 1, j)
            self.dfs(board, i, j + 1)
            self.dfs(board, i, j - 1)
