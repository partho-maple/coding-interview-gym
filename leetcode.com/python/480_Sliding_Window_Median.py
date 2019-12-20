from heapq import *
import heapq


# Solution from https://leetcode.com/problems/find-median-from-data-stream/
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []  # containing first half of numbers
        self.maxHeap = []  # containing second half of numbers

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

    def removeNum(self, num):
        if num <= -self.maxHeap[0]:
            self.removeNumFromHeap(self.maxHeap, -num)
        else:
            self.removeNumFromHeap(self.minHeap, num)
        self.reBalanceHeapes()

    # removes an element from the heap keeping the heap property
    def removeNumFromHeap(self, heap, element):
        idx = heap.index(element)  # find the element
        heap[idx] = heap[-1]  # replace the last to the element to be deleted
        del heap[-1]  # delete the last element

        # we can use heapify to readjust the elements but that would be O(N),
        # instead, we will adjust only one element which will O(logN)
        if idx < len(heap):
            heapq._siftup(heap, idx)
            heapq._siftdown(heap, 0, idx)

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


# Code for this problem
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        medianFinder = MedianFinder()
        mediansArray = [0.0 for x in range(len(nums) - k + 1)]
        for idx, num in enumerate(nums):
            medianFinder.addNum(num)
            if idx - k + 1 >= 0:
                currentWindowMedian = medianFinder.findMedian()
                mediansArray[idx - k + 1] = currentWindowMedian
                elementToBeRemoved = nums[idx - k + 1]
                medianFinder.removeNum(elementToBeRemoved)
        return mediansArray






sol = Solution()
nums = [1,2,3,4,2,3,1,4,2]
k = 3
out = sol.medianSlidingWindow(nums, k)
print("Res: ", out)