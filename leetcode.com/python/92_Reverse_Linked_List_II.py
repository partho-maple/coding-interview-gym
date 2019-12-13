"""""
The problem follows the In-place Reversal of a LinkedList pattern. We can use a similar approach as discussed in Reverse a LinkedList. Here are the steps we need to follow:

1.  Skip the first p-1 nodes, to reach the node at position p.
2.  Remember the node at position p-1 to be used later to connect with the reversed sub-list.
3.  Next, reverse the nodes from p to q using the same approach discussed in Reverse a LinkedList.
4.  Connect the p-1 and q+1 nodes to the reversed sub-list.
"""""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        # after skipping 'm-1' nodes, currentNode will point to 'm'th node
        currentListLength = 0
        previousNode, currentNode = None, head
        while currentNode and currentListLength < m:
            currentListLength += 1
            previousNode = currentNode
            currentNode = currentNode.next
        lastNodeOfFirstPart = previousNode                          # we are interested in three parts of the LinkedList, the part before index 'p', the part between 'p' and 'q', and the part after index 'q'
        lastNodeOfReversedSublist = currentNode                     # after reversing the LinkedList 'current' will become the last-node/tail-node of the sub-list
        currentListLength = 0
        while currentNode and currentListLength < n - m + 1:        # reverse nodes between 'p' and 'q'
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
            currentListLength += 1
        if lastNodeOfFirstPart:                                     # connect with the first part
            lastNodeOfFirstPart.next = previousNode                 # 'previous' is now the first-node/head-node of the sub-list
        else:
            head = previousNode                                     # this means p == 1 i.e., we are changing the first node (head) of the LinkedList
        lastNodeOfReversedSublist.next = currentNode                # connect with the last part
        return head




