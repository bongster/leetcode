# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
#
# Example 2:
#
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        index = len(digits) -1
        overflow = 0
        plus_one = 1
        while index >= 0:
            plus_num = digits[index] + plus_one + overflow
            print(plus_num)
            plus_one = 0
            if plus_num >= 10:
                overflow = 1
                digits[index] = plus_num - 10
                index -= 1
            else:
                overflow = 0
                digits[index] = plus_num
                break
        
        if overflow:
            digits.insert(0, overflow)
        return digits
