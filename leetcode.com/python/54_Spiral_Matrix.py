class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        rowCount, colCount = len(matrix), len(matrix[0])
        seen = [[False] * colCount for _ in matrix]
        ans = []
        rowDirection = [0, 1, 0, -1]
        colDirection = [1, 0, -1, 0]
        row, col, directionIdx = 0, 0, 0
        for _ in range(rowCount * colCount):
            ans.append(matrix[row][col])
            seen[row][col] = True
            cRow, cCol = row + rowDirection[directionIdx], col + colDirection[directionIdx]
            if 0 <= cRow < rowCount and 0 <= cCol < colCount and not seen[cRow][cCol]:
                row, col = cRow, cCol
            else:
                directionIdx = (directionIdx + 1) % 4
                row, col = row + rowDirection[directionIdx], col + colDirection[directionIdx]
        return ans



