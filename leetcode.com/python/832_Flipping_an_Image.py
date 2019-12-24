class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rowCount = len(A)
        columnCount = len(A[0])
        for row in A:
            for columnIdx in range((columnCount + 1) // 2):
                row[columnIdx], row[columnCount - columnIdx - 1] = row[columnCount - columnIdx - 1] ^ 1, row[columnIdx] ^ 1
        return A