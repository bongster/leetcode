# We are given a list of (axis-aligned) rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] , where (xi1, yi1) are the coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner of the ith rectangle.
#
# Find the total area covered by all rectangles in the plane. Since the answer may be too large, return it modulo 109 + 7.
#
#  
# Example 1:
#
#
# Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
# Output: 6
# Explanation: As illustrated in the picture.
#
#
# Example 2:
#
#
# Input: rectangles = [[0,0,1000000000,1000000000]]
# Output: 49
# Explanation: The answer is 1018 modulo (109 + 7), which is (109)2 = (-7)2 = 49.
#
#
#  
# Constraints:
#
#
# 	1 <= rectangles.length <= 200
# 	rectanges[i].length = 4
# 	0 <= rectangles[i][j] <= 109
# 	The total area covered by all rectangles will never exceed 263 - 1 and thus will fit in a 64-bit signed integer.
#
#


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # TODO: get timeLimit error
#         MOD = 10 ** 9 + 7
#         if len(rectangles) == 1:
#             x1, y1, x2, y2 = rectangles[0]
#             return ((x2 - x1) * (y2 - y1)) % MOD
        
#         min_x = 10 * 9 + 1
#         max_x = 0
#         min_y = 10 * 9 + 1
#         max_y = 0
#         for rectangle in rectangles:
#             x1, y1, x2, y2 = rectangle
#             min_x = min(min_x, x1)
#             max_x = max(max_x, x2)
#             min_y = min(min_y, y1)
#             max_y = max(max_y, y2)
        
#         dp = [[0] * (max_y - min_y + 1) for _ in range(max_x - min_x + 1)]
#         for x1, y1, x2, y2 in rectangles:
#             # print(x1,y1, x2, y2)
#             for i in range(x1, x2):
#                 for j in range(y1, y2):
#                     dp[i - min_x][j - min_y] = 1
#         ans = 0
#         for i in range(len(dp)):
#             for j in range(dp[i]):
#                 if dp[i][j] == 1:
#                     ans += 1
#         return ans % MOD
        
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        ys = sorted(set([y for x1, y1, x2, y2 in rectangles for y in [y1, y2]]))
        x_i = {v: i for i, v in enumerate(xs)}
        y_i = {v: i for i, v in enumerate(ys)}
        m, n = len(y_i), len(x_i)
        
        grid = [[0] * m for _ in range(n)]
        for x1, y1, x2, y2 in rectangles:
            for x in range(x_i[x1], x_i[x2]):
                for y in range(y_i[y1], y_i[y2]):
                    grid[x][y] = 1
        ans = 0
        for x in range(n-1):
            for y in range(m-1):
                if grid[x][y]:
                    ans += (xs[x+1] - xs[x]) * (ys[y+1] - ys[y])
        return ans  % (10**9 + 7)
