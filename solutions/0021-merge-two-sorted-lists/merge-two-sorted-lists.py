# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#  
# Example 1:
#
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
#
# Example 2:
#
#
# Input: list1 = [], list2 = []
# Output: []
#
#
# Example 3:
#
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
#
#  
# Constraints:
#
#
# 	The number of nodes in both lists is in the range [0, 50].
# 	-100 <= Node.val <= 100
# 	Both list1 and list2 are sorted in non-decreasing order.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        
        x1 = l1
        x2 = l2
        if x1.val > x2.val:
            res = x2
            x2 = x2.next
        else:
            res = x1
            x1 = x1.next
        
        cur = res
        while x1 or x2:
            if x1 and x2:
                if x1.val > x2.val:
                    cur.next = x2
                    x2 = x2.next
                else:
                    cur.next = x1
                    x1 = x1.next
            elif x1 and not x2:
                cur.next = x1
                break
            else:
                cur.next = x2
                break
            
            cur = cur.next
        
        return res
