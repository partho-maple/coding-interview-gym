class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        memo = {}
        possibleMoves = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2),
                         (-2, -1))  # a list of new (row, col) tuple, clock wise, starting from top right
        return self.knightProbabilityDFSHelper(N, K, memo, possibleMoves, r, c, 0, 1.0)

    def knightProbabilityDFSHelper(self, N, K, memo, possibleMoves, row, col, currentMoveCount, currentPossibility):
        possibility = 0
        if 0 <= row < N and 0 <= col < N:  # a valid position on the board
            if currentMoveCount < K:
                for dRow, dCol in possibleMoves:
                    nextRow, nextCol = row + dRow, col + dCol
                    if (nextRow, nextCol, currentMoveCount + 1) not in memo:
                        memo[(nextRow, nextCol, currentMoveCount + 1)] = self.knightProbabilityDFSHelper(N, K, memo,
                                                                                                         possibleMoves,
                                                                                                         nextRow,
                                                                                                         nextCol,
                                                                                                         currentMoveCount + 1,
                                                                                                         currentPossibility / 8)
                        possibility += memo[(nextRow, nextCol, currentMoveCount + 1)]
            else:  # currentMoveCount == K, this is the last move
                possibility = currentPossibility
        return possibility

# # https://tinyurl.com/y987zy5g
# class Solution:
#     def knightProbability(self, N, K, r, c):
#         memo = {}
#         moves = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
#         def dfs(k, x, y, P):
#             p = 0
#             if 0 <= x < N and 0 <= y < N: #a valid position on the board
#                 if k < K:
#                     for dx, dy in moves:
#                         x_next, y_next = x + dx, y + dy
#                         if (x_next, y_next, k+1) not in memo:
#                             memo[(x_next, y_next, k+1)] = dfs(k+1, x_next, y_next, P/8)
#                         p += memo[(x_next, y_next, k+1)]
#                 else: # k==K, this is the last move
#                     p = P
#             return p
#         return dfs(0, r, c, 1.0)
