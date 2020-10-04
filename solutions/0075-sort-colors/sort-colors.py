# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Follow up:
#
#
# 	Could you solve this problem without using the library's sort function?
# 	Could you come up with a one-pass algorithm using only O(1) constant space?
#
#
#  
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
# Example 3:
# Input: nums = [0]
# Output: [0]
# Example 4:
# Input: nums = [1]
# Output: [1]
#
#  
# Constraints:
#
#
# 	n == nums.length
# 	1 <= n <= 300
# 	nums[i] is 0, 1, or 2.
#
#


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = [0, 0, 0]
        for num in nums:
            c[num] += 1
        
        for i in range(1, len(c)):
            c[i] += c[i - 1]
        print(c)
        output = [0] * len(nums)
        for i in range(len(nums)):
            print(i, nums[i], c[nums[i]] -1)
            output[c[nums[i]] - 1] = nums[i]
            c[nums[i]] -= 1
        
        for i in range(len(output)):
            nums[i] = output[i]
"""
[2,0,2,1,1,0]

[2, 4, 5]
[ , , , , ,2]
2, 5

"""
