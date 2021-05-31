# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
#
#  
# Example 1:
#
#
# Input: x = 121
# Output: true
#
#
# Example 2:
#
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
#
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
# Example 4:
#
#
# Input: x = -101
# Output: false
#
#
#  
# Constraints:
#
#
# 	-231 <= x <= 231 - 1
#
#
#  
# Follow up: Could you solve it without converting the integer to a string?


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x_arr = []
        while x > 0:
            x, val = int(x / 10), int(x % 10)
            x_arr.append(val)
        
        res = True
        x_arr_len = len(x_arr)
        for i in range(int(x_arr_len / 2)):
            if x_arr[i] != x_arr[x_arr_len - i - 1]:
                res = False
                break
    
        return res
            
