# You are given a string s and two integers x and y. You can perform two types of operations any number of times.
#
#
# 	Remove substring "ab" and gain x points.
#
#
# 		For example, when removing "ab" from "cabxbae" it becomes "cxbae".
#
#
# 	Remove substring "ba" and gain y points.
#
# 		For example, when removing "ba" from "cabxbae" it becomes "cabxe".
#
#
#
#
# Return the maximum points you can gain after applying the above operations on s.
#
#  
# Example 1:
#
#
# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.
#
# Example 2:
#
#
# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 105
# 	1 <= x, y <= 104
# 	s consists of lowercase English letters.
#
#


class Solution:
#     memoriation = {}
#     def solve(self, s: str, res: int, x:int, y: int ) -> int:
#         # TODO: create available string from s 
#         # run dynamic programming
#         ssList = set()
#         maxSum = res
#         if s in self.memoriation:
#             return self.memoriation[s]
        
#         for i in range(len(s) - 1):
#             sub_s = s[i: i+2]
#             remained_str = s[0:i] + s[i+2: len(s)]
#             if sub_s == 'ab':
#                 maxSum = max(maxSum, self.solve(remained_str, res + x, x, y))
#             elif sub_s == 'ba':
#                 maxSum = max(maxSum, self.solve(remained_str, res + y, x, y))
        
#         self.memoriation[s] = maxSum
        
#         return maxSum
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # return self.solve(s, 0, x, y)
        st = []
        # TODO: checking `ba`
        a = 'ab'
        b = 'ba'
        if y > x:
            a, b = b, a
            x, y = y, x
        print(a, b, x, y)
        res = 0
        for c in s:
            if not len(st):
                st.append(c)
            elif (st[-1] + c) == a:
                st.pop()
                res += x
            else:
                st.append(c)
        print(res, st)
        s = ''.join(st)
        st = []
        for c in s:
            if not len(st):
                st.append(c)
            elif (st[-1] + c) == b:
                st.pop()
                res += y
            else:
                st.append(c)
        print(res, st)
        return res
