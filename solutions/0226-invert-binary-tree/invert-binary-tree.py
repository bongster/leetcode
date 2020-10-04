# Invert a binary tree.
#
# Example:
#
# Input:
#
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
# Output:
#
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
#
# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
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
