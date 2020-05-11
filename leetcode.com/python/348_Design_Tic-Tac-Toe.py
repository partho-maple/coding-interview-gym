class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows, self.cols, self.diagonal, self.antiDiagonal, self.n = [0]*n, [0]*n, 0, 0, n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        offset = (player * 2) - 3 # To identify players moves uniquely. Lets say for players 1&2 -> "offset = player * 2 - 3" will results -1,1 respectively.
        self.rows[row] += offset
        self.cols[col] += offset
        if row == col:
            self.diagonal += offset
        if row + col == self.n - 1:
            self.antiDiagonal += offset
        if self.n in [self.rows[row], self.cols[col], self.diagonal, self.antiDiagonal]:
            return 2
        if -self.n in [self.rows[row], self.cols[col], self.diagonal, self.antiDiagonal]:
            return 1
        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)