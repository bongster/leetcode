# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
#
#  
# Example 1:
#
#
# Input: n = 3
# Output: 5
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 19
#
#


class Solution:
    memories = {}
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        if self.memories.get(n):
            return self.memories.get(n)
        count = 0
        
        for i in range(1, n + 1):
            count += self.numTrees(i - 1) * self.numTrees(n - i);
        self.memories[n] = count
        return count
