# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k <= 0:
            return head
        listLength, lastNode = self.getLengthWithLastNode(head)
        nodeCountToRotate = k % listLength
        nodeToSkipFromBeginning = listLength - nodeCountToRotate
        lastNode.next = head  # connect the last node with the head to make it a circular list
        newTail, newHead = self.traverseNodesFromHead(head, nodeToSkipFromBeginning)
        newTail.next = None
        return newHead

    def getLengthWithLastNode(self, head):
        count, currentNode, previousNode = 0, head, None
        while currentNode:
            previousNode = currentNode
            currentNode = currentNode.next
            count += 1
        return (count, previousNode)

    def traverseNodesFromHead(self, head, count):
        previousNode, currentNode = None, head
        for i in range(count):
            previousNode = currentNode
            currentNode = currentNode.next
        return (previousNode, currentNode)


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
sol = Solution()
out = sol.rotateRight(head, 2)
print("Res: ", out)