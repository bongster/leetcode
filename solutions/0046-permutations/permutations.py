# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#
#  
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 6
# 	-10 <= nums[i] <= 10
# 	All the integers of nums are unique.
#
#


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # from staring point to num size, swap between char
        def solve(begin, nums, res):
            # print(begin, nums, res)
            if begin >= len(nums):
                # print('num is', nums)
                res.append(nums.copy())
            
            for i in range(begin, len(nums)):
                nums[i], nums[begin] = nums[begin], nums[i]
                solve(begin + 1, nums, res)
                nums[i], nums[begin] = nums[begin], nums[i]
        
        res = []
        solve(0, nums, res)
        # print(res)
        return res
        
