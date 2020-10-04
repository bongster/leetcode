# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#


class Solution:
    # def solve(self, nums, results, subset, start_index):
    #     print(f"{subset}, {results}")
    #     results.append(subset.copy())
    #     for i in range(start_index, len(nums)):
    #         subset.append(nums[i])
    #         self.solve(nums, results, subset, i + 1)
    #         subset.pop()
    def dfs(self, i, subset, res, nums):
        if (i == len(nums)):
            # print("ggggg", subset)
            res.append(subset.copy())
            return
        
        # not choose nums[i], no need to restore
        self.dfs(i + 1, subset, res, nums)
        
        # not choose nums[i], no need to restore
        # subset.append(nums[i])
        self.dfs(i + 1, subset + [nums[i]], res, nums)
        # subset.pop()
        
        
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        results = []
        self.dfs(0, subset, results, nums)
        return results
