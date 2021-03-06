'''
P-141 - Linked List Cycle

Given a linked list, determine if it has a cycle in it. Follow up:Can
you solve it without using extra space?

Tags: Linked List, Two Pointers
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean

    # Two pointers based Solution
    # slow and fast will eventually equal if there is a cycle in the list
    def hasCycle(self, head):
        slow = fast = head
        while slow or fast:
            if slow:
                slow = slow.next
            if fast:
                fast = fast.next
            if fast:
                fast = fast.next
            if slow == fast and slow is not None:
                return True
        return False