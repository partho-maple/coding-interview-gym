import math
from collections import Counter
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        points = [p1, p2, p3, p4]
        distanceCount = Counter()
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distanceCount[self.distance(points[i], points[j])] += 1

        return len(distanceCount) == 2 and 4 in distanceCount.values() and 2 in distanceCount.values()


    def distance(self, p1, p2):
        val = (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
        return val


