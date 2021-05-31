# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
#  
# Example 1:
# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321
# Example 3:
# Input: x = 120
# Output: 21
# Example 4:
# Input: x = 0
# Output: 0
#
#  
# Constraints:
#
#
# 	-231 <= x <= 231 - 1
#
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
    
