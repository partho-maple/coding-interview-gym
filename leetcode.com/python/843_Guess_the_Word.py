# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

# https://tinyurl.com/wqy5ll4
from collections import Counter
import itertools
class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        matchCount = 0
        while matchCount < 6:
            count = Counter()
            for word1, word2 in itertools.permutations(wordlist, 2):
                if self.match(word1, word2) == 0:
                    count[word1] += 1
            gussedWord = min(wordlist, key=lambda word: count[word])    # get the word that has minimum count of 0 in the word Counter
            matchCount = master.guess(gussedWord)
            newWordList = []
            for word in wordlist:
                if self.match(word, gussedWord) == matchCount:
                    newWordList.append(word)
            wordlist = newWordList


    def match(self, word1, word2):
        matches = []
        for c1, c2 in zip(word1, word2):
            if c1 == c2:
                matches.append(1)
            else:
                matches.append(0)
        return sum(matches)

