# Given two strings s and t, return the number of distinct subsequences of s which equals t.
#
# A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# The test cases are generated so that the answer fits on a 32-bit signed integer.
#
#  
# Example 1:
#
#
# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from S.
# rabbbit
# rabbbit
# rabbbit
#
#
# Example 2:
#
#
# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from S.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
#
#  
# Constraints:
#
#
# 	1 <= s.length, t.length <= 1000
# 	s and t consist of English letters.
#
#


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Timeout limit error
#         N = len(s)
#         def dfs(s, t):
#             if not t:
#                 return 1
#             if not s or len(s) < len(t):
#                 return 0
            
#             ans = 0
#             N = len(s)
#             for i in range(N):
#                 if s[i] == t[0]:
#                     ans += dfs(s[i + 1:], t[1:])
#             return ans
        
#         ans = dfs(s, t)
        M = len(s)
        N = len(t)
        dp = [[0] * (M + 1) for _ in range(N +  1)]
    
        for i in range(M + 1):
            dp[0][i] = 1
        
        for i, m in enumerate(t):
            for j, n in enumerate(s):
                if m == n:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j];
        return dp[-1][-1]
        
        
