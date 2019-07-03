# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        overflow = 0
        while a or b:
            len_a, len_b = len(a) -1, len(b) -1
            if not a and b:
                last_a = 0
                last_b, b = int(b[len_b]), b[:len_b]
            elif a and not b:
                last_a, a = int(a[len_a]), a[:len_a]
                last_b = 0
            else:
                last_a, a = int(a[len_a]), a[:len_a]
                last_b, b = int(b[len_b]), b[:len_b]

            v = last_a + last_b + overflow
            if v > 1:
                overflow = 1
                v = v - 2
            else:
                overflow = 0
            res = str(v) + res
        
        if overflow:
            res = "1" + res
        
        return res
