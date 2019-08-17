# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#
# return its bottom-up level order traversal as:
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = []
        
        root.depth = 0
        queue.append(root)
        while len(queue):
            cur, queue = queue[0], queue[1:]
            
            
            if len(res) <= cur.depth:
                res.append([])
            
            res[cur.depth].append(cur.val)
            
            if cur.left:
                cur.left.depth = cur.depth + 1;
                queue.append(cur.left)
            if cur.right:
                cur.right.depth = cur.depth + 1;
                queue.append(cur.right)
        
        res.reverse()
        return res
