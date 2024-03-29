# A substring is a contiguous (non-empty) sequence of characters within a string.
#
# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.
#
# Given a string word, return the number of vowel substrings in word.
#
#  
# Example 1:
#
#
# Input: word = "aeiouu"
# Output: 2
# Explanation: The vowel substrings of word are as follows (underlined):
# - "aeiouu"
# - "aeiouu"
#
#
# Example 2:
#
#
# Input: word = "unicornarihan"
# Output: 0
# Explanation: Not all 5 vowels are present, so there are no vowel substrings.
#
#
# Example 3:
#
#
# Input: word = "cuaieuouac"
# Output: 7
# Explanation: The vowel substrings of word are as follows (underlined):
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
#
#
#  
# Constraints:
#
#
# 	1 <= word.length <= 100
# 	word consists of lowercase English letters only.
#
#


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        res = 0
        if n < 5:
            return res
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        for i in range(n):
            x = ['a', 'e', 'i', 'o', 'u']
            k = 0
            for j in range(i, n):
                # print(word[j], x)
                if word[j] in vowels:
                    if word[j] in x:
                        x.remove(word[j])
                    if not len(x):
                        res += 1
                else:
                    break
        return res
                
            
            
