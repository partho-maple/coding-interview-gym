class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                result = self.searchWord(board, word, row, col)
                if result:
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def searchWord(self, origialBoard, originalWord, row, col):
        if len(originalWord) == 0:  # all the characters are checked
            return True
        if row < 0 or row >= len(origialBoard) or col < 0 or col >= len(origialBoard[0]) or origialBoard[row][col] != originalWord[0]:
            return False
        choice = origialBoard[row][col]
        print("choice: " + choice + ", row: " + str(row) + ", col: " + str(col))
        origialBoard[row][col] = "#"  # first character is found, check the remaining part. And this choice is to avoid to visit the same node agian
        result = self.searchWord(origialBoard, originalWord[1:], row + 1, col) or self.searchWord(origialBoard, originalWord[1:], row - 1, col) or self.searchWord(origialBoard, originalWord[1:], row, col + 1)or self.searchWord(origialBoard, originalWord[1:], row, col - 1)
        origialBoard[row][col] = choice # repairing the origialBoard if the previous recursion call stack returns false.
        return result





sol = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
output = sol.exist(board, word)
print('Result: ',  output)


