# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class MyLinkedList(object):
    INVALID = -1

    def __init__(self):
        self.first = None
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        node = self.getNode(index)
        return node.val if node else self.INVALID

    def getNode(self, index):
        """
        :type index: int
        :rtype: Node | None
        """
        if index >= self.size or index < 0:
            return None
        node = self.first
        while index > 0:
            node = node.next
            index -= 1
        return node

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size or index < 0:
            return
        prev = self.getNode(index - 1)
        if prev:
            prev.next = ListNode(val, prev.next)
        else:
            self.first = ListNode(val, self.first)
        self.size += 1


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyNode = ListNode(-1)
        head = dummyNode
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                dummyNode.next = l1
                l1 = l1.next
            else:
                dummyNode.next = l2
                l2 = l2.next
            dummyNode = dummyNode.next
        if l1 is not None:
            dummyNode.next = l1
        if l2 is not None:
            dummyNode.next = l2

        return head.next


obj1 = MyLinkedList()
obj1.addAtHead(4)
obj1.addAtHead(2)
obj1.addAtHead(1)

obj2 = MyLinkedList()
obj2.addAtHead(4)
obj2.addAtHead(3)
obj2.addAtHead(1)


sol = Solution()
merge = sol.mergeTwoLists(obj1.getNode(0), obj2.getNode(0))
print("List: ", merge)



