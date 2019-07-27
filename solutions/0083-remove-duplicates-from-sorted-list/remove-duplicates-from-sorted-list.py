# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# Example 1:
#
#
# Input: 1->1->2
# Output: 1->2
#
#
# Example 2:
#
#
# Input: 1->1->2->3->3
# Output: 1->2->3
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
