class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        n = len(words)
        L = maxWidth
        currentWordIdx = 0           # the index of the current word
        ans = []
        while currentWordIdx < n:
            wordCountForEachLine = self.getWordsCountForEachLine(currentWordIdx, words, maxWidth)
            line = self.insertSpaces(currentWordIdx, wordCountForEachLine, words, maxWidth)  # create a line which contains words from words[currentWordIdx] to words[currentWordIdx + wordCountForEachLine - 1]
            ans.append(line)
            currentWordIdx += wordCountForEachLine
        return ans


    # How many words we need to form each line;
    def getWordsCountForEachLine(self, currentWordIdx, words, maxWidth):
        wordCountForLine = 1       # figure out how many words can fit into a line, which starts from 1 ssince we are adding  one word initially
        currentLen = len(words[currentWordIdx])
        while currentWordIdx + wordCountForLine < len(words):
            nextLen = len(words[currentWordIdx + wordCountForLine]) + 1 # here, the last added 1 is for an added space at the left
            if currentLen + nextLen <= maxWidth:
                wordCountForLine += 1
                currentLen += nextLen
            else:
                break
        return wordCountForLine



    # How many spaces we should insert between two words.
    def insertSpaces(self, currentWordIdx, wordCountForEachLine, words, maxWidth):
        initialLine = ' '.join(words[currentWordIdx:currentWordIdx + wordCountForEachLine])     # Concatenate words[currentWordIdx:currentWordIdx + wordCountForEachLine] into one line
        finalLine = ""
        if wordCountForEachLine == 1 or currentWordIdx + wordCountForEachLine == len(words):    # if the line contains only one word or it is the last line
            spaces = maxWidth - len(initialLine)                                                # we just need to left assigned it
            finalLine = initialLine + ' '*spaces
        else:
            totalSpaces = maxWidth - len(initialLine) + (wordCountForEachLine - 1)              # total number of spaces we need insert
            averageSpaces = totalSpaces // (wordCountForEachLine - 1)                                  # average number of spaces we should insert between two words
            leftWords = totalSpaces % (wordCountForEachLine - 1)                           # number of 'left' words, i.e. words that have 1 more space than the other words on the right side
            if leftWords > 0:
                finalLine = (" "*(averageSpaces + 1)).join(words[currentWordIdx:currentWordIdx + leftWords])    # left words. The reason for +1 is, these words will have one more spaces then others
                finalLine += " "*(averageSpaces + 1)                                        # spaces between left words & right words
                finalLine += (" "*averageSpaces).join(words[currentWordIdx + leftWords:currentWordIdx + wordCountForEachLine])      # right woreds
            else:
                finalLine = (" "*averageSpaces).join(words[currentWordIdx:currentWordIdx + wordCountForEachLine])
        return finalLine

