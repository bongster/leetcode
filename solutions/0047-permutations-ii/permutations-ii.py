# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
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
