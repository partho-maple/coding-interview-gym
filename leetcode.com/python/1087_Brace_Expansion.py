class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        wordList = []
        allGeneratedWords = []
        self.getWordList(S, wordList)
        self.generateWords(wordList, "", allGeneratedWords)
        return sorted(allGeneratedWords)

    def generateWords(self, wordList, runningWord, allGeneratedWords):
        if not wordList:
            allGeneratedWords.append(runningWord)
            return
        word = wordList[0]
        for j in range(len(word)):
            char = word[j]
            runningWord += char
            self.generateWords(wordList[1:], runningWord, allGeneratedWords)
            runningWord = runningWord[:len(runningWord) - 1]

    def getWordList(self, S, wordList):
        start = S.find('{')
        end = S.find('}')
        if start >= 0:
            if start > 0:
                wordList.append(S[0:start].split(','))
            wordList.append(S[start + 1:end].split(','))
            self.getWordList(S[end+1:], wordList)
        else:
            if S:
                wordList.append(S.split(','))
            return





sol = Solution()
input = "{a,b}{z,x,y}"
output  = sol.expand(input)
print('Res: ', output)