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
                allComboDict[word[:i] + "*" + word[i + 1:]].append(word)
        queue = deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            currentWord, level = queue.popleft()
            for i in range(wordLen):
                intermediateWord = currentWord[:i] + "*" + currentWord[i + 1:]
                for word in allComboDict[intermediateWord]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))

                allComboDict[intermediateWord] = []
        return 0


sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
out = sol.ladderLength(beginWord, endWord, wordList)
print("Res: ", out)