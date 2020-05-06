# Using BFS. My own solution during Mock Test
# https://tinyurl.com/y89mjm4c
from collections import defaultdict
from collections import deque


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return []

        wordLen = len(beginWord)
        letterToWordMap = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(wordLen):
                pattern = word[:i] + "*" + word[i + 1:]
                letterToWordMap[pattern].append(word)

        graph = defaultdict(list)
        for word in wordList:
            for i in range(wordLen):
                pattern = word[:i] + "*" + word[i + 1:]
                nodeList = letterToWordMap[pattern]
                graph[word].extend(nodeList)

        queue = deque([(beginWord, 1)])
        wordSet = set(wordList)
        pathTree = defaultdict(set)
        isFound = False
        while queue and not isFound:
            currentLevelSize = len(queue)
            for i in range(currentLevelSize):
                currentWord, level = queue[i]
                wordSet.discard(currentWord)  # subtract words in current level so that they won't be used again.

            while currentLevelSize > 0:  # for each word in current level
                currentWord, level = queue.popleft()
                currentLevelSize -= 1
                for neighbour in graph[currentWord]:  # for each word with one-diff
                    if neighbour in wordSet:  # only care those in words set
                        if neighbour == endWord:  # if found (reach the shortest solution level), we won't do next level.
                            isFound = True
                        else:
                            queue.append((neighbour, level + 1))  # prepare next queue
                        pathTree[currentWord].add(neighbour)  # add trace

        return self.buildSequence(pathTree, beginWord, endWord)

    def buildSequence(self, pathTree, beginWOrd, endWord):  # backtracking (DFS) for solution
        if beginWOrd == endWord:
            return [[beginWOrd]]
        else:
            return [[beginWOrd] + rest for y in pathTree[beginWOrd] for rest in
                    self.buildSequence(pathTree, y, endWord)]