

# Time O(n) | Space O(n) >> where n is the total number of elements in 2D array
def zigzagTraverse(array):
    height = len(array) - 1
    width = len(array[0]) - 1
    result = []
    row, col = 0, 0
    goingDown = True
    while not isOutOfBound(height, width, row, col):
        result.append(array[row][col])
        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if col == width or row == 0:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1

    return result


def isOutOfBound(height, width, row, col):
    return row < 0 or row > height or col < 0 or col > width
