from collections import defaultdict
from heapq import heappop, heapify

# Source: https://tinyurl.com/tp46c6s
class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        l = len(hand)
        if l % W:
            return False
        if W == 1:
            return True
        counter = defaultdict(int)
        for i in hand:
            counter[i] += 1
        heapify(hand)
        for i in range(l // W):
            start = heappop(hand)
            while counter[start] == 0:
                start = heappop(hand)
            for i in range(W):
                counter[start] -= 1
                if counter[start] < 0:
                    return False
                start += 1
        return True