from collections import Counter
import heapq


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        wordFrequencyMap = Counter(words)

        maxHeap = []
        for word, frequency in wordFrequencyMap.items():
            heapq.heappush(maxHeap, (-frequency, word))

        wordList = []
        while k > 0:
            frequency, word = heapq.heappop(maxHeap)
            wordList.append(word)
            k -= 1

        return wordList

