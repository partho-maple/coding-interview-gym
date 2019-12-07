class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(A) - 1
        result = []
        while left <= right:
            leftSqr = A[left] * A[left]
            rightSqr = A[right] * A[right]
            if leftSqr >= rightSqr:
                result.insert(0, leftSqr)
                left += 1
            else:
                result.insert(0, rightSqr)
                right -= 1
        return result