# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
#
#  
# Example 1:
#
#
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
#
#
# Example 2:
#
#
# Input: p = [1,2], q = [1,null,2]
# Output: false
#
#
# Example 3:
#
#
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#
#
#  
# Constraints:
#
#
# 	The number of nodes in both trees is in the range [0, 100].
# 	-104 <= Node.val <= 104
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        
        p_stack, q_stack = [], []
        p_stack.append(p)
        q_stack.append(q)
        res = True
        while len(p_stack):
            sp, p_stack = p_stack[0], p_stack[1:]
            sq, q_stack = q_stack[0], q_stack[1:]
            if (not sp and sq) or (sp and not sq):
                res = False
                break
            
            if sp.val != sq.val:
                res = False
                break
            
            
            if sp.left and sq.left:
                p_stack.append(sp.left)
                q_stack.append(sq.left)
            elif not sp.left and not sq.left:
                pass
            else:
                res = False
                break
            
            if sp.right and sq.right:
                p_stack.append(sp.right)
                q_stack.append(sq.right)
            elif not sp.right and not sq.right:
                pass
            else:
                res = False
                break
        
        return res
        
            
