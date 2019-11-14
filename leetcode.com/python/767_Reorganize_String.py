from collections import Counter
import heapq

class Solution(object):

    # # Using Heap/PriorityQueue. Original code from here: https://tinyurl.com/u6h7nmd
    # # Also this  explanation: https://leetcode.com/problems/reorganize-string/discuss/113457/Simple-python-solution-using-PriorityQueue/194973
    # def reorganizeString(self, S):
    #     """
    #     :type S: str
    #     :rtype: str
    #     """
    #     result = ""
    #     priorityQueue = []
    #     charFrequencies = Counter(S)
    #     for key, value in charFrequencies.items():
    #         heapq.heappush(priorityQueue, (-value, key))
    #     prevNodeValue, prevNodeKey = 0, ''
    #     while priorityQueue:
    #         currentNodeValue, currentNodeKey = heapq.heappop(priorityQueue)
    #         result += currentNodeKey
    #         if prevNodeValue < 0:
    #             heapq.heappush(priorityQueue, (prevNodeValue, prevNodeKey))
    #         currentNodeValue += 1
    #         prevNodeValue, prevNodeKey = currentNodeValue, currentNodeKey
    #     return "" if len(result) != len(S) else result


    # Greedy solution. Original code from here: https://tinyurl.com/rnsr4gp
    def reorganizeString(self, S):
        a = sorted(sorted(S), key=S.count)
        h = len(a) // 2
        a[1::2], a[::2] = a[:h], a[h:]
        return ''.join(a) if (a[-1:] != a[-2:-1]) else ""  # same as >> return ''.join(a) * (a[-1:] != a[-2:-1])






sol = Solution()
S = "aaab"
out = sol.reorganizeString(S)
print("Res: ", out)