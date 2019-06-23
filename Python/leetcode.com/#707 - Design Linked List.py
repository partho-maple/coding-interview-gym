# https://leetcode.com/problems/design-linked-list/


class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList(object):
    INVALID = -1

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        currentNode = self.head
        currentIndex = 0
        while currentNode is not None and currentIndex != index:
            currentNode = currentNode.next
            currentIndex += 1
        if currentNode is not None:
            return currentNode.val
        else:
            return self.INVALID

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self.tail is None:
            self.addAtHead(val)
            return
        node = Node(val)
        self.insertAfter(self.tail, node)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 and self.head is None:
            self.addAtHead(val)

        if self.head is None and index != 0:
            return -1
        if index == 0:
            self.addAtHead(val)
            return
        elif index == 1:
            self.insertAfter(self.head, Node(val))
            return
        currentNode = self.head.next
        currentIndex = 1
        while currentNode is not None and currentIndex != index:
            currentNode = currentNode.next
            currentIndex += 1
        if currentNode is not None:
            self.insertBefore(currentNode, Node(val))
        if currentNode is None and currentIndex == index:
            self.addAtTail(val)


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        currentNode = self.head
        currentIndex = 0
        while currentNode is not None and currentIndex != index:
            currentNode = currentNode.next
            currentIndex += 1
        if currentNode is not None:
            nodeToDelete = currentNode
        else:
            return None
        if nodeToDelete == -1 or None:
            return None
        if nodeToDelete is self.head:
            self.head = self.head.next
        elif nodeToDelete is self.tail:
            self.tail = self.tail.prev
        else:
            self.removeNodeBinding(nodeToDelete)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def removeNodeBinding(self, nodeToDelete):
        if nodeToDelete.prev is not None:
            nodeToDelete.prev.next = nodeToDelete.next
        if nodeToDelete.next is not None:
            nodeToDelete.next.prev = nodeToDelete.prev
        nodeToDelete.next = None
        nodeToDelete.prev = None






# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1,2)
# obj.get(1)
# obj.deleteAtIndex(1)
# obj.get(1)


# obj.addAtIndex(0, 1)
# obj.addAtIndex(1, 2)
# param_1 = obj.get(1)

# obj.addAtHead(7)
# obj.addAtHead(2)
# obj.addAtHead(1)
# obj.addAtIndex(3, 0)
# obj.deleteAtIndex(2)
# obj.addAtHead(6)
# obj.addAtTail(4)
# param_1 = obj.get(4)

obj.addAtIndex(-1, 0)
param_1 = obj.get(0)

print("value: ", param_1)




