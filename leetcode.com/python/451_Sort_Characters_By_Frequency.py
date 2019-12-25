from collections import Counter
import heapq

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        charFrequencyCounter = Counter(s)       # find the frequency of each character
        maxHeap = []
        for char, frequency in charFrequencyCounter.items():     # add all characters to the max heap
            heapq.heappush(maxHeap, (-frequency, char))

        sortedString = []
        while maxHeap:                      # build a string, appending the most occurring characters first
            frequency, char = heapq.heappop(maxHeap)
            for _ in range(-frequency):
                sortedString.append(char)

        return "".join(sortedString)

