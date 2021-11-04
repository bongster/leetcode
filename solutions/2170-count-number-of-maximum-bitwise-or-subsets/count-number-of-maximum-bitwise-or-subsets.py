# Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.
#
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.
#
# The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
#
#  
# Example 1:
#
#
# Input: nums = [3,1]
# Output: 2
# Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
# - [3]
# - [3,1]
#
#
# Example 2:
#
#
# Input: nums = [2,2,2]
# Output: 7
# Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.
#
#
# Example 3:
#
#
# Input: nums = [3,2,1,5]
# Output: 6
# Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
# - [3,5]
# - [3,1,5]
# - [3,2,5]
# - [3,2,1,5]
# - [2,5]
# - [2,1,5]
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 16
# 	1 <= nums[i] <= 105
#
#


import functools
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Brute force is not working got a timelimit
        maxOr = 0
        for num in nums:
            maxOr |= num

        self.ans = 0
        def permutations(mask, i):
            if i == len(nums):
                if mask == maxOr:
                    self.ans += 1
                return
            
            permutations(mask|nums[i], i+1) #Add Number to our bitmask
            permutations(mask, i+1)         #Don't add number to bitmask
            
        permutations(0, 0)
        return self.ans
    
        # if not len(nums):
        #     return 0
        # x = functools.reduce(lambda x, y: x | y, nums)
        # queue = []
        # visited = [True] * len(nums)
        # queue.append(visited)
        # ans = 1
        # subset = []
        # while len(queue):
        #     q = queue.pop()
        #     if q not in subset:
        #         subset.append(q.copy())
        #     for i in range(len(q)):
        #         if not q[i]:
        #             continue
        #         q[i] = False
        #         queue.append(q.copy())
        #         q[i] = True
        # ans = 0
        # for s in subset:
        #     ss = [nums[i] for i, b in enumerate(s) if b]
        #     if not len(ss):
        #         continue
        #     if functools.reduce(lambda x, y: x | y, ss) == x:
        #         ans += 1
                
#         if not len(nums):
#             return 0
#         x = functools.reduce(lambda x, y: x | y, nums)
#         queue = []
#         queue.append(nums)
#         ans = 1
#         xx = [[nums]]
#         while len(queue):
#             q = queue.pop()
#             if q not in xx:
#                 xx.append(q)
#             for i in range(len(q)):
#                 subset = q[0:i] + q[i + 1:]
#                 if not subset:
#                     continue
                
#                 if functools.reduce(lambda x, y: x | y, subset) == x:
#                     # I thought i need to more when i add result in theirs cuz in duplicated number i got a return e.g) 2,2,2
#                     ans += 1
#                     queue.append(subset)
#         return ans
                
        
