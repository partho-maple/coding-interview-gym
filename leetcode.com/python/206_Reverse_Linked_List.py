# Explanations:
# https://www.youtube.com/watch?v=sYcOK51hl-A
# https://www.youtube.com/watch?v=O0By4Zq0OFc


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head




