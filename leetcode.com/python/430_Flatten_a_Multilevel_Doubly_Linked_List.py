# """
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
# """



# Recursive
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        dummyHead = Node(None, None, head, None)
        self.flattenDFS(dummyHead, head)
        dummyHead.next.prev = None
        return dummyHead.next


    def flattenDFS(self, previous, current):
        """
        :type head: Node
        :rtype: Node
        """
        if not current:
            return previous
        current.prev = previous
        previous.next = current
        tempNext = current.next
        currentTail = self.flattenDFS(current, current.child)
        current.child = None
        return self.flattenDFS(currentTail,  tempNext)




# Iterative
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return
        dummyHead = Node(None, None, head, None)
        previous = dummyHead
        stack = [head, ]
        while stack:
            current = stack.pop()
            current.prev = previous
            previous.next = current
            if current.next:
                stack.append(current.next)
            if current.child:
                stack.append(current.child)
                current.child = None
            previous = current
        dummyHead.next.prev = None
        return dummyHead.next



