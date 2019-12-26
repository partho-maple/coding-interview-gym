import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        maxHeap = []
        for nums1Idx in range(min(k, len(nums1))):
            for nums2Idx in range(min(k, len(nums2))):
                currentPairSum = nums1[nums1Idx] + nums2[nums2Idx]
                if len(maxHeap) < k:
                    heapq.heappush(maxHeap, (-currentPairSum, nums1Idx, nums2Idx))
                else:
                    if currentPairSum < (-maxHeap[0][0]):
                        heapq.heappop(maxHeap)
                        heapq.heappush(maxHeap, (-currentPairSum, nums1Idx, nums2Idx))
                    else:
                        break
        smallestPairs = []
        for (currentPairSum, nums1Idx, nums2Idx) in maxHeap:
            smallestPairs.append([nums1[nums1Idx], nums2[nums2Idx]])
        return smallestPairs

