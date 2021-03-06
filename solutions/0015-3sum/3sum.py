# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Notice that the solution set must not contain duplicate triplets.
#
#  
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []
#
#  
# Constraints:
#
#
# 	0 <= nums.length <= 3000
# 	-105 <= nums[i] <= 105
#
#


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            k = 0 - nums[i]
            low, high = i+1, len(nums) - 1

            while low < high:
                if nums[low] + nums[high] < k:
                    low += 1
                elif nums[low] + nums[high] > k:
                    high -= 1
                elif nums[low] + nums[high] == k:
                    res.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    while low < high and nums[low] == nums[high-1]:
                        high -= 1
                    low += 1
                    high -= 1

        return res
