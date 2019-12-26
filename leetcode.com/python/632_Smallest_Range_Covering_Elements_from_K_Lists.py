import heapq
import math


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        minHeap = []
        rangeStart, rageEnd = 0, float("inf")
        currentMaxNumber = float("-inf")

        # put the 1st element of each array in the max heap
        for rowIdx in range(len(nums)):
            heapq.heappush(minHeap, (nums[rowIdx][0], 0, rowIdx))
            currentMaxNumber = max(currentMaxNumber, nums[rowIdx][0])

        # take the smallest(top) element form the min heap, if it gives us smaller range, update the ranges
        # if the array of the top element has more elements, insert the next element in the heap
        while len(minHeap) == len(nums):
            num, columnIdx, rowIdx = heapq.heappop(minHeap)
            if (rageEnd - rangeStart) > (currentMaxNumber - num):
                rangeStart = num
                rageEnd = currentMaxNumber

            if len(nums[rowIdx]) > columnIdx + 1:
                heapq.heappush(minHeap, (nums[rowIdx][columnIdx + 1], columnIdx + 1, rowIdx))
                currentMaxNumber = max(currentMaxNumber, nums[rowIdx][columnIdx + 1])

        return [rangeStart, rageEnd]
