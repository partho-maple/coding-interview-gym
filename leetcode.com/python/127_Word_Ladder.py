from collections import defaultdict
from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        wordLen = len(beginWord)
        allComboDict = defaultdict(list)
        for word in wordList:
            for i in range(wordLen):
                allComboDict[word[:i] + "*" + word[i + 1:]].append(
                    word)  # Creating the adjacency list of . the intermediate nodes/words. Every Node has 3 intermediate nodes
        queue = deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            currentWord, level = queue.popleft()  # Here the words are the nodes
            for i in range(wordLen):
                intermediateWord = currentWord[:i] + "*" + currentWord[
                                                           i + 1:]  # here the words are the . intermediate nodes. Every Node has 3 intermediate nodes. And here, the nodes doesn't have the adjacency list. The intermediate node has it.
                for word in allComboDict[intermediateWord]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))

                allComboDict[intermediateWord] = []
        return 0


# Using BFS. My own solution during Mock Test
import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        wordLen = len(beginWord)
        patterToWordMap = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(wordLen):
                pattern = word[:i] + "*" + word[i + 1:]
                patterToWordMap[pattern].append(word)

        graph = defaultdict(list)
        for word in wordList:
            for i in range(wordLen):
                pattern = word[:i] + "*" + word[i + 1:]
                nodeList = patterToWordMap[pattern]
                graph[word].extend(nodeList)

        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while queue:
            currentLevelSize = len(queue)
            while currentLevelSize > 0:
                currentWord, level = queue.popleft()
                currentLevelSize -= 1
                for neighbours in graph[currentWord]:
                    if neighbours == endWord:
                        return level + 1
                    else:
                        if neighbours not in visited:
                            visited.add(neighbours)
                            queue.append((neighbours, level + 1))
        return 0



sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
out = sol.ladderLength(beginWord, endWord, wordList)
print("Res: ", out)