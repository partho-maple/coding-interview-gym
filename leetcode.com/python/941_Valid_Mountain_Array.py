class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        aLen = len(A)
        if aLen < 3:
            return False
        peakCout, valleCount = 0, 0
        for i in range(1, aLen - 1):
            prevNum = A[i - 1]
            currNum = A[i]
            nextNum = A[i + 1]
            if (prevNum < currNum > nextNum):
                peakCout += 1
            if (prevNum >= currNum <= nextNum):
                valleCount += 1
        return peakCout == 1 and valleCount == 0
