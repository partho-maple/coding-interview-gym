# Approach 4: Search Space Reduction
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        height = len(matrix)
        weidth = len(matrix[0])

        row = height - 1
        col = 0

        while row >= 0 and col < weidth:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                return True
        return False