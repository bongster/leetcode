# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#
#
# 	0 <= a, b, c, d < n
# 	a, b, c, and d are distinct.
# 	nums[a] + nums[b] + nums[c] + nums[d] == target
#
#
# You may return the answer in any order.
#
#  
# Example 1:
#
#
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
#
# Example 2:
#
#
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 200
# 	-109 <= nums[i] <= 109
# 	-109 <= target <= 109
#
#


class Solution:
    def generate(self, target, nums, res):
        if len(target) == 4:
            target.sort()
            if target not in res:
                res.append(target)
            return
        N = len(nums)
        for i in range(N):
            self.generate(target + [nums[i]], nums[0:i] + nums[i + 1:N], res)
        
        
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # O(N^4)
        # N = len(nums)
        # res = []
        # self.generate([], nums, res)
        # ans = []
        # for i in res:
        #     if sum(i) == target:
        #         ans.append(i)
        # return ans
        
        # TDOO: O(N^2)
        nums.sort()
        # print(nums)
        n = len(nums)
        ans = []
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                left = j + 1
                right = n - 1
                while left < right:
                    v = [nums[i], nums[j], nums[left], nums[right]]
                    # print(v)
                    if sum(v) > target:
                        right -= 1
                    else:
                        if sum(v) == target and v not in ans:
                            ans.append(v)
                        left += 1
        # print(ans)
        return ans

