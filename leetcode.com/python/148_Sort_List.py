# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Recursive approach using merge sort. Time O(nlogn). Space O(n)  since it's recursive approach. To make it iterative, implement the merge sort iteratively
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        fastNode, slowNode = head.next, head            # divide the list into two parts by fast-slow pointer technique
        while fastNode and fastNode.next:
            fastNode = fastNode.next.next
            slowNode = slowNode.next
        secondHalf = slowNode.next
        slowNode.next = None                            # cut down the first part
        leftHalf = self.sortList(head)
        rightHalf = self.sortList(secondHalf)
        return self.mergeTwoLists(leftHalf, rightHalf)


    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 if l1 else l2
        p1, p2, p1Prev = l1, l2, None
        while p1 and p2:
            if p1.val < p2.val:
                p1Prev = p1
                p1 = p1.next
            else:
                if p1Prev:
                    p1Prev.next = p2
                p1Prev = p2
                p2 = p2.next
                p1Prev.next = p1
        if not p1:
            p1Prev.next = p2
        return l1 if l1.val < l2.val else l2

