class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [[0 for x in range(y + 1)] for y in range(rowIndex + 1)]
        memo = {}
        for row in range(rowIndex + 1):
            for column in range(row + 1):
                num = self.generageNumber(row, column, memo)
                result[row][column] = num
                memo[str(row) + "-" + str(column)] = num
        return result[rowIndex]

    def generageNumber(self, row, column, memo):
        if column == 0 or row == column:
            memo[str(row) + "-" + str(column)] = 1
            return 1
        key = str(row) + "-" + str(column)
        if key in memo.keys():
            return memo[str(row) + "-" + str(column)]
        else:
            return self.generageNumber(row - 1, column - 1, memo) + self.generageNumber(row - 1, column, memo)

