import heapq

# Using heap
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]





# Quickselect tecnique, using quicksort
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        position = len(nums) - k
        KthLargest = self.quickSelectHelper(nums, 0, len(nums) - 1, position)
        return KthLargest


    def quickSelectHelper(self, nums, startIdx, endIdx, position):
        while True:
            if startIdx > endIdx:
                return float('inf')
            pivotIdx = startIdx
            leftIdx = startIdx + 1
            rightIdx = endIdx
            while leftIdx <= rightIdx:
                if nums[leftIdx] > nums[pivotIdx] and nums[rightIdx] < nums[pivotIdx]:
                    nums[leftIdx], nums[rightIdx] = nums[rightIdx], nums[leftIdx]
                if nums[leftIdx] <= nums[pivotIdx]:
                    leftIdx += 1
                if nums[rightIdx] >= nums[pivotIdx]:
                    rightIdx -= 1
            nums[pivotIdx], nums[rightIdx] = nums[rightIdx], nums[pivotIdx]
            if rightIdx == position:
                return nums[position]
            elif rightIdx > position:
                endIdx = rightIdx - 1
            else:
                startIdx = rightIdx + 1
