class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) time | O(1) space
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)  # corner case -- setting new head

    # O(1) time | O(1) space
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    # O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        # edge case
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)  # if the node exists in the linked list we will remove it. This step can be skipped
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)  # if the node exists in the linked list we will remove it. This step can be skipped
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next == None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # O(Position) time | O(1) space
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # O(n) time | O(1) space
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            # we need this temp variable because we are losing node.next in removeNodeBindinnodegs()
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    # O(1) time | O(1) space
    def remove(self, node):
        if (node == self.head):
            self.head = self.head.next
        if (node == self.tail):
            self.tail = self.tail.prev
        # checks if we are removing head or tail and updating new head or tail
        self.removeNodeBindings(node)

    # O(n) time | O(1) space
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None


class node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value