# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lengthA = self.getLength(headA)
        lengthB = self.getLength(headB)
        diff = abs(lengthA - lengthB)
        fast, slow = None, None
        if lengthA > lengthB:
            fast, slow = headA, headB
        else:
            fast, slow = headB, headA
        while diff > 0:
            fast = fast.next
            diff -= 1
        while fast and slow:
            if fast is slow:
                return slow
            else:
                fast = fast.next
                slow = slow.next
        return None

    def getLength(self, head):
        count, currentNode = 0, head
        while currentNode:
            currentNode = currentNode.next
            count += 1
        return count

