# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        middleNode = self.middleNode(head)  # find middle of the LinkedList
        headSecondHalf = self.reverseLinkedList(middleNode)  # reverse the second half
        headFirstHalf = head
        while headFirstHalf and headSecondHalf:  # rearrange to produce the LinkedList in the required order
            temp = headFirstHalf.next
            headFirstHalf.next = headSecondHalf
            headFirstHalf = temp
            temp = headSecondHalf.next
            headSecondHalf.next = headFirstHalf
            headSecondHalf = temp
        if headFirstHalf:  # set the next of the last node to 'None'
            headFirstHalf.next = None

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

    def reverseLinkedList(self, head):
        prevNode = None
        while head:
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode
        return prevNode