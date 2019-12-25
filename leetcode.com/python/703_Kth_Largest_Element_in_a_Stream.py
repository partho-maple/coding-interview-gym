import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.minHeap = []
        self.k = k
        if not nums:
            return
        for i in range(k):
            if self.minHeap and len(self.minHeap) >= k:
                heapq.heappop(self.minHeap)
            if len(nums) > i:
                heapq.heappush(self.minHeap, nums[i])
            else:
                return

        for i in range(k, len(nums)):
            if nums[i] > self.minHeap[0]:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, nums[i])


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if not self.minHeap:
            heapq.heappush(self.minHeap, val)
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, val)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)