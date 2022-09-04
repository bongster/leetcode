# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
#  
# Example 1:
#
#
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#
#
# Example 2:
#
#
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
#
#
#  
# Constraints:
#
#
# 	1 <= haystack.length, needle.length <= 104
# 	haystack and needle consist of only lowercase English characters.
#
#


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if not haystack and not needle:
            return 0
        elif not haystack and needle:
            return -1
        elif haystack and not needle:
            return 0
        
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        if needle_len > haystack_len:
            return -1
        
        find_inx = -1
        for i in range(haystack_len - needle_len + 1):
            if haystack[i] == needle[0] and haystack[i:needle_len + i] == needle:
                find_inx = i
                break
        
        return find_inx
                
            
