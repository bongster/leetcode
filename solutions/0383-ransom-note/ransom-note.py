# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#  
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#  
# Constraints:
#
#
# 	1 <= ransomNote.length, magazine.length <= 105
# 	ransomNote and magazine consist of lowercase English letters.
#
#


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = [r for r in ransomNote]
        magazine = [r for r in magazine]
        while len(ransomNote):
            f, ransomNote = ransomNote[0], ransomNote[1:]
            try:
                index = magazine.index(f)
                del magazine[index]
            except:
                return False
        return True
