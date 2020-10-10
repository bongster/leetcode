# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
#
#  
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Example 3:
# Input: haystack = "", needle = ""
# Output: 0
#
#  
# Constraints:
#
#
# 	0 <= haystack.length, needle.length <= 5 * 104
# 	haystack and needle consist of only lower-case English characters.
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
                
            
