# Given a string s, find the length of the longest substring without repeating characters.
#
#  
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
# Example 4:
#
#
# Input: s = ""
# Output: 0
#
#
#  
# Constraints:
#
#
# 	0 <= s.length <= 5 * 104
# 	s consists of English letters, digits, symbols and spaces.
#
#


from functools import reduce

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
    
        res = [0] * len(s)
        
        for i, c in enumerate(s[:len(s)]):
            sub_s = ""
            sub_i = i
            while sub_i < len(s):
                if s[sub_i] in sub_s:
                    break
                else:
                    sub_s += s[sub_i]
                    sub_i += 1
            res[i] = sub_s
        max_sub = reduce(lambda x, y: x if len(x) > len(y) else y, res)

        return len(max_sub)
