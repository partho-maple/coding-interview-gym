class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        longestPeakLen = 0
        i = 1
        while i < len(A) - 1:
            isPeak = A[i - 1] < A[i] > A[i + 1]
            if not isPeak:
                i += 1
                continue

            leftIdx = i - 2
            while leftIdx >= 0 and A[leftIdx] < A[leftIdx + 1]:
                leftIdx -= 1

            rightIdx = i + 2
            while rightIdx < len(A) and A[rightIdx - 1] > A[rightIdx]:
                rightIdx += 1

            currentPeakLen = rightIdx - leftIdx - 1
            longestPeakLen = max(longestPeakLen, currentPeakLen)
            i = rightIdx

        return longestPeakLen

