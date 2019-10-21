# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        if head.next is None:
            return head
        head.val, head.next.val = head.next.val, head.val
        if head.next.next:
            self.swapPairs(head.next.next)
        return head
