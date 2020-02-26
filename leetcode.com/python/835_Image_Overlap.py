from collections import defaultdict
class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        translationDistanceCount = defaultdict(int)
        a1Coordinates, b1Coordinates = [], []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    a1Coordinates.append((i, j))
                if B[i][j] == 1:
                    b1Coordinates.append((i, j))

        for aRow, aCol in a1Coordinates:
            for bRow, bCol in b1Coordinates:
                translation = (bRow - aRow, bCol - aCol)
                translationDistanceCount[translation] += 1
        return max(translationDistanceCount.values()) if translationDistanceCount else 0