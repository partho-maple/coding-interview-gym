# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Inplace iterative solution. SOurce: https://tinyurl.com/s7pns43q
class Solution(object):
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



"""""
# Recursive solution. SOurce: https://tinyurl.com/rfumpm9
class Solution(object):
    def reverseKGroup(self, head, k):
        # :type head: ListNode
        # :type k: int
        # :rtype: ListNode
        if not head:
            return head
        count, currentNode = 0, head
        while currentNode and count < k:
            currentNode = currentNode.next
            count += 1
        if count < k:  # list shorter than k
            return head
        newHead, reversedHead = self.reverseList(head, count)
        head.next = self.reverseKGroup(newHead, k)
        return reversedHead

    def reverseList(self, head, count):
        # :type head: ListNode
        # :rtype: ListNode
        previousNode, currentNode, nextNode = None, head, head
        while count > 0 and currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
            count -= 1
        return (currentNode,  previousNode)  # prev is the head node of the reversed list, the end node of the original list. curr is the head node of the remaining list, since it is the node following prev in the original list
"""""




head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)

sol = Solution()
out = sol.reverseKGroup(head, 3)
print("Res: ", out)
