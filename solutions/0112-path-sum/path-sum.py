# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.
#
#  
# Example 1:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,3], targetSum = 5
# Output: false
#
#
# Example 3:
#
#
# Input: root = [1,2], targetSum = 0
# Output: false
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 5000].
# 	-1000 <= Node.val <= 1000
# 	-1000 <= targetSum <= 1000
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        root.sum = root.val
        queue = deque()
        queue.append(root)
        while len(queue):
            node = queue.pop()
            if node.left:
                node.left.sum = node.sum + node.left.val
                queue.append(node.left)
            if node.right:
                node.right.sum = node.sum + node.right.val
                queue.append(node.right)
            
            if not node.left and not node.right and node.sum == targetSum:
                return True
            
        return False
