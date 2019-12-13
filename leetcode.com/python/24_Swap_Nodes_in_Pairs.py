# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Recursive solution.
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



# Iterative solution.
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverseKGroup(head, 2)

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        lastNodeOfFirstReversedPart = None
        dummyNode = ListNode(0)
        dummyNode.next = lastNodeOfFirstReversedPart
        linkedListLength = self.getLength(head)
        while True:
            newHeadOfUnreversedPart, headOfReversedPart = None, None
            if self.canReverse(linkedListLength, k):
                newHeadOfUnreversedPart, headOfReversedPart = self.reverseList(head, k)
                linkedListLength -= k
                if lastNodeOfFirstReversedPart:
                    lastNodeOfFirstReversedPart.next = headOfReversedPart
                else:
                    dummyNode.next = headOfReversedPart
                lastNodeOfFirstReversedPart = head
                head = newHeadOfUnreversedPart
            else:
                if lastNodeOfFirstReversedPart:
                    lastNodeOfFirstReversedPart.next = head
                else:
                    dummyNode.next = head
                break
        return dummyNode.next


    def canReverse(self, length, k):
        return True if length // k >= 1 else False


    def getLength(self, head):
        count, currentNode = 0, head
        while currentNode:
            currentNode = currentNode.next
            count += 1
        return count


    def reverseList(self, head, k):
        previousNode, currentNode, nextNode = None, head, head
        while k > 0 and currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
            k -= 1
        return (currentNode, previousNode)   # prev is the head node of the reversed list, the end node of the original list. curr is the head node of the remaining list, since it is the node following prev in the original list

