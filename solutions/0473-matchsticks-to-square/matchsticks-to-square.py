# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
#
# Return true if you can make this square and false otherwise.
#
#  
# Example 1:
#
#
# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
#
#
# Example 2:
#
#
# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.
#
#
#  
# Constraints:
#
#
# 	1 <= matchsticks.length <= 15
# 	1 <= matchsticks[i] <= 108
#
#


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)

        side = perimeter // 4
        if side * 4 != perimeter:
            return False
        matchsticks.sort(reverse = True)
        res = [0 for _ in range(4)]

        def backtrack(index):
            if index == len(matchsticks):
                return side == res[0] == res[1] == res[2]

            for i in range(4):
                if res[i] + matchsticks[index] <= side:
                    res[i] += matchsticks[index]
                    ret = backtrack(index + 1)
                    if ret:
                        return True
                    res[i] -= matchsticks[index]

                    if res[i] == 0:
                        break

            return False

        return backtrack(0)
