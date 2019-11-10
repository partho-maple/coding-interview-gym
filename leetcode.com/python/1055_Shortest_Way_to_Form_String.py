from collections import defaultdict
import bisect

class Solution(object):

    # # Greedy solution using two pointer. time O(M*N)
    # def shortestWay(self, source, target):
    #     """
    #     :type source: str
    #     :type target: str
    #     :rtype: int
    #     """
    #     targetIdx, subsequencesCount = 0, 0
    #     while targetIdx < len(target):
    #         sourceIdx = 0
    #         subsequencesExists = False
    #         while sourceIdx < len(source) and targetIdx < len(target):
    #             if source[sourceIdx] == target[targetIdx]:
    #                 sourceIdx += 1
    #                 targetIdx += 1
    #                 subsequencesExists = True
    #             else:
    #                 sourceIdx += 1
    #         subsequencesCount += 1
    #         if not subsequencesExists:
    #             return -1
    #     return subsequencesCount
    #
    #
    #
    #
    # # DP approach using two pointer. time O(M*N)
    # def shortestWay(self, source, target):
    #     """
    #     :type source: str
    #     :type target: str
    #     :rtype: int
    #     """
    #     cache = [float('inf')] * (len(target) + 1)
    #     cache[0] = 0
    #     for cacheIdx in range(1, len(target) + 1):
    #         sourceIdx, targetIdx = len(source) - 1, cacheIdx - 1
    #         while sourceIdx >= 0 and targetIdx >= 0:
    #             if source[sourceIdx] == target[targetIdx]:
    #                 if cache[targetIdx] != float('inf'):
    #                     cache[cacheIdx] = min(cache[cacheIdx], cache[targetIdx] + 1)
    #                 targetIdx -= 1
    #             sourceIdx -= 1
    #     return -1 if cache[-1] == float('inf') else cache[-1]



    # Binary Search approach. time O(M*logN)  -  https://tinyurl.com/t6xap4c
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        sourceCharIndices = defaultdict(list)
        for idx, char in enumerate(source):
            sourceCharIndices[char].append(idx)
        sourceIdx, subsequencesCount = -1, 0
        for char in target:
            if char not in sourceCharIndices:
                return -1
            offsetListForChar = sourceCharIndices[char]
            j = bisect.bisect_left(offsetListForChar, sourceIdx)          # index in sourceCharIndices[char] that is >= sourceIdx
            if j == len(offsetListForChar):
                subsequencesCount += 1
                sourceIdx = offsetListForChar[0] + 1
            else:
                sourceIdx = offsetListForChar[j] + 1
        return subsequencesCount








sol = Solution()
source = "abcab"
target = "aabbaac"
out = sol.shortestWay(source, target)
print('Res: ', out)
