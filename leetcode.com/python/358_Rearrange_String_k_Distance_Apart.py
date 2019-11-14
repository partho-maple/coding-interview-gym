from collections import Counter
import heapq

class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return s
        result, priorityQueue = "", []
        charFrequencies = Counter(s)
        for key, value in charFrequencies.items():
            heapq.heappush(priorityQueue, (-value, key))
        while priorityQueue:
            tempCharHolder, currentDistance = [], 0
            while currentDistance < k:
                if priorityQueue:
                    currentDistance += 1
                    currentCharFrequency, currentChar = heapq.heappop(priorityQueue)
                    result += currentChar
                    if currentCharFrequency != -1:
                        tempCharHolder.append((currentCharFrequency + 1, currentChar))
                else:
                    if tempCharHolder:
                        return ""
                    else:
                        return result
            for item in tempCharHolder:
                heapq.heappush(priorityQueue, item)
        return result




sol = Solution()
# s = "aabbcc"
# k = 3
s = "aa"
k = 2
out = sol.rearrangeString(s, k)
print("res: ", out)
