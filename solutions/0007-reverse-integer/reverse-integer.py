# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#


class Solution:
    def reverse(self, x: int) -> int:
        max_digit_num = 0
        offset = -1 if x < 0 else 1
        x *= offset
        y = x
        while y > 0:
            y = int(y / 10)
            max_digit_num += 1
        
        res = 0
        i = 0
        while x > 0:
            v, x = int(x % 10), int(x / 10)
            # print(i, res, v, x)
            res += v * (10 ** (max_digit_num - i -1))
            i = i + 1
        
        res = res * offset
        # check overflow
        max_integer = 2**31 - 1
        min_integer = 2**31 * -1

        if min_integer > res or res > max_integer:
            return 0
        else:
            return res
    
