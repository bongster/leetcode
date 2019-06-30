# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# Example 1:
#
#
# Input: s = "egg", t = "add"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "foo", t = "bar"
# Output: false
#
# Example 3:
#
#
# Input: s = "paper", t = "title"
# Output: true
#
# Note:
# You may assume both s and t have the same length.
#


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not len(s) and not len(t):
            return True
        
        if not len(s) or not len(t):
            return False
        
        s_map = {}
        t_map = {}
        res = True
        i = 0
        while i < len(s):
            sc = s_map.get(s[i])
            # print(s[i], sc, t[i])
            if sc and sc != t[i]:
                res = False
                break
            elif not sc and t_map.get(t[i]):
                res = False
                break
            else:
                s_map[s[i]] = t[i]
                t_map[t[i]] = s[i]
                i += 1
        
        return res
                
            
