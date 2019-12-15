"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

# Approach 3: Iterative with O(1)O(1) Space .    Source: https://tinyurl.com/tnwofvs
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        weavedListPtr = head
        while weavedListPtr:
            newNode = Node(weavedListPtr.val, None, None)
            newNode.next = weavedListPtr.next
            weavedListPtr.next = newNode
            weavedListPtr = newNode.next
        weavedListPtr = head
        while weavedListPtr:
            weavedListPtr.next.random = weavedListPtr.random.next if weavedListPtr.random else None
            weavedListPtr = weavedListPtr.next.next
        ptrOldList = head
        ptrNewList = head.next
        headNew = ptrNewList
        while ptrOldList:
            ptrOldList.next = ptrOldList.next.next
            ptrNewList.next = ptrNewList.next.next if ptrNewList.next else None
            ptrOldList = ptrOldList.next
            ptrNewList = ptrNewList.next
        return headNew


