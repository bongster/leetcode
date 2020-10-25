# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
#  
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
#
#
# Example 2:
#
#
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 105].
# 	-1000 <= Node.val <= 1000
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = []
        root.depth = 1
        min_depth = None
        queue.append(root)
        while len(queue):
            s, queue = queue[0], queue[1:]
            # print(s.val, s.depth)
            if s.left:
                s.left.depth = s.depth + 1
                queue.append(s.left)
            
            if s.right:
                s.right.depth = s.depth + 1
                queue.append(s.right)
            
            if not s.left and not s.right:
                if not min_depth:
                    min_depth = s.depth
                else:
                    min_depth = min(min_depth, s.depth)
            
        return min_depth
