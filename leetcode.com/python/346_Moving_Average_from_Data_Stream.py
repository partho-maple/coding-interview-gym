from collections import deque


class MovingAverage(object):

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = deque()
        self.widowSum = 0

    def next(self, val: int) -> float:
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        tail = self.queue.popleft() if len(self.queue) > self.size else 0
        self.widowSum = self.widowSum - tail + val
        res = self.widowSum / min(len(self.queue), self.size)
        return res

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


