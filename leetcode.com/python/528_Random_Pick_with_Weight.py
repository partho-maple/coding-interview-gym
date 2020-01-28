import bisect
import random
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefisSum = w
        for i in range(1, len(self.prefisSum)):
            self.prefisSum[i] = self.prefisSum[i] + self.prefisSum[i - 1]


    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.randint(1, self.prefisSum[-1])
        return bisect.bisect_left(self.prefisSum, target)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()