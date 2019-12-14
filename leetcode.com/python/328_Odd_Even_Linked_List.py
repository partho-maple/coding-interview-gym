# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddList = ListNode(0)  # This will also serve as oddList tail node
        evenList = ListNode(0)  # This will also serve as evenList tail node
        oddListHead = oddList
        evenListHead = evenList
        isOdd = True
        while head:
            if isOdd:
                oddList.next = head
                oddList = oddList.next
            else:
                evenList.next = head
                evenList = evenList.next
            head = head.next
            isOdd = not isOdd
        evenList.next = None  # to break the cyclic list
        oddList.next = evenListHead.next
        return oddListHead.next

