# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.
#
#  
# Example 1:
#
#
# Input: left = 5, right = 7
# Output: 4
#
#
# Example 2:
#
#
# Input: left = 0, right = 0
# Output: 0
#
#
# Example 3:
#
#
# Input: left = 1, right = 2147483647
# Output: 0
#
#
#  
# Constraints:
#
#
# 	0 <= left <= right <= 231 - 1
#
#


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Calculate what is the 2 to the N power between left, right
        if two values are not same then don't need to caluclate so return 0
        if two values are same then running bitwise between left and right
        """
        # Got left numbers 2 to the N power
        # i = 0
        # while True:
        #     if left < 2 ** i:
        #         break
        #     i += 1 
        # # Got right numbers 2 to the N power
        # j = 0
        # while True:
        #     if right < 2 ** j:
        #         break
        #     j += 1
        # Checking the value is same or not
        if right >= left * 2:
            return 0
        
        # running iterate then calculate bitwise.
        res = left
        for n in range(left + 1, right + 1):
            res &= n
            if not res:
                return res
        
        return res
        
