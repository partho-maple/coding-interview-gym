import bisect
from collections import Counter
class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        wordFrequecBySmallest = []
        for word in words:
            wordFrequecBySmallest.append(self.getFrequecBySmallest(word))
        wordFrequecBySmallest.sort()
        answer = []
        for querie in queries:
            smallentInQuery = self.getFrequecBySmallest(querie)
            insertionPoint = bisect.bisect_left(wordFrequecBySmallest, smallentInQuery)
            wordCount = len(wordFrequecBySmallest) - insertionPoint
            answer.append(wordCount)
        return answer


    def getFrequecBySmallest(self, word):
        if not word:
            return 0
        counter = Counter(word)
        keys = sorted(counter.keys())
        return counter[keys[0]]


