# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
#  
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
#
#
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
#
#
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
#
#
#  
# Constraints:
#
#
# 	m == board.length
# 	n = board[i].length
# 	1 <= m, n <= 6
# 	1 <= word.length <= 15
# 	board and word consists of only lowercase and uppercase English letters.
#
#
#  
# Follow up: Could you use search pruning to make your solution faster with a larger board?
#


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        words = []
        M = len(board)
        N = len(board[0])
        
        def backtracking(i, j, pos, target):
            if pos == len(target):
                return True

            if 0 <= i < M and 0 <= j < N and board[i][j] == target[pos]:
                tmp = board[i][j]
                board[i][j] = '#'
                direction = [
                    [1, 0], # down
                    [-1, 0], # up
                    [0, -1], # left
                    [0, 1], # right
                ]
                for x,y in direction:
                    if backtracking(i + x, j + y, pos + 1, target):
                        return True
                board[i][j] = tmp
                return False
            else:
                return False
            
        
        for i in range(M):
            for j in range(N):
                if backtracking(i, j, 0, word):
                    return True
        return False
            
            
                
