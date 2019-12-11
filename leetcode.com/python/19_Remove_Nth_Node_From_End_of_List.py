# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyNode = ListNode(0)
        dummyNode.next = head
        fastNode, slowNode = dummyNode, dummyNode
        for _ in range(n):
            fastNode = fastNode.next
        while fastNode and fastNode.next:
            fastNode = fastNode.next
            slowNode = slowNode.next
        slowNode.next = slowNode.next.next
        return dummyNode.next

