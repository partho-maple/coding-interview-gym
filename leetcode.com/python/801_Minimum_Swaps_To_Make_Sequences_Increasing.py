
# Source:   https://tinyurl.com/tzx7wpv
class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        arrLen = len(A)
        swaps, noSwaps = [arrLen] * arrLen, [arrLen] * arrLen
        swaps[0], noSwaps[0] = 1, 0
        for i in range(1, arrLen):
            currentNumA, prevNumA = A[i], A[i - 1]
            currentNumB, prevNumB = B[i], B[i - 1]
            if currentNumA > prevNumA and currentNumB > prevNumB:
                noSwaps[i] = noSwaps[i - 1]
                swaps[i] = swaps[i - 1] + 1
            if currentNumB > prevNumA and currentNumA > prevNumB:
                noSwaps[i] = min(noSwaps[i], swaps[i - 1]) # If we do ot make the swap in this case
                swaps[i] = min(swaps[i], noSwaps[i - 1] + 1) # If we make the swap in this case
        return min(swaps[-1], noSwaps[-1])
