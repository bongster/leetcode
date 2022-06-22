# A positive integer is magical if it is divisible by either a or b.
#
# Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.
#
#  
# Example 1:
#
#
# Input: n = 1, a = 2, b = 3
# Output: 2
#
#
# Example 2:
#
#
# Input: n = 4, a = 2, b = 3
# Output: 6
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 109
# 	2 <= a, b <= 4 * 104
#
#


class Solution:
    def gcd(self, x, y):
        while y > 0:
            x, y = y, x % y
        return x
    
    def lcm (self, A, B):
        return (A * B) // self.gcd(A, B)
    
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        temp = self.lcm(a, b)
        seq = {}
        for i in range(1, temp // a + 1):
            seq[i * a] = 1
        for i in range(1, temp // b + 1):
            seq[i * b] = 1
        cand = sorted([key for key, value in seq.items()])
        ans = ( (n-1) // len(cand) ) * cand[-1] + cand[ n % len(cand)-1]
        return ans % (10**9+7)
        
        
