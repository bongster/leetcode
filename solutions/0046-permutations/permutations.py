# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
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
        
