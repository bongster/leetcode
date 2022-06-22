# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.
#
#
# 	For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
#
#
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.
#
# The test cases are generated so that the answer fits in a 32-bits integer.
#
#  
# Example 1:
#
#
# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
#
#
# Example 2:
#
#
# Input: root = [0]
# Output: 0
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [1, 1000].
# 	Node.val is 0 or 1.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        queue = []
        parent_map = {}
        queue.append(root)
        res = 0
        while len(queue) > 0:
            last, queue = queue[len(queue) -1], queue[:len(queue) -1]
            # print(last.val)
            if last.left:
                parent_map[last.left] = last
                queue.append(last.left)
    
            if last.right:
                parent_map[last.right] = last
                queue.append(last.right)
            
            if last.left == None and last.right == None:
                val_arr = [last.val]
                val = 0
                parent = parent_map.get(last)
                while parent:
                    val_arr.append(parent.val)
                    parent = parent_map.get(parent)
                
                print(val_arr)
                for i, v in enumerate(val_arr):
                    print(i, v, v * (2**i))
                    val += v * (2**i)
                    
                res += val
        return res
                    
            
