# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        fastRuner, slowRuner = head, head
        while fastRuner and fastRuner.next:
            fastRuner = fastRuner.next.next
            slowRuner = slowRuner.next
        return slowRuner
