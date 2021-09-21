# Given an integer array nums, return the number of all the arithmetic subsequences of nums.
#
# A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
#
#
# 	For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
# 	For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
#
#
# A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.
#
#
# 	For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
#
#
# The test cases are generated so that the answer fits in 32-bit integer.
#
#  
# Example 1:
#
#
# Input: nums = [2,4,6,8,10]
# Output: 7
# Explanation: All arithmetic subsequence slices are:
# [2,4,6]
# [4,6,8]
# [6,8,10]
# [2,4,6,8]
# [4,6,8,10]
# [2,4,6,8,10]
# [2,6,10]
#
#
# Example 2:
#
#
# Input: nums = [7,7,7,7,7]
# Output: 16
# Explanation: Any subsequence of this array is arithmetic.
#
#
#  
# Constraints:
#
#
# 	1  <= nums.length <= 1000
# 	-231 <= nums[i] <= 231 - 1
#
#


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # brute force get timelimit Exceeded
#         sequences = []
#         def get_sub_sequence(i, max_length, ans):
#             if len(ans) == max_length:
#                 if ans not in sequences:
#                     sequences.append(ans)
#                 return
#             if i > len(nums):
#                 return
            
#             for j in range(i + 1, len(nums) + 1):
#                 get_sub_sequence(j, max_length, ans + [i])
                
#         for i in range(3, len(nums) + 1):
#             for j in range(len(nums) - 2):
#                 get_sub_sequence(j, i, [])
        
#         ans = 0
#         for x in sequences:
#             different = nums[x[1]] - nums[x[0]]
#             check = True
#             for j in range(2, len(x)):
#                 if nums[x[j]] - nums[x[j -1]] != different:
#                     check = False
#                     break
#             if check:
#                 ans += 1
#         return ans
        ans = 0
        m = {}
        for i in range(len(nums)):
            m[i] = dict()
            for j in range(i):
                diff = nums[j] - nums[i]
                
                if diff not in m[i]:
                    m[i][diff] = 0
                if diff not in m[j]:
                    m[j][diff] = 0
                n2 = m[i][diff]
                n1 = m[j][diff]
                ans += n1
                freq = n1 + n2 + 1
                m[i][diff] = freq
            # print(m[i], ans)
        return ans
                
                
