# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
#  
# Example 1:
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
#
# Example 2:
#
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
#
# Example 3:
#
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
#
#  
# Constraints:
#
#
# 	The number of nodes in each linked list is in the range [1, 100].
# 	0 <= Node.val <= 9
# 	It is guaranteed that the list represents a number that does not have leading zeros.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x1 = l1
        x2 = l2
        sum_value = x1.val + x2.val
        overflow, val = int(sum_value / 10), int(sum_value % 10)
        last = ListNode(val)
        cur = last
        x1, x2 = l1.next, l2.next
        
        if x1 == None and x2 == None and overflow == 0:
            return last
    
        while True:
            new_value = overflow
            
            if x1 != None:
                new_value += x1.val
                x1 = x1.next
            if x2 != None:
                new_value += x2.val
                x2 = x2.next
            
            overflow, val = int(new_value / 10), int(new_value % 10)
            cur.next = ListNode(val)
            cur = cur.next
            
            if x1 == None and x2 == None and overflow == 0:
                break
                
        return last

