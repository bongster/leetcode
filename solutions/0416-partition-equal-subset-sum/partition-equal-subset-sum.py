# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
#
#  
# Example 1:
#
#
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 200
# 	1 <= nums[i] <= 100
#
#


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        """
        Memoization (TLE)
        """        
#         visited = [False] * n
#         def dfs(i, x, target):
#             if i < n and not visited[i] and target > 0:
#                 if x == target:
#                     return True
                
#                 visited[i] = True
#                 for j in range(i + 1, n):
#                     if dfs(j, x + nums[j], target - nums[j]):
#                         return True
#                 visited[i] = False
#                 return False
#             else:
#                 return False
        
#         return dfs(0, nums[0], sum(nums) - nums[0])
        """
        DP
        """
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(target + 1):
                if i == 0 or j == 0:
                    dp[i][j] = False
                elif nums[i - 1] > j:
                    dp[i][j] = dp[i -1][j]
                elif nums[i - 1] == j:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i-1][j] or dp[i -1][j - nums[i -1]]
        return dp[n][target]
