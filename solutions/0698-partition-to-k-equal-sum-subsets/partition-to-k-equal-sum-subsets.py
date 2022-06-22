# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.
#
#  
# Example 1:
#
#
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4], k = 3
# Output: false
#
#
#  
# Constraints:
#
#
# 	1 <= k <= nums.length <= 16
# 	1 <= nums[i] <= 104
# 	The frequency of each element is in the range [1, 4].
#
#


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 0 or sum(nums) % k != 0:
            return False
        v = sum(nums) // k
        used = [False] * len(nums)
        def can_partition(index, arr, used, k, sum_of_num, target):
            if k == 0:
                return True
            if sum_of_num == target:
                return can_partition(0, arr, used, k -1, 0, target)
            for i in range(index, len(arr)):
                if not used[i]:
                    used[i] = True
                    if can_partition(i + 1, arr, used, k, sum_of_num + arr[i], target):
                        return True
                    used[i] = False
            return False
        
        return can_partition(0, nums, used, k, 0, v)
