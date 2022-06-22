# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#  
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#  
# Constraints:
#
#
# 	1 <= s.length, t.length <= 5 * 104
# 	s and t consist of lowercase English letters.
#
#
#  
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
#


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        anagram
        nagaram
        
        1111000
        anag
        naga
        anag
        aang
        """
        
        diff_s = []
        diff_t = []
        if len(s) != len(t): 
            return False
        
        for i in range(len(s)):
            if s[i] != t[i]:
                diff_s.append(s[i])
                diff_t.append(t[i])
        diff_s = sorted(diff_s)
        diff_t = sorted(diff_t)
        return ''.join(diff_s) == ''.join(diff_t)
