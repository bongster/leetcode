# Given a binary array nums, return the maximum number of consecutive 1's in the array.
#
#  
# Example 1:
#
#
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
#
#
# Example 2:
#
#
# Input: nums = [1,0,1,1,0,1]
# Output: 2
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 105
# 	nums[i] is either 0 or 1.
#
#


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return int(nums[0] == 1)
        dp = [0] * N
        if nums[0] == 1:
            dp[0] = 1
        ans = dp[0]
        for i in range(1, N):
            if nums[i] == 1:
                dp[i] = dp[i -1] + 1
            ans = max(ans, dp[i])
        
        return ans
            
