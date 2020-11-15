# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#  
# Example 1:
#
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 45
#
#


class Solution:
    def climbStairs(self, n: int) -> int:
        # recursive
        def solve(remainStairs, n):
            # print(remainStairs, n)
            if remainStairs == 0:
                return 1
            elif remainStairs < 0:
                return 0
            else:
                return solve(remainStairs - 2, n) + solve(remainStairs -1, n)
        
        # res = solve(n, n)
        # return res
        
        # recursive and memorization
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        climb_arr = [0] * (n + 1)
        climb_arr[1] = 1
        climb_arr[2] = 2
        
        for i in range(3, n + 1):
            climb_arr[i] = climb_arr[i - 2] + climb_arr[i - 1]
        
        return climb_arr[n]
