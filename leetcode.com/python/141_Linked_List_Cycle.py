# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fastPtr, slowPtr = head, head
        while fastPtr is not None and fastPtr.next is not None:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
            if fastPtr == slowPtr:
                return True
        return False