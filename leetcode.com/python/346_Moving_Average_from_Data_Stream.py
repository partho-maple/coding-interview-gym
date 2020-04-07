from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.nums = deque()

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.nums) >= self.size:
            self.nums.popleft()
        self.nums.append(val)
        return float(float(sum(self.nums)) / float(len(self.nums)))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


