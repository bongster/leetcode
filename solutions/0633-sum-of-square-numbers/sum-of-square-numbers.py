# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
#
#  
# Example 1:
#
#
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
#
#
# Example 2:
#
#
# Input: c = 3
# Output: false
#
#
#  
# Constraints:
#
#
# 	0 <= c <= 231 - 1
#
#


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # def binary_search(l, r, n):
        #     if l > r:
        #         return False
        #     mid = l + (r - l) // 2
        #     if mid * mid == n:
        #         return True
        #     if mid * mid > n:
        #         r = mid - 1
        #         return binary_search(l, r, n)
        #     return binary_search(mid + 1, r, n)
        # i = 0
        # while i * i <= c:
        #     b = c - (i * i)
        #     if binary_search(0, b, b):
        #         return True
        #     i += 1
        # return False
        dp = []
        i = 0
        while i * i <= c:
            dp.append(c - i * i)
            i += 1
        for x in dp:
            if math.sqrt(x) % 1 == 0:
                return True
        return False
