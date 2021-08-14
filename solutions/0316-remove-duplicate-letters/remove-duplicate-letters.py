# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
#
#  
# Example 1:
#
#
# Input: s = "bcabc"
# Output: "abc"
#
#
# Example 2:
#
#
# Input: s = "cbacdcbc"
# Output: "acdb"
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 104
# 	s consists of lowercase English letters.
#
#
#  
# Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
#


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = []
        remaining = Counter(s)
        res = []
        for c in s:
            if c not in res:
                while res and res[-1] >= c and remaining[res[-1]] > 0:
                    res.pop()
                res.append(c)
            remaining[c] -=1
        return "".join(res)
