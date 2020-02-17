from collections import deque
# Naive brute force solution
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.queue = deque()
        for v in [v1, v2]:
            if v:
                self.queue.append(deque(v))
        print("__init__ - self.queue: ", self.queue)

    def next(self):
        """
        :rtype: int
        """
        # print("-------")
        # print("self.queue: ", self.queue)
        currentV = self.queue.popleft()
        returnVal = currentV.popleft()
        if currentV:
            self.queue.append(currentV)
        return returnVal

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.queue else False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())






from collections import deque
# without modifing the original input
from collections import deque
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.queue = deque()
        for v in [v1, v2]:   # For the follow up question, simply just all the array here like v1, v2,...vk
            if v:
                self.queue.append((deque(v), 0))

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()
        currentV, posistion = self.queue.popleft()
        if posistion < len(currentV):
            returnVal = currentV[posistion]
            self.queue.append((currentV, posistion + 1))
            return returnVal


    def hasNext(self):
        """
        :rtype: bool
        """
        currentQueue = self.queue
        returnVal = False
        while currentQueue:
            currentV, position = self.queue[0]
            if currentV and position < len(currentV):
                returnVal = True
                break
            else:
                returnVal = False
                self.queue.popleft()
        return returnVal

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())