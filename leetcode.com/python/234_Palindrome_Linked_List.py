# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        middleNode = self.middleNode(head)          # find middle of the LinkedList
        reversedListSecondHalf = self.reverseLinkedList(middleNode) # reverse the second half
        copyOfReversedListSecondHalf = reversedListSecondHalf # store the head of reversed part to revert back later
        while head and reversedListSecondHalf:              # compare the first and the second half
            if head.val != reversedListSecondHalf.val:
                break       # not a palindrome
            head = head.next
            reversedListSecondHalf = reversedListSecondHalf.next
        self.reverseLinkedList(copyOfReversedListSecondHalf) # revert the reverse of the second half
        if not head or not reversedListSecondHalf:
            return True
        return False



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


