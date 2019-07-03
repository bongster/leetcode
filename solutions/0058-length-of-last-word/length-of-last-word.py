# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
#
# Input: "Hello World"
# Output: 5
#
#
#  
#


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = s.split()
        
        if not len(c):
            return 0
        
        return len(c[-1])
