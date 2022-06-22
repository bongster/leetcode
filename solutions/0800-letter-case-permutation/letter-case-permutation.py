# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
#
# Return a list of all possible strings we could create. Return the output in any order.
#
#  
# Example 1:
#
#
# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
#
#
# Example 2:
#
#
# Input: s = "3z4"
# Output: ["3z4","3Z4"]
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 12
# 	s consists of lowercase English letters, uppercase English letters, and digits.
#
#


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def permutation(sub: str = "", i: int = 0):
            if len(sub) == len(S):
                res.append(sub)
            else:
                if S[i].isalpha():
                    permutation(sub + S[i].swapcase(), i + 1)
                permutation(sub + S[i], i + 1)
        res = []
        permutation()
        print(res)
        return res
