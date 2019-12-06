from collections import Counter

class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rowCount, columnCount = len(matrix), len(matrix[0])
        submatricesCount = 0

        # For this double-for loop, we are calculating the prefix sum for each row in the matrix, which will be used later
        for row in range(rowCount):
            for column in range(1, columnCount):
                matrix[row][column] += matrix[row][column - 1]

        for columnStart in range(columnCount):
            for columnEnd in range(columnStart, columnCount):
                prefixSumCounter = Counter()
                prefixSumCounter[0] = 1
                currentSumOfSubmatrix = 0

                for row in range(rowCount):
                    submatrixEnd = matrix[row][columnEnd]
                    if columnStart:
                        submatrixStart = matrix[row][columnStart - 1]
                    else:
                        submatrixStart = 0

                    currentSumOfSubmatrix += submatrixEnd - submatrixStart              #  increment current sum
                    prefixSumOfSubmatrix = currentSumOfSubmatrix - target
                    if prefixSumOfSubmatrix in prefixSumCounter:       # check if there is a prefix subarray we can take out to reach target
                        submatricesCount += prefixSumCounter[prefixSumOfSubmatrix]
                    prefixSumCounter[currentSumOfSubmatrix] += 1       # add current sum to sum count

        return submatricesCount


sol = Solution()
matrix = [[0,1,0],[1,1,1],[0,1,0]]
target = 0
out = sol.numSubmatrixSumTarget(matrix,target)
print("Res: ", out)



