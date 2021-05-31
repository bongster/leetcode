# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
#
#  
# Example 1:
#
#
# Input: head = [1,1,2]
# Output: [1,2]
#
#
# Example 2:
#
#
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the list is in the range [0, 300].
# 	-100 <= Node.val <= 100
# 	The list is guaranteed to be sorted in ascending order.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            if not cur.next:
                break
            next_node = cur.next
            while next_node:
                if cur.val == next_node.val:
                    cur.next = next_node.next
                    next_node = next_node.next
                else:
                    break
            
            cur = cur.next
        return head
