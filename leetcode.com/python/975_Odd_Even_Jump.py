# Approach 1: Brute force solution
class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        aLen = len(A)
        if aLen < 1:
            return 0
        result = 0
        for i, a in enumerate(A):
            if i == aLen - 1:
                result += 1
                break
            value = A[i]
            j = i
            while j < aLen:

