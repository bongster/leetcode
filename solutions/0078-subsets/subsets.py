# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
#  
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# Example 2:
#
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 10
# 	-10 <= nums[i] <= 10
# 	All the numbers of nums are unique.
#
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
