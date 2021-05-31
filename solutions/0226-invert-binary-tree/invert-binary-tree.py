# Given the root of a binary tree, invert the tree, and return its root.
#
#  
# Example 1:
#
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#
#
# Example 2:
#
#
# Input: root = [2,1,3]
# Output: [2,3,1]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 100].
# 	-100 <= Node.val <= 100
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        queue = [root]
        
        while len(queue):
            t, queue = queue[0], queue[1:]
            temp = t.left
            t.left = t.right
            t.right = temp
            
            if t.left:
                queue.append(t.left)
            if t.right:
                queue.append(t.right)
                
#             if t.left and t.right:
                
#                 queue.append(t.left)
#                 queue.append(t.right)
#             elif t.left:
#                 t.right = t.left
#                 t.left = None
#                 queue.append(t.right)
#             elif t.right:
#                 t.left = t.right
#                 t.right = None
#                 queue.append(t.left)
        return root
