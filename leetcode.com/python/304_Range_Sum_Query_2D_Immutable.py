# Mock solution
class NumMaipnntrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        self.matrix = matrix
        rowCount, colCount = len(self.matrix), len(self.matrix[0])
        self.prefixSum = [0]
        for row in range(rowCount):
            for col in range(colCount):
                currentNum = self.matrix[row][col]
                idx = (colCount * row) + col
                if idx == 0:
                    self.prefixSum.append(currentNum)
                else:
                    self.prefixSum.append(self.prefixSum[-1] + currentNum)
        print(self.prefixSum)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        rowCount, colCount = len(self.matrix), len(self.matrix[0])
        rangeSum = 0
        for row in range(row1, row2 + 1):
            startIdx = (colCount * row) + col1
            endIdx = (colCount * row) + col2 + 1
            rowSum = self.prefixSum[endIdx] - self.prefixSum[startIdx]
            rangeSum += rowSum
        return rangeSum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)