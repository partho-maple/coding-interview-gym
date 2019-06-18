# https://www.algoexpert.io/questions/Search%20In%20Sorted%20Matrix


# O(n + m)  time | O(1) space
# where 'n' is the length of row and 'm' is the length on column
def search_in_sorted_matrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < row:
            row += 1
        else:
            return [row, col]
    return [-1, -1]

