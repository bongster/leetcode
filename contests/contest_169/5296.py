'''
5296. All Elements in Two Binary Search Trees

Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

https://leetcode.com/contest/weekly-contest-169/problems/all-elements-in-two-binary-search-trees/

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []

        queue = [root1]

        while len(queue):
            node, queue = queue[0], queue[1:]
            if not node:
                pass
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                res.append(node.val)

        queue = [root2]                       
        while len(queue):
            node, queue = queue[0], queue[1:]
            if not node:
                pass
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                res.append(node.val)

        return sorted(res)

