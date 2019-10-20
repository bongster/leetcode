# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
#
# 	I can be placed before V (5) and X (10) to make 4 and 9. 
# 	X can be placed before L (50) and C (100) to make 40 and 90. 
# 	C can be placed before D (500) and M (1000) to make 400 and 900.
#
#
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
#
#
# Input: 3
# Output: "III"
#
# Example 2:
#
#
# Input: 4
# Output: "IV"
#
# Example 3:
#
#
# Input: 9
# Output: "IX"
#
# Example 4:
#
#
# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
#
#
# Example 5:
#
#
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#


class Solution:
    simple_map = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000,
    }
    
    def intToRoman(self, num: int) -> str:
        
        def solve(num, res, i) -> str:
            # print(i, num, res, int(num[0]) * 10**i)
            if i < 0 or num == '0':
                return res
            
            max_i = list(filter(lambda key: self.simple_map[key] <= int(num), self.simple_map.keys()))[-1]
            
            max_v = self.simple_map[max_i]
            int_num = int(num)
            # print(max_i, max_v, int_num)
            while int_num >= max_v:
                int_num -= max_v
                res += max_i
            # print(res, int_num)
            return solve(str(int_num), res, 0 if i == 0 else i - 1)
        
        str_num = str(num)
        res = solve(str_num, '', len(str_num) - 1)
        # print(res)
        return res