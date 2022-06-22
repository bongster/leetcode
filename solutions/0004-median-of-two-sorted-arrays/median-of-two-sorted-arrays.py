# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
#  
# Example 1:
#
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
#  
# Constraints:
#
#
# 	nums1.length == m
# 	nums2.length == n
# 	0 <= m <= 1000
# 	0 <= n <= 1000
# 	1 <= m + n <= 2000
# 	-106 <= nums1[i], nums2[i] <= 106
#
#


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        if n == 1:
            return (nums1 + nums2)[0]
        m = n // 2 + 1
        ans = 0
        prev = 0
        while m > 0:
            if len(nums1) and len(nums2):
                if nums1[0] < nums2[0]:
                    prev = ans
                    ans, nums1 = nums1[0], nums1[1:]
                    m -= 1
                else:
                    prev = ans
                    ans, nums2 = nums2[0], nums2[1:]
                    m -= 1
            elif len(nums1):
                prev = ans
                ans, nums1 = nums1[0], nums1[1:]
                m -= 1
            else:
                prev = ans
                ans, nums2 = nums2[0], nums2[1:]
                m -= 1
        # print(prev, ans)
        if n % 2 == 1:
            return ans
        else:
            return (ans + prev) / 2
