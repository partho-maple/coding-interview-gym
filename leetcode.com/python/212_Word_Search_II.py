# Getting "Maximum recursion depth exceeded. WHy the fuck?  Did't wunderstand why
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
        self.fullWord = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWords(self, words):
        for word in words:
            currentNode = self.root
            for char in word:
                if not currentNode.children[char]:
                    currentNode.children[char] = TrieNode()
                currentNode = currentNode.children[char]
            currentNode.isWord = True
            currentNode.fullWord = word

    def searchWord(self, word):
        cirrentWord = self.root
        for char in word:
            if not cirrentWord.children[char]:
                return False
            cirrentWord = cirrentWord.children[char]
        return True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        allWord = []
        trie = Trie()
        trie.addWords(words)
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.searchBoardDFS(board, row, col, trie.root, allWord)
        return allWord

    def searchBoardDFS(self, board, row, col, currentNode, allWord):
        if currentNode.isWord:
            allWord.append(currentNode.fullWord)
            currentNode.isWord = False # to prevent from adding duplicate word

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return

        currentChar = board[row][col]
        currentNode = currentNode.children[currentChar]

        if not currentNode: # currentChar doesn't exist
            return

        board[row][col] = "#" # to prevent going into loop and revisiting
        self.searchBoardDFS(board, row+1, col, currentNode, allWord)
        self.searchBoardDFS(board, row-1, col, currentNode, allWord)
        self.searchBoardDFS(board, row, col+1, currentNode, allWord)
        self.searchBoardDFS(board, row, col-1, currentNode, allWord)
        board[row][col] = currentChar  # Backtrack




# https://tinyurl.com/y7td7eag
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord


class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, node, i + 1, j, path + tmp, res)
        self.dfs(board, node, i - 1, j, path + tmp, res)
        self.dfs(board, node, i, j - 1, path + tmp, res)
        self.dfs(board, node, i, j + 1, path + tmp, res)
        board[i][j] = tmp