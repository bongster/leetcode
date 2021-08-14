# Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].
#
# The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:
#
#
# 	The rank is an integer starting from 1.
# 	If two elements p and q are in the same row or column, then:
#
# 		If p < q then rank(p) < rank(q)
# 		If p == q then rank(p) == rank(q)
# 		If p > q then rank(p) > rank(q)
#
#
# 	The rank should be as small as possible.
#
#
# It is guaranteed that answer is unique under the given rules.
#
#  
# Example 1:
#
#
# Input: matrix = [[1,2],[3,4]]
# Output: [[1,2],[2,3]]
# Explanation:
# The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
# The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
# The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
# The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.
#
#
# Example 2:
#
#
# Input: matrix = [[7,7],[7,7]]
# Output: [[1,1],[1,1]]
#
#
# Example 3:
#
#
# Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
# Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
#
#
# Example 4:
#
#
# Input: matrix = [[7,3,6],[1,4,5],[9,8,2]]
# Output: [[5,1,4],[1,2,3],[6,3,1]]
#
#
#  
# Constraints:
#
#
# 	m == matrix.length
# 	n == matrix[i].length
# 	1 <= m, n <= 500
# 	-109 <= matrix[row][col] <= 109
#
#


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        def union(x, y):
            r1 = find(x)
            r2 = find(y)
            if r1 != r2:
                parents[r1] = r2
        
        value2Pos = defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                value2Pos[val].append((i, j))
        ans = [[0] * n for _ in range(m)]
        
        rowMaxRank = [0] * m
        colMaxRank = [0] * n
        
        for val in sorted(value2Pos):
            parents = list(range(m + n))
            
            # group nums on the same row / col
            for i, j in value2Pos[val]:
                union(i, j + n)
            
            root2Rank = defaultdict(int)
            
            # calculate new rank for the nums which have the same root( on the same row/ col)
            for i, j in value2Pos[val]:
                root = find(i)
                root2Rank[root] = max(root2Rank[root], max(rowMaxRank[i], colMaxRank[j]) + 1)
            
            # update the ans aand row/colMaxRank
            for i, j in value2Pos[val]:
                root = find(i)
                rank = root2Rank[root]
                ans[i][j] = rank
                rowMaxRank[i] = rank
                colMaxRank[j] = rank
                
                
        return ans
