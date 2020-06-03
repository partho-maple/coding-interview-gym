from collections import defaultdict
import heapq

class FreqStack(object):

    def __init__(self):
        self.counter = defaultdict(int)
        self.stackIdx = -1  # initially the stack is empty
        self.maxHeap = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.counter[x] += 1
        self.stackIdx += 1
        heapq.heappush(self.maxHeap, (-self.counter[x], -self.stackIdx, x))

    def pop(self):
        """
        :rtype: int
        """
        topElement = heapq.heappop(self.maxHeap)
        count, idx, x = -topElement[0], -topElement[1], topElement[2]
        self.counter[x] -= 1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()