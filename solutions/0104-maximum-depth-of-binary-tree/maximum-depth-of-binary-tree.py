# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
#  
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#
#
# Example 2:
#
#
# Input: root = [1,null,2]
# Output: 2
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 104].
# 	-100 <= Node.val <= 100
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # DFS search
        if not root:
            return 0
    
        stack = [root]
        depth_map = {
            root: 1
        }
        while len(stack) > 0:
            last, stack = stack[len(stack) -1], stack[:len(stack) -1]
            # print(last.val)
            if not last:
                continue
            
            if last.left:
                stack.append(last.left)
                depth_map[last.left] = depth_map[last] + 1
            
            if last.right:
                stack.append(last.right)
                depth_map[last.right] = depth_map[last] + 1
        
        return max(depth_map.values())
        
