# You are given several boxes with different colors represented by different positive numbers.
#
# You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.
#
# Return the maximum points you can get.
#
#  
# Example 1:
#
#
# Input: boxes = [1,3,2,2,2,3,4,3,1]
# Output: 23
# Explanation:
# [1, 3, 2, 2, 2, 3, 4, 3, 1] 
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
# ----> [1, 3, 3, 3, 1] (1*1=1 points) 
# ----> [1, 1] (3*3=9 points) 
# ----> [] (2*2=4 points)
#
#
# Example 2:
#
#
# Input: boxes = [1,1,1]
# Output: 9
#
#
# Example 3:
#
#
# Input: boxes = [1]
# Output: 1
#
#
#  
# Constraints:
#
#
# 	1 <= boxes.length <= 100
# 	1 <= boxes[i] <= 100
#
#


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        def dfs(dp, boxes, left, right, streak):
            if left > right:
                return 0
            if left == right:
                return (streak + 1) ** 2
            if dp[left][right][streak] != 0:
                return dp[left][right][streak]
            
            maxValue = dfs(dp, boxes, left + 1, right, 0) + (streak + 1) ** 2
            for i in range(left +1, right + 1):
                if boxes[left] == boxes[i]:
                    maxValue = max(maxValue, dfs(dp, boxes, left + 1, i - 1, 0) + dfs(dp, boxes, i, right, streak + 1))
            dp[left][right][streak] = maxValue
            return maxValue
        
        n = len(boxes)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]
        return dfs(dp, boxes, 0, n -1, 0)
                
