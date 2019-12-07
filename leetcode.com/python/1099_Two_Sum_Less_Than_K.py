class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        i, j = 0, len(A) - 1
        S = -1
        while i < j:
            currentSum = A[i] + A[j]
            if currentSum < K:
                S = max(S, currentSum)
                i += 1
            else:
                j -= 1
        return S
