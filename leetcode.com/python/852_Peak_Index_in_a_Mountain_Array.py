class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        leftIdx, rightIdx = 0, len(A) - 1
        while leftIdx < rightIdx:
            midIdx = leftIdx + (rightIdx - leftIdx) // 2
            if A[midIdx] < A[midIdx + 1]:
                leftIdx = midIdx + 1
            else:
                rightIdx = midIdx
        return leftIdx
