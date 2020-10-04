# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
#
# Example:
#
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
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
