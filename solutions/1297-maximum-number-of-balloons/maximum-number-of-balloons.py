# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
#
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
#
#  
# Example 1:
#
#
#
#
# Input: text = "nlaebolko"
# Output: 1
#
#
# Example 2:
#
#
#
#
# Input: text = "loonbalxballpoon"
# Output: 2
#
#
# Example 3:
#
#
# Input: text = "leetcode"
# Output: 0
#
#
#  
# Constraints:
#
#
# 	1 <= text.length <= 10^4
# 	text consists of lower case English letters only.
#


from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if not text:
            return 0
        a = Counter(text)
        test=list("balon")
        res = []
        for k, v in a.items():
            if k == 'l' or k == 'o':
                if v < 2:
                    return 0
                else:
                    test.remove(k)
                    res.append(v//2)
                    continue
            if k in test:
                test.remove(k)
                res.append(v)
        if test == []:
            return min(res)
        return 0
                
