from collections import Counter
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        counter = Counter(S)
        windowChrSet = set()
        left, right = 0, 0
        partLabels = []
        while left <= right and right < len(S):
            rightChr = S[right]
            windowChrSet.add(rightChr)
            counter[rightChr] -= 1

            if counter[rightChr] == 0:
                del counter[rightChr]
                windowChrSet.discard(rightChr)

            if len(windowChrSet) <= 0:
                partLabels.append(right - left + 1)
                left = right + 1
            right += 1
        return partLabels
