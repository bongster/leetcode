# Given a string s, return the longest palindromic substring in s.
#
#  
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 1000
# 	s consist of only digits and English letters.
#
#


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_palindrome(sub_s):
            return s[i:j] == s[i:j][::-1]
                
        res = ""
        for i in range(len(s)):
            j = len(s)
            while j > i:
                check_str = s[i:j]
                checked = check_palindrome(check_str)
                # print(len(check_str), len(res), checked)
                if checked:
                    res = res if len(res) > len(check_str) else check_str
                    # print(len(check_str), len(res))
                    break
                j -= 1
            
            # check own str are check_palindrome
            if len(res) > len(s[i:]):
                break
        # raise a time limit exceeded error because time complex are N^2
        return res

