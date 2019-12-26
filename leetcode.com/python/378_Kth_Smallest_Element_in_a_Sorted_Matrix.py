import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        minHeap = []

        # put the 1st element of each row in the min heap
        # we don't need to push more than 'k' elements in the heap
        for rowIdx in range(min(k, len(matrix))):
            heapq.heappush(minHeap, (matrix[rowIdx][0], 0, rowIdx))

        currentNumber, currentNumerCount = 0, 0
        while minHeap:
            currentNumber, columnIdx, rowIdx = heapq.heappop(minHeap)
            currentNumerCount += 1
            if currentNumerCount == k:
                break
            else:
                if len(matrix[rowIdx]) > columnIdx + 1:
                    heapq.heappush(minHeap, (matrix[rowIdx][columnIdx + 1], columnIdx + 1, rowIdx))
        return currentNumber


