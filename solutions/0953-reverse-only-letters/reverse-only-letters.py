# Given a string s, reverse the string according to the following rules:
#
#
# 	All the characters that are not English letters remain in the same position.
# 	All the English letters (lowercase or uppercase) should be reversed.
#
#
# Return s after reversing it.
#
#  
# Example 1:
# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 100
# 	s consists of characters with ASCII values in the range [33, 122].
# 	s does not contain '\"' or '\\'.
#
#


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        import re
        i = 0
        j = len(s) - 1
        k = [a for a in s]
        while i < j:
            si = re.match(r'[a-z|A-Z]', k[i])
            sj = re.match(r'[a-z|A-Z]', k[j])
            if not si:
                i += 1
            elif not sj:
                j -= 1
            else:
                k[i], k[j] = k[j], k[i]
                i += 1
                j -= 1
        return "".join(k)
        
