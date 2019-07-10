# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# Example:
#
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = None
        if len(nums) == 3:
            return sum(nums)
        
        for i in range(len(nums) - 2):
            low, high = i+1, len(nums) - 1
            k = target - nums[i]
            
            while low < high:
                comp_v = nums[low] + nums[high] + nums[i] - target
#                 print(
#                     nums[low],
#                     nums[high],
#                     nums[i],
#                     comp_v,
#                     k - nums[low] - nums[high],
#                     res,
#                 )
                
                if nums[low] + nums[high] < k:
                    if res == None:
                        res = comp_v
                    elif abs(res) > abs(comp_v):
                        res = comp_v
                    low += 1
                elif nums[low] + nums[high] > k:
                    if res == None:
                        res = comp_v
                    elif abs(res) > abs(comp_v):
                        res = comp_v
                    high -= 1
                else:
                    res = 0
                    break
        
        # print ('res:{}'.format(res))
        return res + target
        
            

            
