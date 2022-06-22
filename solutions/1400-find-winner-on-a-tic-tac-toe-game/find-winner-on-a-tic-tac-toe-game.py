# Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:
#
#
# 	Players take turns placing characters into empty squares ' '.
# 	The first player A always places 'X' characters, while the second player B always places 'O' characters.
# 	'X' and 'O' characters are always placed into empty squares, never on filled ones.
# 	The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
# 	The game also ends if all squares are non-empty.
# 	No more moves can be played if the game is over.
#
#
# Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".
#
# You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.
#
#  
# Example 1:
#
#
# Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# Output: "A"
# Explanation: A wins, they always play first.
#
#
# Example 2:
#
#
# Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# Output: "B"
# Explanation: B wins.
#
#
# Example 3:
#
#
# Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# Output: "Draw"
# Explanation: The game ends in a draw since there are no moves to make.
#
#
#  
# Constraints:
#
#
# 	1 <= moves.length <= 9
# 	moves[i].length == 2
# 	0 <= rowi, coli <= 2
# 	There are no repeated elements on moves.
# 	moves follow the rules of tic tac toe.
#
#


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        R = 0
        for [x, y] in moves:
            R = max(max(R, x), y)
        
        dp = [[''] * (R + 1) for _ in range(R + 1)]
        def valid(x, y, v):
            """
            Checking valid lines row, column/ diag / reverse-diag
            """
            ans = [True, True, True, True]
            
            for j in range(R + 1):
                # Row
                if dp[x][j] != v or dp[x][j] == '':
                    ans[0] = False
                # Column
                if dp[j][y] != v or dp[j][y] == '':
                    ans[1] = False
                # Diagonal
                if dp[j][j] != v or dp[j][j] == '':
                    ans[2] = False
                # Reverse diagonal
                if dp[j][R - j] != v or dp[j][R - j] == '':
                    ans[3] = False

            return any(ans)

        for i, [x, y] in enumerate(moves):
            v = 'B' if i % 2 else 'A'
            dp[x][y] = v
            if valid(x, y, v):
                return v
        # Checking Pending status
        if len(moves) != (R + 1) ** 2:
            return 'Pending'
        return 'Draw'
            
