# O(mn) approach
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        neighbours = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        rows = len(board)
        cols = len(board[0])
        boardClone = [[board[row][col] for col in range(cols)] for row in range(rows)]
        for row in range(rows):
            for col in range(cols):
                livingNeighbours = 0
                for neighbour in neighbours:
                    r = row + neighbour[0]
                    c = col + neighbour[1]
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (boardClone[r][c] == 1):
                        livingNeighbours += 1
                if boardClone[row][col] == 1 and (livingNeighbours < 2 or livingNeighbours > 3):
                    board[row][col] = 0
                if boardClone[row][col] == 0 and (livingNeighbours == 3):
                    board[row][col] = 1


# O(1) approach
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        neighbours = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                livingNeighbours = 0
                for neighbour in neighbours:
                    r = row + neighbour[0]
                    c = col + neighbour[1]
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (abs(board[r][c]) == 1):
                        livingNeighbours += 1
                if board[row][col] == 1 and (livingNeighbours < 2 or livingNeighbours > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and (livingNeighbours == 3):
                    board[row][col] = 2
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0



