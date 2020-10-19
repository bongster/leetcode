# All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
#  
# Example 1:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:
# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
#
#  
# Constraints:
#
#
# 	0 <= s.length <= 105
# 	s[i] is 'A', 'C', 'G', or 'T'.
#
#


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []
        if n == 10:
            return []
        res = []
        for i in range(n - 10 + 1):
            res.append(s[i:i+10])
        answer = [ k for k, v in collections.Counter(res).items() if v > 1]
        print(answer)
        return answer
        
            
        
