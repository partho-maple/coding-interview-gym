
#   Solution 1
#   O(nm) time | O(nm) - where 'n' represents row and 'm' represents column
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        squares = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
        largestDim = 0
        for rowIdx in range(len(matrix)):
            for columnIdx in range(len(matrix[rowIdx])):
                if matrix[rowIdx][columnIdx] == '0':
                    squares[rowIdx + 1][columnIdx + 1] = 0
                else:
                    squares[rowIdx + 1][columnIdx + 1] = min(squares[rowIdx][columnIdx + 1], squares[rowIdx][columnIdx],
                                                             squares[rowIdx + 1][columnIdx]) + 1
                    largestDim = max(largestDim, squares[rowIdx + 1][columnIdx + 1])
        return largestDim * largestDim




#   Solution 2
#   O(nm) time | O(m) - where 'n' represents row and 'm' represents column
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        oddRow = [0 for i in range(len(matrix[0]) + 1)]
        evenRow = [0 for i in range(len(matrix[0]) + 1)]
        largestDim = 0
        for rowIdx in range(len(matrix)):
            if rowIdx % 2 == 1:
                currentRow = oddRow
                previousRow = evenRow
            else:
                currentRow = evenRow
                previousRow = oddRow

            for columnIdx in range(len(matrix[rowIdx])):
                if matrix[rowIdx][columnIdx] == '0':
                    currentRow[columnIdx + 1] = 0
                else:
                    currentRow[columnIdx + 1] = min(previousRow[columnIdx + 1], previousRow[columnIdx], currentRow[columnIdx]) + 1
                    largestDim = max(largestDim, currentRow[columnIdx + 1])
        return largestDim * largestDim



sol = Solution()
input = [["1","0","1","0"],
         ["1","0","1","1"],
         ["1","0","1","1"],
         ["1","1","1","1"]]
output = sol.maximalSquare(input)
print('Result: ', output)