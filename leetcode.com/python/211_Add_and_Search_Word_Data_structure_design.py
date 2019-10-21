# Ref: https://leetcode.com/problems/add-and-search-word-data-structure-design/discuss/59725/Python-easy-to-follow-solution-using-Trie.

import collections


class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        currentNode = self.root
        for character in word:
            if character not in currentNode.children:
                currentNode.children[character] = TrieNode()
            currentNode = currentNode.children[character]
        currentNode.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        currentNode = self.root
        self.result = False
        self.dfs(currentNode, word)
        return self.result

    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.result = True
            return
        if word[0] == ".":
            for childNode in node.children.values():
                self.dfs(childNode, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)