from heapq import *


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []   # containing first half of numbers
        self.maxHeap = []   # containing second half of numbers

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
        self.reBalanceHeapes()


    def reBalanceHeapes(self):
        # either both the heaps will have equal number of elements or max-heap will have one
        # more element than the min-heap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))



    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] / 2.0) + (self.minHeap[0] / 2.0)
        return -self.maxHeap[0] / 1.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()