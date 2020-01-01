# from collections import defaultdict
# from collections import deque
#
# class Solution(object):
#     def findLadders(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: List[List[str]]
#         """
#         if endWord not in wordList or not endWord or not beginWord or not wordList:
#             return 0
#         wordLen = len(beginWord)
#         allComboDict = defaultdict(list)
#         for word in wordList:
#             for i in range(wordLen):
#                 allComboDict[word[:i] + "*" + word[i + 1:]].append(
#                     word)  # Creating the adjacency list of . the intermediate nodes/words. Every Node has 3 intermediate nodes
#         queue = deque([beginWord])
#         allSequence, currentSequence = [], []
#         visited = {beginWord: True}
#         while queue:
#             currentWord = queue.popleft()  # Here the words are the nodes
#             currentSequence.append(currentWord)
#             for i in range(wordLen):
#                 intermediateWord = currentWord[:i] + "*" + currentWord[i + 1:]  # here the words are the . intermediate nodes. Every Node has 3 intermediate nodes. And here, the nodes doesn't have the adjacency list. The intermediate node has it.
#                 for word in allComboDict[intermediateWord]:
#                     if word == endWord:
#                         if allSequence and len(currentSequence) > len(allSequence[-1]):
#                             allSequence.pop()
#                         currentSequence.append(word)
#                         allSequence.append(list(currentSequence))
#                         currentSequence.pop()
#                         break
#                     if word not in visited:
#                         visited[word] = True
#                         queue.append(word)
#
#                 allComboDict[intermediateWord] = []
#
#         return allSequence
#
#
# sol = Solution()
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# out = sol.findLadders(beginWord, endWord, wordList)
# print("Res: ", out)