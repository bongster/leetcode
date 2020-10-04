# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#  
# Example 1:
#
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
#  
# Constraints:
#
#
# 	0 <= strs.length <= 200
# 	0 <= strs[i].length <= 200
# 	strs[i] consists of only lower-case English letters.
#
#


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        if not len(strs):
            return ""
        
        short_str_len = min([len(s) for s in strs])
        res = ""
        while i < short_str_len:
            c = strs[0][i]
            is_same = True
            for s in strs:
                if c != s[i]:
                    is_same = False
                    break
            
            if is_same:
                res += c
            else:
                break
            
            i += 1
        
        print(res)
        return res

