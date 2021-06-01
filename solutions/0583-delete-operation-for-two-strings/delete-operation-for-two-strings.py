# Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
#
# In one step, you can delete exactly one character in either string.
#
#  
# Example 1:
#
#
# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
#
#
# Example 2:
#
#
# Input: word1 = "leetcode", word2 = "etco"
# Output: 4
#
#
#  
# Constraints:
#
#
# 	1 <= word1.length, word2.length <= 500
# 	word1 and word2 consist of only lowercase English letters.
#
#


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1_len = len(word1)
        word2_len = len(word2)
        
        dp = [0] * (word1_len + 1)
        for i in range(len(dp)):
            dp[i] = [0] * (word2_len + 1)
        for i in range(word1_len + 1):
            for j in range(word2_len + 1):
                if i == 0 or j == 0:
                    continue
                if word1[i - 1] == word2[j -1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return word1_len + word2_len - 2 * dp[word1_len][word2_len]
