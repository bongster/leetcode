# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
#
#  
# Example 1:
#
#
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#
#
# Example 2:
#
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 8
# 	-10 <= nums[i] <= 10
#
#


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def solve(begin, nums, res):
            if begin == len(nums):
                if nums not in res:
                    res.append(nums.copy())
                return res
            
            for i in range(begin, len(nums)):
                nums[i], nums[begin] = nums[begin], nums[i]
                solve(begin + 1, nums, res)
                nums[i], nums[begin] = nums[begin], nums[i]
        
        res = []
        solve(0, nums, res)
        return res
