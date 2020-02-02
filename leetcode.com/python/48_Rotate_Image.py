# Official Sol: https://tinyurl.com/rtyo3wq
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])

        # transpose matrix
        for currRow in range(row):
            for currCol in range(currRow, col):
                matrix[currRow][currCol], matrix[currCol][currRow] = matrix[currCol][currRow], matrix[currRow][currCol]

        # reverse each row
        for currRow in range(row):
            matrix[currRow].reverse()
        return matrix





# Source: https://tinyurl.com/tr62top
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])

        firtRow, lastRow = 0, row - 1
        while firtRow < lastRow:
            matrix[firtRow] ,  matrix[lastRow] = matrix[lastRow], matrix[firtRow]
            firtRow += 1
            lastRow -= 1

        # transpose matrix
        for currRow in range(row):
            for currCol in range(currRow, col):
                matrix[currRow][currCol], matrix[currCol][currRow] = matrix[currCol][currRow], matrix[currRow][currCol]

        return matrix
