def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    finalWords = {}
    visited = [[False for lettern in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, trie.root, visited, finalWords)
    return list(finalWords.keys())


def explore(i, j, board, trie, visited, finalWords):
    if visited[i][j] == True:
        return
    letter = board[i][j]
    if letter not in trie:
        return
    visited[i][j] = True
    trieNode = trie[letter]
    if "*" in trieNode:
        finalWords[trieNode["*"]] = True
    neighbours = getNeighbours(i, j, board)
    for neighbour in neighbours:
        explore(neighbour[0], neighbour[1], board, trieNode, visited, finalWords)
    visited[i][j] = False


def getNeighbours(i, j, board):
    neighbours = []
    possibleDirections = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for direction in possibleDirections:
        di, dj = direction
        newI, newJ = i + di, j + dj
        if 0 <= newI < len(board) and 0 <= newJ < len(board[0]):
            neighbours.append([newI, newJ])
    return neighbours


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word