# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
#  
# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:
# Input: s = "God Ding"
# Output: "doG gniD"
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 5 * 104
# 	s contains printable ASCII characters.
# 	s does not contain any leading or trailing spaces.
# 	There is at least one word in s.
# 	All the words in s are separated by a single space.
#
#


class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for ss in s.split(' '):
            ss = [c for c in ss]
            for i in range(len(ss) // 2):
                ss[i], ss[len(ss) -i - 1] = ss[len(ss) -i - 1], ss[i]
            res.append("".join(ss))
        
        return " ".join(res)
