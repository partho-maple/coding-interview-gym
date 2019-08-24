# # Approach 3: Divide and Conquer
# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if not matrix:
#             return False
#         return self.searchRect(0, 0, len(matrix[0]) - 1, len(matrix) - 1, matrix, target)

#     # Here 3 parameters  are the 4 borders (left and right columns. And up and down/bottom rows).
#     # Which  defines the  area of the matrix
#     def searchRect(self, left, up, right,  down, matrix, target):
#         if left > right or up > down:   # this submatrix has no height or no width.
#             return False
#         elif target > matrix[down][right] or target < matrix[up][left]: # `target` is already larger than the largest element or smaller. than the smallest element in this submatrix.
#             return False
#         mid = left + (right - left) // 2 # mid column of  the new selected  matrix
#         row = up
#         while row <= down and matrix[row][mid] <= target:
#             if matrix[row][mid] == target:
#                 return True
#             row += 1
#         return self.searchRect(left, row, mid - 1, down, matrix, target) or self.searchRect(mid + 1, up, right, row - 1, matrix, target)


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












