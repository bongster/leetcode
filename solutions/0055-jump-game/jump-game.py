# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
#
#  
# Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 104
# 	0 <= nums[i] <= 105
#
#


class Solution:
    def canJump(self, nums: List[int]) -> bool:
#         def dfs(index, last_index):
#             if index == last_index:
#                 return True
#             if index > last_index:
#                 return False
            
#             for j in range(1, nums[index] + 1):
#                 if dfs(index + j, last_index):
#                     return True
#             return False
    
#         ans = dfs(0, len(nums) -1)

        # return ans
        # BFS
#         stack = [0]
#         target = len(nums) -1    
#         visited = [False] * len(nums)
#         while len(stack):
#             i, stack = stack[0], stack[1:]
#             if i == target:
#                 return True
#             for j in range(1, min(nums[i] + 1, target + 1)):
#                 if i + j == target:
#                     return True
#                 elif i + j < target:
#                     if not visited[i + j]:
#                         visited[i + j] = True
#                         stack.append(i + j)
#         return False
    
        maximum, n = 0, len(nums)
        for i in range(len(nums)):
            if maximum < i:
                return False
            if maximum >= len(nums) - 1:
                return True
            maximum = max(maximum, i + nums[i])
    
        return ans
