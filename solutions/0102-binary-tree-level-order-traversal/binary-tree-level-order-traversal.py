# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
#
#  
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [[1]]
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
# 	The number of nodes in the tree is in the range [0, 2000].
# 	-1000 <= Node.val <= 1000
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([])
        queue.append([root, 1])
        ans = []
        while len(queue):
            q, level = queue.popleft()
            if len(ans) < level:
                ans.append([q.val])
            else:
                ans[level -1].append(q.val)
            if q.left:
                queue.append([q.left, level + 1])
            
            if q.right:
                queue.append([q.right, level + 1])
        
        return ans
