# Approach 1: Brute force. Time limit exceeded. 83 / 93 test cases passed.
# Time:  O(n^2)
class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        prefixSumA = [0] * (len(A) + 1)
        for i in range(len(A)):
            prefixSumA[i + 1] = prefixSumA[i] + A[i]

        minSubArrLen = float("inf")
        for i in range(len(prefixSumA)):
            for j in range(i + 1, len(prefixSumA)):
                currentRangeSum = prefixSumA[j] - prefixSumA[i]
                if currentRangeSum >= K:
                    minSubArrLen = min(minSubArrLen, j - i)

        return minSubArrLen if minSubArrLen != float("inf") else -1





# Approach 2: usig monotonic queue and sliding window
# Time: O(n)
from collections import deque
class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        aLen = len(A)
        prefixSumA = [0] * (aLen + 1)
        for i in range(aLen):
            prefixSumA[i + 1] = prefixSumA[i] + A[i]

        minSubArrLen = float("inf")
        monotonicQueue = deque() # keeps the indexes of the startIdx of the sliding window
        for idx, currentSum in enumerate(prefixSumA):
            while monotonicQueue and currentSum <= prefixSumA[monotonicQueue[-1]]:
                monotonicQueue.pop()

            while monotonicQueue and currentSum - prefixSumA[monotonicQueue[0]] >= K:
                minSubArrLen = min(minSubArrLen, (idx - monotonicQueue.popleft()))

            monotonicQueue.append(idx)


        return minSubArrLen if minSubArrLen != float("inf") else -1