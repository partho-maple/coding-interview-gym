# # Using Trie and DFS
# from collections import defaultdict
# class TrieNode:
#     def __init__(self):
#         self.children = defaultdict(TrieNode)
#         self.isWord = False
#         self.finalWord = None

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def addWord(self, word):
#         currentNode = self.root
#         for char in word:
#             if char not in currentNode.children:
#                 currentNode.children[char] = TrieNode()
#             currentNode = currentNode.children[char]
#         currentNode.isWord = True
#         currentNode.finalWord = word


# class Solution(object):
#     def findAllConcatenatedWordsInADict(self, words):
#         """
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         if not words or len(words) <= 0:
#             return []

#         trie = Trie()
#         for word in words:
#             trie.addWord(word)

#         result = []
#         for word in words:
#             if self.isConcatenated(trie.root, word, 0, 0):
#                 result.append(word)

#         return result

#     # DFS method to check word concatination
#     # Return true if word starting from index is concatenated
#     def isConcatenated(self, trieRoot, word, startIdx, concatWordCnt):
#         if startIdx == len(word):
#             return concatWordCnt >= 2

#         for i in range(startIdx, len(word)):
#             char = word[i]
#             if char not in trieRoot.children:
#                 return False
#             trieRoot = trieRoot.children[char]
#             if trieRoot.isWord:
#                 # if trieRoot.finalWord != word:
#                 if self.isConcatenated(trieRoot, word, i + 1, concatWordCnt + 1):
#                     return True
#                 # else:
#                 #     return concatWordCnt > 1
#         return False


# Using only DFS
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d = set(words)

        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix):
                    return True
                if suffix in d and dfs(prefix):
                    return True

            return False

        res = []
        for word in words:
            if dfs(word):
                res.append(word)

        return res






