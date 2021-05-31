# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.
#
# Return the shortest such subarray and output its length.
#
#  
# Example 1:
#
#
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4]
# Output: 0
#
#
# Example 3:
#
#
# Input: nums = [1]
# Output: 0
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 104
# 	-105 <= nums[i] <= 105
#
#
#  
# Follow up: Can you solve it in O(n) time complexity?


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        end = -2;
        mn = sys.maxsize
        mx = -sys.maxsize - 1
        
        for i in range(N):
            mx = max(mx, nums[i])
            if nums[i] < mx:
                end = i
        
        begin = -1
        
        for i in range(N-1, -1, -1):
            mn = min(mn, nums[i])
            if nums[i] > mn:
                begin = i
        
        print(begin, end)
        return end - begin + 1
