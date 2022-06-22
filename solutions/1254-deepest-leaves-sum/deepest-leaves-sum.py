# Given the root of a binary tree, return the sum of values of its deepest leaves.
#  
# Example 1:
#
#
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
#
#
# Example 2:
#
#
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [1, 104].
# 	1 <= Node.val <= 100
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append((root, 0))
        level_sum = defaultdict(int)
        while queue:
            q, level = queue.pop()
            if q.left:
                queue.append((q.left, level + 1))
            if q.right:
                queue.append((q.right, level + 1))
            
            if not q.left and not q.right:
                level_sum[level] += q.val
        
        
        x = sorted(level_sum.items(), key=lambda item: item[0], reverse=True)
        return x[0][1]
