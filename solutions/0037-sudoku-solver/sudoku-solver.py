# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
#
# 	Each of the digits 1-9 must occur exactly once in each row.
# 	Each of the digits 1-9 must occur exactly once in each column.
# 	Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
#
#
# The '.' character indicates empty cells.
#
#  
# Example 1:
#
#
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:
#
#
#
#
#  
# Constraints:
#
#
# 	board.length == 9
# 	board[i].length == 9
# 	board[i][j] is a digit or '.'.
# 	It is guaranteed that the input board has only one solution.
#
#


class Solution:
    N = 9
    def is_valid(self, board, row, col, num):
        # TODO: checking row is valid
        for x in range(9):
            if board[row][x] == num:
                return False
        # TODO: chcking colum in valid
        for x in range(9):
            if board[x][col] == num:
                return False

        # TODO: checking box is valid
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + startRow][j + startCol] == num:
                    return False
        return True
    def solve(self, board, row, col):
        # Reach end of board
        N = self.N
        if row == N -1 and col == N:
            return True

        # if col is same as end of line change col = 0 and row += 1
        if col == N:
            row += 1
            col = 0

        # if has a value in board[row][col] go to next col
        if board[row][col] != '.':
            return self.solve(board, row, col + 1)

        for num in range(1, N + 1):
            num = str(num)
            if self.is_valid(board, row, col, num):
                board[row][col] = num
                if self.solve(board, row, col + 1):
                    return True
            board[row][col] = '.'
        return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # self.N = len(board)
        
        self.solve(board, 0, 0)
