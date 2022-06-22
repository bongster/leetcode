# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
#
#
# 	answer[i] % answer[j] == 0, or
# 	answer[j] % answer[i] == 0
#
#
# If there are multiple solutions, return any of them.
#
#  
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [1,2]
# Explanation: [1,3] is also accepted.
#
#
# Example 2:
#
#
# Input: nums = [1,2,4,8]
# Output: [1,2,4,8]
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 1000
# 	1 <= nums[i] <= 2 * 109
# 	All the integers in nums are unique.
#
#


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        path = [-1] * n
        iMax = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    path[i] = j
                    
            if dp[iMax] < dp[i]:
                iMax = i
                
        ans = []
        while iMax >= 0:
            ans.append(nums[iMax])
            iMax = path[iMax]
        return ans[::-1]
