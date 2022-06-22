# You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.
#
# Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
#
#
# 	'L' means to go from a node to its left child node.
# 	'R' means to go from a node to its right child node.
# 	'U' means to go from a node to its parent node.
#
#
# Return the step-by-step directions of the shortest path from node s to node t.
#
#  
# Example 1:
#
#
# Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
# Output: "UURL"
# Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
#
#
# Example 2:
#
#
# Input: root = [2,1], startValue = 2, destValue = 1
# Output: "L"
# Explanation: The shortest path is: 2 → 1.
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is n.
# 	2 <= n <= 105
# 	1 <= Node.val <= n
# 	All the values in the tree are unique.
# 	1 <= startValue, destValue <= n
# 	startValue != destValue
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # find a common parent node between startNode, and destNode
        # calclulate left and right and merge
        def lca(node): 
            """Return lowest common ancestor of start and dest nodes."""
            if not node or node.val in (startValue , destValue): return node 
            left, right = lca(node.left), lca(node.right)
            return node if left and right else left or right
        
        root = lca(root) # only this sub-tree matters
        
        def fn(val): 
            """Return path from root to node with val."""
            stack = [(root, "")]
            while stack: 
                node, path = stack.pop()
                if node.val == val: return path 
                if node.left: stack.append((node.left, path + "L"))
                if node.right: stack.append((node.right, path + "R"))
        
        path0 = fn(startValue)
        path1 = fn(destValue)
        return "U"*len(path0) + path1
